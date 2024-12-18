from PyQt5.QtWidgets import QMessageBox, QWidget, QHBoxLayout
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
import numpy as np
from mpl_toolkits.mplot3d import art3d

class Plots:

    def draw_arrows(self, point, base, axis, length=10):
        """
        Desenha vetores representando os eixos X, Y e Z a partir de um ponto no espaço 3D.

        Este método utiliza a função `quiver` da biblioteca Matplotlib para desenhar três vetores coloridos a partir de um 
        ponto dado no espaço 3D, representando os eixos X, Y e Z. Os vetores são desenhados com base na matriz `base`, 
        que define as direções dos eixos. O comprimento dos vetores pode ser ajustado com o parâmetro `length`.

        Passos realizados:
        -------------------
        1. Desenha o vetor do eixo X a partir do ponto fornecido, utilizando a direção dada pela primeira coluna da matriz `base`, 
        e colorido de vermelho.
        2. Desenha o vetor do eixo Y a partir do ponto fornecido, utilizando a direção dada pela segunda coluna da matriz `base`, 
        e colorido de verde.
        3. Desenha o vetor do eixo Z a partir do ponto fornecido, utilizando a direção dada pela terceira coluna da matriz `base`, 
        e colorido de azul.
        4. Todos os vetores são desenhados com o ponto de origem no ponto fornecido e um comprimento de vetor especificado pelo 
        parâmetro `length` (padrão é 10).

        Parâmetros:
        -----------
        - `point` (array-like, shape (3,)): O ponto de origem dos vetores no espaço 3D.
        - `base` (numpy.ndarray, shape (3, 3)): A matriz 3x3 que define as direções dos vetores (eixos X, Y e Z).
        - `axis` (matplotlib.axes.Axes3D): O eixo 3D onde os vetores serão desenhados.
        - `length` (float, opcional): O comprimento dos vetores a serem desenhados. O valor padrão é 10.
        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: draw_arrows")
        self.log("Desenhando os vetores da camera...")
        axis.quiver(point[0],point[1],point[2],base[0,0],base[1,0],base[2,0],color='red',pivot='tail',  length=length)
        axis.quiver(point[0],point[1],point[2],base[0,1],base[1,1],base[2,1],color='green',pivot='tail',  length=length)
        axis.quiver(point[0],point[1],point[2],base[0,2],base[1,2],base[2,2],color='blue',pivot='tail',  length=length)
        self.log("Vetores desenhados com sucesso.")
        self.log("Saindo da funcao draw_arrows")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

    def plot3d(self):
        """
        Plota a visualização 3D do modelo, incluindo os vetores da câmera e a malha 3D.

        Este método cria uma nova figura 3D utilizando Matplotlib, onde ele adiciona a malha 3D (`self.urso_vectors`) 
        e desenha os vetores da câmera com a função `draw_arrows()`. A visualização é renderizada em um canvas que é 
        adicionado ao layout da interface. O método também utiliza a coleção de polígonos e linhas para exibir a malha 3D 
        e seus contornos.

        Passos realizados:
        -------------------
        1. Cria uma nova figura (`self.fig2`) utilizando `plt.figure()`.
        2. Cria um eixo 3D (`self.ax2`) e adiciona uma coleção 3D com os vetores de polígono (`self.urso_vectors`).
        3. Adiciona uma coleção de linhas (contornos) à visualização utilizando os vetores de `self.urso_vectors`, 
        com cores pretas e espessura de linha configurada.
        4. Desenha os vetores da câmera no gráfico 3D utilizando a função `draw_arrows()`.
        5. Cria um canvas Matplotlib para exibir a figura no layout da interface com a variável `self.canvas2`.
        6. Adiciona o canvas à interface gráfica, vinculando-o ao layout configurado em `self.canvas_layout`.

        Variáveis envolvidas:
        ----------------------
        - `self.fig2`: A figura Matplotlib que contém o gráfico 3D.
        - `self.ax2`: O eixo 3D onde os objetos gráficos são desenhados.
        - `self.urso_vectors`: Os dados da malha 3D que serão visualizados.
        - `self.cam`: A matriz de transformação da câmera, usada para desenhar os vetores da câmera.
        - `self.canvas2`: O canvas Matplotlib que exibe a visualização 3D.
        - `self.canvas_layout`: O layout da interface onde o canvas é adicionado para exibição.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: plot3d")
        self.log("Configurando plot 3D...")
        self.fig2 = plt.figure()
        self.ax2 = self.fig2.add_subplot(111, projection='3d')
        self.ax2.set_title("Imagem 3D")
        self.ax2.set_xlabel('x-axis')
        self.ax2.set_ylabel('y-axis')
        self.ax2.set_zlabel('z-axis')
        self.ax2.add_collection3d(art3d.Poly3DCollection(self.urso_vectors))
        self.ax2.add_collection3d(art3d.Line3DCollection(self.urso_vectors, colors='k', linewidths=0.2, linestyles='-'))
        
        self.log("Desenhando setas...")
        self.draw_arrows(self.cam[:,-1],self.cam[:,0:3], self.ax2)
        
        self.log("Carregando Canvas...")
        self.canvas2 = FigureCanvas(self.fig2)
        self.canvas_layout.addWidget(self.canvas2)
        self.log("Plot 3D configurado com sucesso.")
        self.log("Saindo da funcao plot3d")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

    def plot2d(self):
        """
        Plota a projeção 2D da malha 3D utilizando os parâmetros intrínsecos da câmera.

        Este método realiza a projeção 2D da malha 3D utilizando a matriz de transformação da câmera e os parâmetros 
        intrínsecos da câmera (como distância focal, escala e ponto principal). A malha projetada é exibida em um gráfico 2D, 
        e a visualização é exibida em um canvas Matplotlib.

        Passos realizados:
        -------------------
        1. Cria uma nova figura (`self.fig1`) e um eixo (`self.ax1`) para o gráfico 2D usando Matplotlib.
        2. Define o título do gráfico como "Imagem".
        3. Calcula a matriz de calibração intrínseca `self.K` com base nos parâmetros intrínsecos fornecidos em 
        `self.params_intrinsc_values`.
        4. Calcula a inversa da matriz de calibração `self.M_ext` e a matriz de transformação 3D para 2D.
        5. Aplica a transformação 2D na malha 3D (`self.urso`) para obter as coordenadas 2D projetadas.
        6. Normaliza as coordenadas 2D dividindo pelos valores da terceira coordenada (homogênea).
        7. Define os limites dos eixos X e Y do gráfico com base nos parâmetros `n_pixels_base:` e `n_pixels_altura:`.
        8. Plota a malha projetada 2D utilizando `self.ax1.plot()` e ajusta o gráfico com uma grade e aspecto igual.
        9. Adiciona o canvas (`self.canvas1`) ao layout da interface para exibição.

        Variáveis envolvidas:
        ----------------------
        - `self.fig1`: A figura Matplotlib que contém o gráfico 2D.
        - `self.ax1`: O eixo 2D onde a projeção da malha 3D é desenhada.
        - `self.cam`: A matriz de transformação da câmera, que é usada para calcular a projeção.
        - `self.params_intrinsc_values`: Dicionário que contém os parâmetros intrínsecos da câmera.
        - `self.K`: A matriz de calibração intrínseca da câmera, utilizada para projetar a malha 3D para 2D.
        - `self.M_ext`: A inversa da matriz de calibração, usada para ajustar a projeção.
        - `self.M_x`: A matriz de transformação da câmera no espaço 3D.
        - `self.P`: A matriz de projeção final utilizada para converter a malha 3D para 2D.
        - `self.urso`: A malha 3D a ser projetada.
        - `self.URSO_2D`: A malha projetada em 2D após a transformação.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: plot2d")
        self.log("Configurando plot 2D...")
        self.fig1, self.ax1 = plt.subplots()
        self.ax1.set_title("Imagem 2D")
        self.ax1.set_xlabel('x-axis')
        self.ax1.set_ylabel('y-axis')
        self.canvas1 = FigureCanvas(self.fig1)

        self.log("Calculando parametros da camera...")
        M = self.cam
        K = np.array([[self.params_intrinsc_values['dist_focal:']*self.params_intrinsc_values["sx:"], 
                            self.params_intrinsc_values['dist_focal:']*self.params_intrinsc_values["s_theta:"], 
                            self.params_intrinsc_values["ox:"]],
                            [0, self.params_intrinsc_values['dist_focal:']*self.params_intrinsc_values["sy:"],
                            self.params_intrinsc_values["oy:"]], [0, 0, 1]])
        
        M_ext = np.linalg.inv(M)
        M_x = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
        P = np.dot(K, np.dot(M_x, M_ext))
        URSO = np.dot(P, self.urso)
        
        # Verificar se a terceira coordenada homogênea tem zeros
        erro=False
        if np.any(URSO[2] == 0):
            erro=True
            URSO[2] = 1 
            self.log("Erro de Projeção: A terceira coordenada homogenea contem zeros. A projecao nao pode ser calculada.")

        # Normalizar as coordenadas 2D
        if (erro):
            QMessageBox.warning( "Erro de Projeção", 
                            "A terceira coordenada homogênea contém zeros. A projeção não pode ser calculada.")

            
        else:
            self.log("Terceira coordenada homogenea nao contem zeros. Projecao calculada com sucesso.")
            URSO_2D = URSO / URSO[2]

        self.log("Configurando limites do plot...");
        self.ax1.set_xlim([0, self.params_intrinsc_values['n_pixels_base:']])
        self.ax1.set_ylim([self.params_intrinsc_values['n_pixels_altura:'],0])   
        self.ax1.plot(URSO_2D[0],URSO_2D[1])
        self.ax1.grid('True')
        self.ax1.set_aspect('equal')

        self.log("Carregando Canvas...")
        self.canvas_layout.addWidget(self.canvas1)

        self.log("Plot 2D configurado com sucesso.")
        self.log("Saindo da funcao plot2d")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")


    def projection_2d(self):
        """
        Calcula os parâmetros de escala e os pontos principais para a projeção 2D da câmera.

        Este método atualiza os parâmetros intrínsecos da câmera relacionados à projeção 2D, incluindo a escala nos 
        eixos X e Y, bem como os pontos principais (ox e oy). Esses parâmetros são utilizados para mapear as coordenadas
        3D do objeto para o sistema de coordenadas 2D da imagem projetada.

        Passos realizados:
        -------------------
        1. Calcula o valor de `sx:` (escala no eixo X), dividindo o número de pixels na base (`n_pixels_base:`) 
        pela largura física do sensor (`ccd_x:`).
        2. Calcula o valor de `sy:` (escala no eixo Y), dividindo o número de pixels na altura (`n_pixels_altura:`) 
        pela altura física do sensor (`ccd_y:`).
        3. Calcula o ponto principal no eixo X (`ox:`), que é a metade do número de pixels na base (`n_pixels_base:`).
        4. Calcula o ponto principal no eixo Y (`oy:`), que é a metade do número de pixels na altura (`n_pixels_altura:`).

        Variáveis envolvidas:
        ----------------------
        - `self.params_intrinsc_values`: Dicionário que contém os parâmetros intrínsecos da câmera, que são atualizados com os valores calculados:
            - "sx:" (escala no eixo X).
            - "sy:" (escala no eixo Y).
            - "ox:" (ponto principal no eixo X).
            - "oy:" (ponto principal no eixo Y).
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: projection_2d")
        self.log("Calculando projeção 2D..")
        self.params_intrinsc_values['sx:'] = self.params_intrinsc_values['n_pixels_base:']/self.params_intrinsc_values["ccd_x:"]
        self.params_intrinsc_values["sy:"] = self.params_intrinsc_values['n_pixels_altura:']/self.params_intrinsc_values["ccd_y:"]
        self.params_intrinsc_values["ox:"] = self.params_intrinsc_values['n_pixels_base:']/2
        self.params_intrinsc_values["oy:"] = self.params_intrinsc_values['n_pixels_altura:']/2
        self.log("Projeção 2D calculada com sucesso!")
        self.log("Novos valores intrínsecos:")
        self.log(f"sx: {self.params_intrinsc_values['sx:']} | sy: {self.params_intrinsc_values['sy:']} | ox: {self.params_intrinsc_values['ox:']} | oy: {self.params_intrinsc_values['oy:']}")
        self.log("Saindo da funcao projection_2d")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")


    def create_matplotlib_canvas(self):
        """
        Cria e retorna um widget contendo um canvas para exibição de gráficos 3D e 2D utilizando Matplotlib.

        Este método cria um `QWidget` para ser usado como o canvas de exibição de gráficos 3D e 2D. O canvas
        é configurado com um layout horizontal e os gráficos de projeção 2D e 3D são gerados e exibidos.

        Passos realizados:
        -------------------
        1. Cria um widget (`QWidget`) que servirá como o canvas para renderização dos gráficos.
        2. Define um layout horizontal (`QHBoxLayout`) para o widget, onde os gráficos serão colocados.
        3. Chama os métodos `projection_2d()`, `plot3d()`, e `plot2d()` para gerar e exibir os gráficos de 
        projeção 2D e gráficos 3D.
        4. Retorna o widget (`self.canvas_widget`) que contém o canvas com os gráficos renderizados.

        Variáveis afetadas:
        -------------------
        - `self.canvas_widget`: O widget que contém o canvas para exibição dos gráficos.
        - `self.canvas_layout`: O layout que organiza os gráficos dentro do `self.canvas_widget`.

        Retorno:
        --------
        - Retorna o widget `self.canvas_widget`, que contém o canvas com os gráficos renderizados.

        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: create_matplotlib_canvas")
        self.log("Criando area de desenho para graficos...")
        self.canvas_widget = QWidget()
        self.canvas_layout = QHBoxLayout()
        self.canvas_widget.setLayout(self.canvas_layout)

        self.log("Criando graficos 3D e 2D...")
        self.projection_2d()
        self.plot2d()
        self.plot3d()

        self.log("Graficos criados com sucesso.")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
        return self.canvas_widget


    def update_canvas(self):
        """
        Limpa os widgets do layout do canvas, fecha figuras existentes e re-renderiza os gráficos.

        Este método é responsável por limpar o layout onde os gráficos são exibidos, fechando qualquer figura existente 
        e removendo os widgets associados do layout. Após limpar a tela, ele chama as funções `plot3d()` e `plot2d()` 
        para re-renderizar os gráficos 3D e 2D com os dados mais atualizados.

        Passos realizados:
        -------------------
        1. Itera sobre os itens no layout `self.canvas_layout` e remove todos os widgets associados.
        2. Fecha as figuras existentes, `self.fig1` (gráfico 2D) e `self.fig2` (gráfico 3D), caso estejam definidas.
        3. Chama o método `plot3d()` para gerar e exibir novamente o gráfico 3D.
        4. Chama o método `plot2d()` para gerar e exibir novamente o gráfico 2D.

        Variáveis envolvidas:
        ----------------------
        - `self.canvas_layout`: O layout do widget onde os gráficos são exibidos. Os widgets antigos são removidos antes de re-renderizar os gráficos.
        - `self.fig1`: A figura Matplotlib que contém o gráfico 2D. Esta figura é fechada antes de ser recriada.
        - `self.fig2`: A figura Matplotlib que contém o gráfico 3D. Esta figura é fechada antes de ser recriada.
        - `self.plot3d`: Função que desenha o gráfico 3D.
        - `self.plot2d`: Função que desenha o gráfico 2D.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: update_canvas")
        self.log("Limpando layout antigo do canvas...")
        while self.canvas_layout.count():
            item = self.canvas_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.log("Atualizando canvas...")
        if hasattr(self, 'fig1'):  
            plt.close(self.fig1)

        if hasattr(self, 'fig2'): 
            plt.close(self.fig2)

        self.plot2d()
        self.plot3d()
        self.log("Canvas atualizado com sucesso.")
        self.log("Saindo da funcao update_canvas")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
