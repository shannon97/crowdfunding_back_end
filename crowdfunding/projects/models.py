from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    title = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    goal = models.IntegerField()
    needed_by = models.DateField(blank=True, null=True)
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )

    @property
    def goal_total(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True, null=True)
    anonymous = models.BooleanField(blank=True, null=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )