#!/usr/bin/env python3
"""
File: template.py
Author: riley cooper
Email: rwr.cooper@gmail.com
Description:
    PyApprox simple linear model example.

Usage:
    template.py 
                    

Options:

    -h, --help
    --option=<n>
"""

import docopt
import sklearn
from scipy import stats
import matplotlib as plt


from pyapprox.approximate import adaptive_approximate_sparse_grid
import pyapprox_interface as pyi


def linear_model(a, b, c):
    """An example target model"""
    return a + b + c


def wrapped_model(X):
    """PyApprox expects models to handle a single input array."""
    return linear_model(*X)


def main():

    nvars = 3
    emulated = (pyi.PyaModel(target_model=wrapped_model,
                            variables=[stats.uniform()] * nvars)
                .define_approx(approach=adaptive_approximate_sparse_grid)
                .sample_training(300)
                .build()
                )

    x = emulated.sample_validation(600).validation_samples
    y = emulated.target_model(x)
    y_hat = emulated.model(x)
    
    pyi.plot_fit(y, y_hat, 
                metric=sklearn.metrics.mean_squared_error,
                metric_name="RMSE",
                squared=False)
    

    # Display sensitivity information
    print(emulated.sensitivities())
        
    return


if __name__ == '__main__':

    main()

