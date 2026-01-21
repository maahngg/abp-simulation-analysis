from simulation_ABP import generate_dynamic_abp
import pandas as pd
import numpy as np
import os

data = generate_dynamic_abp(particles=3, velocity=1.0, rotational_D=0.5, translational_D=0.1)

x = data['x']
y = data['y']
phi = data['phi']
parameters = data['parameters']

col_ids = np.repeat(np.arange(parameters['num_particles']), parameters['steps'])
col_time = np.tile(data['time'], parameters['num_particles'])

df = pd.DataFrame({
    'particle_id': col_ids,
    'time': col_time,
    'pos_x': x.flatten(order='F'),
    'pos_y': y.flatten(order='F'),
    'phi': phi.flatten(order='F')
})

name_archive = f'ABP-p{parameters['num_particles']}_v{parameters['v0']}_Dr{parameters['Dr']}_Dt{parameters['Dt']}_dt{parameters['dt']}_steps{parameters['steps']}'

file_path = os.path.join(r'Data', f'{name_archive}.csv')

df.to_csv(file_path, index=False, float_format='%.6f')