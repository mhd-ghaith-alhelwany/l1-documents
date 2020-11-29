from django.urls import path, re_path

from docs import views

urlpatterns = [
    path("", views.index, name="index"),
    path("table/<int:id>/download_json", views.download_table_json, name='download_table_json'),
    path("table/<int:id>/download_xml", views.download_table_xml, name='download_table_xml'),
    path("<int:id>/download", views.download_document, name='download_document'),
    path("<int:id>/<int:table_id>", views.show, name='show_table'),
    path("<int:id>", views.show, name='show'),
    path("add", views.add, name='index')
]
