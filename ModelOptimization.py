import WORC
import os
import glob


def editconfig(config):
    # Some specific configuration alterations
    config['Normalize']['ROI'] = 'False'  # No Normalization for CT

    config['ImageFeatures']['image_type'] = 'CT'
    config['ImageFeatures']['vessel_radius'] = '0'  # tumors can be really small

    config['Labels']['label_names'] = 'GP'
    config['Labels']['modus'] = 'singlelabel'

    return config


# Inputs
name = 'WORC_CLM_GP'
current_path = os.path.dirname(os.path.abspath(__file__))
label_file = os.path.join(current_path, 'ExampleData', 'pinfo_CLM.txt')
semantics_file = os.path.join(current_path, 'ExampleData', 'sem_CLM.txt')
config = os.path.join(current_path, 'ExampleData', 'config_modeloptimization.ini')

# Altough you can also supply the raw image, we will supply the extracted
# features directly
feature_files = glob.glob(os.path.join(current_path, 'ExampleData', 'ExampleFeaturesCLMRadiomics*.hdf5'))
feature_files.sort()

# As we only have a single feature file, we will repeat it to mimick
# having multiple. We do this in a dictionary, in which the keys
# correspond to the "patient" names also used in the label and semantics files
patient_names = ['CLMRadiomics-' + str(i).zfill(3) for i in range(0, 10)]
features = {k: v for k, v in zip(patient_names, feature_files)}

# Create the WORC network
network = WORC.WORC(name)

# Instead of supplying the .ini file to the network, we will create
# the config object for you directly from WORC,
# so you can interact with it if you want.
# Altough it is a configparser object, it works similar as a dictionary
config = network.defaultconfig()

# The default config from the WORC 2.1.3 version we used, was a stripped
# version in order to get a quick result. The actual default used for normal
# experiments is created through the editconfig function.
config = editconfig(config)

# NOTE: Since we now only use 10 "patients" in this example, we change one setting
# Do not do this for the full experiment.
config['SampleProcessing']['SMOTE_neighbors'] = '1, 1'

# Append the sources to be used
network.features_train.append(features)
network.labels_train.append(label_file)
network.semantics_train.append(semantics_file)
network.configs.append(config)

# Build, set, and execture the network
network.build()
network.set()
network.execute()
