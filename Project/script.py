import json
import os
import re


class Script:
    def __init__(self, name):
        self.name = name
        self.actions = {}

    def add_case(self, l, t, d, r, rest=False):
        if not r:
            l = ''
        self.actions[str(len(self.actions))] = {'label': l,
                                                'text': t,
                                                'duration': d,
                                                'record': r}
        if rest:
            self.add_rest()

    def add_case_before(self, l, t, d, r, curr_key):
        add = {'label': l, 'text': t, 'duration': d, 'record': r}
        temp, i = {}, 0
        for key, value in self.actions.items():
            if key == curr_key:
                temp[str(i)] = add
                i += 1
                temp[str(i)] = value
            else:
                temp[str(i)] = value
            i += 1
        self.actions = temp
        del temp

    def up(self, curr_act):
        if curr_act != 0:
            self.actions[str(curr_act-1)], self.actions[str(curr_act)] = self.actions[str(curr_act)], self.actions[str(curr_act-1)]


    def down(self, curr_act):
        if curr_act != len(self.actions)-1:
            self.actions[str(curr_act+1)], self.actions[str(curr_act)] = self.actions[str(curr_act)], self.actions[str(curr_act+1)]


    def delete_action(self, key):
        del self.actions[key]
        temp, i = {}, 0
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
            exist = [0]
            undone = True
            sc = os.listdir(os.getcwd() + '\\scripts')
            for file in sc:
                match = re.search(re.escape(self.name) + '(\((?P<count>\d+)\))?', file)
                if match is not None and match.group('count') is not None:
                    exist.append(int(match.group('count')))
                if int(exist[-1]) != len(exist) - 1:
                    number = '(' + str(len(exist) - 1) + ')'
                    undone = False
                    break
            if undone:
                number = '(' + str(len(exist)) + ')'
            del exist
        with open('scripts\\' + str(self.name) + number + '.json', 'w') as file:
            json.dump(self.actions, file, indent=2)

    def get_acts(self):
        acts = []
        for key in self.actions.keys():
            acts.append(self.actions[key]['text'])
        return acts
