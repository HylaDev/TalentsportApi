from rest_framework import serializers
from talentsport_app.models import *

# This class is used to serialize the User model
class UserSerializer(serializers.ModelSerializer):
    # This class is used to define the fields of the User model
    class Meta:
        model = User
        fields = ['id','email', 'first_name', 'last_name', 
                  'phone','city','date_of_born','adress','weight',
                  'height','current_club','sex','club_history','profil_pic'
                  ,'level','strong_foot','discipline_sportive','position','password','groups']

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

