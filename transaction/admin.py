from ai_django_core.admin.model_admins.mixins import (
    AdminRequestInFormMixin,
    CommonInfoAdminMixin,
)
from bson import ObjectId
from django.contrib.admin import register
from djongo.admin import ModelAdmin

from account.models import User
from transaction.models import Transaction


@register(Transaction)
class TransactionAdmin(ModelAdmin, CommonInfoAdminMixin, AdminRequestInFormMixin):
    # TODO CT: Saving a related model does not work (I think its because of mongos _id field) See error
    # FAILED SQL: SELECT %(0)s AS "a" FROM "account_user" WHERE "account_user"."_id" = %(1)s LIMIT 1
    # backend_1  | Params: (1, ObjectId('63cefcb729963627345c3082'))

    _mongo_id_fields = ("created_by", "lastmodified_by", "paid_for")

    def get_form(self, request, obj=None, change=False, **kwargs):
        if request.POST:
            # Remember old state
            _mutable = request.POST._mutable

            # Set to mutable
            request.POST._mutable = True

            # Change the values you want
            for mongo_id_field in self._mongo_id_fields:
                field_value = request.POST.get(mongo_id_field, "")

                if field_value == "":
                    continue

                # del request.POST[mongo_id_field]

                # user = User.objects.get(_id=ObjectId(field_value))
                # request.POST[mongo_id_field] = user._id

                request.POST[mongo_id_field] = ObjectId(field_value)
                request.POST[mongo_id_field + "__id"] = ObjectId(field_value)

            # Set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, change=change, **kwargs)
