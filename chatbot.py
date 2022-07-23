#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#a chatbot to solve basic queries to solve knowledge issues
answers = {
    "HR" : "go to human resource management system",
    "CIRCULAR": "go to circulars page"
}

def questions(ques):
    for a in answers.keys():
        if a in question.upper():
            print(answers[a])

question = input(str("Heyy how can i help you: "))
questions(question)

# In[ ]:


def feedback(feed):
    feedback = input(str("Was i able to solve your query?: "))
    if feedback.upper()[0] == "Y":
        print("I am glad to hear that! Do revisit")
    else:
        improvement = input(str("Can you give me a minute to help me improve my understanding skill?: "))
        if improvement.upper()[0] == "Y":
            key = input(str("Define your query in one keyword?: "))
            keyword_answer = input(str("Which site would have solved the query: "))
            answers[key] = keyword_answer
        elif improvement.upper()[0] == "N":
            print("I will be better next time you visit me! :-)")
        else:
            print("Sorry I couldnot understand what you are saying!")
feedback(question)




# In[ ]:




