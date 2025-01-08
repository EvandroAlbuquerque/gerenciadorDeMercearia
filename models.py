import datetime

class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        
class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, produto: Produto, quantidadeVendida, comprador, vendedor, dataHora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')):
        self.produto = produto
        self.quantidadeVendida = quantidadeVendida
        self.vendedor = vendedor
        self.comprador = comprador
        self.dataHora = dataHora


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, email, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Funcionario:
    def __init__(self, pessoa: Pessoa, clt):
        self.pessoa = pessoa
        self.clt = clt

# class Compra()


# caixa
# Relatório geral de vendas
# Relatório de vendas por data
# Relatório de produtos mais vendidos
# Relatório de clientes que mais compraram