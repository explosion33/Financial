from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import * 
#import pandas as pd
#from django_pandas.io import read_frame
import datetime
from math import ceil

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

    Client.objects.filter(id=kwargs['client_id']).delete()
    return HttpResponseRedirect('/GILTI')
    

    
class SubView(generic.DetailView):
    model = Client
    template_name = 'GILTI/subview.html'

    def get_context_data(self, **kwargs):
        client = kwargs['object']


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
    model = Client
    template_name = 'GILTI/subdetail.html'

    def get_context_data(self, **kwargs):
        client = kwargs['object']
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

        us_calc = []
        
        if len(subs) > 0:

            for sub in subs:
                slist = [
                    sub.gross_income,   #0
                    sub.eci,    #1
                    sub.sub_f,  #2
                    sub.rp_div  #3
                ]

                slist.append(slist[0] + slist[1] + slist[2] + slist[3]),    #4
                slist += [
                    0,  #5
                ]

                if sub.gross_income < 0:
                    for i in range(0, 5):
                        slist[i] = 0

                slist += [
                    slist[0] + slist[1] + slist[2] + slist[3],  #6
                    sub.for_tax,    #7
                    sub.qbai    #8
                ]
                slist += [
                    '', #9
                    sub.int_exp,    #10
                ]
                slist += [
                    slist[0]*(sub.ownership/100),  #11
                    slist[1]*(sub.ownership/100),   #12
                    slist[2]*(sub.ownership/100),   #13
                    slist[3]*(sub.ownership/100)   #14
                ]

                

                if sub.gross_income < 0:
                    for i in range(11, 15):
                        slist[i] = 0

                    slist[5] = sub.gross_income
                    slist[6] = slist[5]
                    #slist[16] = slist[11]
                    #slist[17] = slist[11]

                slist += [
                    slist[14] + slist[13] + slist[12] + slist[11],   #15
                    sub.gross_income *(sub.ownership/100),    #16
                ]

                if sub.gross_income < 0:
                    slist[15] = 0
                else:
                    slist[16] = 0

                slist += [
                    slist[15] + slist[16], #17
                    slist[7] * (sub.ownership/100),   #18
                    #slist[2]*(sub.ownership/100) + slist[3]*(sub.ownership/100),    #19
                    #slist[7]*(sub.ownership/100),    #20
                    slist[8]*(sub.ownership/100),   #19
                    '', #20
                    slist[10]*(sub.ownership/100),    #21

                ]

                
                sub_data.append(slist)

            gross = 0
            eci = 0
            subf = 0
            rpdiv = 0
            subtot = 0
            loss = 0
            CFCTInc = 0
            forinc = 0
            qbai = 0
            int_exp = 0
            tinc = 0
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0

            for sub in sub_data:
                gross += sub[0] #0
                eci += sub[1]   #1
                subf += sub[2]  #2
                rpdiv += sub[3] #3
                subtot += sub[4]    #4
                loss += sub[5]  #5
                CFCTInc += sub[6]   #6
                forinc = 0  #7
                qbai += sub[8]  #8
                int_exp += sub[10]  #10
                tinc += sub[11] #11
                a += sub[12]    #12
                b += sub[13]    #13
                c += sub[14]    #14
                d += sub[15]    #15
                e += sub[16]    #16
                f += sub[17]    #17
                g += sub[19]    #19
                h += sub[21]    #21

            us_calc.extend((gross, eci, subf, rpdiv, subtot, loss, CFCTInc, forinc,
                            qbai, (qbai/10), int_exp, tinc, a, b, c, d, e, f, 0, g, g/10, h))

            if us_calc[20] - us_calc[21] <= 1:  #22
                us_calc.append(0)
            else:
                us_Calc.append(us_calc[20] - us_calc[21])

            if us_calc[17] - us_calc[22] < 0:   #23
                us_calc.append(0)
            else:
                us_calc.append(us_calc[17] - us_calc[22])
            if us_calc[15] == 0:
                us_calc.append(0)
            elif us_calc[23]/us_calc[15] <= 1:    #24
                us_calc.append((us_calc[23]/us_calc[15]) * 100)
            else:
                us_calc.append('ERROR')

            us_calc.extend((0, 0, client.tax_inc, us_calc[23], 0))

            if (us_calc[27] + us_calc[28]) <= 0: #30
                us_calc.append(0)
            else:
                us_calc.append(us_calc[27] + us_calc[28])

            us_calc.append(0)   #31

            if us_calc[30] < 0: #32
                us_calc.append(0)
            else:
                us_calc.append(us_calc[30])

            us_calc.extend((client.exp_alloc, (us_calc[30] + client.exp_alloc)))
            us_calc.append(us_calc[34] * 0.21)
            us_calc.append(us_calc[32] * 0.37)

            if us_calc[35] < 0:
                us_calc.append(35)
            else:
                us_calc.append(0)

            us_calc.extend((us_calc[36] - us_calc[37], 0,
                            client.US_Rate, client.tax_inc, 0, 0, 0))

            #, 0, us_calc[23], client.exp_alloc))

            sub_data.append(us_calc)
            lst = []
            for i in range(0, len(sub_data[len(sub_data)-1])):
                lst.append(i)

            #sub_data.append(lst)

            for i in range(0, len(sub_data)):
                for l in range(0, len(sub_data[i])):
                    if l == 24:
                        sub_data[i][l] = round(sub_data[i][l], 2)
                    elif type(sub_data[i][l]) == float:
                        
                        if abs(sub_data[i][l] - int(sub_data[i][l])) == 0.5:

                            if sub_data[i][l] < 0:
                                sub_data[i][l] = ceil(abs((sub_data[i][l]))) * -1
                            else:
                                sub_data[i][l] = ceil(sub_data[i][l])
                        else:

                            sub_data[i][l] = round(sub_data[i][l])
                    

        

        context = {
            'sub_data':sub_data,
            'fields':data_fields,
            'subs':subs,
            'client':client
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

    sub_id = kwargs['pk']

    sub = Subsidiary.objects.filter(id=sub_id)
    id = sub[0].client_id
    sub.delete()
    return HttpResponseRedirect('/GILTI/sub-' + str(id) +'/detail')





