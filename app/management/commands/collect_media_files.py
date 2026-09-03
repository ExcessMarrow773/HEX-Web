import os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = "Collect all file paths in MEDIA_ROOT"

	def handle(self, *args, **kwargs):
		media_files = set()
		media_root = settings.MEDIA_ROOT


		# Walk through MEDIA_ROOT and collect file paths
		for root, _, files in os.walk(media_root):
			for file in files:
				# Get relative path from MEDIA_ROOT
				rel_path = os.path.relpath(os.path.join(root, file), media_root)
				media_files.add(rel_path)

		# Save to a text file
		with open('media_files.txt', 'w') as f:
			for path in sorted(media_files):
				f.write(f"{path}\n")

		self.stdout.write(f"Saved {len(media_files)} media file paths to media_files.txt")