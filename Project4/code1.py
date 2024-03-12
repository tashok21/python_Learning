import subprocess       # Module to run applications 

import shutil           # Copies source to destination

import numpy as np      # To perform math operations

main_file = "InvChain_main.sp"

netlist = "InvChain.sp"


# Using the copy function logic, transferring from source to destination file
def netlist_c(e,r):

   shutil.copy(main_file, netlist)       # Transfers to destination file

   hspice_f = open(netlist, "a")

   var = ord('a')                                            # Conversion of ASCII

   hspice_f.write("\n" ".param fan = " + str(r) + "\n")

   for q in range(1, e + 1):



        line = "Xinv" + str(q) + " " + chr(var) + " "

        if q == e:

             line += "z inv M="  # Next Value Find

        else:

            var += 1         #Updating the ASCII Value

            line += chr(var) + " inv M="

        if q == 1:

             line += "1\n"

        else:

             line += ((q - 2) * "fan*") + "fan\n"
        hspice_f.write( line)

        hspice_f.write(".end")

   hspice_f.close()



# Function to calculate delay values for fans and inverters

def delay_of_inverter():

    INVERT = 0         #inverter initialization

    FAN_Varia = 0         # Fan initialization

    inverters_sweep = range(1, 15, 2)   # Inverter Value Sweep from 1 to 15 by steps of 2

    fans = range(2, 12)  # Fan Value Sweep

    tphl_value = 10 # considering the tphl value as 10 initially 

    for no_of_inverters in inverters_sweep:

        for no_of_fan in fans:

            netlist_c(no_of_inverters, no_of_fan)

            proce = subprocess.Popen(["hspice", "InvChain.sp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            output, err = proce.communicate()  # Output Read

            value_dat = np.recfromcsv("InvChain.mt0.csv", comments="$", skip_header=3) # tphl values

            tphl = value_dat["tphl_inv"]   # getting the tphl

            print("N :", no_of_inverters,",", "F :", no_of_fan,",", "tphl = ", tphl,"ps")



            if tphl<tphl_value:       # Delay Updation
               tphl_value = tphl

               INVERT = no_of_inverters      #Inverte Updation

               FAN_Varia  = no_of_fan      #Fan Updation

    return  INVERT, FAN_Varia , tphl_value



INVERT, FAN_Varia , tphl_value = delay_of_inverter()

print("The minimum delay obtained is %s ps for N = %s and Fan = %s" % (tphl_value, INVERT, FAN_Varia))   # Min Delay   

print("Inverter Count is : " ,INVERT)

print("Fan Count is : " , FAN_Varia )