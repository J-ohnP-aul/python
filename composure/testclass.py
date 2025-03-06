import unittest as tst

class AnonymousSurvey():
    def __init__(self,question):        
        '''store questions and prepare to sstore answers'''
        self.question = question
        self.response = []    
    def showQuiz(self):
        '''show survey quiestion'''
        print(question)
        
    def store_response(self, new_response):
        '''store single response to the survey'''
        self.response.append(new_response)
        
    def show_results(self):
        '''show all the response that are given'''
        print("survey results:")
        for respons in response:
            print('- '+ respons)