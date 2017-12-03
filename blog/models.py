from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Travel_group(models.Model):
	group_name = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.group_name
	def publish(self):
		self.save()
	
	class Meta:
		ordering = ('group_name',)
	

	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	travel_groups = models.ManyToManyField(Travel_group)

	
@receiver(post_save, sender=User) #декоратор для обновления
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)#автоматически обновляться
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()