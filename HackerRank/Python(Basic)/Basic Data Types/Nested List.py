if __name__ == '__main__':
    nested_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        nested_list.append([name, score])

    grades = set([grade[1] for grade in nested_list])
    grades_list = sorted(list(grades))

    second_lowest_grade = grades_list[1]

    names = sorted([p[0] for p in nested_list if p[1] == second_lowest_grade])

    for name in names:
        print(name)

