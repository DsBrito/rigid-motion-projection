from PyQt5.QtWidgets import QMessageBox, QPushButton, QLineEdit, QLabel, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QDoubleValidator
import numpy as np

from src.utils.transformations import move, x_rotation, y_rotation, z_rotation

class World:
    def world_parameter(self):
        """
        Inicializa os parâmetros de transformação do mundo com valores padrão.

        Este trecho de código define os valores iniciais de movimentação e rotação do objeto 3D nos eixos X, Y e Z,
        que serão utilizados para manipular a posição e orientação do objeto no espaço tridimensional. Os valores
        são armazenados em um dicionário, que facilita o acesso e a modificação desses parâmetros ao longo da execução.

        Parâmetros configurados:
        -------------------------
        - X(move): 0   # Movimento do objeto no eixo X.
        - X(angle): 0  # Rotação do objeto ao redor do eixo X (em graus).
        - Y(move): 0   # Movimento do objeto no eixo Y.
        - Y(angle): 0  # Rotação do objeto ao redor do eixo Y (em graus).
        - Z(move): 0   # Movimento do objeto no eixo Z.
        - Z(angle): 0  # Rotação do objeto ao redor do eixo Z (em graus).

        Variáveis afetadas:
        -------------------
        - self.world_values: Dicionário que armazena os parâmetros de transformação do mundo:
            - "X(move):"  # Movimento do objeto no eixo X.
            - "X(angle):"  # Rotação do objeto no eixo X.
            - "Y(move):"  # Movimento do objeto no eixo Y.
            - "Y(angle):"  # Rotação do objeto no eixo Y.
            - "Z(move):"  # Movimento do objeto no eixo Z.
            - "Z(angle):"  # Rotação do objeto no eixo Z.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: world_parameter")
        self.log("Inicializando parametros de transformacao do mundo...")
        self.world_values["X(move):"] = ""
        self.world_values["X(angle):"] = ""
        self.world_values["Y(move):"] = ""
        self.world_values["Y(angle):"] = ""
        self.world_values["Z(move):"] = ""
        self.world_values["Z(angle):"] = ""
        self.log("Parametros de transformacao do mundo inicializados com sucesso.")
        self.log("Saindo da funcao world_parameter")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

    def populate_world_fields(self):
        """
        Popula os campos de entrada da interface com os valores atuais das transformações do mundo.

        Este trecho de código itera sobre os itens do dicionário `self.world_values` e, para cada chave e valor, verifica 
        se a chave correspondente está presente em `self.world_line_edits` (dicionário que armazena os campos de entrada 
        relacionados às transformações do mundo). Se a chave for encontrada, o campo de entrada correspondente é preenchido 
        com o valor atual associado à chave.

        Passos realizados:
        -------------------
        1. Itera sobre os itens no dicionário `self.world_values`, onde cada item é uma chave (parâmetro de transformação 
        do mundo) e seu respectivo valor.
        2. Verifica se a chave está presente no dicionário `self.world_line_edits` (dicionário que contém os campos de 
        entrada para os parâmetros de transformação do mundo).
        3. Se a chave for encontrada em `self.world_line_edits`, o campo de entrada correspondente é atualizado com o 
        valor atual de `self.world_values`, convertendo-o para uma string.

        Variáveis afetadas:
        -------------------
        - `self.world_line_edits`: Dicionário que contém os campos de entrada para os parâmetros de transformação do mundo.
        - `self.world_values`: Dicionário que armazena os valores atuais das transformações do mundo.
        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: populate_world_fields")
        for key, value in self.world_values.items():
            if key in self.world_line_edits:
                self.world_line_edits[key].setText(str(value))
        self.log("Campos de entrada preenchidos com sucesso.")
        self.log("Saindo da funcao populate_world_fields")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")   

    def create_world_widget(self, title):
        """
        Cria um widget contendo campos de entrada para os parâmetros de transformação do mundo.

        Este método cria e configura um `QGroupBox` que contém campos de entrada (QLineEdit) para os parâmetros de 
        transformação do mundo, como o movimento e a rotação nos eixos X, Y e Z. O widget inclui um layout de grade 
        para organizar os campos de entrada e um botão "Atualizar" para aplicar as transformações. Além disso, o método 
        configura a validação de entradas para garantir que apenas valores numéricos sejam inseridos.

        Passos realizados:
        -------------------
        1. Cria um `QGroupBox` com o título fornecido como argumento.
        2. Define o layout do `QGroupBox` como um `QVBoxLayout`, que contém uma grade (`QGridLayout`).
        3. Cria campos de entrada (QLineEdit) para os seguintes parâmetros de transformação do mundo:
            - `X(move):`
            - `X(angle):`
            - `Y(move):`
            - `Y(angle):`
            - `Z(move):`
            - `Z(angle):`
        4. Adiciona uma validação de entrada (`QDoubleValidator`) para garantir que os valores inseridos sejam numéricos.
        5. Organiza os campos de entrada e os rótulos em um layout de grade, associando cada campo ao rótulo correspondente.
        6. Cria um botão "Atualizar" que, ao ser clicado, chama o método `update_world()` para aplicar as transformações com base nos valores inseridos.
        7. Atualiza os campos de entrada com os valores atuais dos parâmetros de transformação do mundo utilizando a função `populate_world_fields()`.

        Variáveis envolvidas:
        ----------------------
        - `self.world_line_edits`: Dicionário que armazena os campos de entrada para os parâmetros de transformação do mundo.
        - `self.populate_world_fields`: Função chamada para preencher os campos de entrada com os valores dos parâmetros de transformação do mundo.
        - `self.update_world`: Função chamada para aplicar as transformações no mundo com base nos valores inseridos.

        Retorno:
        --------
        - Retorna o `QGroupBox` que contém os campos de entrada e o botão "Atualizar".
        """
        
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: create_world_widget")
        self.log("Criando widget para parametros do mundo...")
        line_edit_widget = QGroupBox(title)
        line_edit_layout = QVBoxLayout()
        line_edit_widget.setLayout(line_edit_layout)

        grid_layout = QGridLayout()

        self.log("Configurando campos de entrada para parametros do mundo...")
        labels = ['X(move):', 'X(angle):', 'Y(move):', 'Y(angle):', 'Z(move):', 'Z(angle):']  
        self.world_line_edits = {}  

        self.log("Adicionando campos de entrada para parametros do mundo...")
        for i in range(len(labels)):
            line_edit = QLineEdit()
            label = QLabel(labels[i])  
            validator = QDoubleValidator()  
            line_edit.setValidator(validator) 
            grid_layout.addWidget(label, i//2, 2*(i % 2)) 
            grid_layout.addWidget(line_edit, i//2, 2*(i % 2) + 1)
            self.world_line_edits[labels[i]] = line_edit  

        self.log("Adicionando acao no botao de atualizacao...")
        update_button = QPushButton("Atualizar")
        update_button.clicked.connect(self.update_world)
        line_edit_layout.addLayout(grid_layout)
        line_edit_layout.addWidget(update_button)


        self.populate_world_fields()
        self.log("Campos de entrada configurados com sucesso.")
        self.log("Saindo da funcao create_world_widget")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")   
        return line_edit_widget

    def update_world(self):
        """
        Atualiza os parâmetros de transformação do mundo com base nos valores inseridos nos campos de entrada.

        Este trecho de código percorre os campos de entrada relacionados aos parâmetros de transformação do mundo, obtém 
        os valores inseridos pelo usuário e atualiza tanto as variáveis do dicionário `self.world_values` quanto as variáveis
        da instância. Em caso de erro na conversão de um valor (quando o texto inserido não pode ser convertido para `float`), 
        um erro é registrado no console. Se os valores forem atualizados com sucesso, uma mensagem de sucesso é exibida.

        Passos realizados:
        -------------------
        1. Itera sobre os campos de entrada relacionados aos parâmetros de transformação do mundo, presentes em 
        `self.world_line_edits`.
        2. Para cada campo de entrada, obtém o texto inserido, verifica se há texto e, em seguida, tenta converter o texto 
        para um número (`float`).
        3. Se a conversão for bem-sucedida, o valor é armazenado no dicionário `self.world_values` e a função `world_action` 
        é chamada para aplicar a transformação.
        4. Se a conversão falhar (exceção `ValueError`), um erro é impresso no console indicando qual chave e valor causaram 
        a falha.
        5. Se todos os parâmetros forem atualizados com sucesso, uma mensagem de sucesso é exibida usando `QMessageBox`.

        Variáveis envolvidas:
        ----------------------
        - `self.world_line_edits`: Dicionário que contém os campos de entrada para os parâmetros de transformação do mundo.
        - `self.world_values`: Dicionário que armazena os valores dos parâmetros de transformação do mundo, que são atualizados com os valores inseridos.
        - `self.world_action`: Função que é chamada para aplicar a transformação com base no valor inserido para cada parâmetro.
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: update_world")
        self.log("Atualizando parametros de transformacao do mundo...")
        erro=False
        for key, world_line_edit in self.world_line_edits.items():
            text = world_line_edit.text()
            if text: 
                try:
                    self.world_values[key] = float(text)

                    self.world_action(key, self.world_values[key])


                except ValueError:
                    erro=True
                    self.ke=key
                    self.te=text
                    print(f"Erro ao converter {key} {text}")

        self.log("-----------------------------------------")
        print(erro)
        if(erro):
            QMessageBox.warning(self, "Erro de Validacao", "Os seguintes campos estao fora dos limites ou invalidos:\n\n  "+self.ke+" : "+self.te)
        else:
            QMessageBox.information(self, "Atualizacao bem-sucedida", "Parametros atualizados com sucesso!")
        self.log("Saindo da funcao update_world")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")   

    
    def move (self, dx,dy,dz):
        T = np.eye(4)
        T[0,-1] = dx
        T[1,-1] = dy
        T[2,-1] = dz
        return T

    def world_action(self, key, value):
        """
        Executa ações específicas de transformação do mundo com base no parâmetro `key` e no valor atualizado.

        Este método aplica uma transformação ao mundo, alterando a posição ou a orientação da câmera com base nos 
        parâmetros fornecidos. O método verifica o valor de `key` e aplica a transformação correspondente ao mover 
        ou rotacionar a câmera nos eixos X, Y ou Z. Após cada transformação, a função `update_canvas()` é chamada 
        para re-renderizar a cena com as novas configurações.

        Passos realizados:
        -------------------
        1. Verifica o valor de `key` para identificar qual transformação (movimento ou rotação) deve ser aplicada ao mundo.
        2. Dependendo do eixo (X, Y ou Z) e da transformação (movimento ou rotação), calcula a transformação necessária 
        utilizando as funções `move()`, `x_rotation()`, `y_rotation()`, ou `z_rotation()`.
        3. Aplica a transformação calculada, alterando a matriz de transformação da câmera (`self.cam`).
        4. Chama a função `update_canvas()` para atualizar a visualização da cena com as novas transformações aplicadas.

        Parâmetros:
        -----------
        - `key` (str): A chave que identifica qual transformação aplicar à câmera no espaço tridimensional. Pode ser um dos seguintes:
            - "X(move)" para mover a câmera ao longo do eixo X.
            - "X(angle)" para rotacionar a câmera ao redor do eixo X.
            - "Y(move)" para mover a câmera ao longo do eixo Y.
            - "Y(angle)" para rotacionar a câmera ao redor do eixo Y.
            - "Z(move)" para mover a câmera ao longo do eixo Z.
            - "Z(angle)" para rotacionar a câmera ao redor do eixo Z.
        - `value` (float): O valor de deslocamento ou ângulo de rotação a ser aplicado à transformação do mundo.

        Variáveis envolvidas:
        ----------------------
        - `self.cam`: A matriz de transformação da câmera, que é atualizada após cada transformação.
        - `self.zero_cam`: A configuração inicial da câmera, usada como referência para as transformações.
        - `self.T`: A matriz de transformação calculada para aplicar a operação de movimento ou rotação.
        - `self.update_canvas`: Função chamada para re-renderizar a visualização com as novas transformações aplicadas.

        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: world_action")
        self.log("Atualizando parametros do mundo..")
        self.log(f"Campo: {key} | Valor: {value}")

        if "X(move)" in key:
            self.T =move(value, 0, 0)
            #self.cam = np.dot(self.T, self.zero_cam) ##FIXME: Erro esta aqui, era pra ter utilizado "self.cam"
            self.cam = np.dot(self.T, self.cam)

            self.update_canvas()          


            self.update_canvas()    
        elif "X(angle)" in key:
            self.T = x_rotation(value)
            self.cam = np.dot(self.T, self.cam)
            self.update_canvas()           

        elif "Y(move)" in key:
            self.T = move(0, value, 0)
            self.cam = np.dot(self.T, self.cam)
            self.update_canvas()        

        elif "Y(angle)" in key:
            self.T = y_rotation(value)
            self.cam = np.dot(self.T, self.cam)
            self.update_canvas()          

        elif "Z(move)" in key:
            self.T = move(0, 0, value)
            self.cam = np.dot(self.T, self.cam)
            self.update_canvas()           

        elif "Z(angle)" in key:
            self.T = z_rotation(value)
            self.cam = np.dot(self.T, self.cam)
            self.update_canvas()
        self.log("Saindo da funcao world_action")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------") 