# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PolicyDetails(models.Model):
    user_id = models.IntegerField(primary_key=True)
    plan_id = models.IntegerField()
    strategy_id = models.IntegerField(blank=True, null=True)
    execution_time = models.DateField()
    execution_time_description = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'policy_details'
        unique_together = (('user_id', 'plan_id', 'strategy_id', 'execution_time'),)



class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to='my.Users', to_field="user_id", on_delete=models.DO_NOTHING, db_column='user_id')
    plan_name = models.CharField(max_length=255)
    strategy_id = models.ForeignKey(to='strategys.Strategys', to_field="strategy_id", on_delete=models.DO_NOTHING,
                                    blank=True, null=True, db_column='strategy_id')
    current_time = models.DateField()
    begin_time = models.DateField()
    end_time = models.DateField()
    status = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField()
    plan_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans'
