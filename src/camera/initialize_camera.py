import numpy as np

from src.utils.transformations import move, x_rotation





def initialize_camera():
    """
    Inicializa a câmera com rotação e translação aplicadas.

    Returns:
        dict: Configurações iniciais da câmera.
    """
    # Define os vetores base
    e1 = np.array([[1], [0], [0], [0]])  # X
    e2 = np.array([[0], [1], [0], [0]])  # Y
    e3 = np.array([[0], [0], [1], [0]])  # Z
    base = np.hstack((e1, e2, e3))

    # Define o ponto de referência
    point = np.array([[0], [0], [0], [1]])

    # Configura a câmera inicial
    cam = np.hstack((base, point))
    zero_cam = cam.copy()

    # Aplica rotação de -90 graus no eixo X
    angle=-90
    x_90 = x_rotation(angle)

    # Aplica translação (dx=0, dy=-60, dz=35)
    T = move(0, -60, 35)

    # Atualiza a câmera com as transformações
    cam = np.dot(x_90, cam)
    cam = np.dot(T, cam)

    # Configurações de exibição
    config = {
        "cam": cam,
        "zero_cam": zero_cam,
        "a": 100,
        "w": 100,
        "largura": 900,
        "altura": 600,
        "title": "Trabalho 1",
        "e1": e1,
        "e2": e2,
        "e3": e3,
        "base": base,
        "point": point,
        "x_90": x_90,
        "T": T,
    }
    return config

    # camera_config = initialize_camera()
    #     self.e1 = camera_config['e1']
    #     self.e2 = camera_config['e2']
    #     self.e3 = camera_config['e3']
    #     self.Rx  = camera_config['x_90']
    #     self.T = camera_config['T']
    #     self.base = camera_config['base']
    #     self.cam = camera_config['cam']
    #     self.zero_cam = self.cam
    #     self.a = camera_config['a']
    #     self.w = camera_config['w']
    #     self.largura = camera_config['largura']
    #     self.altura = camera_config['altura']
    #     self.title = camera_config['title']