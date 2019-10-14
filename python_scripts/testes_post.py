import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_post import *


class TestPost(unittest.TestCase):
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


    def test_adiciona_post(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        # Checa se o perigo existe.
        res = acha_post_info_por_id(conn, id_post)
        res_esperado = (2, 'titulo', 'texto', 'url_imagem')

        self.assertCountEqual(res, res_esperado)

    def test_acha_post_info_por_id(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        # Checa se o perigo existe.
        res = acha_post_info_por_id(conn, id_post)
        res_esperado = (2, 'titulo', 'texto', 'url_imagem')

        self.assertCountEqual(res, res_esperado)

    def test_acha_post_ativo_por_id(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        # Checa se o perigo existe.
        res = acha_post_ativo_por_id(conn, id_post)
        res_esperado = 1

        self.assertEqual(res, res_esperado)

        update_post_ativo(conn, id_post, 0)

        res2 = acha_post_ativo_por_id(conn, id_post)
        res2_esperado = 0

        self.assertEqual(res2, res2_esperado)
    
    def test_lista_post_id_por_id_usuario(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post1 = cursor.fetchone()[0]

        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post2 = cursor.fetchone()[0]

        # Checa se o perigo existe.
        res = lista_post_id_por_id_usuario(conn, 2)
        res_esperado = (id_post1, id_post2)

        self.assertCountEqual(res, res_esperado)

        res2 = lista_post_id_por_id_usuario(conn, 1)

        self.assertIsNone(res2)

    def test_lista_post_id_por_palavra(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto liu oba"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        # Checa se o perigo existe.
        res = lista_post_id_por_palavra(conn, "liu")
        res_esperado = [id_post]

        self.assertCountEqual(res, res_esperado)

        res2 = lista_post_id_por_palavra(conn, "nisbe")

        self.assertIsNone(res2)

    def test_update_post_titulo(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]


        update_post_titulo(conn, id_post, "titulo2")

        # Checa se o perigo existe.
        res = acha_post_info_por_id(conn, id_post)[1]
        res_esperado = "titulo2"

        self.assertCountEqual(res, res_esperado)


    def test_update_post_texto(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]


        update_post_texto(conn, id_post, "texto2")

        # Checa se o perigo existe.
        res = acha_post_info_por_id(conn, id_post)[2]
        res_esperado = "texto2"

        self.assertCountEqual(res, res_esperado)

    
    def test_update_post_url_imagem(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]


        update_post_url_imagem(conn, id_post, "url_imagem2")

        # Checa se o perigo existe.
        res = acha_post_info_por_id(conn, id_post)[3]
        res_esperado = "url_imagem2"

        self.assertCountEqual(res, res_esperado)


    def test_update_post_ativo(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        # Checa se o perigo existe.
        res = acha_post_ativo_por_id(conn, id_post)
        res_esperado = 1

        self.assertEqual(res, res_esperado)

        update_post_ativo(conn, id_post, 0)

        res2 = acha_post_ativo_por_id(conn, id_post)
        res2_esperado = 0

        self.assertEqual(res2, res2_esperado)

    def test_remove_post(self):
        conn = self.__class__.connection

        id_usuario = 2
        titulo = "titulo"
        texto = "texto"
        url_imagem = "url_imagem"

        # Adiciona um perigo não existente.
        adiciona_post(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        # Checa se o perigo existe.
        res = acha_post_info_por_id(conn, id_post)
        res_esperado = (2, 'titulo', 'texto', 'url_imagem')

        self.assertCountEqual(res, res_esperado)

        remove_post(conn, id_post)

        res2 = acha_post_info_por_id(conn, id_post)

        self.assertIsNone(res2)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
