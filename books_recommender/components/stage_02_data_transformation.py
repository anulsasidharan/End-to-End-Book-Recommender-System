import os
import sys
import pickle
import pandas as pd
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.config.configuration import AppConfiguration

class DataTransformation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.data_transformation_config = app_config.get_data_transformation_config()
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e
        
    def get_data_transformer(self):
        try:
            # Create a new dataframe for the cleaned dataset
            df = pd.read_csv(self.data_transformation_config.clean_data_file_path)

            # Let's create the pivot table
            book_pivot = df.pivot_table(columns='user-id', index='title', values='rating')
            logging.info(f"Shape of the book pivio table: {book_pivot.shape}")

            # Let's fill the NaN values with zeros
            book_pivot.fillna(0, inplace=True)

            # Saving pivot table data
            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            pickle.dump(book_pivot, open(os.path.join(self.data_transformation_config.transformed_data_dir, "transformed_data.pkl"), 'wb'))
            logging.info(f"Saved book_names serialization objects to {self.data_validation_config.serialized_object_dir}")

            # Keeping books name
            book_names = book_pivot.index

            # Saving book_names objects for web app
            os.makedirs(self.data_validation_config.serialized_object_dir, exist_ok=True)
            pickle.dump(book_names, open(os.path.join(self.data_validation_config.serialized_object_dir, "book_names.pkl"), 'wb'))
            logging.info(f"Saved book_names serialization objects to {self.data_validation_config.serialized_object_dir}")

            # Saving book_pivot object for web app
            os.makedirs(self.data_validation_config.serialized_object_dir, exist_ok=True)
            pickle.dump(book_pivot, open(os.path.join(self.data_validation_config.serialized_object_dir, "book_pivot.pkl"), 'wb'))
            logging.info(f"Saved book_pivot serialization object to {self.data_validation_config.serialized_object_dir}")

        except Exception as e:
            raise AppException(e, sys) from e
        
    def initiate_data_transformation(self):
        try:
            logging.info(f"{'='*20}Data Transformation log started.{'='*20} ")
            self.get_data_transformer()
            logging.info(f"{'='*20}Data Transformation log Completed.{'='*20} ")
        except Exception as e:
            raise AppException(e, sys) from e