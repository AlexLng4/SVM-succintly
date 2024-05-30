from magic_data.data_handler import DataHandler
import json
from pathlib import Path


def main():

    # useful path for manipulating the data
    file_name = '2D-data-liniar_sep'
    base_path = Path(__file__).resolve().parent
    config_path = base_path / 'config' / 'data_config.json'
    config_path_csv = base_path / 'training_data' / file_name
    if not Path(config_path_csv).exists():
        Path(config_path_csv).mkdir(parents=True, exist_ok=True)

    with open(config_path) as data:
        data_cofiguration = json.load(data)
    data_generator = DataHandler(data_configuration=data_cofiguration, file_name=file_name, file_route=config_path_csv)
    #data_generator.generate_samples()

if __name__ == "__main__":
    main()