**Contribuidores/Contributors**:
- [FelippeTeracini](https://github.com/FelippeTeracini)
- [LiuSeeker](https://github.com/LiuSeeker)
---

(PT-BR)

### Projeto 1 - Criação de uma rede social

O nosso primeiro projeto será a construção da base de dados para uma rede
social para observadores de pássaros. O projeto será desenvolvido em duas
etapas:

1. Implantação da base inicial e população com exemplos fictícios de dados.
2. Incorporação de novos requisitos.

#### Fase 1
Requisitos iniciais:
- Dados pessoais do usuário: nome, email, cidade onde mora.
- Um usuário pode também declarar várias preferências de pássaros.
- Cada post nessa rede social tem um título (obrigatorio), um texto (opcional), e uma URL de uma foto (opcional) – vamos supor que as fotos são armazenadas por algum outro sistema, que disponibiliza as URLs.
- O usuário pode apagar seus posts, mas eles não devem ser removidos fisicamente da base, apenas marcados como inativos (delete lógico).
- Os textos podem ter tags # marcando o tipo de pássaro de que se fala no post
- O texto também pode ter tags @ referenciando outros usuários (@shouts), e isso vai ser importante destacar também.
- Ao guardar informações de quem viu o post, queremos também guardar o tipo de aparelho (Android ou iOS), browser (Chrome, IE, Firefox, Safari, outros), IP, e instante da visualização.

Entregáveis:
- [x] Modelo Entidade-Relacionamento
- [x] Modelo Relacional
- [x] Script de criação do banco de dados
- [x] Script de criação de triggers e outros constrians
- [x] Programa em Python que testa a funcionalidade do banco de dados

#### Fase 2
Novos rerquisitos:

- [x] Joinhas: Um usuário pode registrar um joinha ou um anti-joinha em qualquer post. O sistema não deverá permitir que o mesmo usuário dê vários joinhas ou anti-joinhas no mesmo post – deve ser possível apenas cancelar ou mudar de ideia.
- [x] O sistema deve permitir a adição de posts, obviamente. Note que ao adicionar um post vocês devem também registrar os #tags e @shouts.
- [x] O sistema deve permitir que um post seja removido (note que na fase 1 vocês fizeram o design que permitia que isso fosse feito, agora na fase 2 vocês estão fazendo as queries que executam essas operações).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O sistema deve permitir várias consultas:
- - [x] Posts do usuário em ordem cronológica reversa.
- - [x] Usuários mais popular de cada cidade.
- - [x] Lista de usuários que referenciam um dado usuário.
- - [x] Tabela cruzada de quantidade de aparelhos por tipo e por browser.
- - [x] Lista com URLs de imagens e respectivos #tags de tipo de pássaro.

- [x] Crie uma feature do seu interesse.
- [x] Todas essas operações de interação com o banco de dados devem ser feitas através de um serviço REST escrito em Python. Use FastAPI (https://fastapi.tiangolo.com/), teste com sua ferramenta favorita de interação com serviços web.
- [x] Obviamente a documentação do modelo (modelagem E-R, modelagem relacional, dicionário de dados) deverá ser atualizada
- [x] Todas as alterações de schema devem ser feitas com scripts delta, sem alterar os scripts anteriores
- [x] Testes unitários deverão ser feitos para os novos itens

---

(EN-US)

### Project 1 - Creation of a Social Network

Our first project will be building the database for a network
social for bird watchers. The project will be developed in two
phases:

1. Implementation of initial base and population with dummy examples of data.
2. Incorporation of new requirements

#### Phase 1
Initial requirements:
- User infos: name, email, city.
- A user can also declare various bird preferences
- Each post on this social network has a title (required), text (optional), and a photo URL (optional) - let's assume the photos are stored by some other system, which provides the URLs.
- The user can delete their posts, but they should not be physically removed from the base, only marked as inactive (logical delete).
- Texts may have tags # marking the type of bird spoken of in the post
- The text can also have @ tags referencing other users (@shouts), and this will be important to highlight as well.
- When saving information from who saw the post, we also want to save the device type (Android or iOS), browser (Chrome, IE, Firefox, Safari, others), IP, and timestamp of the view

Deliverables:
- [x] Entity-Relationship Model
- [x] Relational Model
- [x] Database creation script
- [x] Script for creating triggers and other constrians
- [x] Python program that tests database functionality

#### Fase 2
New requirements:

- [x] Like: A user can register a like or anti-like on any post. The system should not allow the same user to give multiple likes or anti-likes on the same post - it should just be possible to cancel or change the like.
- [x] The system should allow the addition of posts, obviously. Note that when adding a post you must also register #tags and @shouts.
- [x] The system should allow a post to be removed (note that in phase 1 you made the design that allowed it to be done, now in phase 2 you are making the queries that perform these operations).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The system must allow several consultations:
- - [x] User posts in reverse chronological order.
- - [x] Most popular users of each city.
- - [x] List of users that reference a given user.
- - [x] Cross tables of device numbers by type and browser.
- - [x] List with image URLs and their #tags of bird type.

- [x] Create a feature of interest.
- [x] All these database interaction operations must be done through a REST service written in Python. Use FastAPI (https://fastapi.tiangolo.com/), test with your favorite web services interaction tool.
- [x] Obviously the model documentation (E-R modeling, relational modeling, data dictionary) should be updated.
- [x] All schema changes must be made with delta scripts, without changing previous scripts.
- [x] Unit tests should be done for new items.
