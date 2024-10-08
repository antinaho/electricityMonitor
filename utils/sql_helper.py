from psycopg2 import extras
import psycopg2 as p

def batch_execute(cursor, sql_file, params) -> None:
    with open(sql_file, "r") as file:
        command = file.read()
        try:
            extras.execute_batch(cursor, command, params)
        except (Exception, p.DatabaseError) as e:
            print(f"SQL Batch execute error, {e}")

def execute_sql_file(cursor, sql_file_name) -> None:
    with open(sql_file_name, "r") as file:
        sql_commands = file.read().split(";")
        for command in sql_commands:
            try:
                cursor.execute(command)
            except (Exception, p.DatabaseError) as e:
                print(f"SQL execute error, {e}")

def execute_command(cursor, command) -> None:
    try:
        cursor.execute(command)
    except (Exception, p.DatabaseError) as e:
        print(f"SQL execute error, {e}")