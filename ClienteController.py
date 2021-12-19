from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == 'Cadastrar':
                
                nome = values['nome']
                codigo = (values['codigo'])
                try:
                    codigo = int(codigo)
                except:
                    resultado = 'Codigo deve ser um número inteiro'
                if isinstance(codigo, int):
                    if codigo not in self.__clientes.keys():
                        self.adiciona_cliente(codigo, nome)
                        resultado = 'Cliente cadastrado'
                        self.__telaCliente.limpa_caixa('nome')
                        self.__telaCliente.limpa_caixa('codigo')
                            
                    else:
                            resultado = 'Cliente já está cadastrado'
                            self.__telaCliente.limpa_caixa('nome')
                            self.__telaCliente.limpa_caixa('codigo')
            
            elif event == 'Consultar':
                nome = values['nome']
                codigo =( values['codigo'])
                if codigo != '' and nome != '':
                    resultado = 'Digite apenas em um dos campos'
                elif codigo =='' and nome == '':
                    resultado = 'Digite em um dos campos'
                elif nome != '':
                        resultado = self.busca_nome(nome)
                        self.__telaCliente.limpa_caixa('nome')
                else: 
                    resultado = self.busca_codigo(codigo)
                    self.__telaCliente.limpa_caixa('codigo')
                    
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()

    def busca_codigo(self, codigo):
        try:
            codigo = int(codigo)
        except:
            return 'O codigo deve ser um número inteiro'
        if isinstance (codigo, int):
            if codigo in self.__clientes.keys():
                return self.__clientes[codigo]
            else:
                return 'Código não encontrado'

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return self.__clientes[key]
        return 'Cliente não encontrado'
