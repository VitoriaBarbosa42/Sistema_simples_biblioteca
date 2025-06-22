class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

class Biblioteca:
    total_livros_na_biblioteca = 0
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    def adicionar_livro(self, livro):
        self.livros.append(vars(livro))
        Biblioteca.total_livros_na_biblioteca = len(self.livros)
        for i in self.livros:
            print(f'Livro {i['titulo']} adicionado a biblioteca')
        print(f'Total de livro {Biblioteca.total_livros_na_biblioteca}')
        return self.livros
    def listar_livros(self):
        if len(self.livros) > 0:
            for i in self.livros:
                if i['disponivel'] == True:
                    disponivel = 'Sim'
                else:
                    disponivel = 'Não'
                print (f'Título: {i['titulo']} |Autor: {i['autor']} | Ano: {i['ano_publicacao']} | Disponível: {disponivel}')
        else:
            return('A biblioteca está vazia.')
        
    def emprestar_livro(self, titulo_livro):
        condicao = False
        for titulo in self.livros:
            if titulo_livro in titulo['titulo']:
                condicao = True
                if titulo['disponivel'] == True:
                    titulo['disponivel'] = False
                    print(titulo)
                else:
                    print('Livro indisponivel')
        if condicao == False:
            print('Livro não encontrado')

    def devolver_livro(self, titulo_livro):
        condicao = False
        for titulo in self.livros:
            if titulo_livro in titulo['titulo']:
                condicao = True
                if titulo['disponivel'] == False:
                    titulo['disponivel'] = True
                    print(titulo)
                else:
                    print('Livro já está na biblioteca')
        if condicao == False:
            print('Livro não encontrado')


livro1 = Livro('Pequeno Principe', 'Antoine de Saint-Exupéry', 1943)
livro2 = Livro('O Cortiço', 'Aluísio Azevedo', 1890)
livro3 = Livro('Vidas Secas', 'Graciliano Ramos', 1938)
livro4 = Livro('Grande Sertão: Veredas', 'Guimarães Rosa', 1956)
livro5 = Livro('A Hora da Estrela,', 'Clarice Lispecto', 1977)
livro6 = Livro('Dom Casmurro', 'Machado de Assis', 1899)


biblioteca1 = Biblioteca('Vilas Boas')
biblioteca1.adicionar_livro(livro1)
biblioteca1.adicionar_livro(livro2)
biblioteca1.adicionar_livro(livro3)
biblioteca1.adicionar_livro(livro4)
biblioteca1.adicionar_livro(livro5)
biblioteca1.adicionar_livro(livro6)

biblioteca1.listar_livros()
biblioteca1.emprestar_livro('Grande Sertão')
biblioteca1.emprestar_livro('Grande Sertão')
biblioteca1.devolver_livro('Grande Sertão')
biblioteca1.devolver_livro('Grande Sertão')


