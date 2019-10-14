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

    # def test_adiciona_mencao_usuario(self):
    #     conn = self.__class__.connection

    #     id_post = 1
    #     id_usuario = 2
    #     res_esperado = [1]

    #     adiciona_mencao_usuario(conn, id_post, id_usuario)

    #     try:
    #         adiciona_mencao_usuario(conn, id_post, id_usuario)
    #         self.fail(
    #             'Nao deveria ter adicionado a mesma preferencia duas vezes.')
    #     except ValueError as e:
    #         pass

    #     res = lista_mencao_usuario_por_id_usuario(conn, id_usuario)
    #     self.assertCountEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
