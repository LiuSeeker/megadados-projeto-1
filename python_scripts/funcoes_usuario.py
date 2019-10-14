import pymysql


def adiciona_usuario(conn, nome, sobrenome, username, email, cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO usuario (nome, sobrenome, username, email, cidade, ativo) VALUES (%s, %s, %s, %s, %s, %s)",
                           (nome, sobrenome, username, email, cidade, "1"))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir usuário')


def acha_usuario_info_por_id(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT nome, sobrenome, username, email, cidade FROM usuario WHERE id_usuario=%s", (id_usuario))
        res = cursor.fetchall()
        if res:
            return res[0]
        else:
            return None


def acha_usuario_id_por_username(conn, username):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id_usuario FROM usuario WHERE username=%s", (username))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None


def acha_usuario_ativo_por_id(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT ativo FROM usuario WHERE id_usuario=%s", (id_usuario))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None


def lista_usuario_usernames(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT username FROM usuario")
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def lista_usuario_usernames_por_cidade(conn, cidade):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT username FROM usuario WHERE cidade=%s", (cidade))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def lista_usuario_username_por_nome_e_sobrenome(conn, nome, sobrenome):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT username FROM usuario WHERE nome=%s AND sobrenome=%s", (nome, sobrenome))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def lista_usuario_username_por_palavra(conn, palavra):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT username FROM usuario WHERE username LIKE %{$%s}", (palavra))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def update_usuario_nome(conn, id_usuario, nome):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE usuario SET nome=%s where id_usuario=%s", (nome, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em usuário')


def update_usuario_sobrenome(conn, id_usuario, sobrenome):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE usuario SET sobrenome=%s where id_usuario=%s", (sobrenome, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em usuário')


def update_usuario_username(conn, id_usuario, username):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE usuario SET username=%s where id_usuario=%s", (username, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em usuário')


def update_usuario_email(conn, id_usuario, email):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE usuario SET email=%s where id_usuario=%s", (email, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em usuário')


def update_usuario_cidade(conn, id_usuario, cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE usuario SET cidade=%s where id_usuario=%s", (cidade, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em usuário')


def update_usuario_ativo(conn, id_usuario, ativo):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "UPDATE usuario SET ativo=%s where id_usuario=%s", (ativo, id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar update em usuário')


def remove_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'DELETE FROM usuario WHERE id_usuario=%s', (id_usuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em usuario')
