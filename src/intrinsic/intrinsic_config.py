from PyQt5.QtWidgets import QMessageBox, QPushButton, QLineEdit, QLabel, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QDoubleValidator

class Intrinsic:
    def intrinsc_parameter(self):
        """
        Inicializa os parâmetros intrínsecos da câmera com valores padrão e calcula parâmetros derivados.

        Este trecho de código configura e calcula os principais parâmetros necessários para a calibração da câmera, 
        incluindo a resolução do sensor, as dimensões físicas, a distância focal e os pontos principais. Além disso, 
        são calculados os parâmetros de escala para os eixos X e Y, que são usados nas projeções 2D e 3D.

        Parâmetros definidos:
        ---------------------
        - n_pixels_base: 1050   # Número de pixels na base (horizontal) do sensor.
        - n_pixels_altura: 700  # Número de pixels na altura (vertical) do sensor.
        - ccd_x: 36             # Largura física do sensor em milímetros (mm).
        - ccd_y: 24             # Altura física do sensor em milímetros (mm).
        - dist_focal: 10        # Distância focal da câmera em milímetros (mm).
        - s_theta: 0            # Inclinação do sensor.
        - sx: Calculado como a razão entre o número de pixels na base e a largura física do sensor (n_pixels_base / ccd_x).
        - sy: Calculado como a razão entre o número de pixels na altura e a altura física do sensor (n_pixels_altura / ccd_y).
        - ox: Ponto principal no eixo x, calculado como a metade do número de pixels na base (n_pixels_base / 2).
        - oy: Ponto principal no eixo y, calculado como a metade do número de pixels na altura (n_pixels_altura / 2).

        Variáveis afetadas:
        -------------------
        - self.params_intrinsc_values: Dicionário que armazena os parâmetros intrínsecos da câmera:
            - "n_pixels_base:"  # Número de pixels na base do sensor.
            - "n_pixels_altura:"  # Número de pixels na altura do sensor.
            - "ccd_x:"  # Largura física do sensor.
            - "ccd_y:"  # Altura física do sensor.
            - "dist_focal:"  # Distância focal da câmera.
            - "s_theta:"  # Inclinação do sensor .
            - "sx:"  # Escala no eixo x.
            - "sy:"  # Escala no eixo y.
            - "ox:"  # Ponto principal no eixo x (meia largura do sensor).
            - "oy:"  # Ponto principal no eixo y (meia altura do sensor).

        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: intrinsc_parameter")
        self.log("Inicializando parametros intrinsecos da camera...")
        self.params_intrinsc_values["n_pixels_base:"] = 1050
        self.params_intrinsc_values["n_pixels_altura:"] = 700
        self.params_intrinsc_values["ccd_x:"] = 36
        self.params_intrinsc_values["ccd_y:"] = 24
        self.params_intrinsc_values["dist_focal:"] = 10
        self.params_intrinsc_values["s_theta:"] = 0
        self.params_intrinsc_values["sx:"] = self.params_intrinsc_values["n_pixels_base:"]/self.params_intrinsc_values["ccd_x:"]
        self.params_intrinsc_values["sy:"] = self.params_intrinsc_values["n_pixels_altura:"]/self.params_intrinsc_values["ccd_y:"]
        self.params_intrinsc_values["ox:"] = self.params_intrinsc_values["n_pixels_base:"]/2
        self.params_intrinsc_values["oy:"] = self.params_intrinsc_values["n_pixels_altura:"]/2
        self.log("Parametros intrinsecos da camera inicializados com sucesso.")
        self.log("Saindo da funcao intrinsc_parameter")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

    def populate_intrinsic_fields(self):
        """
        Popula os campos de entrada da interface com os valores atuais dos parâmetros intrínsecos da câmera.

        Este método itera sobre os itens do dicionário `self.params_intrinsc_values` e, para cada chave e valor, 
        verifica se a chave correspondente está presente em `self.params_intrinsc_line_edits` (dicionário que 
        armazena os campos de entrada relacionados aos parâmetros intrínsecos). Se a chave for encontrada, o campo 
        de entrada correspondente é preenchido com o valor atual associado à chave.

        Passos realizados:
        -------------------
        1. Itera sobre os itens no dicionário `self.params_intrinsc_values`, onde cada item é uma chave (parâmetro 
        intrínseco da câmera) e seu respectivo valor.
        2. Verifica se a chave está presente no dicionário `self.params_intrinsc_line_edits` (dicionário que contém 
        os campos de entrada para os parâmetros intrínsecos).
        3. Se a chave for encontrada em `self.params_intrinsc_line_edits`, o campo de entrada correspondente é 
        atualizado com o valor atual de `self.params_intrinsc_values`, convertendo-o para uma string.

        Variáveis afetadas:
        -------------------
        - `self.params_intrinsc_line_edits`: Dicionário que contém os campos de entrada para os parâmetros 
        intrínsecos da câmera.
        - `self.params_intrinsc_values`: Dicionário que armazena os valores atuais dos parâmetros intrínsecos da câmera.

        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: populate_intrinsic_fields")
        for key, value in self.params_intrinsc_values.items():
            if key in self.params_intrinsc_line_edits:
                self.params_intrinsc_line_edits[key].setText(str(value))
        self.log("Campos de entrada preenchidos com sucesso.")
        self.log("Saindo da funcao populate_intrinsic_fields")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

    def create_intrinsic_widget(self, title):
        """
        Cria um widget contendo campos de entrada para os parâmetros intrínsecos da câmera.

        Este método cria e configura um `QGroupBox` que contém campos de entrada (QLineEdit) para os principais 
        parâmetros intrínsecos da câmera, como número de pixels, dimensões do sensor e distância focal. Além disso,
        ele inclui validações de entrada para garantir que os valores inseridos estejam dentro dos limites permitidos.

        Passos realizados:
        -------------------
        1. Cria um `QGroupBox` com o título fornecido como argumento.
        2. Define o layout do `QGroupBox` como um `QVBoxLayout` que contém uma grade (`QGridLayout`).
        3. Cria campos de entrada (QLineEdit) para cada um dos seguintes parâmetros:
            - `n_pixels_base:`
            - `n_pixels_altura:`
            - `ccd_x:`
            - `ccd_y:`
            - `dist_focal:`
            - `s_theta:`
        4. Adiciona validações de entrada para garantir que os valores inseridos estejam dentro de limites definidos para cada parâmetro.
        5. Cria um botão "Atualizar" que, ao ser clicado, valida e atualiza os parâmetros com base nos valores inseridos.
        6. Popula os campos de entrada com os valores atuais dos parâmetros intrínsecos.

        Variáveis afetadas:
        -------------------
        - `self.params_intrinsc_line_edits`: Dicionário que armazena os campos de entrada para os parâmetros intrínsecos.
        - `self.line_edit_widget`: O widget contendo os campos de entrada organizados em um layout.

        Retorno:
        --------
        - Retorna o `QGroupBox` que contém os campos de entrada e o botão "Atualizar".
        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: create_intrinsic_widget")
        self.log("Criando widget para parametros intrinsecos...")
        line_edit_widget = QGroupBox(title)
        line_edit_layout = QVBoxLayout()
        line_edit_widget.setLayout(line_edit_layout)
        grid_layout = QGridLayout()



        self.log("Definindo limites para os campos de entrada...")
        limits = {
            'n_pixels_base:': (640, 1920),
            'n_pixels_altura:': (480, 1080),
            'ccd_x:': (10, 50),
            'ccd_y:': (10, 50),
            'dist_focal:': (1, 1000),
            's_theta:': (-1000, 1000)
        }

        self.log("Configurando campos de entrada para parametros intrinsecos...")
        self.params_intrinsc_line_edits = {} 
        labels = [
            'n_pixels_base:', 
            'n_pixels_altura:', 
            'ccd_x:', 
            'ccd_y:', 
            'dist_focal:', 
            's_theta:'
        ]
        for i, label_text in enumerate(labels):
            line_edit = QLineEdit()
            label = QLabel(label_text)

            min_val, max_val = limits[label_text]
            validator = QDoubleValidator(float(min_val), float(max_val), 2, self)
            validator.setNotation(QDoubleValidator.StandardNotation)
            line_edit.setValidator(validator) 

            grid_layout.addWidget(label, i // 2, 2 * (i % 2))
            grid_layout.addWidget(line_edit, i // 2, 2 * (i % 2) + 1)

            self.params_intrinsc_line_edits[label_text] = line_edit
        self.log("Campos de entrada configurados com sucesso.")

        self.log("Adicionando botao de atualizacao...")
        update_button = QPushButton("Atualizar")
        update_button.clicked.connect(lambda: self.validate_and_update_params(limits))
        line_edit_layout.addLayout(grid_layout)
        line_edit_layout.addWidget(update_button)
        self.log("Botao de atualizacao adicionado com sucesso.")

        self.populate_intrinsic_fields()
        self.log("Campos de entrada preenchidos com valores iniciais.")
        self.log("Saindo da funcao create_intrinsic_widget")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

        return line_edit_widget

    def validate_and_update_params(self, limits):
        
        """
        Valida os campos de entrada antes de atualizar os parâmetros intrínsecos.

        Este trecho de código valida os campos de entrada relacionados aos parâmetros intrínsecos da câmera para garantir
        que os valores inseridos estejam dentro dos limites definidos para cada campo. Caso algum valor seja inválido ou 
        fora do intervalo permitido, um erro será exibido ao usuário. Se todos os campos forem válidos, os parâmetros 
        serão atualizados com os valores fornecidos.

        Passos realizados:
        -------------------
        1. Itera sobre os itens em `self.params_intrinsc_line_edits`, que contém os campos de entrada.
        2. Para cada campo, obtém o valor inserido e verifica se ele está dentro dos limites definidos em `limits`.
        3. Se o valor estiver fora do intervalo permitido ou for inválido (não for um número), ele é adicionado a uma lista de campos inválidos.
        4. Se houver campos inválidos, exibe uma mensagem de erro com os detalhes dos campos fora dos limites ou com valores inválidos.
        5. Se todos os campos forem válidos, chama o método `update_params_intrinsc` para atualizar os parâmetros.

        Variáveis e componentes envolvidos:
        -----------------------------------
        - `self.params_intrinsc_line_edits`: Dicionário que contém os campos de entrada para os parâmetros intrínsecos.
        - `limits`: Dicionário que define os limites mínimo e máximo para cada parâmetro.
        - `invalid_fields`: Lista que armazena os campos inválidos encontrados durante a validação.
        - `error_message`: Mensagem de erro que será exibida ao usuário caso existam campos inválidos.

        """

        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: validate_and_update_params")
        
        self.log("Validando campos de entrada...")
        invalid_fields = []

        for label, line_edit in self.params_intrinsc_line_edits.items():
            text = line_edit.text()
            min_val, max_val = limits[label]
            self.log(f"Validando campo {label} com valor {text} (min: {min_val}, max: {max_val})")  
            try:
                value = float(text)
                if value < min_val or value > max_val:
                    invalid_fields.append(f"{label} (valor digitado: {text}, limite: {min_val} a {max_val})")
            except ValueError:
                invalid_fields.append(f"{label} (valor digitado: {text}, valor invalido)")

        if invalid_fields:
            error_message = "Os seguintes campos estao fora dos limites ou invalidos:\n\n" + "\n".join(invalid_fields)
            QMessageBox.warning(self, "Erro de Validacao", error_message)
            return
        
        self.update_params_intrinsc()
        self.log("Campos de entrada validados com sucesso.")
        self.log("Saindo da funcao validate_and_update_params")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")

    def update_params_intrinsc(self):
        """
        Atualiza as variáveis e o dicionário de parâmetros intrínsecos com base nos valores inseridos nos campos de entrada.

        Este método percorre os campos de entrada relacionados aos parâmetros intrínsecos da câmera, obtém os valores 
        inseridos pelo usuário e os utiliza para atualizar tanto as variáveis de instância correspondentes quanto os 
        valores armazenados no dicionário `params_intrinsc_values`. Caso algum valor inserido seja inválido, um erro é 
        exibido e a atualização não ocorre para o campo com o erro.

        Passos realizados:
        -------------------
        1. Itera sobre os campos de entrada (QLineEdit) presentes em `self.params_intrinsc_line_edits`.
        2. Para cada campo, obtém o texto inserido, converte para `float` e atualiza a variável de instância correspondente
        usando `setattr`.
        3. Exibe uma mensagem de sucesso utilizando `QMessageBox` informando que os parâmetros foram atualizados com sucesso.
        4. Em seguida, o método percorre novamente os campos de entrada, atualizando os valores no dicionário `params_intrinsc_values`
        e chama uma função de ação (`params_intrinsc_action`) para processar as atualizações.
        5. Se algum valor inserido for inválido (não puder ser convertido para número), exibe um erro no console.

        Variáveis envolvidas:
        ----------------------
        - `self.params_intrinsc_line_edits`: Dicionário que contém os campos de entrada para os parâmetros intrínsecos da câmera.
        - `self.params_intrinsc_values`: Dicionário que armazena os valores atualizados dos parâmetros intrínsecos da câmera.
        - `self`: O objeto de instância, cujas variáveis correspondentes aos parâmetros intrínsecos são atualizadas.
        """
        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: update_params_intrinsc")

        for label, line_edit in self.params_intrinsc_line_edits.items():
            text = line_edit.text()
            setattr(self, label.replace(':', ''), float(text))
        QMessageBox.information(self, "Atualizacao bem-sucedida", "Parametros atualizados com sucesso!")

        self.log("Atualizando parametros intrinsecos...")
        for key, params_intrinsc_line_edit in self.params_intrinsc_line_edits.items():
            text = params_intrinsc_line_edit.text()
            if text:  
                try:
                    self.params_intrinsc_values[key] = float(text)

                    self.params_intrinsc_action(key, self.params_intrinsc_values[key])

                except ValueError:
                    print(f"Erro ao converter {key} {text}")
        self.log("Parametros intrinsecos atualizados com sucesso.")
        self.log("Saindo da funcao update_params_intrinsc")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
    
    def params_intrinsc_action(self, key, value):
        """
        Executa ações específicas com base no campo `key` e no valor atualizado.

        Este método realiza a atualização dos valores intrínsecos da câmera armazenados no dicionário `params_intrinsc_values` 
        de acordo com o parâmetro `key` fornecido. Dependendo do valor de `key`, o método atualiza o respectivo parâmetro 
        intrínseco (como o número de pixels, a distância focal, ou as dimensões do sensor). Após a atualização, o método 
        chama as funções `projection_2d()` e `update_canvas()` para atualizar a projeção 2D e os gráficos na interface.

        Passos realizados:
        -------------------
        1. Verifica o valor de `key` para determinar qual parâmetro intrínseco deve ser atualizado.
        2. Atualiza o valor correspondente no dicionário `self.params_intrinsc_values`.
        3. Após atualizar o valor, chama a função `projection_2d()` para recalcular a projeção 2D com base no novo valor.
        4. Em seguida, chama a função `update_canvas()` para atualizar os gráficos ou a interface com as novas configurações.

        Parâmetros:
        -----------
        - `key` (str): A chave que identifica qual parâmetro intrínseco deve ser atualizado. Pode ser um dos seguintes:
            - "n_pixels_base:"
            - "n_pixels_altura:"
            - "ccd_x:"
            - "ccd_y:"
            - "dist_focal:"
            - "s_theta:"
        - `value` (float): O novo valor que será atribuído ao parâmetro identificado pela chave `key`.

        Variáveis envolvidas:
        ----------------------
        - `self.params_intrinsc_values`: Dicionário que armazena os valores dos parâmetros intrínsecos da câmera.
        - `self.projection_2d`: Função chamada para recalcular a projeção 2D após a atualização dos parâmetros.
        - `self.update_canvas`: Função chamada para atualizar os gráficos ou visualizações na interface com os novos parâmetros.

        """


        self.log("-----------------------------------------")
        self.log("FUNCAO CHAMADA: params_intrinsc_action")
        self.log("Atualizando parametros intrinsecos..")
        self.log(f"Campo: {key} | Valor: {value}")   

        if "n_pixels_base:" in key:
            self.params_intrinsc_values['n_pixels_base:'] = value
        elif "n_pixels_altura:" in key:
            self.params_intrinsc_values['n_pixels_altura:'] = value
        elif "ccd_x:" in key:
            self.params_intrinsc_values['ccd_x:'] = value
        elif "ccd_y:" in key:
            self.params_intrinsc_values['ccd_y:'] = value
        elif "dist_focal:" in key:
            self.params_intrinsc_values['dist_focal:'] = value
        elif "s_theta:" in key:
            self.params_intrinsc_values['s_theta:'] = value

        self.projection_2d()
        self.update_canvas()       
        self.log("Saindo da funcao params_intrinsc_action")
        self.log("-----------------------------------------")
        self.log("-----------------------------------------")
