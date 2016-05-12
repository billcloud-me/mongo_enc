from django.db import models
from mongoengine import *

# Create your models here.
class Nodes(Document):
    node = StringField(max_length=200, required=True)
    classes = ListField(StringField(max_length=200), required=True)
