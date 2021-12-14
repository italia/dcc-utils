DCC Utils
=========

Python library to decode the EU Covid-19 vaccine certificate, as
`specified by the
EU <https://ec.europa.eu/health/ehealth/covid-19_en>`__.

Setup
-----

.. code:: sh

   pip install dcc-utils

Make sure ``zbar`` is installed in your system \* For Mac OS X, it can
be installed via ``brew install zbar`` \* Debian systems via
``apt install libzbar0``. `Source <https://pypi.org/project/pyzbar/>`__
\* Fedora / Red Hat ``dnf install zbar``

Usage
-----

Parse DCC
~~~~~~~~~

This library takes an image with a QR code or a raw repr. of a vaccine
certificate as the parameter and will show the certificate’s content.

.. code:: py

   from dcc_utils import from_image

   dcc_from_img = from_image("/my/certificate/path")
   dcc_from_raw = from_raw("HC1:6BF...FTPQ3C3F")

Then you can access to ``payload`` and ``kid``

.. code:: py

   assert dcc_from_img.kid == "53FOjX/4aJs="
   assert dcc_from_img.payload["v"][0]["ci"] == "URN:UVCI:01:FR:W7V2BE46QSBJ#L"

``from_image`` and ``from_raw`` methods may rise ``DCCParsingError``

.. code:: py

   from dcc_utils.exceptions import DCCParsingError

Validate DCC digital signature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

   signature = """
   -----BEGIN CERTIFICATE-----
   MIIIAjCCBeqgAwIBAgIQAnq8g/T
   -----END CERTIFICATE-----
   """
   assert dcc.check_signature(signature)

``check_signature`` method may rise ``DCCSignatureError``

.. code:: py

   from dcc_utils.exceptions import DCCSignatureError

Dev setup
---------

Install dependencies via your distribution or via pip:

::

   pip install -r requirements-dev.txt

Run tests

::

   make test

EU Digital COVID Certificate Specifications
-------------------------------------------

What’s in a EU Digital COVID/Green Certificate? \* Value Sets for
Digital Green Certificates
https://ec.europa.eu/health/sites/default/files/ehealth/docs/digital-green-certificates_dt-specifications_en.pdf
\* JSON schema: https://github.com/ehn-dcc-development/ehn-dcc-schema

Sample data
~~~~~~~~~~~

Digital Green Certificate Gateway (DGCG) samples for all participating
countries: https://github.com/eu-digital-green-certificates/dgc-testdata

License
-------

This library is available under the
`MIT <https://opensource.org/licenses/mit-license.php>`__ license.
