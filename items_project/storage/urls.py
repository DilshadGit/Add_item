from django.conf.urls import include, patterns, url
from django.contrib import admin

from .views import (
		item_list,
		create_new_item,
		item_details,
		update_item,
		delete_item,
	)

urlpatterns = (
	url(r'^$', item_list, name='item_list'),
	url(r'^create/$', 'storage.views.create_new_item', name='create_new_item'),
	url(r'^(?P<slug>[\w-]+)/$', 'storage.views.item_details', name='details'),

	url(r'^(?P<slug>[\w-]+)/edit/$', 'storage.views.update_item', name='update_item'),


	url(r'^(?P<id>\d+)/delete/$', 'storage.views.delete_item', name='delete_item'),
)