from smtplib import SMTP  

sender = 'python.practice.bot@gmail.com'
Password = 'yetcezmcvxueacvl'
recipient = 'candelariabenegas@gmail.com'

connect_server = SMTP( host ='smtp.gmail.com', port = 587)
connect_server
connect_server.starttls()
connect_server.login(user = sender, password = Password)
connect_server.sendmail(
	from_addr = sender, 
	to_addrs = recipient, msg = 'Subject:Mail de prueba\n\n Te amo miniso')
connect_server.close()
