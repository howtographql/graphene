# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_user 1'] = {
    'data': {
        'createUser': {
            'email': 'peter@griffin.com',
            'id': 'VXNlcjox',
            'name': 'peter'
        }
    }
}

snapshots['test_login 1'] = {
    'data': {
        'signinUser': {
            'user': {
                'id': 'VXNlcjox'
            }
        }
    }
}
