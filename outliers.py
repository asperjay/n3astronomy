from astropy.io import fits
import csv
import numpy as np

outliers = [201691, 1462946, 202382, 202840, 1269256, 1269223, 203024, 1269195, 1269097, 594828]

small = 2.9
big = 3
print(len(outliers))
# Open the FITS file
with fits.open('COSMOS2020_CLASSIC_R1_v2.2_p3.fits') as hdul:
    data = hdul[1].data

    all_lp_mass_med = []
    for outlier in outliers:
        if data['lp_zBEST'][outlier] < big and data['lp_zBEST'][outlier] > small:
            all_lp_mass_med.append(data['lp_mass_med'][outlier])
    all_lp_mass_med.sort()
    print(sum(all_lp_mass_med)/len(all_lp_mass_med))
    all_lp_mass_med = []
    totalList = []
    for massmed in range(len(data['lp_zBEST'])):
        if data['lp_zBEST'][massmed] < big and data['lp_zBEST'][massmed] > small:
            if massmed not in outliers:
                totalList.append(data['lp_mass_med'][massmed])
    print(sum(totalList)/len(totalList))


    all_lp_mass_med = []
    for outlier in outliers:
        if data['lp_zBEST'][outlier] < big and data['lp_zBEST'][outlier] > small:
            all_lp_mass_med.append(data['lp_SFR_med'][outlier])
    all_lp_mass_med.sort()
    print(sum(all_lp_mass_med)/len(all_lp_mass_med))
    all_lp_mass_med = []
    totalList = []
    for massmed in range(len(data['lp_zBEST'])):
        if data['lp_zBEST'][massmed] < big and data['lp_zBEST'][massmed] > small:
            if massmed not in outliers:
                totalList.append(data['lp_SFR_med'][massmed])
    print(sum(totalList)/len(totalList))


    all_lp_mass_med = []
    for outlier in outliers:
        if data['lp_zBEST'][outlier] < big and data['lp_zBEST'][outlier] > small:
            all_lp_mass_med.append(data['lp_sSFR_med'][outlier])
    all_lp_mass_med.sort()
    print(sum(all_lp_mass_med)/len(all_lp_mass_med))
    all_lp_mass_med = []
    totalList = []
    for massmed in range(len(data['lp_zBEST'])):
        if data['lp_zBEST'][massmed] < big and data['lp_zBEST'][massmed] > small:
            if massmed not in outliers:
                totalList.append(data['lp_sSFR_med'][massmed])
    print(sum(totalList)/len(totalList))
