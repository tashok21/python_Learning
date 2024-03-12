from scipy.optimize import fsolve  
from scipy.optimize import leastsq  
from scipy import optimize 
import matplotlib.pyplot as plt  
import numpy as np 
import pandas as pd   

def opt_r(r_value,ide_value,phi_value,area,temp,src_v,meas_i):
    est_v = np.zeros_like(src_v) # an array to hold the diode voltages
    diode_i = np.zeros_like(src_v) # an array to hold the diode currents
    prev_v = VDD_STEP # an initial guess for the voltage

    # need to compute the reverse bias saturation current for this phi!
    is_value = area * temp * temp * np.exp(-phi_value * Q / ( KB * temp ) )
    for index in range(len(src_v)):
        prev_v =fsolve(diode_voltage,prev_v,(src_v[index],r_value,ide_value,temp,is_value),xtol=1e-12)[0]
        est_v[index] = prev_v # store for error analysis
# compute the diode current
    diode_i = diode_current(est_v,ide_value,temp,is_value)
    return meas_i - diode_i

# Constants required for calculation
VDD_STEP=0.1
n_constant = 1.7  # Ideality factor
R_constant = 11e3  # Resistor value in series with diode
temp = 350  # Temperature coefficient: Problem 1
temp2 = 375  # Temperature coefficient: Problem 2
ISat_constant = 1e-9  # Saturation current of the diode
Q= 1.6021766208e-19
KB=  1.380648e-23
Is=0


Vs_init = np.arange(0.1, 2.5, 0.1)  # voltage range of 0.1 V to 2.5 V with step size of 0.1(given)
step_size = (2.5 - 0.1) / 0.1
V = [1 for i in range(int(step_size + 1))]


def diode_voltage(Vd, V, R, Is, n, temp):
    Err = (Vd / R) - (V / R) + diode_current(Vd, Is, n, temp)
    return Err

def diode_current(Vd, Is, n, temp):
    return Is * (np.exp((Vd * Q) / (n * KB * temp)) - 1) 
# to find the voltage across the diode that gives the least error
diode_v = fsolve(diode_voltage, V, args=(Vs_init, R_constant, ISat_constant, n_constant, temp))
diode_c = diode_current(diode_v, ISat_constant, n_constant, temp)

# plot

plt.title("Voltage-Current  Characteristics")
plt.ylabel("Diode current")
plt.xlabel("Voltage")

plt.plot(Vs_init, np.log10(diode_c),label="Source Voltage")  # Plot between the source voltage and diode current
plt.plot(diode_v, np.log10(diode_c),label="Diode Voltage")  # Plot between diode voltage and diode current
plt.legend()  # to include the legends in the plot
plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------
n = 1.5  # Ideality factor of the diode
R = 10000  # Resistance in series with the diode
phi = 0.8  # Barrier height for the diode
A = 1e-8  
Res=1e-15
meas_i=0

def opt_barr(phi,n,R,A,temp,src_v,meas_i):
    est_v = np.zeros_like(src_v) # an array to hold the diode voltages
    diode_i = np.zeros_like(src_v) # an array to hold the diode currents
    prev_v = VDD_STEP # an initial guess for the voltage

    # need to compute the reverse bias saturation current for this phi!
    is_value = A * temp * temp * np.exp(-phi * Q / ( KB * temp ) )
    for index in range(len(src_v)):
        prev_v = fsolve(diode_voltage,prev_v,(src_v[index],R,n,temp,is_value),xtol=1e-12)[0]
        est_v[index] = prev_v # store for error analysis
# compute the diode current
    diode_i = diode_current(est_v,n,temp,is_value)
    return (meas_i - diode_i)/(meas_i+diode_i+1e-15)

def opt_id(n,phi,R,A,temp,src_v,meas_i):
    
    est_v = np.zeros_like(src_v) # an array to hold the diode voltages
    diode_i = np.zeros_like(src_v) # an array to hold the diode currents
    prev_v = VDD_STEP # an initial guess for the voltage
    
    # need to compute the reverse bias saturation current for this phi!
    is_value = A * temp * temp * np.exp(-phi * Q / ( KB * temp) )
    for index in range(len(src_v)):
        prev_v = fsolve(diode_voltage,prev_v,(src_v[index],R,n,temp,is_value),xtol=1e-12)[0]
        est_v[index] = prev_v # store for error analysis
    diode_i = diode_current(est_v,n,temp,is_value)
    return (meas_i - diode_i)/(meas_i+diode_i+1e-15)


#Read the diode file
f = pd.read_csv('DiodeIV.txt',sep=" ", header=None)
src_v = f.iloc[1:, 0].values  
diode_im = f.iloc[1:, 1].values  
count= 100 
j = 0
while j < count:
    r_opt = optimize.leastsq(opt_r, R, args=(n, phi, A, temp2, src_v, diode_im))
    R = r_opt[0][0]   

    b_opt = optimize.leastsq(opt_barr, phi, args=(n, R, A, temp2, src_v,diode_im))
    phi = b_opt[0][0] 
    
    
    i_opt = optimize.leastsq(opt_id, n, args=(R,phi, A, temp2, src_v, diode_im))
    n = i_opt[0][0]  

    residual = opt_id(n, R, phi, A, temp2, src_v, diode_im)
    error = np.mean(np.abs(residual)) 
    if error < 1e-9:   
        break
    print("Count %s : " % (j))
    print("Resistor : %f " % (R))
    print("Ideality : %f " % (n))
    print("Phi barr  : %f " % (phi))
    print("Mean : %f " % (error))
    j+=1

print("\nThe optimized value for resistance is : %.2f " % R)  
print("The optimized value for barrier height is : %.2f  " % phi)  
print("The optimized value for ideality is : %.2f  " % n)  
   
diode_m= []
for V in src_v:
    rem = A * temp2 * temp2 * np.exp(-phi * Q / (KB* temp2))  
    root = fsolve(diode_voltage, VDD_STEP, args=(V, R, n, temp2,rem), xtol=1e-12)  
    volt = root[0]
    meas_i = diode_current(volt, n, temp2, rem)
    diode_m.append(meas_i)        

# Plot
plt.xlabel("Source voltage ")
plt.ylabel("Diode current")
plt.title("Diode current vs Source voltage")

# Plot of source voltage and actual diode current
plt.plot(src_v, np.log10(diode_im), label="Actual")

# Plot of source voltage and predicted diode current
plt.plot(src_v, np.log10(diode_m),label="Predicted")
plt.legend()
plt.show()
             
