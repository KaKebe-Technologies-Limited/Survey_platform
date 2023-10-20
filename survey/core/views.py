from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Survey
from .forms import MyForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success')
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})

def afterlogin_view(request):
    return redirect('admin-dashboard')

@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    survey = Survey.objects.all()
    context = {
        'survey':survey
    }
    return render(request, 'dashboard.html', context)


def view_item(request,id):
    item = get_object_or_404(Survey, pk=id)  # Retrieve the item by its ID or return a 404 response if not found
    return render(request, 'view.html', {'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Survey, pk=item_id)
    
    if request.method == 'POST':
        item.delete()  # Delete the item from the database
        # Redirect to a success page or any other appropriate view after deletion
        return render(request, 'delete_success.html')
    
    return render(request, 'delete_confirmation.html', {'item': item})


def success_page(request):
    return render(request, 'submit_success.html')



