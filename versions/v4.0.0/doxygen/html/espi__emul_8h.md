---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/espi__emul_8h.html
original_path: doxygen/html/espi__emul_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_emul.h File Reference

Public APIs for the eSPI emulation drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[zephyr/drivers/espi.h](espi_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](espi__emul_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [emul\_espi\_device\_api](structemul__espi__device__api.md) |
|  | Definition of the eSPI device emulator API. [More...](structemul__espi__device__api.md#details) |
| struct | [espi\_emul](structespi__emul.md) |
|  | Node in a linked list of emulators for eSPI devices. [More...](structespi__emul.md#details) |
| struct | [emul\_espi\_driver\_api](structemul__espi__driver__api.md) |
|  | Definition of the eSPI controller emulator API. [More...](structemul__espi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [EMUL\_ESPI\_HOST\_CHIPSEL](group__espi__emul__interface.md#ga18fb55455f95a7f7ba93fdc49de2b9c0)   0 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [emul\_espi\_api\_set\_vw](group__espi__emul__interface.md#gab1068f48bf931fbc86668fb9108e07c7)) (const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Passes eSPI virtual wires set request (virtual wire packet) to the emulator. |
| typedef int(\* | [emul\_espi\_api\_get\_vw](group__espi__emul__interface.md#ga06c214788ceff221e776394318517f91)) (const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level) |
|  | Passes eSPI virtual wires get request (virtual wire packet) to the emulator. |
| typedef struct [espi\_emul](structespi__emul.md) \*(\* | [emul\_find\_emul](group__espi__emul__interface.md#gaa9e27e6a744a73a13415e01fa2c09bca)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chipsel) |
|  | Find an emulator present on a eSPI bus. |
| typedef int(\* | [emul\_trigger\_event](group__espi__emul__interface.md#ga2abff7d857738254cc4a8a939264924f)) (const struct [device](structdevice.md) \*dev, struct [espi\_event](structespi__event.md) \*evt) |
|  | Triggers an event on the emulator of eSPI controller side which causes calling specific callbacks. |

| Functions | |
| --- | --- |
| int | [espi\_emul\_register](group__espi__emul__interface.md#gaaccb8ef6060c0477151001af52310769) (const struct [device](structdevice.md) \*dev, struct [espi\_emul](structespi__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |
| int | [emul\_espi\_host\_send\_vw](group__espi__emul__interface.md#ga67deaf77a17682671ec28488ed3113fc) (const struct [device](structdevice.md) \*espi\_dev, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Sets the eSPI virtual wire on the host side, which will trigger a proper event(and callbacks) on the emulated eSPI controller. |
| int | [emul\_espi\_host\_port80\_write](group__espi__emul__interface.md#ga16c67d1d52f94b7062144e2c2f45d15a) (const struct [device](structdevice.md) \*espi\_dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Perform port80 write on the emulated host side, which will trigger a proper event(and callbacks) on the emulated eSPI controller. |

## Detailed Description

Public APIs for the eSPI emulation drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [espi\_emul.h](espi__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
