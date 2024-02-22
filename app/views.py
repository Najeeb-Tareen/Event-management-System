from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Event, Registration, Person, Team
from .forms import Person_form, Reg_Form, Team_form
from django.views.generic import TemplateView, CreateView

def create_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        location = request.POST.get('location')

        eve = Event.objects.create(title=title, description=description, date=date, location=location)
        eve.save()

        return render(request,"app/added.html")
    return render(request, 'app/event.html')

class lending(TemplateView):
    template_name = "app/lending.html"


class Creat_team(CreateView):
    model = Team
    template_name = 'app/creat_team.html'
    form_class = Team_form



# def do_register(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         event = request.POST.get('event')
#         event = Event.objects.get(title=event)

#         fit = Registration.objects.create(name=name, email=email, event=event)
#         fit.save()
#         return render(request,'app/confirm.html')
#     return render(request, 'app/registration.html')

def do_register(request):
    if request.method == "POST":
        form = Reg_Form(request.POST)
        
        form.save()
        return HttpResponse('form done')
    else:
        form = Reg_Form()
        return render(request, 'app/registration.html', {'key1':form})


        









def Event_list(request):
    eventlst = Event.objects.all()
    context = {'eventlst': eventlst}
    return render(request, 'app/eventlst.html', context)



def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'app/detail.html', {'event': event})


def person_dtl(request):
    if request.method == "POST":
        form = Person_form(request.POST) 
        form.save()
        return HttpResponse('done it')
    else:
        form = Person_form()
    return render(request, "app/person.html", {
        "form":form
    })




# def person_dtl(request):
#     if request.method == 'POST':
#         form = Person_form(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             # print(name)
#             # print(email)
#             # print(password)
#             prs = Person(name=name, email=email, password=password)
#             form.save()
#             return HttpResponse('done')

#     else:
#         form = Person_form()
#         return render(request, 'app/person.html', {'form':form})
