from django.contrib import admin
from .models import MyUser


# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
 #fields = ('first_name', ('last_name', 'username'),'is_active')
 list_display=['username','combine_val','first_name','last_name']
 search_fields = ['first_name', 'username', 'email']
 #actions_on_bottom = True
 date_hierarchy = 'date_joined'

 def combine_val(self,obj):
  return ("%s %s" % (obj.first_name, obj.last_name))

