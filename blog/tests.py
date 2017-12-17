"This is a file with Tests, duh"
from django.utils import timezone
from django.urls import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.utils import log
from blog.models import Post
from blog.models import Travel_group
import re

logger = log.logging.getLogger(__name__)

class PostsTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user('test','test@bla.com','passwd22')
        p = Post.objects.create(author=u,title="test_post",
                            text="this is a test post",created_date=timezone.now())
        p.save()

    def test_posts_are_postable(self):
        p = Post.objects.get(title='test_post')
        self.assertIsNotNone(p, "Post was created")
        res = p.publish()
        p.save()

    def test_post_is_editable(self):
        c = Client()
        c.post("/login/",{'username': 'test', 'password':'passwd22'})
        p = Post.objects.get(title='test_post')
        resp = c.get(reverse("post_edit",args=[p.pk]))
        self.assertEquals(resp.status_code, 200, "Post is posted")
        # logger.info ("response %{}",resp)

class LoginTest(TestCase):
    def test_login(self):
        c = Client()
        resp = c.post("/login/",{'username': 'test', 'password':'passwd22'})
        self.assertEquals(resp.status_code,200, "login with correct credentials is possible")


# t1 = PostsTestCase()
# t2 = LoginTest()
# t1.run()
# t2.run()
