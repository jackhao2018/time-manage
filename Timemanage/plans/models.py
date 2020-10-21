# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='my.Users', on_delete=models.DO_NOTHING)
    plan_name = models.CharField(max_length=255)
    strategy = models.ForeignKey(to='strategys.Strategys', on_delete=models.DO_NOTHING,blank=True, null=True)
    current_time = models.DateTimeField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans'