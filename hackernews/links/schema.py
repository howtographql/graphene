import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from .models import Link as LinkModel, Vote as VoteModel


class Link(DjangoObjectType):
    class Meta:
        # This class will recreate the GraphQL fields
        # from the LinkModel
        model = LinkModel
        interfaces = (relay.Node, )


class Vote(DjangoObjectType):
    class Meta:
        # This class will recreate the GraphQL fields
        # from the VoteModel
        model = VoteModel
        interfaces = (relay.Node, )


class LinkFilter(graphene.InputObjectType):
    OR = graphene.List(lambda: LinkFilter)
    description_contains = graphene.String(name='description_contains')
    url_contains = graphene.String(name='url_contains')


class LinkOrderBy(graphene.Enum):
    createdAt_ASC = 1
    createdAt_DESC = 2


class LinkQuery(graphene.AbstractType):
    all_links = graphene.List(
        graphene.NonNull(Link),
        filter=LinkFilter(),
        order_by=LinkOrderBy(),
        skip=graphene.Int(default_value=0),
        first=graphene.Int(default_value=10),
        required=True, )

    def resolve_all_links(self, args, context, info):
        order_by = args.get('order_by')
        skip = args.get('skip')
        first = args.get('first')

        assert skip >= 0, "Skip must be >= 0"
        assert first >= 0, "First must be > 0"
        if order_by == LinkOrderBy.createdAt_ASC:
            order_by = '-created_at'
        else:
            order_by = 'created_at'
        return LinkModel.objects.all().order_by(order_by)[skip:first + skip]


class CreateLink(graphene.Mutation):
    class Input:
        description = graphene.String(required=True)
        url = graphene.String(required=True)
        posted_by_id = graphene.ID(required=True)

    Output = Link

    @classmethod
    def mutate(cls, root, input, context, info):
        description = input.get('description')
        url = input.get('url')
        posted_by_id = input.get('posted_by_id')

        link = LinkModel(
            description=description,
            url=url,
            posted_by_id=posted_by_id, )
        link.save()
        return link


class CreateVote(graphene.Mutation):
    class Input:
        link_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    Output = Vote

    @classmethod
    def mutate(cls, root, input, context, info):
        user_id = input.get('user_id')
        link_id = input.get('link_id')

        vote = VoteModel(user_id=user_id, link_id=link_id)
        vote.save()
        return vote
