import PySimpleGUI as sg

#TODO - Função para unir todos os grupos
def escolha(imagem):
    #imgTransf = Transformada(imagem) 2
    #resultadoFreq = editar(imgTransf) #quando acabar retorna imagem editada 3
    #resultado = TransformadaInversa(resultadoFreq) 2
    #mostrar(resultado) #abre nova janela mostrando resultado 1
    return

#Salvando imagens em variáveis
image_mulie = '../data/mulie.png'
image_zebra = '../data/zebra.png'
image_mario = '../data/mario.png'
image_pengu = '../data/pengu.png'

#Elementos da janela primária
layout = [
    [sg.Text("Bem vindo ao protótipo do projeto fourier, por favor selecione uma imagem", justification="center")],
    [sg.Button(image_filename= image_mulie, image_size=(200, 200), key = '_1_'),
    sg.Button(image_filename= image_zebra, image_size=(200, 200), key = '_2_')],
    [sg.Button(image_filename= image_mario, image_size=(200, 200), key = '_3_'),
    sg.Button(image_filename= image_pengu, image_size=(200, 200), key = '_4_')]
]

#Criar janela primária com (Nome, Layout, tamanho, centralizador)
window = sg.Window("Projeto Fourier", layout, size=(600, 450), element_justification='c')

while True:
    event, values = window.read()
    if event == '_1_':
        escolha(image_mulie)
        break
    elif event == '_2_':
        escolha(image_zebra)
        break
    elif event == '_3_':
        escolha(image_mario)
        break
    elif event == '_4_':
        escolha(image_pengu)
        break
    if event == sg.WIN_CLOSED:
        break

window.close()
