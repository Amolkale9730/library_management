from django.shortcuts import render
from libapp.models import lib

def lib_viewe(request):
    data=lib.objects.all()
    return render(request, 'libapp/viewall.html', {"data":data})



def lib_get(request, id):
    obj=lib.objects.get(pk=id)
    return render(request, 'libapp/view.html', {"obj":obj})



def lib_add(request):
    if request.method=="POST":
        book_name=request.POST.get('name')
        published_year=request.POST.get('bpublished')
        price=request.POST.get('bprice')

        obj=lib(book_name=name, published_year=bpublished, price=bprice)
        obj.save()

        return redirect('/viewall/')
    return render(request, 'libapp/add.html')


def lib_update(request, id):
    obj=Emp.objects.get(pk=id)
    if request.method=="POST":
        obj.book_name=request.POST.get('ebook')
        obj.published_year=request.POST.get('epublished')
        obj.price=request.POST.get('eprice')
        obj.save()
        return redirect(f'/view/{obj.id}')
    return render(request, 'libapp/update.html', {'obj':obj})

def lib_delete(request, id):
    obj=lib.objects.get(pk=id)
    obj.delete()
    return redirect('/viewall/')


