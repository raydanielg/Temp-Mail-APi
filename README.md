Temp-Mail Python API Wrapper
This is a Python wrapper for the temp-mail.org service. Temp-Mail allows you to generate temporary email addresses to receive anonymous emails for free. This can be particularly useful for protecting your personal email, testing email services, or bypassing unwanted spam.

You can find the full API documentation at api2.temp-mail.org.

Features
Generate temporary email addresses.

Retrieve emails from temporary inboxes.

Support for custom login names and domains.

Requirements
Before using this API wrapper, make sure you have the following Python packages installed:

requests (required) - To make HTTP requests to the Temp-Mail API.

simplejson (optional) - To speed up JSON decoding. This is recommended for performance in large-scale operations.

You can install both using pip:

bash
Copy
Edit
pip install requests simplejson
Installation
To install the Temp-Mail Python API Wrapper package via pip, run the following command in your terminal:

bash
Copy
Edit
pip install temp-mail
Usage
1. Get All Emails From a Given Email Login and Domain
If you have a specific login and domain (e.g., denis@gnail.pw), you can fetch all the emails sent to that address:

python
Copy
Edit
from tempmail import TempMail

# Initialize with specific login and domain
tm = TempMail(login='denis', domain='@gnail.pw')

# Retrieve and print all emails sent to 'denis@gnail.pw'
print(tm.get_mailbox())  
Output: A list of emails in the inbox of denis@gnail.pw.

2. Generate a New Temporary Email and Get Emails
You can also generate a new temporary email address and fetch emails sent to it:

python
Copy
Edit
from tempmail import TempMail

# Initialize TempMail (this generates a random email)
tm = TempMail()

# Generate a new email address
email = tm.get_email_address()
print(f"Generated Email: {email}")

# Retrieve and print emails sent to the generated address
print(tm.get_mailbox(email))
Output: A new temporary email address is generated, and all emails sent to it will be displayed.

Example Output:
plaintext
Copy
Edit
Generated Email: v5gwnrnk7f@gnail.pw
Mail #1: Test email 1
Mail #2: Test email 2
Additional Information
For more advanced features or customization, such as retrieving emails by filtering specific criteria, refer to the Temp-Mail API documentation.