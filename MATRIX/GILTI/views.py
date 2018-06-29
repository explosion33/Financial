from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import *
import datetime

# Create your views here.

class ClientView(generic.ListView):
    template_name = 'GILTI/clientview.html'
    
    def get_queryset(self):
        client_list = Client.objects.all()
        
        return client_list

def ClientCreate(*args, **kwargs):
    c = Client(name='')
    c.save()
    return HttpResponseRedirect(reverse('GILTI:updateclient', args=[c.id]))


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


        data_fields = [
            'Gross Income over deductions (including taxes)',
            'CFC Exclusions - ECI',
            'CFC Exclusions - Subpart F',
            'CFC Exclusions - Related Party Dividends',
            'CFC Subtotal * Ownership',
            'Tested Loss',
            'Net CFC Tested Income',
            'Tested Foreign Income Taxes',
            'Qualified Business Asset Investment',
            '10% of QBAI',
            'Interest Expense that reduced tested income and corresponding income not included in tested income',
            'Tested Income',
            'CFC Exclusions - ECI',
            'CFC Exclusions - Subpart F',
            'CFC Exclusions - Related Party Dividends',
            'CFC Subtotal * Ownership',
            'Tested Loss',
            'Net CFC Tested Income',
            'Tested Foreign Income Taxes',
            'Qualified Business Asset Investment',
            '10% of QBAI',
            'Interest Expense that reduced tested income and corresponding income not included in tested income',
            'Net deemed tangible income',
            'GILTI',
            'Inclusion percentage',
            'Deemed paid credit before 20% haircut',
            'Deemed paid credit after 20% haircut',
            'Taxable Income before GILTI and NOLs',
            'Grossed up GILTI',
            'Net Operating Loss Deduction',
            'Net GILTI',
            '50% Deduction',
            'Taxable income before credit and expense allocation',
            'Expense allocation to GILTI basket',
            'GILTI for FTC Limitation',
            'FTC Limitation',
            'US tax before credit',
            'Foreign Tax Credit',
            'US Tax on GILTI',
            'Foreign Effective Tax rate on tested income',
            'U.S. effective rate',
            'Taxable Income before GILTI and NOLs',
            'Net Operating Loss Available',
            'Amount used for Taxable Income + GILTI',
            'Net Operating Loss Carryforward',
        ]

        context = {
            'sub_list':sub_list,
            'client':client,
            'fields':data_fields,
        }

        return context

class SubDetail(generic.DetailView):
    model = Subsidiary
    template_name = 'GILTI/subdetail.html'

    def get_context_data(self, **kwargs):
        sub = kwargs['object']
        client = sub.client
        numFields = []
        sub_data=[]

        data_fields = [
            'Gross Income over deductions (including taxes)',
            'CFC Exclusions - ECI',
            'CFC Exclusions - Subpart F',
            'CFC Exclusions - Related Party Dividends',
            'CFC Subtotal * Ownership',
            'Tested Loss',
            'Net CFC Tested Income',
            'Tested Foreign Income Taxes',
            'Qualified Business Asset Investment',
            '10% of QBAI',
            'Interest Expense that reduced tested income and corresponding income not included in tested income',
            'Tested Income',
            'CFC Exclusions - ECI',
            'CFC Exclusions - Subpart F',
            'CFC Exclusions - Related Party Dividends',
            'CFC Subtotal * Ownership',
            'Tested Loss',
            'Net CFC Tested Income',
            'Tested Foreign Income Taxes',
            'Qualified Business Asset Investment',
            '10% of QBAI',
            'Interest Expense that reduced tested income and corresponding income not included in tested income',
            'Net deemed tangible income',
            'GILTI',
            'Inclusion percentage',
            'Deemed paid credit before 20% haircut',
            'Deemed paid credit after 20% haircut',
            'Taxable Income before GILTI and NOLs',
            'Grossed up GILTI',
            'Net Operating Loss Deduction',
            'Net GILTI',
            '50% Deduction',
            'Taxable income before credit and expense allocation',
            'Expense allocation to GILTI basket',
            'GILTI for FTC Limitation',
            'FTC Limitation',
            'US tax before credit',
            'Foreign Tax Credit',
            'US Tax on GILTI',
            'Foreign Effective Tax rate on tested income',
            'U.S. effective rate',
            'Taxable Income before GILTI and NOLs',
            'Net Operating Loss Available',
            'Amount used for Taxable Income + GILTI',
            'Net Operating Loss Carryforward',
        ]

        for n in range(0, len(data_fields)):
            data_fields[n] += ':'
            numFields.append(n)

        
        subs = Subsidiary.objects.filter(client_id=client.id)
    
        for sub in subs:
            slist=[]
            for i in range(0,45):
                slist.append(i)
            sub_data.append(slist)
        
        print(numFields)
        context = {
            'sub_data':sub_data,
            'fields':data_fields,
            'numF':numFields
        }
        return context
        
def SubCreate(*args, **kwargs):
    cid = kwargs['client_id']
    c = Client.objects.filter(id=cid)[0]
    s = Subsidiary(client=c, country='', ref='')
    s.save()
    return HttpResponseRedirect(reverse('GILTI:updatesub', kwargs={'pk':s.id}))

class SubUpdate(generic.UpdateView):
    model = Subsidiary
    fields = '__all__'
    template_name = 'GILTI/updateclient.html'
    client = None



def SubDelete(*args, **kwargs):

    client_id = kwargs['client_id']
    sub_id = kwargs['pk']

    sub = Subsidiary.objects.filter(id=sub_id)
    sub.delete()
    return HttpResponseRedirect('/GILTI/sub' + str(client_id))





