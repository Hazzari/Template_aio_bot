from utils.db_api.sqlite import Database

db = Database()


def test():
    db.create_table_users()
    users = db.select_all_users()
    print('До добавления:', users)
    db.add_user(1, 'One', 'email@mail.dsa')
    db.add_user(2, 'Vasya', 'vv@mail.vv')
    db.add_user(3, 1, 1)
    db.add_user(4, 1, 1)
    db.add_user(5, 'john', 'john@gmail.com')

    users = db.select_all_users()
    print('После добавления:', users)
    user = db.select_user(Name='john', id=5)
    print('Получил пользователя', user)


test()
