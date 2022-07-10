#By Sleepy_Miner

import random as r
user_input = int(input("Enter how long the password should be?:"))
all_characters = ['0','1','2','3','4','5','6','7','8','9','!','@','#',"$","%","^","&","*","(",")","_","<",">","a",'b','c','d','e','f'\
                'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D'\
                'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
pwd = ""
for i in range(user_input):
    pwd+=r.choice(all_characters)
print("Generated password is:",pwd)