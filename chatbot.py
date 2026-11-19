print("My name is laila,i am here to support")
print("tell me your name")
name=input("you:")
print("hello",name,"how can i help you?")
print("you can ask me:hi,how are you?,who created you?")

message=input("you:")
while message!="bye":
    if message.lower()=="hi":
        print("laila:hiii how you doin?")
    elif message=="how are you?":
        print("laila:i am fine,thankyou")
        print("what about you?")
    elif message=="i am good"or message=="i am fine":
        print("lovely,how can i help")
        print("you can ask me:hi,how are you?,who created you?")
    elif message=="who created you?":
        print("laila: miss siddhi did")
    else:
        print("sorry i don't understand it")
        print("you can ask me:hi,how are you?,who created you?")

    message=input("you:")


print("byee!see yaa")


