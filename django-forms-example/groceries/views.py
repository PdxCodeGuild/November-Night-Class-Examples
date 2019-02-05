from django.shortcuts import render, redirect

from .models import GroceryItem
from .forms import GroceryItemForm

def groceries(request):
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groceries:list')
    else:
        form = GroceryItemForm()

    items = GroceryItem.objects.all()
    return render(request, 'groceries.html', {'items': items, 'form': form})