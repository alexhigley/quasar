
################################################################################################
#											alex_compare 				        		       #
#	Program to find quasars with a dicernable difference in z values between VI and Pipline.   #
#	Alex's first real program 																   #	
################################################################################################



file=input('file_name: ')
print('comparing from file: ',file)

import numpy as np 
from astropy.io import fits

qr = fits.open('file_name')[1].data #creating array of fits file data
wq = np.where(qr['CLASS_PERSON']=='QSO')[0]
wwq = qr[wq]

wp = np.array(wwq['Z_PIPE']) #creating array of pipeline redshifts
wv = np.array(wwq['Z_VI']) #creating array of visually inspected redshift

dif = np.absolute(wp-wv) #finding difference between wp and wv

qsos = np.any(dif >= 0.1) #defined any significant differance as anything greater than or equal to 0.1
if np.any(dif >= 0.1): #in 'file_name', does any of the data agree with qsos? if yes:
	nqsos = np.where(dif >= 0.1)[0] #making array of all diff data greater than or equal to 0.1
	x=(qr['PLATE'][nqsos]) #finding Plate-MJD-FiberID values for nqsos. IS THERE A WAY TO COMBINE X, Y, & Z so it appears in the order of Plate-MJD-FiberID?
	y=(qr['MJD'][nqsos])
	z=(qr['FIBERID'][nqsos])

	startart='#'*45 #decoration
	boxart=' '*9
	lineart='-'*70

	print('\n') #cover
	print(startart)
	print("#{0}Alex's First Real Program{0}#".format(boxart))
	print(startart)
	print('\n')
	print(lineart)

	print('ADDRESS:') #address, which line nqsos is in, not starting at 0.
	print(nqsos+1) 
	print(lineart)

	print('HOW MANY?') #how many values in nqsos
	print(len(nqsos))
	print(lineart)

	print('PLATE-MJD-FIBERID:') #printing Plate-MJD-FiberIDs of all in nqsos, still want better way to do this.
	print('\n')
	print('Plate:',x)
	print('MJD:',y)
	print('FiberID:',z)

else: #if no diff values greater than or equal to 0.1:
	lineart='-'*70 #decoration
	print('\n')
	print(lineart)
	print('		~Damn Computers Taking Our Jobs~')
	print(lineart)
print('\n')

