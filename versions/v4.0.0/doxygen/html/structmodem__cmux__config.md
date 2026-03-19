---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmodem__cmux__config.html
original_path: doxygen/html/structmodem__cmux__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_cmux\_config Struct Reference

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md) » [Modem CMUX](group__modem__cmux.md)

Contains CMUX instance configuration data.
[More...](#details)

`#include <[cmux.h](cmux_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923) | [callback](#a2cba948c704f02429022d360326b9838) |
|  | Invoked when event occurs. |
| void \* | [user\_data](#a6714790f733ba7e4431353b6cdbbe3ee) |
|  | Free to use pointer passed to event handler when invoked. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_buf](#a2935694a75a95da8571b1c520a9800c8) |
|  | Receive buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_size](#a2fcf4ba7f088701ec6c5b750c8af3a89) |
|  | Size of receive buffer in bytes [127, ...]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [transmit\_buf](#a6920bf8f7c52522e8b76ba09051887c5) |
|  | Transmit buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [transmit\_buf\_size](#ae028b4dde63311a810c67686dc662154) |
|  | Size of transmit buffer in bytes [149, ...]. |

## Detailed Description

Contains CMUX instance configuration data.

## Field Documentation

## [◆ ](#a2cba948c704f02429022d360326b9838)callback

| [modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923) modem\_cmux\_config::callback |
| --- |

Invoked when event occurs.

## [◆ ](#a2935694a75a95da8571b1c520a9800c8)receive\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_cmux\_config::receive\_buf |
| --- |

Receive buffer.

## [◆ ](#a2fcf4ba7f088701ec6c5b750c8af3a89)receive\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_cmux\_config::receive\_buf\_size |
| --- |

Size of receive buffer in bytes [127, ...].

## [◆ ](#a6920bf8f7c52522e8b76ba09051887c5)transmit\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_cmux\_config::transmit\_buf |
| --- |

Transmit buffer.

## [◆ ](#ae028b4dde63311a810c67686dc662154)transmit\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_cmux\_config::transmit\_buf\_size |
| --- |

Size of transmit buffer in bytes [149, ...].

## [◆ ](#a6714790f733ba7e4431353b6cdbbe3ee)user\_data

| void\* modem\_cmux\_config::user\_data |
| --- |

Free to use pointer passed to event handler when invoked.

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[cmux.h](cmux_8h_source.md)

- [modem\_cmux\_config](structmodem__cmux__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
