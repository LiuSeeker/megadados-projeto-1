import pymysql


def consulta_posts_de_usuario_em_ordem_reversa(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('''
                SELECT id_post, titulo, instante
                FROM post
                WHERE post.id_usuario = %s AND post.ativo = 1
                ORDER BY post.instante
                DESC
                           ''', (id_usuario))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def consulta_usuario_mais_popular_de_cada_cidade(conn):
    with conn.cursor() as cursor:
        cursor.execute('''
                SELECT DISTINCT username, cidade
                FROM usuario
                INNER JOIN mencao_usuario USING(id_usuario)
                GROUP BY id_usuario
                           ''')
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def consulta_lista_de_usuarios_que_referenciam_determinado_usuario(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('''
                SELECT DISTINCT username
                FROM usuario
                WHERE usuario.id_usuario IN (
                    SELECT DISTINCT post.id_usuario
                    FROM post
                    INNER JOIN mencao_usuario USING(id_post)
                    WHERE mencao_usuario.id_usuario = %s
                )
                           ''', (id_usuario))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def consulta_tabela_cruzada_de_quantidade_de_aparelhos_por_tipo_e_por_browser(conn):
    with conn.cursor() as cursor:
        cursor.execute('''
                SELECT COUNT(aparelho)
                FROM visualizacao
                GROUP BY aparelho
                           ''')
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None
