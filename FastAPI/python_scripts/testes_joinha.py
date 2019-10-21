import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from funcoes_joinha import *
from funcoes_post import adiciona_post, acha_post_info_por_id

class TestJoinha(unittest.TestCase):
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


    def test_adiciona_pro_joinha(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_pro_joinha(conn, id_post, id_usuario)

        try:
            adiciona_pro_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_todos_joinha_por_id_post(conn, id_post)
        res_esperado = [(id_post, id_usuario, 1)]
        self.assertCountEqual(res, res_esperado)

    def test_adiciona_anti_joinha(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_anti_joinha(conn, id_post, id_usuario)

        try:
            adiciona_anti_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_todos_joinha_por_id_post(conn, id_post)
        res_esperado = [(id_post, id_usuario, 0)]
        self.assertCountEqual(res, res_esperado)


    def test_lista_todos_joinha_por_id_post(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_pro_joinha(conn, id_post, id_usuario)

        try:
            adiciona_pro_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_todos_joinha_por_id_post(conn, id_post)
        res_esperado = [(id_post, id_usuario, 1)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha(conn, id_post, id_usuario)

        res2 = lista_todos_joinha_por_id_post(conn, id_post)
        
        self.assertIsNone(res2)

    def test_lista_pro_joinha_por_id_post(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_pro_joinha(conn, id_post, id_usuario)

        try:
            adiciona_pro_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_pro_joinha_por_id_post(conn, id_post)
        res_esperado = [(id_post, id_usuario, 1)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha(conn, id_post, id_usuario)

        res2 = lista_pro_joinha_por_id_post(conn, id_post)
        
        self.assertIsNone(res2)

    def test_lista_anti_joinha_por_id_post(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_anti_joinha(conn, id_post, id_usuario)

        try:
            adiciona_anti_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_anti_joinha_por_id_post(conn, id_post)
        res_esperado = [(id_post, id_usuario, 0)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha(conn, id_post, id_usuario)

        res2 = lista_anti_joinha_por_id_post(conn, id_post)
        
        self.assertIsNone(res2)


    def test_lista_todos_joinha_por_id_usuario(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_pro_joinha(conn, id_post, id_usuario)

        try:
            adiciona_pro_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_todos_joinha_por_id_usuario(conn, id_usuario)
        res_esperado = [(id_post, id_usuario, 1)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha(conn, id_post, id_usuario)

        res2 = lista_todos_joinha_por_id_usuario(conn, id_usuario)
        
        self.assertIsNone(res2)

    def test_lista_pro_joinha_por_id_usuario(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_pro_joinha(conn, id_post, id_usuario)

        try:
            adiciona_pro_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_pro_joinha_por_id_usuario(conn, id_usuario)
        res_esperado = [(id_post, id_usuario, 1)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha(conn, id_post, id_usuario)

        res2 = lista_pro_joinha_por_id_usuario(conn, id_usuario)
        
        self.assertIsNone(res2)

    def test_lista_anti_joinha_por_id_usuario(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_anti_joinha(conn, id_post, id_usuario)

        try:
            adiciona_anti_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_anti_joinha_por_id_usuario(conn, id_usuario)
        res_esperado = [(id_post, id_usuario, 0)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha(conn, id_post, id_usuario)

        res2 = lista_anti_joinha_por_id_usuario(conn, id_usuario)
        
        self.assertIsNone(res2)

    def test_update_pro_joinha(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_anti_joinha(conn, id_post, id_usuario)

        try:
            adiciona_anti_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass


        update_pro_joinha(conn, id_post)
        
        res = lista_pro_joinha_por_id_post(conn, id_post)
        res_esperado = [(id_post, id_usuario, 1)]

        self.assertCountEqual(res, res_esperado)

        res2 = lista_anti_joinha_por_id_post(conn, id_post)
        
        self.assertIsNone(res2)


    def test_update_anti_joinha(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_pro_joinha(conn, id_post, id_usuario)

        try:
            adiciona_pro_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass


        update_anti_joinha(conn, id_post)
        
        res = lista_anti_joinha_por_id_post(conn, id_post)
        res_esperado = [(id_post, id_usuario, 0)]

        self.assertCountEqual(res, res_esperado)

        res2 = lista_pro_joinha_por_id_post(conn, id_post)
        
        self.assertIsNone(res2)

    def test_remove_joinha(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_anti_joinha(conn, id_post, id_usuario)

        try:
            adiciona_anti_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_anti_joinha_por_id_usuario(conn, id_usuario)
        res_esperado = [(id_post, id_usuario, 0)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha(conn, id_post, id_usuario)

        res2 = lista_anti_joinha_por_id_usuario(conn, id_usuario)
        
        self.assertIsNone(res2)

    def test_remove_joinha_por_post(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_anti_joinha(conn, id_post, id_usuario)

        try:
            adiciona_anti_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_anti_joinha_por_id_usuario(conn, id_usuario)
        res_esperado = [(id_post, id_usuario, 0)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha_por_post(conn, id_post)

        res2 = lista_anti_joinha_por_id_post(conn, id_post)
        
        self.assertIsNone(res2)


    def test_remove_joinha_por_usuario(self):
        conn = self.__class__.connection

        adiciona_post(conn, 1, "titulo", "texto", "url_imagem")
        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        id_usuario = 1

        adiciona_anti_joinha(conn, id_post, id_usuario)

        try:
            adiciona_anti_joinha(conn, id_post, id_usuario)
            self.fail(
                'Nao deveria ter adicionado joinha duas vezes.')
        except ValueError as e:
            pass

        
        res = lista_anti_joinha_por_id_usuario(conn, id_usuario)
        res_esperado = [(id_post, id_usuario, 0)]

        self.assertCountEqual(res, res_esperado)

        remove_joinha_por_usuario(conn, id_usuario)

        res2 = lista_anti_joinha_por_id_usuario(conn, id_usuario)
        
        self.assertIsNone(res2)

if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)