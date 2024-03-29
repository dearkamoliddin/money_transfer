import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, query_type, fetchall=False, fetchone=False, fetchmany=False):
        database = db.connect(
            database="bank",
            host="localhost",
            user="postgres",
            password="8991"
        )
        curses = database.cursor()
        curses.execute(query=query)

        query_types = ["insert", "update", "delete", "create"]
        if query_type in query_types:
            database.commit()
            return "Done"
        else:
            if fetchall:
                return curses.fetchall()
            elif fetchone:
                return curses.fetchone()
            elif fetchmany:
                return curses.fetchmany()
            return curses.fetchall()