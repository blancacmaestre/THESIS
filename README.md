FIRST OF ALL:
I do not have pyBBarolo in the git so I copied my version
All of this code is working with my version of pyBbarolo so I think you have to initialise that one

## Files and Directories

### pyBB_simulate_galaxies.py

This script is used to create models of galaxies. 
You need pyBbarolo to run this.

The opuput is a folder of the name of the galaxy saved in "models" that contains:
-  the cube in a fits file
- ring file with the parametars 
- text file where all the inputs used are listed
- There is also a folder called slices with the pv slices.

### test_BBB.ipynb

This is the main file to run the bayesian Bbarolo. The outputs are in the folder you choose. 
You need pyBbarolo to run this.

The output folder contains:
- the corner plot
- file called "parameters" that include the imput and output plots 
- mask used for the fitting (in a fits)
- error file
- Folder called slices containing the PV slices
- Folder called barbamodel containing the ring file, fits file and density profile of the new model 

### Tools.py

This script contains functions to slice the PVs and to get the channels from the velocity and vice versa. This is called in test_BBB.ipynb and in plot_PV

### Mega_loop Files

These files are used to run multiple tests simultaneously, allowing for overnight execution. They serve as the base for `run_long_test.py` and will be compiled into a simpler code soon. 

### Plot_PV 

My attempt at the PV plots. They are stored in the folder pv_plot.

### Plot_results_inc  

Just to plot the results of some tests (the iclination plot is here).

### Files Not in Use

- **BBB_parallel.py**: An attempt by Enrico to parallelize the code, but it is not currently in use.
- **Cannubi.p**: Cannubi code from Filippo.
- **Mock_gal_params.ipynb**: Notes on the different parameters.

## How to Use

### Creating Models

To create models, use the `pyBB_simulate_galaxies.py` script. You can choose different parameters for the galaxy and the cube itself.

I have a bunch of commented parameters from other tests.

### Running BBB

This code is divided in a bunch of sections.
--> First you need the fits file and ring file of the mock you want to run, and then you have to choose the output file.
--> You can also choose your sampler between nautilus and Dynesty (Nautilus is waaaaaa faster) since they have different outputs in the main code (bayesian.py in pyBbarolo.py)

#### Fitting

here you have to set the bounds, the radii and how many parameters, because you can calculate tem by ring or as single values

#### Model of resulting parameters

here i took the characteristics of the imput cube, and the parameters outputed by BBB and created another mock galaxy (which is essentially teh resulting one) 

#### Outputs

In outputs I just plot all the different graphs, there are a couple of if statements so that it does not have to be changed at all independently of the options. Also I create the PV slices of the model

#### Errors

Here I calculate the errors as Enrico did it with Dynesty and I believe I correctly made them for Nautilus,I use  the percentiles to do this.
Then they are stored in a file

The last part is just plotting the parameters.
