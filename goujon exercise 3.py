import random
#global variable
ans = " "
#-----------------------------------
#lists
gojoun = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"]
#--------------------------------------------
gojounLeft = len(gojoun)
while gojounLeft >=1:
    random.shuffle(gojoun)
    print(gojoun[0])
    if gojoun[0] == "あ":
        ans = "a"
    elif gojoun[0] == "い":
        ans = "i"
    elif gojoun[0] == "う":
        ans = "u"
    elif gojoun[0] == "え":
        ans = "e"
    elif gojoun[0] == "お":
        ans = "o"
    elif gojoun[0] == "か":
        ans = "ka"
    elif gojoun[0] == "き":
        ans = "ki"
    elif gojoun[0] == "く":
        ans = "ku"
    elif gojoun[0] == "け":
        ans = "ke"
    elif gojoun[0] == "こ":
        ans = "ko"
    elif gojoun[0] == "さ":
        ans = "sa"
    elif gojoun[0] == "し":
        ans = "si"
    elif gojoun[0] == "す":
        ans = "su"
    elif gojoun[0] == "せ":
        ans = "se"
    elif gojoun[0] == "そ":
        ans = "so"
    elif gojoun[0] == "た":
        ans = "ta"
    elif gojoun[0] == "ち":
        ans = "chi"
    elif gojoun[0] == "つ":
        ans = "tsu"
    elif gojoun[0] == "て":
        ans = "te"
    elif gojoun[0] == "と":
        ans = "to"
    elif gojoun[0] == "な":
        ans = "na"
    elif gojoun[0] == "に":
        ans = "ni"
    elif gojoun[0] == "ぬ":
        ans = "nu"
    elif gojoun[0] == "ね":
        ans = "ne"
    elif gojoun[0] == "の":
        ans = "no"
    elif gojoun[0] == "は":
        ans = "ha"
    elif gojoun[0] == "ひ":
        ans = "hi"
    elif gojoun[0] == "ふ":
        ans = "Fu"
    elif gojoun[0] == "へ":
        ans = "he"
    elif gojoun[0] == "ほ":
        ans = "ho"
    elif gojoun[0] == "ま":
        ans = "ma"
    elif gojoun[0] == "み":
        ans = "mi"
    elif gojoun[0] == "む":
        ans = "mu"
    elif gojoun[0] == "め":
        ans = "me"
    elif gojoun[0] == "も":
        ans = "mo"
    elif gojoun[0] == "や":
        ans = "ya"
    elif gojoun[0] == "ゆ":
        ans = "yu"
    elif gojoun[0] == "よ":
        ans = "yo"
    elif gojoun[0] == "ら":
        ans = "ra"
    elif gojoun[0] == "り":
        ans = "ri"
    elif gojoun[0] == "る":
        ans = "ru"
    elif gojoun[0] == "れ":
        ans = "re"
    elif gojoun[0] == "ろ":
        ans = "ro"
    elif gojoun[0] == "わ":
        ans = "wa"
    elif gojoun[0] == "を":
        ans = "wo"
    elif gojoun[0] == "ん":
        ans = "n"
    else:
        print("Error")


    myAnswer = input("Enter you answer:")
    if myAnswer == ans:
        print("Correct")
        print("---------------------------------------------------")
        gojoun.remove(gojoun[0])
    else:
        print("Try again")
        print("The correct answer is", ans)
        print("--------------------------------------------------")

print("Congregs! You have done all of them!")

    
