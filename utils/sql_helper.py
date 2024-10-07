from psycopg2 import extras
import psycopg2 as p

def execute_sql_file(filename, cursor, params=None) -> None:
    with open(filename, "r") as file:
        sql = file.read()

        commands = sql.split(";")
        for command in commands:
            if params:
                execute_sql_file_with_params(command, cursor, params)
                continue

            try:
                cursor.execute(command)
            except (Exception, p.DatabaseError) as e:
                ...


def execute_sql_file_with_params(command, cursor, params) -> None:
    try:
        extras.execute_batch(cursor, command, params)
    except (Exception, p.DatabaseError) as e:
        ...