---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__eth__errors.html
original_path: doxygen/html/structnet__stats__eth__errors.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_eth\_errors Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Ethernet error statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_length\_errors](#aca0e2e4807fa70279dee8ddaad2d7ef7) |
|  | Number of RX length errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_over\_errors](#a9afee89f5bb01907e7cd515e2a0ff1b5) |
|  | Number of RX overrun errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_crc\_errors](#a4dab70cf219269bb393ce14faf0ed77e) |
|  | Number of RX CRC errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_frame\_errors](#a8dfcc5cd1b4decec5783d01ba7033b05) |
|  | Number of RX frame errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_no\_buffer\_count](#a82622736d226b4d3b999f1f22ccf8529) |
|  | Number of RX [net\_pkt](structnet__pkt.md "Network packet.") allocation errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_missed\_errors](#a2d2b2c4e3764ebec841f1ecbe7058d99) |
|  | Number of RX missed errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_long\_length\_errors](#a0e83e270a35222ed3e927800be4159e7) |
|  | Number of RX long length errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_short\_length\_errors](#a5e3d39d8417bb180cbfcb8c901006e81) |
|  | Number of RX short length errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_align\_errors](#a7618f10af3443c49a6e256bb41e77781) |
|  | Number of RX buffer align errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_dma\_failed](#a7bcfbb13836f162ceeb5f021304b5c76) |
|  | Number of RX DMA failed errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_buf\_alloc\_failed](#adbcae9c10c081f1cdf304bcdce740aa4) |
|  | Number of RX [net\_buf](structnet__buf.md "Network buffer representation.") allocation errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_aborted\_errors](#afec6a7e24c6f3cc74dd9f739f27b3e48) |
|  | Number of TX aborted errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_carrier\_errors](#a0043d1a1481040a6d7439bd23423ec12) |
|  | Number of TX carrier errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_fifo\_errors](#a84630da9b82557f56dc35cd59ca2f7ae) |
|  | Number of TX FIFO errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_heartbeat\_errors](#ae2a13733c1a5f0cc3e00efca0c3f429d) |
|  | Number of TX heartbeat errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_window\_errors](#a17624a12d6473bdd78698076fed0d122) |
|  | Number of TX window errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_dma\_failed](#abfbf6478b7afdd5935d7c6948c9ef426) |
|  | Number of TX DMA failed errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [uncorr\_ecc\_errors](#a07d0a435f2129556520c732571d28edf) |
|  | Number of uncorrected ECC errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [corr\_ecc\_errors](#a257113639f0e0e3085febb7a147f498f) |
|  | Number of corrected ECC errors. |

## Detailed Description

Ethernet error statistics.

## Field Documentation

## [◆ ](#a257113639f0e0e3085febb7a147f498f)corr\_ecc\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::corr\_ecc\_errors |
| --- |

Number of corrected ECC errors.

## [◆ ](#a7618f10af3443c49a6e256bb41e77781)rx\_align\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_align\_errors |
| --- |

Number of RX buffer align errors.

## [◆ ](#adbcae9c10c081f1cdf304bcdce740aa4)rx\_buf\_alloc\_failed

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_buf\_alloc\_failed |
| --- |

Number of RX [net\_buf](structnet__buf.md "Network buffer representation.") allocation errors.

## [◆ ](#a4dab70cf219269bb393ce14faf0ed77e)rx\_crc\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_crc\_errors |
| --- |

Number of RX CRC errors.

## [◆ ](#a7bcfbb13836f162ceeb5f021304b5c76)rx\_dma\_failed

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_dma\_failed |
| --- |

Number of RX DMA failed errors.

## [◆ ](#a8dfcc5cd1b4decec5783d01ba7033b05)rx\_frame\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_frame\_errors |
| --- |

Number of RX frame errors.

## [◆ ](#aca0e2e4807fa70279dee8ddaad2d7ef7)rx\_length\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_length\_errors |
| --- |

Number of RX length errors.

## [◆ ](#a0e83e270a35222ed3e927800be4159e7)rx\_long\_length\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_long\_length\_errors |
| --- |

Number of RX long length errors.

## [◆ ](#a2d2b2c4e3764ebec841f1ecbe7058d99)rx\_missed\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_missed\_errors |
| --- |

Number of RX missed errors.

## [◆ ](#a82622736d226b4d3b999f1f22ccf8529)rx\_no\_buffer\_count

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_no\_buffer\_count |
| --- |

Number of RX [net\_pkt](structnet__pkt.md "Network packet.") allocation errors.

## [◆ ](#a9afee89f5bb01907e7cd515e2a0ff1b5)rx\_over\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_over\_errors |
| --- |

Number of RX overrun errors.

## [◆ ](#a5e3d39d8417bb180cbfcb8c901006e81)rx\_short\_length\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::rx\_short\_length\_errors |
| --- |

Number of RX short length errors.

## [◆ ](#afec6a7e24c6f3cc74dd9f739f27b3e48)tx\_aborted\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::tx\_aborted\_errors |
| --- |

Number of TX aborted errors.

## [◆ ](#a0043d1a1481040a6d7439bd23423ec12)tx\_carrier\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::tx\_carrier\_errors |
| --- |

Number of TX carrier errors.

## [◆ ](#abfbf6478b7afdd5935d7c6948c9ef426)tx\_dma\_failed

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::tx\_dma\_failed |
| --- |

Number of TX DMA failed errors.

## [◆ ](#a84630da9b82557f56dc35cd59ca2f7ae)tx\_fifo\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::tx\_fifo\_errors |
| --- |

Number of TX FIFO errors.

## [◆ ](#ae2a13733c1a5f0cc3e00efca0c3f429d)tx\_heartbeat\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::tx\_heartbeat\_errors |
| --- |

Number of TX heartbeat errors.

## [◆ ](#a17624a12d6473bdd78698076fed0d122)tx\_window\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::tx\_window\_errors |
| --- |

Number of TX window errors.

## [◆ ](#a07d0a435f2129556520c732571d28edf)uncorr\_ecc\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_errors::uncorr\_ecc\_errors |
| --- |

Number of uncorrected ECC errors.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_eth\_errors](structnet__stats__eth__errors.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
