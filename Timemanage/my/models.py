# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Collects(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    strategy = models.OneToOneField('Strategys', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'collects'


class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    plan_name = models.CharField(max_length=255)
    strategy = models.ForeignKey('Strategys', models.DO_NOTHING, blank=True, null=True)
    current_time = models.DateTimeField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans'


class PolicyDetails(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    plan = models.ForeignKey(Plans, models.DO_NOTHING)
    strategy = models.ForeignKey('Strategys', models.DO_NOTHING)
    execution_time = models.DateTimeField(blank=True, null=True)
    execution_time_description = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'policy_details'


class Strategys(models.Model):
    strategy_id = models.AutoField(primary_key=True)
    strategy_name = models.CharField(max_length=255)
    strategy_details = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strategys'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    create_time = models.DateTimeField(blank=True, null=True)
    logout = models.PositiveIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
