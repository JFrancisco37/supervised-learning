import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    # raise NotImplementedError  # substituir pelo seu codigo
    x = data[:, 0]
    y = data[:, 1]
    h = w*x+b

    mse = np.mean((h-y)**2)

    return mse


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    # raise NotImplementedError  # substituir pelo seu codigo
    x = data[:, 0]
    y = data[:, 1]
    h = w*x+b
    
    b_prime = b - alpha*np.mean(2*(h-y))
    w_prime = w - alpha*np.mean(2*x*(h-y))
    
    return b_prime, w_prime


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    # raise NotImplementedError  # substituir pelo seu codigo

    b_list = [b]
    w_list = [w]

    for _ in range(num_iterations):
        b, w = step_gradient(b, w, data, alpha)
        b_list.append(b)
        w_list.append(w)

    return b_list, w_list
