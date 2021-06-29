wife_children = {
    'raíssa': {'first': 'ráfila', 'last': 'jorge', 'location': 'aramina', },
    'eder': {'first': 'cantanhede', 'last': 'silva', 'location': 'franca', },
    'josué': {'first': 'jorge', 'last': 'cantanhede', 'location': 'aramina'},
    'caleb': {'first': 'jorge', 'last': 'cantanhede', 'location': 'aramina'},
    'heitor': {'first': 'jorge', 'last': 'cantanhede', 'location': 'aramina'},
}
for my_family, user_info in wife_children.items():
    print("\nMinha família: " + my_family)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tNome completo: " + full_name.title())
    print("\tLocalização: " + location.title())
