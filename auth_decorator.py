user ={
    'name': 'MyName',
    'valid': False
}

user2 = {
    'name': 'OtherName',
    'valid': True
}

def auth(fn):
    def wrapper(*args, **kwargs):
        if user['valid'] == True:
            return fn(*args, **kwargs)
        else:
            print('user is not valid')
    return wrapper

@auth
def message_user(user):
    print('message sent from valid user')


message_user(user)
print()
 