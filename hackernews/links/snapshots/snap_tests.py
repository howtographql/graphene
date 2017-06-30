# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_link 1'] = {
    'data': {
        'createLink': {
            'description': 'OHO!',
            'id': 'TGluazox',
            'postedBy': {
                'id': 'VXNlcjox'
            },
            'url': 'http://xxx.com'
        }
    }
}

snapshots['test_create_vote 1'] = {
    'data': {
        'createVote': {
            'link': {
                'id': 'TGluazox'
            },
            'user': {
                'id': 'VXNlcjox'
            }
        }
    }
}
