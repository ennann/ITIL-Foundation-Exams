import random
import datetime


# generate the question number
question_num_list = random.sample(range(1, 199), 40)
print(question_num_list)

# get question from json file
import json


def read_json():
    with open("/Users/Elton/Code-stuff/pythonlearning/itil_foundation/questions_and_answers.json") as f:
        pop_data = json.load(f)
        return pop_data


# get the json data
questions_dict = read_json()


# generate 40 random questions
def generate_questions(question_num_list, questions_dict):
    generated_questions = {}
    generated_answers = {}

    # get the questions
    for i in range(1, 41):
        question_num = question_num_list[i - 1]
        single_question = questions_dict[str(question_num)]
        print(single_question)
        generated_questions[i] = single_question

    # get the answers
    for i in question_num_list:
        single_answer = questions_dict[str(i)]["answer"]
        generated_answers[i] = single_answer

    return generated_questions, generated_answers


question_list, answers_list = generate_questions(question_num_list, questions_dict)
# print("数据类型为：", type(question_list), type(answers_list))
# print(question_list, "\n", answers_list)


# for loop the question_list and print the questions and choices and answers
def print_questions(question_list, answers_list):
    for i in range(1, 41):
        single_question = question_list[i]
        question = single_question["question"].split(".", 1)[1].strip()
        choice_a = single_question["choice"]["choice_a"]
        choice_b = single_question["choice"]["choice_b"]
        choice_c = single_question["choice"]["choice_c"]
        choice_d = single_question["choice"]["choice_d"]
        print(i, question, '\n', 'A.', choice_a, '\n', 'B.', choice_b, '\n', 'C.', choice_c, '\n', 'D.', choice_d, '\n', )

    # get all the answers from the dict, print the answers for ten in a line
    answers_list = list(answers_list.values())
    for i in range(0, 40, 10):
        print(f"{i + 1} - {i + 10}", str.join("", answers_list[i:i + 5]), str.join("", answers_list[i + 5:i + 10]))






# print_questions(question_list, answers_list)

# write to txt file
def write_to_txt(question_list, answers_list):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S');

    with open(f"/Users/Elton/Code-stuff/pythonlearning/itil_foundation/exam_{date}.txt", "w") as f:
        for i in range(1, 41):
            single_question = question_list[i]
            question = single_question["question"].split(".", 1)[1].strip()
            choice_a = single_question["choice"]["choice_a"]
            choice_b = single_question["choice"]["choice_b"]
            choice_c = single_question["choice"]["choice_c"]
            choice_d = single_question["choice"]["choice_d"]

            f.write(f"{i} {question} \n A. {choice_a} \n B. {choice_b} \n C. {choice_c} \n D. {choice_d} \n")
            f.write("\n")

        f.write("\n\n\n\n\n\n\n\n\n\n\n\n")

        # get all the answers from the dict, print the answers for ten in a line
        answers_list = list(answers_list.values())
        for i in range(0, 40, 10):
            f.write(f"{i + 1} - {i + 10} {str.join('', answers_list[i:i + 5])} {str.join('', answers_list[i + 5:i + 10])} \n")



write_to_txt(question_list, answers_list)