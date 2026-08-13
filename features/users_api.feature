# language: pt
Funcionalidade: Listagem de usuários via API

  Cenário: Consultar segunda página de usuários com sucesso
    Dado que a API reqres.in está disponível
    Quando eu solicito a lista de usuários na página 2
    Então o status da resposta deve ser 200
    E a resposta deve conter exatamente 6 usuários
    E cada usuário deve conter os campos obrigatórios
    E o campo "page" da resposta deve ser igual a 2