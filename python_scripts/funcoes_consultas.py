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


def consulta_usuario_mais_popular_de_cada_cidade(conn, cidade):
    with conn.cursor() as cursor:
        cursor.execute('''
                SELECT u.username
                FROM usuario u 
                INNER JOIN mencao_usuario mu USING(id_usuario)
                WHERE u.cidade = %s
                GROUP BY u.username
                ORDER BY count(mu.id_post) DESC
                           ''', (cidade))
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
                SELECT COUNT(aparelho), aparelho, browser
                FROM visualizacao
                GROUP BY aparelho, browser
                           ''')
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None


def consulta_url_com_hashtags(conn):
    with conn.cursor() as cursor:
        cursor.execute('''
                SELECT especie, url_imagem
                FROM post
                INNER JOIN mencao_passaro USING (id_post)
                WHERE mencao_passaro.ativo = 1
                           ''')
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None
