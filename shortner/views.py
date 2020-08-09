from django.shortcuts import redirect, render
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner


# Create your views here.
def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url, )


def Make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            print(a)
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid Url"
    return render(request, 'shortner/home.html', {'form': form, 'a': a})
from django.shortcuts import render

# Create your views here.
