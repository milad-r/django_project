from django.shortcuts import render 
from . import models
from django.views import generic
from django.shortcuts import render
class Index(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = models.Post.objects.all().count()
        context['authors'] = models.Writer.objects.all().count()

        return context



class PostListView(generic.ListView):
    model = models.Post
    template_name = 'post_list.html'
    

class WriterListView(generic.ListView):
    model         = models.Writer
    template_name = 'writer_list.html'


class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'post_detail.html'

def User_profile_view(request):
    user_name = models.User_profile.user_name
    firstname = models.User_profile.user_first_name
    lastname  = models.User_profile.user_last_name

    return render(request , '../templates/registration/profile.html' ,{'user_name':user_name , 'firstname':firstname , 'lastname':lastname})