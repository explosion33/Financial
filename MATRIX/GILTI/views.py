from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

class ClientView(generic.ListView):
    template_name = 'GILTI/clientview.html'
    
    def get_queryset(self):
        client_list = Client.objects.all()
        
        return client_list

class ClientCreate(generic.UpdateView):
    pass


class ClientUpdate(generic.UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'GILTI/updateclient.html'



def ClientDelete(*args, **kwargs):
    print("")
    print("")
    Client.objects.filter(id=kwargs['client_id']).delete()
    return HttpResponseRedirect('/GILTI')
    

    
class SubView(generic.DetailView):
    model = Client
    template_name = 'GILTI/subview.html'

    def get_context_data(self, **kwargs):
        client = kwargs['object']
        print("")

        sub_list = Subsidiary.objects.filter(client_id=client.id)

        context = {
            'sub_list':sub_list,
        }

        return context

class SubDetail(generic.DetailView):
    model = Subsidiary
    template_name = 'GILTI/subdetail.html'

    def get_context_data(self, **kwargs):
        sub = kwargs['object']
        context = {
            'sub':sub
        }
        return context
        
class SubCreate():
    pass    
def SubDelete(*args, **kwargs):

    client_id = kwargs['client_id']
    sub_id = kwargs['pk']

    sub = Subsidiary.objects.filter(id=sub_id)
    sub.delete()
    return HttpResponseRedirect('/GILTI/sub' + str(client_id))





