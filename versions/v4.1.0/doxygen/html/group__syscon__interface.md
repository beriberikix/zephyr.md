---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__syscon__interface.html
original_path: doxygen/html/group__syscon__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SYSCON Interface

[Device Driver APIs](group__io__interfaces.md)

SYSCON Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [syscon\_driver\_api](structsyscon__driver__api.md) |
|  | System Control (syscon) register driver API. [More...](structsyscon__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [syscon\_api\_get\_base](#ga51cf97235e40c0fa63d5c91fcee62819)) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr) |
|  | API template to get the base address of the syscon region. |
| typedef int(\* | [syscon\_api\_read\_reg](#gab23dbb591174dcb5944ce534c851eea8)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | API template to read a single register. |
| typedef int(\* | [syscon\_api\_write\_reg](#ga1939885e191dbf49ef1698425085ee56)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | API template to write a single register. |
| typedef int(\* | [syscon\_api\_get\_size](#gae09207fe29a18f32f9e52a77c8c1695f)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | API template to get the size of the syscon register. |

| Functions | |
| --- | --- |
| int | [syscon\_get\_base](#ga14c9c3bb09cec4c297a22f1ec751ceff) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr) |
|  | Get the syscon base address. |
| int | [syscon\_read\_reg](#ga2b912d694cce403011212b83e98a7426) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Read from syscon register. |
| int | [syscon\_write\_reg](#gad38b74cf372f8cdeb0439d6524af7da8) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Write to syscon register. |
| int | [syscon\_get\_size](#ga431adee943fe536fc0c4abe7e169bdf5) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Get the size of the syscon register in bytes. |

## Detailed Description

SYSCON Interface.

## Typedef Documentation

## [◆ ](#ga51cf97235e40c0fa63d5c91fcee62819)syscon\_api\_get\_base

| typedef int(\* syscon\_api\_get\_base) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr) |
| --- |

`#include <[syscon.h](syscon_8h.md)>`

API template to get the base address of the syscon region.

See also
:   [syscon\_get\_base](#ga14c9c3bb09cec4c297a22f1ec751ceff)

## [◆ ](#gae09207fe29a18f32f9e52a77c8c1695f)syscon\_api\_get\_size

| typedef int(\* syscon\_api\_get\_size) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
| --- |

`#include <[syscon.h](syscon_8h.md)>`

API template to get the size of the syscon register.

See also
:   [syscon\_get\_size](#ga431adee943fe536fc0c4abe7e169bdf5)

## [◆ ](#gab23dbb591174dcb5944ce534c851eea8)syscon\_api\_read\_reg

| typedef int(\* syscon\_api\_read\_reg) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
| --- |

`#include <[syscon.h](syscon_8h.md)>`

API template to read a single register.

See also
:   [syscon\_read\_reg](#ga2b912d694cce403011212b83e98a7426)

## [◆ ](#ga1939885e191dbf49ef1698425085ee56)syscon\_api\_write\_reg

| typedef int(\* syscon\_api\_write\_reg) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| --- |

`#include <[syscon.h](syscon_8h.md)>`

API template to write a single register.

See also
:   [syscon\_write\_reg](#gad38b74cf372f8cdeb0439d6524af7da8)

## Function Documentation

## [◆ ](#ga14c9c3bb09cec4c297a22f1ec751ceff)syscon\_get\_base()

| int syscon\_get\_base | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *addr* ) |

`#include <[syscon.h](syscon_8h.md)>`

Get the syscon base address.

Parameters
:   | dev | The device to get the register size for. |
    | --- | --- |
    | addr | Where to write the base address. |

Returns
:   0 When addr was written to.

## [◆ ](#ga431adee943fe536fc0c4abe7e169bdf5)syscon\_get\_size()

| int syscon\_get\_size | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size* ) |

`#include <[syscon.h](syscon_8h.md)>`

Get the size of the syscon register in bytes.

Parameters
:   | dev | The device to get the register size for. |
    | --- | --- |
    | size | Pointer to write the size to. |

Returns
:   0 for success.

## [◆ ](#ga2b912d694cce403011212b83e98a7426)syscon\_read\_reg()

| int syscon\_read\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *val* ) |

`#include <[syscon.h](syscon_8h.md)>`

Read from syscon register.

This function reads from a specific register in the syscon area

Parameters
:   | dev | The device to get the register size for. |
    | --- | --- |
    | reg | The register offset |
    | val | The returned value read from the syscon register |

Returns
:   0 on success, negative on error

## [◆ ](#gad38b74cf372f8cdeb0439d6524af7da8)syscon\_write\_reg()

| int syscon\_write\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[syscon.h](syscon_8h.md)>`

Write to syscon register.

This function writes to a specific register in the syscon area

Parameters
:   | dev | The device to get the register size for. |
    | --- | --- |
    | reg | The register offset |
    | val | The value to be written in the register |

Returns
:   0 on success, negative on error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
