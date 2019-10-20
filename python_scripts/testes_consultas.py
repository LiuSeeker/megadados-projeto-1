import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql
import time

from funcoes_consultas import *
from funcoes_post import *
from funcoes_usuario import *
from funcoes_visualizacao import *
from funcoes_mencao_usuario import *


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

    def test_consulta_posts_de_usuario_em_ordem_reversa(self):
        conn = self.__class__.connection

        nome = 'Nome'
        sobrenome = 'Sobrenome'
        username = 'usuario_teste'
        email = 'email'
        cidade = 'SP'

        adiciona_usuario(conn, nome, sobrenome, username, email, cidade)

        id_usuario = acha_usuario_id_por_username(conn, username)

        adiciona_post(conn, id_usuario, '1', 'texto 1', 'url 1')
        time.sleep(1)
        adiciona_post(conn, id_usuario, '2', 'texto 2', 'url 2')
        time.sleep(1)
        adiciona_post(conn, id_usuario, '3', 'texto 3', 'url 3')

        res = consulta_posts_de_usuario_em_ordem_reversa(conn, id_usuario)

        res_esperado = ['3', '2', '1']
        res_lista = [res[0][1], res[1][1], res[2][1]]
        self.assertListEqual(res_lista, res_esperado)

    # def test_consulta_usuario_mais_popular_de_cada_cidade(self):
    #     conn = self.__class__.connection

    #     for i in range(5):
    #         adiciona_usuario(conn, 'nome{}'.format(i), 'sobrenome{}'.format(
    #             i), 'username{}'.format(i), 'email{}'.format(i), 'cidade1')

    #     for i in range(5):
    #         adiciona_usuario(conn, 'nome{}'.format(i+5), 'sobrenome{}'.format(
    #             i+5), 'username{}'.format(i+5), 'email{}'.format(i+5), 'cidade2')

    def test_consulta_lista_de_usuarios_que_referenciam_determinado_usuario(self):
        conn = self.__class__.connection

        adiciona_usuario(conn, 'nome_teste', 'sobrenome_teste',
                         'username_teste', 'email', 'cidade')

        for i in range(3):
            adiciona_usuario(conn, 'nome{}'.format(i), 'sobrenome{}'.format(
                i), 'username{}'.format(i), 'email{}'.format(i), 'cidade1')

        for i in range(2):
            adiciona_post(conn, acha_usuario_id_por_username(
                conn, 'username{}'.format(i)), 'titulo', 'texto', 'url')

            with conn.cursor() as cursor:
                cursor.execute('SELECT LAST_INSERT_ID()')
                id_post = cursor.fetchone()[0]

            adiciona_mencao_usuario(
                conn, id_post, acha_usuario_id_por_username(conn, 'username_teste'))

        res = consulta_lista_de_usuarios_que_referenciam_determinado_usuario(
            conn, acha_usuario_id_por_username(conn, 'username_teste'))

        res_esperado = ['username0', 'username1']
        res_lista = []
        for i in range(len(res)):
            res_lista.append(res[i][0])

        self.assertListEqual(res_lista, res_esperado)

    def test_consulta_tabela_cruzada_de_quantidade_de_aparelhos_por_tipo_e_por_browser(self):
        conn = self.__class__.connection

        nome = 'Nome'
        sobrenome = 'Sobrenome'
        username = 'usuario_teste'
        email = 'email'
        cidade = 'SP'

        adiciona_usuario(conn, nome, sobrenome, username, email, cidade)

        id_usuario = acha_usuario_id_por_username(conn, username)

        adiciona_post(conn, id_usuario, 'titulo', 'texto', 'url')

        with conn.cursor() as cursor:
            cursor.execute('SELECT LAST_INSERT_ID()')
            id_post = cursor.fetchone()[0]

        for i in range(5):
            adiciona_visualizacao(
                conn, id_post, id_usuario, 'iphone11', '0000', 'chrome')
            time.sleep(1)

        for i in range(3):
            adiciona_visualizacao(
                conn, id_post, id_usuario, 's9', '0000', 'chrome')
            time.sleep(1)

        for i in range(2):
            adiciona_visualizacao(
                conn, id_post, id_usuario, 'iphone11', '0000', 'opera')
            time.sleep(1)

        res = consulta_tabela_cruzada_de_quantidade_de_aparelhos_por_tipo_e_por_browser(
            conn)

        res_esperado = [(5, 'iphone11', 'chrome'),
                        (3, 's9', 'chrome'), (2, 'iphone11', 'opera')]

        self.assertCountEqual(res, res_esperado)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
