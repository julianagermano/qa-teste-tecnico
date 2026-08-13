# language: pt
Funcionalidade: Adicionar produto ao carrinho

  Cenário: Adicionar item disponível ao carrinho
    Dado que o usuário está logado no SauceDemo
    Quando ele adiciona a "Sauce Labs Backpack" ao carrinho
    Então o ícone do carrinho deve mostrar 1 item
    E o item "Sauce Labs Backpack" deve aparecer no carrinho com nome e preço corretos