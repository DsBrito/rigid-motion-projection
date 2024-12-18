from PyQt5.QtWidgets import QMessageBox, QPushButton, QLineEdit, QLabel, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QDoubleValidator
import numpy as np

from src.utils.transformations import move, x_rotation, y_rotation, z_rotation

class Reset:
    def reset_parameter(self):
        """
        Reseta os parâmetros da câmera, intrínsecos e de transformação do mundo para seus valores iniciais.

        Este método chama funções responsáveis por redefinir os parâmetros da câmera, os parâmetros intrínsecos e as 
        transformações do mundo para seus valores padrão. Após isso, ele atualiza os campos de entrada da interface com 
        os valores padrão, recalcula a projeção 2D e atualiza a visualização com a nova configuração.

        Passos realizados:
        -------------------
        1. Chama a função `intrinsc_parameter()` para redefinir os parâmetros intrínsecos da câmera para os valores padrão.
        2. Chama a função `camera_parameter()` para redefinir os parâmetros da câmera (movimento e rotação) para os valores padrão.
        3. Chama a função `world_parameter()` para redefinir os parâmetros de transformação do mundo para os valores padrão.
        4. Atualiza os campos de entrada da interface gráfica com os valores padrão dos parâmetros intrínsecos, da câmera e do mundo, 
        utilizando as funções `populate_intrinsic_fields()`, `populate_cam_fields()` e `populate_world_fields()`.
        5. Recalcula a projeção 2D chamando a função `projection_2d()`.
        6. Chama a função `update_canvas()` para atualizar a visualização com os novos parâmetros e projeções.

        Variáveis envolvidas:
        ----------------------
        - `self.intrinsc_parameter`: Função que redefine os parâmetros intrínsecos da câmera.
        - `self.camera_parameter`: Função que redefine os parâmetros da câmera.
        - `self.world_parameter`: Função que redefine os parâmetros de transformação do mundo.
        - `self.populate_intrinsic_fields`: Função que atualiza os campos de entrada com os valores dos parâmetros intrínsecos.
        - `self.populate_cam_fields`: Função que atualiza os campos de entrada com os valores dos parâmetros da câmera.
        - `self.populate_world_fields`: Função que atualiza os campos de entrada com os valores dos parâmetros de transformação do mundo.
        - `self.projection_2d`: Função que recalcula a projeção 2D após a redefinição dos parâmetros.
        - `self.update_canvas`: Função que atualiza a visualização dos gráficos com os novos parâmetros.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: reset_parameter")
        self.log("Resetando parametros..")        
        self.intrinsc_parameter()
        self.camera_parameter()
        self.world_parameter()

        
        self.populate_intrinsic_fields()
        self.populate_cam_fields()
        self.populate_world_fields()

        self.projection_2d()
        self.update_canvas()
        self.log("Saindo da funcao reset_parameter")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
        
    def reset(self):
        """
        Reseta a configuração da câmera para o estado inicial.

        Este método redefine a posição e a orientação da câmera para valores padrão, realizando a redefinição da matriz
        de transformação da câmera (`self.cam`). Ele também configura a câmera para o ponto de origem no espaço tridimensional 
        e realiza uma rotação e translação iniciais. Após a execução, a câmera estará em uma posição inicial predefinida.

        Passos realizados:
        -------------------
        1. Inicializa os vetores de base (`e1`, `e2`, `e3`) para os eixos X, Y e Z, respectivamente, e cria a matriz de base.
        2. Cria o ponto de origem `point` na posição `[0, 0, 0, 1]` (homogêneo).
        3. Concatena a matriz de base com o ponto de origem para formar a matriz de transformação inicial `self.cam`.
        4. Define `self.zero_cam` como a configuração inicial da câmera.
        5. Aplica uma rotação de -90 graus no eixo X utilizando a função `x_rotation(-90)`.
        6. Aplica uma translação de 35 unidades ao longo do eixo Z e -60 unidades ao longo do eixo Y usando a função `move(0, -60, 35)`.
        7. Atualiza `self.cam` com a nova matriz resultante das transformações de rotação e translação.

        Variáveis envolvidas:
        ----------------------
        - `self.cam`: A matriz de transformação da câmera, que é atualizada com a nova posição e orientação.
        - `self.zero_cam`: A configuração inicial da câmera, que é salva para referência futura.
        - `x_90`: A matriz de rotação que realiza a rotação de -90 graus no eixo X.
        - `T`: A matriz de translação que aplica a translação de 35 unidades ao longo do eixo Z e -60 unidades ao longo do eixo Y.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: reset")
        self.log("Resetando..")
        e1 = np.array([[1],[0],[0],[0]]) # X
        e2 = np.array([[0],[1],[0],[0]]) # Y
        e3 = np.array([[0],[0],[1],[0]]) # Z
        base = np.hstack((e1,e2,e3))

        point =np.array([[0],[0],[0],[1]])

        self.cam = np.hstack((base,point))

        self.zero_cam = self.cam

        x_90 =x_rotation(-90)

        T = move(0, -60, 35)

        self.cam = np.dot(x_90, self.cam)
        self.cam = np.dot(T, self.cam)
        self.log("Saindo da funcao reset")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
    def reset_canvas(self):
        """
        Reseta a configuração da câmera, os parâmetros e o canvas de visualização para o estado inicial.

        Este método realiza a reinicialização completa da câmera, dos parâmetros da câmera, intrínsecos e de transformação 
        do mundo, e a atualização do canvas de visualização. Ele chama os métodos `reset()` e `reset_parameter()` para 
        redefinir todos os parâmetros e a configuração da câmera, e então exibe uma mensagem de sucesso.

        Passos realizados:
        -------------------
        1. Chama o método `reset()` para redefinir a configuração inicial da câmera, incluindo a posição e orientação.
        2. Chama o método `reset_parameter()` para redefinir os parâmetros intrínsecos, de câmera e de transformação do mundo.
        3. Exibe uma mensagem de sucesso usando `QMessageBox.information()` informando que os parâmetros foram atualizados com sucesso.

        Variáveis envolvidas:
        ----------------------
        - `self.reset()`: Método que redefine a configuração inicial da câmera.
        - `self.reset_parameter()`: Método que redefine os parâmetros da câmera, intrínsecos e de transformação do mundo.

        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: reset_canvas")
        self.log("Resetando canvas..")        
        self.reset()
        self.reset_parameter()
        QMessageBox.information(self, "Reset bem-sucedido", "Parametros atualizados com sucesso!")
        self.log("Saindo da funcao reset_canvas")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
    