# You will be provided with a block of text, spanning not more than hundred lines.
# Your task is to find the unique e-mail addresses present in the text.
# You could use Regular Expressions to simplify your task.
# And remember that the "@" sign can be used for a variety of purposes!
# Requirements are simplified versus real world.
# There can be a number of strings separated by dots before and after the "@" symbol.
# Strings will be made up of characters in the ranges a-z, A-Z, 0-9, _ (underscore).
#
# Input Format:
# ------------
# The first line contains an integer N (N<=100), which is the number of lines present in the text fragment
# which follows.
# From the second line, begins the text fragment (of N lines) in which you need to search for e-mail addresses.
#
# Output Format:
# -------------
# All the unique e-mail addresses detected by you, in one line, in lexicographical order,
# with a semicolon as the delimiter.

import re

class EmailValidator:
     def __init__(self):
         # The outermost parenthesis is the capturing group for
         # re to grab the entire email id. match group 0 will contain
         # the full matched string, match group 1 will contain matched
         # string for the second parenthesis; similarly match-group 3 for
         # 3rd parenthesis
         self.pattern = r'([a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*@([a-zA-Z0-9_]+\.)+[a-zA-Z0-9_]+)'

     def grab_email_ids(self, text: str) -> str:
        match_groups = re.findall(self.pattern, text) # will return [(email1-match-group-0, email1-match-group-1, email1-match-group-2),
                                                      #              (email2-match-group-0, email2-match-group-1, email2-match-group-2)...]
        unique_emails = set()
        for group in match_groups:
            unique_emails.add(group[0])  # group[0] is full match
        unique_emails = list(unique_emails)
        unique_emails.sort()
        return ";".join(unique_emails)

     # Solution 2(using re.finditer())
     # def grab_email_ids(self, text: str) -> str:
     #    matches = re.finditer(self.pattern, text)
     #    emails = []
     #    for match in matches:
     #        #print(match.group(0), match.group(1), match.group(2))
     #        emails.append(match.group(0))
     #    return ";".join(emails)


if __name__ == "__main__":
    text = '''
    This is a block of text with some email addresses.
    Email 1: user1@example.com and also user2@example.org.in, how about foo.bar.baz@xyz.co.jp
    Email 2: user2@email.org
    Adding user2@email.org as a duplicate email for test
    Some more text here.
    Email 3: user3@gmail.com
    adding some more email ids such as a@b.com, aaa@bb.in, cc.dd@x.y.z, not_valid_email@domain_without_dot
    '''
    validator = EmailValidator()
    print(validator.grab_email_ids(text))