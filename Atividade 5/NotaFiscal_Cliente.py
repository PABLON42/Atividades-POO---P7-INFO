class Cliente():
    def __init__(self, id, nome, codigo, cnpjcpf):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf

    def str(self):
        string = "\nId={3} Codigo={2} Nome={1} CNPJ/CPF={0} ".format(self._cnpjcpf, self._codigo,
                                                                             self._nome, self._id)
        return string


if __name__ == '__main__':
    cliente = Cliente(1, "Joseph", 100, '607,256,369-69' )
    print(cliente.str())

