---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/unionmipi__stp__decoder__data.html
original_path: doxygen/html/unionmipi__stp__decoder__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_stp\_decoder\_data Union Reference

[Operating System Services](group__os__services.md) » [STP Decoder API](group__mipi__stp__decoder__apis.md)

Union with data associated with a given STP opcode.
[More...](#details)

`#include <[mipi_stp_decoder.h](mipi__stp__decoder_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#a3c7d85bc475b27f570b9059745d7d11f) |
|  | ID - used for major and channel. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [freq](#a3b3cae98d63ceda950e88690da282966) |
|  | Frequency. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ver](#a3dc68ca2196c807965071d754c139655) |
|  | Version. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [err](#ace873d9e7d38a5f39338618b4d74cdf4) |
|  | Error code. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dummy](#a70db937ada38cb0f97cd45fa78bd9466) |
|  | Dummy. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [data](#a1cb5f92d1d0976f1ec047e7398e6d95d) |
|  | Data. |

## Detailed Description

Union with data associated with a given STP opcode.

## Field Documentation

## [◆ ](#a1cb5f92d1d0976f1ec047e7398e6d95d)data

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mipi\_stp\_decoder\_data::data |
| --- |

Data.

## [◆ ](#a70db937ada38cb0f97cd45fa78bd9466)dummy

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_stp\_decoder\_data::dummy |
| --- |

Dummy.

## [◆ ](#ace873d9e7d38a5f39338618b4d74cdf4)err

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_stp\_decoder\_data::err |
| --- |

Error code.

## [◆ ](#a3b3cae98d63ceda950e88690da282966)freq

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mipi\_stp\_decoder\_data::freq |
| --- |

Frequency.

## [◆ ](#a3c7d85bc475b27f570b9059745d7d11f)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mipi\_stp\_decoder\_data::id |
| --- |

ID - used for major and channel.

## [◆ ](#a3dc68ca2196c807965071d754c139655)ver

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_stp\_decoder\_data::ver |
| --- |

Version.

---

The documentation for this union was generated from the following file:

- zephyr/debug/[mipi\_stp\_decoder.h](mipi__stp__decoder_8h_source.md)

- [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
