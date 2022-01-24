import graphene
from graphql_jwt.decorators import login_required
from service.account.graphql import types


class AccountQuery(graphene.ObjectType):
    current_user = graphene.Field(types.UserType, required=True)

    @login_required
    def resolve_current_user(root, info):
        return info.context.user
