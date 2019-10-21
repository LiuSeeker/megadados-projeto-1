import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_mencao_usuario import *
from funcoes_post import *


class TestMencaoUsuario(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global config
        cls.connection = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='rede_passaro'
        )

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def setUp(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('START TRANSACTION')

    def tearDown(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('ROLLBACK')

    def test_adiciona_mencao_usuario(self):
        conn = self.__class__.connection

        id_usuario = 1

        titulo = 'teste'
        texto = 'testetest'
        url_imagem = 'sadadsasd'

        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        res_esperado = [id_post]

        adiciona_mencao_usuario(conn, id_post, id_usuario)

        try:
            adiciona_mencao_usuario(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado a mesma preferencia duas vezes.')
        except ValueError as e:
            pass

        res = lista_mencao_usuario_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

    def test_lista_mencao_usuario_por_id_usuario(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = 'teste'
        texto = 'testetest'
        url_imagem = 'sadadsasd'

        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            ids_post = cursor.fetchall()

        id_post1 = ids_post[0][0]
        id_post2 = ids_post[1][0]

        res_esperado = [id_post1, id_post2]

        adiciona_mencao_usuario(conn, id_post1, id_usuario)
        adiciona_mencao_usuario(conn, id_post2, id_usuario)

        res = lista_mencao_usuario_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

    def test_lista_mencao_usuario_por_id_post(self):
        conn = self.__class__.connection

        id_usuario1 = 1
        id_usuario2 = 2
        titulo = 'teste'
        texto = 'testetest'
        url_imagem = 'sadadsasd'

        adiciona_post(conn, id_usuario1, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            ids_post = cursor.fetchall()

        id_post1 = ids_post[0][0]

        res_esperado = [id_usuario1, id_usuario2]

        adiciona_mencao_usuario(conn, id_post1, id_usuario1)
        adiciona_mencao_usuario(conn, id_post1, id_usuario2)

        res = lista_mencao_usuario_por_id_post(conn, id_post1)
        self.assertCountEqual(res, res_esperado)

    def test_remove_mencao_usuario(self):
        conn = self.__class__.connection

        id_usuario1 = 1
        id_usuario2 = 2
        titulo = 'teste'
        texto = 'testetest'
        url_imagem = 'sadadsasd'

        adiciona_post(conn, id_usuario1, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            ids_post = cursor.fetchall()

        id_post1 = ids_post[0][0]

        res_esperado = [id_usuario1, id_usuario2]

        adiciona_mencao_usuario(conn, id_post1, id_usuario1)
        adiciona_mencao_usuario(conn, id_post1, id_usuario2)

        res = lista_mencao_usuario_por_id_post(conn, id_post1)
        self.assertCountEqual(res, res_esperado)

        res_esperado = [id_usuario2]
        remove_mencao_usuario(conn, id_post1, id_usuario1)

        res = lista_mencao_usuario_por_id_post(conn, id_post1)
        self.assertCountEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
