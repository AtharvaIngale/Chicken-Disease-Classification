artifacts_root: artifacts


data_ingestion:
  root_dir: artifacts/data_ingestion
  source_URL: https://github.com/AtharvaIngale/Datasets/blob/78136fd3d6a86b8011e53bb35079d81927af27b7/Chicken-fecal-images.zip
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion



prepare_base_model:
  root_dir: artifacts/prepare_base_model
  base_model_path: artifacts/prepare_base_model/base_model.h5
  updated_base_model_path: artifacts/prepare_base_model/base_model_updated.h5




prepare_callbacks:
  root_dir: artifacts/prepare_callbacks
  tensorboard_root_log_dir: artifacts/prepare_callbacks/tensorboard_log_dir
  checkpoint_model_filepath: artifacts/prepare_callbacks/checkpoint_dir/model.h5




training:
  root_dir: artifacts/training
  trained_model_path: artifacts/training/model.h5