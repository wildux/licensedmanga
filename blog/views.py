from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Post, Category, Author, Publisher, Serie, Volume, Announcement, Genre, Demography
from django.views.generic import ListView


'''
BLOG
'''

def list_posts(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #PAGINATION
	return render(request, 'blog/list_posts.html', {'posts': posts})

def list_posts_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render(request, 'blog/view_category.html', {
		'category': category,
		'posts': Post.objects.filter(categories=category)[:5] #PAGINATION
	})

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/view_post.html', {'post': post})


'''
SERIES
'''

def list_series(request, demography='all'):
	if demography == 'all':
		series = Serie.objects.order_by('title')
		return render(request, 'blog/list_series.html', {'series': series})
	else:
		demography = get_object_or_404(Demography, slug=demography)
		return render(request, 'blog/list_series.html', {
			'demography': demography,
			'series': Serie.objects.filter(demographies=demography).order_by('title')
		})

def list_series_genre(request, genre):
	genre = get_object_or_404(Genre, slug=genre)
	return render(request, 'blog/list_series.html', {
		'genre': genre,
		'series': Serie.objects.filter(genres=genre).order_by('title')
	})


def view_serie(request, slug):
	serie = get_object_or_404(Serie, slug=slug)
	volumes = Volume.objects.filter(serie=serie)
	return render(request, 'blog/view_serie.html', {
		'serie': serie,
		'volumes': volumes
	})


'''
PUBLISHERS
'''

def list_publishers(request, origin='all', state='all'): #all = eng+original (state GET ?)
	publishers = Publisher.objects.order_by('name')
	return render(request, 'blog/list_publishers.html', {'publishers': publishers})

def view_publisher(request, slug, demography='all'):
	publisher = get_object_or_404(Publisher, slug=slug)
	if demography == 'all':
		return render(request, 'blog/view_publisher.html', {
			'publisher': publisher,
			'demography': demography,
			'demographies': Demography.objects.all(),
			'series': Serie.objects.order_by('title')
		})
	else:
		demography = get_object_or_404(Demography, slug=demography)
		return render(request, 'blog/view_publisher.html', {
			'publisher': publisher,
			'demography': demography,
			'demographies': Demography.objects.all(),
			'series': Serie.objects.filter(demographies=demography).order_by('title')
		})


'''
AUTHORS
'''

def list_authors(request):
	authors = Author.objects.order_by('name')
	return render(request, 'blog/list_authors.html', {'authors': authors})

def view_author(request, slug, demography='all'):
	author = get_object_or_404(Author, slug=slug)
	if demography == 'all':
		return render(request, 'blog/view_author.html', {
			'author': author,
			'demography': demography,
			'demographies': Demography.objects.all(),
			'series': Serie.objects.order_by('title')
		})
	else:
		demography = get_object_or_404(Demography, slug=demography)
		return render(request, 'blog/view_author.html', {
			'author': author,
			'demography': demography,
			'demographies': Demography.objects.all(),
			'series': Serie.objects.filter(demographies=demography).order_by('title')
		})


'''
VOLUMES (CALENDAR)
'''

def list_volumes(request, month='', year=''):
	if not(month.isdigit() and year.isdigit() and int(month) <= 12):
		month = timezone.now().month
		year = timezone.now().year
	volumes = Volume.objects.filter(release__month=month,release__year=year).order_by('release')
	return render(request, 'blog/list_volumes.html', {
		'volumes': volumes,
		'year': int(year),
		'month': int(month)
	})


'''
ANNOUNCEMENTS
'''

def list_announcements(request, year=timezone.now().year):
	announcements = Announcement.objects.filter(a_date__year=year).order_by('a_date') #
	return render(request, 'blog/list_announcements.html', {
		'announcements': announcements,
		'year': year
	})


'''
LINKS
'''

def list_links(request):
	return render(request, 'blog/links.html')


'''
DEMOGRAPHY MENU
'''

class DemographyMenu(object):
	def get_context_data(self, **kwargs):
		context = super(DemographyMenu, self).get_context_data(**kwargs)
		context['demographies'] = Demography.objects.all()
		return context


class AuthorsView(DemographyMenu, ListView):
	model = Author
	context_object_name = 'authors'
	template_name = "blog/list_authors.html"
