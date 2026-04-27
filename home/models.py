from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.course_name