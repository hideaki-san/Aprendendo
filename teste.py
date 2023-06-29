class livro():
    def __init__(self, nome, genero, paginas):
        self.nome = nome
        self.genero = genero
        self.pag = paginas
        self.id = 0

    def cadastrar(self, id):
        self.id = id

    def cadastro_livro(self):
        if self.id == 0:
            print(self.nome, "(Livro não cadastrado)")
        else:
            print(self.nome, self.genero, self.pag, self.id)