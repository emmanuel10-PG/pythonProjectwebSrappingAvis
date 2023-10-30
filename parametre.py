import sys
import logging


# nombre de page
nb_page = 60

# repertoire d enregistrement des sorties
output_reviews_path = "data/reviews_data.xlsx"
output_process_reviews_path = "data/df_processing_path.xlsx"
output_pros_process_path = "data/oro_df.xlsx"
output_cons_process_path = "data/pro_cons_df.xlsx"


def get_logger(name):
    logging.basicConfig(stream=sys.stdout , format= '%(asctime)s - %(levelname)s - %(name)e - %(message)')
    logger = get_logger(name)
    return logger