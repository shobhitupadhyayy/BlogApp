from django.db import models
from Home.models import blogTitle

# Create your models here.
class createBlog(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    blogTitle=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.blogTitle}"
    
class AddTaskForm(models.ModelForm):

    blog = models.CharField(max_length = 1000,
                            widget = models.TextInput(
                                attrs = {
                                    'class' : 'form-control',
                                    'placeholder' : 'Enter Your Blog', 
                                }
                            )
                        )

    class Meta:
        model = blogTitle
        fields = '__all_'
