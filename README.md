# DCC Utils
Python library to decode the EU Covid-19 vaccine certificate, as [specified by the EU](https://ec.europa.eu/health/ehealth/covid-19_en).

This script takes an image with a QR code or a raw repr. of a vaccine certificate as
the parameter and will show the certificate's content. It will also validate the digital signature.

## Setup

```sh
pip install dcc-utils
```

Make sure `zbar` is installed in your system
  * For Mac OS X, it can be installed via `brew install zbar`
  * Debian systems via `apt install libzbar0`. [Source](https://pypi.org/project/pyzbar/)
  * Fedora / Red Hat `dnf install zbar`


## Dev setup

Install dependencies via your distribution or via pip:

```
pip install -r requirements.txt
```

Run tests

```
make test
```

# EU Digital COVID Certificate Specifications
What's in a EU Digital COVID/Green Certificate?
* Value Sets for Digital Green Certificates https://ec.europa.eu/health/sites/default/files/ehealth/docs/digital-green-certificates_dt-specifications_en.pdf
* JSON schema: https://github.com/ehn-dcc-development/ehn-dcc-schema

## Sample data
Digital Green Certificate Gateway (DGCG) samples for all participating countries:
https://github.com/eu-digital-green-certificates/dgc-testdata

