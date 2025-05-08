from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in)
def my_custom_login_stuff(sender, request, user, **kwargs):
    raise Exception("PRUEBA") 
    print('my_custom_login_stuff() was called.')

