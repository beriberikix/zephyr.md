---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__ptp__extended__time.html
original_path: doxygen/html/structnet__ptp__extended__time.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_ptp\_extended\_time Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [PTP time](group__ptp__time.md)

Generalized Precision Time Protocol Extended Timestamp format.
[More...](#details)

`#include <[ptp_time.h](ptp__time_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [second](#a97b1711e17fa229bab129da4148c3e55) |  |
| }; |  |
|  | Seconds encoded on 48 bits. |
| union { |  |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [fract\_nsecond](#a94ec079b5d38fcd12ec54baf707ec587) |  |
| }; |  |
|  | Fractional nanoseconds on 48 bits. |

## Detailed Description

Generalized Precision Time Protocol Extended Timestamp format.

This structure represents an extended timestamp according to the Generalized Precision Time Protocol standard (IEEE 802.1AS), see section 6.4.3.5.

Seconds are encoded as 48 bits unsigned integer. Fractional nanoseconds are encoded as 48 bits, their unit is 2\*(-16) ns.

A precise definition of PTP timestamps and their uses in Zephyr is given in the description of [net\_ptp\_time](structnet__ptp__time.md "net_ptp_time").

## Field Documentation

## [◆ ](#ad25464518fff96894c194dc6996472eb)[union]

| union { ... } [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) |
| --- |

Seconds encoded on 48 bits.

## [◆ ](#a99ac75beb26991d142f039067a066006)[union]

| union { ... } [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) |
| --- |

Fractional nanoseconds on 48 bits.

## [◆ ](#a94ec079b5d38fcd12ec54baf707ec587)fract\_nsecond

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_ptp\_extended\_time::fract\_nsecond |
| --- |

## [◆ ](#a3b4b8dcfa8e6aab5dd0e7ef26ad129ce)high

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_ptp\_extended\_time::high |
| --- |

## [◆ ](#a9fa067e7bb793c0eda1f30cba570a15d)low

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_ptp\_extended\_time::low |
| --- |

## [◆ ](#a97b1711e17fa229bab129da4148c3e55)second

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_ptp\_extended\_time::second |
| --- |

## [◆ ](#a20379af8395fe3afc1f6f9c45b711115)unused

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_ptp\_extended\_time::unused |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ptp\_time.h](ptp__time_8h_source.md)

- [net\_ptp\_extended\_time](structnet__ptp__extended__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
