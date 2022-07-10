def starting_text():
 print("I am not a robot test")
 print("Type the Following to test that you are a bot or not!")
 correct_txt="I am made with python"
 print(correct_txt)
 user_input=input(">>>>")
 if user_input==correct_txt:
    username=input("Enter The Username:")
    password=input("Enter Your Password:")
    correct="Sleepy_Miner"
    correct_pass="123456"
    if (username==correct and password==correct_pass):
     print("Hello! Sleepy_Miner Welcome Back")
    else:
     print("Wrong Username or Password!")
 else:
    print("Sorry! You are not a human")
    print("""Do you Want to take the test again?
Answer in 'Yes'or'No'""")
    second_input=input(">>>>")
    if second_input.upper=="YES":
        starting_text()
    elif second_input.upper=="NO":
        print("Thanks For Taking the test!!!")
    else:
        print("Wrong Input")
starting_text()



   