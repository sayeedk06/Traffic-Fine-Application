from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from google.cloud import vision
import io
from .forms import FineForm
from .models import Fine
# Create your views here.

@login_required
def fine(request):
    if request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']
        # print(uploaded_file.name)
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)

        client = vision.ImageAnnotatorClient()
        path = "media/"+uploaded_file.name
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        image_context = vision.types.ImageContext(language_hints=["bn"])
        response = client.text_detection(image=image,image_context=image_context)
        texts = response.text_annotations
        print('Texts:')
        num = 0
        for text in texts[:1]:
            # print('\n"{0}"'.format(text.description))
            num = text.description
        form = Fine(amount=request.POST['amount'],numberPlate=num)
        form.save()



        os.remove(os.path.join(settings.MEDIA_ROOT,str(uploaded_file.name) ))
        return render(request, 'user/profile.html', {
            'uploaded_file_url': uploaded_file_url
        })
    else:
        return render(request,'assignFine/assignFine.html')
