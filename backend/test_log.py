import pytest
from .log import Log

def test_sanity():
    assert True;

def test_log_creation():
    log = Log(1,"IM00001", "Reasignment", '07-01-2013 08:17:54')
    assert log.log_id == 1
    assert log.incident_id == 'IM00001'
    assert log.date_stamp == '07-01-2013 08:17:54'
    assert log.incident_activity_type == "Reasignment"