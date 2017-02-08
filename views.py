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
        iOperator = request.POST.get('Operator', '')
        itemId = request.POST.get('ItemId', '')
        iItem = Item.objects.get(ItemId=1)

        iAmount = request.POST.get('Amount', '')

        inStockBill.InStockBillCode = iCode
        inStockBill.InStockDate = iDate
        inStockBill.Operator = iOperator
        inStockBill.Item = iItem
        inStockBill.Amount = iAmount

        try:
          inStockBill.save()
        except:
            return HttpResponse("inStockbill表格保存失败！")
        """
        xfbdebugs = ''
        xfbdebugs = 'iCode:'+iCode+'|<p>  iDate:'+iDate +' <p> | iAmount:'+iAmount \
             + ' <p> | iOperator:'+iOperator +' |<p> itemId:' +itemId + '<p> Item: '+iItem.ItemName +' ---|---'
        return HttpResponse(xfbdebugs)
        """
        return HttpResponse("/success/")
    return render(request,'InStockAdd.html',{'errors':errors})
def success(request):
    return HttpResponse("表单提交成功！")
