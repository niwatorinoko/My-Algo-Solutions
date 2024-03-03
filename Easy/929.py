class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email = set()
        for i in emails:
            l, d = i.split('@')
            l = l.split("+")[0]
            l = l.replace(".","")
            email.add(l+"@"+d)
        print(email)
        return len(email)