import numpy as np
from ..base import antenna_structures
import open3d as o3d

def antenna_stats(freq, x, y, z):
    """
    Utility for evaluating electrical size

    Parameters
    ----------
    freq : float
        frequency of the antenna in Hz
    x : float
        largest dimension in x, or half width in x direction (m)
    y : float
        largest dimension in y, or half width in y direction (m)
    z : float
        largest dimension in z, or half width in z direction (m)

    Returns
    -------

    """
    wavelength = 3e8 / freq
    k = (2 * np.pi) / wavelength
    a = np.sqrt((x) ** 2 + (y) ** 2 + (z) ** 2) * 0.5

    print("ka={:1.5f}".format(k * a))
    print("Radius in Wavelengths={:1.5f}".format(a / wavelength))

def antenna_size(freq,antenna_structure):
    """
    Utility for calculating the electrical size of a given antenna structure

    Parameters
    ----------
    freq : float
        frequency of the antenna in Hz
    antenna_structure :
        antenna structure

    Returns
    -------
    ka : float
        electrical size of antenna structure for given frequency
    """
    total_points=antenna_structure.export_all_points()
    max_points=total_points.get_max_bound()
    min_points = total_points.get_min_bound()
    x=max_points[0]+np.abs(min_points[0])
    y = max_points[1] + np.abs(min_points[1])
    z = max_points[2] + np.abs(min_points[2])
    wavelength = 3e8 / freq
    k = (2 * np.pi) / wavelength
    ka = np.sqrt((x) ** 2 + (y) ** 2 + (z) ** 2) * 0.5
    return ka

