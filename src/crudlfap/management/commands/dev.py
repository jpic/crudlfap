import os
import os.path
import secrets
import string
import sys

import django.dispatch
from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.core.management.commands.runserver import Command
from django.utils.timezone import now

signal = django.dispatch.Signal()


def rnpw(num=28):
    return ''.join(secrets.choice(
        string.ascii_uppercase + string.digits) for _ in range(num))


class Command(Command):
    help = 'Start development environment'

    def handle(self, *args, **options):
        call_command('migrate')
        self.createusers()
        self.runserver(*args, **options)

    def runserver(self, *args, **options):
        try:
            pid = os.fork()
        except OSError:
            sys.exit(1)

        if pid == 0:
            signal.send(sender=self)
        else:
            return super().handle(*args, **options)

    def createusers(self):
        user_model = apps.get_model(settings.AUTH_USER_MODEL)

        def createuser(username, **defaults):
            user, created = user_model.objects.update_or_create(
                username=username,
                defaults=defaults,
            )

            last_login = None
            if user.last_login:
                last_login = now() - user.last_login

            if created or (last_login and last_login.seconds >= 3600):
                password = rnpw()
                user.set_password(password)
                user.save()
                print('Login with {} / {}'.format(username, password))

            return user, created

        createuser('dev', is_staff=True, is_superuser=True)
        createuser('staff', is_staff=True)
        createuser('user')
