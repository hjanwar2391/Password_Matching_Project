from django.shortcuts import render
from django.http import HttpResponse
from . form import Student, PasswordChack
# Create your views here.


def home(request):
    return render(request, './home/home.html')

# def form(request):
#     if request.method == "POST":
#         forms = Student(request.POST)
#         if forms.is_valid():
#             print(forms.cleaned_data)
#     else: 
#         forms = Student()
#     return render(request, './form/form.html', {'form':forms})

def PasswordChacker(request):
    if request.method == "POST":
        forms = PasswordChack(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
    else: 
        forms = PasswordChack()
    return render(request, './form/form.html', {'form':forms}) 
