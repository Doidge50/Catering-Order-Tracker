from django.core.exceptions import PermissionDenied
from tracker.models import User


def error_403_if_not_mentioned_student_or_admin(request, user):
    requesting_user = User.objects.get(email=request.user.email)
    if not (request.user == user or requesting_user.is_superuser):
        raise PermissionDenied