from django.db import models

# Create your models here.
class Todo_list(models.Model):
    title = models.CharField(max_length=155, verbose_name= 'заголовок')
    description = models.TextField(max_length=155)
    is_completed = models.BooleanField (default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="ту ду лист "
