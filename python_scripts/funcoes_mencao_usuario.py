import pymysql


def adiciona_mencao_usuario(conn, id_post, id_usuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO mencao_usuario (id_post, id_usuario) VALUES (%s, %s)",
                           (id_post, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir mencao usuario')


def lista_mencao_usuario_por_id_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id_post FROM mencao_usuario WHERE id_usuario=%s", (id_usuario))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def lista_mencao_usuario_por_id_post(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id_usuario FROM mencao_usuario WHERE id_post=%s", (id_post))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def remove_mencao_usuario(conn, id_post, id_usuario):
    with conn.cursor as cursor:
        try:
            cursor.execute(
                'DELETE FROM mencao_usuario WHERE id_post=%s AND id_usuario=%s', (id_post, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em mencao usuario')
