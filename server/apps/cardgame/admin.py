from django.contrib import admin
from .models import User, Game
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'title', 'devtool',)
 
admin.site.register(User)
admin.site.register(Game)