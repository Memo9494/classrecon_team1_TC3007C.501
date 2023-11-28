from django.db import models
from django.contrib.auth.models import AbstractUser
# from cryptography.fernet import Fernet
# import cv2
import os
# import face_recognition
import time
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(("Description"), blank=True, null=True, help_text=("Description"))
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    semester = models.CharField(max_length=10, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name= 'courses')
    face_encoding = models.CharField(max_length=150, null=True, blank=True)
    photo = models.ImageField(upload_to='static/images/', null=True, blank=True)
    def __str__(self):
        return self.username
    
    # def face_encode(self, photo):
    #     if photo:
    #         #show image
    #         image_ = face_recognition.load_image_file(photo)
            
            
    #         face_locations = face_recognition.face_locations(image_)[0]                                          # Obtiene las coordenadas del rostro en la imagen
    #         face_encoding = face_recognition.face_encodings(image_, known_face_locations=[face_locations])[0]    # Obtenemos las características del rostro encontrado
    #         encoding_str = ",".join(map(str, face_encoding))
    #         return encoding_str
    #     else:
    #         print("No photo")
    #     return None

    # def save(self, *args, **kwargs):
    #     if self.photo:
    #         self.face_encoding = self.face_encode(self.photo)
            
    #     super().save(*args, **kwargs)

    
class Attendance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey('course', on_delete=models.CASCADE)
    date = models.DateField(unique_for_date=True)
    is_attended = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user) + ' ' + str(self.course) + ' ' + str(self.date) + ' ' + str(self.is_attended)
    
class Participation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey('course', on_delete=models.CASCADE)
    date = models.DateField(unique_for_date=True)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user) + ' ' + str(self.course) + ' ' + str(self.date) + ' ' + str(self.amount)
    


