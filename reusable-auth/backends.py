from models import User

'''
Here, we have created a class that will replace the standard AUTH object that
Django uses to check logins, and we override two of its default methods.
'''


class EmailAuth(object):
    def authenticate(self, email=None, password=None):
        """
        Get an instance of User using the supplied email
        and check its password
        """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Used by the Django authentication system to
        retrieve an instance of User
        """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
