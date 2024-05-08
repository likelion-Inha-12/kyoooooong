from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)  # null=True 추가
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=200, null=True, blank=True)
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name="comments")
    member_id = models.ForeignKey(Member, verbose_name="Member", on_delete=models.CASCADE, related_name="comments", null=True) #null=True

    def __str__(self):
        return self.content
    
    

class UserPost(models.Model):
    user_id = models.ForeignKey(Member, verbose_name="user", on_delete=models.CASCADE, related_name='liked_posts')  
    post_id = models.ForeignKey(Post, verbose_name="post", on_delete=models.CASCADE, related_name='likers')  
    