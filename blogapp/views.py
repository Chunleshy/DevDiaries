# Import the required modules and models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q
from django.utils.text import slugify
from django.contrib import messages
from .models import Blog, Profile, Comment, Category
from .forms import RegisterForm, ProfileForm, PostForm, CommentForm

# View for displaying the list of all blogs on the index page

# Define a view function to handle the rendering of the index page.
def index(request):
    # Retrieve the 'search' parameter from the GET request
    keyword = request.GET.get("search")
    msg = ""  # Initialize an empty message variable for search results

    # Check if a search keyword exists
    if keyword:
        # If a keyword exists, filter blog objects based on the keyword and publish status
        blogs = Blog.objects.filter(
            Q(title__icontains=keyword) | Q(category__title__icontains=keyword) |
            Q(body__icontains=keyword) & Q(published=True)
        )
        
        # If blogs match the search no action, but if not set a message indicating no results found
        if  blogs.exists():
            pass
        else:
            msg = "There is no article with that keyword"
    else:
        # If no search keyword provided, retrieve all published blogs
        blogs = Blog.objects.filter(published=True)

    


    # Retrieve all categories available in the system
    categories = Category.objects.all()

# Prepare context data containing blogs, categories, and search message
    context = {"blogs": blogs, "categories": categories, "msg": msg}

# Render the 'index.html' template with the context data
    return render(request, "blogapp/index.html", context)


# View for displaying the details of a specific blog
def detail(request, pk, slug):

    blog = get_object_or_404(Blog, pk=pk, slug=slug) #Get a blog object by their primary key
    # filter other blogs of the same category exclude the current blog
    related_blogs = Blog.objects.filter(category__title = blog.category.title).exclude(id=blog.id)
    if request.user.is_authenticated:
        author = Profile.objects.get(user=request.user)
        if blog.likes.filter(id=request.user.id).exists():
            like = "yes" # When a user likes the blog
            
        else:
            like=""  # User has not yet like the blog
    
    else:
        like="" # if the user has not logged, like should be an empty string
    
    like_count = blog.likes.count() # The number of likes the blog has
            
    comments = Comment.objects.filter(post=blog)
    form = CommentForm() # makes the form visible
    if request.method == 'POST':
        if request.POST.get("comment"):
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = blog  # The blog you are commenting under
                comment.author = author  # the person that makes comment
                comment.save()
                messages.success(request, "Comment added successfully!")
                return redirect("detail", pk=blog.id, slug=blog.slug)
        
        
        else:
            # Check if user has logged in
            if request.user.is_authenticated:
                # Check if user has liked the blog before
                if blog.likes.filter(id=request.user.id).exists(): 
                    #Enable the use to unlike the blog
                    blog.likes.remove(request.user) 
                else:
                    # Enable the user to like the blog
                    blog.likes.add(request.user) 
            else:
                # Direct user to login page if the user has not logged in
                return redirect("signin") 
            
            return redirect("detail", pk=blog.id, slug=blog.slug)
            
    print(like)
    context = {"blog": blog, "form": form, "blogs": related_blogs,"comments": comments, "like_count": like_count, "like": like} 
    return render(request, "blogapp/detail.html", context)



# View for user signup
def signup(request):
    # Initialize an empty RegisterForm
    form = RegisterForm() # render the form on the page
    
    # Check if the HTTP request method is POST
    if request.method == 'POST':
        # If the method is POST, populate the form with the submitted data
        form = RegisterForm(request.POST)
        
        # Check if the submitted form data is valid
        if form.is_valid():
            # If the form is valid, save the form data to create a new user account
            form.save()
            
            # Display a success message indicating the successful account creation
            messages.success(request, "Account created successfully")
            
            # Redirect the user to the 'signin' page after successful signup
            return redirect("signin")
    
    # Prepare context data to render the signup.html page with the form
    context = {"form": form}
    
    # Render the signup.html page with the form and context data
    return render(request, "blogapp/signup.html", context)

# View for user login
def signin(request):
    # Get the group called authenticated
    auth_group = Group.objects.get(name='Authenticated')
    # Check if the HTTP request method is POST
    if request.method == 'POST':
        # Retrieve the email and password from the POST request data
        email = request.POST["email"]
        password = request.POST["password"]
        
        # Authenticate the user using the provided email and password done by  abstraction in Django
        user = authenticate(request, email=email, password=password) 
        
        # Check if the authentication was successful
        if user is not None:
            # Add the login user to authenticated group
            user.groups.add(auth_group)
            # If authentication succeeds, log in the user
            login(request, user)
            
            # Redirect the user to the 'index' page upon successful login
            return redirect("index")
        else:
            # If authentication fails, display a warning message about invalid credentials
            messages.warning(request, "Invalid Credentials")

    # Render the 'signin.html' page when the request method is not POST or if authentication fails
    return render(request, "blogapp/signin.html")


# View for user logout
def signout(request):
    # Log out the user and redirect to the index page
    logout(request)
    return redirect("index")

@login_required(login_url='signin')
def update_profile(request):
    # Fetch the profile associated with the currently logged-in user
    # Get a profile that belong to logged in user
    profile = Profile.objects.get(user=request.user) 
    
    # Initialize a ProfileForm instance with the current profile details
    # Fetch the current profile to be updated
    form = ProfileForm(instance=profile) 
    # Get newbies group
    newbie_group = Group.objects.get(name='Newbies')
    # Get professional group
    professional_group = Group.objects.get(name='Professionals')
    # Check if the HTTP request method is POST
    if request.method == 'POST':
        # If the method is POST, populate the form with the submitted data and files
        # Handles all the data in the form
        form = ProfileForm(request.POST, request.FILES, instance=profile) 
        
        # Check if the submitted form data is valid
        if form.is_valid():
            # If the form is valid, update the profile
            if int(request.POST['years_of_experience']) > 2:
                # Save the information temporarily
                profile = form.save(commit=False) 
                # Set proficiency to True if years of experience greater than 2
                profile.proficiency = True 
                # Add the user that has that profile to the professional group if the years of experince is greater than 2 
                request.user.groups.add(professional_group) 
            
            else:
                # Add the user to newbies group if the user years of experince is less than 3 
                request.user.groups.add(newbie_group)
            # Save the updated profile
            profile.save() 
            
            # Display a success message indicating the successful profile update
            messages.success(request, "Profile updated successfully")
            
            # Redirect the user to their profile page after updating the profile
            return redirect("profile")
    
    # Prepare context data to render the profile_update.html page with the form
    context = {"form": form} # Context variable is used prepare the data to be sent to the template for redering
    
    # Render the profile_update.html page with the form and context data
    return render(request, "blogapp/profile_update.html", context)



# Ensures the user must be logged in to access this view; redirects to 'signin' page if not authenticated
@login_required(login_url='signin')
def profile(request):
    # Fetching the profile associated with the currently logged-in user
    profile = Profile.objects.get(user=request.user)
    
    # Retrieving all blog posts authored by the logged-in user's profile
    posts = Blog.objects.filter(author=profile)
    
    # Context data to render the profile.html page with user profile details and their posts
    context = {"profile": profile, "posts": posts}
    
    # Rendering the profile.html page with the context data
    return render(request, "blogapp/profile.html", context)


def view_user_profile(request, pk):
    # Fetching the profile using the provided ID (pk)
    profile = Profile.objects.get(id=pk)
    
    # Retrieving all blog posts associated with the fetched profile
    posts = Blog.objects.filter(author=profile)
    
    # Initializing flags for follow status and checking if the user is following this profile
    follow = "yes"  # Initialized with a string value, might need modification
    following = False  # Defaulting to False
    
    # Checking if the user is authenticated
    if request.user.is_authenticated:
        # Checking if the currently logged-in user follows the profile being viewed
        if profile.follow.filter(id=request.user.id).exists():
            following = True  # Indicates that the user is following this profile
        else:
            following = False  # Indicates that the user is not following this profile
    else:
        follow = ""  # Setting to an empty string when the user is not authenticated
    
    # Handling follow/unfollow action via POST request
    if request.method == 'POST':
        if profile.follow.filter(id=request.user.id).exists():
            profile.follow.remove(request.user)  # Unfollow the profile
        else:
            profile.follow.add(request.user)  # Follow the profile
    
    # Counting the total number of followers for this profile
    follow_count = profile.follow.count()
    
    # Printing the 'following' status (could be for debugging purposes)
    print(following)
    
    # Context data for rendering the profile.html page with profile details, posts, and follow-related information
    context = {
        "profile": profile,
        "posts": posts,
        "follow": follow,  
        "following": following,
        "follow_count": follow_count}
    # Might need further modification based on usage
    
    # Rendering the profile.html page with the context data
    return render(request, "blogapp/profile.html", context)
    

# Ensures the user must be logged in to access this view; redirects to 'signin' page if not authenticated
@login_required(login_url='signin')
def create_post(request):
    # Initialize an empty PostForm
    form = PostForm()
    
    # Fetch the profile of the logged-in user
    profile = Profile.objects.get(user=request.user)
    
    # Check if the HTTP request method is POST
    if request.method == 'POST':
        # If the method is POST, populate the form with the submitted data and files
        form = PostForm(request.POST, request.FILES) # Handle all post data and image file
        
        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, save the new post details
            post = form.save(commit=False)
            
            # Set the post's author as the logged-in user's profile
            post.author = profile
            
            # Generate a slug for the post based on the title
            post.slug = slugify(request.POST["title"]) # change title to a slug format
            
            # Save the new post
            post.save()
            
            # Display a success message indicating the successful post creation
            messages.success(request, "Post created, wait for admin's approval")
            
            # Redirect the user to their profile page after creating the post
            return redirect("profile")
    
    # Prepare context data to render the create.html page with the form
    context = {"form": form}
    
    # Render the create.html page with the form and context data
    return render(request, "blogapp/create.html", context)


# Ensures the user must be logged in to access this view; redirects to 'signin' page if not authenticated
@login_required(login_url='signin') 
def update_post(request, pk):
    # Fetch the specific blog post based on the provided ID (pk)
    post = Blog.objects.get(id=pk)
    
    # Initialize a PostForm instance with the current blog post details
    form = PostForm(instance=post) # To select the exact post to be updated
    
    # Check if the HTTP request method is POST
    if request.method == 'POST':
        # If the method is POST, update the form with the submitted data and files
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # If the form is valid, save the changes to the blog post
            post = form.save(commit=False)
            
            # Update the post's slug based on the updated title
            post.slug = slugify(request.POST["title"])
            
            # Save the updated post
            post.save()
            
            # Display a success message indicating the successful update of the post
            messages.success(request, "Your post has been updated successfully!!")
            
            # Redirect the user to their profile page after updating the post
            return redirect("profile")
    
    # Set a flag indicating this is an update form view
    update_form = True
    
    # Prepare context data to render the create.html page with the updated form and flag
    context = {"form": form, "up": update_form}
    
    # Render the create.html page with the updated form and context data
    return render(request, "blogapp/create.html", context)

# Ensures the user must be logged in to access this view; redirects to 'signin' page if not authenticated
@login_required(login_url='signin')
def delete_post(request, pk):
    # Fetch the specific blog post based on the provided ID (pk)
    post = Blog.objects.get(id=pk)
    
    # Fetch the profile of the logged-in user
    profile = Profile.objects.get(user=request.user)
    
    # Fetch all posts authored by the logged-in user
    posts = Blog.objects.filter(author=profile)
    
    # Check if the HTTP request method is POST
    if request.method == 'POST':
        # If the method is POST, delete the specified blog post
        post.delete()
        
        # Display a success message indicating the successful deletion of the post
        messages.success(request, "Post deleted successfully!")
        
        # Redirect the user to their profile page after deleting the post
        return redirect("profile")
    
    # Set a flag indicating this is a delete post view
    delete_post = True
    
    # Prepare context data to render the profile page with information about the deleted post and user's posts
    context = {"post": post, "del": delete_post, "profile": profile, "posts": posts}
    
    # Render the profile page with the context data
    return render(request, "blogapp/profile.html", context)


