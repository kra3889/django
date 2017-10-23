# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# apps.secret_key = "keepitasecretbozo"
# hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
# print (hash1)
# $2b$12$Wdc2qwiP6u0WdQdKwmer7.DMIcY6q76GxvrJgaodnpRDmpP8mwkDa
# Create your models here.

class RegManager(models.Manager):
    def Reg_validator(self, post_data):
        errors = []
        if len(post_data['first_name']) < 2:
            errors.append("first name should be at least 2 characters")
        if len(post_data['last_name']) < 2:
            errors.append("last name should be at least 2 characters")
        if len(Reg.objects.filter(email=post_data['email'])) > 0:
            errors.append("email already in use")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        if post_data['password'] != post_data['passconf']:
            errors.append("passwords do not match")

        print ("***********  errors", errors)
        if not errors:
            hash1 = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            password = hash1
            print (hash1)
            new_register = self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                email=post_data['email'],
                password=hash1
            )
            # print ("added registerer")
            return new_register
        return errors

    def login_validator(self, post_data):
            errors = []
            # check DB for post_data['email']
            if len(self.filter(email=post_data['email'])) > 0:
                # check this Reg's password
                Reg = self.filter(email=post_data['email'])[0]
                # print (Reg)
                # print (Reg.password.encode())
                # print (post_data['password'].encode())
                if not bcrypt.checkpw(post_data['password'].encode(), Reg.password.encode()):
                    errors.append('email/password incorrect - 1')
            else:
                    errors.append('email/password incorrect - 2')

            if errors:
                return errors
            return Reg


class Reg(models.Model):
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        email = models.CharField(max_length=255)
        password = models.CharField(max_length=255)
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)
        objects = RegManager()
        def __str__(self):
           return self.email


# models come with a hidden key:
#       objects = models.Manager()
# we are going to overwrite this!
# """
# Create your models here.
# bcrypt.checkpw('test'.encode(), hash1)
