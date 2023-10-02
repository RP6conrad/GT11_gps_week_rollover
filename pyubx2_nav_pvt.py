"""
UBX Protocol Output payload definitions

THESE ARE THE PAYLOAD DEFINITIONS FOR _GET_ MESSAGES _FROM_ THE RECEIVER
(e.g. Periodic Navigation Data; Poll Responses; Info messages)

Created on 27 Sep 2020

Information sourced from public domain u-blox Interface Specifications © 2013-2021, u-blox AG

:author: semuadmin
"""
"NAV-PVT": {
        "iTOW": U4,
        "year": U2,
        "month": U1,
        "day": U1,
        "hour": U1,
        "min": U1,
        "second": U1,
        "valid": (
            X1,
            {
                "validDate": U1,
                "validTime": U1,
                "fullyResolved": U1,
                "validMag": U1,
            },
        ),
        "tAcc": U4,
        "nano": I4,
        "fixType": U1,
        "flags": (
            X1,
            {
                "gnssFixOk": U1,
                "difSoln": U1,
                "psmState": U3,
                "headVehValid": U1,
                "carrSoln": U2,
            },
        ),
        "flags2": (
            X1,
            {
                "reserved": U5,
                "confirmedAvai": U1,
                "confirmedDate": U1,
                "confirmedTime": U1,
            },
        ),
        "numSV": U1,
        "lon": [I4, SCAL7],
        "lat": [I4, SCAL7],
        "height": I4,
        "hMSL": I4,
        "hAcc": U4,
        "vAcc": U4,
        "velN": I4,
        "velE": I4,
        "velD": I4,
        "gSpeed": I4,
        "headMot": [I4, SCAL5],
        "sAcc": U4,
        "headAcc": [U4, SCAL5],
        "pDOP": [U2, SCAL2],
        "flags3": (
            X2,
            {
                "invalidLlh": U1,
                "lastCorrectionAge": U4,
            },
        ),
        "reserved0": U4,  # NB this is incorrectly stated as U5 in older documentation
        "headVeh": [I4, SCAL5],
        "magDec": [I2, SCAL2],
        "magAcc": [U2, SCAL2],
    }