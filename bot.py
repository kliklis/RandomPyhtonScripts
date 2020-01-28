#artofwill@hotmail.com William
#alvonasion@gmail.com septiawan alvin
#https://www.artstation.com/ggp geaorge


#Billy Christian billcreative@ymail.com
#Magdalena Radziej radziejmagdalena@gmail.com
#Yigit Koroglu yigitkoroglu@gmail.com
#Lucas Parolin lucas@lucasparolin.com
#Artem Demura stargrave24@gmail.com




import smtplib

NAMES = ["Yigit","Lucas","Artem","Magdalena","Billy"]

to = ['yigitkoroglu@gmail.com','lucas@lucasparolin.com','stargrave24@gmail.com','radziejmagdalena@gmail.com','billcreative@ymail.com']

#to=['kklimantakis@gmail.com','kklimantakis@gmail.com']
#NAMES = ["kostas","kostas2"]
gmail_user = 'kklimantakis@gmail.com'
gmail_pwd = '#xeith3kE'

c=0
for i in to:
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + i + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Card Game Artwork\n'
    print(header)
    msg = header + '\n Hi '+NAMES[c]+''', I plan to make a TCG - style game (for android and physical) and I need some awesome artwork.
Could you create about 60 custom images for me and how much should I pay per image?
Could you tell me an average price for a non-custom image (like those on your artstation page)?\n\nThank you in advance!'''
    smtpserver.sendmail(gmail_user, to, msg)
    print('done!')
    c+=1
    smtpserver.close()



'''
import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("kklimantakis@gmail.com", "#xeith3kE")
server.sendmail(
  "kklimantakis@gmail.com", 
  "kklimantakis@gmail.com", 
  "this message is from python")
server.quit()'''
