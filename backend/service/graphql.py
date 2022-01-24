import graphene

from service.account.graphql import queries, mutations


class Query(queries.AccountQuery, graphene.ObjectType):
    pass


class Mutation(mutations.AccountMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
