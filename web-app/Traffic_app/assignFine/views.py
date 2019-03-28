from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
@login_required
def fine(request):
    if request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        os.remove(os.path.join(settings.MEDIA_ROOT,str(uploaded_file.name) ))
        return render(request, 'assignFine/assignFine.html', {
            'uploaded_file_url': uploaded_file_url
        })
    else:
        return render(request,'assignFine/assignFine.html')
