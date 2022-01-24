from graphene_django import DjangoObjectType

from service.account.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
