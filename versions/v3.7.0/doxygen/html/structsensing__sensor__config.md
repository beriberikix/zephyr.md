---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensing__sensor__config.html
original_path: doxygen/html/structsensing__sensor__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_config Struct Reference

[Sensing](group__sensing.md) » [Sensing Subsystem API](group__sensing__api.md)

Sensing subsystem sensor configure, including interval, sensitivity, latency.
[More...](#details)

`#include <[sensing.h](sensing_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [sensing\_sensor\_attribute](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2) | [attri](#a9bdf50a1018d6d9426efd991d05bf72b) |
|  | Attribute of the sensor configuration. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [data\_field](#ac4389c439db16cb25a2e622baf0aeb9b) |
|  | [SENSING\_SENSITIVITY\_INDEX\_ALL](group__sensing__api.md#ga16ac7bd397836280f7e8b4aa82f8eb4c "SENSING_SENSITIVITY_INDEX_ALL") |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [interval](#a7512f7254f6960ed398150db23868965) |  |
|  | Interval between two sensor samples in microseconds (us). [More...](#a7512f7254f6960ed398150db23868965) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [sensitivity](#acc1270dbe02ff6324e0f66acbde8ce33) |  |
|  | Sensitivity threshold for reporting new data. [More...](#acc1270dbe02ff6324e0f66acbde8ce33) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [latency](#af9d2ee27b3a04fd65baa1d1d0cb2badc) |  |
|  | Maximum duration for batching sensor samples before reporting in microseconds (us). [More...](#af9d2ee27b3a04fd65baa1d1d0cb2badc) |
| }; |  |

## Detailed Description

Sensing subsystem sensor configure, including interval, sensitivity, latency.

## Field Documentation

## [◆ ](#ac6e3e46290fc929d6126f5582a8a4795)[union]

| union { ... } [sensing\_sensor\_config](structsensing__sensor__config.md) |
| --- |

## [◆ ](#a9bdf50a1018d6d9426efd991d05bf72b)attri

| enum [sensing\_sensor\_attribute](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2) sensing\_sensor\_config::attri |
| --- |

Attribute of the sensor configuration.

## [◆ ](#ac4389c439db16cb25a2e622baf0aeb9b)data\_field

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) sensing\_sensor\_config::data\_field |
| --- |

[SENSING\_SENSITIVITY\_INDEX\_ALL](group__sensing__api.md#ga16ac7bd397836280f7e8b4aa82f8eb4c "SENSING_SENSITIVITY_INDEX_ALL")

Data field of the sensor configuration.

## [◆ ](#a7512f7254f6960ed398150db23868965)interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_config::interval |
| --- |

Interval between two sensor samples in microseconds (us).

## [◆ ](#af9d2ee27b3a04fd65baa1d1d0cb2badc)latency

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sensing\_sensor\_config::latency |
| --- |

Maximum duration for batching sensor samples before reporting in microseconds (us).

This defines how long sensor samples can be accumulated before they must be reported.

## [◆ ](#acc1270dbe02ff6324e0f66acbde8ce33)sensitivity

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_config::sensitivity |
| --- |

Sensitivity threshold for reporting new data.

A new sensor sample is reported only if the difference between it and the previous sample exceeds this sensitivity value.

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing.h](sensing_8h_source.md)

- [sensing\_sensor\_config](structsensing__sensor__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
