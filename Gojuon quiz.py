import random
#global variable
ans = " "
#-----------------------------------
#lists
gojuon = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"]
#--------------------------------------------
gojuonLeft = len(gojuon)
while gojuonLeft !=0:
    random.shuffle(gojuon)
    print(gojuon[0])
    if gojuon[0] == "あ":
        ans = "a"
    elif gojuon[0] == "い":
        ans = "i"
    elif gojuon[0] == "う":
        ans = "u"
    elif gojuon[0] == "え":
        ans = "e"
    elif gojuon[0] == "お":
        ans = "o"
    elif gojuon[0] == "か":
        ans = "ka"
    elif gojuon[0] == "き":
        ans = "ki"
    elif gojuon[0] == "く":
        ans = "ku"
    elif gojuon[0] == "け":
        ans = "ke"
    elif gojuon[0] == "こ":
        ans = "ko"
    elif gojuon[0] == "さ":
        ans = "sa"
    elif gojuon[0] == "し":
        ans = "si"
    elif gojuon[0] == "す":
        ans = "su"
    elif gojuon[0] == "せ":
        ans = "se"
    elif gojuon[0] == "そ":
        ans = "so"
    elif gojuon[0] == "た":
        ans = "ta"
    elif gojuon[0] == "ち":
        ans = "chi"
    elif gojuon[0] == "つ":
        ans = "tsu"
    elif gojuon[0] == "て":
        ans = "te"
    elif gojuon[0] == "と":
        ans = "to"
    elif gojuon[0] == "な":
        ans = "na"
    elif gojuon[0] == "に":
        ans = "ni"
    elif gojuon[0] == "ぬ":
        ans = "nu"
    elif gojuon[0] == "ね":
        ans = "ne"
    elif gojuon[0] == "の":
        ans = "no"
    elif gojuon[0] == "は":
        ans = "ha"
    elif gojuon[0] == "ひ":
        ans = "hi"
    elif gojuon[0] == "ふ":
        ans = "Fu"
    elif gojuon[0] == "へ":
        ans = "he"
    elif gojuon[0] == "ほ":
        ans = "ho"
    elif gojuon[0] == "ま":
        ans = "ma"
    elif gojuon[0] == "み":
        ans = "mi"
    elif gojuon[0] == "む":
        ans = "mu"
    elif gojuon[0] == "め":
        ans = "me"
    elif gojuon[0] == "も":
        ans = "mo"
    elif gojuon[0] == "や":
        ans = "ya"
    elif gojuon[0] == "ゆ":
        ans = "yu"
    elif gojuon[0] == "よ":
        ans = "yo"
    elif gojuon[0] == "ら":
        ans = "ra"
    elif gojuon[0] == "り":
        ans = "ri"
    elif gojuon[0] == "る":
        ans = "ru"
    elif gojuon[0] == "れ":
        ans = "re"
    elif gojuon[0] == "ろ":
        ans = "ro"
    elif gojuon[0] == "わ":
        ans = "wa"
    elif gojuon[0] == "を":
        ans = "wo"
    elif gojuon[0] == "ん":
        ans = "n"
    else:
        print("Error")

    
    myAnswer = input("Enter you answer:")
    if myAnswer == ans:
        print("Correct")
        print("---------------------------------------------------")
        gojuon.remove(gojuon[0])
        gojuonLeft = gojuonLeft-1
    elif myAnswer == "?":
        print("There are only", gojuonLeft, "questions left!")
        print("---------------------------------------------------")
    else:
        print("Try again")
        print("The correct answer is", ans)
        print("---------------------------------------------------")

print("Congrags! You have done all of them!")

    
