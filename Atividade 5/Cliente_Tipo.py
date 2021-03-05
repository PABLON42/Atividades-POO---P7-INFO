import enum

class TipoClient(enum.Enum):
    PESSOA_FISICA = 1
    PESSOA_JURIDICA = 2


if __name__ == '__main__':
    print("Os numeros enum sao: ")
    for tipo in (TipoClient):
        print(type(tipo))
        print(tipo)
