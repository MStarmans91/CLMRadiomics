import WORC
import os
import glob


def editconfig(config):
    config['General']['Segmentix'] = 'True'

    config['PREDICTGeneral']['Joblib_ncores'] = '1'
    config['PREDICTGeneral']['Joblib_backend'] = 'threading'

    config['Normalize']['ROI'] = 'False'  # No Normalization for CT

    config['ImageFeatures']['coliage'] = 'False'
    config['ImageFeatures']['vessel'] = 'True'
    config['ImageFeatures']['phase'] = 'True'
    config['ImageFeatures']['log'] = 'True'
    config['ImageFeatures']['image_type'] = 'CT'
    config['ImageFeatures']['vessel_radius'] = '0'  # tumors can be really small

    config['Featsel']['Variance'] = 'True, False'

    config['SelectFeatGroup']['shape_features'] = 'True, False'
    config['SelectFeatGroup']['histogram_features'] = 'True, False'
    config['SelectFeatGroup']['orientation_features'] = 'True, False'
    config['SelectFeatGroup']['texture_Gabor_features'] = 'True, False'
    config['SelectFeatGroup']['texture_GLCM_features'] = 'True, False'
    config['SelectFeatGroup']['texture_GLCMMS_features'] = 'True, False'
    config['SelectFeatGroup']['texture_GLRLM_features'] = 'True, False'
    config['SelectFeatGroup']['texture_GLSZM_features'] = 'True, False'
    config['SelectFeatGroup']['texture_NGTDM_features'] = 'True, False'
    config['SelectFeatGroup']['texture_LBP_features'] = 'True, False'
    config['SelectFeatGroup']['patient_features'] = 'True, False'
    config['SelectFeatGroup']['semantic_features'] = 'True, False'
    config['SelectFeatGroup']['coliage_features'] = 'False'
    config['SelectFeatGroup']['vessel_features'] = 'True, False'
    config['SelectFeatGroup']['phase_features'] = 'True, False'
    config['SelectFeatGroup']['log_features'] = 'True, False'

    config['CrossValidation']['N_iterations'] = '100'

    config['Genetics']['label_names'] = 'GP'
    config['Genetics']['modus'] = 'singlelabel'

    config['HyperOptimization']['N_iterations'] = '100000'
    config['HyperOptimization']['n_jobspercore'] = '4000'

    config['SampleProcessing']['SMOTE'] = 'True'
    config['SampleProcessing']['Oversampling'] = 'False'

    config['Ensemble']['Use'] = 'False'

    return config


# Inputs
name = 'WORC_CLM_GP'
current_path = os.path.dirname(os.path.abspath(__file__))
label_file = os.path.join(current_path, 'pinfo_CLM.txt')
semantics_file = os.path.join(current_path, 'sem_CLM.txt')
config = os.path.join(current_path, 'config_modeloptimization.ini')

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

# The default config from the WORC 2.1.2 version we used, was a stripped
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
