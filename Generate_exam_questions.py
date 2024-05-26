import random
import datetime
import json
import os


# generate the question number
question_num_list = random.sample(range(1, 199), 40)
print(question_num_list)

# get question from json file
def read_json(file_path):
    with open(file_path) as f:
        pop_data = json.load(f)
        return pop_data

# Relative path or use environment variable to manage the path
base_dir = os.path.dirname(__file__)  # Get the directory of the current script
json_file_path = os.path.join(base_dir, "questions_and_answers.json")

# get the json data
questions_dict = read_json(json_file_path)

# generate 40 random questions
def generate_questions(question_num_list, questions_dict):
    generated_questions = {}
    generated_answers = {}

    # get the questions
    for i, question_num in enumerate(question_num_list, 1):
        single_question = questions_dict[str(question_num)]
        generated_questions[i] = single_question

    # get the answers
    for i in question_num_list:
        single_answer = questions_dict[str(i)]["answer"]
        generated_answers[i] = single_answer

    return generated_questions, generated_answers

question_list, answers_list = generate_questions(question_num_list, questions_dict)

# for loop the question_list and print the questions and choices and answers
def print_questions(question_list, answers_list):
    for i in range(1, 41):
        single_question = question_list[i]
        question = single_question["question"].split(".", 1)[1].strip()
        choice_a = single_question["choice"]["choice_a"]
        choice_b = single_question["choice"]["choice_b"]
        choice_c = single_question["choice"]["choice_c"]
        choice_d = single_question["choice"]["choice_d"]
        print(f"{i}. {question}\nA. {choice_a}\nB. {choice_b}\nC. {choice_c}\nD. {choice_d}\n")

    # get all the answers from the dict, print the answers for ten in a line
    answers_list_values = list(answers_list.values())
    for i in range(0, 40, 10):
        print(f"{i + 1} - {i + 10} {' '.join(answers_list_values[i:i + 5])} {' '.join(answers_list_values[i + 5:i + 10])}")

# print_questions(question_list, answers_list)

# write to txt file
def write_to_txt(question_list, answers_list, output_dir):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')
    file_path = os.path.join(output_dir, f"exam_{date}.txt")

    with open(file_path, "w") as f:
        for i in range(1, 41):
            single_question = question_list[i]
            question = single_question["question"].split(".", 1)[1].strip()
            choice_a = single_question["choice"]["choice_a"]
            choice_b = single_question["choice"]["choice_b"]
            choice_c = single_question["choice"]["choice_c"]
            choice_d = single_question["choice"]["choice_d"]

            f.write(f"{i}. {question}\nA. {choice_a}\nB. {choice_b}\nC. {choice_c}\nD. {choice_d}\n\n")

        f.write("\n\n\n\n\n\n\n\n\n\n\n\n")

        # get all the answers from the dict, print the answers for ten in a line
        answers_list_values = list(answers_list.values())
        for i in range(0, 40, 10):
            f.write(f"{i + 1} - {i + 10} {' '.join(answers_list_values[i:i + 5])} {' '.join(answers_list_values[i + 5:i + 10])}\n")

output_dir = base_dir  # You can customize the output directory
write_to_txt(question_list, answers_list, output_dir)
