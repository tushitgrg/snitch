from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Topics
from .models import snitch
from .models import Message, imageuser
from .forms import snitchform, messageform, topicform
import re
import random
from django.contrib.auth import login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
  if request.GET.get('query') != None:
    query = request.GET.get('query')
    allsnitch = snitch.objects.filter(
        Q(Title__icontains=query) or Q(snitchtext__Text__icontains=query)
        or Q(snitchtext__author__username__icontains=query))
  else:
    allsnitch = snitch.objects.all()
  alltopics = Topics.objects.all()

  allmessage = Message.objects.all()
  context = {
      'topics': alltopics,
      'snitches': allsnitch,
      'messagess': allmessage,
  }

  return render(request, 'projectApp/index.html', context)


@login_required(login_url="loginn")
def addsnitch(request):
  if request.method == 'POST':
    sform = snitchform()
    mform = messageform()

    title = request.POST.get('title')

    content = request.POST.get('snitchtext')
    hashtags = re.findall(r"#(\w+)", content)
    messagee = Message.objects.create(author=request.user,
                                      Text=content,
                                      is_reply="false")
    snitchee = snitch.objects.create(Title=title, snitchtext=messagee)
    topics = snitchee.topics.all()

    if len(hashtags) != 0:
      for hashtag in hashtags:
        tform = topicform()
        topic1 = Topics.objects.get_or_create(name=hashtag)
        topic1 = Topics.objects.get(name=hashtag)
        snitchee.topics.add(topic1)
    return redirect('home')

  return render(request, 'projectApp/add-snitch.html')


def topics(request):

  alltopics = Topics.objects.all()
  allsnitch = snitch.objects.all()
  context = {
      'topics': alltopics,
      'snitches': allsnitch,
  }
  for topic in alltopics:
    for snitchi in topic.topics.all():
      print(snitchi.Title)

  return render(request, 'projectApp/topics.html', context)


def topicc(request, pk):
  try:
    topicselect = Topics.objects.get(id=int(pk))
    allsnitch = topicselect.topics.all()
    alltopics = Topics.objects.all()

    allmessage = Message.objects.all()
    context = {
        'topics': alltopics,
        'snitches': allsnitch,
        'messages': allmessage
    }

    return render(request, 'projectApp/index.html', context)
  except:
    return redirect('home')


def snitchh(request, sk):
  snitchselect = snitch.objects.get(id=int(sk))
  allsnitch = snitch.objects.all()
  if request.method == 'POST':
    if not request.user.is_authenticated:
      return redirect('loginn')
    else:
      replyy = Message.objects.create(author=request.user,
                                      Text=request.POST.get('replytxt'))

      snitchselect.replies.add(replyy)

  context = {
      'snitchh': snitchselect,
      'snitches': allsnitch,
  }
  return render(request, 'projectApp/snitch.html', context)


@login_required(login_url="loginn")
def upvote(request, sk, link):
  snitchselect = Message.objects.get(id=int(sk))
  if request.user not in snitchselect.upvotedusers.all():

    snitchselect.upvotes = str(int(snitchselect.upvotes) + 1)
    snitchselect.upvotedusers.add(request.user)
    snitchselect.save()
  if request.user in snitchselect.downvotedusers.all():
    snitchselect.downvotes = str(int(snitchselect.downvotes) - 1)
    snitchselect.downvotedusers.remove(request.user)
    snitchselect.save()
  if "index" in link:
    return redirect('home')

  else:
    return redirect('/snitchh/' + link)


@login_required(login_url="loginn")
def downvote(request, sk, link):
  snitchselect = Message.objects.get(id=int(sk))
  if request.user not in snitchselect.downvotedusers.all():
    snitchselect.downvotes = str(int(snitchselect.downvotes) + 1)
    snitchselect.downvotedusers.add(request.user)
    snitchselect.save()
  if request.user in snitchselect.upvotedusers.all():
    snitchselect.upvotes = str(int(snitchselect.upvotes) - 1)
    snitchselect.upvotedusers.remove(request.user)
    snitchselect.save()
  if "index" in link:
    return redirect('home')

  else:
    return redirect('/snitchh/' + link)


def loginn(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':

      email = request.POST.get('email')
      password = request.POST.get('password')
      if len(User.objects.filter(email=email)) == 0:
        first_names = [
            "Aurora", "Phoenix", "Zephyr", "Luna", "Orion", "Nova", "Kai",
            "Seraphina", "Atlas", "Lyra", "Xander", "Ember", "Kairos", "Azura",
            "Rune", "Avalon", "Cassius", "Esme", "Orion", "Aria", "Jaxon",
            "Freya", "Orion", "Soren", "Thalia", "Xena", "Kairos", "Nova",
            "Dax", "Indigo", "Seraphim", "Vega", "Rhea", "Caelum", "Nyx",
            "Kairos", "Astrid", "Dante", "Lyric", "Zara", "Phoenix", "Orion",
            "Lysander", "Nova", "Selene", "Ajax", "Azura", "Ember", "Nyx",
            "Orion", "Kai", "Luna", "Thorne", "Nova", "Aurora", "Phoenix",
            "Orion", "Zephyr", "Seraphina", "Kairos", "Aria", "Azura", "Orion",
            "Freya", "Xander", "Ember", "Kairos", "Cassius", "Nova", "Lyra",
            "Soren", "Xena", "Thalia", "Kairos", "Avalon", "Esme", "Orion",
            "Rune", "Jaxon", "Aurora", "Seraphina", "Nyx", "Kai", "Vega",
            "Ember", "Astrid", "Phoenix", "Orion", "Kairos", "Dante", "Zara",
            "Nova", "Lyric", "Orion", "Thorne", "Selene", "Azura", "Ember",
            "Kairos", "Orion"
        ]

        last_names = [
            "Everhart", "Blackwood", "Nightingale", "Frost", "Stormborn",
            "Silvermoon", "Steelheart", "Wintersong", "Shadowcaster",
            "Firebrand", "Ironwood", "Starfury", "Brightblade", "Wilder",
            "Darkbane", "Shadowthorn", "Frostborn", "Lightbringer",
            "Moonshadow", "Emberfall", "Stormbreaker", "Swiftwind",
            "Thornbrook", "Skywatcher", "Frostfire", "Dawnstrider",
            "Blackthorn", "Flameheart", "Stormrider", "Silverglade",
            "Shadowstalker", "Frostwind", "Darkthorn", "Emberheart",
            "Nightshade", "Shadowfang", "Firestorm", "Silverthorn",
            "Winterblade", "Starfrost", "Stormcloud", "Brightwood",
            "Swiftblade", "Ironbane", "Nightfall", "Dawnblade", "Frostglade",
            "Darkblade", "Shadowbrook", "Emberstorm", "Moonshade",
            "Silverbrook", "Frostshade", "Stormforge", "Nightwatcher",
            "Emberflame", "Darkheart", "Shadowfire", "Frostbrook", "Stormsong",
            "Moonwind", "Brightbane", "Silverfire", "Emberbrook", "Darkfury",
            "Shadowfall", "Frostthorn", "Starshadow", "Nightbringer",
            "Stormlight", "Emberwood", "Darkwatcher", "Frostflame",
            "Silverdawn", "Shadowblade", "Emberglade", "Stormborn",
            "Brightflame", "Nightblade", "Frostwatcher", "Shadowdawn",
            "Starstrike", "Moonfire", "Emberstrike", "Darkglade",
            "Frostcaster", "Shadowflame", "Firewatcher", "Stormflame",
            "Brightstorm", "Nightglade", "Silvermoon", "Shadowfrost",
            "Emberlight", "Frostfire", "Stormbinder", "Darkfire",
            "Silverblade", "Emberbreeze", "Nightshade"
        ]
        usernamefound = False
        Username = "1"
        while not usernamefound:
          firstname = random.choice(first_names)
          lastname = random.choice(last_names)
          Username = firstname + lastname
          if len(User.objects.filter(username=Username)) == 0:
            usernamefound = True
        user1 = User.objects.create(username=Username,
                                    password=password,
                                    email=email,
                                    first_name=firstname,
                                    last_name=lastname)

        imageuser.objects.create(
            relation=user1,
            imageurl=f"https://api.multiavatar.com/{Username}.svg")
        login(request, user1)
        return redirect('home')
      else:
        user1 = User.objects.get(email=email)
        if user1.password == password:
          login(request, user1)
          return redirect('home')
    return render(request, 'projectApp/login.html')
  else:
    return redirect('home')


def logoutt(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('home')
  else:
    return redirect('loginn')
