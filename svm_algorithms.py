from magic_data.data_generator import DataGenerator
from magic_data.data_analyse import DataAnalyse  
from pathlib import Path

def main():
    file_name = '2D-data-liniar_sep'
    base_path = Path(__file__).resolve().parent
    config_path_csv = base_path / 'training_data' / file_name
    data_generator = DataGenerator(file_name=file_name,file_route=config_path_csv, data_configuration={})
    data_analyse = DataAnalyse(file_route=config_path_csv)
    return


if __name__== "__main__":
    main()