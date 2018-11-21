# Miojo
  Solução de um problema proposto para uma oferta de emprego n IBM.

## Enunciado
  Problema do Miojo:

  João é um fanático por miojos; ele os adora, e, como era de se esperar, ele levou vários pacotes quando foi acampar com seus colegas. Como João só gosta de miojos feitos com o tempo exato, ele se deseperou ao perceber que havia esquecido seu relógio em casa.

  Por sorte, ele conseguiu, no caminho, comprar duas ampulhetas de durações diferentes. Por exemplo, se o miojo precisa de 3 minutos para ficar pronto, e João tiver uma ampulheta de 5 minutos e outra de 7, uma possível forma de cozinhar o miojo é:


    João começa virando as duas ampulhetas ao mesmo tempo.
    Quando a areia da ampulheta de 5 minutos se esgotar, João torna a virá-la.
    João começa a preparar o miojo quando a areia da ampulheta de 7 minutos acabar.
    João tira o miojo do fogo quando a ampulheta de 5 minutos acabar novamente.
    Dessa forma, o miojo ficará 3 minutos no fogo (do minuto 7 ao minuto 10).


  Assim, apesar do miojo levar apenas três minutos para ser cozido, ele precisa de 10 minutos para ficar pronto.

  Faça um programa que, dado o tempo de preparo do miojo, e os tempos das duas ampulhetas (ambos maiores que o tempo do miojo), determina o tempo mínimo necessário para o miojo ficar pronto ou se não é possível cozinhar o miojo no tempo exato com as ampulhetas disponíveis.

## Pré-Requisitos

  Para utilizar esse progama é necessário a versão mais recente do python3 e as seguintes bibliotecas: unittest. Em um sistema linux com pip3 e python3 instalado, é possivel instalar estas bilibotecas globalmente com

    $ sudo pip3 install <nome da biblioteca>

## CLI Interface
   Para utilizar CLI interface basta executar o comando

    $ python3 miojo.py <a> <b> <c>

   onde a e b são as durações de ambas as ampulhetas e c é o tempo necessário para o cozimento do miojo. Caso a input seja valida e o problma solúvel o sistema devera imprimir o tempo mínimo em minutos que joão necessitara usar para cozer o miojo.

## Testes de Unidade
  Para executar os testes de unidade do módulo algorithms basta executar o módulo com o comando

    $ python3 algorithms

  não se esqueça de possuir a biblioteca unittests instalada no seu computador para tanto.
