from generator.data_generator import DataGenerator
import json
from pathlib import Path

def generate_data(base_path):
    
    config_path = base_path / 'config' / 'data_config.json' 
    with open(config_path) as data:
        data_cofiguration = json.load(data)

    data_generator = DataGenerator(data_configuration=data_cofiguration)
    config_path_csv = base_path / 'training_data'
    data_generator.extract_as_csv(file_name='2D-data', file_route=config_path_csv)


def main():
    base_path = Path(__file__).resolve().parent
    
        

if __name__ == "__main__":
    main()