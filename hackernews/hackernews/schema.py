import graphene
from links.schema import LinkQuery, CreateLink, CreateVote
from users.schema import SigninPayload, CreateUser


class Query(LinkQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(graphene.ObjectType):
    signin_user = SigninPayload.Field(required=True)
    create_user = CreateUser.Field()
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
