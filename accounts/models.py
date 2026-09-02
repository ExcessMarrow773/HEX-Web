from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import validators
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUsernameValidator(UnicodeUsernameValidator):
	regex = r'^[\w+-]+$'  # Modify this regex to allow/disallow characters
	message = _(
		'Enter a valid username. This value may contain only letters, '
		'numbers, and ./-/_ characters.'
	)

class Profile(models.Model):
	small_profile_pic = models.ImageField(_("Profile Picture"), upload_to="profilePics", default="static/img/pfpDefault.png", blank=True)
	headshot = models.ImageField(_("Headshot"), upload_to="headshots", blank=True)

	description = models.TextField(_("Description"), blank=True, max_length=255)
	job_title = models.CharField(_("Job Title"), max_length=50, blank=True)

	def __str__(self) -> str:
		return


class CustomUser(AbstractUser):
	username_validator = CustomUsernameValidator()

	email = models.EmailField(_("email address"))
	first_name = models.CharField(_("first name"), max_length=150)
	last_name = models.CharField(_("last name"), max_length=150)
	
	goes_on_staff_page = models.BooleanField(_("Goes on staff page?"), default=False)

	profile = models.ForeignKey(Profile, on_delete=models.RESTRICT)

	username = models.CharField(
		max_length=32,
		unique=True,
		validators=[username_validator],
		help_text=_(
			'Required. 150 characters or fewer. Letters, digits and +/-/_ only.'
		),
	)

	def __str__(self):
		return self.username

	def __int__(self):
		return self.id

