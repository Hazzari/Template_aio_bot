import sqlite3
from dataclasses import dataclass


def logger(statement):
    print(f"""
    -------------------------
    Executing:
    {statement}
    -------------------------
    """)


@dataclass
class Database:
    path_to_db = 'data/main.db'

    @property
    def connection(self):
        """Подключение к database"""
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = tuple(), fetchone=False, fetchall=False, commit=False, ):
        """ """

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        data = None
        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
        id int NOT NULL,
        Name varchar(255) NOT NULL,
        email varchar(255),
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, name: str, email: str = None):
        """
        example:
        sql = "INSERT INTO Users(id, Name, email) VALUES(?, ?, ?)"
        """

        sql = "INSERT INTO Users(id, Name, email) VALUES(?, ?, ?)"
        parameters = (id, name, email)
        self.execute(sql=sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def formats_args(sql, parameters: dict):

        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):

        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.formats_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute(sql="SELECT COUNT(*) FROM Users;", fetchall=True)

    def update_email(self, email, id):
        """
        sql_example = "UPDATE Users SET email=mail@gmail.com WHERE id=123"
        """
        sql = "UPDATE Users SET email=? WHERE id=?"
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_one_user(self, id):
        sql = "DELETE FROM Users WHERE id=?"
        self.execute(sql, parameters=(id,), commit=True)

    def delete_all_users(self, ):
        self.execute("DELETE FROM Users WHERE True")
