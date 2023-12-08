from django.test import TestCase
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.core.files.uploadedfile import SimpleUploadedFile
# from .models import Category, Blog, Profile, Comment
# # Create your tests here.


# class BlogPlatformTests(TestCase):

#     def setUp(self):
#         # Create a test user
#         self.test_user = get_user_model().objects.create_user(
#             email='testuser@example.com',
#             username='testuser',
#             password='testpassword'
#         )
        
#         # Check if a profile already exists for the user
#         self.test_profile = Profile.objects.get_or_create(user=self.test_user)[0]

#         # Create a test category
#         self.test_category = Category.objects.create(title='Test Category')

#         # Create a test blog post
#         self.test_blog_post = Blog.objects.create(
#             title='Test Blog Post',
#             slug='test-blog-post',
#             body='This is a test blog post.',
#             author=Profile.objects.create(user=self.test_user),
#             category=self.test_category,
#         )

#         # Create a test comment
#         self.test_comment = Comment.objects.create(
#             post=self.test_blog_post,
#             author=Profile.objects.create(user=self.test_user),
#             body='Test comment on the blog post.'
#         )

#     def test_user_creation(self):
#         self.assertEqual(get_user_model().objects.count(), 1)
#         self.assertEqual(str(self.test_user), 'testuser@example.com')

#     def test_category_creation(self):
#         self.assertEqual(Category.objects.count(), 1)
#         self.assertEqual(str(self.test_category), 'Test Category')

#     def test_blog_creation(self):
#         self.assertEqual(Blog.objects.count(), 1)
#         self.assertEqual(str(self.test_blog_post), 'Test Blog Post')
#         self.assertEqual(self.test_blog_post.author.user, self.test_user)
#         self.assertEqual(self.test_blog_post.category, self.test_category)

#     def test_profile_creation(self):
#         self.assertEqual(Profile.objects.count(), 2)  # Two profiles are created in the setup
#         self.assertEqual(str(self.test_user.profile), 'testuser')

#     def test_comment_creation(self):
#         self.assertEqual(Comment.objects.count(), 1)
#         self.assertEqual(str(self.test_comment), 'testuser')

#     def test_blog_likes(self):
#         # Test liking a blog post
#         self.test_blog_post.likes.add(self.test_user)
#         self.assertEqual(self.test_blog_post.likes.count(), 1)
#         self.assertTrue(self.test_user in self.test_blog_post.likes.all())

#         # Test unliking a blog post
#         self.test_blog_post.likes.remove(self.test_user)
#         self.assertEqual(self.test_blog_post.likes.count(), 0)
#         self.assertFalse(self.test_user in self.test_blog_post.likes.all())
