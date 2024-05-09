import re

text = "Emails: info@gmail.com, support@hotmail.com, customer-service@yahoo.com, customer-support@hotmail.com"
# Comments for regex:
    # user_email: Matches one or more word characters (letters, digits, or underscores), dots, or hyphens.
    # domain: Matches one or more letters (uppercase or lowercase), digits, dots, or hyphens for the domain name part.
    # (?!hotmail\.com): Exclude all emails that have domain name of hotmail.com
    # @ and . included in the email address
    # Top-level domain (TLD): Matches two or more letters (uppercase or lowercase) for the top-level domain

emails = re.findall(r"\b[\w\.-]+@(?!hotmail\.com)[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}\b", text)
print(emails)