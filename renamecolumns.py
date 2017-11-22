def render(table, params):
    cols = params['newcolnames'].split(',')
    cols = [c.strip() for c in cols]
    if len(cols) != 1 or cols[0] != '':
        table.columns = cols
    return table
