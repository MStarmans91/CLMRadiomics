# CLMRadiomicsFeatures
Script to compute the features used in the paper "A multi-observer radiomics method for distinguishing pure histopathological growth patterns of colorectal liver metastases on CT: a pilot study.", M.P.A. Starmans, F. E. Buisman et al.

## Installation
For the feature extraction, only the PREDICT package, version 2.1.3,
and the subsequent dependencies are required, which can be installed through pip:

    pip install "PREDICT==2.1.3"

For the model optimization, additionally WORC, version 2.1.3, is required:

    pip install "WORC==2.1.3"

## Usage: Feature Extraction
The ExtractFeatures.py script can be used to extract all features. We provided
you with the exact same configuration file that was used in the study. The
script can be easily modified to use your own data instead of the
provided example data and requires:

1. An image in ITK Image format, e.g. .nii, .nii.gz, .tiff, .nrrd, .raw
2. A segmentation in ITK Image format.
3. Optionally, metadata in DCM format

Extracting the features from the example data should take less than 10 seconds.
Using a larger image and/or mask may result in a longer computation time.

## Usage: Model Optimization
The ModelOptimization.py script can be used for the model optimization. Againg, 
we provided you with the exact same configuration file that was used in the study. 
The script can be easily modified to use your own data instead of the
provided example data and requires: see for more details the script itself.

Note that the script performs a dummy experiment: it supplies 10x the example
features to WORC, which will result in non-separable dataset, and thus no
sensible model. Usage of your own data is therefore highly recommended.

## Known Issues

### Pyradiomics
The PyRadiomics package we use requires numpy in the installation, hence
you may need to install numpy manually beforehand:

    pip install "numpy==1.6.4"

From version 2.2.0 and above, PyRadiomics removed a function and might throw
this error:

'''AttributeError: 'module' object has no attribute "RadiomicsFeaturesExtractor"'''

This can be overcome by downgrading to version 2.1.2:

    pip install "pyradiomics==2.1.2"

### Missingpy
Missingpy verion 0.2.0 may throw an ascii error: in that case, manually
remove and reinstall the package:

    pip uninstall missingpy
    pip install "missingpy==0.2.0"
