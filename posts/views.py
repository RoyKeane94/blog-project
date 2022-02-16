from django.shortcuts import render

from .models import Post

# Create your views here.
def HomeView(request):
    return render(request, "posts/home.html", {
        "posts" : Post.objects.all()
    })

def IndividualPostView(request, id):
    obj = Post.objects.get(id=id)
    return render(request, "posts/individual-post.html", {
        "individual_post" : obj,
    })