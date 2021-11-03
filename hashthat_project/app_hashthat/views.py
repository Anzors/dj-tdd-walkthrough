from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib

# Create your views here.

def home(request):
    # if it is a POST check if we already have a hash of that text
    if request.method == 'POST':
        print(request.POST)
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            # get the input text
            clearText = filled_form.cleaned_data['text']
            # hash it
            hashText = hashlib.sha256(clearText.encode('utf-8')).hexdigest()

            try:
                hashPulled = Hash.objects.get(hash=hashText)
            except Hash.DoesNotExist:
                # Save it to the database
                newHash = Hash()
                newHash.text = clearText
                newHash.hash = hashText
                newHash.save()
            return redirect('hash', hash=hashText)  

def hash(request, hash):
    # get the hash object from db
    #####   hashobj = Hash.objects.get(hash=hash)
    try:
        hashobj = Hash.objects.get(hash=hash)
    except:
        newHash = Hash()    
        newHash.text = "Stop hacking me"
        newHash.hash = "INVALID"
    # pass this object to a html file to use
    return render (request, 'hashing/hash.html',{'hash': hashobj}) 

def home(request):
    return render(request, 'hashing/home.html')

def home(request):
    form = HashForm()
    return render(request, 'hashing/home.html',{'form': form})

