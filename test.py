#!/usr/bin/env python2

import datetime
import nose.tools as n
from run import parse

observed_data = parse(open('test.xml').read())
expected_data = [
    {
        'page': 7, 'within_page': 1,
        'id': '8541981221',
        'owner': '63130627@N07',
        'title': 'Aurora_Coming @^_^@!',
        'dateadded': datetime.datetime.fromtimestamp(1362860132),
  datetaken DATETIME NOT NULL,
  description TEXT NOT NULL,
  url_l TEXT NOT NULL,
  longitude REAL NOT NULL,
  latitude REAL NOT NULL,
    },
    {
        'page': 7, 'within_page': 2,
	    'id': '8541904081',
        'owner': '63130627@N07',
        'title': 'Aurora_Dancing @ Iceland',
        'dateadded': datetime.datetime.fromtimestamp(1362858321),
    },
    {
        'page': 7, 'within_page': 3,
        'id': '8541845647',
        'owner': '35612079@N08',
        'title': 'View from my house II',
        'dateadded': datetime.datetime.fromtimestamp(1362856667),
    }
]

def test_perfect_data_match():
    n.assert_list_equal(observed_data, expected_data)
