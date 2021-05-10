email_id=input("enter your email:").strip()
username=email_id[:email_id.index('@')]
domainname=email_id[(email_id.index("@")+1):]
print('Your username is {} and domainname is {}'.format(username,domainname))
