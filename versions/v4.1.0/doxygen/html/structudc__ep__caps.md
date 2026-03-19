---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structudc__ep__caps.html
original_path: doxygen/html/structudc__ep__caps.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_ep\_caps Struct Reference

USB device controller endpoint capabilities.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mps](#a5e90d1362855dd77a1f7ef9e0cd82ef8): 16 |
|  | Maximum packet size of the endpoint buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [control](#a98afb85c03ff01ba82d55884cea0ea31): 1 |
|  | Control transfer capable endpoint (for completeness). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interrupt](#a73f06f9e2af5770cab84d2adb76d42de): 1 |
|  | Interrupt transfer capable endpoint. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bulk](#a73ec7e7c7fd043065a7c59c89c6cc36e): 1 |
|  | Bulk transfer capable endpoint. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [iso](#a15ce10028e09b3af021a83dc36eba99a): 1 |
|  | ISO transfer capable endpoint. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [high\_bandwidth](#ad556a4c17a01bb6b8355fb6b5ea9d418): 1 |
|  | High-Bandwidth (interrupt or iso) capable endpoint. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [in](#a3a944cda429c916b60cff3a332b970a7): 1 |
|  | IN transfer capable endpoint. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [out](#afc424ee2bb31c19451facc0b79bb73c7): 1 |
|  | OUT transfer capable endpoint. |

## Detailed Description

USB device controller endpoint capabilities.

## Field Documentation

## [◆ ](#a73ec7e7c7fd043065a7c59c89c6cc36e)bulk

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::bulk |
| --- |

Bulk transfer capable endpoint.

## [◆ ](#a98afb85c03ff01ba82d55884cea0ea31)control

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::control |
| --- |

Control transfer capable endpoint (for completeness).

## [◆ ](#ad556a4c17a01bb6b8355fb6b5ea9d418)high\_bandwidth

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::high\_bandwidth |
| --- |

High-Bandwidth (interrupt or iso) capable endpoint.

## [◆ ](#a3a944cda429c916b60cff3a332b970a7)in

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::in |
| --- |

IN transfer capable endpoint.

## [◆ ](#a73f06f9e2af5770cab84d2adb76d42de)interrupt

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::interrupt |
| --- |

Interrupt transfer capable endpoint.

## [◆ ](#a15ce10028e09b3af021a83dc36eba99a)iso

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::iso |
| --- |

ISO transfer capable endpoint.

## [◆ ](#a5e90d1362855dd77a1f7ef9e0cd82ef8)mps

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::mps |
| --- |

Maximum packet size of the endpoint buffer.

## [◆ ](#afc424ee2bb31c19451facc0b79bb73c7)out

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_caps::out |
| --- |

OUT transfer capable endpoint.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_ep\_caps](structudc__ep__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
