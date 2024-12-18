from stl import mesh
import numpy as np

def load_stl(filepath):
    """
    Carrega um arquivo STL e retorna os dados necessários para plotagem.

    Parâmetros:
        filepath (str): Caminho para o arquivo STL.

    Retorna:
        urso (numpy.ndarray): Coordenadas homogêneas (x, y, z, 1).
        urso_vectors (numpy.ndarray): Vetores dos triângulos que compõem o objeto.
    """
    # Carrega o arquivo STL
    your_mesh = mesh.Mesh.from_file(filepath)

    # Obtém as coordenadas x, y, z
    x = your_mesh.x.flatten()
    y = your_mesh.y.flatten()
    z = your_mesh.z.flatten()

    # Obtém os vetores dos triângulos
    urso_vectors = your_mesh.vectors

    # Cria as coordenadas homogêneas
    urso = np.array([x.T, y.T, z.T, np.ones(x.size)])

    return urso, urso_vectors
