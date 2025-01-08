from models import *

class CategoriaDAO:
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(categoria+'\n')
    
    @classmethod
    def listar(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categorias = arq.readlines()

        cls.categorias = list(map(lambda c: c.replace('\n', ''), cls.categorias))
        
        listaCategorias = [Categoria(c) for c in cls.categorias]

        return listaCategorias
    
    @classmethod
    def sobrescrever(cls, listaCategorias):
        with open('categorias.txt', 'w') as arq:
            for c in listaCategorias:
                arq.writelines(c.nome + '\n')


class VendaDAO:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.produto.nome + ' | ' + venda.produto.categoria + ' | ' + venda.produto.preco + ' | ' + str(venda.quantidadeVendida) + ' | ' + 
                           venda.comprador + ' | ' + venda.vendedor + ' | ' + venda.dataHora + ' \n')
    
    @classmethod
    def listar(cls):
        with open('vendas.txt', 'r') as arq:
            cls.vendas = arq.readlines()

        cls.vendas = list(map(lambda c: c.replace('\n', ''), cls.vendas))
        cls.vendas = list(map(lambda c: c.split(' | '), cls.vendas))
        
        listaVendas = [Venda(Produto(v[0],v[1],v[2]),v[3],v[4],v[5],v[6]) for v in cls.vendas]
        
        return listaVendas
    
    @classmethod
    def sobrescrever(cls, listaVendas):
        with open('vendas.txt', 'w') as arq:
            for venda in listaVendas:
                arq.writelines(venda.produto.nome + ' | ' + venda.produto.categoria + ' | ' + venda.produto.preco + ' | ' + str(venda.quantidadeVendida) + ' | ' + 
                           venda.comprador + ' | ' + venda.vendedor + ' | ' + venda.dataHora + ' \n')
    

class EstoqueDAO:
    @classmethod
    def salvar(cls, estoque: Estoque):
        with open('estoques.txt', 'a') as arq:
            arq.writelines(estoque.produto.nome + ' | ' + estoque.produto.categoria + ' | ' + str(estoque.produto.preco) + ' | ' + 
                           str(estoque.quantidade) + '\n')
    
    @classmethod
    def listar(cls):
        with open('estoques.txt', 'r') as arq:
            cls.estoques = arq.readlines()

        cls.estoques = list(map(lambda c: c.replace('\n', ''), cls.estoques))
        cls.estoques = list(map(lambda c: c.split(' | '), cls.estoques))
        
        listaEstoques = [Estoque(Produto(e[0],e[1],e[2]), e[3]) for e in cls.estoques]
        
        return listaEstoques
    
    @classmethod
    def sobrescrever(cls, listaEstoques):
        with open('estoques.txt', 'w') as arq:
            for e in listaEstoques:
                arq.writelines(e.produto.nome + ' | ' + e.produto.categoria + ' | ' + str(e.produto.preco) + ' | ' + str(e.quantidade) + '\n')


class FornecedorDAO:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + ' | ' + fornecedor.cnpj + ' | ' + fornecedor.telefone + ' | ' + 
                           fornecedor.email + ' | ' + fornecedor.categoria + ' n')
    
    @classmethod
    def listar(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda f: f.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda f: f.split(' | '), cls.fornecedores))
        
        listaFornecedores = [Fornecedor(f[0], f[1], f[2], f[3], f[4]) for f in cls.fornecedores]
        
        return listaFornecedores
    
    @classmethod
    def sobrescrever(cls, listaFornecedores):
        with open('fornecedores.txt', 'w') as arq:
            for f in listaFornecedores:
                arq.writelines(f.nome + ' | ' + f.cnpj + ' | ' + f.telefone + ' | ' + f.email + ' | ' + f.categoria + '\n')


class FuncionarioDAO:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.pessoa.nome + ' | ' + funcionario.pessoa.cpf + ' | ' + funcionario.pessoa.telefone + ' | ' + funcionario.pessoa.email + ' | ' + 
                           funcionario.pessoa.endereco + ' | ' + funcionario.clt + '\n')
    
    @classmethod
    def listar(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda f: f.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda f: f.split(' | '), cls.funcionarios))
        
        listaFuncionarios = [Funcionario(Pessoa(f[0], f[1], f[2], f[3], f[4]), f[5]) for f in cls.funcionarios]
        
        return listaFuncionarios
    
    @classmethod
    def sobrescrever(cls, listaFuncionarios):
        with open('funcionarios.txt', 'w') as arq:
            for f in listaFuncionarios:
                arq.writelines(f.pessoa.nome + ' | ' + f.pessoa.cpf + ' | ' + f.pessoa.telefone + ' | ' + f.pessoa.email + ' | ' + f.pessoa.endereco + ' | ' + f.clt + '\n')


class PessoaDAO:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + ' | ' + pessoa.cpf + ' | ' + pessoa.telefone + ' | ' + pessoa.email + ' | ' + 
                           pessoa.endereco + '\n')
    
    @classmethod
    def listar(cls):
        with open('clientes.txt', 'r') as arq:
            cls.pessoas = arq.readlines()

        cls.pessoas = list(map(lambda c: c.replace('\n', ''), cls.pessoas))
        cls.pessoas = list(map(lambda c: c.split(' | '), cls.pessoas))
        
        listaPessoas = [Pessoa(p[0], p[1], p[2], p[3], p[4]) for p in cls.pessoas]
        
        return listaPessoas
    
    @classmethod
    def sobrescrever(cls, listaClientes):
        for c in listaClientes:
            with open('clientes.txt', 'w') as arq:
                arq.writelines(c.nome + ' | ' + c.cpf + ' | ' + c.telefone + ' | ' + c.email + ' | ' + c.endereco + '\n')