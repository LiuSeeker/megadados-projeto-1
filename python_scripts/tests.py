import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_usuario import *


class TestUsuario(unittest.TestCase):
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

    def test_adiciona_usuario(self):
        conn = self.__class__.connection
    
        nome = 'liu'
        sobrenome = 'seeker'
        username = "LiuSeeker"
        email = "liuliu@liu.liu"
        cidade = "sp"

        # Adiciona um perigo não existente.
        adiciona_usuario(conn, nome, sobrenome, username, email, cidade)

        # Tenta adicionar o mesmo perigo duas vezes.
        try:
            adiciona_usuario(conn, nome, sobrenome, username, email, cidade)
            self.fail('Nao deveria ter adicionado o mesmo username duas vezes.')
        except ValueError as e:
            pass

        # Checa se o perigo existe.
        id = acha_usuario_id_por_username(conn, username)
        self.assertIsNotNone(id)

        # Tenta achar um perigo inexistente.
        id = acha_usuario_id_por_username(conn, 'dasdasd')
        self.assertIsNone(id)

if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
