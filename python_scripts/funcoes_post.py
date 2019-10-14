import pymysql


def adiciona_post(conn, id_usuario, titulo, texto, url_imagem):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO post (id_usuario, titulo, texto, url_imagem, ativo) VALUES (%s, %s, %s, %s, %s)",
                           (id_usuario, titulo, texto, url_imagem, 1))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir post')


def acha_post_info_por_id(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id_usuario, titulo, texto, url_imagem FROM post WHERE id_post=%s", (id_post))
        res = cursor.fetchall()
        if res:
            return res[0]
        else:
            return None


def acha_post_ativo_por_id(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute("SELECT ativo FROM post WHERE id_post=%s", (id_post))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None


def lista_post_id_por_id_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id_post FROM post WHERE id_usuario=%s", (id_usuario))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def lista_post_id_por_palavra(conn, palavra):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id_post FROM post WHERE texto LIKE %{$%s}", (palavra))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def update_post_titulo(conn, id_post, titulo):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE post SET titulo=%s where id_post=%s", (titulo, id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em post')


def update_post_texto(conn, id_post, texto):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE post SET texto=%s where id_post=%s", (texto, id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em post')


def update_post_url_imagem(conn, id_post, url_imagem):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE post SET url_imagem=%s where id_post=%s", (url_imagem, id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em post')


def update_post_ativo(conn, id_post, ativo):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE post SET ativo=%s where id_post=%s", (ativo, id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em post')


def remove_post(conn, id_post):
    with conn.cursor() as cursor:
        try:
            cursor.execute('DELETE FROM post WHERE id_post=%s', (id_post))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em post')
