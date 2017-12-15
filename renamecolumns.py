def render(table, params):

    names = params['newcolnames']
    if names is None or names.strip() == '':
        return table

    try:
        name_dict = json.loads(names)
    except json.JSONDecodeError:
        return table

    # dict tells us old and new column names. Ignore any columns that no longer exist.
    cols = [str(c) for c in table.columns]
    newcols = cols.copy()
    for i,c in enumerate(cols):
      if c in name_dict:
          newcols[i] = name_dict[c]

    table.columns = newcols

    return table
