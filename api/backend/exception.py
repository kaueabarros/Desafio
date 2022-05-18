class NomeNaoLocalizado(Exception):
    def __init__(self, message = 'Nome não localizado !'):
        self.message = message
        super().__init__(self.message)