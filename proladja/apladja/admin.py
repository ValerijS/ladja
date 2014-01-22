from django.contrib import admin
from apladja.models import users

admin.site.register(users)

from apladja.models import rooms

admin.site.register(rooms)

from apladja.models import users2
admin.site.register(users2)
from apladja.models import rooms2
admin.site.register(rooms2)
