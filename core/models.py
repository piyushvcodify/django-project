from django.db import models


class Employee(models.Model):
    employee_Id = models.IntegerField()
    employee_first_name = models.CharField(max_length=150)
    employee_last_name = models.CharField(max_length=150)
    job_name  = models.CharField(max_length=150)
    date_of_joinning  = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.employee_id)+" : "+self.employee_name

    class Meta:
        db_table = "tbl_employees"
        verbose_name = "Employee"
        verbose_name_plural = "Employee's"
