import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

yourmail = input("enter your email : "
yourpassword = input("enter your password : "
targetmail = input("enter target mail : "

server.login(yourmail,yourpassword)

msg = "< your message >"

server.sendmail(yourmail,targetmail,msg)
