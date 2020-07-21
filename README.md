# django-blog
A simple blog development with Django framework

Requirement :
1. Installing python3 (download from official website)
2. Installing pip3 (apt install python3-pip)

Step 1 :
Installing Django
- #pip3 install django
- #django-admin startproject blog_site [create project]
- #python3 manage.py runserver [running project]

Step 2 :
Routing django
- Add route url to blog_site/urls.py
- Create views.py on blog_site folder
- Add method on views.py adjust to url routes

Step 3 :
Apps in django
- #python3 manage.py startapp blogs [create apps with name blogs (plural name), folder with name blogs will generated]
- copy urls.py from blog_site/ to blogs/
- modify urls.py on blog_site for loaded blog apps
- add new routes on blogs/urls.py
- add new views for the created method on blogs/views.py\

Step 4 :
Setting database and timezone
- Go to blog_site/settings.py
- Change timezone and setup database

Step 5 :
Model and migration
- Go to blog_site/settings.py then, add blogs app to INSTALLED_APPS
- Add blog models to blogs/models.py
- #python3 manage.py makemig
rations blogs [create migration blogs]
- #python3 manage.py migrate [migration tables]

Step 6 :
Check sqlite db from shell
- add feedback data on blogs/models.py
- Running shell for checking data
  1. #sqlite3 db.sqlite3
  2. >.tables
  3. >.exit
  4. python3 manage.py shell
  5. >from blogs.models import Blog
  6. >blog = Blog()
  7. >blog.title = 'first blog'
  8. >blog.desc = 'first description'
  9. >blog.save()
  10. >Blog.objects.all()

Step 7 :
Show value blogs table to browser
- Modify return from views.index on blogs/views.py
- load url blogs from browser [http://localhost:8000/blogs]
