import os
import sys
import ast
import pandas as pd
import pickle
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException

class DataValidation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e
        
    def processing_data(self):
        try:
            ratings = pd.read_csv(self.data_validation_config.rating_csv_file, sep=";", on_bad_lines='skip', encoding='latin-1')
            books = pd.read_csv(self.data_validation_config.books_csv_file, sep=";", on_bad_lines='skip', encoding='latin-1')

            logging.info(f"Shape of ratings data file: {ratings.shape}")
            logging.info(f"Shape of books data file: {books.shape}")

            # Here the Image URL columns is important for the poster. So we will have to keep . 
            # Remaining unwanted columns can be discarded. 
            books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher','Image-URL-L']]
            # Let's rename the weared column names in books
            books.rename(columns={
                    'Book-Title':'title',
                    'Book-Author':'author',
                    'Year-Of-Publication':'year',
                    'Publisher':'publisher',
                    'Image-URL-L':'image-url',
                    }, inplace=True)
            
            # Let's rename some wared column names in ratings
            ratings.rename(columns={'User-ID':'user-id', 
                                    'Book-Rating':'rating'}, inplace=True)
            
            # Let's store the users who had at least rated more than 200 books
            x = ratings['user-id'].value_counts() > 200
            y = x[x].index
            ratings = ratings[ratings['user-id'].isin(y)]

            # Now join ratings with books
            rating_with_books = ratings.merge(books, on='ISBN')
            number_rating = rating_with_books.groupby('title')['rating'].count().reset_index()
            number_rating.rename(columns={'rating':'num_of_rating'}, inplace=True)
            final_rating = rating_with_books.merge(number_rating, on='title')

            # Let's take those books which got at least 50 ratings of user
            final_rating = final_rating[final_rating['num_of_rating']>=50]

            # Let's drop the duplicates
            final_rating.drop_duplicates(['user-id','title'], inplace=True)
            logging.info(f"Shape of the final clean dataset: {final_rating.shape}")

            # Saving the cleaned data for transformation
            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            final_rating.to_csv(os.path.join(self.data_validation_config.clean_data_dir, 'clean_data.csv'), index = False)
            logging.info(f"Saved final_rating serialization object to {self.data_validation_config.serialized_object_dir}")

            # Saving final_rating objects for web app
            os.makedirs(self.data_validation_config.serialized_object_dir, exist_ok=True)
            pickle.dump(final_rating, open(os.path.join(self.data_validation_config.serialized_object_dir, "final_rating.pkl"), 'wb'))
            logging.info(f"Saved final_rating serialization object to {self.data_validation_config.serialized_object_dir}")

        except Exception as e:
            raise AppException(e, sys) from e
        
    def initiate_data_validation(self):
        try:
            logging.info(f"{'='*20}Data Validation log Started{'='*20}")
            self.processing_data()
            logging.info(f"{'='*20}Data Validation log Completed{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e


