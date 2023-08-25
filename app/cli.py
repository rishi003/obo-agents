import os
import sys
import subprocess
from time import sleep
import shutil
from sys import platform
from multiprocessing import Process
from app.logger import logger


def check_command(command, message):
    if not shutil.which(command):
        logger.info(message)
        sys.exit(1)


# def run_npm_commands(shell=False):
#     os.chdir("gui")
#     try:
#         subprocess.run(["npm", "install"], check=True, shell=shell)
#     except subprocess.CalledProcessError:
#         logger.error(f"Error during '{' '.join(sys.exc_info()[1].cmd)}'. Exiting.")
#         sys.exit(1)
#     os.chdir("..")


def run_server(shell=False):
    api_process = Process(target=subprocess.run, args=(["uvicorn", "main:app", "--host", "localhost", "--port", "8000"],), kwargs={"shell": shell})
    celery_process = Process(target=subprocess.run, args=(["celery", "-A", "app.worker", "worker", "--loglevel=info", "--pool=solo"],), kwargs={"shell": shell})
    api_process.start()
    celery_process.start()

    return api_process, celery_process


def cleanup(api_process, celery_process):
    logger.info("Shutting down processes...")
    api_process.terminate()
    celery_process.terminate()
    logger.info("Processes terminated. Exiting.")
    sys.exit(1)


if __name__ == "__main__":
    # check_command("node", "Node.js is not installed. Please install it and try again.")
    # check_command("npm", "npm is not installed. Please install npm to proceed.")
    check_command("uvicorn", "uvicorn is not installed. Please install uvicorn to proceed.")

    isWindows = False
    if platform == "win32" or platform == "cygwin":
        isWindows = True
    # run_npm_commands(shell=isWindows)

    try:
        api_process, celery_process = run_server(isWindows)
        while True:
            try:
                sleep(30)
            except KeyboardInterrupt:
                cleanup(api_process, celery_process)
    except Exception as e:
        cleanup(api_process, celery_process)
