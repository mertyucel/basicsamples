import random

class Question:

    def __init__(self,text,choices,answer) -> None:
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        if (answer not in self.choices):
            raise ValueError("Hatalı Bilgi")
        return answer == self.answer

class Quiz:

    def __init__(self,questions) -> None:
        self.questions = random.sample(questions,len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-"+q)
        answer = input("Cevap :")

        if(question.checkAnswer(answer)):
            self.score += 1    
            print("Tebrikler bildiniz")
        self.questionIndex += 1
        self.loadQuestion()
        
    def loadQuestion(self):    
        if (len(questions) == self.questionIndex):
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayScore(self):
        print("Test özetiniz : ".center(100,'*'))
        puan = 100 / len(self.questions)
        toplamPuan = round(self.score * puan)
        print(f"Toplam {len(self.questions)} sorudan {self.score} tanesini bildiniz")
        print("Kazandığınız Puan :",toplamPuan)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumer = self.questionIndex+1

        print(f" Toplam {totalQuestion} sorunun {questionNumer}. sorusundasınız ".center(100,'*'))

q1 = Question("En iyi programlama dili hangisidir?",["PHP","JAVA","GO","PYTHON","C#"],"PYTHON")
q2 = Question("En hızlı programlama dili hangisidir?",["JAVA","GO","PYTHON","C#","PHP"],"GO")
q3 = Question("En zor programlama dili hangisidir?",["GO","PHP","JAVA","PYTHON","C#"],"JAVA")
q4 = Question("En sevilen programlama dili hangisidir?",["GO","PHP","JAVA","PYTHON","C#"],"C#")
q5 = Question("En kolay programlama dili hangisidir?",["GO","PHP","JAVA","PYTHON","C#"],"PYTHON")

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)
quiz.loadQuestion()

