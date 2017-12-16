"This is a file with Tests, duh"
from django.utils import timezone
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from blog.models import Post
from blog.models import Travel_group

class PostsTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user('test','test@bla.com','passwd22')
        p = Post.objects.create(author=u,title="test_post",
                            text="this is a test post",created_date=timezone.now())
        p.save()

    def posts_are_postable(self):
        p = Post.objects.get(title='test_post')
        self.assertIsNotNone(p, "Post was created")
        self.assert_(p.publish(), "Posts are publishable")
        self.fail("FAIL")

class LoginTest(TestCase):
    c = Client()
    resp = c.post("/login/",{'username': 'test', 'password':'passwd22'})

# t1 = PostsTestCase()
# t2 = LoginTest()
# t1.run()
# t2.run()
