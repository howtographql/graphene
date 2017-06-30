# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from users.models import User
from .models import Link, Vote
from oauth2_provider.models import get_access_token_model

AccessToken = get_access_token_model()


def create_test_user():
    user = User(username="peter", email="peter@griffin.com")
    user.set_password("1234")
    user.save()
    return user


def test_create_link(snapshot, db, graphql_client):
    user = create_test_user()
    snapshot.assert_match(
        graphql_client.execute(
            '''
    mutation createLink($url: String!, $postedById: ID!, $description: String!) {
        createLink(url: $url ,postedById: $postedById, description: $description) {
            id
            url
            description
            postedBy {
                id
            }
        }
    }
    ''',
            variable_values={
                'url': 'http://xxx.com',
                'postedById': user.id,
                'description': 'OHO!'
            }))
    link = user.links.first()
    assert link
    assert link.posted_by == user


def test_create_vote(snapshot, db, graphql_client):
    user = create_test_user()
    link = Link(
        url='http://xxx.com',
        posted_by=user,
        description=':D', )
    link.save()
    snapshot.assert_match(
        graphql_client.execute(
            '''
    mutation createVote($userId: ID!, $linkId: ID!) {
        createVote(userId: $userId, linkId: $linkId) {
            user {
                id
            }
            link {
                id
            }
        }
    }
    ''',
            variable_values={
                'userId': user.id,
                'linkId': link.id,
            }))

    assert link.votes.count() == 1
