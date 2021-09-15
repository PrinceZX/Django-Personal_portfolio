from django.shortcuts import render, get_object_or_404
from .forms import CommentForm

from .models import AutoProject
# Create your views here.

def home(request):
    projects = AutoProject.objects.all()
    return render(request, 'project/home.html', {'projects':projects})

def all_projects(request):
    projects = AutoProject.objects.order_by('-date')[:5]
    return render(request, 'project/all_projects.html', {'projects':projects})

def detail(request, project_id):
    project = get_object_or_404(AutoProject, pk=project_id)
    return render(request, 'project/detail.html', {'project':project})
#
#
# def post_detail(request, slug):
#     template_name = 'detail.html'
#     post = get_object_or_404(AutoProject, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})