from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import Comment
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json
# from django import forms
# Create your views here.

def index(request):
  context = RequestContext(request)
  context_dict={}
  all_messages = []
  all_users = User.objects.all()
  context_dict['all_users'] = all_users
  context_dict['all_messages'] = all_messages
  return render_to_response('home.html', context_dict, context)

def home(request):
  context = RequestContext(request)
  context_dict={}
  return render_to_response('home.html', context_dict, context)

class Users(ListView):
	model = User
	template_name = 'users.html'

	def get_queryset(self):
		return self.model.objects.order_by('-pk')[:25]


def user_page(request,user_id):
    context=RequestContext(request)
    context_dict={}
    other_user_id=user_id

    other_user = User.objects.get(id=other_user_id)
    current_messages = Comment.objects.filter(receiving_user=other_user)
    # print(current_messages)

    context_dict['other_user'] = other_user
    context_dict['current_messages'] = current_messages
    return render_to_response('user_page.html', context_dict, context)

@csrf_exempt
def get_comments(request,user_id):
    print("Calling Get_Comments")
    current_user = request.user
    other_user = User.objects.get(id=user_id)
    # all_messages = Comment.objects.filter(buyer=current_buyer)

		# Here we're getting the "relevant messages" for these users, ie all messages where only these users are involved
    relevant_messages = Comment.objects.filter(Q(sending_user=current_user,receiving_user=other_user) | Q(sending_user=other_user,receiving_user=current_user)).order_by('-created')
    json_messages = []

    if request.POST:
        print("Retrieving new comment ")
        # new_auth = request.POST.get('author')

        sending_user = current_user
        print(sending_user)
        receiving_user = other_user
        print(receiving_user)
        new_text = request.POST.get('text')

        new_comment = Comment(author=current_user.username, sending_user=current_user, receiving_user=receiving_user, text=new_text)
        print(new_comment)
        new_comment.save()

    for e in relevant_messages:
        temp = {}
        temp['id'] = e.id
        temp['author'] = str(e.author)
        temp['sending_user'] = str(e.sending_user)
        temp['receiving_user'] = str(e.receiving_user)
        temp['text'] = str(e.text)
        temptime = e.created.strftime("%a. %b %d, %Y %I:%M %p")
        temp['created'] = str(temptime)
        json_messages.append(temp)
        # print(data) 

    json_data = json.dumps(json_messages)
    return HttpResponse(json_data)


@csrf_exempt
def get_all_comments(request):
    print("Calling ALL Comments")
    current_user = request.user
    relevant_messages = Comment.objects.all()
    json_messages = []


    for e in relevant_messages:
        temp = {}
        temp['id'] = e.id
        temp['author'] = str(e.author)
        temp['sending_user'] = str(e.sending_user)
        temp['receiving_user'] = str(e.receiving_user)
        temp['text'] = str(e.text)
        temptime = e.created.strftime("%a. %b %d, %Y %I:%M %p")
        temp['created'] = str(temptime)
        json_messages.append(temp)
        # print(data) 

    json_data = json.dumps(json_messages)
    return HttpResponse(json_data)
