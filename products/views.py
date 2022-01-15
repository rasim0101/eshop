from django.shortcuts import render

def product_list(request):
	return render(request, 'products/product_list.html')


def product_detail(request):
	return render(request, 'products/product_detail.html')

def create_product(request):
	return render(request, 'products/create_product.html')
