library_books = ["プリンセスとデータベース:王国のSQL",
                 "時をかける寿司:過去のワサビ",
                 "ゾンビとお茶会:アフタヌーン・アポカリプス",
                 "宇宙人との結婚式:愛の放射線",
                 "忍者ペンギン:氷山の下の秘密"]
'''
borrowbook = "宇宙人との結婚式:愛の放射線"
if borrowbook in library_books:
    library_books.remove(borrowbook)
    print(borrowbook, "貸し出しました。")
else:
    print(borrowbook, "は存在しませんでした。")
print(library_books)
'''
'''
returnBook = "コーヒー豆の冒険：エスプレッソ宇宙へ"
library_books.append(returnBook)
print(returnBook, "が返却されました。")
print(library_books)
'''
print("今現在図書館にある書籍は：")
for item in library_books:
    print(item)