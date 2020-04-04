import torch as to

from src.domain.loss_function_selector import LossFunctionSelector
from src.domain.optimizer_selector import OptimizerSelector
from src.repository.interface.repository import Repository
from src.repository.training_data_repository import TrainingDataRepository
from src.usecase.training import Training


class MessagePassingNN:
    def __init__(self, training: Training, repository: Repository, device: str) -> None:
        self.training = training
        self.repository = repository
        self.device = device

    def start(self):
        self.training.start(self.repository, self.device)


def create(dataset: str,
           epochs: int,
           loss_function_selection: str,
           optimizer_selection: str,
           data_path: str,
           enable_gpu: bool) -> MessagePassingNN:
    create_success_file()
    device = setup_gpu(enable_gpu)
    training_data_repository = TrainingDataRepository(data_path, dataset)
    loss_function = LossFunctionSelector(loss_function_selection).loss_function
    optimizer = OptimizerSelector(optimizer_selection).optimizer
    training = Training(epochs, loss_function, optimizer)
    return MessagePassingNN(training, training_data_repository, device)


def setup_gpu(enable_gpu: bool) -> str:
    if enable_gpu:
        device = to.device("cuda" if to.cuda.is_available() else "cpu")
    else:
        device = "cpu"
    return device


def create_success_file():
    f = open("SUCCESS", "w")
    f.close()
