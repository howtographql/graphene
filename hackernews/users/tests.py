# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User
from oauth2_provider.models import get_access_token_model

AccessToken = get_access_token_model()


def test_create_user(snapshot, db, graphql_client):
    snapshot.assert_match(
        graphql_client.execute('''
    mutation createUser {
        createUser(name:"peter", authProvider: {email: {email: "peter@griffin.com", password:"1234"}}) {
            id
            email
            name
        }
    }
    '''))
    user = User.objects.first()
    assert user
    assert user.username == "peter"
    assert user.email == "peter@griffin.com"


def test_login(snapshot, db, graphql_client):
    user = User(username="peter", email="peter@griffin.com")
    user.set_password("1234")
    user.save()
    result = graphql_client.execute('''
    mutation getToken {
        signinUser(email: {email: "peter@griffin.com", password:"1234"}) {
            user {
                id
            }
            token
        }
    }
    ''')
    token = result['data']['signinUser'].pop('token')
    snapshot.assert_match(result)
    access_token = AccessToken.objects.filter(token=token).first()
    assert access_token
    assert access_token.user == user
