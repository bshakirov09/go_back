from django.contrib import admin
from explore.models.explore import Tag, Explore, ExploreImage

admin.site.register([Tag,Explore,ExploreImage])