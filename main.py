

# Importacoes necessarias para o código funcionar corretamente 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, 
    QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QIcon
from src.utils.load_stl import load_stl
from src.camera.initialize_camera import initialize_camera
from src.plot.plot import Plots
from src.world.world_config import World
from src.intrinsic.intrinsic_config import Intrinsic
from src.reset.reset_config import Reset
from src.camera.camera import Camera  # Import the Camera class
from src.utils.tutorial_popup import TutorialPopup
import matplotlib.pyplot as plt

class MainWindow(QMainWindow, Plots, Camera, World, Intrinsic,Reset):

    def log(self, message):
        print(f"[LOG] {message}")
    
    def __init__(self):
        """
        Inicializa a janela principal e configura as variáveis, valores padrão, e a interface de usuário.
        Este método cria a estrutura básica do programa, definindo:
        - Título e dimensões da janela.
        - Valores padrão para transformações do mundo, transformações da câmera e parâmetros intrínsecos da câmera.
        - Configura a interface gráfica inicial.
        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: __init__")
        self.log("Iniciando a aplicacao...")

        # Chamada ao construtor da classe base QMainWindow.
        super().__init__()
        self.log("Construtor da classe base chamado com sucesso.")

        # Inicializa as variaveis de configuracao necessarias para a aplicacao.
        self.set_variables()

        # Define os textos nas janelas e icones.
        self.setWindowTitle("Github: Dsbrito ~ Visão Computacional com a Professora Raquel ~ Trabalho 1 - Movimento de Corpo Rígido e Projeção Perspectiva")
        self.setWindowIcon(QIcon('./assets/img/icon.png'))
        
        self.log("Textos da janela configurado.")

        # Define a posicao inicial e o tamanho da janela.
        self.setGeometry(100, 100, 1280, 720)
        self.log("Dimensoes da janela configuradas para 1280x720 pixels.")

        # Inicializa os valores padrao para transformacoes do mundo.
        self.world_values = {  
            "X(move):":  0,
            "X(angle):":  0,
            "Y(move):":  0,
            "Y(angle):": 0,
            "Z(move):":  0,
            "Z(angle):": 0,
        }
        self.log(f"Valores padrao de transformacoes do mundo inicializados: {self.world_values}")

        # Inicializa os valores padrao para transformacoes da camera.
        self.cam_values = { 
            "X(move):":  0,
            "X(angle):":  0,
            "Y(move):":  0,
            "Y(angle):": 0,
            "Z(move):":  0,
            "Z(angle):": 0,
        }   
        self.log(f"Valores padrao de transformacoes da camera inicializados: {self.cam_values}")

        # Inicializa os parametros intrinsecos da camera.
        self.params_intrinsc_values = { 
            "n_pixels_base:": 0,
            "n_pixels_altura:": 0,
            "ccd_x:": 0,
            "ccd_y:": 0,
            "dist_focal:": 0,
            "s_theta:": 0,
            "sx:": 0,
            "sy:": 0,
            "ox:": 0,
            "oy:": 0,
        }
        self.log(f"Parametros intrinsecos da camera inicializados: {self.params_intrinsc_values}")

        # Configura e exibe a interface grafica principal do programa.
        try:
            self.InterfaceUI()
            self.log("Interface grafica configurada com sucesso.")
            self.log("Saindo da funcao __init__.")
            self.log("-----------------------------------------")
            self.log("-----------------------------------------")


        except Exception as e:
            self.log(f"Erro ao configurar a interface grafica: {e}")
            self.log("-----------------------------------------")

    def set_variables(self):
        """
        Inicializa as variáveis essenciais para a aplicação, incluindo a malha 3D e a configuração da câmera.

        Esta função realiza as seguintes tarefas:
        1. Carrega a malha STL do arquivo especificado e armazena as informações necessárias para manipulação.
        2. Inicializa as configurações da câmera, incluindo vetores, matriz de transformação, 
        posição inicial e parâmetros adicionais.

        Variáveis inicializadas:
        ------------------------
        - self.urso: Objeto da malha STL carregada.
        - self.urso_vectors: Coordenadas dos vetores da malha STL.
        - self.e1, self.e2, self.e3: Vetores base da câmera no espaço 3D.
        - self.Rx: Matriz de rotação no eixo X.
        - self.T: Matriz de transformação.
        - self.base: Base inicial da câmera.
        - self.cam: Matriz de configuração atual da câmera (pose e orientação no espaço 3D).
        - self.zero_cam: Configuração inicial da câmera, usada como referência.
        - self.a: Parâmetro adicional, relacionado à câmera.
        - self.w: Parâmetro adicional, relacionado à câmera.
        - self.largura: Largura do campo de visão da câmera.
        - self.altura: Altura do campo de visão da câmera.
        - self.title: Título associado à configuração da câmera.

        Dependências:
        -------------
        - `load_stl`: Função externa responsável por carregar o arquivo STL e retornar os dados da malha.
        - `initialize_camera`: Função externa que retorna as configurações iniciais da câmera.

        Arquivo necessário:
        -------------------
        - './assets/2020.STL': Caminho relativo para o arquivo STL contendo a malha 3D.

        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: set_variables")
        self.log("Carregando tutorial...")
        your_mesh=TutorialPopup()
        self.log("Tutorial carregado com sucesso.")

        self.log("Inicializando variaveis essenciais para a aplicacao...")
        self.log("Carregando malha STL...")
        self.log(f"Malha STL escolhida: {your_mesh}")

        try: 
            self.urso, self.urso_vectors = load_stl(your_mesh)
            self.log("Malha STL carregada com sucesso.")
        except Exception as e:
            urso_mesh = './assets/stl/urso.STL'
            QMessageBox.warning(self, "Erro", f" Voce não escolheu nenhuma malha e fechou o tutorial.arregando a malha padrão: {urso_mesh}", QMessageBox.Ok)
            self.log(f"Voce fechou o tutorial, a malha carregada sera: {urso_mesh}")
            self.urso, self.urso_vectors = load_stl(urso_mesh)
            
        self.log("Inicializando configuracoes da camera...")   

        camera_config = initialize_camera()
        self.e1 = camera_config['e1']
        self.e2 = camera_config['e2']
        self.e3 = camera_config['e3']
        self.Rx  = camera_config['x_90']
        self.T = camera_config['T']

        self.base = camera_config['base']
        self.cam = camera_config['cam']
        self.zero_cam = self.cam
        self.a = camera_config['a']
        self.w = camera_config['w']
         
        self.largura = camera_config['largura']
        self.altura = camera_config['altura']
        self.title = camera_config['title']

        self.log("Variaveis essenciais inicializadas com sucesso.")
        self.log("Saindo da funcao set_variables.")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
    
    def InterfaceUI(self):
        """
        Configura e exibe a interface gráfica principal da aplicação, incluindo widgets e layout.

        Este método inicializa a interface do usuário, configurando os parâmetros necessários, widgets 
        e a organização do layout da interface. Ele inclui a exibição de elementos gráficos, como botões, 
        campos de entrada e gráficos interativos, proporcionando uma interface visual para interação com 
        a projeção 3D e os parâmetros da câmera.

        Passos realizados:
        -------------------
        1. Exibe um tutorial interativo usando a função `TutorialPopup()`.
        2. Inicializa os parâmetros da câmera, parâmetros intrínsecos e transformações do mundo através das 
        funções `intrinsc_parameter()`, `camera_parameter()`, e `world_parameter()`.
        3. Cria e organiza widgets de entrada para o ajuste de parâmetros (referência de mundo, câmera, e parâmetros intrínsecos).
        4. Cria e exibe a área de desenho 3D interativo usando o `create_matplotlib_canvas()`.
        5. Adiciona um botão "Reset" que, ao ser pressionado, reseta os parâmetros e re-renderiza a interface.
        6. Organiza os widgets e elementos gráficos em um layout de grade (grid layout).

        Componentes adicionados ao layout:
        -----------------------------------
        - `line_edit_widget1`: Widget de entrada para manipulação de parâmetros do mundo.
        - `line_edit_widget2`: Widget de entrada para manipulação de parâmetros da câmera.
        - `line_edit_widget3`: Widget de entrada para manipulação dos parâmetros intrínsecos.
        - `self.canvas`: Área de desenho para projeções 3D e 2D.
        - `reset_button`: Botão para reiniciar os parâmetros e atualizar os gráficos.

        Variáveis afetadas:
        -------------------
        - `self.canvas`: Área de desenho onde os gráficos são renderizados.
        - `self.grid_layout`: Layout que organiza os widgets na interface.
        - `self.central_widget`: Widget central que contém o layout da interface.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: InterfaceUI")
        self.log("Configurando interface grafica...")
        self.log("Criando layout da interface...")


        self.log("Configurando parametros ...")
        self.intrinsc_parameter()
        self.camera_parameter()
        self.world_parameter()
        self.log("Parametros configurados com sucesso.")

        self.log("Criando widgets da interface...")
        grid_layout = QGridLayout()

        line_edit_widget1 = self.create_world_widget("Referencia do Mundo")
        line_edit_widget2  = self.create_cam_widget("Referencia da Camera")
        line_edit_widget3  = self.create_intrinsic_widget("Params Intrinsecos")
        self.canvas = self.create_matplotlib_canvas()
        grid_layout.addWidget(line_edit_widget1, 0, 0)
        grid_layout.addWidget(line_edit_widget2, 0, 1)
        grid_layout.addWidget(line_edit_widget3, 0, 2)
        grid_layout.addWidget(self.canvas, 1, 0, 1, 3)

        self.log("Configurando botao de reset...")
        reset_widget = QWidget()
        reset_layout = QHBoxLayout()
        reset_widget.setLayout(reset_layout)
        reset_button = QPushButton("Reset")
        reset_button.setFixedSize(50, 30)  
        style_sheet = """
            QPushButton {
                color : white ;
                background: rgba(255, 127, 130,128);
                font: inherit;
                border-radius: 5px;
                line-height: 1;
            }
        """
        reset_button.setStyleSheet(style_sheet)
        reset_button.clicked.connect(self.reset_canvas)
        reset_layout.addWidget(reset_button)
        grid_layout.addWidget(reset_widget, 2, 0, 1, 3)
        self.log("Botao de reset configurado com sucesso.")

        central_widget = QWidget()
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)
        self.log("Interface grafica configurada com sucesso.")
        self.log("Saindo da funcao InterfaceUI.")
        self.log("-----------------------------------------")


if __name__=="__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())