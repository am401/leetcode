class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:    
        email_list = []
        email = ''
        for i in emails:
            start = i.find("+")
            end = i.find("@")
            remove_local = i.replace(i[start:end], "")
            split_email = remove_local.split("@")
            for j in split_email[0]:
                if j != ".":
                    email += j
            email_combined = email+"@"+split_email[1]
            email_list.append(email_combined)
            email = ''
        return len(set(email_list))
