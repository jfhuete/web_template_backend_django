from django.contrib import admin
from my_example_app.models import Musician, Album

admin.site.register(Musician, admin.ModelAdmin)
admin.site.register(Album, admin.ModelAdmin)
