import os
import datetime
from dcc_utils import rule, dcc


def test_simple_rule():
    my_dcc = dcc.from_image(os.path.join("tests", "test_data", "valid_certificate.png"))
    my_rule = rule.from_file(os.path.join("tests", "test_data", "de_v_rule.json"))
    res = my_rule.evaluate_dcc(my_dcc, 4)
    assert res


def test_rule_outta_time():
    my_dcc = dcc.from_image(os.path.join("tests", "test_data", "valid_certificate.png"))
    my_rule = rule.from_file(os.path.join("tests", "test_data", "de_v_rule_2.json"))
    clock = datetime.datetime(2022, 10, 10, 0, 0, tzinfo=datetime.timezone.utc)
    res = my_rule.evaluate_dcc(
        my_dcc,
        {
            "validationClock": clock,
        },
    )
    assert not res
