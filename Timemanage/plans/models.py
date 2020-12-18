from django.db import models


class PolicyDetails(models.Model):
    detail_id = models.AutoField(primary_key=True)
    plan_id = models.IntegerField()
    strategy_id = models.IntegerField()
    execution_time = models.DateField()
    execution_time_description = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField()

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
