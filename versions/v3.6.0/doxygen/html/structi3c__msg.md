---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi3c__msg.html
original_path: doxygen/html/structi3c__msg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_msg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Transfer API](group__i3c__transfer__api.md)

One I3C Message.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#aa9d8920782b1a024b70970d60886deff) |
|  | Data buffer in bytes. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#ada6582cdd126f36e64f17f66ae3817f0) |
|  | Length of buffer in bytes. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_xfer](#a572d9f55461561fb9a8c31e46f0ebfe5) |
|  | Total number of bytes transferred. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a05113fb61ebbc95ded15fcfe374c0217) |
|  | Flags for this message. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [hdr\_mode](#a53f5ef80b2cf467e9ff557be7cc568c9) |
|  | HDR mode (`I3C_MSG_HDR_MODE*`) for transfer if any `I3C_MSG_HDR_*` is set in `flags`. |

## Detailed Description

One I3C Message.

This defines one I3C message to transact on the I3C bus.

Note
:   Some of the configurations supported by this API may not be supported by specific SoC I3C hardware implementations, in particular features related to bus transactions intended to read or write data from different buffers within a single transaction. Invocations of [i3c\_transfer()](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8 "Perform data transfer from the controller to a I3C target device.") may not indicate an error when an unsupported configuration is encountered. In some cases drivers will generate separate transactions for each message fragment, with or without presence of [I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295 "I3C_MSG_RESTART") in [flags](#a05113fb61ebbc95ded15fcfe374c0217).

## Field Documentation

## [◆ ](#aa9d8920782b1a024b70970d60886deff)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* i3c\_msg::buf |
| --- |

Data buffer in bytes.

## [◆ ](#a05113fb61ebbc95ded15fcfe374c0217)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_msg::flags |
| --- |

Flags for this message.

## [◆ ](#a53f5ef80b2cf467e9ff557be7cc568c9)hdr\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_msg::hdr\_mode |
| --- |

HDR mode (`I3C_MSG_HDR_MODE*`) for transfer if any `I3C_MSG_HDR_*` is set in `flags`.

Use SDR mode if none is set.

## [◆ ](#ada6582cdd126f36e64f17f66ae3817f0)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3c\_msg::len |
| --- |

Length of buffer in bytes.

## [◆ ](#a572d9f55461561fb9a8c31e46f0ebfe5)num\_xfer

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3c\_msg::num\_xfer |
| --- |

Total number of bytes transferred.

A Target can issue an EoD or the Controller can abort a transfer before the length of the buffer. It is expected for the driver to write to this after the transfer.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_msg](structi3c__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
