class Importable:
    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        cols = wf_module.get_param_string('newcolnames').split(',')
        cols = [c.strip() for c in cols]
        wf_module.set_ready(notify=False)
        table.columns = cols
        newtab = table
        return newtab