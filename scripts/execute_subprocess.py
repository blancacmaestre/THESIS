import subprocess
import numpy as np

# EXECUTABLE LISTS:
# PARAMETER BOUNDS:
#vrots = [[0, 30], [0, 30], [0, 30], [0, 30], [0, 30], [0, 30], [0, 350], [0, 350], [0, 350], [0, 350], [0, 350], [0, 350], [0, 500], [0, 500], [0, 500], [0, 500], [0, 500], [0, 500]]
#vdisps = [[1, 30], [1, 30], [1, 30], [1, 30], [1, 30], [1, 30], [1, 40], [1, 40], [1, 40], [1, 40], [1, 40], [1, 40], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100]]

#phis = [[-20, 20], [-20, 20], [-20, 20], [-20, 20], [-20, 20], [-20, 20], [-20, 60], [-20, 60], [-20, 60], [-20, 60], [-20, 60], [-20, 60], [-40, 120], [-40, 120], [-40, 120], [-40, 120], [-40, 120], [-40, 120]]
#denss = [[0, 20], [0, 20], [0, 20], [0, 20], [0, 20], [0, 20], [1, 60], [1, 60], [1, 60], [1, 60], [1, 60], [1, 60], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100]]

#freepar = [['vrot', 'vdisp', 'inc_single', 'phi_single'], ['vrot', 'vdisp', 'dens', 'inc_single', 'phi_single']]
#fittings = [freepar[0], freepar[0], freepar[0], freepar[0], freepar[0]]
#fittings = [freepar[0]]


""" masks = ["SEARCH", "SEARCH", "SEARCH","SEARCH","SEARCH"]
models = ["CGal_6_70_0.01_E_nau","CGal_5_70_0.01_E_nau", "CGal_4_70_0.01_E_nau", "CGal_3_70_0.01_E_nau", "CGal_2_70_0.01_E_nau"]
beamsizes = [40,48,60,80,120]
halfbeams = [20,24,30,40,60]
centres =  [38.5,32,25.5,19,12.5]

fitsnames = [ "/home/user/THESIS/MODELS_THESIS/RESO/CGal_6_70_0.01/CGal_6_70_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/RESO/CGal_5_70_0.01/CGal_5_70_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/RESO/CGal_4_70_0.01/CGal_4_70_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/RESO/CGal_3_70_0.01/CGal_3_70_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/RESO/CGal_2_70_0.01/CGal_2_70_0.01.fits"]
truths =[[100,100,100,100,100,100,10,10,10,10,10,10,70,30],[100,100,100,100,100,10,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,10,10,10,70,30],[100,100,10,10,70,30]] 
 """


""" masks = ["SEARCH", "SEARCH", "SEARCH","SEARCH","SEARCH", "SEARCH", "SEARCH", "SEARCH"]  
models = ["CGal_4_20_0.01_C_nau","CGal_4_30_0.01_C_nau", "CGal_4_40_0.01_C_nau", "CGal_4_50_0.01_C_nau", "CGal_4_60_0.01_C_nau", "CGal_4_70_0.01_C_nau", "CGal_4_80_0.01_C_nau", "CGal_4_85_0.01_C_nau"] 
beamsizes = np.full(len(models),60)  
halfbeams = np.full(len(models),30)
centres = np.full(len(models),25.5)
fitsnames = [ "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_20_0.01/CGal_4_20_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_30_0.01/CGal_4_30_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_40_0.01/CGal_4_40_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_50_0.01/CGal_4_50_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_60_0.01/CGal_4_60_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_70_0.01/CGal_4_70_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_80_0.01/CGal_4_80_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/INC/CGal_4_85_0.01/CGal_4_85_0.01.fits"]
incs = [20,30,40,50,60,70,80,85]
truths =[[100,100,100,100,10,10,10,10,20,30],[100,100,100,100,10,10,10,10,30,30],[100,100,100,100,10,10,10,10,40,30],[100,100,100,100,10,10,10,10,50,30],[100,100,100,100,10,10,10,10,60,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,80,30],[100,100,100,100,10,10,10,10,85,30]]
 """
 
""" masks = ["SEARCH", "SEARCH", "SEARCH","SEARCH","SEARCH", "SEARCH"]
models = ["CGal_4_70_0.001_E_nau","CGal_4_70_0.005_E_nau", "CGal_4_70_0.01_E_nau", "CGal_4_70_0.03_E_nau", "CGal_4_70_0.05_E_nau", "CGal_4_70_0.1_E_nau"] 
beamsizes = np.full(len(models),60)  
halfbeams = np.full(len(models),30)
centres = np.full(len(models),25.5)
fitsnames = [ "/home/user/THESIS/MODELS_THESIS/NOISE/CGal_4_70_0.001/CGal_4_70_0.001.fits",\
              "/home/user/THESIS/MODELS_THESIS/NOISE/CGal_4_70_0.005/CGal_4_70_0.005.fits",\
              "/home/user/THESIS/MODELS_THESIS/NOISE/CGal_4_70_0.01/CGal_4_70_0.01.fits",\
              "/home/user/THESIS/MODELS_THESIS/NOISE/CGal_4_70_0.03/CGal_4_70_0.03.fits",\
              "/home/user/THESIS/MODELS_THESIS/NOISE/CGal_4_70_0.05/CGal_4_70_0.05.fits",\
              "/home/user/THESIS/MODELS_THESIS/NOISE/CGal_4_70_0.1/CGal_4_70_0.1.fits"]  
truths =[[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30]]
 """

masks = ["SEARCH", "SEARCH", "SEARCH","SEARCH","SEARCH", "SEARCH"]
models = ["CGal_4_70_0.01_1_E_nau","CGal_4_70_0.01_10_E_nau", "CGal_4_70_0.01_20_E_nau", "CGal_4_70_0.01_30_E_nau", "CGal_4_70_0.01_50_E_nau"] 
beamsizes = np.full(len(models),60)  
halfbeams = np.full(len(models),30)
centres = np.full(len(models),25.5)
fitsnames = [ "/home/user/THESIS/MODELS_THESIS/THICK/CGal_4_70_0.01_1/CGal_4_70_0.01_1.fits",\
              "/home/user/THESIS/MODELS_THESIS/THICK/CGal_4_70_0.01_10/CGal_4_70_0.01_10.fits",\
              "/home/user/THESIS/MODELS_THESIS/THICK/CGal_4_70_0.01_20/CGal_4_70_0.01_20.fits",\
              "/home/user/THESIS/MODELS_THESIS/THICK/CGal_4_70_0.01_30/CGal_4_70_0.01_30.fits",\
              "/home/user/THESIS/MODELS_THESIS/THICK/CGal_4_70_0.01_50/CGal_4_70_0.01_50.fits"]
thicks = [1,10,20,30,50]  
truths =[[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30],[100,100,100,100,10,10,10,10,70,30]]

# Ensure all lists have the same length
assert """ len(vrots) == len(vdisps) == len(incs) == len(phis) == len(denss) ==  len(fittings) == """ 

len(masks) == len(models) == len(fitsnames) == len(beamsizes) == len(centres) == len(halfbeams) == len(truths) == len(thicks), "All parameter lists must have the same length"

# Loop through the parameters and execute BBB_template
for i in range(len(models)):
    #vrot = vrots[i]
    #vdisp = vdisps[i]
    #inc = incs[i]
    #phi = phis[i]
    #dens = denss[i]
    #fitting = fittings[i]
    mask = masks[i]
    model = models[i]
    fitsname = fitsnames[i]
    beamsize = beamsizes[i]
    centre = centres[i]
    halfbeam = halfbeams[i]
    truth = truths[i]
    thick = thicks[i]

    print(f"Running BBB_template with  mask: {mask}, model: {model}, beamsize: {beamsize}, fitsname: {fitsname}, centre: {centre}, halfbeam: {halfbeam}, truth: {truth} thick: {thick}") #vrot: {vrot}, vdisp: {vdisp}, inc: {inc}, phi: {phi}, dens: {dens}, fitting: {fitting},
    subprocess.run(['python', '/home/user/THESIS/scripts/BBB_test_subprocess.py', '--mask', mask, '--model', model,  '--beamsize', str(beamsize),  '--fitsname', fitsname, '--centre', str(centre),  '--halfbeam', str(halfbeam) , '--truth', str(truth), '--thick', str(thick)])# '--fitting', ','.join(fitting),