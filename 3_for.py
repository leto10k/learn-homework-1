"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

marks = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '7a', 'scores': [5,3,4,3,2]},
        {'school_class': '10b', 'scores': [4,2,5,5,3]},
        {'school_class': '1a', 'scores': [5,5,5,5,5]},
        {'school_class': '9b', 'scores': [3,2,2,3,2]},]

def main(marks):

    srednii_ball = 0

    for i in marks:
        print(f"Среднией балл класса {i['school_class']}: {sum(i['scores'])/len(i['scores'])}")
        srednii_ball += sum(i['scores'])/len(i['scores'])

    print(f"Средний балл по  всей школе: {srednii_ball / len(marks)}")
    
if __name__ == "__main__":
    main(marks)