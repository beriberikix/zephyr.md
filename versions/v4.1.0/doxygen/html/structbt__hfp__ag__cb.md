---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hfp__ag__cb.html
original_path: doxygen/html/structbt__hfp__ag__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hfp\_ag\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hands Free Profile - Audio Gateway (HFP-AG)](group__bt__hfp__ag.md)

HFP profile AG application callback.
[More...](#details)

`#include <[hfp_ag.h](hfp__ag_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#a1468a8757c6809ea29fa66983303284f) )(struct bt\_hfp\_ag \*ag) |
|  | HF AG connected callback to application. |
| void(\* | [disconnected](#af9c53ab021dbbf1017d71895581960c4) )(struct bt\_hfp\_ag \*ag) |
|  | HF disconnected callback to application. |
| void(\* | [sco\_connected](#aac2b1ff4d80361e0e5eea2481027b4cf) )(struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn) |
|  | HF SCO/eSCO connected Callback. |
| void(\* | [sco\_disconnected](#ab2f62feda2c535db446d55a5f56922f9) )(struct bt\_hfp\_ag \*ag) |
|  | HF SCO/eSCO disconnected Callback. |
| int(\* | [memory\_dial](#af335450c5e63139485fa5a131814d650) )(struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number) |
|  | HF memory dialing request Callback. |
| void(\* | [outgoing](#a967407f8869798b99287740e19ea215b) )(struct bt\_hfp\_ag \*ag, const char \*number) |
|  | HF outgoing Callback. |
| void(\* | [incoming](#adea86dd7d3b5b3ecabd093bace2de1fc) )(struct bt\_hfp\_ag \*ag, const char \*number) |
|  | HF incoming Callback. |
| void(\* | [ringing](#acae15cb697a20b6ca292d1f7f32ae0db) )(struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) in\_band) |
|  | HF ringing Callback. |
| void(\* | [accept](#a149ddc0677064aa85bf3fd0fd43f922c) )(struct bt\_hfp\_ag \*ag) |
|  | HF call accept Callback. |
| void(\* | [reject](#a9b857cdfd8b29f2bc08013b7eb62081b) )(struct bt\_hfp\_ag \*ag) |
|  | HF call reject Callback. |
| void(\* | [terminate](#aa00e1cb683e8cbe05483204649604e53) )(struct bt\_hfp\_ag \*ag) |
|  | HF call terminate Callback. |
| void(\* | [codec](#a2f15172060cc5d225894be5c8311610b) )(struct bt\_hfp\_ag \*ag, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ids) |
|  | Supported codec Ids callback. |

## Detailed Description

HFP profile AG application callback.

## Field Documentation

## [◆ ](#a149ddc0677064aa85bf3fd0fd43f922c)accept

| void(\* bt\_hfp\_ag\_cb::accept) (struct bt\_hfp\_ag \*ag) |
| --- |

HF call accept Callback.

If this callback is provided it will be called whenever the call is accepted.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#a2f15172060cc5d225894be5c8311610b)codec

| void(\* bt\_hfp\_ag\_cb::codec) (struct bt\_hfp\_ag \*ag, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ids) |
| --- |

Supported codec Ids callback.

If this callback is provided it will be called whenever the supported codec ids are updated.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#a1468a8757c6809ea29fa66983303284f)connected

| void(\* bt\_hfp\_ag\_cb::connected) (struct bt\_hfp\_ag \*ag) |
| --- |

HF AG connected callback to application.

If this callback is provided it will be called whenever the AG connection completes.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#af9c53ab021dbbf1017d71895581960c4)disconnected

| void(\* bt\_hfp\_ag\_cb::disconnected) (struct bt\_hfp\_ag \*ag) |
| --- |

HF disconnected callback to application.

If this callback is provided it will be called whenever the connection gets disconnected, including when a connection gets rejected or cancelled or any error in SLC establishment.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#adea86dd7d3b5b3ecabd093bace2de1fc)incoming

| void(\* bt\_hfp\_ag\_cb::incoming) (struct bt\_hfp\_ag \*ag, const char \*number) |
| --- |

HF incoming Callback.

If this callback is provided it will be called whenever a new call is incoming.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Incoming number |

## [◆ ](#af335450c5e63139485fa5a131814d650)memory\_dial

| int(\* bt\_hfp\_ag\_cb::memory\_dial) (struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number) |
| --- |

HF memory dialing request Callback.

If this callback is provided it will be called whenever a new call is requested with memory dialing from HFP unit. Get the phone number according to the given AG memory location.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | location | AG memory location |
    | number | Dailing number |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a967407f8869798b99287740e19ea215b)outgoing

| void(\* bt\_hfp\_ag\_cb::outgoing) (struct bt\_hfp\_ag \*ag, const char \*number) |
| --- |

HF outgoing Callback.

If this callback is provided it will be called whenever a new call is outgoing.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Dailing number |

## [◆ ](#a9b857cdfd8b29f2bc08013b7eb62081b)reject

| void(\* bt\_hfp\_ag\_cb::reject) (struct bt\_hfp\_ag \*ag) |
| --- |

HF call reject Callback.

If this callback is provided it will be called whenever the call is rejected.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#acae15cb697a20b6ca292d1f7f32ae0db)ringing

| void(\* bt\_hfp\_ag\_cb::ringing) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) in\_band) |
| --- |

HF ringing Callback.

If this callback is provided it will be called whenever the call is in the ringing

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | in\_bond | true - in-bond ringing, false - No in-bond ringing |

## [◆ ](#aac2b1ff4d80361e0e5eea2481027b4cf)sco\_connected

| void(\* bt\_hfp\_ag\_cb::sco\_connected) (struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn) |
| --- |

HF SCO/eSCO connected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection completes.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | sco\_conn | SCO/eSCO Connection object. |

## [◆ ](#ab2f62feda2c535db446d55a5f56922f9)sco\_disconnected

| void(\* bt\_hfp\_ag\_cb::sco\_disconnected) (struct bt\_hfp\_ag \*ag) |
| --- |

HF SCO/eSCO disconnected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection gets disconnected.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | sco\_conn | SCO/eSCO Connection object. |

## [◆ ](#aa00e1cb683e8cbe05483204649604e53)terminate

| void(\* bt\_hfp\_ag\_cb::terminate) (struct bt\_hfp\_ag \*ag) |
| --- |

HF call terminate Callback.

If this callback is provided it will be called whenever the call is terminated.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[hfp\_ag.h](hfp__ag_8h_source.md)

- [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
