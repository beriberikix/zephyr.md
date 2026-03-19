---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/syscon_8h.html
original_path: doxygen/html/syscon_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscon.h File Reference

Public SYSCON driver APIs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/syscon.h>`

[Go to the source code of this file.](syscon_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [syscon\_driver\_api](structsyscon__driver__api.md) |
|  | System Control (syscon) register driver API. [More...](structsyscon__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [syscon\_api\_get\_base](group__syscon__interface.md#ga51cf97235e40c0fa63d5c91fcee62819)) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr) |
|  | API template to get the base address of the syscon region. |
| typedef int(\* | [syscon\_api\_read\_reg](group__syscon__interface.md#gab23dbb591174dcb5944ce534c851eea8)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | API template to read a single register. |
| typedef int(\* | [syscon\_api\_write\_reg](group__syscon__interface.md#ga1939885e191dbf49ef1698425085ee56)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | API template to write a single register. |
| typedef int(\* | [syscon\_api\_get\_size](group__syscon__interface.md#gae09207fe29a18f32f9e52a77c8c1695f)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | API template to get the size of the syscon register. |

| Functions | |
| --- | --- |
| int | [syscon\_get\_base](group__syscon__interface.md#ga14c9c3bb09cec4c297a22f1ec751ceff) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr) |
|  | Get the syscon base address. |
| int | [syscon\_read\_reg](group__syscon__interface.md#ga2b912d694cce403011212b83e98a7426) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Read from syscon register. |
| int | [syscon\_write\_reg](group__syscon__interface.md#gad38b74cf372f8cdeb0439d6524af7da8) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Write to syscon register. |
| int | [syscon\_get\_size](group__syscon__interface.md#ga431adee943fe536fc0c4abe7e169bdf5) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Get the size of the syscon register in bytes. |

## Detailed Description

Public SYSCON driver APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [syscon.h](syscon_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
