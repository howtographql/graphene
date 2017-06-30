import datetime

import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import authenticate
from django.utils import timezone
from oauth2_provider.models import (get_access_token_model,
                                    get_application_model)
import uuid

Application = get_application_model()
AccessToken = get_access_token_model()

from .models import User as UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel
        # This class will recreate the GraphQL fields
        # from the UserModel
        only_fields = ['id', 'created_at', 'email']
        interfaces = (relay.Node, )

    name = graphene.String(source='username')
    password = graphene.String(source='raw_password')


class AuthProviderEmail(graphene.InputObjectType):
    class Meta:
        name = 'AUTH_PROVIDER_EMAIL'

    email = graphene.String(required=True)
    password = graphene.String(required=True)


class AuthProviderSignupData(graphene.InputObjectType):
    email = AuthProviderEmail()


class SigninPayload(graphene.Mutation):
    class Input:
        email = AuthProviderEmail()

    token = graphene.String()
    user = graphene.Field(User)

    @classmethod
    def mutate(cls, root, input, context, info):
        # In here, context is the request object
        email = input.get('email')
        password = email.get('password')
        email = email.get('email')

        user = authenticate(context, username=email, password=password)
        if not user:
            raise Exception("Username/password doesn't match")

        application = Application.objects.first()
        token = AccessToken.objects.create(
            user=user,
            token=str(uuid.uuid4()),
            application=application,
            expires=timezone.now() + datetime.timedelta(days=1),
            scope="read write")

        return SigninPayload(token=token, user=user)


class CreateUser(graphene.Mutation):
    class Input:
        name = graphene.String(required=True)
        auth_provider = AuthProviderSignupData()

    Output = User

    @classmethod
    def mutate(cls, root, input, context, info):
        username = input.get('name')
        email = input.get('auth_provider', {}).get('email')
        password = email.get('password')
        email = email.get('email')

        user = UserModel(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
