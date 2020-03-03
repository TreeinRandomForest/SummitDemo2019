import pathlib

class MODEL_COORDINATES:
	model_name = 'saved_model'
	PATH_TO_LABELS = 'label_map.pbtxt'

class IMAGE_COORDINATES:
	PATH_TO_TRAIN_IMAGES_DIR = pathlib.Path('test')
	PATH_TO_TEST_IMAGES_DIR = pathlib.Path('test')

	FILE_FORMAT = "png"

	SAVE_PATH = 'predictions'