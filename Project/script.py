import json


class Script:
    def __init__(self, name):
        self._name = name
        self.actions = {}

    def add_case(self, l, t, d, r, rest=False):
        self.actions['action' + str(len(self.actions) + 1)] = {'label': l,
                                                               'text': t,
                                                               'duration': d,
                                                               'record': r}
        if rest:
            self.add_rest()

    def add_rest(self, d):
        self.actions['rest'] = {'label': None,
                                'text': 'rest',
                                'duration': d,
                                'record': False}

    def save_script(self):
        with open('scripts\\' + str(self._name) + '.json', 'w') as file:
            json.dump(self.actions, file, indent=2)

    def make_str(self):
        res_str = ''
        for act in self.actions.keys():
            res_str += act + '\n'
            for a in self.actions[act].items():
                res_str += '  ' + str(a) + '\n'
        return res_str
