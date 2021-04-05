# Vote_App
 Voting app  
 
 Pyton version 3.8.7  
 Django version 3.1.7  
 
 ## About 
 A web-application developed with Python/Django that takes polls and tallies user responses.  

## Purpose
 Delve into the realm of Django to develop a voting_app.  In doing so, aim to learn effective web-development techniques and useful tools.  

## Run()

### install polls package:
* In order for the application to run as intended, the polls app must be installed first.  In the project directory run the following command:  
```bash
python3 -m pip install --user django-polls/dist/django-polls-0.1.tar.gz
```

### execute program:
1. In Terminal, navigate to the 'vote_app' directory  
2. execute the following command:  
```bash
python3 manage.py runserver
```  
3. In your choice web broswer, enter the address *'127.0.0.1:8000/polls'*  

### Login to admin
* Create superuser using the command:
```
python3 manage.py createsuperuser
```
* login with default: U: admin P: Passw0rd

### Add new questions/choices
1. Make sure your logged into the admin page using either a created superuser or the default admin credentials.
2. In *'127.0.0.1:8000/admin'* navigate to the Questions change list.  
3. From here you can change a question and its answers or add new ones.  
