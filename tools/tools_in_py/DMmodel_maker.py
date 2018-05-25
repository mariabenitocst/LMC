
#This program is to produce '.xml' models for different dark matter masses and final states (particles).

import gammalib
import math
import numpy as np

#PATHS

LMC_PATH = "/home/queenmab/GitHub/LMC"
DATA_PATH = "/home/queenmab/DATA/"
PATH_SPEC=LMC_PATH+'/spectra/DM/' #Path where the spectra (filefunctions) are stored.
PATH_MODELS=LMC_PATH+'/models/'  #Path to store the models created (.xml)

#Open model file
models = gammalib.GModels(PATH_MODELS+"example_model.xml") #Open an example model file to modify. Its a diffuse source where the spatial part is a counts cube (J Factor fits file) and the spectral part is a FileFunction. 

particle = 'Mu' #Final state particle (W, b, Mu...)

#Masses of dark matter particle in TeV
masses = [0.100,0.200,0.300,0.400,0.500,0.600,0.800,1,4,5,8,10,40,50,80,100] 
#masses = [0.300,0.400,0.600,0.700,0.800,0.900,2,3,4,5,6,7,8,9,10]

jfactorname = "DM/jfactor/jfactorLMC.fits"

for mass in masses:
    #Standarized name for the produced model so the other programs can use it easily:
    #_______________________________________________________________________________
    if mass < 1:
        masstr = str(int(mass*1000))+'GeV'
    else:
        masstr = str(mass)+'TeV'
    specname = 'flux'+particle+masstr+'.txt'
    modelname = 'dm_LMC_'+particle+masstr
    #_______________________________________________________________________________

    for model in models:
        model.spectral().filename(PATH_SPEC+specname) #Put the spectrum for the specific mass in the model file

    models.save(PATH_MODELS+modelname+'.xml') #Save the model
