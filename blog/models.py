from django.db import models
from django.utils import timezone
from django.db.models import permalink

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)
	categories = models.ManyToManyField('blog.Category',blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	
	@permalink
	def get_absolute_url(self):
		return ('view_post', None, { 'slug': self.slug })


class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('list_posts_category', None, { 'slug': self.slug })

	class Meta:
		verbose_name_plural = "categories"


class Author(models.Model):
	MALE = 'male'
	FEMALE = 'female'
	COMPANY = 'company'
	OTHER = 'other'
	UNKNOWN = 'unknown'

	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(COMPANY, 'Company'),
		(OTHER, 'Other'),
		(UNKNOWN, 'Unknown'),
	)

	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=UNKNOWN)
	birth_place = models.CharField(max_length=100, blank=True)
	birth_date = models.CharField(max_length=50, blank=True)
	comments = models.TextField(blank=True)

	@permalink
	def get_absolute_url(self):
		return ('view_author', None, { 'slug': self.slug })

	def __str__(self):
		return self.name


class Publisher(models.Model):
	ENGLISH = 'English'
	ORIGINAL = 'Original'

	ORIGIN_CHOICES = (
		(ENGLISH, 'English publisher'),
		(ORIGINAL, 'Original publisher'),
	)

	DEFUNCT = 'Defunct'
	ACTIVE = 'Active'
	UNKNOWN = 'Unknown'

	STATE_CHOICES = (
		(DEFUNCT, 'Defunct'),
		(ACTIVE, 'Active'),
		(UNKNOWN, 'Unknown'),
	)

	name = models.CharField(max_length=60, unique=True)
	slug = models.SlugField(max_length=60, unique=True)
	location = models.CharField(max_length=100, blank=True)
	year = models.PositiveSmallIntegerField(blank=True, null=True)
	website = models.URLField(blank=True)
	origin = models.CharField(max_length=10, choices=ORIGIN_CHOICES, default=ORIGINAL)
	state = models.CharField(max_length=10, choices=STATE_CHOICES, default=UNKNOWN)
	image = models.ImageField(blank=True)
	comments = models.TextField(blank=True)

	@permalink
	def get_absolute_url(self):
		return ('view_publisher', None, { 'slug': self.slug })

	def __str__(self):
		return self.name

	def getBootstrapColor(self):
		if self.state == self.DEFUNCT:
			return "danger"
		elif self.state == self.ACTIVE:
			return "success"
		else:
			return "default"


class Serie(models.Model):
	ONGOING = 'Ongoing'
	COMPLETED = 'Completed'
	DROPPED = 'Dropped'
	ORIG_DROPPED = 'Axed'
	UNKNOWN = 'Unknown'

	ORIG_STATE_CHOICES = (
		(ONGOING, 'Ongoing'),
		(COMPLETED, 'Completed'),
		(DROPPED, 'Dropped'),
		(UNKNOWN, 'Unknown'),
	)

	STATE_CHOICES = (
		(ONGOING, 'Ongoing'),
		(COMPLETED, 'Completed'),
		(DROPPED, 'Dropped'),
		(ORIG_DROPPED, 'Axed (origin)'),
		(UNKNOWN, 'Unknown'),
	)

	HARDCOVER = 'Hardcover'
	PAPERBACK = 'Paperback'
	COMICBOOK = 'Comic-book'
	DIGITAL = 'Digital'

	EDITION_CHOICES = (
		(HARDCOVER, 'Hardcover'),
		(PAPERBACK, 'Paperback'),
		(COMICBOOK, 'Comic-book'),
		(DIGITAL, 'Digital'),
		(UNKNOWN, 'Unknown'),
	)

	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	original_title = models.CharField(max_length=200, blank=True)
	demographies = models.ManyToManyField('blog.Demography', blank=True)
	genres = models.ManyToManyField('blog.Genre', blank=True)
	synopsis = models.TextField(blank=True)
	publisher = models.ForeignKey(
		'blog.Publisher',
		limit_choices_to={'origin': Publisher.ENGLISH},
		related_name="publishers",
		related_query_name="publisher",
		blank=True,
	)
	original_publisher = models.ForeignKey(
		'blog.Publisher',
		limit_choices_to={'origin': Publisher.ORIGINAL},
		related_name="original_publishers",
		related_query_name="original_publisher",
		blank=True,
	)
	artists = models.ManyToManyField(
		'blog.Author',
		blank=True,
		related_name="artists"
	)
	writers = models.ManyToManyField(
		'blog.Author',
		blank=True,
		related_name="writers"
	)
	state = models.CharField(max_length=15, choices=STATE_CHOICES, default=UNKNOWN)
	orig_state = models.CharField(max_length=10, choices=ORIG_STATE_CHOICES, default=UNKNOWN)
	year = models.PositiveSmallIntegerField(blank=True, null=True)
	orig_volumes = models.PositiveSmallIntegerField(blank=True, null=True)
	edition = models.CharField(max_length=10, choices=EDITION_CHOICES, default=UNKNOWN)
	edition_comments = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('view_serie', None, { 'slug': self.slug })

	def getStateColor(self):
		if self.state == self.UNKNOWN:
			return "default"
		elif self.state == self.ONGOING:
			return "success"
		elif self.state == self.COMPLETED:
			return "primary"
		else:
			return "danger"

	def getOriginalStateColor(self):
		if self.orig_state == self.UNKNOWN:
			return "default"
		elif self.orig_state == self.ONGOING:
			return "success"
		elif self.orig_state == self.COMPLETED:
			return "primary"
		else:
			return "danger"

class Volume(models.Model):
	FULL_DATE = 'fd'
	YEAR_MONTH = 'ym'
	YEAR_ONLY = 'yo'
	QUARTER = 'qt'
	UNKNOWN = 'un'

	DATE_CHOICES = (
		(FULL_DATE, 'Full date'),
		(YEAR_MONTH, 'Year and month'),
		(YEAR_ONLY, 'Year only'),
		(QUARTER, 'Quarter'),
		(UNKNOWN, 'Unknown'),
	)

	FIRST = 'f'
	LAST = 'l'
	ONESHOT = 'o'
	NORMAL = 'n'

	VOLUME_CHOICES = (
		(NORMAL, 'Normal volume'),
		(FIRST, 'First volume'),
		(LAST, 'Last volume'),
		(ONESHOT, 'Single volume'),
	)

	serie = models.ForeignKey('blog.Serie')
	num = models.PositiveSmallIntegerField()
	release = models.DateField(blank=True, null=True)
	precision = models.CharField(max_length=2, choices=DATE_CHOICES, default=UNKNOWN)
	options = models.CharField(max_length=1, choices=VOLUME_CHOICES, default=NORMAL)
	image = models.ImageField(blank=True)
	price = models.CharField(max_length=50, blank=True)
	comments = models.CharField(max_length=50, blank=True)

	def __str__(self):
		if self.options == self.ONESHOT:
			return self.serie.title
		return str(self.num) + ' - ' + self.serie.title

'''
class Price(models.Model):
	EURO = '€'
	DOLLAR = '$'
	CAD = 'CAD'
	POUND = '£'
	YEN = '¥'

	CURRENCY_CHOICES = (
		(DOLLAR, '$'),
		(EURO, '€'),
		(CAD, 'CAD'),
		(POUND, '£'),
		(YEN, '¥'),
	)
	volume = models.ForeignKey('blog.Volume')
	num = models.FloatField()
	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=DOLLAR)
'''

class Announcement(models.Model):
	serie = models.OneToOneField('blog.Serie')
	a_date = models.DateField(verbose_name="announcement date")
	image = models.ImageField(blank=True)

	def __str__(self):
		return self.serie.title


class Genre(models.Model):
	title = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(max_length=20, unique=True)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('list_series_genre', None, { 'genre': self.slug })


class Demography(models.Model):
	title = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(max_length=20, unique=True)
	color = models.CharField(max_length=7)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('list_series_demography', None, { 'demography': self.slug })

	class Meta:
		verbose_name_plural = "demographies"
