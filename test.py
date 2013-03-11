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
        'ownername': 'noomplayboy',
        'dateadded': datetime.datetime.fromtimestamp(1362860132),
    },
    {
        'page': 7, 'within_page': 2,
	    'id': '8541904081',
        'owner': '63130627@N07',
        'title': 'Aurora_Dancing @ Iceland',
        'ownername': 'noomplayboy',
        'dateadded': datetime.datetime.fromtimestamp(1362858321),
    },
    {
        'page': 7, 'within_page': 3,
        'id': '8541845647',
        'owner': '35612079@N08',
        'title': 'View from my house II',
        'ownername': 'Norseman1968',
        'dateadded': datetime.datetime.fromtimestamp(1362856667),
    }
]

n.assert_list_equal(observed_data, expected_data)
