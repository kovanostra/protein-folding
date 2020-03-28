import os
import pickle
from typing import List, Tuple, Any

from src.repository.interface.repository import Repository


class TrainingDataRepository(Repository):
    def __init__(self, path='src/data/') -> None:
        super().__init__()
        self.path = path

    def save(self, filename: str, dataset: Any) -> None:
        with open(self.path + filename, 'wb') as file:
            pickle.dump(dataset, file)

    def get_all_features_and_labels_from_separate_files(self) -> List[Tuple[Any, Any]]:
        files_in_path = self._extract_name_prefixes_from_filenames()
        dataset = []
        for file in files_in_path:
            dataset.append((self._get_features(file), self._get_labels(file)))
        return dataset

    def _get_labels(self, file):
        with open(self.path + file + 'labels.pickle', 'rb') as labels_file:
            labels = pickle.load(labels_file)
        return labels

    def _get_features(self, file):
        with open(self.path + file + 'features.pickle', 'rb') as features_file:
            features = pickle.load(features_file)
        return features

    def _extract_name_prefixes_from_filenames(self):
        return set([self._reconstruct_filename(file) for file in self._get_data_filenames()])

    def _get_data_filenames(self):
        return sorted([file for file in os.listdir(self.path) if file.endswith(".pickle")])

    @staticmethod
    def _reconstruct_filename(file):
        return "_".join(file.split("_")[:-1]) + "_"
