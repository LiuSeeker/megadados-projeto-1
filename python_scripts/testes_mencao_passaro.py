import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_mencao_passaro import *
from funcoes_post import adiciona_post, acha_post_info_por_id

class TestMencaoPassaro(unittest.TestCase):
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

    def test_adiciona_mencao_passaro(self):
        conn = self.__class__.connection
        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        especie = "tucano"
        res_esperado = [id_post]

        adiciona_mencao_passaro(conn, id_post, especie)

        try:
            adiciona_mencao_passaro(conn, id_post, especie)
            self.fail(
                'Nao deveria ter adicionado a mesma mencao duas vezes.')
        except ValueError as e:
            pass

        res = lista_mencao_passaro_por_especie(conn, especie)
        self.assertCountEqual(res, res_esperado)

    def test_lista_mencao_passaro_por_especie(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]


        especie = "tucano"
        adiciona_mencao_passaro(conn, id_post, especie)

        res1 = lista_mencao_passaro_por_especie(conn, "tucano")
        res1_esperado = [id_post]

        res2 = lista_mencao_passaro_por_especie(conn, "canario")

        self.assertCountEqual(res1, res1_esperado)
        self.assertIsNone(res2)

    def test_lista_mencao_passaro_por_id_post(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        adiciona_mencao_passaro(conn, id_post, "tucano")

        res = lista_mencao_passaro_por_id_post(conn, id_post)
        res_esperado = ["tucano"]

        self.assertCountEqual(res, res_esperado)

        adiciona_mencao_passaro(conn, id_post, "canario")

        res2 = lista_mencao_passaro_por_id_post(conn, id_post)
        res2_esperado = ["tucano", "canario"]

        self.assertCountEqual(res2, res2_esperado)

    def test_remove_mencao_passaro(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        adiciona_mencao_passaro(conn, id_post, "tucano")

        remove_mencao_passaro(conn, id_post, "tucano")

        res = lista_mencao_passaro_por_id_post(conn, id_post)

        self.assertIsNone(res)



if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
