import pymysql


def adiciona_visualizacao(conn, id_post, id_usuario, aparelho, ip, browser):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Visualizacao (id_post, id_usuario, aparelho, ip, browser) VALUES (%s, %s, %s, %s, %s)",
                           (id_post, id_usuario, aparelho, ip, browser))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir visualizacao')


def lista_visualizacao_por_id_post(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Visualizacao WHERE id_post=%s", (id_post))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def lista_visualizacao_por_id_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Visualizacao WHERE id_usuario=%s", (id_usuario))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def lista_visualizacao_por_aparelho(conn, aparelho):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Visualizacao WHERE aparelho=%s", (aparelho))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def lista_visualizacao_por_ip(conn, ip):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Visualizacao WHERE ip=%s", (ip))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def remove_visualizacao(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'DELETE FROM Visualizacao WHERE id_post=%s AND id_usuario=%s', (id_post, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em visualizacao')
