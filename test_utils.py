import pytest
import datetime

from backend.mongodb_connector.utils import csv_to_filtered_json, fix_date_type_in_json


@pytest.fixture
def temp_csv_file_1_row(tmp_path):
    content = """Column1;Column2;Column3\nValue1;Value2;Value3"""
    csv_file = tmp_path / 'test.csv'
    csv_file.write_text(content)
    return csv_file

@pytest.fixture
def temp_csv_file_2_rows(tmp_path):
    content = """Column1;Column2;Column3\nValue1;Value2;Value3\nValue4;Value5;Value6"""
    csv_file = tmp_path / 'test.csv'
    csv_file.write_text(content)
    return csv_file

def test_csv_to_filtered_json_no_valid_columns_1_row(temp_csv_file_1_row):
    valid_columns = []
    expected_data = [{}]

    result = csv_to_filtered_json(temp_csv_file_1_row, valid_columns)

    assert result == expected_data

def test_csv_to_filtered_json_no_valid_columns_2_rows(temp_csv_file_2_rows):
    valid_columns = []
    expected_data = [{},{}]

    result = csv_to_filtered_json(temp_csv_file_2_rows, valid_columns)

    assert result == expected_data

def test_csv_to_filtered_json_valid_columns(temp_csv_file_1_row):
    valid_columns = ['Column1', 'Column3']
    expected_data = [{'Column1': 'Value1', 'Column3': 'Value3'}]

    result = csv_to_filtered_json(temp_csv_file_1_row, valid_columns)

    assert result == expected_data

def test_csv_to_filtered_json_valid_columns_2_rows(temp_csv_file_2_rows):
    valid_columns = ['Column1', 'Column3']
    expected_data = [{'Column1': 'Value1', 'Column3': 'Value3'}, {'Column1': 'Value4', 'Column3': 'Value6'}]

    result = csv_to_filtered_json(temp_csv_file_2_rows, valid_columns)

    assert result == expected_data

def test_fix_date_type_in_json_empty():
    input_json = [{}]
    expected_json = [{}]
    fix_date_type_in_json(input_json)

    assert expected_json == input_json

def test_fix_date_type_in_json_no_date_type_fieldname():
    input_json = [{"name":"Cuba"}]
    expected_json = [{"name":"Cuba"}]
    fix_date_type_in_json(input_json)

    assert expected_json == input_json

def test_fix_date_type_in_json_date_type_in_fieldnames():
    input_json = [{"name":"Cuba", "DateStamp":"04-11-2013 13:41:30"}]
    expected_date_stamp = datetime.datetime(day=4, month=11, year=2013, hour=13, minute=41, second=30)
    expected_json = [{"name":"Cuba", "DateStamp": expected_date_stamp}]
    fix_date_type_in_json(input_json)

    assert expected_json == input_json

def test_fix_date_type_in_json_date_type_in_fieldnames_2_documents():
    input_json = [{"name":"Cuba", "DateStamp":"04-11-2013 13:41:30"}, {"name":"Lipa", "DateStamp":"01-02-3456 10:11:12"}]
    expected_date_stamp_1 = datetime.datetime(day=4, month=11, year=2013, hour=13, minute=41, second=30)
    expected_date_stamp_2 = datetime.datetime(day=1, month=2, year=3456, hour=10, minute=11, second=12)
    expected_json = [{"name":"Cuba", "DateStamp": expected_date_stamp_1}, {"name":"Lipa", "DateStamp": expected_date_stamp_2}]
    fix_date_type_in_json(input_json)

    assert expected_json == input_json