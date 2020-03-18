import numpy as np

<<<<<<< HEAD
# Aircraft Parameters

S = 30 # m^2
b = 15.911
c_bar = 2.0569
AR = b*b/S

#Standard Parameters

W_s = 60500 #N
g_0 = 9.80665 # m/s^2
lbs = 0.45359 #kg
inc = 0.0254 #m

# Atmosphere Parameters

R = 287.0
R_sp = 287.058 #J/kgK
=======
# Atmosphere Parameters
p_0 = 101325 # Pa
>>>>>>> 74260b684284eeaf340d8f7c7b328dcc2e3720ed
a_layer = -0.0065 # K/m

p_0 = 101325 # Pa
T_0 = 288.15 # K
rho_0 = p_0/(R_sp*T_0)
gamma = 1.4

<<<<<<< HEAD
w_fuel     = 2640*lbs*g_0
w_fuel_ref = 4050*lbs*g_0

w_oew = 9165.0*lbs*g_0
=======
# Aircraft Parameters
S = 30 # m^2
b = 15.911
c_bar = 2.0569
AR = b*b/S
OEW = 9165.0 * 0.453592 * g_0
>>>>>>> 74260b684284eeaf340d8f7c7b328dcc2e3720ed

# Matrices for the flight data
# nr, time, ET, altitude, IAS, alpha, FFl, FFr, Fused, TAT
measurement_matrix_real = np.array([[3,1682, 0, 18020, 222, 2.0, 608, 668, 634, -4.8],[4,1800, 0, 17990, 200, 2.9, 508, 548, 665, -6.8],[5,1890, 0, 18000, 182, 3.6, 453, 488, 688, -8.2],[1,1358, 0, 18000, 161, 5.0, 392, 450, 538, -9.5],[2,1520, 0, 17990, 131, 8.1, 369, 378, 569, -11.5],[6,2115, 0, 18010, 114, 10.7, 431, 480, 729, -12.8] ])
trim_matrix_real = np.array([[3, 2640, 0, 18940, 134, 7.5, -1.2, 2.5, -31, 404, 455, 865, -13.5], [2, 2520, 0, 18360, 147, 6.3, -0.7, 2.5, -14, 407, 466, 840, -11.5], [1, 2400, 0, 18060, 156, 5.2, -0.3, 2.5, 1, 409, 470, 811, -10.2], [7, 2940, 0, 18360, 156, 5.2, -0.2, 2.5, 1, 480, 469, 940, -11.2], [4, 2700, 0, 18350, 168, 4.4, 0.1, 2.5, 26, 410, 471, 888, -10.5], [5, 2760, 0, 18090, 176, 3.8, 0.4, 2.5, 50, 416, 448, 901, -9.5], [6, 2820, 0, 17680, 186, 3.3, 0.7, 2.5, 83, 420, 484, 912, -7.8]])
W_passenger_real = (95 +102 +89 +82 +66 +81 +69 +85 +96) * 0.453592 * g_0
W_blockfuel_real = 2640 * 0.453592 * g_0
W0_real = OEW + W_passenger_real + W_blockfuel_real
W_matrix_real = W0_real - measurement_matrix_real[:,8]
measurement_matrix_real = np.c_[np.array(measurement_matrix_real),np.array(W_matrix_real)] #appends weight at each point to measurement matrix

# Reference data
# nr, time, ET, altitude, IAS, alpha, de, detr, Fe, FFl, FFr, Fused, TAT
trim_matrix = np.array([[1, 2239, 0, 6060, 161, 5.3, 0, 2.8, 0, 462, 486, 664, 5.5], [2, 2351, 0, 6350, 150, 6.3, -0.4, 2.8, -23, 458, 482, 694, 4.5], [3, 2484, 0, 6550, 140, 7.3, -0.9, 2.8, -29, 454, 477, 730, 3.5], [4, 2576, 0, 6880, 130, 8.5, -1.5, 2.8, -46, 449, 473, 755, 2.5], [5, 2741, 0, 6160, 173, 4.5, 0.4, 2.8, 26, 465, 489, 798, 5.0], [6, 2840, 0, 5810, 179, 4.1, 0.6, 2.8, 40, 472, 496, 825, 6.2], [7, 2920, 0, 5310, 192, 3.4, 1.0, 2.8, 83, 482, 505, 846, 8.2]])
# nr, time, ET, altitude, IAS, alpha, FFl, FFr, Fused, TAT
measurement_matrix = np.array([[1,30, 2000, 5010, 249, 1.7, 798, 813, 360, 12.5],[2,2137, 2000, 5020, 221, 2.4, 633, 682, 412, 10.5],[3,2436, 2000, 5020, 192, 3.6, 561, 579, 447, 8.8],[4,2604, 2000, 5030, 163, 5.4, 463, 484, 478, 7.2],[5,2947, 2000, 5020, 130, 8.7, 443, 467, 532, 6],[6,3200, 2000, 5110, 118, 10.6, 474, 499, 570, 5.2] ])
W_passenger = (95 +92 +74 +66 +61 +75 +78 +86 +68) * 0.453592 * g_0
W_blockfuel = 4050 * 0.453592 * g_0
W0 = OEW + W_passenger + W_blockfuel
W_matrix = W0 - measurement_matrix[:,8]
measurement_matrix = np.c_[np.array(measurement_matrix),np.array(W_matrix)] #appends weight at each point to measurement matrix


# Adjustments of the measurement matrices to correct units
def convert(mat: np.ndarray):
    mat = np.column_stack((mat[:,0:3],mat[:,3]*0.3048,mat[:,4]*0.514444,mat[:,5:-4],mat[:,-4:-2]*(0.453592/3600),mat[:,-2]*0.453592,mat[:,-1]+273.15))
    return mat

measurement_matrix = convert(measurement_matrix)
measurement_matrix_real = convert(measurement_matrix_real)
trim_matrix = convert(trim_matrix)
trim_matrix_real = convert(trim_matrix_real)

'''
for row in measurement_matrix:
    row[3] = row[3] * 0.3048
    row[4] = row[4] * 0.514444
    row[6] = row[6] * (0.453592/3600)
    row[7] = row[7] * (0.453592/3600)
    row[8] = row[8] * 0.453592
    row[9] = row[9] + 273.15

for row in measurement_matrix_real:
    row[3] = row[3] * 0.3048
    row[4] = row[4] * 0.514444
    row[6] = row[6] * (0.453592/3600)
    row[7] = row[7] * (0.453592/3600)
    row[8] = row[8] * 0.453592
    row[9] = row[9] + 273.15

for row in trim_matrix:
    row[3] = row[3] * 0.3048
    row[4] = row[4] * 0.514444
    row[9] = row[9] * (0.453592/3600)
    row[10] = row[10] * (0.453592/3600)
    row[11] = row[11] * 0.453592
    row[12] = row[12] + 273.15

for row in trim_matrix_real:
    row[3] = row[3] * 0.3048
    row[4] = row[4] * 0.514444
    row[9] = row[9] * (0.453592/3600)
    row[10] = row[10] * (0.453592/3600)
    row[11] = row[11] * 0.453592
    row[12] = row[12] + 273.15
<<<<<<< HEAD
'''
=======
>>>>>>> 74260b684284eeaf340d8f7c7b328dcc2e3720ed
