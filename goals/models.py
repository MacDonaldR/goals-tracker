from django.db import models

# Create your models here.

# Users can create multiple goals with an associated start/end date and motivation
# Goals can have multiple resources (books, websites, etc.) associated with them
# Goals can have multiple milestones used to track progress
# Goals can have multiple sessions with resources to make progress


class Goal(models.Model):
    name = models.CharField(max_length=100)
    commitment_date = models.DateField(auto_now_add=True)
    committed_effort = models.CharField(max_length=100)
    planned_completion_date = models.DateField()
    actual_completion_date = models.DateField()
    motivation = models.TextField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.CharField(max_length=50,
        choices=[('L','Low'),('M','Medium'),('H','High')])
    level = models.CharField(max_length=50,
        choices=[('B','Beginner'),('I','Intermediate'),('A','Advanced')])

    def __str__(self):
        return self.name


class Session(models.Model):
    date = models.DateField()
    duration = models.IntegerField()
    description = models.TextField()
    resource = models.ForeignKey('Resource',
        on_delete=models.CASCADE)
    goal = models.ForeignKey('Goal',
        on_delete=models.CASCADE)


    def __str__(self):
        return self.description

class Milestone(models.Model):
    name = models.CharField(max_length=50)
    goal = models.ForeignKey('Goal',
        on_delete=models.CASCADE)
    planned_completion_date = models.DateField()
    actual_completion_date = models.DateField()
    reward = models.TextField()
    proof = models.TextField()

    def __str__(self):
        return self.name