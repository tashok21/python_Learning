################################################################################
#                           EEE-591 Project 3                                  #          
#                             Saradeep Manam                                   #
#                               1225662945                                     #
################################################################################

################################################################################
# Including the necessary libraries                                            #
################################################################################
from scipy.optimize import fsolve  
from scipy.optimize import leastsq  
from scipy import optimize 
import matplotlib.pyplot as plt  
import numpy as np 
import pandas as pd  

################################################################################
# This function does the optimization for the resistor                         #
# Inputs:                                                                      #
#    r_value   - value of the resistor                                         #
#    ide_value - value of the ideality                                         #
#    phi_value - value of phi                                                  #
#    area      - area of the diode                                             #
#    temp      - temperature                                                   #
#    src_v     - source voltage                                                #
#    meas_i    - measured current                                              #
# Outputs:                                                                     #
#    err_array - array of error measurements                                   #
################################################################################
def opt_r(init_resis, init_ideality, init_phi_val, A, temp, v_src, i):
    est_volt= np.zeros_like(v_src)  
    diode_curr = np.zeros_like(v_src)  
    previ_vl = Initial_voltage  
    bias_value = A * temp * temp * np.exp(-init_phi_val * Charge / (Kb * temp)) 
    for k in range(len(v_src)):
        previ_vl = fsolve(diode_voltage, previ_vl, (v_src[k], init_resis, init_ideality, temp, bias_value), xtol=1e-12)[0] 
        est_volt[k] = previ_vl  # Error Analysis
    diode_curr = diode_current(est_volt, init_ideality, temp, bias_value)  # Diode Current
    return i - diode_curr

################################################################################
# Function to calculate error for diode voltage                                #           
################################################################################
def diode_voltage(diode_volt, volt, r, p, temperature, i): 
    diode_curent = diode_current(diode_volt, p, temperature, i) 
    error = (diode_volt - volt) / r + diode_curent  
    return error

################################################################################
# Function to calculate the diode current
################################################################################
def diode_current(Vd, n, Temp, i):   # function for calculating diode current
    Vt = n * Kb * Temp / Charge
    return i * (np.exp(Vd / Vt) - 1)

################################################################################
# The code for the 1st problem                                                 #
################################################################################
Is = 1e-9
N = 1.7
R = 110000
temp = 350
Charge = 1.6021766208e-19
Kb =  1.380648e-23
i = 0
Initial_voltage = 0.1
Final_voltage = 2.5
VS = np.arange (Initial_voltage , ( Final_voltage + 0.1 ) , 0.1 )

diode_V = []
diode_I = []
while ( i < len(VS) ):
    V = VS[i]
    root = fsolve(diode_voltage, Initial_voltage, args=(V, R, N, temp, Is), xtol=1e-12) #funtion call
    Initial_volt = root[0]
    diode_V.append(root[0])  #appending the diode voltage
    i = i+1
for i in diode_V:
    I = diode_current(i, N, temp, Is)
    diode_I.append(I)

plt.title("Voltage-Current  Characteristics")              # Title of plot
plt.plot(VS, diode_I, label="Diode Current VS source Voltage")   # Passing the Voltages and currents to plot the graph
plt.plot(diode_V, diode_I, label="Diode Current VS Diode voltage")
plt.xlabel("Voltage")                           # X axis label
plt.ylabel("Diode current")               # Y axis label
plt.yscale('log')
plt.legend()
plt.grid()
plt.show()


################################################################################
# Variable setup for the second problem                                        #
################################################################################
initial_ideality = 1.5  
initial_phi = 0.8  
initial_resistance = 10000  
A = 1e-8  
temperature = 375  

################################################################################
# Function for optimization of barrier height                                  #
################################################################################
def op_barr(initial_phi, initial_ideality, initial_resistance, A, temp, v_src, i):
    est_volt = np.zeros_like(v_src)  
    diode_curr = np.zeros_like(v_src)  
    previ_vl = Initial_voltage  
    bias_value = A * temp * temp * np.exp(-initial_phi * Charge / (Kb * temp))  
    for k in range(len(v_src)):
        previ_vl = fsolve(diode_voltage, previ_vl, (v_src[k], initial_resistance, initial_ideality, temp, bias_value), xtol=1e-12)[0]
        est_volt[k] = previ_vl
    diode_curr = diode_current(est_volt, initial_ideality, temp, bias_value)  
    return (i - diode_curr) / (i + diode_curr + 1e-15)

################################################################################
# Function for optimization of ideality value                                  #
################################################################################
def opt_id(initial_ideality, initial_resistance, initial_phi, A, temp, v_src, i):
    est_volt = np.zeros_like(v_src)  
    diode_curr = np.zeros_like(v_src)  
    previ_vl = Initial_voltage
    bias_value = A * temp * temp * np.exp(-initial_phi * Charge / (Kb * temp)) 
    for k in range(len(v_src)):
        previ_vl = fsolve(diode_voltage, previ_vl, (v_src[k], initial_resistance, initial_ideality, temp, bias_value), xtol=1e-12)[0]  
        est_volt[k] = previ_vl  
    diode_curr = diode_current(est_volt, initial_ideality, temp, bias_value)  
    return (i - diode_curr) / (i + diode_curr + 1e-15)

################################################################################
# Main function for the second problem                                         #
################################################################################
diode_dt = pd.read_csv('DiodeIV.txt', sep=" ", header=None)
v_src = diode_dt.iloc[1:, 0].values  
diode_cur = diode_dt.iloc[1:, 1].values  
iterations = 100 
j = 0
while j < iterations:
    resis_val_opt = optimize.leastsq(opt_r, initial_resistance, args=(initial_ideality, initial_phi, A, temperature, v_src, diode_cur))
    initial_resistance = resis_val_opt[0][0]   
    barrier_val_opt = optimize.leastsq(op_barr, initial_phi, args=(initial_ideality, initial_resistance, A, temperature, v_src, diode_cur))
    initial_phi = barrier_val_opt[0][0] 
    ideal_val_opt = optimize.leastsq(opt_id, initial_ideality, args=(initial_resistance, initial_phi, A, temperature, v_src, diode_cur))
    initial_ideality = ideal_val_opt[0][0]  
    res = opt_id(initial_ideality, initial_resistance, initial_phi, A, temperature, v_src, diode_cur)
    error = np.mean(np.abs(res)) 
    if error < 1e-9:   
        break
    print(">>  Iteration Number %s : " % (j))
    print("    Resistor value  : %f " % (initial_resistance))
    print("    Ideality value  : %f " % (initial_ideality))
    print("    Phi barr value : %f " % (initial_phi))
    print("    Mean error : %f " % (error))
    j += 1
print("\nThe final optimized value of the resistance is : %.2f Ohms " % initial_resistance)  
print("The final optimized value of the barrier height is : %.2f  " % initial_phi)  
print("The final optimized value of the ideality is : %.2f  " % initial_ideality)  
diode_curr2 = []
for V in v_src:
    current = A * temperature * temperature * np.exp(-initial_phi * Charge / (Kb * temperature))  
    root = fsolve(diode_voltage, Initial_voltage, args=(V, initial_resistance, initial_ideality, temperature, current), xtol=1e-12)  
    Intial_volt = root[0]
    i = diode_current(Intial_volt, initial_ideality, temperature, current)
    diode_curr2.append(i)                     
plt.title("Diode current vs Source voltage")  
plt.plot(v_src, diode_cur, linewidth=7, label=" Identified Diode current") 
plt.plot(v_src, diode_curr2, linewidth=4, linestyle='--', label="Calculated Diode current ") 
plt.xlabel("Source voltage") 
plt.ylabel("Diode current (log)") 
plt.yscale('log') 
plt.legend() 
plt.grid() 
plt.show() 

