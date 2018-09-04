from django.shortcuts import render,HttpResponse,redirect
from blogger.models import BlogPost,Comment

# Create your views here.
def home(request):
	posts = BlogPost.objects.all()
	# print(posts)
	# print(type(posts))
	for post in posts:
		print (post)
	return render(request, 'home.html', {"posts":posts})


# def hello(request):
# 	return render(request, "hello.html")

def post_page(request, post_id):
	mypost = BlogPost.objects.get(pk=post_id)
	comments = Comment.objects.filter(post =mypost)
	context = {"post":mypost,"comments":comments}
	return render (request, "post.html",context)

def create_comment(request, post_id):
	comment_txt = request.POST.get('comment')
	user = request.user
	post = BlogPost.objects.get(pk=post_id)
	comment = Comment(post=post, text=comment_txt, user=user)
	comment.save()
	return redirect(f"/post/{post_id}")
def publish(request):
	if request.method=="POST":
		title = request.POST.get('title')
		body =request.POST.get('body')
		publish = BlogPost(title=title,body=body)
		publish.save()
		return redirect(f"/")
	return render(request, "publish.html")
