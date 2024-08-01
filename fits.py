from astropy.io import fits
import csv

outliers = [1464623,1270774,1463827,1463319,202709,203039,1462759,203220,1270128,694250]


# Open the FITS file
with fits.open('COSMOS2020_CLASSIC_R1_v2.2_p3.fits') as hdul:
    data = hdul[1].data

    subset = []
    indexData = []
    for i in range(len(data['lp_zBEST'])):
        if data['lp_zBEST'][i] != 'nan':
            if data['lp_zBEST'][i] < 0.25 and data['lp_zBEST'][i] > 0.2:
                subset.append([i,
                               data['ez_restU'][i]-data['ez_restB'][i],
                               data['ez_restB'][i]-data['ez_restV'][i],
                               data['ez_restV'][i]-data['ez_restJ'][i]])
with open('subset_indexed.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing the data
    writer.writerows(subset)
