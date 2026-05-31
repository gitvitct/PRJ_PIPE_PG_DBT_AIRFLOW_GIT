# tests/unit/test_logger.py

import os
from scripts.logger_config import log_file, logger


def test_log_file_path():
    assert log_file.endswith("pipeline.log")


def test_log_directory_exists():
    assert os.path.exists(os.path.dirname(log_file))


def test_logger_can_write():
    logger.info("teste logger")

    assert os.path.exists(log_file)