import json
import os


class Script:
    def __init__(self, name):
        self.name = name
        self.actions = {}

    def add_case(self, l, t, d, r, rest=False):
        self.actions['action' + str(len(self.actions) + 1)] = {'label': l,
                                                               'text': t,
                                                               'duration': d,
                                                               'record': r}
        if rest:
            self.add_rest()

    def add_case_before(self, l, t, d, r, curr_key):
        add = {'label': l, 'text': t, 'duration': d, 'record': r}
        temp, i = {}, 1
        for key, value in self.actions.items():
            if key == curr_key:
                temp['action' + str(i)] = add
                i += 1
                temp['action' + str(i)] = value
            else:
                temp['action' + str(i)] = value
            i += 1
        self.actions = temp
        del temp

    def add_rest(self, d):
        self.actions['action' + str(len(self.actions) + 1)] = {'label': None,
                                                             'text': 'Отдых',
                                                             'duration': d,
                                                             'record': False}

    def delete_action(self, key):
        del self.actions[key]
        temp, i = {}, 1
        for key, value in self.actions.items():
            if key[-1] != str(i):
                temp[key[:len(key) - 1] + str(i)] = value
            else:
                temp[key] = value
            i += 1
        self.actions = temp
        del temp

    def save_script(self):
        number = ''
        if os.path.exists(os.getcwd() + '\\scripts\\' + self.name + '.json'):
            exist = []
            sc = os.listdir(os.getcwd() + '\\scripts')
            for file in sc:
                if self.name in os.path.splitext(file)[0]:
                    if self.name == os.path.splitext(file)[0]:
                        number = ' (1)'
                    else:
                        if len(os.path.splitext(file)[0]) > 2:
                            exist.append(os.path.splitext(file)[0][-2:-1])
                        else:
                            exist.append(os.path.splitext(file)[0][-1])
            print(exist)
            if len(exist) > 0:
                for i in range(len(exist)):
                    if i != int(exist[i])-1:
                        number = ' (' + str(i+1) + ')'
                        break
                    else:
                        number = ' (' + str(len(exist)+1) + ')'
        with open('scripts\\' + str(self.name) + number + '.json', 'w') as file:
            json.dump(self.actions, file, indent=2)

    def make_str(self):
        res_str = ''
        for act in self.actions.keys():
            res_str += act + '\n'
            for a in self.actions[act].items():
                res_str += '  ' + str(a) + '\n'
        return res_str

