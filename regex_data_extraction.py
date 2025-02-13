import re

# This function finds email addresses in the text
# It looks for patterns like user@example.com or firstname.lastname@company.co.uk
# - [\w\.-]+: Finds letters, numbers, dots, or hyphens before the @ symbol
# - @[\w\.-]+: Finds the @ symbol followed by the domain name
# - \.\w{2,3}: Looks for a dot followed by 2 or 3 letters (like .com or .uk)
def extract_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w{2,3}'
    return re.findall(pattern, text)

# This function finds website links (URLs) in the text
# It looks for links that start with http or https
# - https?: Checks for http or https at the start
# - (?:www\.)?: Looks for www. if it's there but doesn't require it
# - \S+: Finds all characters that are not spaces for the main part of the link
# - \.\w{2,3}: Looks for a dot followed by 2 or 3 letters (like .com)
# - (?:/\S*)?: Optionally finds the rest of the URL after the domain name
def extract_urls(text):
    pattern = r'https?://(?:www\.)?\S+\.\w{2,3}(?:/\S*)?'
    return re.findall(pattern, text)

# This function finds phone numbers in different formats
# It matches patterns like (123) 456-7890, 123-456-7890, or 123.456.7890
# - \(?\d{3}\)?: Looks for an optional area code with or without parentheses
# - [-.]?: Checks for an optional separator (hyphen or dot)
# - \d{3}: Matches three digits for the main part of the number
# - \d{4}: Matches the last four digits of the phone number
def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}'
    return re.findall(pattern, text)

# This function finds time in 12-hour and 24-hour formats
# It matches times like 14:30 (24-hour) or 2:30 PM (12-hour)
# - (?:[01]?\d|2[0-3]): Finds the hour part of the time
# - [0-5]\d: Matches the minutes (00 to 59)
# - (?: [APap][Mm])?: Optionally checks for AM or PM for 12-hour times
def extract_time(text):
    pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?: [APap][Mm])?\b'
    return re.findall(pattern, text)

# This section tests the functions with example text and shows the results
if __name__ == '__main__':
    sample_text = '''
        Contact us at support@example.com or sales@example.co.uk.
        Visit our website at https://www.example.com or http://example.org/page.
        Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
        The event starts at 14:30 and ends at 2:30 PM.
        Invalid email: user@.com and malformed URL: http://example
        Random text with no matches.
    '''
    print("Emails Found:")
    print("-", "\n- ".join(extract_emails(sample_text)) or "None")
    print("\nURLs Found:")
    print("-", "\n- ".join(extract_urls(sample_text)) or "None")
    print("\nPhone Numbers Found:")
    print("-", "\n- ".join(extract_phone_numbers(sample_text)) or "None")
    print("\nTimes Found:")
    print("-", "\n- ".join(extract_time(sample_text)) or "None")
