phone_list = {
    "tom": "+123456",
    "bob": "+098765",
    "alice": "+657483",
    "dilan": "+990888",
    "adam": "+344868",
    "dora": "+776445",
    "chuck": "+611234"
}
while True:
    user_input = input('enter a command: ') # commands: stats, add, delete <name>, list, show <name>
    if user_input =='stats':
        print(len(phone_list))
    elif user_input =='add':
        name_phone_input = input('enter name and phone ')
        split_input = name_phone_input.split()
        name = split_input[0]
        phone = split_input[1]
        if name in phone_list:
            print(f'{name} already exists')
        else:
            phone_list[name] = phone
    elif user_input =='delete':
        name_phone_input_d = input('enter name ')
        if name_phone_input_d in phone_list:
            del phone_list[name_phone_input_d]
        else:
            print(f'there is no {name_phone_input_d} in phone list')
    elif user_input == 'list':
        print(phone_list.keys())
    elif user_input =='show':
        name_phone_input_s = input('enter name ')
        print(phone_list.get(name_phone_input_s))
