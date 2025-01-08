from controllers import *
import os.path

def criarArquivos(*nome):
    for arquivo in nome:
        if not os.path.exists(arquivo):
            with open(arquivo, "w") as arq:
                arq.write("")

criarArquivos('categorias.txt', 'clientes.txt', 'estoques.txt', 'fornecedores.txt', 'funcionarios.txt', 'vendas.txt')

def sair():
    print("Até mais!")
    exit()

def menuPrincipal():
    opcao = input("\n\n\n>>>MENU PRINCIPAL<<<\n\n"
                    "Digite uma das opções:\n\n"
                    "1 para menu de Categoria. \n"
                    "2 para menu de Estoque. \n"
                    "3 para menu de Venda. \n"
                    "4 para menu de Fornecedor. \n"
                    "5 para menu de Funcionário. \n"
                    "6 para menu de Cliente. \n"
                    "0 para sair. \n\n\n")

    match opcao:
        case "0":
            sair()
        case "1":
            menuCategoria()
        case "2":
            menuEstoque()
        case "3":
            menuVenda()
        case "4":
            menuFornecedor()
        case "5":
            menuFuncionario()
        case "6":
            menuCliente()
        case _:
            print('Escolha uma opção válida.')
            menuPrincipal()


def menuCategoria():
    opcao = input("\n\nMENU DE CATEGORIA \n\n"
                    "1 para ver todas. \n"
                    "2 para cadastrar. \n"
                    "3 para editar uma. \n"
                    "4 para remover uma. \n"
                    "9 para voltar ao menu principal. \n"
                    "0 para sair. \n\n")
    
    if opcao == "0":
        sair()
    
    c = CategoriaController()
    
    match opcao:
        case "1":
            c.listar()
            menuCategoria()
        case "2":
            novaCategoria = input('Digite o nome da nova categoria: \n')
            c.cadastrar(novaCategoria)
            menuCategoria()
        case "3":
            categoria = input('Digite o nome da categoria a ser alterada: \n')
            categoriaAtualizada = input('Digite o novo nome da categoria: \n')
            c.editar(categoria, categoriaAtualizada)
            menuCategoria()
        case "4":
            nomeCategoria = input('Digite o nome da categoria a ser removida: \n')
            c.remover(nomeCategoria)
            menuCategoria()
        case "9":
            menuPrincipal()
        case _:
            print('Escolha uma opção válida.')
            menuCategoria()


def menuEstoque():
    opcao = input("\n\nMENU DE ESTOQUE:\n\n"
                    "1 para ver todos os produtos no estoque. \n"
                    "2 para cadastrar um produto no estoque. \n"
                    "3 para adicionar estoque de um produto. \n"
                    "4 para reduzir estoque de um produto. \n"
                    "5 para remover um produto do estoque. \n"
                    "9 para voltar ao menu principal. \n"
                    "0 para sair. \n\n")
    
    if opcao == "0":
        sair()
    
    e = EstoqueController()
    
    match opcao:    
        case "1":
            e.listar()
            menuEstoque()
        case "2":
            nome = input('Digite o nome do produto: \n')
            categoria = input('Digite a categoria do produto: \n')
            preco = float(input('Digite o preco do produto: \n'))
            quantidade = int(input('Digite a quantidade a ser adicionada no estoque: \n'))
            e.registrarProduto(nome=nome, categoria=categoria, preco=preco, quantidade=quantidade)
            menuEstoque()
        case "3":
            nomeProduto = input('Digite o nome do produto: \n')
            quantidade = int(input('Digite a quantidade do produto a ser adicionada ao estoque: \n'))
            e.adicionarQuantidadeProduto(nome=nomeProduto, quantidade=quantidade)
            menuEstoque()
        case "4":
            nomeProduto = input('Digite o nome do produto: \n')
            quantidade = int(input('Digite a quantidade do produto a ser removida do estoque: \n'))
            e.subtrairQuantidadeProduto(nome=nomeProduto, quantidade=quantidade)
            menuEstoque()
        case "5":
            nomeProduto = input('Digite o nome do produto a ser removido: \n')
            e.removerProduto(nomeProduto)
            menuEstoque()
        case "9":
            menuPrincipal()
        case _:
            print('Escolha uma opção válida.')
            menuEstoque()


def menuVenda():
    opcao = input("\n\nMENU DE VENDA \n\n"
                    "1 para ver todas. \n"
                    "2 para ver os produtos mais vendidos. \n"
                    "3 para ver as vendas de um período. \n"
                    "4 para cadastrar uma. \n"
                    "5 para cancelar uma. \n"
                    "9 para voltar ao menu principal. \n"
                    "0 para sair. \n\n")
    
    if opcao == "0":
        sair()
    
    v = VendaController()
    
    match opcao:
        case "1":
            v.listar()
            menuVenda()
        case "2":
            v.maisVendidos()
            menuVenda()
        case "3":
            dataInicial = input('Digite a data inicial do período (utilize o padrão dd/mm/aaaa): \n')
            dataFinal = input('Digite a data final do período (utilize o padrão dd/mm/aaaa): \n')
            v.vendasPorPeriodo(dataInicial=dataInicial, dataFinal=dataFinal)
            menuVenda()
        case "4":
            nomeProduto = input('Digite o nome do produto: \n')
            quantidade = int(input('Digite a quantidade do produto a ser vendida. \n'))
            comprador = input('Digite o nome do comprador: \n')
            vendedor = input('Digite o nome do vendedor: \n')
            v.registrar(nomeProduto=nomeProduto, quantidadeVendida=quantidade, comprador=comprador, vendedor=vendedor)
            menuVenda()
        case "5":
            nomeProduto = input('Digite o nome do produto: \n')
            comprador = input('Digite o nome do comprador: \n')
            vendedor = input('Digite o nome do vendedor: \n')
            v.cancelar(nomeProduto=nomeProduto, comprador=comprador, vendedor=vendedor)
        case "9":
            menuPrincipal()
        case _:
            print('Escolha uma opção válida.')
            menuVenda()


def menuFornecedor():
    opcao = input("\n\nMENU DE FORNECEDOR \n\n"
                    "1 para ver todos. \n"
                    "2 para ver um em detalhes. \n"
                    "3 para cadastrar. \n"
                    "4 para remover um. \n"
                    "9 para voltar ao menu principal. \n"
                    "0 para sair. \n\n")
    
    if opcao == "0":
        sair()
    
    f = FornecedorController()
    
    match opcao:
        case "1":
            f.listar()
            menuFornecedor()
        case "2":
            cnpj = input('Digite o CNPJ do fornecedor: \n')
            f.detalhar(cnpj=cnpj)
            menuFornecedor()
        case "3":
            nomeFornecedor = input('Digite o nome do novo fornecedor: \n')
            cnpj = input('Digite o CNPJ: \n')
            email = input('Digite o e-mail: \n')
            telefone = input('Digite o telefone: \n')
            categoria = input('Digite a categoria dos produtos que ele fornece: \n')
            f.cadastrar(nome=nomeFornecedor, cnpj=cnpj, email=email, telefone= telefone, categoria=categoria)
            menuFornecedor()
        case "4":
            cnpj = input('Digite o CNPJ do fornecedor a ser removido: \n')
            f.remover(cnpj)
            menuFornecedor()
        case "9":
            menuPrincipal()
        case _:
            print('Escolha uma opção válida.')
            menuFornecedor()


def menuFuncionario():
    opcao = input("\n\nMENU DE FUNCIONÁRIO \n\n"
                    "1 para ver todos. \n"
                    "2 para ver um em detalhes. \n"
                    "3 para cadastrar. \n"
                    "4 para remover um. \n"
                    "9 para voltar ao menu principal. \n"
                    "0 para sair. \n\n")
    
    if opcao == "0":
        sair()
        
    f = FuncionarioController()
    
    match opcao:
        case "1":
            f.listar()
            menuFuncionario()
        case "2":
            cpf = input('Digite o CPF do funcionário: \n')
            f.detalhar(cpf)
            menuFuncionario()
        case "3":
            nome = input('Digite o nome do novo funcionário: \n')
            cpf = input('Digite o CPF: \n')
            telefone = input('Digite o telefone: \n')
            email = input('Digite o e-mail: \n')
            endereco = input('Digite o endereço: \n')
            clt = input('Digite o número da CLT: \n')
            f.cadastrar(nome=nome, cpf=cpf, telefone=telefone, email=email, endereco=endereco, clt=clt)
            menuFuncionario()
        case "4":
            cpf = input('Digite o CPF do funcionário: \n')
            f.remover(cpf)
            menuFuncionario()
        case "9":
            menuPrincipal()
        case _:
            print('Escolha uma opção válida.')
            menuFuncionario()


def menuCliente():
    opcao = input("\n\nMENU DE CLIENTE \n\n"
                    "1 para ver todos. \n"
                    "2 para ver um em detalhes. \n"
                    "3 para cadastrar. \n"
                    "4 para remover um. \n"
                    "9 para voltar ao menu principal. \n"
                    "0 para sair. \n\n")
    
    if opcao == "0":
        sair()
    
    c = ClienteController()
    
    match opcao:
        case "1":
            c.listar()
            menuCliente()
        case "2":
            cpf = input('Digite o CPF do cliente: \n')
            c.detalhar(cpf)
            menuCliente()
        case "3":
            nome = input('Digite o nome do novo cliente: \n')
            cpf = input('Digite o CPF: \n')
            telefone = input('Digite o telefone: \n')
            email = input('Digite o e-mail: \n')
            endereco = input('Digite o endereço: \n')
            c.cadastrar(nome=nome, cpf=cpf, telefone=telefone, email=email, endereco=endereco)
            menuCliente()
        case "4":
            cpf = input('Digite o CPF do cliente: \n')
            c.remover(cpf)
            menuCliente()
        case "9":
            menuPrincipal()
        case _:
            print('Escolha uma opção válida.')
            menuCliente()



if __name__ == "__main__":
    while True:
        menuPrincipal()