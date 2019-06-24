from django.shortcuts import render
from home.forms import BookForms

# Create your views here.

def form_view(request):
    context=None
    msg = None
    form = None
    if request.method=='POST':
        form=BookForms(request.POST)
        if form.is_valid():
            book=Book(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('pur_date'),
                #genre=form.cleaned_data.get('author')
            )
            book.save()
            msg='book added successfully'
        else:
            msg=form.errors
    else:
       form=BookForms()
    return render(request,'forms.html',{"head":msg,"forms":form})