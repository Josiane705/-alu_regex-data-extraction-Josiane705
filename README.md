# -alu_regex-data-extraction-Josiane705
This project uses Regular Expressions (Regex) in Python to find and extract useful information from large amounts of text. The main goal is to create a web app that gathers and shows relevant data from different online sources. Specifically, it looks for:

Email Addresses (e.g., user@example.com, firstname.lastname@company.co.uk)
URLs (e.g., https://www.example.com, http://example.org/page)
Phone Numbers (e.g., (123) 456-7890, 123-456-7890, 123.456.7890)
Time (in both 12-hour and 24-hour formats, like 14:30 or 2:30 PM)
Objective
The goal is to use Regex to quickly and accurately extract important data from API responses. This makes it easier to find specific information in large text blocks.

Features
Email Extraction: Catches standard and complex email formats.
URL Extraction: Finds links with or without subdomains and paths.
Phone Number Extraction: Handles various formats, including dashes, dots, and parentheses.
Time Extraction: Supports 24-hour and 12-hour time formats.
Why Regex?
Regex is perfect for finding patterns in text, which makes it great for extracting data like emails, URLs, and more.

Edge Cases Covered
Invalid Emails (e.g., user@.com, @example.com)
Malformed URLs (e.g., http://example, https://.com)
No Matches Found: Displays a message when no relevant data is found.
Tech Used
Python for coding.
Regex (re module) for pattern matching.
Fun Fact!
Learning Regex not only makes this project work but also boosts your skills in data cleaning, web scraping, and input validation! 

