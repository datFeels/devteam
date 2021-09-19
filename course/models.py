from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=10, verbose_name="课程名称")
    desc = models.TextField(verbose_name="课程目标")

    def __str__(self):
        return str(self.id)


class Lecture(models.Model):
    lname = models.CharField(max_length=20, verbose_name="课名称", blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    program = models.BooleanField(verbose_name="程序")
    sprites = models.BooleanField(verbose_name="素材")
    plan = models.BooleanField(verbose_name="大纲")
    ppt = models.BooleanField()
    knowledge = models.TextField(blank=True, verbose_name="知识点")
    game = models.BooleanField(verbose_name="教具/游戏")

    def __str__(self):
        return str(self.id)
