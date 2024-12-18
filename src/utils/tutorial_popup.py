from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

def TutorialPopup():
    # Criando a janela do popup
    popup = QDialog()
    popup.setWindowTitle("Tutorial")
    popup.resize(600, 400)  # Aumente o tamanho inicial da janela aqui (largura x altura)

    # Texto explicativo
    tutorial_text = (
        "<h1 style='text-align: center;'>Bem-vindo ao Sistema de Projeção 3D</h1>"
        "<p>Este programa permite visualizar e manipular uma malha STL em 3D, ajustando parâmetros da câmera e do mundo. "
        "Veja como cada seção funciona:</p>"
        "<h2>❗ Avisos</h2>"
        "<ul>"
        "<li><b>LOG:</b> Exibirá um log no terminal sobre o estado deste sistema e alterações enquanto estiver ativo.</li>"
        "<li><b>Fechar tutorial (em caso de não escolha):</b> será carregada a malha de urso </li>"
        "<li><b>Alteração nos parâmetros (update ou reset):</b> exibirá um popup.</li>"
        "<li><b>Parâmetros intrísecos fora do limite permitido:</b> exibirá  um popup.</li>"
        "<li><b>Limites: </b></li>"
        "<ol>"
        "<li><b>Distância Focal:</b> (min: 1, max: 1000)</li>"
        "<li><b>Foco (dist_focal):</b> (min: 1, max: 1000)</li>"
        "<li><b>Centro da imagem (ccd_x,ccd_y):</b> (min: 10, max: 50)</li>"
        "<li><b>Coeficientes de escala (n_pixels_base):</b> (min: 640, max: 1920)</li>"
        "<li><b>Coeficientes de escala (n_pixels_altura):</b> (min: 480, max: 1080)</li>"
        "<li><b>Ângulo s0 (s_theta):</b> (min: -1000, max: 1000)</li>"
        "</ol>"
        "</ul>"
        "<h2>⚙️ Parâmetros Disponíveis</h2>"
        "<ul>"
        "<li><b> Transformações do Mundo:</b> Alterações no posicionamento e rotação do objeto 3D no espaço.</li>"
        "<li><b> Transformações da Câmera:</b> Ajustes de posição e orientação da câmera em relação ao objeto.</li>"
        "<li><b> Parâmetros Intrínsecos:</b> Configurações da câmera, como distância focal, dimensões do sensor e resolução.</li>"
        "</ul>"
        "<h2>📊 Interface Principal</h2>"
        "<ol>"
        "<li><b>Visualização:</b> Gráficos 3D e projeções 2D da malha STL.</li>"
        "<li><b>Campos de Entrada:</b> Ajuste dos parâmetros intrínsecos, do mundo e da câmera.</li>"
        "<li><b>Botões Interativos:</b> Aplicação de alterações e visualização dos resultados em tempo real.</li>"
        "</ol>"
        "<h2>🔍 Explore e Experimente</h2>"
        "<p>Altere os parâmetros na interface principal e observe os efeitos nos gráficos em tempo real. "
        "Experimente diferentes configurações para entender como cada parâmetro afeta a projeção 3D.</p>"
        "<h2>✔️ Escolha a malha a ser renderizada</h2>"
        "<p>Selecione abaixo a malha que deseja visualizar e manipular. Cada opção representa um modelo 3D diferente. Experimente renderizar diferentes objetos para entender as funcionalidades do programa:</p>"
        
    )

    # Layout principal
    layout = QVBoxLayout()
    popup.setWindowTitle("Github: Dsbrito ~ Movimento de Corpo Rígido e Projeção Perspectiva")
    popup.setWindowIcon(QIcon('./assets/img/icon.png'))
    # Adicionando um QLabel com texto formatado
    tutorial_label = QLabel(tutorial_text)
    tutorial_label.setWordWrap(True)  # Quebra de linha automática
    tutorial_label.setTextFormat(Qt.TextFormat.RichText)  # Permite HTML no texto
    layout.addWidget(tutorial_label)

    # Botões de escolha de mesh
    mesh_buttons_layout = QHBoxLayout()

    # Caminhos para as meshes
    meshes = {
        "Urso": ('./assets/stl/urso.STL', "🐻"),
        "Mario": ('./assets/stl/mario.STL', "🧑‍🎮"),
        "Link Zelda": ('./assets/stl/link_zelda.STL', "🛡️"),
        "Megaman": ('./assets/stl/megaman.STL', "🤖"),
        "Donkey Kong": ('./assets/stl/donkey_kong.STL', "🦍")
    }

    # Variável para armazenar a escolha do usuário
    chosen_mesh = {"path": None}

    # Função para definir a mesh escolhida e fechar o popup
    def choose_mesh(mesh_path):
        chosen_mesh["path"] = mesh_path
        popup.accept()

    # Criar um botão com ícone para cada mesh
    for mesh_name, (mesh_path, icon) in meshes.items():
        button = QPushButton(f"{icon} {mesh_name}")
        button.clicked.connect(lambda _, path=mesh_path: choose_mesh(path))
        mesh_buttons_layout.addWidget(button)

    # Adicionar espaçamento abaixo dos botões
    spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    mesh_buttons_layout.addSpacerItem(spacer)

    layout.addLayout(mesh_buttons_layout)

    # Define o layout na janela
    popup.setLayout(layout)

    # Exibe o popup e espera o usuário escolher
    popup.exec_()

    # Retorna a mesh escolhida
    return chosen_mesh["path"]
