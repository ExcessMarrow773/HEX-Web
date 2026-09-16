# sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"  # Options: always, hourly, daily, weekly, monthly, yearly, never
    priority = 0.8         # Importance scale: 0.0 to 1.0

    def items(self):
        # Return the queryset of items you want in the sitemap
        return Post.objects.all()

    def lastmod(self, obj):
        # Optional: Returns the last modified date of individual items
        return obj.updated_at
