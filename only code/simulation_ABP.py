import numpy as np

def generate_dynamic_abp(*, particles: int, velocity: float,
                      rotational_D: float, translational_D: float, total_time: float = 50., step_dt: float = 0.001) -> dict:

    """
    Simula o comportamento de partículas Brownianas Ativas, de maneira simples, utilizando Euler-Maruyama
    
    :param particles: quantidade de partículas
    :type particles: int
    :param velocity: velocidade de propulsão da partícula
    :type velocity: float
    :param rotational_D: Coeficiente de difusão rotacional
    :type rotational_D: float
    :param translational_D: Coeficiente de difusão translacional
    :type translational_D: float
    :param total_time: tempo total da simulação em unidades do total_steps * step_dt
    :type total_time: float
    :param step_dt: passo de tempo (intervalo de tempo entre as execuções)
    :type step_dt: float
    :return: retorna o dicionário com posições e ângulo de polarização, array de tempo de execução e os parâmetros como outro dicionário. 
    :rtype: dict
    """

    total_steps = int(total_time / step_dt)

    x = np.zeros((total_steps, particles))
    y = np.zeros((total_steps, particles))
    phi = np.zeros((total_steps, particles))
    
    time_array = np.arange(total_steps) * step_dt

    phi[0] = np.random.uniform(0, 2 * np.pi, particles)

    sqrt_trans = np.sqrt(2 * translational_D * step_dt)
    sqrt_rot = np.sqrt(2 * rotational_D * step_dt)

    for t in range(total_steps - 1):
        noise_phi = np.random.normal(0, sqrt_rot, particles)
        noise_x = np.random.normal(0, sqrt_trans, particles)
        noise_y = np.random.normal(0, sqrt_trans, particles)

        phi[t + 1] = phi[t] + noise_phi
        x[t + 1] = x[t] + (velocity * np.cos(phi[t]) * step_dt) + noise_x
        y[t + 1] = y[t] + (velocity * np.sin(phi[t]) * step_dt) + noise_y

    simulation_data = {
        "x": x, "y": y, "phi": phi,
        "time": time_array,
        "parameters": {
            "v0": velocity,
            "Dr": rotational_D,
            "Dt": translational_D,
            "dt": step_dt,
            "num_particles": particles,
            "steps": total_steps
        }
    }

    return simulation_data