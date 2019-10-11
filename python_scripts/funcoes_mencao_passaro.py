import pymysql

def adiciona_mencao_passaro(conn, id_post, especie):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO mencao_passaro (id_post, especie) VALUES (%s, %s)", \
                (id_post, especie))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir mencao passaro')

def lista_mencao_passaro_por_especie(conn, especie):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM mencao_passaro WHERE especie=%s", (especie))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None

def lista_mencao_passaro_por_id_post(conn, id_post):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM mencao_passaro WHERE id_post=%s", (id_post))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None

def remove_mencao_passaro(conn, id_post, especie):
    with conn.cursor as cursor:
        try:
            cursor.execute('DELETE FROM mencao_passaro WHERE id_post=%s AND especie=%s', (id_post, especie))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em mencao passaro')