import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql
import datetime

from funcoes_visualizacao import *
from funcoes_post import adiciona_post, acha_post_info_por_id

class TestVisualizacao(unittest.TestCase):
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

    def test_adiciona_visualizacao(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        id_usuario = 2
        aparelho = 'iphone6'
        ip = '0.0.0.0'
        instante = '1970-01-01 00:00:01'

        res_esperado = [id_post, 2, 'iphone6', '0.0.0.0', datetime.datetime(1970, 1, 1, 0, 0, 1)]

        adiciona_visualizacao(conn, id_post, id_usuario,
                              aparelho, ip, instante)

        try:
            adiciona_visualizacao(
                conn, id_post, id_usuario, aparelho, ip, instante)
            self.fail(
                'Nao deveria ter adicionado a mesma preferencia duas vezes.')
        except ValueError as e:
            pass

        res = lista_visualizacao_por_id_post(conn, id_post)
        self.assertCountEqual(res[0], res_esperado)


    def test_lista_visualizacao_por_id_post(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        adiciona_post(conn, 2, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post2 = cursor.fetchone()[0]

        id_usuario = 2
        aparelho = 'iphone6'
        ip = '0.0.0.0'
        instante = '1970-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post, id_usuario,
                                aparelho, ip, instante)


        id_usuario2 = 1
        aparelho2 = 'iphone5'
        ip2 = '0.0.0.1'
        instante2 = '1971-01-01 00:00:01'

        res_esperado = [id_post, 2, 'iphone6', '0.0.0.0', datetime.datetime(1970, 1, 1, 0, 0, 1)]

        adiciona_visualizacao(conn, id_post2, id_usuario2,
                                aparelho2, ip2, instante2)


        res = lista_visualizacao_por_id_post(conn, id_post)
        self.assertCountEqual(res[0], res_esperado)

    def test_lista_visualizacao_por_id_usuario(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        adiciona_post(conn, 2, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post2 = cursor.fetchone()[0]

        id_usuario = 2
        aparelho = 'iphone6'
        ip = '0.0.0.0'
        instante = '1970-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post, id_usuario,
                                aparelho, ip, instante)

        id_usuario2 = 1
        aparelho2 = 'iphone5'
        ip2 = '0.0.0.1'
        instante2 = '1971-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post2, id_usuario2,
                                aparelho2, ip2, instante2)

        res_esperado = [id_post, 2, 'iphone6', '0.0.0.0', datetime.datetime(1970, 1, 1, 0, 0, 1)]

        res = lista_visualizacao_por_id_usuario(conn, 2)
        self.assertCountEqual(res[0], res_esperado)


    def test_lista_visualizacao_por_aparelho(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        adiciona_post(conn, 2, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post2 = cursor.fetchone()[0]

        id_usuario = 2
        aparelho = 'iphone6'
        ip = '0.0.0.0'
        instante = '1970-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post, id_usuario,
                                aparelho, ip, instante)

        id_usuario2 = 1
        aparelho2 = 'iphone5'
        ip2 = '0.0.0.1'
        instante2 = '1971-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post2, id_usuario2,
                                aparelho2, ip2, instante2)

        res_esperado = [id_post, 2, 'iphone6', '0.0.0.0', datetime.datetime(1970, 1, 1, 0, 0, 1)]

        res = lista_visualizacao_por_aparelho(conn, 'iphone6')
        self.assertCountEqual(res[0], res_esperado)

    def test_lista_visualizacao_por_ip(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        adiciona_post(conn, 2, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post2 = cursor.fetchone()[0]

        id_usuario = 2
        aparelho = 'iphone6'
        ip = '0.0.0.0'
        instante = '1970-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post, id_usuario,
                                aparelho, ip, instante)

        id_usuario2 = 1
        aparelho2 = 'iphone5'
        ip2 = '0.0.0.1'
        instante2 = '1971-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post2, id_usuario2,
                                aparelho2, ip2, instante2)

        res_esperado = [id_post, 2, 'iphone6', '0.0.0.0', datetime.datetime(1970, 1, 1, 0, 0, 1)]

        res = lista_visualizacao_por_ip(conn, '0.0.0.0')
        self.assertCountEqual(res[0], res_esperado)


    def test_remove_visualizacao(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 2
        aparelho = 'iphone6'
        ip = '0.0.0.0'
        instante = '1970-01-01 00:00:01'

        adiciona_visualizacao(conn, id_post, id_usuario,
                              aparelho, ip, instante)

        remove_visualizacao(conn, id_post, id_usuario)

        res = lista_visualizacao_por_id_post(conn, id_post)
        self.assertIsNone(res)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
