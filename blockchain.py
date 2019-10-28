"""Estudo: Blockchain -> Classe Block."""

from block import Block

class Blockchain:
    """Classe Blockchain.

    A definição da estrutura de dados do blockchain consiste em 'blocos'
    vinculados para formar uma 'cadeia'. É por isso que é chamado de 'blockchain'.

    Valores de configuração:
     diff - dificuldade de mineração.
     maxNonce - 2^32, é o valor máximo que podemos armazenar em 32 bits.
     target - hash que será minerado.
    """
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    # O primeiro bloco gerado é chamado de Genesis
    block = Block("Genesis")

    # define como o cabeçalho da nossa blockchain
    head = block #self.block

    def add(self, Newblock):
        """Método add - Adiciona um determinado bloco à cadeia de blocos.

        O bloco a ser adicionado é o único parâmetro.
        """
        # Definir o hash de um determinado bloco como anterior do novo bloco.
        Newblock.previous_hash = self.block.hash()
        # Incrementa o número do bloco
        Newblock.blockNo = self.block.blockNo+1
        # Definir o próximo bloco igual a si mesmo. Esta é a nova 'head'
        self.block.next = Newblock
        # o bloco que eu criei na classe é o bloco que estou adicionando agora
        self.block = Newblock

    def mine(self, Newblock):
        """Método mine - Determina se podemos adicionar ou não um determinado bloco à blockchain."""
        # de 0 até 2^32

        # se o valor do hash do bloco fornecido menor que o nosso alvo,
        # adicione o bloco à cadeia

        for n in range(self.maxNonce):
            # verifica se o hash é válido
            if int(Newblock.hash(), 16) <= self.target:
                # adiciona o bloco
                self.add(Newblock)
                break
            else:
                Newblock.nonce += 1

blockchain = Blockchain()

for b in range(10):
    blockchain.mine(Block("Bloco "+str(b+1)))

while blockchain.head:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
