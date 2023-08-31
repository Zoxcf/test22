
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Advertisment
from .forms import AdvertismentForm
from django.urls import reverse


from django.contrib.auth import get_user_model
from django.db.models import Count


# Create your views here.
def index(request):
    title = request.GET.get('query')
    print('-------->',title)
    if title:
        # advertisement = Advertisment.objects.filter(title = title)
        # advertisement = Advertisment.objects.filter(price__lt = int(title))
        # advertisement = Advertisment.objects.filter(price__gt = title)
        # advertisement = Advertisment.objects.filter(price__gte = float(title))
        # advertisement = Advertisment.objects.filter(price__lte = float(title))
        # advertisement = Advertisment.objects.filter(price = float(title))
        advertisement = Advertisment.objects.filter(title__contains  = title)
        # advertisement = Advertisment.objects.filter(title__icontains  = title)
        # advertisement  = Advertisment.objects.filter(title__endswith = title)
        # advertisement  = Advertisment.objects.filter(title__startswith = title)

    else: 
        advertisement = Advertisment.objects.all()
    context = {
        'advertisement':advertisement,
        'title':title,
               }
    return render(request,'advertisments/index.html',context=context)

User = get_user_model()
def top(request):
    users = User.objects.annotate(adv_count = Count('advertisment')).order_by('-adv_count')
    context = {
        'users':users
    }
    return render(request,'advertisments/top-sellers.html',context)


def advertisement_post(request):
    if request.method == "POST":
        form = AdvertismentForm(request.POST,request.FILES)
        if form.is_valid():
            advertisement = Advertisment( **form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('/')
            return redirect(url)
    else:
        form = AdvertismentForm()
    context = {'form':form}
    return render(request,'advertisments/advertisement-post.html',context=context)


def advertisement(request,pk):
    advertisement = Advertisment.objects.get(id = pk)
    context = {
        'advertisement':advertisement
    }
    return render(request,'advertisments/advertisement.html',context)