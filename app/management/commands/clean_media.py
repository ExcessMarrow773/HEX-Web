import os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Delete unused media files (not referenced in the database)"

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Preview deletions without actually removing files'
        )

    def handle(self, *args, **options):
        # Reuse the find_unused_files logic here (or import it)
        from find_unused_files import find_unused_files
        unused_files = find_unused_files()

        dry_run = options['dry_run']
        media_root = settings.MEDIA_ROOT
        deleted_count = 0

        for path in unused_files:
            full_path = os.path.join(media_root, path)
            if not os.path.exists(full_path):
                self.stdout.write(self.style.WARNING(f"File not found: {full_path}"))
                continue

            if dry_run:
                self.stdout.write(f"Would delete: {full_path}")
            else:
                os.remove(full_path)
                self.stdout.write(self.style.SUCCESS(f"Deleted: {full_path}"))
                deleted_count += 1
        self.stdout.write(self.style.SUCCESS(f"\nDry run: {dry_run} | Total deleted: {deleted_count}"))