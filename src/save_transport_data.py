import datetime
import random
from config import logger
from data_processing import save_times_data


def random_time_samples(datetime_start):
    time_samples = []
    time = datetime_start
    while time < datetime.datetime(2020, 3, 30, 23, 0, 0):
        time += datetime.timedelta(seconds=random.uniform(420, 720))
        time_samples.append(time)
    return time_samples


def experiment_data():
    datetime_start = datetime.datetime(2020, 3, 30, 14, 45, 17)
    time_samples = random_time_samples(datetime_start)

    for idx, item in enumerate(time_samples):
        save_times_data(item)
        logger.info(f"{idx + 1}/{len(time_samples)} of time samples")


if __name__ == "__main__":
    experiment_data()
