"""
Functions used by the math education game app.
These functions must be called from the main.py file, as appropriate.
"""

import random


def roll_die():
    """
    Generates a pseudo-random integer between the 1 and 6, inclusive.
    Use the function random.randint() to generate the pseudo-random number.

    :returns: the pseudo-random integer.
    """
    return random.randint(1, 6)


def get_question_type():
    """
    Pseudo-randomly decides whether to give an addition question or a subtraction question.
    Use the function random.randint() to generate a pseudo-random number between 1 and 6, inclusive, that is used to determine the question type.

    :returns: "sum" for an addition question, "difference" for a subtraction question.
    """
    number = random.randint(1, 6)

    if number <= 3:
        return "sum"
    else:
        return "difference"


def print_question(die_1_value, die_2_value, question_type):
    """
    Prints out a math question that asks the user to calculate either the sum or difference of the two numbers rolled on virtual dice.
    """
    if question_type == "sum":
        print("You rolled a {} and a {}... What is the sum of {} and {}?".format(
            die_1_value, die_2_value, die_1_value, die_2_value
        ))
    else:
        print("You rolled a {} and a {}... What is the difference between {} and {}?".format(
            die_1_value, die_2_value, die_1_value, die_2_value
        ))


def input_answer():
    """
    Asks the user to enter their answer to the most recent question.
    """
    answer = input("Enter your answer: ")
    answer = answer.strip()

    if answer.isdigit():
        return int(answer)
    else:
        return -1


def is_correct_answer(die_1_value, die_2_value, question_type, given_answer):
    """
    Determines whether the user's given answer to a question is correct.
    """
    if question_type == "sum":
        correct_answer = die_1_value + die_2_value
    else:
        correct_answer = abs(die_1_value - die_2_value)

    return given_answer == correct_answer


def print_congratulations(question_type):
    """
    Congratules the user for answering a question correctly.
    """
    if question_type == "sum":
        print("Yes! Congratulations on the successful addition!")
    else:
        print("Yes! Congratulations on the successful subtraction!")


def print_correct_answer(die_1_value, die_2_value, question_type):
    """
    Prints the correct answer to the question.
    """
    if question_type == "sum":
        correct_answer = die_1_value + die_2_value
        print("No! The sum of {} and {} is {}!".format(
            die_1_value, die_2_value, correct_answer
        ))
    else:
        correct_answer = abs(die_1_value - die_2_value)
        print("No! The difference between {} and {} is {}!".format(
            die_1_value, die_2_value, correct_answer
        ))


def print_error_message():
    """
    Prints an error message indicating that the user has given an invalid response.
    """
    print("Sorry - that is an invalid answer.  Bye Bye!")