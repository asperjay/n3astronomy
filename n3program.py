from astropy.io import fits
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerPathCollection
np.random.seed(1)
import csv

def update_legend_marker_size(handle, orig):
    "Customize size of the legend marker"
    handle.update_from(orig)
    handle.set_sizes([20])

data = []
with open('subset.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        if len(row) == 4:
            data.append([float(i) for i in row])

clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(data)
X_scores = clf.negative_outlier_factor_

sorted_indices = np.argsort(np.array(X_scores))[:10]
for i in sorted_indices:
    print(data[i][0])


dataArray = np.array(data)[:, 1:]

plt.scatter(dataArray[:,0], dataArray[:,1], color="k", s=3.0, label="Data points")
# plot circles with radius proportional to the outlier scores
radius = (X_scores.max() - X_scores) / (X_scores.max() - X_scores.min())
scatter = plt.scatter(
    dataArray[:,0],
    dataArray[:,1],
    s=1000 * radius,
    edgecolors="r",
    facecolors="none",
    label="Outlier scores",
)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
#plt.xlabel("prediction errors: %d" % (n_errors))
plt.legend(
    handler_map={scatter: HandlerPathCollection(update_func=update_legend_marker_size)}
)
plt.title("Local Outlier Factor (LOF)")
plt.show()
