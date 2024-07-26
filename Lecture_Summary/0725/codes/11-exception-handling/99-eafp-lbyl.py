my_dict = {'key': 'value'}

# EAFP (Easier to Ask for Forgiveness than Permission)
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')


# LBYL (Look Before You Leap)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
