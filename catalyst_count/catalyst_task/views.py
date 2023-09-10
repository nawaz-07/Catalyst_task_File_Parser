from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from allauth.account.views import LoginView,SignupView,LogoutView
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyFileSerializer
import gc



# Create your views here.
def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',', encoding='utf-8-sig')
    list_csv = [list(row) for row in df.values]

    objectsCreate = []
    for i in list_csv:
        obj = CSVData(
            emp_id=i[0],
            name=i[1],
            domain=i[2],
            year=i[3],
            industry=i[4],
            size=i[5],
            area=i[6],
        )
        objectsCreate.append(obj) 
    CSVData.objects.bulk_create(objectsCreate)
            

        
@login_required
def main(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['file']
            obj = File.objects.create(file=files)
            create_db(obj.file.path)
            return redirect('filter')
    else:
        form = UploadFileForm

    context = {'form': form}
    return render(request, 'upload.html', context)

@login_required
def filter_view(request):
    if request.method == 'GET':
        emp_id = request.GET.get('emp_id')
        name = request.GET.get('name')
        year = request.GET.get('year')
        domain = request.GET.get('domain')
        industry = request.GET.get('industry')
        size = request.GET.get('size')
        area = request.GET.get('area')

        filtered_data = CSVData.objects.all()

        # Perform filtering based on selected options
        if emp_id:
            filtered_data = filtered_data.filter(Emp_id=emp_id)
        if name:
            filtered_data = filtered_data.filter(name=name)
        if year:
            filtered_data = filtered_data.filter(year=year)
        if domain:
            filtered_data = filtered_data.filter(domain=domain)
        if industry:
            filtered_data = filtered_data.filter(industry=industry)
        if size:
            filtered_data = filtered_data.filter(size=size)
        if area:
            filtered_data = filtered_data.filter(area=area)

        context = {
            'filtered_data': filtered_data,
        }

        return render(request, 'filter.html', context)

    return render(request, 'filter.html')


# Django RestFrameWork

@login_required
@api_view(['GET'])
def filter_api(request):
    emp_id = request.GET.get('emp_id')
    name = request.GET.get('name')
    year = request.GET.get('year')
    domain = request.GET.get('domain')
    industry = request.GET.get('industry')
    size = request.GET.get('size')
    area = request.GET.get('area')

    filtered_data = CSVData.objects.all()

    # Perform filtering based on selected options
    if emp_id:
        filtered_data = filtered_data.filter(Emp_id=emp_id)
    if name:
        filtered_data = filtered_data.filter(name=name)
    if year:
        filtered_data = filtered_data.filter(year=year)
    if domain:
        filtered_data = filtered_data.filter(domain=domain)
    if industry:
        filtered_data = filtered_data.filter(industry=industry)
    if size:
        filtered_data = filtered_data.filter(size=size)
    if area:
        filtered_data = filtered_data.filter(area=area)

    serializer = MyFileSerializer(filtered_data, many=True)
    return Response(serializer.data)


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Replace with your custom login template
    
class CustomSignupView(SignupView):
        template_name = 'signup.html'
    
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'