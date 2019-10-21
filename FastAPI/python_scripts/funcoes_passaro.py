import pymysql


def adiciona_passaro(conn, especie):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO Passaro (especie) VALUES (%s)", (especie))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao inserir passaro')


def lista_passaros(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Passaro")
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def lista_passaro_por_palavra(conn, palavra):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT especie FROM Passaro WHERE especie LIKE %{$%s}", (palavra))
        res = cursor.fetchall()
        if res:
            return tuple(x[0] for x in res)
        else:
            return None


def remove_passaro(conn, especie):
    with conn.cursor() as cursor:
        try:
            cursor.execute('DELETE FROM Passaro WHERE especie=%s', (especie))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao dar delete em usuario')
