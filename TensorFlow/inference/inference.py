import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import pathlib

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from IPython.display import display

#from object_detection.utils import ops as utils_ops
import config
import label_utils as label_map_util
import image_utils

# patch tf1 into `utils.ops`
#utils_ops.tf = tf.compat.v1

# Patch the location of gfile
tf.gfile = tf.io.gfile


#png vs jpg
FILE_FORMAT = config.IMAGE_COORDINATES.FILE_FORMAT

#label locations
PATH_TO_LABELS = config.MODEL_COORDINATES.PATH_TO_LABELS
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)


#train and test images
PATH_TO_TRAIN_IMAGES_DIR = config.IMAGE_COORDINATES.PATH_TO_TRAIN_IMAGES_DIR
TRAIN_IMAGE_PATHS = sorted(list(PATH_TO_TRAIN_IMAGES_DIR.glob(f"*.{FILE_FORMAT}")))

PATH_TO_TEST_IMAGES_DIR = config.IMAGE_COORDINATES.PATH_TO_TEST_IMAGES_DIR
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob(f"*.{FILE_FORMAT}")))


def load_local_model(model_path):
  model = tf.saved_model.load(str(model_path))
  model = model.signatures['serving_default']

  return model

#model
model_name = config.MODEL_COORDINATES.model_name
detection_model = load_local_model(model_name)


def run_inference_for_single_image(model, image):
  image = np.asarray(image)
  # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
  input_tensor = tf.convert_to_tensor(image)
  # The model expects a batch of images, so add an axis with `tf.newaxis`.
  input_tensor = input_tensor[tf.newaxis,...]

  # Run inference
  output_dict = model(input_tensor)

  # All outputs are batches tensors.
  # Convert to numpy arrays, and take index [0] to remove the batch dimension.
  # We're only interested in the first num_detections.
  num_detections = int(output_dict.pop('num_detections'))
  output_dict = {key:value[0, :num_detections].numpy() 
                 for key,value in output_dict.items()}
  output_dict['num_detections'] = num_detections

  # detection_classes should be ints.
  output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
       
  return output_dict


def create_bbox_image(model, image_path, save_path = None):
  #read image
  image_np = np.array(Image.open(image_path))

  #make prediction
  output_dict = run_inference_for_single_image(model, image_np)

  #visualize bounding boxes
  image_box = image_utils.visualize_boxes_and_labels_on_image_array(image_np, output_dict['detection_boxes'], output_dict['detection_classes'], \
                                                                 output_dict['detection_scores'], category_index, instance_masks=output_dict.get('detection_masks_reframed', None), \
                                                                 use_normalized_coordinates=True, line_thickness=8)  


  if save_path is not None:
    save_name = str(image_path).split('/')[-1]
    Image.fromarray(image_box).save(f'{save_path}/{save_name}')

  return output_dict


def save_all_bboxes(model, image_paths, save_path):
  outputs = {}
  for path in image_paths:
    try:
      outputs[path] = create_bbox_image(detection_model, path, save_path)
    except Exception as e:
      print(f"Issue: {e}")

  return outputs

#venv
#python models/research/object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path workspace/training_demo/training/ssd.config --trained_checkpoint_prefix workspace/training_demo/training/model.ckpt-48684 --output_directory workspace/training_demo/trained-inference-graphs/output_inference_graph-48684.pb/      

#venv_tf2 - inference