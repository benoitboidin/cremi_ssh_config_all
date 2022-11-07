if __name__ == "__main__":
    try:
        username = input("Enter username: ")
        with open('cremi_servers.txt') as input_file:
            lines = input_file.readlines()
            with open('cremi_config.txt', 'w+') as output_file:
                for name in lines:
                    name = name.replace('\n', '')
                    print('Adding {} to config file.'.format(name))
                    output_file.write('Host' + name + '\n  HostName'+ name + '.emi.u-bordeaux.fr\n  User ' + username +  '\n  ProxyJump cremi\n  ForwardX11 yes\n\n')
    except TypeError:
        print("Error")
