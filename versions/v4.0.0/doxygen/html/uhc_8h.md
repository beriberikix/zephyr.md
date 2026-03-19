---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/uhc_8h.html
original_path: doxygen/html/uhc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uhc.h File Reference

USB host controller (UHC) driver API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/usb/usb_ch9.h](usb__ch9_8h_source.md)>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`

[Go to the source code of this file.](uhc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uhc\_transfer](structuhc__transfer.md) |
|  | UHC endpoint buffer info. [More...](structuhc__transfer.md#details) |
| struct | [uhc\_event](structuhc__event.md) |
|  | USB host controller event. [More...](structuhc__event.md#details) |
| struct | [uhc\_device\_caps](structuhc__device__caps.md) |
|  | USB host controller capabilities. [More...](structuhc__device__caps.md#details) |
| struct | [uhc\_data](structuhc__data.md) |
|  | Common UHC driver data structure. [More...](structuhc__data.md#details) |

| Macros | |
| --- | --- |
| #define | [UHC\_STATUS\_INITIALIZED](group__uhc__api.md#ga09ad6fc9251212fa0dffececb767ff9e)   0 |
|  | Controller is initialized by [uhc\_init()](group__uhc__api.md#gabfee9100a18fdf67c5d4f8f99928d530 "Initialize USB host controller."). |
| #define | [UHC\_STATUS\_ENABLED](group__uhc__api.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)   1 |
|  | Controller is enabled and all API functions are available. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9)) (const struct [device](structdevice.md) \*dev, const struct [uhc\_event](structuhc__event.md) \*const event) |
|  | Callback to submit UHC event to higher layer. |

| Enumerations | |
| --- | --- |
| enum | [uhc\_control\_stage](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8) { [UHC\_CONTROL\_STAGE\_SETUP](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8) = 0 , [UHC\_CONTROL\_STAGE\_DATA](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5) , [UHC\_CONTROL\_STAGE\_STATUS](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f) } |
|  | USB control transfer stage. [More...](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8) |
| enum | [uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) {     [UHC\_EVT\_DEV\_CONNECTED\_LS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70) , [UHC\_EVT\_DEV\_CONNECTED\_FS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce) , [UHC\_EVT\_DEV\_CONNECTED\_HS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f) , [UHC\_EVT\_DEV\_REMOVED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30) ,     [UHC\_EVT\_RESETED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3) , [UHC\_EVT\_SUSPENDED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a) , [UHC\_EVT\_RESUMED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848) , [UHC\_EVT\_RWUP](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e) ,     [UHC\_EVT\_EP\_REQUEST](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483) , [UHC\_EVT\_ERROR](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)   } |
|  | USB host controller event types. [More...](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [uhc\_is\_initialized](group__uhc__api.md#ga3251967d36b67169d7892a615323c14e) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is initialized. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [uhc\_is\_enabled](group__uhc__api.md#ga09b71dc5c334f09fb92cf37e2ecf51eb) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is enabled. |
| static int | [uhc\_bus\_reset](group__uhc__api.md#ga4ceb0400168cd53201f0dde5f596452f) (const struct [device](structdevice.md) \*dev) |
|  | Reset USB bus. |
| static int | [uhc\_sof\_enable](group__uhc__api.md#gafe55e97cbf31d163b10616c03da39414) (const struct [device](structdevice.md) \*dev) |
|  | Enable Start of Frame generator. |
| static int | [uhc\_bus\_suspend](group__uhc__api.md#ga897081ff02dab4377c68bcba343f492c) (const struct [device](structdevice.md) \*dev) |
|  | Suspend USB bus. |
| static int | [uhc\_bus\_resume](group__uhc__api.md#ga6669bc2ac56395b38292fa796b99bfd9) (const struct [device](structdevice.md) \*dev) |
|  | Resume USB bus. |
| struct [uhc\_transfer](structuhc__transfer.md) \* | [uhc\_xfer\_alloc](group__uhc__api.md#ga14a5d093d97fc19c7d8e9ec9f0330eaa) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attrib, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout, void \*const udev, void \*const cb) |
|  | Allocate UHC transfer. |
| struct [uhc\_transfer](structuhc__transfer.md) \* | [uhc\_xfer\_alloc\_with\_buf](group__uhc__api.md#ga520161e0e390c94b9c745edc83b32816) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attrib, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout, void \*const udev, void \*const cb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate UHC transfer with buffer. |
| int | [uhc\_xfer\_free](group__uhc__api.md#gab2f6328e8051559edccc05ae3552f4f9) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer) |
|  | Free UHC transfer and any buffers. |
| int | [uhc\_xfer\_buf\_add](group__uhc__api.md#ga779dbd7ee8ac5fce487e087706791ea7) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Add UHC transfer buffer. |
| struct [net\_buf](structnet__buf.md) \* | [uhc\_xfer\_buf\_alloc](group__uhc__api.md#gab4f7439fab8c57e203862bc408a6e46b) (const struct [device](structdevice.md) \*dev, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate UHC transfer buffer. |
| void | [uhc\_xfer\_buf\_free](group__uhc__api.md#gac4bd26a85f8abc2006ecf2622669d615) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Free UHC request buffer. |
| int | [uhc\_ep\_enqueue](group__uhc__api.md#ga7a07b598c00d53393e15f6dae5cf1c4a) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer) |
|  | Queue USB host controller transfer. |
| int | [uhc\_ep\_dequeue](group__uhc__api.md#ga7c362cba29e0181ffcc8f70060100e62) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer) |
|  | Remove a USB host controller transfers from queue. |
| int | [uhc\_init](group__uhc__api.md#gabfee9100a18fdf67c5d4f8f99928d530) (const struct [device](structdevice.md) \*dev, [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9) event\_cb) |
|  | Initialize USB host controller. |
| int | [uhc\_enable](group__uhc__api.md#gafe94b7f9e32aada9634166ebb2115c2f) (const struct [device](structdevice.md) \*dev) |
|  | Enable USB host controller. |
| int | [uhc\_disable](group__uhc__api.md#ga9ec92df4497588adbf8da6f0777a4afd) (const struct [device](structdevice.md) \*dev) |
|  | Disable USB host controller. |
| int | [uhc\_shutdown](group__uhc__api.md#gac6d1feb9481882a711e58c3e55e915cb) (const struct [device](structdevice.md) \*dev) |
|  | Poweroff USB host controller. |
| static struct [uhc\_device\_caps](structuhc__device__caps.md) | [uhc\_caps](group__uhc__api.md#ga8796569eba96260ce332e611fb520033) (const struct [device](structdevice.md) \*dev) |
|  | Get USB host controller capabilities. |

## Detailed Description

USB host controller (UHC) driver API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [uhc.h](uhc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
