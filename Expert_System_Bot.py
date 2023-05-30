print("welcome to --- bank!!")
while True:
    question=input('Enter the question:')
    if question in ['hello','hi','hii']:
        print('Hello, How can I help you?')
    elif question in ['how are you?']:
        print('I am fine! How are you')
    elif question in ['what is the timing of bank?']:
        print('Monday to Saturday\nFrom 10:00am To 05:00pm')
    elif question in ['what is lunch time?']:
        print('It is From 01:00pm To 02:00pm')
    elif question in ['Is Bank have any Application for E-banking?']:
        print('Yes We have an application for E-banking')
    elif question in ['Does bank have any loan scheme for farmers?']:
        print('Yes')
    elif question in ['what is customer helpline number?']:
        print('74996*****')
    elif question in ['Thank you']:
        print("You're Welcome, Have a nice day")
    else:
        print('Sorry I am unable to process your request')
        print('please enter the valid question')


"""
    Output -
    
 welcome to --- bank!!
Enter the question:hi
Hello, How can I help you?

Enter the question:what is the timing of bank?
Monday to Saturday
From 10:00am To 05:00pm

Enter the question:what is lunch time?
It is From 01:00pm To 02:00pm

Enter the question:Is Bank have any Application for E-banking?
Yes We have an application for E-banking

Enter the question:Does bank have any loan scheme for farmers?
Yes

Enter the question:what is customer helpline number?
88888*****

Enter the question:You're Welcome, Have a nice day
Sorry I am unable to process your request
please enter the valid question
    
"""
