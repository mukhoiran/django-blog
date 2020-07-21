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
