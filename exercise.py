### KBC program
def questions(question):
    print(question)



def answer(answers,correct_answer,amount):
    print(answers)
    
    answer = int(input("Enter the Option:"))
    if(answer == correct_answer):
        amount = amount+2
    else:
        amount = amount+0

    return amount    

amount = 0

question = [
    "1. Who is PM of India?", "2. Name of National Bird?", "3.National fruit?","4. Python is?"
]

answers = [
    ["1. Modi","2. Lodi","3. Sodi","4.Jodi"],["1.Bird","2.Crow","3.Eagle","4. Peacock"],["1.Apple","2.Mango","3.Berry","4.Cherry"],
    ["1.Computer","2.Mobile","3.Logic Gate","4. PL"]
]

questions(question[0])
amount = answer(answers[0],1,amount)
questions(question[1])
amount = answer(answers[1],4,amount)
questions(question[2])
amount = answer(answers[2],2,amount)
questions(question[3])
amount = answer(answers[3],4,amount)

print("Winning Prize:",amount)

