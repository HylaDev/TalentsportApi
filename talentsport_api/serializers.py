from rest_framework import serializers
from talentsport_app.models import *

# This class is used to serialize the User model
class UserSerializer(serializers.ModelSerializer):
    # This class is used to define the fields of the User model
    class Meta:
        model = User
        fields = ['id',
                  'email', 
                  'first_name', 
                  'last_name', 
                  'phone',
                  'city',
                  'date_of_born',
                  'adress',
                  'weight',
                  'height',
                  'current_club',
                  'sex',
                  'club_history',
                  'joined_date',
                  'update_date',
                  'profil_pic'
                  ,'level',
                  'strong_foot',
                  'discipline_sportive',
                  'position',
                  'password',
                  'groups',
                  'followers']
        extra_kwargs = {'password': {'write_only': True},
                        }

    def create(self, validated_data):
        user_lname = validated_data.get("last_name")
        user_fname = validated_data.get("first_name")
        user_phone = validated_data.get('phone')
        user_adress = validated_data.get('adress')
        user_email = validated_data.get('email')
        user_phone = validated_data.get('phone')
        user_weight = validated_data.get('weight')
        user_height = validated_data.get('height')
        user_current_club = validated_data.get('current_club')
        user_city = validated_data.get('city')
        user_pwd = validated_data.get('password')
        user_sex = validated_data.get('sex')
        user_club_history = validated_data.get('club_history ')
        user_profil_pic = validated_data.get('profil_pic ')
        user_level = validated_data.get('level')
        user_strong_foot = validated_data.get('strong_foot')
        user_discipline_sportive = validated_data.get('discipline_sportive')
        user_position = validated_data.get('position')
        user_grp = validated_data.get('groups')
        user_date = validated_data.get('date_of_born')
        user_joined_date = validated_data.get('joined_date')
        user_followers = validated_data.get('followers')
        

        user = User.objects.create_user(user_email, user_fname, user_lname, user_phone,
                                        user_city, user_date, user_adress, user_weight, user_height, user_current_club,
                                        user_club_history, user_profil_pic, user_sex,user_level, user_strong_foot,
                                        user_discipline_sportive,user_position,user_joined_date,user_grp,user_followers,user_pwd)
        user.followers.set(user_followers)
        user.save()
        return user
        

# This class is used to serialize the Posts model
class PostsSerializers(serializers.ModelSerializer):

    """# This field is used to get the user's email from the slug_field
    user = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='email'
    )

    # This field is used to get the category's designation from the slug_field
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='designation'
    )
    
    # This field is used to get the discipline sportive's designation from the slug_field
    discipline_sportive = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='designation'
    )"""
    
    # This class is used to define the fields of the Posts model
    class Meta:
        model = Posts
        fields = ['id','user', 'text', 'category', 'discipline_sportive','date','images','is_valid','videos','likes']

# This class is used to serialize the Posts model
class PostsByIdSerializers(serializers.ModelSerializer):

    # This field is used to get the user's email from the slug_field
    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='email'
    )

    # This field is used to get the category's designation from the slug_field
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='designation'
    )
    
    # This field is used to get the discipline sportive's designation from the slug_field
    discipline_sportive = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='designation'
    )
    
    # This class is used to define the fields of the Posts model
    class Meta:
        model = Posts
        fields = ['id','user', 'text', 'category', 'discipline_sportive','date','images','is_valid','videos','likes','update_date']

# This class serializes the PostCategeory model 
class PostCategeorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PostCategeory
        fields = ['designation','description']

# This class serializes the DisciplineSportive model 
class DisciplineSportiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = DisciplineSportive
        fields = ['designation','description']

class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields =['type','send_from','send_to','send_date','comment','post','is_open']

