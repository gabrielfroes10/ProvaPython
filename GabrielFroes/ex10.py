def add_book(livros):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    
    livros.append({
        'titulo': titulo,
        'autor': autor,
    })
    print(f"livro {titulo} adicionado com sucesso.")

def list_books(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    print("Livros:")
    for livro in livros:
        print(f"titulo: {livro['titulo']}, autor: {livro['autor']}")

def find_book_by_title(livros):
    pesquisa = input("Digite o titulo do livro: ")
    for livro in livros:
        if(livro['titulo'] == pesquisa):
            print(f"titulo: {livro['titulo']}, autor: {livro['autor']}")
        else:
            print("O livro não foi encontrado")
        

def menu():
    livros = []
    while True:
        print("\nBiblioteca")
        print("1. Adicionar Livro")
        print("2. Listar livros")
        print("3. Procurar livro")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            add_book(livros)
        elif opcao == '2':
            list_books(livros)
        elif opcao == '3':
            find_book_by_title(livros)
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()


