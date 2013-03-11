#!/usr/bin/env python2
import os
import datetime
from requests import get
from lxml.etree import fromstring
from dumptruck import DumpTruck

FLICKR_REST = 'http://api.flickr.com/services/rest/'
GROUPS = ['40371529@N00']

def p(**special_params):
    result = {
        'method': 'flickr.groups.pools.getPhotos',
        'api_key': os.environ['FLICKR_KEY'],
        'per_page': 100,
        'extras': 'description,url_l,longitude,latitude',
    }
    result.update(special_params)
    return result

def download(group_id, page):
    '''
    Return a page of the photo pool for a group.
    Find the `group_id` here: http://idgettr.com.
    The `page` is a natural number.
    '''
    r = get(FLICKR_REST, params = p(group_id = group_id, page = page))
    if r.status_code != 200:
        print r.text
        raise ValueError(r.status_code)

    return r.text

def parse(text):
    rsp = fromstring(text.encode('utf-8'))

    # Check for errors.
    stat = rsp.xpath('@stat')[0]
    if stat != 'ok':
        raise ValueError(stat)

    page = int(rsp.xpath('//photos/@page')[0])
    photos = []
    for i, photo in enumerate(rsp.xpath('//photo')):
        descriptions = photo.xpath('description')
        description_text = descriptions[0].xpath('string()') if len(descriptions) == 1 else ''

        photo_data = {
            'page': page,
            'within_page': i + 1,
            'id': photo.xpath('@id')[0],
            'owner': photo.xpath('@owner')[0],
            'title': photo.xpath('@title')[0],
            'dateadded': datetime.datetime.fromtimestamp(int(photo.xpath('@dateadded')[0])),

            'description': description_text,
        }

        datetakens = photo.xpath('@datetaken')
        if len(datetakens) == 1:
            photo_data['datetaken'] = datetime.datetime.strptime(datetakens[0], "%Y-%m-%d %H:%M:%S"),

        dateuploadeds = photo.xpath('@dateuploaded')
        if len(dateuploadeds) == 1:
            photo_data['dateuploaded'] = datetime.datetime.fromtimestamp(int(dateuploadeds[0])),

        photo_data['url_sq'] = photo.attrib.get('url_sq', '')
        photo_data['url_l'] = photo.attrib.get('url_l', '')
        photo_data['longitude'] = float(photo.attrib.get('longitude', 0))
        photo_data['latitude'] = float(photo.attrib.get('latitude', 0))

        for key in ['longitude', 'latitude']:
            if photo_data[key] == 0.0:
                del(photo_data[key])

        photos.append(photo_data)

    return photos

def group(dt, group_id, verbose = False):
    'Download a group.'
    n_pages = 1
    n_page = 1
    while n_page <= n_pages:

        # Acquire
        text = download(group_id, n_page)
        data = parse(text)
        for row in data:
            row['group_id'] = group_id

        # Save
        dt.insert(data, 'photo')

        # Continue
        photos = fromstring(text.encode('utf-8')).xpath('//photos')[0]
        n_page = int(photos.xpath('@page')[0])
        n_pages = int(photos.xpath('@pages')[0])
        if verbose:
            print('Downloaded page %d of %d' % (n_page, n_pages))
        n_page += 1


def main():
    dt = DumpTruck(dbname = 'aurora.db', adapt_and_convert = True)
    for group_id in GROUPS:
        group(dt, group_id, verbose = True)

if __name__ == '__main__':
    main()
