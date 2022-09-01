from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Employee Endpoints':{
		'List':'http://127.0.0.1:8000/employee-list/',
		'Detail View':'http://127.0.0.1:8000/employee-detail/<str:pk>/',
		'Create':'http://127.0.0.1:8000/employee-create/',
		'Update':'http://127.0.0.1:8000/employee-update/<str:pk>/',
		'Delete':'http://127.0.0.1:8000/employee-delete/<str:pk>/',
		'filter':'http://127.0.0.1:8000/employee-filter/<str:pk>/',
		}
		}

	return Response(api_urls,status=status.HTTP_200_OK)

@api_view(['GET'])
def employeeList(request):
	employees = Employee.objects.all().order_by('-id')
	serializer = EmployeeSerializer(employees, many=True)
	return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def employeeDetail(request, pk):
	employees = Employee.objects.get(id=pk)
	serializer = EmployeeSerializer(employees, many=False)
	return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def employeeCreate(request):
	serializer = EmployeeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def employeeUpdate(request, pk):
	employees = Employee.objects.get(id=pk)
	serializer = EmployeeSerializer(instance=employees, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['DELETE'])
def employeeDelete(request, pk):
	employee = Employee.objects.get(id=pk)
	employee.delete()

	return Response('Item succsesfully delete!',status=status.HTTP_200_OK)



