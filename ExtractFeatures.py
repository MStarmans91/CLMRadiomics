import PREDICT
import os

# Configure location of input
current_path = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(current_path, 'ExampleData', 'ExampleImage.nii.gz')
segmentation = os.path.join(current_path, 'ExampleData', 'ExampleSegmentation.nii.gz')
metadata = os.path.join(current_path, 'ExampleData', 'ExampleDCM.dcm')
config = os.path.join(current_path, 'ExampleData', 'config_features.ini')

# Configure location of output
output = os.path.join(current_path, 'ExampleData', 'ExampleFeatures.hdf5')


PREDICT.CalcFeatures.CalcFeatures(image=image, segmentation=segmentation,
                                  parameters=config, metadata_file=metadata,
                                  output=output)
