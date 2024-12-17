"""
Use our linear and cubic fits to predict where the point corresponding to 
hanging a 1.5kg weight would lie. Modify the code so that it produces the plot 
that uses the model to make a prediction.
"""


import numpy as np
import matplotlib.pyplot as plt


# Extracting the data from a file

def get_data(input_file):
    with open(input_file, "r") as data_file:
        distances = []
        masses = []
        data_file.readline() # ignore header
        for line in data_file:
            d, m = line.split(",")
            distances.append(float(d))
            masses.append(float(m))
    return (masses, distances)

    
# Fitting a curve to data

def fit_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances)
    forces = np.array(masses) * 9.81
    plt.plot(forces, distances, "ko", 
             label = "Measured displacements")
    plt.title("Measured Displacement of Spring")
    plt.xlabel("|Force| (Newtons)")
    plt.ylabel("Distance (meters)")
    forces_extr = np.append(forces, [1.5 * 9.81])
    # find linear fit
    a, b = np.polyfit(forces, distances, 1)
    predicted_distances_linear = a * np.array(forces) + b
    k = 1.0 / a # see explanation in text
    linear_model = np.poly1d(np.polyfit(forces, distances, 1))
    predicted_distance_linear = linear_model(1.5 * 9.81)
    predicted_distances_linear = np.append(predicted_distances_linear, [predicted_distance_linear])
    plt.plot(forces_extr, predicted_distances_linear, 
             label = f"Linear fit, k = {k:.4f}")
    # find cubic fit
    fit = np.polyfit(forces, distances, 3)
    # a, b, c, d = np.polyfit(forces, distances, 3)
    predicted_distances_cubic = np.polyval(fit, forces)
    # predicted_distances = a * (forces**3) + b * forces**2 + c * forces + d
    cubic_model = np.poly1d(np.polyfit(forces, distances, 3))
    predicted_distance_cubic = cubic_model(1.5 * 9.81)
    predicted_distances_cubic = np.append(predicted_distances_cubic, [predicted_distance_cubic])
    plt.plot(forces_extr, predicted_distances_cubic, "k:", label = "cubic fit")
    plt.legend(loc = "best")
    plt.show()
    
fit_data("springData.csv")