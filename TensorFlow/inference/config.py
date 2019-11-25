import pathlib

class MODEL_COORDINATES:
	model_name = 'workspace/training_demo/trained-inference-graphs/output_inference_graph-48684.pb/saved_model'
	PATH_TO_LABELS = 'workspace/training_demo/annotations/label_map.pbtxt'

class IMAGE_COORDINATES:
	PATH_TO_TRAIN_IMAGES_DIR = pathlib.Path('/home/sanjay/TensorFlow/workspace/training_demo/images/train')
	PATH_TO_TEST_IMAGES_DIR = pathlib.Path('/home/sanjay/TensorFlow/workspace/training_demo/images/test')

	FILE_FORMAT = "png"

	SAVE_PATH = 'workspace/training_demo/images/test_inference'