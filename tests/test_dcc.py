import os

from dcc_utils import from_image, from_raw


def test_certificate_from_raw():
    with open(
        os.path.join("tests", "test_data", "raw_cert")
    ) as cert:
        dcc = from_raw(cert.read())
        assert dcc.payload["nam"]["fn"] == "Mustermann"


def test_certificate_from_image():
    dcc = from_image(os.path.join("tests", "test_data", "mouse.jpeg"))
    assert dcc.kid == "53FOjX/4aJs="
    assert dcc.payload["v"][0]["ci"] == "URN:UVCI:01:FR:W7V2BE46QSBJ#L"


def test_ec_certificate():
    dcc = from_image(os.path.join("tests", "test_data", "signed_cert.png"))
    with open(
        os.path.join("tests", "test_data", "signing_certificate.crt"), "rb"
    ) as pem_file:
        assert dcc.check_signature(pem_file.read())


def test_rsa_certificate():
    dcc = from_image(os.path.join("tests", "test_data", "valid_ch_certificate.png"))
    with open(os.path.join("tests", "test_data", "cert_rsa.crt"), "rb") as pem_file:
        assert dcc.check_signature(pem_file.read())
