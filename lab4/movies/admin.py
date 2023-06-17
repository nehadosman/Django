from django.contrib import admin


from movies.models import Category, Cast, Movie


admin.site.register(Category)
admin.site.register(Cast)
admin.site.register(Movie)

