from django.shortcuts import render
from faker import Faker
from . import models
from .models import Job
from decouple import config

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')\

def result(request):
    name = request.POST.get('name')
    if Job.objects.filter(name = name):
        job = Job.objects.get(name=name)
        import requests
        api = config("GIPHY_API_KEY")
        url = f'http://api.giphy.com/v1/gifs/search?api_key={api}&q={job}&lang=kr'
        response = requests.get(url).json()
        try:
            image_url = response['data'][0].get('images').get("original").get('url')
        except:
            image_url = None
        context = {
            'job': job,
            'name': name,
            'url' : image_url,
        }

        return render(request, 'jobs/result.html', context)
    else:
        fake = Faker('ko_KR')
        f_jobs = str(fake.job())
        jobs = Job(name=name, job=f_jobs)
        jobs.save()
        job = Job.objects.all()
        context = {
            'name': name,
            'job': job,
        }
        return render(request, 'jobs/result.html', context)
