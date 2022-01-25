user = {
    'age': 30,
    'username': 'Samarai',
    'weapons': ['fist',],
    'is_active': True,
    'clan': 'Treaty'
}
print(user.keys())

user['weapons'].append('shield')
print(user)

user.update({'is_banned': False})
print(user)

user.update({'is_banned': True})
print(user)

user2 = user.copy
user2.update({'age': 25, 'username': 'Mobli'})
print(user2)

