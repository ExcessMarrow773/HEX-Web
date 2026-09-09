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
	small_profile_pic = models.ImageField(_("Profile Picture"), upload_to="profilePics", default="static/image/pfpDefault.png", blank=True)
	headshot = models.ImageField(_("Headshot"), upload_to="headshots", blank=True, default="static/image/headshotDefault.png")

	description = models.TextField(_("Description"), blank=True, max_length=255)
	job_title = models.CharField(_("Job Title"), max_length=50, blank=True)


	def account(self):
		return self.customuser_set.first()
	
	def display_name(self):
		display = f"{self.job_title} ({self.account().first_name} {self.account().last_name})"
		return display


	def __str__(self) -> str:
		# display_name = f"{self.job_title} ({self.account().first_name} {self.account().last_name})"
		return self.display_name()


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

