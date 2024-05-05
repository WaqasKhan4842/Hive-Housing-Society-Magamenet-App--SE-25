from django.db import models
from Account.models import User
from Building.models import Society

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    society =models.ForeignKey(Society, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.post_id} by {self.user.user_name} at {self.date_posted}"
    

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    username = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.comment_id} by {self.username.username} on Post {self.post.post_id} at {self.date}"