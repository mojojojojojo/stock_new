"""
test for storage module

"""

import os
import sys
sys.path.insert(0, os.getcwd())

from Modules_brand_new.storage import Storage
from Modules_brand_new.Data import Data


def gen_data():
    storage = Storage("test")
    data = Data()
    data.b_pattern = "0, 0"
    data.s_pattern = "0, 1"
    data.revenue_in_percent = 12
    storage.update_data_pattern(data)

    data.b_pattern = "0, 1"
    data.s_pattern = "0, 1"
    data.revenue_in_percent = 12
    storage.update_data_pattern(data)

    data.b_pattern = "0, 1"
    data.s_pattern = "0, 0, 1"
    data.revenue_in_percent = 20
    storage.update_data_pattern(data)

    data.s_pattern = "0, 0, 1"
    data.b_pattern = "0, 1, 0"
    data.revenue_in_percent = 20
    storage.update_data_pattern(data)


    return storage

def test_load_save():
    storage = gen_data()
    storage.save_format_file()
    storage = Storage("test")
    storage.load_format_file()

    for f in storage.data_patterns[2]:
        assert f.revenue_in_percent == 12
        assert len(storage.data_patterns[2]) == 2
    for f in storage.data_patterns[3]:
        assert f.revenue_in_percent == 20
        assert len(storage.data_patterns[2]) == 2
    os.remove("test.moj")

def test_buy_data():
    storage = gen_data()
    buy_data = storage.get_relevant_buy_data(2)
    assert len(buy_data) == 3
    assert buy_data[1].b_pattern == "0, 1"

def test_sell_data():
    storage = gen_data()
    sell_data = storage.get_relevant_sell_data(3,"0, 1")
    assert len(sell_data) == 1
    assert sell_data[0].s_pattern == "0, 0, 1"
