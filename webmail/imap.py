﻿import imaplib, webmail, osimport getpassusername = input("Enter User Account: ")accpass = getpass.getpass("Enter Account Password: ")user = usernamepassword = accpasshost = ['outlook.office365.com',        'imap.gmail.com',        'imap.mail.me.com',        'imap-mail.outlook.com',        'imap.aol.com',        ]def hostarr():    i = 0    hostlen = len(host)    while i < hostlen:        print(i, ': ', host[i])        i += 1print(hostarr())hostSelected = int(input("Enter the number corresponding to the host: "))host = host[hostSelected]print("Selected Host is:", host)imap_url = hostM = imaplib.IMAP4_SSL(imap_url)M.login(user, password)M.select('INBOX')typ, data = M.search(None, 'All')for num in data[0].split():    typ, data = M.fetch(num, '(RFC822)')    print('Message %s\n%s\n' % (num, data[0][1]))    print("---------------------------------------------------------------------------------------------------------------------------")    print("------------------------------------------------------ Message Load Complete ----------------------------------------------")    print("---------------------------------------------------------------------------------------------------------------------------")M.close()M.logout()print("Account {} logout".format(username))