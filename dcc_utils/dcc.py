import zlib
import PIL.Image
import json
import base45
import cbor2
from pyzbar import pyzbar
from cose.messages import CoseMessage, sign1message
from cose.headers import KID

from .utils import verify_signature
from .errors import DCCError


class DCC:
    def __init__(
        self, payload: dict, raw: str, cose_msg: sign1message.Sign1Message, kid: bytes
    ):
        self._payload = payload[-260][1]
        self._raw = raw
        self._cose = cose_msg
        self._kid = kid

    def __str__(self) -> str:
        return json.dumps(self._payload, indent=2, default=str, ensure_ascii=False)

    def check_signature(self, cert: bytes) -> bool:
        return verify_signature(self._cose, self._kid, cert)


def from_raw(raw_data: str) -> DCC:
    # Code adapted from:
    # https://github.com/HQJaTu/vacdec/blob/main/vacdec
    b45data = raw_data[4:]
    zlibdata = base45.b45decode(b45data)
    decompressed = zlib.decompress(zlibdata)
    cose_msg = CoseMessage.decode(decompressed)
    pkid, ukid = cose_msg.phdr.get(KID), cose_msg.uhdr.get(KID)
    if not pkid and not ukid:
        raise DCCError("Certificate not signed!")
    else:
        kid = pkid or ukid
    payload = cbor2.loads(cose_msg.payload)
    return DCC(payload, raw_data, cose_msg, kid)


def from_image(image_path: str) -> DCC:
    data = pyzbar.decode(PIL.Image.open(image_path))
    if len(data) == 0:
        raise DCCError("Not valid image!")
    return from_raw(data[0].data.decode())
