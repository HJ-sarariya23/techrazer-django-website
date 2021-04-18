from django.contrib import admin
from home.models import Post,Categorie
# Register your models here.

# admin.site.register(Post)
admin.site.register(Categorie)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)