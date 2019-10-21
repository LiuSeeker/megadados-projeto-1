import pymysql


def consulta_posts_de_usuario_em_ordem_reversa(conn, id_usuario):
    with conn.cursor() as cursor:
        cursor.execute('''
                SELECT id_post, titulo, instante
                FROM Post
                WHERE Post.id_usuario = %s AND Post.ativo = 1
                ORDER BY Post.instante
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
                FROM Usuario u 
                INNER JOIN Mencao_Usuario mu USING(id_usuario)
                WHERE u.cidade = %s
<<<<<<< HEAD
                GROUP BY u.username
=======
                GROUP BY u.nome
>>>>>>> 08125243e65b67fce55e01de71699a6d078e1636
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
                FROM Usuario
                WHERE Usuario.id_usuario IN (
                    SELECT DISTINCT Post.id_usuario
                    FROM Post
                    INNER JOIN Mencao_Usuario USING(id_post)
                    WHERE Mencao_Usuario.id_usuario = %s
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
                FROM Visualizacao
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
                FROM Post
                INNER JOIN Mencao_Passaro USING (id_post)
                WHERE Mencao_Passaro.ativo = 1
                           ''')
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None
