from cose.headers import KID
from cose.messages import CoseMessage
from cose.keys import cosekey, keyops, keyparam, curves, keytype
from cose import algorithms
from cose.exceptions import CoseIllegalAlgorithm

from cryptography import x509
from cryptography import hazmat

from .exceptions import DCCSignatureError


def _cert_to_cose_key(cert: x509.Certificate, key_id: KID = None) -> cosekey.CoseKey:
    try:
        public_key = cert.public_key()
    except ValueError as ex:
        raise DCCSignatureError(ex)
    key_dict = None

    if isinstance(public_key, hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey):
        curve_name = public_key.curve.name
        matching_curve = None
        for name in dir(curves):
            if name.startswith("_"):
                continue
            if curve_name.lower() == name.lower():
                if name == "SECP256R1":
                    matching_curve = curves.P256
                elif name == "SECP384R1":
                    matching_curve = curves.P384
                else:
                    raise DCCSignatureError("Unknown curve {}!".format(curve_name))
                break

        if not matching_curve:
            raise DCCSignatureError(
                "Could not find curve {} used in X.509 certificate from COSE!".format(
                    curve_name
                )
            )

        public_numbers = public_key.public_numbers()
        size_bytes = public_key.curve.key_size // 8
        x = public_numbers.x.to_bytes(size_bytes, byteorder="big")
        y = public_numbers.y.to_bytes(size_bytes, byteorder="big")
        key_dict = {
            keyparam.KpKeyOps: [keyops.VerifyOp],
            keyparam.KpKty: keytype.KtyEC2,
            keyparam.EC2KpCurve: matching_curve,
            keyparam.KpAlg: algorithms.Es256,
            keyparam.EC2KpX: x,
            keyparam.EC2KpY: y,
            keyparam.KpKid: bytes(key_id.hex(), "ASCII"),
        }
    else:
        public_numbers = public_key.public_numbers()
        size_bytes = public_key.key_size
        n = public_numbers.n.to_bytes(256, byteorder="big")
        e = public_numbers.e.to_bytes(4, byteorder="big")
        key_dict = {
            keyparam.KpAlg: algorithms.Ps256,
            keyparam.KpKty: keytype.KtyRSA,
            keyparam.RSAKpN: n,
            keyparam.RSAKpE: e,
            keyparam.KpKid: bytes(key_id.hex(), "ASCII"),
        }

    key = cosekey.CoseKey.from_dict(key_dict)

    return key


def verify_signature(cose_msg: CoseMessage, kid: bytes, cert: bytes) -> bool:
    cert = x509.load_pem_x509_certificate(cert)
    key = _cert_to_cose_key(cert, kid)
    try:
        cose_msg.key = key
        verified = cose_msg.verify_signature()
        return verified
    except CoseIllegalAlgorithm:
        return False
