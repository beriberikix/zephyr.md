---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structzperf__results.html
original_path: doxygen/html/structzperf__results.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zperf\_results Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Zperf API](group__zperf.md)

Performance results.
[More...](#details)

`#include <[zperf.h](zperf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nb\_packets\_sent](#adfd2738991c8bea53f20079421da6d96) |
|  | Number of packets sent. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nb\_packets\_rcvd](#acf312d831d8e6707f7e769da92f8eb70) |
|  | Number of packets received. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nb\_packets\_lost](#ac9ad68ef3b6081b64f290720ad9b5bc8) |
|  | Number of packets lost. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nb\_packets\_outorder](#aa1e3c86bcab447bc888bba0bbaa057d1) |
|  | Number of packets out of order. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [total\_len](#a517ba180a6414a2f2d1484e698d57650) |
|  | Total length of the transferred data. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [time\_in\_us](#aafb7f2c221c91c59ab0d6936ebc6ce2a) |
|  | Total time of the transfer in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [jitter\_in\_us](#af4a5ce512fb37ddae8e2c12a0b67c3a2) |
|  | Jitter in microseconds. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [client\_time\_in\_us](#a550158fd641799c2a6b2d25617ac9a6c) |
|  | Client connection time in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [packet\_size](#a8aedf97a8eeace1f4b9cda7e07e17e28) |
|  | Packet size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nb\_packets\_errors](#a5fcccf6747c449418c246ac1d945a1f8) |
|  | Number of packet errors. |

## Detailed Description

Performance results.

## Field Documentation

## [◆ ](#a550158fd641799c2a6b2d25617ac9a6c)client\_time\_in\_us

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) zperf\_results::client\_time\_in\_us |
| --- |

Client connection time in microseconds.

## [◆ ](#af4a5ce512fb37ddae8e2c12a0b67c3a2)jitter\_in\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_results::jitter\_in\_us |
| --- |

Jitter in microseconds.

## [◆ ](#a5fcccf6747c449418c246ac1d945a1f8)nb\_packets\_errors

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_results::nb\_packets\_errors |
| --- |

Number of packet errors.

## [◆ ](#ac9ad68ef3b6081b64f290720ad9b5bc8)nb\_packets\_lost

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_results::nb\_packets\_lost |
| --- |

Number of packets lost.

## [◆ ](#aa1e3c86bcab447bc888bba0bbaa057d1)nb\_packets\_outorder

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_results::nb\_packets\_outorder |
| --- |

Number of packets out of order.

## [◆ ](#acf312d831d8e6707f7e769da92f8eb70)nb\_packets\_rcvd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_results::nb\_packets\_rcvd |
| --- |

Number of packets received.

## [◆ ](#adfd2738991c8bea53f20079421da6d96)nb\_packets\_sent

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_results::nb\_packets\_sent |
| --- |

Number of packets sent.

## [◆ ](#a8aedf97a8eeace1f4b9cda7e07e17e28)packet\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zperf\_results::packet\_size |
| --- |

Packet size.

## [◆ ](#aafb7f2c221c91c59ab0d6936ebc6ce2a)time\_in\_us

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) zperf\_results::time\_in\_us |
| --- |

Total time of the transfer in microseconds.

## [◆ ](#a517ba180a6414a2f2d1484e698d57650)total\_len

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) zperf\_results::total\_len |
| --- |

Total length of the transferred data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[zperf.h](zperf_8h_source.md)

- [zperf\_results](structzperf__results.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
