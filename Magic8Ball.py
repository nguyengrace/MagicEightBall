'''
Name: Grace Nguyen
U-Number: U86550360
Description: The program simulates a magic 8 ball toy as it prompts the user to
ask a question, and gives the user a result to their question based on a randomly
chosen response from the list of 20 standard answers. Once the answer has been
given, the program will ask the user if they want to ask another question. So long
as the user answers anything but "no", the questions and answers will continue.
'''

import random

def results(response):
    results = ['It is certain.', 'It is decidedly so.', 'Without a doubt.',\
               'Yes = definitely.', 'You may rely on it.', 'As I see it, yes.',\
               'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',\
               'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',\
               'Cannot predict now.', 'Concentrate and ask again.',\
               "Don't count on it.", "My reply is no.", 'My sources say no.',\
               'Outlook not so good.', 'Very doubtful.']
    print(results[response])

def main():
    question = input('What is your question? ')
    response = random.randint(0, 19)
    results(response)
    question = str.casefold(input('Would you like to ask another question? '))
    while question != 'no' :
        question = input('What is your question? ')
        response = random.randint(0, 19)
        results(response)
        question = str.casefold(input('Would you like to ask another question? '))

main()

    
