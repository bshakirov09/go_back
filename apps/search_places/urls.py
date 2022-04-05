from django.urls import path

from search_places.views import ListMikVahView, GetMikVahView, ListShuLView, GetShuLView

urlpatterns = [
    path("list_mikvah/", ListMikVahView.as_view(), name="list_mikvah"),
    path("get_mikvah/", GetMikVahView.as_view(), name="get_mikvah"),
    path("list_shul/", ListShuLView.as_view(), name="list_shul"),
    path("get_shul/", GetShuLView.as_view(), name="get_shul"),
]
