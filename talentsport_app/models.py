from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin,Group
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.utils import timezone

# Create your models here.
#Discipline sportives model
"""
This model stores the different disciplines sportives.
"""
class DisciplineSportive(models.Model):
	designation = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
	    return str(self.designation)

# Player Position model
"""
This model stores the different player position.
"""
class PlayerPosition(models.Model):
    designation = models.CharField(max_length=255)
    description = models.TextField()
    discipline_sportive = models.ForeignKey(DisciplineSportive,on_delete= models.SET_NULL,verbose_name="Discipline Sportive",null=True, blank=False)

    def __str__(self):
        return str(self.designation)
        

#Custom user model manager where email is the unique identifiers
#for authentication instead of usernames.
class UserManager(BaseUserManager):
    """
    Create and save a user with the given email, first_name, last_name, phone, city, date_of_born, adress and password.
    """
    def create_user(self, email,first_name,last_name,phone,city,
                    date_of_born,adress,weight,height,current_club,club_history,
                    profil_pic,sex,level,strong_foot,discipline_sportive,position,
                    joined_date,groups,followers,password, **extra_fields):
        """
        Create and save a user.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, 
                         last_name=last_name, phone=phone,
                         city=city,date_of_born=date_of_born, 
                         adress=adress,weight=weight,height=height,
                         current_club=current_club,club_history=club_history,
                         profil_pic=profil_pic,sex=sex,level=level,strong_foot=strong_foot,
                         discipline_sportive=discipline_sportive,position=position,joined_date=joined_date,groups=groups,**extra_fields)
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

#User model class
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email'), unique=True,null=False, blank=False)
    first_name = models.CharField(
        _('Prénom'), max_length=30, null=True, blank=True)
    last_name = models.CharField(
        _('Nom'), max_length=30, null=True, blank=True)
    phone = models.CharField(_('Téléphone'), max_length=30, null=True, blank=True)
    country = models.CharField(_('Country'), max_length=50, null=True, blank=True)
    city = models.CharField(_('Ville'), max_length=30, null=True, blank=True)
    date_of_born = models.DateField(_('Date de naissance'),blank=True,null=True)
    adress = models.TextField(_('Adresse'),blank=True,null=True)
    weight = models.CharField(_('Poids'),max_length=20,blank=True,null=True)
    height = models.CharField(_('Taille'),max_length=20,blank=True,null=True)
    current_club = models.TextField(_('Club Actuel'),blank=True,null=True)
    club_history = models.TextField(_('Historique de club'),blank=True,null=True)
    profil_pic = models.ImageField(_('Profil'),upload_to='images/profil_pic%Y/%m/%d',blank=True,null=True)
    followers = models.ManyToManyField('self',symmetrical=False, blank=True, verbose_name='Abonnés') 
    class Sex(models.TextChoices):
        F = 'F', _('Féminin')
        M = 'M', _('Masculin')
    sex = models.CharField(_('Sexe'),max_length=15, blank=True, null=True, choices=Sex.choices)

    class Level(models.TextChoices):
        DEBUTANT = 'DEBUTANT', _('Débutant')
        INTERMEDIAIRE = 'INTERMEDIAIRE', _('Intermédiaire')
        PASSIONNER = 'PASSIONNER', _('Passioner')
        PROFESSIONNEL = 'PROFESSIONNEL', _('Professionnel')
    level = models.CharField(_('Niveau'),max_length=15, blank=True, null=True, choices=Level.choices)

    class Strong_foot(models.TextChoices):
        GAUCHE = 'GAUCHE', _('Gauche')
        DROIT = 'DROIT', _('Droit')

    strong_foot = models.CharField(_('Pied Fort'),max_length=15, blank=True, null=True, choices=Strong_foot.choices)
    discipline_sportive = models.ForeignKey(DisciplineSportive, on_delete=models.SET_NULL, verbose_name='Discipline Sportive', null=True, blank=False)
    position = models.ForeignKey(PlayerPosition, on_delete=models.SET_NULL,verbose_name='Poste', null=True, blank=False)
    groups = models.ForeignKey(Group,on_delete=models.SET_NULL,verbose_name='Groupe',null=True, blank=True)
    joined_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    is_actif = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone',
                       'city', 'date_of_born','adress']
    
    objects = UserManager()

    def __str__(self):
        return self.email  

#Publications models
"""
This model stores the different categories of posts.
"""
class PostCategeory(models.Model):
    designation = models.CharField(_('Désignation'),max_length=30)
    description = models.TextField(_('Description'))

    def __str__(self):
        return self.designation

"""
This model stores the different posts.
"""
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Utilisateur")
    text = models.TextField(_('Texte'))
    category = models.ForeignKey(PostCategeory,on_delete= models.CASCADE,verbose_name="Catégorie",null=False, blank=False)
    discipline_sportive = models.ForeignKey(DisciplineSportive, on_delete=models.CASCADE, null=False, blank=False,verbose_name="Discipline Sportive")	
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(_('Photos'),upload_to="images/%Y/%m/%d",null=True, blank=True)
    is_valid = models.BooleanField(_('Valide'),default=False, null=True, blank = True)
    videos = models.FileField(_('Vidéos'),upload_to="videos/%Y/%m/%d", null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name= 'likes')
    update_date = models.DateTimeField(_('Date mise à jour'),default=timezone.now,blank=True, null=True)
	

    def __str__(self):
     return self.text
    

class Challenges(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Utilisateur")
    discipline_sportive = models.ForeignKey(DisciplineSportive, on_delete=models.CASCADE, null=False, blank=False,verbose_name="Discipline Sportive")	
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(_('Photos'),upload_to="images/%Y/%m/%d",null=True, blank=True)
    is_valid = models.BooleanField(_('Valide'),default=False, null=True, blank = True)
    videos = models.FileField(_('Vidéos'),upload_to="videos/%Y/%m/%d", null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name= 'chanllenge_like')
    update_date = models.DateTimeField(_('Date mise à jour'),default=timezone.now,blank=True, null=True)
	


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, on_delete = models.CASCADE, null=True)
	comment_date = models.DateTimeField(auto_now_add=True)
	comment = models.TextField()
	likes = models.ManyToManyField(User, related_name='commentaire_like', blank=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="+")

	@property
	def children(self):
		return Comment.objects.filter(parent=self).order_by('-comment_date').all()


	@property
	def is_parent(self):
		if self.parent is None:
			return True
		return False


"""
This model stores the different notifications 
"""
class Notification(models.Model):
    # 1 = Like 2 = comment  3 = Followers
	type = models.IntegerField()
	send_from = models.ForeignKey(User, on_delete = models.CASCADE, null=True,blank=True, related_name="Expéditeur")
	send_to = models.ForeignKey(User, on_delete = models.CASCADE, null=True,blank=True, related_name="Destinataire") 
	post = models.ForeignKey(Posts, on_delete = models.CASCADE,blank=True, null=True, related_name="+")
	comment = models.ForeignKey(Comment, on_delete = models.CASCADE,blank=True, null = True, related_name="+")
	send_date = models.DateTimeField(auto_now_add=True)
	is_open = models.BooleanField(default=False)
    