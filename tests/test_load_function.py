import os
from dotenv import load_dotenv

from read import load_cards
  
# Load environment variables.
load_dotenv()

# Assign environment variables.
test_path_1 = os.getenv("TEST_PATH_1")
test_path_2 = os.getenv("TEST_PATH_2")


def test_file_single_line_content_to_list():
    """Does passing a path to a file with a single line return a list?"""
    test_list = load_cards(test_path_1)
    assert test_list == ['This is a test']


def test_file_multiple_lines_content_to_list():
    """Does passing a path to a file with multiple lines return a list?"""
    test_list = load_cards(test_path_2)
    assert test_list == ['This', 'is', 'a', 'test']

