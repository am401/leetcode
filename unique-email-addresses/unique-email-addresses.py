class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        start = 
        email_chars = ''
        for i in emails:
            email_split = i.split('@')
            for j in email_split[0]:
                if j not in {".", "+"}:
                    email_chars += j
                else:
                    continue
            print(email_chars+"@"+email_split[1])
