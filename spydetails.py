spy_is_online=False
spy_name = raw_input("Enter your Name")
spy_salutation= raw_input("Are You Mr. or Ms. ?")
spy_password=raw_input("Create your password")
print("you have created a password")
spy_age = raw_input("Enter your age")
spy_rate=raw_input("Enter your rating (out of 5)")
if len(spy_name)>0 and spy_age>="18" and spy_age<="45" and spy_rate>="3.0" and spy_rate<="5.0":
    print"Congratulations " +spy_salutation +spy_name,
    print"! \nYou have successfully created your account"
    spy_is_online=True
else:
    print"Sorry!could not proceed\neither you have entered wrong input or your details doesn't fulfil our requirements"

friends = [
    {
        'name': 'Nitesh',
        'saultation': 'Mr.',
        'rating': 4.5,
        'age': 25,
        'chats': []
    },
    {
        'name': 'Shreya',
        'saultation': 'Ms.',
        'rating': 4.4,
        'age': 21,
        'chats': []
    },
    {
        'name': 'abhilash',
        'saultation': 'Mr.',
        'rating': 4,
        'age': 19,
        'chats': []
    }
]
