import os

from dcc_utils import from_image


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
