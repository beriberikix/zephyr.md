---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mspi__emul_8h.html
original_path: doxygen/html/mspi__emul_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_emul.h File Reference

Public APIs for the MSPI emulation drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[zephyr/drivers/mspi.h](mspi_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](mspi__emul_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [emul\_mspi\_device\_api](structemul__mspi__device__api.md) |
|  | Definition of the MSPI device emulator API. [More...](structemul__mspi__device__api.md#details) |
| struct | [mspi\_emul](structmspi__emul.md) |
|  | Node in a linked list of emulators for MSPI devices. [More...](structmspi__emul.md#details) |
| struct | [emul\_mspi\_driver\_api](structemul__mspi__driver__api.md) |
|  | Definition of the MSPI controller emulator API. [More...](structemul__mspi__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef struct [mspi\_emul](structmspi__emul.md) \*(\* | [mspi\_emul\_find\_emul](group__mspi__emul__interface.md#gabecb33236ed3a6a93a28edef0a4c3ae7)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_idx) |
|  | Find an emulator present on a MSPI bus. |
| typedef int(\* | [mspi\_emul\_trigger\_event](group__mspi__emul__interface.md#gaaa0c99ea6582cacba89f8630d8d554be)) (const struct [device](structdevice.md) \*dev, enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type) |
|  | Triggers an event on the emulator of MSPI controller side which causes calling specific callbacks. |
| typedef int(\* | [emul\_mspi\_dev\_api\_transceive](group__mspi__emul__interface.md#ga15df8cc9ccc2831c5446002e864f1717)) (const struct [emul](structemul.md) \*target, const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \*packets, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_packet, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) async, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout) |
|  | Loopback MSPI transceive request to the device emulator as no real hardware attached. |

| Functions | |
| --- | --- |
| int | [mspi\_emul\_register](group__mspi__emul__interface.md#ga98c9a359f3385f49fbfe52b27254d261) (const struct [device](structdevice.md) \*dev, struct [mspi\_emul](structmspi__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |

## Detailed Description

Public APIs for the MSPI emulation drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mspi\_emul.h](mspi__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
