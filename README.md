### Visitor Management System

Three types of user :<br/>
1.admin<br/>
2.Entryperson<br/>
3.user(host)<br/>

Admin : admin can register host,visitor,event and admin can do create update and delete operation on host,vistor,event.<br/>
Entryperson : Will be having the responsible to create visitor comming to visit and he/she can entry the purpose of person entry.And also have the responsible to enter the visitor comming to visit the event. <br/>
user(host): host will be given a user name and password to login. It will be issued by admin.host can create event,update event,delete event and see his account.And also update account.<br/>

# Local setup for project
<pre><code>pip install django</code></pre>
<pre><code>pip install pillow</code></pre>
<h5>Go to visitor_manage_system file and type in cmd or terminal </h5>
<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python managepy migrate</code></pre>
<pre><code>python manage.py createsuperuser</code></pre>
<h5>after creating superuser then go to url "127.0.0.1/admin" </h5>
<h5>after login then create group</h5>
