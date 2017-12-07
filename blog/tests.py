"This is a file with Tests, duh"
from time import time
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from blog.models import Post
from blog.models import Travel_group

class PostsTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user('test')
        Post(author=u,title="test_post", text="this is a test post",created_date=time())
    def posts_are_postable(self):
        p = Post.objects.get(title='test_post')
        p.publish()


class LoginTest(TestCase):
    c = Client()
    resp = c.post("/login/",{'username': 'test', 'password':'testtest'})
