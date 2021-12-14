import os
import pytest

from dcc_utils import from_image, from_raw
from dcc_utils.exceptions import DCCError, DCCSignatureError


def test_certificate_from_raw():
    with open(os.path.join("tests", "test_data", "raw_cert")) as cert:
        dcc = from_raw(cert.read())
        assert dcc.payload["nam"]["fn"] == "Mustermann"


def test_certificate_from_raw_base45_expl():
    with open(os.path.join("tests", "test_data", "raw_cert_base45_expl")) as cert:
        with pytest.raises(DCCError):
            from_raw(cert.read())


def test_certificate_from_image():
    dcc = from_image(os.path.join("tests", "test_data", "mouse.jpeg"))
    assert dcc.kid == "53FOjX/4aJs="
    assert dcc.payload["v"][0]["ci"] == "URN:UVCI:01:FR:W7V2BE46QSBJ#L"


def test_certificate_from_not_valid_image():
    with pytest.raises(DCCError):
        from_image(os.path.join("tests", "test_data", "not_valid_certificate.png"))


def test_ec_certificate():
    dcc = from_image(os.path.join("tests", "test_data", "signed_cert.png"))
    with open(
        os.path.join("tests", "test_data", "signing_certificate.crt"), "rb"
    ) as pem_file:
        assert dcc.check_signature(pem_file.read())


def test_not_valid_certificate():
    dcc = from_image(os.path.join("tests", "test_data", "signed_cert.png"))
    with open(
        os.path.join("tests", "test_data", "wrong_signing_certificate.crt"), "rb"
    ) as pem_file:
        with pytest.raises(DCCSignatureError):
            dcc.check_signature(pem_file.read())


def test_wrong_certificate():
    dcc = from_image(os.path.join("tests", "test_data", "signed_cert.png"))
    with open(os.path.join("tests", "test_data", "cert_rsa.crt"), "rb") as pem_file:
        assert not dcc.check_signature(pem_file.read())


def test_rsa_certificate():
    dcc = from_image(os.path.join("tests", "test_data", "valid_ch_certificate.png"))
    with open(os.path.join("tests", "test_data", "cert_rsa.crt"), "rb") as pem_file:
        assert dcc.check_signature(pem_file.read())
