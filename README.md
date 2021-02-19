# passwordless-app

### To start my project you need to:
1. Install requirements ---> ```pip3 install -r requirements.txt```
2. Run app.py ---> ```python3 wsgi.py```

### Pay attention to app/config.py
There is two important variables:


```PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)``` ------> session time equal to 30 minutes
```TOKEN_TIME_EXPIRED_IN_MIN = 3``` ------> token time to expire equal to 3 min
