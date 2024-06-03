from magic_data.data_generator import DataGenerator
from magic_data.data_analyse import DataAnalyse  
from pathlib import Path

def main():
    file_name = '2D-data-liniar_sep'
    base_path = Path(__file__).resolve().parent
    data_path = Path(base_path / 'training_data' / file_name)
    data_analyse = DataAnalyse("2D-data-liniar_sep", data_path)
    data = data_analyse.extract_data()
    return

if __name__== "__main__":
    main()