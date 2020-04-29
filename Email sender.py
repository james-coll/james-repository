import smtplib
import time

#logging in
print ("spam bot made by james and a bit of help from mr.yao")
Rec_email = input("Enter the victims email:")
Message = input("Type out your message to them:")
Loop_amount = int(input("how many times would you like this to send:"))

i = 1

#connecting to online server
for i in range (Loop_amount):
    Server = smtplib.SMTP('smtp.gmail.com', 587)
    Server.starttls() # encripter
    Server.login("Noreply.specialoffers@gmail.com", "fakeemail123") # use your email and password here
    Server.sendmail("Noreply.specialoffers@gmail.com", Rec_email, Message)
    print ("You sent", Message, "it better not be anything bad lmao")
    print ("Email has been sent to", Rec_email, "better not of sent any bad shit -James:)")
    time.sleep(1)