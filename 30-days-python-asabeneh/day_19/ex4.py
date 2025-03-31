# ex4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.

from utils import readEmailsBigFromTxtFile

emails = readEmailsBigFromTxtFile()
email_addresses = []
for line in emails.splitlines():
    if line.startswith("From:"):
        email = line.split()[1]
        email_addresses.append(email)

[print(emailAddress) for emailAddress in email_addresses]
