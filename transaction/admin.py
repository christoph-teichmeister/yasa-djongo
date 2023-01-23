from ai_django_core.admin.model_admins.mixins import (
    AdminRequestInFormMixin,
    CommonInfoAdminMixin,
)
from django.contrib import admin
from django.contrib.admin import register

from transaction.models import Transaction


@register(Transaction)
class TransactionAdmin(admin.ModelAdmin, CommonInfoAdminMixin, AdminRequestInFormMixin):
    pass
