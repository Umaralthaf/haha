from django.shortcuts import render,redirect
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        
        if password == 'DEEPCODERS':
            # If password is correct, render the login form
            return redirect('login_successful', username=username)
        else:
            # If password is incorrect, return an error message
            return render(request, "nopass.html", {'username': username})
    else:
        # If the request method is not POST, render the login form
        return render(request, 'index.html')

def login_successful(request, username):
    if request.method == 'POST':
        course = request.POST.get('course')
        
        
        if course == "C":
            # If the course selected is C, render the c.html template with username
            return render(request, "c.html", {'username':  username})
        elif course == "PYTHON":
            return render(request, "python.html", {'username': username})
        elif course == "JAVA":
            return render(request, "java.html", {'username': username})
        elif course == "DJANGO":
            return render(request, "django.html", {'username':username})
        elif course == "MERN-STACK":
            return render(request, "mernstack.html", {'username': username})
        elif course == "SQL AND DATABASE":
            return render(request, "sql.html", {'username':  username})
        elif course == "MONGODB":
            return render(request, "mongodb.html", {'username': username})
        elif course == "MACHINE LEARNING":
            return render(request, "ml.html", {'username':  username})
        elif course == "PYTHON TKINTER":
            return render(request, "tkinter.html", {'username': username})
        else:
            # For other courses, return an error message
            return render(request, "nocou.html", {'username':  username})
    else:
        # If the request method is not POST, render the index.html template
        return redirect('login_view')