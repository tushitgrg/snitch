from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import snitch, User, Message, Topics


class snitchform(ModelForm):

  class Meta:
    model = snitch
    fields = '__all__'
    exclude = ['replies']


class messageform(ModelForm):

  class Meta:
    model = Message
    fields = '__all__'


class topicform(ModelForm):

  class Meta:
    model = Topics
    fields = '__all__'
