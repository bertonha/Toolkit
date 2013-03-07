def format_input(value):
    if value.startswith('#'):
        return value[1:]
    elif value == '':
        return 'null'
    elif value.isnumeric():
        return value
    else:
        return "'%s'" % value


def read_file(upload_file):
    data = upload_file.read()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = data.decode("latin1")
    return text.splitlines()


def read_csv(upload_file):
    data = read_file(upload_file)
    headers = data[0].split(',')
    values = []
    for line in data[1:]:
        fields = line.split(',')
        row = [format_input(field) for field in fields]
        values.append(row)
    return (headers, values)


def generate_insert_sql(table, headers, values):
    sql = []
    for row in values:
        sql.append("INSERT INTO %s (%s) VALUES (%s);\n\n" %
                   (table, ', '.join(headers), ', '.join(row)))
    sql.append("COMMIT;\n")
    return sql
