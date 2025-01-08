from daos import *
import datetime

class CategoriaController:
    def cadastrar(self, novaCategoria):
        categorias = CategoriaDAO.listar()
        exists = False
        
        for c in categorias:
            if c.nome == novaCategoria:
                exists = True
                print('Esta categoria já existe.')
        
        if not exists:
            CategoriaDAO.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
            
    def editar(self, categoria, categoriaAtualizada):
        categorias = CategoriaDAO.listar()
        categoriaExiste = False
        novaCategoriaExiste = False
        estoques = EstoqueDAO.listar()
        
        for c in categorias:
            if c.nome == categoriaAtualizada:
                novaCategoriaExiste = True
                
            if c.nome == categoria:
                c.nome = categoriaAtualizada
                categoriaExiste = True
            
        if novaCategoriaExiste:
            print('A nova categoria já existe.')
        elif categoriaExiste:
            CategoriaDAO.sobrescrever(categorias)
                    
            for i in range(len(estoques)):
                    if estoques[i].produto.categoria == categoria:
                        estoques[i].produto.categoria = categoriaAtualizada
            
            EstoqueDAO.sobrescrever(estoques)
                        
            print('Categoria atualizada com sucesso!')
        else:
            print('Esta categoria não existe.')

    def remover(self, categoria):
        categorias = CategoriaDAO.listar()
        categoriaExcluida = True
        estoques = EstoqueDAO.listar()
            
        try:
            for i in range(len(categorias)):
                if categorias[i].nome == categoria:
                    del categorias[i]
                    categoriaExcluida = True
                    break
            
            CategoriaDAO.sobrescrever(categorias)
            
            if categoriaExcluida:
                for i in range(len(estoques)):
                    if estoques[i].produto.categoria == categoria:
                        estoques[i].produto.categoria = 'SEM CATEGORIA'
            
                EstoqueDAO.sobrescrever(estoques)
            
            print('Categoria excluída com sucesso!')
        except ValueError:
            print('Esta categoria não existe.')
        except Exception as e:
            print(f'Problema ao tentar remover categoria: {e}')
    
    def listar(self):
        categorias = CategoriaDAO.listar()
        
        if len(categorias) == 0:
            print('Não há categorias cadastradas.')
        else:
            print('TODAS AS CATEGORIAS: \n')
            for c in categorias:
                print(f'Categoria: {c.nome}')


class EstoqueController:
    def registrarProduto(self, nome, categoria, preco, quantidade):
        estoques = EstoqueDAO.listar()
        categorias = CategoriaDAO.listar()
        categoriaExiste = False
        produtoExiste = False
        
        for c in categorias:
            if c.nome == categoria:
                categoriaExiste = True
        
        if not categoriaExiste:
            print('Categoria não cadastrada.')
        else:
            for e in estoques:
                if e.produto.nome == nome:
                    produtoExiste = True
                    print('Produto já registrado no estoque.')
                    break
        
        if categoriaExiste and not produtoExiste:
            novoProduto = Produto(nome, categoria, float(preco))
            EstoqueDAO.salvar(Estoque(novoProduto, quantidade))
            print('Produto registrado com sucesso!')
    
    def adicionarQuantidadeProduto(self, nome, quantidade):
        estoques = EstoqueDAO.listar()
        produtoExiste = False
        
        for i in range(len(estoques)):
            if estoques[i].produto.nome == nome:
                produtoExiste = True
                qtd = int(estoques[i].quantidade)
                qtd += quantidade
                estoques[i].quantidade = str(qtd)
                break
        
        if produtoExiste:
            EstoqueDAO.sobrescrever(estoques)
            
            print('Adição de quantidade do produto atualizada com sucesso!')
        else:
            print('Produto não registrado no estoque.')
    
    def subtrairQuantidadeProduto(self, nome, quantidade):
        estoques = EstoqueDAO.listar()
        produtoExiste = False
        
        for i in range(len(estoques)):
            if estoques[i].produto.nome == nome:
                produtoExiste = True
                qtd = int(estoques[i].quantidade)
                qtd -= quantidade
                estoques[i].quantidade = str(qtd)
                break
        
        if produtoExiste:
            EstoqueDAO.sobrescrever(estoques)
            
            print('Subtração de quantidade do produto atualizada com sucesso!')
        else:
            print('Produto não registrado no estoque.')
    
    def atualizarProduto(self, nome, novoNome, novaCategoria, novoPreco):
        mesmoProduto = False
        if nome == novoNome:
            mesmoProduto = True
            print('Não há motificações no produto.')
            
        if not mesmoProduto:
            estoques = EstoqueDAO.listar()
            produtoExiste = False
            novoProdutoExiste = False
            indiceProduto = 0
            
            for i in range(len(estoques)):
                if estoques[i].produto.nome == nome:
                    produtoExiste = True
                    indiceProduto = i
                elif estoques[i].produto.nome == novoNome:
                    novoProdutoExiste = True
                    print('O produto atualizado já está registrado.')
                    break
            
            if not produtoExiste:
                print('Este produto não existe, verifique os dados inseridos.')
            elif not novoProdutoExiste:
                estoques[indiceProduto].produto.nome = novoNome
                estoques[indiceProduto].produto.categoria = novaCategoria
                estoques[indiceProduto].produto.preco = novoPreco
                
                EstoqueDAO.sobrescrever(estoques)
                print('Produto atualizado com sucesso!')
    
    def removerProduto(self, nome):
        estoques = EstoqueDAO.listar()
        categoriaExcluida = False
        
        for i in range(len(estoques)):
            if estoques[i].produto.nome == nome:
                categoriaExcluida = True
                del estoques[i]
                break
        
        if categoriaExcluida:
            EstoqueDAO.sobrescrever(estoques)
                    
            print('Categoria excluída com sucesso!')
    
    def listar(self):
        estoques = EstoqueDAO.listar()
        
        for e in estoques:
            print(f'{e.produto.nome} | {e.produto.categoria} | {e.produto.preco} | {e.quantidade}')


class VendaController:
    def registrar(self, nomeProduto, quantidadeVendida, comprador, vendedor):
        estoques = EstoqueDAO.listar()
        produtoExiste = False
        indiceProduto = int
        
        for i in range(len(estoques)):
            if estoques[i].produto.nome == nomeProduto:
                produtoExiste = True
                indiceProduto = i
                break
        
        if produtoExiste:
            if int(estoques[indiceProduto].quantidade) >= quantidadeVendida:
                produto = estoques[indiceProduto].produto
                VendaDAO.salvar(Venda(produto, quantidadeVendida, comprador, vendedor))
                EstoqueController().subtrairQuantidadeProduto(nomeProduto, quantidadeVendida)
                
                print("Venda registrada com sucesso!")
            else:
                print("Esta quantidade não está disponível no estoque.")
        else:
            print("Este produto não está registrado no estoque.")
    
    def cancelar(self, nomeProduto, comprador, vendedor):
        vendas = VendaDAO.listar()
        vendaExiste = False
        estoques = EstoqueDAO.listar()
        quantidadeVendida = 0
        
        for i in range(len(vendas)):
            if vendas[i].produto.nome == nomeProduto and vendas[i].comprador == comprador and vendas[i].vendedor == vendedor:
                vendaExiste = True
                quantidadeVendida = vendas[i].quantidadeVendida
                del vendas[i]
                break
                
        if vendaExiste:
            VendaDAO.sobrescrever(vendas)
            
            with open('estoques.txt', 'w') as arq:
                for i in range(len(estoques)):
                    if estoques[i].produto.nome == nomeProduto:
                        totalAtual = int(estoques[i].quantidade)
                        totalAtual += int(quantidadeVendida)
                        estoques[i].quantidade = str(totalAtual)
                    
                    arq.writelines(estoques[i].produto.nome + ' | ' + estoques[i].produto.categoria + ' | ' + estoques[i].produto.preco + ' | ' + estoques[i].quantidade + '\n')
                    
            print("Venda cancelada com sucesso!")
        else:
            print("Não há vendas com estas informações.")

    
    def listar(self):
        vendas = VendaDAO.listar()
        
        for v in vendas:
            print(f'Nome do produto: {v.produto.nome} | Quantidade: {v.quantidadeVendida} | Comprador: {v.comprador} | Vendedor: {v.vendedor} | Data e Hora: {v.dataHora}')


    def maisVendidos(self):
        vendas = VendaDAO.listar()
        
        produtosVendidos = []
        for v in vendas:
            nomeProduto = v.produto.nome
            quantidade = int(v.quantidadeVendida)
        
            if any(p['produto'] == nomeProduto for p in produtosVendidos):
                produtosVendidos = list(map(lambda v: {'produto': nomeProduto, 'quantidade': int(v['quantidade']) + quantidade}
                                        if v['produto'] == nomeProduto else v, produtosVendidos))
            else:
                produtosVendidos.append({'produto': nomeProduto, 'quantidade': quantidade})
        
        produtosVendidosOrdenados = sorted(produtosVendidos, key=lambda v: v['quantidade'], reverse=True)
        
        for p in produtosVendidosOrdenados:
            print(f'Produto: {p['produto']} | Quantidade vendida: {p['quantidade']}\n')


    def vendasPorPeriodo(self, dataInicial, dataFinal):
        vendas = VendaDAO.listar()
        dataInicio = datetime.datetime.strptime(dataInicial, '%d/%m/%Y').date()
        dataFim = datetime.datetime.strptime(dataFinal, '%d/%m/%Y').date()
        
        vendasPeriodo = list(filter(lambda v : datetime.datetime.strptime(v.dataHora, '%d/%m/%Y %H:%M:%S ').date() >= dataInicio and 
                                    datetime.datetime.strptime(v.dataHora, '%d/%m/%Y %H:%M:%S ').date() <= dataFim, vendas))
        
        for venda in vendasPeriodo:
            print(f'Produto: {venda.produto.nome} | Quantidade vendida: {venda.quantidadeVendida} | Comprador: {venda.comprador} | Vendedor: {venda.vendedor} | Data: {venda.dataHora}\n')


class FornecedorController:
    def cadastrar(self, nome, cnpj, telefone, email, categoria):
        categorias = CategoriaDAO.listar()
        categoriaExiste = False
        
        if any(c.nome == categoria for c in categorias):
            with open('fornecedores.txt', 'a') as arq:
                arq.writelines(nome + ' | ' + cnpj + ' | ' + telefone + ' | ' + email + ' | ' + categoria + '\n')
            categoriaExiste = True
            print("Fornecedor cadastrado com sucesso!")
    
        if not categoriaExiste:
            print("Esta categoria não existe.")
    
    def detalhar(self, **dado):
        nome = dado.get('nome')
        cnpj = dado.get('cnpj')
        
        fornecedores = FornecedorDAO.listar()
        
        if nome:
            for f in fornecedores:
                if f.nome == nome:
                    print(f'Nome: {f.nome}, CNPJ: {f.cnpj}, E-mail: {f.email}, Telefone: {f.telefone}, Categoria: {f.categoria}. \n')
        elif cnpj:
            for f in fornecedores:
                if f.cnpj == cnpj:
                    print(f'Nome: {f.nome}, CNPJ: {f.cnpj}, E-mail: {f.email}, Telefone: {f.telefone}, Categoria: {f.categoria}. \n')
        else:
            print('Não há fornecedor com o nome ou CNPJ inserido.')
          
    
    def listar(self):
        fornecedores = FornecedorDAO.listar()
        
        if not fornecedores:
            print('Não há fornecedores cadastrados.')
        else:
            print(f'FORNECEDORES: \n')
            for f in fornecedores:
                print(f'Nome: {f.nome}, CNPJ: {f.cnpj}, Categoria: {f.categoria}.\n')
    
    def remover(self, cnpj):
        fornecedores = FornecedorDAO.listar()
        fornecedorRemovido = False
        
        for i in range(len(fornecedores)):
            if fornecedores[i].cnpj == cnpj:
                del fornecedores[i]
                fornecedorRemovido = True
                break
            
        if fornecedorRemovido:
            FornecedorDAO.sobrescrever(fornecedores)
            print('Fornecedor removido com sucesso!')


class FuncionarioController:
    def cadastrar(self, nome, cpf, telefone, email, endereco, clt):
        pessoa = Pessoa(nome, cpf, telefone, email, endereco)
        funcionario = Funcionario(pessoa, clt)
        
        FuncionarioDAO.salvar(funcionario)
        print('Funcionário cadastrado com sucesso!')
    
    def detalhar(self, cpf):
        funcionarios = FuncionarioDAO.listar()
        
        if not funcionarios:
            print('Não há funcionários cadastrados.')
        else:
            for f in funcionarios:
                if f.pessoa.cpf == cpf:
                    print(f'Nome: {f.pessoa.nome}, CPF: {f.pessoa.cpf}, Telefone: {f.pessoa.telefone}, E-mail: {f.pessoa.email}, Endereço: {f.pessoa.endereco}, CLT: {f.clt}.')
    
    def listar(self):
        funcionarios = FuncionarioDAO.listar()
        
        if not funcionarios:
            print('Não há funcionários cadastrados.')
        else:
            print(f'FUNCIONÁRIOS: \n')
            for f in funcionarios:
                print(f'Nome: {f.pessoa.nome}, CPF: {f.pessoa.cpf}, CLT: {f.clt}.\n')
    
    def remover(self, cpf):
        funcionarios = FuncionarioDAO.listar()
        funcionarioRemovido = False
        
        if not funcionarios:
            print('Não há funcionários cadastrados.')
        else:
            for i in range(len(funcionarios)):
                if funcionarios[i].pessoa.cpf == cpf:
                    del funcionarios[i]
                    funcionarioRemovido = True
                    break
        
        if funcionarioRemovido:
            FuncionarioDAO.sobrescrever(funcionarios)
            print('Funcionário removido com sucesso!')
        else:
            print('Nenhum funcionário removido, verifique o CPF inserido.')


class ClienteController:
    def cadastrar(self, nome, cpf, telefone, email, endereco):
        PessoaDAO.salvar(Pessoa(nome, cpf, telefone, email, endereco))
        print('Cliente cadastrado com sucesso!')
    
    def detalhar(self, cpf):
        clientes = PessoaDAO.listar()
        
        if not clientes:
            print('Não há clientes cadastrados.')
        else:
            for c in clientes:
                if c.cpf == cpf:
                    print(f'Nome: {c.nome}, CPF: {c.cpf}, Telefone: {c.telefone}, E-mail: {c.email}, Endereço: {c.endereco}.')
    
    def listar(self):
        clientes = PessoaDAO.listar()
        
        if not clientes:
            print('Não há clientes cadastrados.')
        else:
            print(f'CLIENTES: \n')
            for c in clientes:
                print(f'Nome: {c.nome}, CPF: {c.cpf}, Telefone: {c.telefone}.\n')
    
    def remover(self, cpf):
        clientes = PessoaDAO.listar()
        clienteRemovido = False
        
        if not clientes:
            print('Não há clientes cadastrados.')
        else:
            for i in range(len(clientes)):
                if clientes[i].cpf == cpf:
                    del clientes[i]
                    clienteRemovido = True
                    break
        
        if clienteRemovido:
            PessoaDAO.sobrescrever(clientes)
            print('Cliente removido com sucesso!')
        else:
            print('Nenhum cliente removido, verifique o CPF inserido.')