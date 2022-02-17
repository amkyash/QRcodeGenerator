import qrcode
def data():

    name=input("Enter Name")
    age=int(input("Enter Age"))
    contact_num=int(input("Enter Contact Number"))
    Addr=input("Enter Address")
    li=(f"{name}'s age is {age}.")
    li=li+(f"His Contact Number is {contact_num} and his address is {Addr}")
    return li
for i in range(1,int(input("Number of people"))+1):
    img=qrcode.make(data())
    img.save(f"data{i}.jpg")



    
#####################BASIC_PRACTICE_CODES_AND_TRIES#####################
'''
#1st
import qrcode
img = qrcode.make((input("Amount of Data to be Filled")))
img.save("data.jpg")
'''
'''
#2nd

import qrcode
def data():
    name=input("Enter Your Name")
    return name
n=int(input("Amount of Data to be Filled"))
li=[]
for i in range(n):
    a=data()
    li.append(a)
img = qrcode.make(''.join(li))
img.save("data1.jpg")
'''
