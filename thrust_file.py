import math
import numpy as np
import inputs

m_dot_fs = [0.048] * 6

def calc_M(measurement_matrix):
    M_array = []
    for row in measurement_matrix:
        M = row[4]/math.sqrt(inputs.gamma*inputs.R*row[9])
        M_array.append(M)
    return M_array

def calc_deltaT(measurement_matrix):
    deltaT_array = []
    for row in measurement_matrix:
        T_ISA = inputs.T_0 + (row[3]*inputs.a_layer)
        T_delta = T_ISA -row[9]
        deltaT_array.append(T_delta)
    return deltaT_array


thrust_matrix = np.transpose(np.array([inputs.measurement_matrix[:,3], calc_M(inputs.measurement_matrix), calc_deltaT(inputs.measurement_matrix), inputs.measurement_matrix[:,6], inputs.measurement_matrix[:,7] ]))
thrust_matrix_nominal = np.transpose(np.array([inputs.measurement_matrix[:,3], calc_M(inputs.measurement_matrix), calc_deltaT(inputs.measurement_matrix), m_dot_fs, m_dot_fs ]))

thrust_matrix_real = np.transpose(np.array([inputs.measurement_matrix_real[:,3], calc_M(inputs.measurement_matrix_real), calc_deltaT(inputs.measurement_matrix_real), inputs.measurement_matrix_real[:,6], inputs.measurement_matrix_real[:,7] ]))
thrust_matrix_real_nominal =np.transpose(np.array([inputs.measurement_matrix_real[:,3], calc_M(inputs.measurement_matrix_real), calc_deltaT(inputs.measurement_matrix_real), m_dot_fs, m_dot_fs ]))

thrust_input = np.savetxt("matlab.DAT", thrust_matrix_nominal, fmt="%.6f", delimiter=" ")
