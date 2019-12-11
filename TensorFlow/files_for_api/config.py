import pathlib

class MODEL_COORDINATES:
	model_name = 'workspace/rhfedora/trained-inference-graphs/output_inference_graph-928.pb/saved_model'
	PATH_TO_LABELS = 'workspace/rhfedora/annotations/label_map.pbtxt'

class IMAGE_COORDINATES:
	PATH_TO_TRAIN_IMAGES_DIR = pathlib.Path('/home/sanjay/FinalObjectDetection/TensorFlow/workspace/rhfedora/images/train')
	PATH_TO_TEST_IMAGES_DIR = pathlib.Path('/home/sanjay/FinalObjectDetection/TensorFlow/workspace/rhfedora/images/test')

	FILE_FORMAT = "jpg"

	TRAIN_SAVE_PATH = 'workspace/rhfedora/images/train_inference'
	TEST_SAVE_PATH = 'workspace/rhfedora/images/test_inference'