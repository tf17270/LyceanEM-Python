import pytest
import numpy as np
import open3d as o3d
from numpy.testing import assert_equal, assert_allclose
from scipy.spatial.transform import Rotation as R
from ..base_classes import antenna_structures,structures,points

def cube():
    # a cube centered at the origin, with side lengths of 1m (default)
    cube = o3d.geometry.TriangleMesh.create_box()
    cube.translate(np.array([-0.5,-0.5,-0.5]))
    return cube

def point():
    #a single point on the +x center of the cube with consistent normal vector
    source_point=o3d.geometry.PointCloud()
    source_point.points=o3d.utility.Vector3dVector(np.array([0.5,0,0]))
    source_point.normals=o3d.utility.Vector3dVector(np.array([1, 0, 0]))
    return source_point

def antenna():
    base = structures([cube()])
    source_point = points([point()])
    antenna = antenna_structures()
    return antenna

@pytest.fixture
def standard_antenna():
    return antenna()

def test_excitation_function_x(standard_antenna):
    #test that an unrotated antenna with u (horizontal-y) polarisation gives horizontal-y polarisation
    desired_E_vector=np.array([0,1,0],dtype=np.complex64)
    assert_allclose(standard_antenna.excitation_function(desired_E_vector=desired_E_vector),desired_E_vector,atol=1e-12)

def test_excitation_function_x_y(standard_antenna):
    #test that a rotated antenna (about z, rotating x to y direction with u (horizontal-y) polarisation gives horizontal-x polarisation
    desired_E_vector=np.array([0,1,0],dtype=np.complex64)
    final_vector=np.array([1,0,0],dtype=np.complex64)
    standard_antenna.
    assert_allclose(standard_antenna.excitation_function(desired_E_vector=desired_E_vector),final_vector,atol=1e-12)

