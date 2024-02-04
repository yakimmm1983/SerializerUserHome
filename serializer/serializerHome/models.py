from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    def __init__(self,name,login,password,email):
        self.name = name
        self.login = login
        self.password = password
        self.email = email

