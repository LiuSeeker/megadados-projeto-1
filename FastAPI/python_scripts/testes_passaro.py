import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_passaro import *


class TestPassaro(unittest.TestCase):
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

    def test_adiciona_passaro(self):
        conn = self.__class__.connection

        especie = 'coruja'
        res_esperado = ['canario', 'tucano', 'coruja']

        # Adiciona uma especie não existente.
        adiciona_passaro(conn, especie)

        # Tenta adicionar a mesma especie duas vezes.
        try:
            adiciona_passaro(conn, especie)
            self.fail('Nao deveria ter adicionado a mesma especie duas vezes.')
        except ValueError as e:
            pass

        res = lista_passaros(conn)
        self.assertCountEqual(res, res_esperado)

    def test_lista_passaros(self):
        conn = self.__class__.connection

        especies_esperado = ['canario', 'tucano']

        especies_novo = lista_passaros(conn)
        self.assertCountEqual(especies_novo, especies_esperado)

    # def test_lista_passaro_por_palavra(self):
    #     conn = self.__class__.connection

    #     palavra = 'io'
    #     especies_esperado = ['canario']

    #     especies_novo = lista_passaro_por_palavra(conn, palavra)
    #     self.assertCountEqual(especies_novo, especies_esperado)

    def test_remove_passaro(self):
        conn = self.__class__.connection

        especie = 'pardal'

        res_esperado = ['canario', 'tucano', 'pardal']

        adiciona_passaro(conn, especie)
        res = lista_passaros(conn)
        self.assertCountEqual(res, res_esperado)

        remove_passaro(conn, especie)

        res_esperado = ['canario', 'tucano']
        res = lista_passaros(conn)
        self.assertCountEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
