from django.shortcuts import render
def aditya(request):
    return render(request,'aditya.html',context={'name':'aditya'})

def neel(request):
    return render(request,'neel.html',context={'greetings':'Thanks for reading'})
