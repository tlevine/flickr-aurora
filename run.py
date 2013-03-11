#!/usr/bin/env python2
import os
import datetime
from requests import get
from lxml.etree import fromstring

FLICKR_REST = 'http://api.flickr.com/services/rest/'
GROUPS = ['40371529@N00']

def p(**special_params):
    result = {
        'method': 'flickr.groups.pools.getPhotos',
        'api_key': os.environ['FLICKR_KEY'],
        'per_page': 3, #100,
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
        photos.append({
            'page': page,
            'within_page': i + 1,
            'id': photo.xpath('@id')[0],
            'owner': photo.xpath('@owner')[0],
            'title': photo.xpath('@title')[0],
            'ownername': photo.xpath('@ownername')[0],
            'dateadded': datetime.datetime.fromtimestamp(int(photo.xpath('@dateadded')[0])),
        })

    return photos
