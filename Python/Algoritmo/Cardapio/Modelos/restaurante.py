class restaurante: 

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._avaliacoes = []
        self._cardapio = []
        self._status = False

    def __str__(self):
        return  f'{self._nome} | {self._categoria}'
    
    @property
    def status(self):
        return 'Aberto' if self._status else 'Fechado'
    
    def alternar_status(self):
        self._status = not self._status
    
    def alternar_status(self):
        self._status = not self._status