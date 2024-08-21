from fits1 import write_subset_data
from outliers import print_data_for_outliers
from n3program import find_outliers

outlierBounds = [(0.2,0.25),(0.97,1),(2.9,3)]
for outlierBound in outlierBounds:
    (small,big) = outlierBound
    print(small,big)
    write_subset_data(small, big)
    outlierData = data_for_outliers(small, big, find_outliers())
    
