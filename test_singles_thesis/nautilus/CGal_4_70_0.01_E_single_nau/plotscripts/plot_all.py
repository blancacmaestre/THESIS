########################################################################
#### This script simply calls all other python scripts for plotting ####
########################################################################
import os 

scriptdir = '/home/user/THESIS/test_singles_thesis/nautilus/CGal_4_70_0.01_E_single_nau/plotscripts/' 
cmd = '' 

for f in os.listdir(scriptdir): 
	if '.py' in f and f!='plot_all.py': 
		cmd += 'python "%s/%s" & '%(scriptdir,f) 

os.system(cmd[:-2]) 
