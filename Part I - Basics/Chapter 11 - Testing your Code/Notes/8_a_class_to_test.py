"""
Testing a class is similar to testing a function- Much of your work involves
testing the behaviour of the methods in the class. But there are a few
differences, so let's write a class to test. Consider a class that helps
administer anonymous surveys:
"""
# This is the code found in file survey.py

# class AnonymousSurvey():
#     """Collect anonymous answers to a survey question."""

#     def __init__(self, question):
#         """Store a question, and prepare to store responses."""
#         self.question = question
#         self.responses = []

#     def show_question(self):
#         """Show the survey question."""
#         print(self.question)

#     def store_response(self, new_response):
#         """Store a single response to the survey."""
#         self.responses.append(new_response)

#     def show_results(self):
#         """Show all the responses that have been given."""
#         print("Survey results:")
#         for response in self.responses:
#             print("- " + response)
"""
This class starts with a survey question that you provide(line 12) and
includes an empty list to store responses. The class has methods to print the
survey question(line 17), add a new response to the response list(line 21),
and print all the responses stored in the list(line 25). To create an instance
from this class, all you have to provide is a question.

Once you have an instance representing a particular survey, you
display the survey question with show_question(), store a response using
store_response(), and show results with show_results().

To show that the AnonymousSurvey class works, let's write a program that uses the
class:
"""
# This is the code found in language_survey.py

# from survey import AnonymousSurvey

# # Define a question, and make a survey.
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)

# # Show the question, and store responses to the question.
# my_survey.show_question()

# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         None
#         break
#     my_survey.store_response(response.title())

# # Show the survey results.
# print("\nThank you to everyone who participated in the survey!")
#     my_survey.show_results()

"""
This program defines a question("What language did you first learn to speak?")
and creates an AnonymousSurvey object with that question. The program calls 
show_question() to display the question and then prompts for responses. Each
response is stored as it is received. When all responses have been entered
(The user inputs 'q' to quit), show_results() prints the survey results:

==============================================================
|                                                            |
|   # What language did you first learn to speak?            |
|   # Enter 'q' at any time to quit.                         |
|                                                            |
|   # Language: english                                      |
|   # Language: french                                       |
|   # Language: q                                            |
|                                                            |
|   # Thank you to everyone who participated in the survey!  |
|   # Survey results:                                        |
|   # - English                                              |
|   # - French                                               |
==============================================================

This class works for a simple anonymous survey. But let's say we want to 
improve AnonymousSurvey and the module it's in, survey. We could allow each
user to enter more than one response. We could write a emthod to list only unique 
responses and to report how many  times each response was given. We could write 
another class to manage nonanonymous surveys. 

Implementing such changes would risk affecting the current behavior of the class
AnonymousSurvey. For example, it's possible that while trying to allow each user
to enter multiple responses, we could accidentally change how single responses
are handled. To ensure we don't break existing behaviour as we develop this module, 
we can write tests for the class.
"""
