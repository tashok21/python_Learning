import numpy as np
import subprocess
import shutil

file = "InvChain_main.sp"
netlist = "InvChain.sp"
def netlist_c(inv_c,fan_c):
   shutil.copy(file, netlist)
   hspice_f = open(netlist, "a")
   var = ord('a')
   hspice_f.write("\n" ".param fan = " + str(fan_c) + "\n")
   for i in range(1, inv_c+ 1):
        line = "Xinv" + str(i) + " " + chr(var) + " "
        if i == inv_c:
             line += "z inv M=" 
        else:
            var += 1         
            line += chr(var) + " inv M="
        if i == 1:
             line += "1\n"
        else:
             line += ((i - 2) * "fan*") + "fan\n"
        hspice_f.write( line)
        hspice_f.write(".end")
   hspice_f.close()

# Function to calculate delay values 
def delay_of_inverter():
    INV= 0
    fan = 0
    inverters_sweep = range(1, 15, 2)
    fans = range(2, 12)
    config= 10
    for no_of_inverters in inverters_sweep:
        for no_of_fan in fans:
            netlist_c(no_of_inverters, no_of_fan)
            proce = subprocess.Popen(["hspice", "InvChain.sp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = proce.communicate()
            value_dat = np.recfromcsv("InvChain.mt0.csv", comments="$", skip_header=3)
            config_values = value_dat["tphl_inv"]
            print("N :", no_of_inverters,",", "F :", no_of_fan,",", "config= ", config_values)
            if config_values<config:       # Delay Updation
               config = config_values
               INV = no_of_inverters
               fan = no_of_fan
    return  INV, fan , config

INV, fan , config = delay_of_inverter()
print("Minimum delay %s  N = %s and F = %s" % (config, INV, fan))   # Min Delay   
print("Inverter Count : " ,INV)
print("Fan Count: " , fan )