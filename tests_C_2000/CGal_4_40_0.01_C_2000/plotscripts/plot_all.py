########################################################################
#### This script simply calls all other python scripts for plotting ####
########################################################################
import os 

scriptdir = '/home/user/THESIS/tests_C_2000/CGal_4_40_0.01_C_2000/plotscripts/' 
cmd = '' 

for f in os.listdir(scriptdir): 
	if '.py' in f and f!='plot_all.py': 
		cmd += 'python "%s/%s" & '%(scriptdir,f) 

os.system(cmd[:-2]) 
