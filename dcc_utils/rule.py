import functools
import json
from dcc_utils.dcc import DCC
from json_logic.cert_logic import certLogic


class Rule:
    def __init__(self, payload: dict):
        self._payload = payload
        self._descriptions = functools.reduce(
            lambda descs, el: descs.update({el["lang"]: el["desc"]}) or descs,
            self._payload["Description"],
            {},
        )

    @property
    def payload(self) -> dict:
        return self._payload

    @property
    def description(self) -> dict:
        return self._descriptions

    def evaluate_dcc(self, dcc: DCC, external: dict = {}) -> bool:
        return certLogic(
            self._payload["Logic"], {"payload": dcc.payload, "external": external}
        )


def from_json(json_data: dict) -> Rule:
    return Rule(json_data)


def from_file(file_path: str) -> Rule:
    with open(file_path) as f:
        return from_json(json.loads(f.read()))
