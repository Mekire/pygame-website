from django.shortcuts import render, get_object_or_404

from forums.models import Forum, Thread, Comment

POSTS_PER_PAGE = 20

def viewForums(request):
	# get all the forums, order by date
	context = {'forums':Forum.objects.all().order_by('published')}
	return(render(request, 'forums.html', context))

def viewSingleForum(request, forum_id):
	forum = get_object_or_404(Forum, pk=int(forum_id))
	threads = Thread.objects.filter(forum=forum)
	context = {'forum':forum, 'threads':threads}
	return(render(request, 'single_forum.html', context))

def viewSingleThread(request, thread_id):
	thread = get_object_or_404(Thread, pk=int(thread_id))
	comments = Comment.objects.filter(thread=thread)
	context = {'thread':thread, 'comments':comments}
	return(render(request, 'single_thread.html', context))

def viewThreadPage(request, thread_id, index):
	# view a single page of requests
	pass

def viewComment(request, comment_id):
	comment = get_object_or_404(Comment, int(comment_id))
	return(render(request, 'singe_comment.html', {'comment':comment}))


