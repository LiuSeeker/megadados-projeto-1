import pymysql

def adiciona_pro_joinha(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Joinha (id_post, id_usuario, pro_joinha) VALUES (%s, %s, %s)",
                (id_post, id_usuario, "1"))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir joinha')

def adiciona_anti_joinha(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Joinha (id_post, id_usuario, anti_joinha) VALUES (%s, %s, %s)",
                (id_post, id_usuario, "1"))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir joinha')

def lista_todos_joinha_por_id_post(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Joinha WHERE id_post=%s", (id_post))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

def lista_pro_joinha_por_id_post(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Joinha WHERE id_post=%s AND pro_joinha=1", (id_post))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

def lista_anti_joinha_por_id_post(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Joinha WHERE id_post=%s AND anti_joinha=1", (id_post))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def lista_todos_joinha_por_id_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Joinha WHERE id_usuario=%s", (id_usuario))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

def lista_pro_joinha_por_id_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Joinha WHERE id_usuario=%s AND pro_joinha=1", (id_usuario))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

def lista_anti_joinha_por_id_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Joinha WHERE id_usuario=%s AND anti_joinha=1", (id_usuario))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

def update_pro_joinha(conn, id_post, pro_joinha):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'UPDATE joinha SET pro_joinha=%s WHERE id_post=%s', (pro_joinha, id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em joinha')

def update_anti_joinha(conn, id_post, anti_joinha):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'UPDATE joinha SET anti_joinha=%s WHERE id_post=%s', (anti_joinha, id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em joinha')

def remove_joinha(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'DELETE FROM Joinha WHERE id_post=%s AND id_usuario=%s', (id_post, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em joinha')

def remove_joinha_por_post(conn, id_post):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'DELETE FROM Joinha WHERE id_post=%s', (id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em joinha')

def remove_joinha_por_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'DELETE FROM Joinha WHERE id_usuario=%s', (id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em joinha')