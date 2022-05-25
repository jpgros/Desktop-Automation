import time

def expensive_api_call():
    time.sleep(100) # takes 1,000 seconds
    return 123

def addition(a , b):
    return a+b