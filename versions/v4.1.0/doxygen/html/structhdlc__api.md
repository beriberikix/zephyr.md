---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structhdlc__api.html
original_path: doxygen/html/structhdlc__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hdlc\_api Struct Reference

HDLC interface configuration data.
[More...](#details)

`#include <[hdlc_rcp_if.h](hdlc__rcp__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#abeb64661526d0a3e241e6515707284de) |
|  | HDLC interface API. |
| int(\* | [register\_rx\_cb](#a2b18e7cd6dc393769b3d3ad2c8bf63ed) )([hdlc\_rx\_callback\_t](hdlc__rcp__if_8h.md#a58fa03009f99c7927c930b06fd1dfd0e) hdlc\_rx\_callback, void \*param) |
|  | Register the Spinel HDLC RX callback. |
| int(\* | [send](#a5a1958253b254008cd142c2c3ab33d2a) )(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*frame, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Transmit a HDLC frame. |
| int(\* | [deinit](#a33486d7c73df2958bf89bfe500b27464) )(void) |
|  | Deinitialize the device. |

## Detailed Description

HDLC interface configuration data.

## Field Documentation

## [◆ ](#a33486d7c73df2958bf89bfe500b27464)deinit

| int(\* hdlc\_api::deinit) (void) |
| --- |

Deinitialize the device.

Parameters
:   | none |  |
    | --- | --- |

Return values
:   | 0 | The interface was successfully stopped. |
    | --- | --- |
    | -EIO | The interface could not be stopped. |

## [◆ ](#abeb64661526d0a3e241e6515707284de)iface\_api

| struct net\_if\_api hdlc\_api::iface\_api |
| --- |

HDLC interface API.

## [◆ ](#a2b18e7cd6dc393769b3d3ad2c8bf63ed)register\_rx\_cb

| int(\* hdlc\_api::register\_rx\_cb) ([hdlc\_rx\_callback\_t](hdlc__rcp__if_8h.md#a58fa03009f99c7927c930b06fd1dfd0e) hdlc\_rx\_callback, void \*param) |
| --- |

Register the Spinel HDLC RX callback.

Parameters
:   | hdlc\_rx\_callback | pointer to the spinel HDLC RX callback |
    | --- | --- |
    | param | pointer to the spinel HDLC interface |

Return values
:   | 0 | The callback was successfully registered. |
    | --- | --- |
    | -EIO | The callback could not be registered. |

## [◆ ](#a5a1958253b254008cd142c2c3ab33d2a)send

| int(\* hdlc\_api::send) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*frame, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
| --- |

Transmit a HDLC frame.

Parameters
:   | frame | pointer to the HDLC frame to be transmitted. |
    | --- | --- |
    | length | length of the HDLC frame to be transmitted. |

Return values
:   | 0 | The frame was successfully sent. |
    | --- | --- |
    | -EIO | The frame could not be sent due to some unspecified interface error (e.g. the interface being busy). |

---

The documentation for this struct was generated from the following file:

- zephyr/net/hdlc\_rcp\_if/[hdlc\_rcp\_if.h](hdlc__rcp__if_8h_source.md)

- [hdlc\_api](structhdlc__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
