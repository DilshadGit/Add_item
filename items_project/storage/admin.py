from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):


	class Meta:
		model = Item

	list_display = ('item_name', 'item_code', 'create_date', 'updated')
	search_fields = ['item_name', 'create_date', 'updated']
	list_filter = ['create_date']

admin.site.register(Item, ItemAdmin)