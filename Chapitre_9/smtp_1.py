#!/usr/bin/env python3
import email.utils
import datetime
import smtplib

serveursmtp = 'smtp.free.fr'

From = 'Patrice Clement <patrice.clement@posteo.net>'
To = 'Patrice Clement <patrice.clement@posteo.net>'
Subject = 'Le sujet de cet email.'
Date = email.utils.formatdate()

entetes = ("""From: %s
To: %s
Date: %s
Subject: %s""" % (
    From,
    To,
    Date,
    Subject
  )
)

corps = entetes + """
Ceci est un test. Date du message: %s
""" % (datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))

print('Envoie du couriel...')
serveur = smtplib.SMTP(serveursmtp)
serveur.set_debuglevel(1)
erreur = serveur.sendmail(From, To, corps)
serveur.quit()
if erreur:
    print('Erreur! ', erreur)
else:
    print('OK!')
