# passwordless-app

### To start my project you need to:
1. Install requirements ---> ```pip3 install -r requirements.txt```
2. Run app.py ---> ```python3 wsgi.py```

### Pay attention to app/config.py
There are two important variables:


```PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)``` ------> session time equal to 30 minutes
```TOKEN_TIME_EXPIRED_IN_MIN = 3``` ------> token time to expire equal to 3 min

### Steps to check that everything is working properly:

1. Go to ----> https://passwordless-app.herokuapp.com/
2. Switch to login page
3. If you don't have an account yet, switch to the signup page and register
4. Now, when you have your own account go to the login_passwordless page, and enter your email
5. Then you will recieve an email, open it, and follow the link
6. After that, you had to be redirected to the profile page
7. On the profile page, you are able to see the magic link counter, that will be reset after every 10 times.
