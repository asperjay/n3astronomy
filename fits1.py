from astropy.io import fits
import csv


def write_subset_data(small, big):
    with fits.open('COSMOS2020_CLASSIC_R1_v2.2_p3.fits') as hdul:
        data = hdul[1].data

        subset = []
        indexData = []
        for i in range(len(data['lp_zBEST'])):
            if data['lp_zBEST'][i] != 'nan':
                if data['lp_zBEST'][i] < big and data['lp_zBEST'][i] > small:
                    subset.append([i,
                                   data['ez_restU'][i]-data['ez_restB'][i],
                                   data['ez_restB'][i]-data['ez_restV'][i],
                                   data['ez_restV'][i]-data['ez_restJ'][i]])
    with open('subset_indexed.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(subset)

