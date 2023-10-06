subjectList = ["生活態度","国語","数学","地理","歴史","生物","化学","英語","体育","保健体育","家庭科","音楽","情報技術"]

A_subjectscore_List = [65,70,84,95,51,60,71,89,65,44,55,60,72]
B_subjectscore_List = [90,65,78,40,80,78,77,60,80,70,42,80,45]
C_subjectscore_List = [90,82,78,86,80,78,77,99,80,70,87,80,90]

Entrance_subjectslist = ["生活態度","化学","英語","体育","地理","歴史"]
S_Entrance_subjectslist = [85,70,70,80,75,80]

#sumA = 0
flag = True
for i in subjectList:
    if i in Entrance_subjectslist:
        subjectscore = A_subjectscore_List[subjectList.index(i)]
        #sumA += subjectscore
        if subjectscore < S_Entrance_subjectslist[Entrance_subjectslist.index(i)]:
            print(f"学生A {i} 不合格")
            print(f"学生Aを推薦することはできません。")
            flag = False
            break
        else:
            print(f"学生A {i} 合格")

if flag:
    print(f"学生Aを推薦することができます。")