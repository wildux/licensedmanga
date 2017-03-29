from django.contrib import admin
from .models import Post, Category, Author, Publisher, Serie, Volume, Genre, Demography, Announcement, Price
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class PostAdmin(admin.ModelAdmin):
	exclude = ['published_date']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class PublisherAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class GenreAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class DemographyAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


class EditLinkToInlineObject(object):
	def edit_link(self, instance):
		url = reverse('admin:%s_%s_change' % (
			instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
		if instance.pk:
			return mark_safe(u'<a href="{u}">Details</a>'.format(u=url))
		else:
			return ''

class PriceInline(admin.TabularInline):
	model = Price
	extra = 1

class VolumeAdmin(admin.ModelAdmin):
	inlines = [PriceInline]

class VolumeInline(admin.TabularInline):
	model = Volume
	extra = 1
	show_change_link = True

class SerieAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	filter_horizontal = ('writers', 'artists', 'genres', 'demographies')
	inlines = [VolumeInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Demography, DemographyAdmin)
admin.site.register(Announcement)
