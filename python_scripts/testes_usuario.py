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

    def test_acha_usuario_info_por_id(self):
        conn = self.__class__.connection

        id_usuario = '1'
        res_esperado = ['Guilherme', 'Moraes',
                        'guigs10mil', 'guigui@hotmail.com', 'Sao Paulo']

        # Lista infos do usuario 1 e compara com as esperadas.
        res = acha_usuario_info_por_id(conn, id_usuario)
        self.assertCountEqual(res, res_esperado)

    def test_acha_usuario_id_por_username(self):
        conn = self.__class__.connection

        username = 'guigs10mil'
        id_esperado = 1

        # Lista id do username guigs10mil e compara com o esperado.
        id_novo = acha_usuario_id_por_username(conn, username)
        self.assertEqual(id_novo, id_esperado)

    def test_acha_usuario_ativo_por_id(self):
        conn = self.__class__.connection

        id = 1
        ativo_esperado = 1

        # Lista ativo do usuario de id = 1 e compara com o esperado
        ativo_novo = acha_usuario_ativo_por_id(conn, id)
        self.assertEqual(ativo_novo, ativo_esperado)

    def test_lista_usuario_usernames(self):
        conn = self.__class__.connection

        usernames_esperado = ['guigs10mil', 'JJ',
                              'BearVaz', 'Folguinha', 'Jorge_Insper']

        # Lista ativo do usuario de id = 1 e compara com o esperado
        usernames_novo = lista_usuario_usernames(conn)
        self.assertCountEqual(usernames_novo, usernames_esperado)

    def test_lista_usuario_usernames_por_cidade(self):
        conn = self.__class__.connection

        usernames_esperado = ['guigs10mil', 'Folguinha']
        cidade = 'Sao Paulo'

        # Lista usernames dos usuarios daquela cidade e compara com o esperado
        usernames_novo = lista_usuario_usernames_por_cidade(conn, cidade)
        self.assertCountEqual(usernames_novo, usernames_esperado)

    def test_lista_usuario_username_por_nome_e_sobrenome(self):
        conn = self.__class__.connection

        nome = 'Guilherme'
        sobrenome = 'Moraes'
        username_esperado = ['guigs10mil']

        # lista username do usuario com certo nome e sobrenome e compara com o esperado
        username_novo = lista_usuario_username_por_nome_e_sobrenome(
            conn, nome, sobrenome)
        self.assertCountEqual(username_novo, username_esperado)

    # def test_lista_usuario_username_por_palavra(self):
    #     conn = self.__class__.connection

    #     palavra = 'Vaz'
    #     username_esperado = ['BearVaz']

    #     # lista username do usuario com certo nome e sobrenome e compara com o esperado
    #     username_novo = lista_usuario_username_por_palavra(
    #         conn, palavra)
    #     self.assertCountEqual(username_novo, username_esperado)

    def test_update_usuario_nome(self):
        conn = self.__class__.connection

        nome = 'Guinga'

        update_usuario_nome(conn, 1, nome)

        nome_novo = acha_usuario_info_por_id(conn, 1)[0]
        self.assertEqual(nome_novo, nome)

    def test_update_usuario_sobrenome(self):
        conn = self.__class__.connection

        sobrenome = 'Mina'

        update_usuario_sobrenome(conn, 1, sobrenome)

        sobrenome_novo = acha_usuario_info_por_id(conn, 1)[1]
        self.assertEqual(sobrenome_novo, sobrenome)

    def test_update_usuario_username(self):
        conn = self.__class__.connection

        username = 'guigui'

        update_usuario_username(conn, 1, username)

        username_novo = acha_usuario_info_por_id(conn, 1)[2]
        self.assertEqual(username_novo, username)

    def test_update_usuario_email(self):
        conn = self.__class__.connection

        email = 'guigui@gmail.com'

        update_usuario_email(conn, 1, email)

        email_novo = acha_usuario_info_por_id(conn, 1)[3]
        self.assertEqual(email_novo, email)

    def test_update_usuario_cidade(self):
        conn = self.__class__.connection

        cidade = 'Campinas'

        update_usuario_cidade(conn, 1, cidade)

        cidade_novo = acha_usuario_info_por_id(conn, 1)[4]
        self.assertEqual(cidade_novo, cidade)

    def test_update_usuario_ativo(self):
        conn = self.__class__.connection

        ativo = 0

        update_usuario_ativo(conn, 1, ativo)

        ativo_novo = acha_usuario_ativo_por_id(conn, 1)
        self.assertEqual(ativo_novo, ativo)

    def test_remove_usuario(self):
        conn = self.__class__.connection

        nome = 'liu'
        sobrenome = 'seeker'
        username = "LiuSeeker"
        email = "liuliu@liu.liu"
        cidade = "sp"

        res_esperado = ['liu', 'seeker', 'LiuSeeker', 'liuliu@liu.liu', 'sp']

        adiciona_usuario(conn, nome, sobrenome, username, email, cidade)
        id = acha_usuario_id_por_username(conn, username)
        res = acha_usuario_info_por_id(conn, id)
        self.assertCountEqual(res, res_esperado)

        remove_usuario(conn, id)

        res = acha_usuario_info_por_id(conn, id)
        self.assertFalse(res)


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
