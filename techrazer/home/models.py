from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True , blank=True)

    def __str__(self):
        return 'Message From : ' + self.name +', Email : ' + self.email


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    choices = Categorie.objects.all().values_list('name','name')
    choice_list = []
    for item in choices:
        choice_list.append(item)    

    category = models.CharField(default='',max_length=255,choices=choice_list)
    author = models.CharField(max_length=20)
    views = models.IntegerField(default = 0)
    slug = models.CharField(max_length=200)
    image = models.ImageField( upload_to="",default = "")
    timestamp = models.DateTimeField(blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def __str__(self):
        return self.title +' by ' + self.author

