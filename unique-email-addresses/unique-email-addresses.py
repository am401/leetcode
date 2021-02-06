class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:    
        email_list = []
        email_chars = ''
        for i in emails:
            email_split = i.split('@')
            for j in email_split[0]:
                if j != ".":
                    email_chars += j
                for k in email_chars:
                    if k == "+":
                        start = email_chars.find("+")
                        end = email_chars.find("@")
                        remove_string = email_chars.replace(email_chars[start:end], "")
                combine_email = remove_string[:-1]+"@"+email_split[1]
                email_list.append(combine_email)
        return len(set(email_list))
            
        #for i in emails:
        #    start = i.find("+")
        #    end = i.find("@")
        #    remove_string = i.replace(i[start:end], "")
        #    print(remove_string)
