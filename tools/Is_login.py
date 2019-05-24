from myapp.models import User


def is_login(request):

        user_id = request.session.get('uid')
        if user_id:
            user = User.objects.get(uid=user_id)
        else:
            user = None
        return user