---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structdevice.html
original_path: doxygen/html/structdevice.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device Struct Reference

[Device Model](group__device__model.md)

Runtime device structure (in ROM) per driver instance.
[More...](#details)

`#include <[device.h](device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a1e74e8d3b0b1a981c67e1d0284ccac3d) |
|  | Name of the device instance. |
| const void \* | [config](#aca2d801eb15996cf1c74dc65cfa651fc) |
|  | Address of device instance config information. |
| const void \* | [api](#a4a2e6a2cfeb6efed7d5383c33458f46d) |
|  | Address of the API structure exposed by the device instance. |
| struct [device\_state](structdevice__state.md) \* | [state](#abe18f600adc4ab760963928477cc944e) |
|  | Address of the common device state. |
| void \* | [data](#a27573cbd10ee145f8bb1396242b27a3e) |
|  | Address of the device instance private data. |
| const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* | [deps](#a1452f3badd041e8eccf726756700e8fe) |
|  | Optional pointer to dependencies associated with the device. |
| union { |  |
| struct [pm\_device\_base](structpm__device__base.md) \*   [pm\_base](#a05ebf64a113d562fb9328ea62cfa8f99) |  |
| struct [pm\_device](structpm__device.md) \*   [pm](#a204619a873db1b99ea31f1c190760052) |  |
| struct [pm\_device\_isr](structpm__device__isr.md) \*   [pm\_isr](#a1526ad6d863e16287de8f06dff7164dc) |  |
| }; |  |
|  | Reference to the device PM resources (only available if `CONFIG_PM_DEVICE` is enabled). |
| const struct device\_dt\_metadata \* | [dt\_meta](#adb4f64c583cbc3396d3ffe78fa0169ba) |

## Detailed Description

Runtime device structure (in ROM) per driver instance.

## Field Documentation

## [◆ ](#ac0b45f25ec699ee8c700348a2eb1ffca)[union]

| union { ... } [device](structdevice.md) |
| --- |

Reference to the device PM resources (only available if `CONFIG_PM_DEVICE` is enabled).

## [◆ ](#a4a2e6a2cfeb6efed7d5383c33458f46d)api

| const void\* device::api |
| --- |

Address of the API structure exposed by the device instance.

## [◆ ](#aca2d801eb15996cf1c74dc65cfa651fc)config

| const void\* device::config |
| --- |

Address of device instance config information.

## [◆ ](#a27573cbd10ee145f8bb1396242b27a3e)data

| void\* device::data |
| --- |

Address of the device instance private data.

## [◆ ](#a1452f3badd041e8eccf726756700e8fe)deps

| const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3)\* device::deps |
| --- |

Optional pointer to dependencies associated with the device.

This encodes a sequence of sets of device handles that have some relationship to this node. The individual sets are extracted with dedicated API, such as [device\_required\_handles\_get()](group__device__model.md#ga2157bbfc2deecfae6514f58221663618 "Get the device handles for devicetree dependencies of this device."). Only available if `CONFIG_DEVICE_DEPS` is enabled.

## [◆ ](#adb4f64c583cbc3396d3ffe78fa0169ba)dt\_meta

| const struct device\_dt\_metadata\* device::dt\_meta |
| --- |

## [◆ ](#a1e74e8d3b0b1a981c67e1d0284ccac3d)name

| const char\* device::name |
| --- |

Name of the device instance.

## [◆ ](#a204619a873db1b99ea31f1c190760052)pm

| struct [pm\_device](structpm__device.md)\* device::pm |
| --- |

## [◆ ](#a05ebf64a113d562fb9328ea62cfa8f99)pm\_base

| struct [pm\_device\_base](structpm__device__base.md)\* device::pm\_base |
| --- |

## [◆ ](#a1526ad6d863e16287de8f06dff7164dc)pm\_isr

| struct [pm\_device\_isr](structpm__device__isr.md)\* device::pm\_isr |
| --- |

## [◆ ](#abe18f600adc4ab760963928477cc944e)state

| struct [device\_state](structdevice__state.md)\* device::state |
| --- |

Address of the common device state.

---

The documentation for this struct was generated from the following file:

- zephyr/[device.h](device_8h_source.md)

- [device](structdevice.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
