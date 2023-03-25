from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from catering.settings import DASHBOARD_URL
from tracker.models import User


def guest_user_required(view_func=None, redirect_field_name=None, login_url=DASHBOARD_URL):
    def _is_guest_user(user):
        return user.is_authenticated == False
    custom_decorator = user_passes_test(_is_guest_user, login_url=login_url, redirect_field_name=redirect_field_name)
    return custom_decorator(view_func) if view_func else custom_decorator