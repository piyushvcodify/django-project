from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, emp_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return None

     # 3. Retrieve
    def get(self, request, emp_id, *args, **kwargs):
        '''
        Retrieves the Employee with given emp_id
        '''
        emp_instance = self.get_object(emp_id)
        if not emp_instance:
            return Response(
                {"res": "Object with Employee id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmployeeSerializer(emp_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the employee with given employee data
        '''
        data = {
            "employee_Id": request.data.get('employee_Id'),
            "employee_first_name": request.data.get('employee_first_name'),
            "employee_last_name": request.data.get('employee_last_name'),
            "job_name": request.data.get('job_name'),
            "date_of_joinning": request.data.get('date_of_joinning'),
            "department_name": 2
        }

        obj = Employee.objects.filter(employee_Id=request.data.get('employee_Id'))
        if not obj:
            serializer = EmployeeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Passed employee_Id already exists.", status=status.HTTP_400_BAD_REQUEST)


    
    def put(self, request, emp_id, *args, **kwargs):
            '''
            Updates the todo item with given todo_id if exists
            '''
            emp_instance = self.get_object(emp_id)
            if not emp_instance:
                return Response(
                    {"res": "Object with employee id does not exists"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer = EmployeeSerializer(instance = emp_instance, data=request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, emp_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(emp_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


