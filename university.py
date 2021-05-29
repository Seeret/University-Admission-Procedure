max_app = int(input())
all_app, del_list = [], []
bio, chem, engineer, math, phys, = [], [], [], [], []
bio_temp, chem_temp, engineer_temp, math_temp, phys_temp = [], [], [], [], []
list_of_main = [bio, chem, engineer, math, phys]
list_of_temp = [bio_temp, chem_temp, engineer_temp, math_temp, phys_temp]
list_of_exam1 = ['chem_exam', 'chem_exam', 'it_exam', 'math_exam', 'phys_exam']
list_of_exam2 = ['phys_exam', 'chem_exam', 'math_exam', 'math_exam', 'math_exam']


def del_app():
    for i in del_list:
        all_app.remove(i)
    del_list.clear()


def sort(lst, test1, test2):
    lst.sort(key=lambda x: (x['name'], x['surname']))
    lst.sort(reverse=True, key=lambda x: max((x[test1] + x[test2]) / 2, x['adm_exam']))


def append(main, tmp):
    for inc in tmp:
        if len(main) < max_app:
            main.append(inc)
            del_list.append(inc)


def check(dep):
    for el in all_app:
        if el.get(dep) == 'Biotech':
            bio_temp.append(el)
        elif el.get(dep) == 'Chemistry':
            chem_temp.append(el)
        elif el.get(dep) == 'Engineering':
            engineer_temp.append(el)
        elif el.get(dep) == 'Mathematics':
            math_temp.append(el)
        elif el.get(dep) == 'Physics':
            phys_temp.append(el)


def cycle(dep):
    check(dep)
    list(map(sort, list_of_temp, list_of_exam1, list_of_exam2))
    list(map(append, list_of_main, list_of_temp))
    del_app()
    list(map(lambda x: x.clear(), list_of_temp))


with open('applicant_list_7.txt', 'r') as f:
    for line in f:
        temp = line.split()
        all_app.append({'name': temp[0], 'surname': temp[1], 'phys_exam': float(temp[2]), 'chem_exam': float(temp[3]),
                        'math_exam': float(temp[4]), 'it_exam': float(temp[5]), 'adm_exam': float(temp[6]),
                        'first_dep': temp[7], 'second_dep': temp[8], 'third_dep': temp[9]})
cycle('first_dep')
cycle('second_dep')
cycle('third_dep')
list(map(sort, list_of_main, list_of_exam1, list_of_exam2))
with open('Biotech.txt', 'w') as f:
    for app in bio:
        f.write(app.get('name') + ' ' + app.get('surname') + ' '
                + str(max((app.get('chem_exam') + app.get('phys_exam')) / 2, app.get('adm_exam'))) + '\n')
with open('Chemistry.txt', 'w') as f:
    for app in chem:
        f.write(app.get('name') + ' ' + app.get('surname') + ' '
                + str(max(app.get('chem_exam'), app.get('adm_exam'))) + '\n')
with open('Engineering.txt', 'w') as f:
    for app in engineer:
        f.write(app.get('name') + ' ' + app.get('surname') + ' '
                + str(max((app.get('it_exam') + app.get('math_exam')) / 2, app.get('adm_exam'))) + '\n')
with open('Mathematics.txt', 'w') as f:
    for app in math:
        f.write(app.get('name') + ' ' + app.get('surname') + ' '
                + str(max(app.get('math_exam'), app.get('adm_exam'))) + '\n')
with open('Physics.txt', 'w') as f:
    for app in phys:
        f.write(app.get('name') + ' ' + app.get('surname') + ' '
                + str(max((app.get('math_exam') + app.get('phys_exam')) / 2, app.get('adm_exam'))) + '\n')
