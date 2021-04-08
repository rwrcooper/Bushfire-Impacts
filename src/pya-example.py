from scipy.stats import uniform
import sklearn
import numpy as np

import pyapprox as pya
import pyapprox_interface as pyi

from pyapprox.models.wrappers import evaluate_1darray_function_on_2d_array


def example_function(x):
    a = x[0]
    b = x[1]
    output = a+b
    return output  # np.array([output])


def fun(sample):
    assert sample.ndim==1
    return np.sum(sample**2)


def target_function(x):
    output = evaluate_1darray_function_on_2d_array(example_function, x)
    return output


# Define model interface
pyam = pyi.PyaModel(target_model=target_function,
                    variables=[uniform(-1, 2), uniform(-1, 2)]
                    )


# Build emulator by:
# 1. Specifying the emulation approach to use
# 2. Building the emulator, using default options (admissibility=None)
#    (adaptive approaches do not require samples to be taken beforehand)
emulator = (pyam.define_pce(approach=pya.AdaptiveInducedPCE,
                            transform_approach=pya.AffineRandomVariableTransformation)
                .build())

# Get Sobol sensitivity indicators
emulator.sensitivities()

# Plot emulated performance
emulator.sample_validation(1500)
X = emulator.validation_samples
y = emulator.target_model(X)
y_hat = emulator.model(X)


__import__('IPython').embed()


pyi.plot_fit(y, y_hat,
             metric=sklearn.metrics.mean_squared_error,
             metric_name="RMSE",
             squared=False)
