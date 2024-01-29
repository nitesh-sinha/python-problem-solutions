import concurrent.futures
import logging
import random
import time

# Configure logging to write messages to two different log files
logging.basicConfig(level=logging.INFO)
success_logger = logging.getLogger('success_logger')
success_logger.addHandler(logging.FileHandler('file1.log'))
failure_logger = logging.getLogger('failure_logger')
failure_logger.addHandler(logging.FileHandler('file2.log'))

def process_data(data):
    # Simulating processing time
    time.sleep(random.uniform(0.1, 0.5))

    # Simulating success or failure
    success = random.choice([True, False])

    if success:
        success_logger.info(f"Success: {data}")
    else:
        failure_logger.info(f"Failure: {data}")

# Sample data to be processed
data_to_process = ["Data1", "Data2", "Data3", "Data4", "Data5"]


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submitting tasks to the ThreadPoolExecutor
    futures = [executor.submit(process_data, data) for data in data_to_process]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)

# Optionally, you can retrieve the results if needed
# results = [future.result() for future in futures]
