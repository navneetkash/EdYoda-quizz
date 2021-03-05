questions_dict = {"Easy":{"1-> Capital of Gujarat ?":["(a): Ahmedabad","(b): Surat","(c): Gandhinagar","(d): Rajkot"],"2-> Capital of Maharashtra ???":["(a): Pune","(b): Mumbai","(c): New york","(d): Nagpur"],"3-> Captian of Indian Cricket team ??":["(a): Virat Kolhi","(b): M S Dhoni","(c): Rohit Sharma","(d): Ajinkya Rahane"],"4-> President of BCCI":["(a): Sunil Gavaskar","(b): Sachin tendulkar","(c): Rahul Dravid","(d): Sourabh Ganguly"]},"Intermediate":{"1-> Largest mamal ??":["(a): Lion","(b): blue wale","(c): Elephant","(d): Tiger"],"2-> Home minister of India ??":["(a): Amit Shah","(b): Yogi Adityanath","(c): Narendra Singh Tomar","(d): Ashok Ghelot"],"3-> Fastest animal ??":["(a): leopard","(b): panther","(c): Cheetah","(d): Lioness"]},"Hard":{"1-> value of gravitational force in meter per second square ??":["(a): 9.8","(b): 10","(c): 11","(d): 9.72"],"2-> The Central Rice Research Station is situated in ??":["(a): Chennai","(b): Cuttack","(c): Bangalore","(d): Quilon"],"3-> Who among the following wrote Sanskrit grammar?":["(a): Kalidasa","(b): Charak","(c): Panini","(d): Aryabhatt"]}}
answers_list = ["c","b","a","d","b","a","c","a","b","c"]

def play():
    user_answers=[]
    UserloginAccount()
    print("\n==========QUIZ START==========")
    for i,j in questions_dict["Easy"].items():
        print("Questins. (Level: Easy)")
        print("\t",i)
        print("Options")
        for k in j:
            print("\t",k)
        print("  Enter your option:")
        ans = input()
        user_answers.append(ans)
    for i,j in questions_dict["Intermediate"].items():
        print("Questins. (Level: Intermediate)")
        print("\t",i)
        print("Options")
        for k in j:
            print("\t",k)
        print("  Enter your option:")
        ans = input()
        user_answers.append(ans)
    for i,j in questions_dict["Hard"].items():
        print("Questins. (Level: Hard)")
        print("\t",i)
        print("Options")
        for k in j:
            print("\t",k)
        print("  Enter your option:")
        ans = input()
        user_answers.append(ans)
		
    count = 0
    for i in range(len(user_answers)):
        if user_answers[i]==answers_list[i]:
            count += 1
    print("Your Score is :")
    print(count)
    user_answers = []


def addquizQuestions():
    print("Process of adding question starts::::::")
    print("\n")
    typeofquestion = input("Please enter the type of question you would like to add.\tEasy\tIntermediate\tHard->")
    removequestions(typeofquestion)
    question = input("Please enter the question.")
    options = []
    for i in range(97,101):
        temp = input("Please enter the option ")
        final = "("+chr(i)+")"+temp
        options.append(final)
    if typeofquestion == "Easy":
        questions_dict["Easy"][question] = options
    elif typeofquestion == "Intermediate":
        questions_dict["Intermediate"][question] = options
    elif typeofquestion == "Hard":
        questions_dict["Hard"][question] = options
    else:
        print("Please choose the correst parameter")

def removequestions(typeof):
    print("\nPlease remove the question first before adding more questions to the question list")
    if typeof == "Easy":
        for i,j in questions_dict["Easy"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Easy"].pop(i)
                break
            else:
                continue
    elif typeof == "Intermediate":
        for i,j in questions_dict["Intermediate"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Intermediate"].pop(i)
                break
            else:
                continue
    elif typeof == "Hard":
        for i,j in questions_dict["Hard"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Hard"].pop(i)
                break
            else:
                continue
    else:
        print("Please choose the correst parameter")

def UserloginAccount():
	print("\n==========PLAYER'S DATA PANEL==========")
	playername = input("Please enter your name \n")
	playerdob = input("Please enter your date of birth")
	print("\n",playername,"\t\t",playerdob)

def exit():
    print("======THE END=======")

def rules():
	print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press a/b/c/d (case-sensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
3. Level of first 4 question is Easy and next 3 of Intermediate and last 3 are Hard.
	''')

def about():
	print('''\n==========ABOUT US==========
This project has been created by Navneet Kashyap.
It is a basic Python Project as a part of my basic python assessment.''')

if __name__ == "__main__":
    choice = 1
    while choice != 7:
        print('\n=========WELCOME TO QUIZ MASTER==========')
        print('-----------------------------------------')
        print('1. PLAY QUIZ')
        print('2. ADD QUIZ QUESTIONS')
        print('3. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
        print('4. ABOUT US')
        print('5. EXIT')
        choice = int(input('ENTER YOUR CHOICE: '))
        if choice == 1:
            play()
        elif choice == 2:
            supername = input("Enter your name ?")
            if supername == "SuperUser":
                addquizQuestions()
            else:
                print(supername,"you are not authorized to make changes in the question")
        elif choice == 3:
            rules()
        elif choice == 4:
            about()
        elif choice == 5:
            exit()
            break
        else:
            print('WRONG INPUT. ENTER THE CHOICE AGAIN')

































































# questions_dict = {"Easy":{"1-> Capital of Gujarat ?":["(a): Ahmedabad","(b): Surat","(c): Gandhinagar","(d): Rajkot"],"2-> Capital of Maharashtra ???":["(a): Pune","(b): Mumbai","(c): New york","(d): Nagpur"],"3-> Captian of Indian Cricket team ??":["(a): Virat Kolhi","(b): M S Dhoni","(c): Rohit Sharma","(d): Ajinkya Rahane"],"4-> President of BCCI":["(a): Sunil Gavaskar","(b): Sachin tendulkar","(c): Rahul Dravid","(d): Sourabh Ganguly"]},"Intermediate":{"1-> Largest mamal ??":["(a): Lion","(b): blue wale","(c): Elephant","(d): Tiger"],"2-> Home minister of India ??":["(a): Amit Shah","(b): Yogi Adityanath","(c): Narendra Singh Tomar","(d): Ashok Ghelot"],"3-> Fastest animal ??":["(a): leopard","(b): panther","(c): Cheetah","(d): Lioness"]},"Hard":{"1-> value of gravitational force in meter per second square ??":["(a): 9.8","(b): 10","(c): 11","(d): 9.72"],"2-> The Central Rice Research Station is situated in ??":["(a): Chennai","(b): Cuttack","(c): Bangalore","(d): Quilon"],"3-> Who among the following wrote Sanskrit grammar?":["(a): Kalidasa","(b): Charak","(c): Panini","(d): Aryabhatt"]}}
# answers_list = ["c","b","a","d","b","a","c","a","b","c"]