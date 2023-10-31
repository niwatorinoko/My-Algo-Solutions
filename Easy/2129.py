class Solution:
    def capitalizeTitle(self, title: str) -> str:
        li = []
        for i in title.split():
            if len(i) <= 2:
                li.append(i.lower())
            else:
                li.append(i.title())

        return " ".join(li)