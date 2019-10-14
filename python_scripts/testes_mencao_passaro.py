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
'''
    def test_lista_mencao_passaro_por_especie(self):
        conn = self.__class__.connection

        especie1 = 'tucano'
        especie2 = 'canario'
        id_usuario = 2
        res_esperado = ['tucano', 'canario']

        adiciona_preferencia(conn, id_usuario, especie1)
        adiciona_preferencia(conn, id_usuario, especie2)

        res = lista_preferencia_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)
'''
    # def test_lista_preferencia_por_especie(self):
    #     conn = self.__class__.connection

    #     especie = 'tucano'
    #     id_usuario1 = 1
    #     id_usuario2 = 2
    #     res_esperado = [1, 2]

    #     adiciona_preferencia(conn, id_usuario1, especie)
    #     adiciona_preferencia(conn, id_usuario2, especie)

    #     res = lista_preferencia_por_especie(conn, especie)
    #     self.assertCountEqual(res, res_esperado)

    # def test_remove_preferencia(self):
    #     conn = self.__class__.connection

    #     especie1 = 'tucano'
    #     especie2 = 'canario'
    #     id_usuario = 1

    #     res_esperado = ['tucano', 'canario']

    #     adiciona_preferencia(conn, id_usuario, especie1)
    #     adiciona_preferencia(conn, id_usuario, especie2)
    #     res = lista_preferencia_por_id_usuario(conn, id_usuario)
    #     self.assertCountEqual(res, res_esperado)

    #     remove_preferencia(conn, id_usuario, especie2)

    #     res_esperado = ['tucano']
    #     res = lista_preferencia_por_id_usuario(conn, id_usuario)
    #     self.assertCountEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
