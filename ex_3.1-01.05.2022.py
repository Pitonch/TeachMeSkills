from pprint import pprint
print('Организация ООО "ЕРО"')
organization_structure = {
    'administration' : {
        'CEO': [{'name': 'Mr.Braun', 'age': 43, 'salary': 5000},
                {'name': 'Mr.Black', 'age': 40, 'salary': 6000}],
        'assistant CEO': [{'name': 'Mr.W', 'age': 40, 'salary': 4000},
                          {'name': 'Mr.P', 'age': 40, 'salary': 4000}],
        'secretary': [{'name': '1', 'age': 25, 'salary': 1500},
                      {'name': '2', 'age': 25, 'salary': 1500},
                      {'name': '3', 'age': 25, 'salary': 1500},
                      {'name': '4', 'age': 25, 'salary': 1500},
                      {'name': '5', 'age': 25, 'salary': 1500},
                      {'name': '6', 'age': 25, 'salary': 1500}]
                        },

    # вверху то что нужно, внизу посложнее реализовано
    'personnel_management_pm' : [{'Chief_pm': {'name': 'Mr.Skott', 'age': 43, 'salary': 1000}},
                                 {'worker_pm_1': {'name': 'Vadim', 'age': 50, 'salary': 1000}},
                                 {'worker_pm_2': {'name': 'Boris', 'age': 45, 'salary': 1000}},
                                 {'worker_pm_3': {'name': 'Juli', 'age': 35, 'salary': 1000}}],
    'development_department_dd' : [{'Chief_dd': {'name': 'Mr.P', 'age': 43, 'salary': 1000}},
                                 {'worker_dd_1': {'name': 'Denis', 'age': 50, 'salary': 2000}},
                                 {'worker_dd_2': {'name': 'Boris', 'age': 45, 'salary': 3000}},
                                 {'worker_dd_3': {'name': 'Olga', 'age': 35, 'salary': 1500}},
                                {'worker_dd_4': {'name': 'Valeri', 'age': 38, 'salary': 1600}},
                                {'worker_dd_5': {'name': 'Larisa', 'age': 37, 'salary': 1800}},
                                {'worker_dd_6': {'name': 'Jenia', 'age': 30, 'salary': 1900}}],
    'operations_department_od' : [{'Chief_od': {'name': 'Mr.S', 'age': 60, 'salary': 6000}},
                                 {'worker_od_1': {'name': 'Qwerty', 'age': 65, 'salary': 1000}},
                                 {'worker_od_2': {'name': 'Asdf', 'age': 48, 'salary': 2500}},
                                 {'worker_od_3': {'name': 'Zxcv', 'age': 43, 'salary': 2600}},
                                {'worker_od_4': {'name': 'Rewq', 'age': 20, 'salary': 600}},
                                {'worker_od_5': {'name': 'Fdsa', 'age': 18, 'salary': 800}}],
    'testing_department_td' : [{'Chief_td': {'name': 'Mr.Q', 'age': 65, 'salary': 10000}},
                                 {'worker_td_1': {'name': 'Pit"', 'age': 65, 'salary': 2000}},
                                 {'worker_td_2': {'name': 'Pet', 'age': 48, 'salary': 2500}},
                                 {'worker_td_3': {'name': 'Vik', 'age': 43, 'salary': 2600}},
                                 {'worker_td_4': {'name': 'Kiva', 'age': 18, 'salary': 800}}],
    'sales_department_sd' : [{'Chief_od': {'name': 'Mr.W', 'age': 50, 'salary': 1050}},
                                 {'worker_sd_1': {'name': 'Qwerty', 'age': 65, 'salary': 2300}},
                                 {'worker_sd_2': {'name': 'Asdf', 'age': 52, 'salary': 5500}},
                                 {'worker_sd_3': {'name': 'Zxcv', 'age': 26, 'salary': 3600}},
                                {'worker_sd_4': {'name': 'Rewq', 'age': 83, 'salary': 1600}},
                                {'worker_sd_5': {'name': 'Fdsa', 'age': 19, 'salary': 1800}}],
}
# добавление отдела с сотрудниками
organization_structure ['stock_department_std'] = {'Chief_od': {'name': 'Mr.S', 'age': 60, 'salary': 6000}}
pprint(organization_structure, depth=1)

# удаление отдела
del organization_structure ['testing_department_td']
pprint(organization_structure, depth=1)

# добавить по одному сотруднику в отдел
organization_structure['sales_department_sd'].append({'worker_sd_6': {'name': '6666', 'age': 666, 'salary': 666}})
pprint(organization_structure, depth=1)

# обращение к определенному сотруднику
print(organization_structure['administration']['CEO'][1])

pprint(organization_structure['administration']['secretary'][])










# administration = [{'CEO': {'name': 'Mr.Braun', 'age': 43, 'salary': 5000}},
#                   {'assistant CEO': {'name': 'Mr.Black', 'age': 40, 'salary': 4000}},
#                   {'secretary': {'name': 'Anna', 'age': 25, 'salary': 1500}}]
# personnel_management_pm = [{'Chief_pm': {'name': 'Mr.Skott', 'age': 43, 'salary': 1000}},
#                                  {'worker_pm_1': {'name': 'Vadim', 'age': 50, 'salary': 1000}},
#                                  {'worker_pm_2': {'name': 'Boris', 'age': 45, 'salary': 1000}},
#                                  {'worker_pm_3': {'name': 'Juli', 'age': 35, 'salary': 1000}}]
# development_department_dd = [{'Chief_dd': {'name': 'Mr.P', 'age': 43, 'salary': 1000}},
#                                  {'worker_dd_1': {'name': 'Denis', 'age': 50, 'salary': 2000}},
#                                  {'worker_dd_2': {'name': 'Boris', 'age': 45, 'salary': 3000}},
#                                  {'worker_dd_3': {'name': 'Olga', 'age': 35, 'salary': 1500}},
#                                 {'worker_dd_4': {'name': 'Valeri', 'age': 38, 'salary': 1600}},
#                                 {'worker_dd_5': {'name': 'Larisa', 'age': 37, 'salary': 1800}},
#                                 {'worker_dd_6': {'name': 'Jenia', 'age': 30, 'salary': 1900}}]
# operations_department_od = [{'Chief_od': {'name': 'Mr.S', 'age': 60, 'salary': 6000}},
#                                  {'worker_od_1': {'name': 'Qwerty', 'age': 65, 'salary': 1000}},
#                                  {'worker_od_2': {'name': 'Asdf', 'age': 48, 'salary': 2500}},
#                                  {'worker_od_3': {'name': 'Zxcv', 'age': 43, 'salary': 2600}},
#                                 {'worker_od_4': {'name': 'Rewq', 'age': 20, 'salary': 600}},
#                                 {'worker_od_5': {'name': 'Fdsa', 'age': 18, 'salary': 800}}]
# testing_department_td = [{'Chief_td': {'name': 'Mr.Q', 'age': 65, 'salary': 10000}},
#                                  {'worker_td_1': {'name': 'Pit"', 'age': 65, 'salary': 2000}},
#                                  {'worker_td_2': {'name': 'Pet', 'age': 48, 'salary': 2500}},
#                                  {'worker_td_3': {'name': 'Vik', 'age': 43, 'salary': 2600}},
#                                  {'worker_td_4': {'name': 'Kiva', 'age': 18, 'salary': 800}}]
# sales_department_sd = [{'Chief_od': {'name': 'Mr.W', 'age': 50, 'salary': 1050}},
#                                  {'worker_sd_1': {'name': 'Qwerty', 'age': 65, 'salary': 2300}},
#                                  {'worker_sd_2': {'name': 'Asdf', 'age': 52, 'salary': 5500}},
#                                  {'worker_sd_3': {'name': 'Zxcv', 'age': 26, 'salary': 3600}},
#                                 {'worker_sd_4': {'name': 'Rewq', 'age': 83, 'salary': 1600}},
#                                 {'worker_sd_5': {'name': 'Fdsa', 'age': 19, 'salary': 1800}}]




