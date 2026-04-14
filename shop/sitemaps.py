from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        # Бул жердеги аталыштар сиздин shop/urls.py ичиндеги name'дерге дал келиши керек
        return ['home', 'about', 'price', 'contact', 'reviews']

    def location(self, item):
        return reverse(item)