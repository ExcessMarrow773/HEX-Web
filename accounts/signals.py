from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import CustomUser, Profile


@receiver(pre_save, sender=CustomUser)
def create_profile_for_new_user(sender, instance, **kwargs):
	"""
	Ensure every CustomUser has a Profile attached before it's first saved.

	CustomUser.profile is a required ForeignKey, so this has to run on
	pre_save (before the row is inserted) rather than post_save — by the
	time post_save fires, the row (with a null/missing profile_id) would
	already have failed to insert.

	`not instance.pk` limits this to the initial creation of the user, so
	existing users saved again later (e.g. changing their username) don't
	get a new Profile swapped in.
	"""
	if not instance.pk and not instance.profile_id:
		instance.profile = Profile.objects.create()