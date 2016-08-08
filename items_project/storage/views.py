from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect


from .forms import ItemForm
from .models import Item


def item_list(request):
	items = Item.objects.all().order_by('-create_date')
	context = {
		'query_set': items,
	}

	return render(request, 'item_list.html', context)

def create_new_item(request):
	form = ItemForm(request.POST or None)
	if form.is_valid():
		obj_form = form.save(commit=False)
		obj_form.save()

		messages.success(request, 'Successfully created ')
		return HttpResponseRedirect(obj_form.get_absolute_url())
	context = {
		'form': form,
	}

	return render(request, 'create_item.html', context)

def item_details(request, slug=None):
	instance_obj = get_object_or_404(Item, slug=slug)

	context = {
		'title': instance_obj.item_name,
		'content': instance_obj.item_desc,
		'create_date': instance_obj.create_date,
	}
	return render(request, 'item_detail.html', context)



def update_item(request, slug=None):
	instance = get_object_or_404(Item, slug=slug)

	form = ItemForm(request.POST or None, instance=instance)
	if form.is_valid():
		obj_form = form.save(commit=False)
		obj_form.save()

		messages.success(request, 'Successfully Updated ')
		return HttpResponseRedirect(obj_form.get_absolute_url())
	context = {
		'title': instance.item_name,
		'instance': instance,
		'form': form,
	}
	return render(request, 'create_item.html', context)


def delete_item(request, slug=None):
	instance = get_object_or_404(Item, slug=slug)
	instance.delete()
	messages.success(request, 'The Item successfully Deleted ')
	return redirect('storage:item_list')