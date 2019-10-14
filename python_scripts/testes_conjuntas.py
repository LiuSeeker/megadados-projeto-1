import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_conjuntas import *
from funcoes_post import *


class TestConjuntas(unittest.TestCase):
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

    def test_adiciona_post_e_mencoes(self):
        conn = self.__class__.connection

        id_usuario = 1
        titulo = 'teste'
        texto = 'ola @guigs10mil #tucano'
        url_imagem = 'sadadsasd'

        adiciona_post_e_mencoes(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        res_esperado = [1]
        res = lista_mencao_usuario_por_id_post(conn, id_post)
        self.assertCountEqual(res, res_esperado)

        res_esperado = ['tucano']
        res = lista_mencao_passaro_por_id_post(conn, id_post)
        self.assertCountEqual(res, res_esperado)

        res_esperado = [id_post]
        res = lista_post_id_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

    def test_update_post_texto_e_mencoes(self):
        conn = self.__class__.connection

        id_usuario = 1
        titulo = 'teste'
        texto = 'ola @guigs10mil #tucano'
        url_imagem = 'sadadsasd'

        adiciona_post_e_mencoes(conn, id_usuario, titulo, texto, url_imagem)

        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM post')
            id_post = cursor.fetchone()[0]

        res_esperado = [1]
        res = lista_mencao_usuario_por_id_post(conn, id_post)
        self.assertCountEqual(res, res_esperado)

        res_esperado = ['tucano']
        res = lista_mencao_passaro_por_id_post(conn, id_post)
        self.assertCountEqual(res, res_esperado)

        res_esperado = [id_post]
        res = lista_post_id_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

        texto_novo = 'ola @JJ #canario'
        update_post_texto_e_mencoes(conn, id_post, texto_novo)

        res_esperado = [2]
        res = lista_mencao_usuario_por_id_post(conn, id_post)
        self.assertCountEqual(res, res_esperado)

        res_esperado = ['canario']
        res = lista_mencao_passaro_por_id_post(conn, id_post)
        self.assertCountEqual(res, res_esperado)

        res_esperado = 'ola @JJ #canario'
        res = acha_post_info_por_id(conn, id_post)[2]
        print(res)
        self.assertEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
