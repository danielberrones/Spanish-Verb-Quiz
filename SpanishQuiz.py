## Spanish Verb Quiz
## Created by Daniel Berrones

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

spanishQuestions = [
     "What's the future tense of the verb hacer in the 2nd person singular?\n(a)harás\n(b)hará\n(c)haremos\n(d)haré\n",
     "What's the imperfect tense of the verb hablar in the 3rd person plural?\n(a)tocaban\n(b)hablaban\n(c)tocaron\n(d)hablaron\n",
     "What's the present subjunctive verb decir in the 1st person plural?\n(a)dijéramos\n(b)estemos\n(c)digamos\n(d)estamos\n",
     "What's the present indicative of the verb ser in the 3nd person singular?\n(a)sea\n(b)es\n(c)seas\n(d)eres\n",
     "What's the present subjunctive verb querer in the 1st person plural?\n(a)queramos\n(b)quieren\n(c)queremos\n(d)querremos\n",
     "What's the future tense of the verb ver in the 1st person plural?\n(a)veremos\n(b)vemos\n(c)verán\n(d)vean\n",
     "What's the imperfect tense of the verb estudiar in the 3rd person plural?\n(a)estudiaré\n(b)estudiaste\n(c)estudiaban\n(d)estudiaremos\n",
     "What's the present subjunctive of the verb amar in the 1st person plural?\n(a)amamos\n(b)amemos\n(c)amáramos\n(d)amarán\n",
     "What's the present indicative of the verb estar in the 3nd person plural?\n(a)estaban\n(b)estarán\n(c)están\n(d)son\n",
     "What's the future tense of the verb sonreír in the 1st person singular?\n(a)sonrien\n(b)sonries\n(c)sonreía\n(d)sonreiré\n",
]

questionsList = [
    Question(spanishQuestions[0], "a"),
    Question(spanishQuestions[1], "b"),
    Question(spanishQuestions[2], "c"),
    Question(spanishQuestions[3], "a"),
    Question(spanishQuestions[4], "a"),
    Question(spanishQuestions[5], "a"),         
    Question(spanishQuestions[6], "c"),    
    Question(spanishQuestions[7], "b"),   
    Question(spanishQuestions[8], "c"),
    Question(spanishQuestions[9], "d"),
     ]

def start_quiz(spanishQuestions):
     score = 0
     counter = 1
     for question in questionsList:
         print(f"Question #{counter}:")
         answer = input(question.prompt + "\n>>> ")
         print()
         if answer == question.answer:
               score += 1
         counter += 1
     print("Congrats!  You earned", score, "out of", len(questionsList))

start_quiz(questionsList)