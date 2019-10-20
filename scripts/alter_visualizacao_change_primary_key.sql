use rede_passaro;
ALTER TABLE visualizacao drop primary key, add primary key(id_post, id_usuario, instante);