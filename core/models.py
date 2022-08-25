from django.db import models


class Team(models.Model):
    pass
class Project(models.Model):
    pass

class Role(models.Model):
    role_name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "tbl_role"
        verbose_name = "Role"
        verbose_name_plural = "Role"

class Department(models.Model):
    department_name = models.CharField(max_length=150)
    department_description = models.TextField(blank=True,null=True)
    role = models.ManyToManyField(Role)
    
    def __str__(self):
        return self.department_name

    # def save(self,*args, **kwargs):
    #     self.department_name = self.department_name.title()
    #     super(Department, self).save(*args, **kwargs)

    class Meta:
        db_table = "tbl_department"
        verbose_name = "Department"
        verbose_name_plural = "Department"

class Employee(models.Model):
    employee_Id = models.IntegerField()
    employee_first_name = models.CharField(max_length=150)
    employee_last_name = models.CharField(max_length=150)
    job_name  = models.CharField(max_length=150)
    date_of_joinning  = models.DateField()
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.employee_Id)+" : "+self.employee_first_name +" "+ self.employee_last_name

    class Meta:
        db_table = "tbl_employees"
        verbose_name = "Employee"
        verbose_name_plural = "Employee's"
