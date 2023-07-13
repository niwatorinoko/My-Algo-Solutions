'''
n = input()
li = []

for i in range(len(str(n))):
    temp = []
    for j in range(int(n[i])):
        temp.append("#")
    for j in range(9-int(n[i])):
        temp.append(".")
    li.append(temp)

li = [["(0,0)","(0,1)","(0,2)","(0,3)","(0,4)","(0,5)","(0,6)","(0,7)","(0,8)"],
      ["(1,0)","(1,1)","(1,2)","(1,3)","(1,4)","(1,5)","(1,6)","(1,7)","(1,8)"],
      ["(2,0)","(2,1)","(2,2)","(2,3)","(2,4)","(2,5)","(2,6)","(2,7)","(2,8)"]]

for i in range(0,len(str(n)),3):
    for row in li:
        output = ""
        for element in row:
            output += element
        print(output.strip())
'''
def generate_barcode(n):
    barcode = ""
    digits = str(n)
    
    for i in range(0, len(digits), 3):
        segment = digits[i:i+3]
        
        for row in range(3):
            for digit in segment:
                count = int(digit)
                
                if row < count:
                    barcode += "#"
                else:
                    barcode += "."
            
            barcode += "\n"
    
    return barcode.strip()

# 数値の入力
n = int(input())

# 二次元バーコードの生成
barcode = generate_barcode(n)

# 出力
print(barcode)

