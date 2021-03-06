# Copyright (c) 2020 Paddle Quantum Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
HGenerator
"""

from numpy import array, kron

__all__ = ["H_generator"]


def H_generator():
    """
    Generate a Hamiltonian with trivial descriptions
    Returns: A Hamiltonian

    """
    sigma_I = array([[1, 0], [0, 1]])
    sigma_X = array([[0, 1], [1, 0]])
    sigma_Y = array([[0, -1j], [1j, 0]])
    sigma_Z = array([[1, 0], [0, -1]])
    H = 0.4 * kron(sigma_Z, sigma_I) + 0.4 * kron(
        sigma_I, sigma_Z) + 0.2 * kron(sigma_X, sigma_X)
    # H = numpy.diag([0.1, 0.2, 0.3, 0.4])
    return H.astype('complex64')
