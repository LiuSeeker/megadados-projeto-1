import pymysql

def adiciona_preferencia(conn, id_usuario, especie):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO preferencia (id_usuario, especie) VALUES (%s, %s)", \
                (id_usuario, especie))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir preferencia')

def lista_preferencia_por_id_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM preferencia WHERE id_usuario=%s", (id_usuario))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None

def lista_preferencia_por_especie(conn, especie):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM preferencia WHERE especie=%s", (especie))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None

def remove_preferencia(conn, id_usuario, especie):
    with conn.cursor as cursor:
        try:
            cursor.execute('DELETE FROM preferencia WHERE id_usuario=%s AND especie=%s', (id_usuario, especie))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em preferencia')
