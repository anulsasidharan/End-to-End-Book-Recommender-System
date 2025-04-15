# Entity given the return type of the function
from collections import namedtuple

DataIngestionConfig = namedtuple("DatasetConfig", ["dataset_download_url",
                                                   "raw_data_dir",
                                                   "ingested_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
                                                           "books_csv_file",
                                                           "rating_csv_file",
                                                           "serialized_object_dir"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["clean_data_file_path",
                                                                   "transformed_data_dir"])

ModelTrainingConfig = namedtuple("ModelTrainingConfig", ["transformed_data_file_dir",
                                                         "trained_model_dir",
                                                         "trained_model_name"])

ModelRecommendationConfig = namedtuple("ModelRecommendationConfig", ["book_name_serialized_objects",
                                                                     "book_pivot_serialized_objects",
                                                                     "final_rating_serialized_objects",
                                                                     "trained_model_path"])