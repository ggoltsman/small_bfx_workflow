import os
import pandas
import sqlite3
from modules import loadIt


def setup_function(function):
    print("Running setup: %s" % {function.__name__})
    function.vcf_fn = "data/unit_test.vcf"
    function.db_name = "unit_test_db"
    function.conn = sqlite3.connect(function.db_name)


def teardown_function(function):
    print("Running Teardown: %s" % {function.__name__})
    function.conn.close()


def test_loadIt():
    assert loadIt(test_loadIt.vcf_fn, test_loadIt.db_name) == 1
    os.remove(test_loadIt.db_name)
