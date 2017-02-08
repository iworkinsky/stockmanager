from django.shortcuts import render
from django.http import  HttpResponse
import datetime
from learn.models import *


# Create your views here.
def search_form(request):
    return render(request,'search_form.html')
def search(request):
    if  'q' in request.GET :
        q = request.GET['q']
    if not q:
        error = True
    else:
        items = Item.objects.filter(ItemName__icontains=q)
        return render(request,'search_results.html',{'items':items,'query':q})
    return render(request, 'search_form.html', {'error': error})

def AddInStock(request):
    return render(request, 'InStockAdd.html')
def AddInStockBill(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('InStockBillCode',''):
            errors.append('Please enter a InStockBillCode.')
        if not request.POST.get('InStockDate', ''):
            errors.append('Please enter a InStockDate.')
        if not request.POST.get('Amount', ''):
            errors.append('Please enter a Amount.')
        if not request.POST.get('Operator', ''):
            errors.append('Please enter a Operator.')
    if not errors:
        inStockBill = InStockBill()
        iCode = request.POST.get('InStockBillCode','')
        iDate = request.POST.get('InStockDate', '')
        iAmount = request.POST.get('Amount', '')
        iOperator = request.POST.get('Operator', '')
        itemId = request.POST.get('ItemId','')
        try:
            obj = InStockBill(InStockBillCode=iCode,InStockDate=iDate,Amount=iAmount,Operator=iOperator)
            obj.save()
        except:
            return HttpResponse("插入到InStockBill失败。 %s" % iCode)
        #inStockBill.save()

        return HttpResponse("/success/")
    return render(request,'InStockAdd.html',{'errors':errors})
def success(request):
    return HttpResponse("表单提交成功！")
