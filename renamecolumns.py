class Importable:
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        cols = wf_module.get_param_string('newcolnames').split(',')
        cols = [c.strip() for c in cols]
        wf_module.set_ready(notify=False)
        if len(cols) != 1 or cols[0] != '':
            table.columns = cols
        newtab = table
        return newtab