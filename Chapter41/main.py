import time, sys, html, os

maxline = 60
DATE = time.strftime('%A, %b %d, %Y')
NAME = input('Please enter your name: ').strip() or 'An unknown reader'
BOOK = 'Learning Python, 6th Edition'

certificate_text = f"""
{'*' * maxline}
     OFFICIAL CERTIFICATE
Date: {DATE}
This certifies that: {NAME}
Has survived the massive tome: {BOOK}
{'*' * maxline}
"""

filename = 'Certificate.txt'
with open(filename, 'w', encoding='utf8') as file:
    file.write(certificate_text)

print(certificate_text)
print(f"File saved to: {os.path.abspath(filename)}")
