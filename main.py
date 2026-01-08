import PySimpleGUI as sg

# Simulação de Banco de Dados (Dicionário: 'usuario': 'senha')
USUARIOS_CADASTRADOS = {
    'Lucas.Souza': 'Lucas_Senha01',
    'Bruna.Gomes': 'OláMundo231'
}

sg.theme('DarkAmber') # NeonYellow1 pode ser visualmente cansativo

layout = [
    [sg.Text('Usuário:'), sg.Input(key='-USUARIO-', size=(20,1))],
    [sg.Text('Senha:  '), sg.Input(key='-SENHA-', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?', key='-SALVAR-')],
    [sg.Button('Entrar'), sg.Button('Sair')]
]

janela = sg.Window('StarChild Enterprises - Acesso', layout)

while True:
    eventos, valores = janela.read()

    if eventos in (sg.WINDOW_CLOSED, 'Sair'):
        break

    if eventos == 'Entrar':
        usuario = valores['-USUARIO-']
        senha = valores['-SENHA-']

        # Lógica de verificação otimizada
        if usuario in USUARIOS_CADASTRADOS and USUARIOS_CADASTRADOS[usuario] == senha:
            sg.popup(f'Acesso concedido!\nBem-vindo, {usuario}.')
        else:
            sg.popup_error('Erro: Usuário ou senha inválidos.')

janela.close()