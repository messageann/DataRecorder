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

    def add_rest(self, d):
        self.actions['rest' + str(len(self.actions) + 1)] = {'label': None,
                                                             'text': 'rest',
                                                             'duration': d,
                                                             'record': False}

    def save_script(self):
        exist = []
        number = ''
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
        if len(exist) > 0:
            exist.insert(0, 0)
            for i in range(len(exist)):
                if i != int(exist[i]):
                    number = ' (' + str(i) + ')'
                    break
                else:
                    number = ' (' + str(len(exist)) + ')'
        with open('scripts\\' + str(self.name) + number + '.json', 'w') as file:
            json.dump(self.actions, file, indent=2)

    def make_str(self):
        res_str = ''
        for act in self.actions.keys():
            res_str += act + '\n'
            for a in self.actions[act].items():
                res_str += '  ' + str(a) + '\n'
        return res_str
