from django.core.management import BaseCommand
from django.apps import apps
from django.db.models import FileField

class Command(BaseCommand):
	help = "Collect all media file paths refrenced in the database"

	def handle(self, *args, **kwargs):
		db_files = set()

		# Iterate over all models and their FileField/ImageField fields
		for model in apps.get_models():
			file_fields = [f for f in model._meta.get_fields() if isinstance(f, FileField)]
			if not file_fields:
				continue

			for field in file_fields:
				paths = model.objects.exclude(**{field.name: ''}).values_list(field.name, flat=True)
				db_files.update(paths)
		with open('db_referenced_files.txt', 'w') as f:
			for path in sorted(db_files):
				f.write(f"{path}\n")

		self.stdout.write(f"Saved {len(db_files)} referenced file paths to db_referenced_files.txt")