from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from letterbox.models import Notice

class NoticeTest(TestCase):
    def setUp(self):
        self.joe = User.objects.create(username='joe')
        self.jane = User.objects.create(username='jane')

    def test_for_user(self):
        Notice.objects.create(sender=self.joe,recipient=self.jane,subject="Test",message="This is a test")
        self.assertEqual(1, len(Notice.objects.notices_for(self.jane)))

        self.assertEqual(1,len(Notice.objects.notices_for(self.jane,archived=False)))

    def test_send(self):
        Notice.send(self.jane, self.joe, "Test Message","default.html",{"message":"test"})
        self.assertEqual(1, len(Notice.objects.all()))
        self.assertEqual(1, len(Notice.objects.notices_for(self.joe)))

    def test_send_notice(self):
        Notice.send_notice(self.jane, self.joe, "Test Message","Test Message")
        self.assertEqual(1, len(Notice.objects.all()))
        self.assertEqual(1, len(Notice.objects.notices_for(self.joe)))

    def test_unread_count(self):
        notice = Notice.send_notice(self.jane, self.joe, "Test Message","Test Message")
        self.assertEqual(1, Notice.objects.unread_count_for(self.joe))
        notice.is_read()
        self.assertEqual(0, Notice.objects.unread_count_for(self.joe))

    def test_archived(self):
        notice = Notice.send_notice(self.jane, self.joe, "Test Message","Test Message")
        notice.archive()
        self.assertEqual(len(Notice.objects.archived(self.joe)), 1)
        self.assertEqual(len(Notice.objects.notices_for(self.joe)), 0)



class ViewTests(TestCase):
    def setUp(self):
        self.joe = User.objects.create_user(username='joe',email='joe@acme.com',password='test')
        self.jane = User.objects.create(username='jane', email='jane@acme.com', password='test')
        self.notice = Notice.objects.create(sender=self.joe, recipient=self.jane, subject='Test', message='Test Message')
        self.client.login(username='joe', password='test')

    def test_default(self):
        response = self.client.get('/notices/')
        self.assertIn("notices", response.context)
        self.assertEqual(len(response.context['notices']), 1)
        assert False

    def test_archived(self):
        assert False

    def test_all(self):
        assert False

    def test_unread(self):
        assert False

    def test_archive(self):
        assert False

    def test_detail(self):
        response = self.client.get('/notices/1/')
        pass
