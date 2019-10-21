from fastapi import FastAPI
import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from pydantic import BaseModel

from funcoes_usuario import *
from funcoes_post import *
from funcoes_conjuntas import *
from funcoes_consultas import *

global config
with open('config_tests.json', 'r') as f:
        config = json.load(f)
conn = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='rede_passaro'
        )

app = FastAPI()


@app.get("/usuarios/{id_usuario}")
def read_usuarios(id_usuario: int):
    res = acha_usuario_info_por_id(conn, id_usuario)
    return {"nome": res[0],
            "sobrenome": res[1],
            "username": res[2],
            "email": res[3],
            "cidade": res[4]
            }

@app.post("/posts")
def create_post(id_usuario: int, titulo: str, texto: str, url_imagem: str):
        with conn.cursor() as cursor:
                cursor.execute('START TRANSACTION')
                adiciona_post_e_mencoes(conn, id_usuario, titulo, texto, url_imagem)
                cursor.execute('COMMIT')
        return {"id_usuario": id_usuario,
                "titulo": titulo,
                "texto": texto,
                "url_imagem": url_imagem,
                }

@app.delete("/posts/{id_post}")
def delete_post(id_post: int):
        with conn.cursor() as cursor:
                cursor.execute('START TRANSACTION')
                update_post_ativo(conn, id_post, 0)
                cursor.execute('COMMIT')
        return {"id_post": id_post}

@app.get("/usuarios/{id_usuario}/posts")
def read_posts_de_usuario_ordem_cronologica(id_usuario: int):
        res = consulta_posts_de_usuario_em_ordem_reversa(conn, id_usuario)
        return{"posts": res}

@app.get("/usuarios/{cidade}")
def read_usuario_popular_por_cidade(cidade: str):
        res = consulta_usuario_mais_popular_de_cada_cidade(conn, cidade)
        return{"usuario_popular": res}

@app.get("/usuarios/{id_usuario}/usuarios")
def read_usuarios_que_referenciam_usuario(id_usuario: int):
        res = consulta_lista_de_usuarios_que_referenciam_determinado_usuario(conn, id_usuario)
        return{"usuarios_que_referenciam": res}

@app.get("/visualizacao")
def read_tabela_cruzada():
        res = consulta_tabela_cruzada_de_quantidade_de_aparelhos_por_tipo_e_por_browser(conn)
        return{"tabela": res}

@app.get("/visualizacao/passaros")
def read_lista_urls_com_hashtags():
        res = consulta_url_com_hashtags(conn)
        return{"urls": res}

@app.put("/posts/{id_post}")
def update_texto_post(id_post: int, texto: str):
        update_post_texto_e_mencoes(conn, id_post, texto)
        return{
                "id_post": id_post,
                "texto": texto
        }

