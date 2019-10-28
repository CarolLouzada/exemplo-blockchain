"""Estudo: Blockchain -> Classe Block."""

import datetime
import hashlib

class Block:
    """Classe Block - definindo a estrutura de dados do 'bloco'.

    Cada bloco possui 7 atributos:

        1. blockNo - número do bloco.
        2. data - quais dados são armazenados neste bloco?
        3. next - ponteiro para o próximo bloco.
        4. hash - o hash deste bloco (serve como um ID exclusivo e verifica
            sua integridade). Um hash é uma função que converte dados em um
            número dentro de um determinado intervalo.
        5. nonce - um nonce é um número usado apenas uma vez.
        6. previous_hash - armazena o hash (ID) do bloco anterior na cadeia.
        7. timestamp -  registro de data e hora.
    """
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        """Construtor - Inicializamos o bloco armazenando alguns dados nele."""
        self.data = data


    def hash(self):
        """Método hash - Calcula o 'hash' de um bloco.

        Um hash atua como um identificador exclusivo e útil para validar a
        integridade de qualquer dado.

        No caso do blockchain, se alguém alterar o hash de um bloco, ou seja,
        alterar um dado, os blocos seguintes devem ser alterados, o que é
        de extrema dificuldade, esta característica ajuda a tornar o
        blockchain imutável.

        O SHA-256 é um algoritmo de hash que gera uma assinatura quase
        exclusiva de 256 bits, que representa um dado qualquer.

        A entrada para o algoritmo SHA-256 será uma sequência concatenada que
        consiste em 5 atributos de bloco: nonce, hash anterior,
        'data e hora' e por fim o bloco propriamente.
        """
        # Estanciando o sha256
        hash = hashlib.sha256()

        # Determina como irá ser o bloco
        hash.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )

        # Retorna uma string hexadecimal
        return hash.hexdigest()

    def __str__(self):
        """Imprimir o valor de um bloco."""
        return ("Block Hash: " + str(self.hash()) +
                "\nBlockNo: " + str(self.blockNo) +
                "\nBlock Data: " + str(self.data) +
                "\nHashes: " + str(self.nonce) + "\n--------------")
