from django.shortcuts import render

def product_list(request):
	return render(request, 'products/product_list.html')


def product_detail(request):
	return render(request, 'products/product_detail.html')
