from django.shortcuts import render, redirect
from .forms import ProductForm

def product_list(request):
	return render(request, 'products/product_list.html')


def product_detail(request):
	return render(request, 'products/product_detail.html')

def create_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			return redirect('product_list')
	else:
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, 'products/create_product.html', context)

