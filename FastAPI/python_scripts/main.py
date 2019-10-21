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

from funcoes_usuario import *

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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/usuario/{id_usuario}")
def read_usuarios(id_usuario: int):
    res = acha_usuario_info_por_id(conn, id_usuario)
    return {"nome": res[0],
            "sobrenome": res[1],
            "username": res[2],
            "email": res[3],
            "cidade": res[4]
            }


    
