print("Welcome to Mad Libs.Let's test your grammar!!")
print("Enter the inputs accordingly :-\n1.Holiday\n2.Noun\n3.Place\n4.Person\n5.Adjective\n6.Body Part(Plural)\n7.Verb\n8.Adjective\n9.Noun\
    \n10.Food\n11.Plural Noun")
all_inputs=[]
i = 0
a=0
while i<11:
    user_input=input("Enter the inputs according to the above order please:")
    all_inputs.append(user_input)
    i+=1
print("I can't believe it's already ",all_inputs[a]," !I can't wait to put on my ",all_inputs[a+1]," and visit every ",all_inputs[a+2]," in my neighborhood.This year,I am going to dress up as (a) ",all_inputs[a+3]," with ", all_inputs[a+4]," ", all_inputs[a+5],".Before I ", all_inputs[a+6]," I make sure to grab my ", all_inputs[a+7]," ", all_inputs[a+8]," to hold all of my", all_inputs[a+9]\
    ," .Finally,all of my",all_inputs[a+10]," are ready to go!")