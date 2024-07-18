def bar(names, age_user, if_id):
    return names != 'bobby', age_user >= 21, if_id != 'n'


name = str(input('What is your name?: '))
age = int(input("What's your age?: "))
has_id = str(input('Do you have ID: (y/n) '))


def main():
    result = bar(name, age, has_id)
    return result


def check():
    allowed = main()
    match allowed:
        case (True, True, True):
            print('You may enter.')
        case _:
            print('Get out!')


check()
