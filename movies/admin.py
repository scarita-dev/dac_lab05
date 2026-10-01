from django.contrib import admin
from .models import Genre, Person, Movie, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    readonly_fields = ('created_at',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'created_at', 'updated_at')
    list_filter = ('genres', 'release_year')
    search_fields = ('title', 'directors__first_name', 'directors__last_name')
    filter_horizontal = ('genres', 'directors')
    inlines = [RatingInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'score', 'created_at')
    list_filter = ('score', 'created_at')
    search_fields = ('movie__title', 'comment')
    readonly_fields = ('created_at',)