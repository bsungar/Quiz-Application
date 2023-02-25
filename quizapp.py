# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer
# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionindex = 0
    def getQuestion(self):
        return self.questions[self.questionindex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionindex + 1}: {question.text}")
        for q in question.choices:
            print("-" + q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()
    
    
    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score +=1
        self.questionindex +=1


    def loadQuestion(self):
        if len(self.questions) == self.questionindex:
            self.showScore()
        else:
            self.showProgress()
            self.displayQuestion()

    def showScore(self):
        print("score: ", self.score)
    def showProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionindex +1
        if(questionNumber > totalQuestion):
            print("Quiz bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))
      
    

q1 = Question("En iyi programlama dili hangisidir?", ["c#","python","javascript","java"], "python")
q2 = Question("Limon ne renktir?", ["Sarı","Turuncu","Yeşil"], "Sarı")
q3 = Question("Manisa hangi bölgededir?", ["Marmara","Ege","Akdeniz"], "Ege")
questions = [q1,q2,q3]

quiz =  Quiz(questions)
question = quiz.getQuestion()
quiz.loadQuestion()