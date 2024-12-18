import numpy as np

from src.utils.transformations import move, x_rotation, y_rotation, z_rotation
from PyQt5.QtWidgets import QMessageBox, QPushButton, QLineEdit, QLabel, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QDoubleValidator



class Camera:
    def camera_parameter(self):
        """
        Inicializa os parâmetros de transformação da câmera com valores padrão.

        Este método define os valores iniciais de movimentação e rotação da câmera nos eixos X, Y e Z.
        Os parâmetros configurados são usados para controlar a posição e a orientação da câmera no espaço 3D.

        Parâmetros inicializados:
        -------------------------
        - X(move): 0
        - X(angle): 0
        - Y(move): 0
        - Y(angle): 0
        - Z(move): 0
        - Z(angle): 0

        A função não recebe parâmetros e altera o estado da variável `self.cam_values` para refletir
        os valores de transformação da câmera. Esses valores são posteriormente utilizados para manipulação
        e renderização da cena.

        Variáveis afetadas:
        -------------------
        - self.cam_values: Dicionário contendo os parâmetros de movimento e rotação da câmera:
            - "X(move):" - Movimento da câmera no eixo X.
            - "X(angle):" - Rotação da câmera ao redor do eixo X.
            - "Y(move):" - Movimento da câmera no eixo Y.
            - "Y(angle):" - Rotação da câmera ao redor do eixo Y.
            - "Z(move):" - Movimento da câmera no eixo Z.
            - "Z(angle):" - Rotação da câmera ao redor do eixo Z.
        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: camera_parameter")
        self.log("Inicializando parametros de transformacao da camera...")
        self.cam_values["X(move):"] = ""
        self.cam_values["X(angle):"] = ""
        self.cam_values["Y(move):"] = ""
        self.cam_values["Y(angle):"] = ""
        self.cam_values["Z(move):"] = ""
        self.cam_values["Z(angle):"] = ""
        self.log("Parametros de transformacao da camera inicializados com sucesso.")
        self.log("Saindo da funcao camera_parameter")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")


    def populate_cam_fields(self):
        """
        Popula os campos de entrada da interface com os valores atuais da câmera.

        Este trecho de código itera sobre os itens do dicionário `self.cam_values` e, para cada chave e valor, verifica 
        se a chave correspondente está presente em `self.cam_line_edits` (dicionário que armazena os campos de entrada 
        relacionados à câmera). Se a chave for encontrada, o campo de entrada correspondente é preenchido com o valor 
        atual associado à chave.

        Passos realizados:
        -------------------
        1. Itera sobre os itens no dicionário `self.cam_values`, onde cada item é uma chave (parâmetro da câmera) 
        e seu respectivo valor.
        2. Verifica se a chave está presente no dicionário `self.cam_line_edits` (dicionário que contém os campos de 
        entrada para os parâmetros da câmera).
        3. Se a chave for encontrada em `self.cam_line_edits`, o campo de entrada correspondente é atualizado com o 
        valor atual de `self.cam_values`, convertendo-o para uma string.

        Variáveis afetadas:
        -------------------
        - `self.cam_line_edits`: Dicionário que contém os campos de entrada para os parâmetros da câmera.
        - `self.cam_values`: Dicionário que armazena os valores atuais dos parâmetros da câmera.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: populate_cam_fields")
        self.log("Preenchendo campos de entrada para parametros da camera...")
        for key, value in self.cam_values.items():
            if key in self.cam_line_edits:
                self.cam_line_edits[key].setText(str(value))
        #self.log("Campos de entrada preenchidos com sucesso.")
        self.log("Saindo da funcao camera_parameter")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

    def create_cam_widget(self, title):
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: create_cam_widget")
        self.log("Criando widget para parametros da camera...")
        line_edit_widget = QGroupBox(title)
        line_edit_layout = QVBoxLayout()
        line_edit_widget.setLayout(line_edit_layout)
        grid_layout = QGridLayout()

        self.log("Configurando campos de entrada para parametros da camera...")
        labels = ['X(move):', 'X(angle):', 'Y(move):', 'Y(angle):', 'Z(move):', 'Z(angle):']  
        self.cam_line_edits = {} 

        for i in range(len(labels)):
            line_edit = QLineEdit()
            label = QLabel(labels[i]) 
            validator = QDoubleValidator()
            line_edit.setValidator(validator) 
            grid_layout.addWidget(label, i//2, 2*(i % 2))  
            grid_layout.addWidget(line_edit, i//2, 2*(i % 2) + 1)
            self.cam_line_edits[labels[i]] = line_edit 
        self.log("Campos de entrada configurados com sucesso.")

        self.log("Adicionando acao no botao de atualizacao...")
        update_button = QPushButton("Atualizar")
        update_button.clicked.connect(self.update_cam)
        line_edit_layout.addLayout(grid_layout)
        line_edit_layout.addWidget(update_button)
        self.log("Acao adicionada com sucesso.")

        self.populate_cam_fields()
        self.log("Saindo da funcao create_cam_widget")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

        return line_edit_widget

    def update_cam(self):
        """
        Atualiza os valores no dicionário `cam_values` com base no input do usuário.

        Este método percorre os campos de entrada relacionados aos parâmetros da câmera, obtém os valores inseridos 
        pelo usuário, os converte para o tipo adequado e atualiza tanto os valores no dicionário `self.cam_values` quanto
        as variáveis associadas. Caso algum valor inserido seja inválido (não puder ser convertido para `float`), o erro 
        será registrado no console. Após a atualização bem-sucedida, uma mensagem de sucesso é exibida.

        Passos realizados:
        -------------------
        1. Itera sobre os campos de entrada presentes em `self.cam_line_edits`, que contêm os valores para os parâmetros da câmera.
        2. Para cada campo de entrada, obtém o texto inserido e tenta convertê-lo para `float`.
        3. Se a conversão for bem-sucedida, o valor é armazenado no dicionário `self.cam_values`, e a função `cam_action` 
        é chamada para aplicar a transformação ou atualização associada.
        4. Se a conversão falhar (exceção `ValueError`), um erro é impresso no console com o nome da chave e o valor falho.
        5. Após a atualização de todos os parâmetros, uma mensagem de sucesso é exibida usando `QMessageBox`.

        Variáveis envolvidas:
        ----------------------
        - `self.cam_line_edits`: Dicionário que contém os campos de entrada para os parâmetros da câmera.
        - `self.cam_values`: Dicionário que armazena os valores atualizados dos parâmetros da câmera.
        - `self.cam_action`: Função que é chamada para processar a atualização ou transformação da câmera com base nos valores inseridos.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: update_cam")
        self.log("Atualizando parametros da camera...")

        # printar cada elemento do dicionario
        for key, value in self.cam_values.items():
            print(f"{key}: {value}")
        erro=False

        for key, cam_line_edit in self.cam_line_edits.items():

            text = cam_line_edit.text()
            if text: 
                try:
                    self.cam_values[key] = float(text)

                    self.cam_action(key, self.cam_values[key])


                except ValueError:
                    erro=True
                    self.ke=key
                    self.te=text
                    print(f"Erro ao converter {key} {text}")
                    print(erro)
        self.log("-----------------------------------------------------------------------------------------")
        if(erro):
            QMessageBox.warning(self, "Erro de Validacao", "Os seguintes campos estao fora dos limites ou invalidos:\n\n  "+self.ke+" : "+self.te)
        else:
            QMessageBox.information(self, "Atualizacao bem-sucedida", "Parametros atualizados com sucesso!")
        self.log("Saindo da funcao update_cam")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
    
    def cam_action(self, key, value):
        """
        Executa ações específicas para mover ou rotacionar a câmera com base nos parâmetros fornecidos.

        Este método realiza a atualização da posição ou orientação da câmera no espaço tridimensional com base no parâmetro 
        `key` e no valor `value`. O método identifica qual transformação aplicar à câmera (movimento ou rotação nos eixos X, Y ou Z) 
        e aplica a transformação correspondente. Após a atualização, o método chama `update_canvas()` para renderizar as alterações.

        Passos realizados:
        -------------------
        1. Verifica o valor de `key` para determinar qual transformação aplicar (movimento ou rotação) na câmera.
        2. Dependendo do eixo identificado (X, Y ou Z), calcula a transformação correspondente (movimento ou rotação) 
        utilizando as funções `move()`, `x_rotation()`, `y_rotation()`, ou `z_rotation()`.
        3. Aplica a transformação calculada na câmera, atualizando a matriz de transformação `self.cam`.
        4. Chama a função `update_canvas()` para re-renderizar a visualização com a nova posição e orientação da câmera.

        Parâmetros:
        -----------
        - `key` (str): A chave que identifica qual transformação aplicar à câmera. Pode ser um dos seguintes:
            - "X(move)" para mover a câmera ao longo do eixo X.
            - "X(angle)" para rotacionar a câmera ao redor do eixo X.
            - "Y(move)" para mover a câmera ao longo do eixo Y.
            - "Y(angle)" para rotacionar a câmera ao redor do eixo Y.
            - "Z(move)" para mover a câmera ao longo do eixo Z.
            - "Z(angle)" para rotacionar a câmera ao redor do eixo Z.
        - `value` (float): O valor de deslocamento ou ângulo de rotação a ser aplicado à câmera.

        Variáveis envolvidas:
        ----------------------
        - `self.cam`: A matriz de transformação da câmera, que é atualizada com a nova posição ou orientação.
        - `self.zero_cam`: A configuração inicial da câmera (referência para a transformação).
        - `self.T`: A matriz de transformação calculada para a operação de movimento ou rotação.
        - `self.update_canvas`: Função chamada para atualizar a renderização da cena após a transformação.

        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: cam_action")
        self.log("Atualizando parametros da camera..")
        self.log(f"Campo: {key} | Valor: {value}")
        if "X(move)" in key:
           
            accumulated_cam = self.cam
            self.T = move(value,0,0)
            aux_cam = np.dot(self.T,self.zero_cam)
            self.cam = np.dot(accumulated_cam,aux_cam)
            self.update_canvas()            

        elif "X(angle)" in key:
            accumulated_cam = self.cam
            self.T = x_rotation(value)
            aux_cam = np.dot(self.T,self.zero_cam)
            self.cam = np.dot(accumulated_cam,aux_cam)
            self.update_canvas()           
        elif "Y(move)" in key:
            accumulated_cam = self.cam
            self.T = move(0,value,0)
            aux_cam = np.dot(self.T,self.zero_cam)
            self.cam = np.dot(accumulated_cam,aux_cam)
            self.update_canvas()            

        elif "Y(angle)" in key:
            accumulated_cam = self.cam
            self.T = y_rotation(value)
            aux_cam = np.dot(self.T,self.zero_cam)
            self.cam = np.dot(accumulated_cam,aux_cam)
            self.update_canvas()   

        elif "Z(move)" in key:
            accumulated_cam = self.cam
            self.T = move(0, 0, value)
            aux_cam = np.dot(self.T,self.zero_cam)
            self.cam = np.dot(accumulated_cam,aux_cam)
            self.update_canvas()           

        elif "Z(angle)" in key:
            accumulated_cam = self.cam
            self.T = z_rotation(value)
            aux_cam = np.dot(self.T,self.zero_cam)
            self.cam = np.dot(accumulated_cam,aux_cam)
            self.update_canvas()          
        self.log("Saindo da funcao cam_action")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")