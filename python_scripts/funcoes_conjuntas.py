import pymysql
from funcoes_usuario import *
from funcoes_mencao_usuario import *
from funcoes_mencao_passaro import *
from funcoes_post import *
from parsers import *


def adiciona_post_e_mencoes(conn, id_usuario, titulo, texto, url_imagem):
    mencoes_usuario_usernames = parser1(texto, '@')
    mencoes_passaro_especies = parser1(texto, '#')
    mencoes_usuario_ids = []

    adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

    with conn.cursor() as cursor:
        cursor.execute('SELECT LAST_INSERT_ID()')
        id_post = cursor.fetchone()

    for i in mencoes_usuario_usernames:
        mencoes_usuario_ids.append(acha_usuario_id_por_username(conn, i))

    for j in mencoes_usuario_ids:
        adiciona_mencao_usuario(conn, id_post, j)

    for k in mencoes_passaro_especies:
        adiciona_mencao_passaro(conn, id_post, k)
