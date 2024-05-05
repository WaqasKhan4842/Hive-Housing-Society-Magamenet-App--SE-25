from django.shortcuts import render,redirect,get_object_or_404
from collections import defaultdict
from django.utils import timezone
from .models import Post,Comment
from Account.models import User
from Resident.models import Resident
from Building.models import Society
# Create your views here.


from collections import defaultdict

def society_forum(request):
    user = User.objects.get(user_name=request.session.get('user_name'))
    resident = Resident.objects.get(user_name=user)
    society = Society.objects.get(building_id=resident.building.building_id)
    society_name = society.society_name
    
    # Count all residents living in the society
    residents_count = Resident.objects.filter(building__society_name=society_name).count()
    
    # Get posts associated with the current society
    society_posts = Post.objects.filter(society=society)
    
    # Create a dictionary to store comments associated with each post
    post_comments = defaultdict(list)
    
    # Get comments associated with each post and store in the dictionary
    for post in society_posts:
        comments = Comment.objects.filter(post=post)
        post_comments[post.post_id] = comments
    
    context = {
        'society_name': society_name,
        'resident_count': residents_count,
        'society_posts': society_posts,
        'post_comments': post_comments,  # Add the dictionary to the context
    }
    return render(request, 'society_forum.html', context)



def submit_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = User.objects.get(user_name=request.session.get('user_name'))
        resident = Resident.objects.get(user_name=user)
        society = Society.objects.get(building_id=resident.building.building_id)
        
        # Set the current date and time
        current_date = timezone.now().date()

        # Create a new post object
        new_post = Post(content=content, user=user, society=society, date_posted=current_date)
        new_post.save()

        # Redirect to the forum page or any other page you want
        return redirect('society_forum')

    # If the request method is not POST, render a form or any other page
    return render(request, 'submit_post.html')


def submit_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        username = User.objects.get(user_name=request.session.get('user_name'))
        
        # Retrieve the post object using post_id
        post = get_object_or_404(Post, pk=post_id)
        
        # Create a new comment object
        new_comment = Comment(content=content, username=username, post=post)
        new_comment.save()

        # Redirect to the same page or any other page you want
        return redirect('society_forum')

    # Handle GET requests or any other cases
    return redirect('society_forum')