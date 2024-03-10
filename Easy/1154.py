class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split("-")
        today = datetime.date(year=int(date[0]), month=int(date[1]), day=int(date[2]))
        fday = datetime.date(year=int(date[0]), month=1, day=1)
        td = abs(fday - today)
        return td.days+1