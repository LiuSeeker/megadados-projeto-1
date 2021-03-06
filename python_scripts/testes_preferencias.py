import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_preferencia import *


class TestPreferencias(unittest.TestCase):
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

    def test_adiciona_preferencia(self):
        conn = self.__class__.connection

        especie = 'tucano'
        id_usuario = 2
        res_esperado = ['tucano']

        # Adiciona uma preferencia não existente.
        adiciona_preferencia(conn, id_usuario, especie)

        # Tenta adicionar a mesma preferencia duas vezes.
        try:
            adiciona_preferencia(conn, id_usuario, especie)
            self.fail(
                'Nao deveria ter adicionado a mesma preferencia duas vezes.')
        except ValueError as e:
            pass

        res = lista_preferencia_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

    def test_lista_preferencia_por_id_usuario(self):
        conn = self.__class__.connection

        especie1 = 'tucano'
        especie2 = 'canario'
        id_usuario = 2
        res_esperado = ['tucano', 'canario']

        adiciona_preferencia(conn, id_usuario, especie1)
        adiciona_preferencia(conn, id_usuario, especie2)

        res = lista_preferencia_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

    def test_lista_preferencia_por_especie(self):
        conn = self.__class__.connection

        especie = 'tucano'
        id_usuario1 = 1
        id_usuario2 = 2
        res_esperado = [1, 2]

        adiciona_preferencia(conn, id_usuario1, especie)
        adiciona_preferencia(conn, id_usuario2, especie)

        res = lista_preferencia_por_especie(conn, especie)
        self.assertCountEqual(res, res_esperado)

    def test_remove_preferencia(self):
        conn = self.__class__.connection

        especie1 = 'tucano'
        especie2 = 'canario'
        id_usuario = 1

        res_esperado = ['tucano', 'canario']

        adiciona_preferencia(conn, id_usuario, especie1)
        adiciona_preferencia(conn, id_usuario, especie2)
        res = lista_preferencia_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

        remove_preferencia(conn, id_usuario, especie2)

        res_esperado = ['tucano']
        res = lista_preferencia_por_id_usuario(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
