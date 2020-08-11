### Visitor Management System

Three types of user :<br/>
1.admin<br/>
2.Entryperson<br/>
3.user(host)<br/>

Admin : admin can register host,visitor,event and admin can do create update and delete operation on host,vistor,event.<br/>
Entryperson : Will be having the responsible to create visitor comming to visit and he/she can entry the purpose of person entry.And also have the responsible to enter the visitor comming to visit the event. <br/>
user(host): host will be given a user name and password to login. It will be issued by admin.host can create event,update event,delete event and see his account.And also update account.<br/>

# Local setup for this project
<pre><code>pip install django <br/></code></pre>
<pre><code>pip install pillow</code></pre>
<h5>1. Go to visitor_manage_system file and type in cmd or in terminal </h5>
<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python manage.py migrate</code></pre>
<pre><code>python manage.py createsuperuser</code></pre>
<h5>2.after creating superuser then go to url "127.0.0.1/admin" and login, Then create group in Groups</h5>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2013-39-57.png"  width="400" height="250">
<h3>2. Create three group admin,entryperson,host</h3>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2013-42-45.png"  width="400" height="250">
<br/>
<h3>3. Create credentials for admin</h3>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-45.png"  width="400" height="250">
 <h3>and checkbox superuser and chosen groups as admin</h3>
 <img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-55.png"  width="400" height="250">
 <br/>
 <h3>4. Create credentials for entryperson. Username as entryperson </h3>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-07.png"  width="400" height="250">
 <h3>and checkbox staff status and chosen groups as entryperson</h3>
 <img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-21.png"  width="400" height="250">
 <br/>
 <p>Now be in the folder where manage.py is present and run command as</p>
<pre><code>python manage.py runserver</code></pre>
<p>5. Copy and paste the url in browser or type "127.0.0.1:8000" in browser</p>
