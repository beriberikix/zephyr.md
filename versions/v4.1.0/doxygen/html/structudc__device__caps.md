---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structudc__device__caps.html
original_path: doxygen/html/structudc__device__caps.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_device\_caps Struct Reference

USB device controller capabilities.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hs](#aea376ff4a0c5a27c3b8f7d4416e17b5b): 1 |
|  | USB high speed capable controller. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rwup](#aab85e74e40876040c3d2f961c36b9780): 1 |
|  | Controller supports USB remote wakeup. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [out\_ack](#a0adada5003bccfbd6df8329198639dc0): 1 |
|  | Controller performs status OUT stage automatically. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [addr\_before\_status](#aefef262532e3eab3baa90eb8e79f9dc8): 1 |
|  | Controller expects device address to be set before status stage. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_detect\_vbus](#a7aaf6ecac2904acb5560f2f90cfef8d1): 1 |
|  | Controller can detect the state change of USB supply VBUS. |
| enum [udc\_mps0](udc_8h.md#ac254f8a970f890d14e35c43474c915fd) | [mps0](#a63affa3fe08cbaec8351297ad9d26911): 2 |
|  | Maximum packet size for control endpoint. |

## Detailed Description

USB device controller capabilities.

This structure is mainly intended for the USB device stack.

## Field Documentation

## [◆ ](#aefef262532e3eab3baa90eb8e79f9dc8)addr\_before\_status

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_device\_caps::addr\_before\_status |
| --- |

Controller expects device address to be set before status stage.

## [◆ ](#a7aaf6ecac2904acb5560f2f90cfef8d1)can\_detect\_vbus

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_device\_caps::can\_detect\_vbus |
| --- |

Controller can detect the state change of USB supply VBUS.

## [◆ ](#aea376ff4a0c5a27c3b8f7d4416e17b5b)hs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_device\_caps::hs |
| --- |

USB high speed capable controller.

## [◆ ](#a63affa3fe08cbaec8351297ad9d26911)mps0

| enum [udc\_mps0](udc_8h.md#ac254f8a970f890d14e35c43474c915fd) udc\_device\_caps::mps0 |
| --- |

Maximum packet size for control endpoint.

## [◆ ](#a0adada5003bccfbd6df8329198639dc0)out\_ack

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_device\_caps::out\_ack |
| --- |

Controller performs status OUT stage automatically.

## [◆ ](#aab85e74e40876040c3d2f961c36b9780)rwup

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_device\_caps::rwup |
| --- |

Controller supports USB remote wakeup.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_device\_caps](structudc__device__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
