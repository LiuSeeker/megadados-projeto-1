import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_visualizacao import *


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

    # def test_adiciona_visualizacao(self):
    #     conn = self.__class__.connection

    #     id_post = 1
    #     id_usuario = 2
    #     aparelho = 'iphone6'
    #     ip = '0.0.0.0'
    #     instante = '1970-01-01 00:00:01'

    #     res_esperado = [1, 2, 'iphone6', '0.0.0.0', '1970-01-01 00:00:01']

    #     adiciona_visualizacao(conn, id_post, id_usuario,
    #                           aparelho, ip, instante)

    #     try:
    #         adiciona_visualizacao(
    #             conn, id_post, id_usuario, aparelho, ip, instante)
    #         self.fail(
    #             'Nao deveria ter adicionado a mesma preferencia duas vezes.')
    #     except ValueError as e:
    #         pass

    #     res = lista_visualizacao_por_id_post(conn, id_post)
    #     self.assertCountEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
