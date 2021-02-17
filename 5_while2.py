"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'Лучший язык программирования?': 'Python',
                        'Как тебя зовут?': 'Алиса', 'Какой год?': '2021'}

def ask_user(answers_dict):

    while True:
        question = input('Задай мне вопрос: \n')
        if question in answers_dict.keys():
            print(answers_dict[question])
        elif question == 'Пока':
            print('До свидания!')
            break
        else:    
            print('Ответа на этот вопрос у меня нету')
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
