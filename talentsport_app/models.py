from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email,first_name,last_name,phone,city,date_of_born,adress,password, **extra_fields):
        """
        Create and save a user.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, 
                          last_name=last_name, phone=phone,
                          city=city,date_of_born=date_of_born, 
                          adress=adress
                          ,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,first_name,last_name,phone,city,date_of_born,adress,password, **extra_fields):
        """
        Create and save a SuperUser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email,first_name,last_name,phone,city,date_of_born,adress,password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email'), unique=True)
    first_name = models.CharField(
        _('Prénom'), max_length=30, null=True, blank=True)
    last_name = models.CharField(
        _('Nom'), max_length=30, null=True, blank=True)
    phone = models.CharField(_('Téléphone'), max_length=30, null=True, blank=True)
    city = models.CharField(_('Ville'), max_length=30, null=True, blank=True)
    date_of_born = models.DateField(_('Date de naissance'),blank=False,null=False)
    adress = models.TextField(_('Adresse'),blank=False,null=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    is_actif = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone',
                       'city', 'date_of_born','adress']
    
    objects = UserManager()

    def __str__(self):
        return self.email  

"""Discipline sportives"""
class DisciplineSportive(models.Model):
	designation = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
	    return str(self.designation)

"""Publications models"""

class PostCategeory(models.Model):
    designation = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.designation


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    category = models.ForeignKey(PostCategeory, on_delete= models.CASCADE)
    discipline_sportive = models.ForeignKey(DisciplineSportive, on_delete=models.CASCADE, null=True, blank=True)	
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to="images/%Y/%m/%d",null=True, blank=True)
    is_valid = models.BooleanField(default=False, null=True, blank = True)
    videos = models.FileField(upload_to="videos/%Y/%m/%d", null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name= 'likes')
	

    def __str__(self):
     return self.text