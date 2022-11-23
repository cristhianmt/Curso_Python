"""
8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    user_info['fist_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('linus', 'Torvalds',
                             location='usa',
                             field='software Engineering ')
print(user_profile)