# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PolicyDetails(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    plan = models.ForeignKey('Plans', models.DO_NOTHING)
    strategy = models.ForeignKey('Strategys', models.DO_NOTHING)
    execution_time = models.DateField()
    execution_time_description = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'policy_details'
        unique_together = (('user', 'plan', 'strategy', 'execution_time'),)
