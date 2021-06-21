users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
    'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', },
}
for username, user_info in users.items():  # username = keys --- user_info = values
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']  # acessa o dicionario interno
    location = user_info['location']  # acessa o dicionario interno
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
