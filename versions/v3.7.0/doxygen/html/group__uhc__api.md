---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__uhc__api.html
original_path: doxygen/html/group__uhc__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB host controller driver API

[Device Driver APIs](group__io__interfaces.md)

USB host controller (UHC) driver API.
[More...](#details)

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
| #define | [UHC\_STATUS\_INITIALIZED](#ga09ad6fc9251212fa0dffececb767ff9e)   0 |
|  | Controller is initialized by [uhc\_init()](#gabfee9100a18fdf67c5d4f8f99928d530). |
| #define | [UHC\_STATUS\_ENABLED](#ga230e104bd7be1d4b83b2d31ee72ac3c4)   1 |
|  | Controller is enabled and all API functions are available. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [uhc\_event\_cb\_t](#ga3cda056094ceef79dd62ad9c6852daf9)) (const struct [device](structdevice.md) \*dev, const struct [uhc\_event](structuhc__event.md) \*const event) |
|  | Callback to submit UHC event to higher layer. |

| Enumerations | |
| --- | --- |
| enum | [uhc\_control\_stage](#gaef9b0703714676c1f7bd1cad57f49bc8) { [UHC\_CONTROL\_STAGE\_SETUP](#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8) = 0 , [UHC\_CONTROL\_STAGE\_DATA](#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5) , [UHC\_CONTROL\_STAGE\_STATUS](#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f) } |
|  | USB control transfer stage. [More...](#gaef9b0703714676c1f7bd1cad57f49bc8) |
| enum | [uhc\_event\_type](#gabaf69c1e69fe0fb3d912b92daf8754eb) {     [UHC\_EVT\_DEV\_CONNECTED\_LS](#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70) , [UHC\_EVT\_DEV\_CONNECTED\_FS](#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce) , [UHC\_EVT\_DEV\_CONNECTED\_HS](#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f) , [UHC\_EVT\_DEV\_REMOVED](#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30) ,     [UHC\_EVT\_RESETED](#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3) , [UHC\_EVT\_SUSPENDED](#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a) , [UHC\_EVT\_RESUMED](#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848) , [UHC\_EVT\_RWUP](#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e) ,     [UHC\_EVT\_EP\_REQUEST](#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483) , [UHC\_EVT\_ERROR](#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)   } |
|  | USB host controller event types. [More...](#gabaf69c1e69fe0fb3d912b92daf8754eb) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [uhc\_is\_initialized](#ga3251967d36b67169d7892a615323c14e) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is initialized. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [uhc\_is\_enabled](#ga09b71dc5c334f09fb92cf37e2ecf51eb) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is enabled. |
| static int | [uhc\_bus\_reset](#ga4ceb0400168cd53201f0dde5f596452f) (const struct [device](structdevice.md) \*dev) |
|  | Reset USB bus. |
| static int | [uhc\_sof\_enable](#gafe55e97cbf31d163b10616c03da39414) (const struct [device](structdevice.md) \*dev) |
|  | Enable Start of Frame generator. |
| static int | [uhc\_bus\_suspend](#ga897081ff02dab4377c68bcba343f492c) (const struct [device](structdevice.md) \*dev) |
|  | Suspend USB bus. |
| static int | [uhc\_bus\_resume](#ga6669bc2ac56395b38292fa796b99bfd9) (const struct [device](structdevice.md) \*dev) |
|  | Resume USB bus. |
| struct [uhc\_transfer](structuhc__transfer.md) \* | [uhc\_xfer\_alloc](#ga14a5d093d97fc19c7d8e9ec9f0330eaa) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attrib, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout, void \*const udev, void \*const cb) |
|  | Allocate UHC transfer. |
| struct [uhc\_transfer](structuhc__transfer.md) \* | [uhc\_xfer\_alloc\_with\_buf](#ga520161e0e390c94b9c745edc83b32816) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attrib, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout, void \*const udev, void \*const cb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate UHC transfer with buffer. |
| int | [uhc\_xfer\_free](#gab2f6328e8051559edccc05ae3552f4f9) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer) |
|  | Free UHC transfer and any buffers. |
| int | [uhc\_xfer\_buf\_add](#ga779dbd7ee8ac5fce487e087706791ea7) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Add UHC transfer buffer. |
| struct [net\_buf](structnet__buf.md) \* | [uhc\_xfer\_buf\_alloc](#gab4f7439fab8c57e203862bc408a6e46b) (const struct [device](structdevice.md) \*dev, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate UHC transfer buffer. |
| void | [uhc\_xfer\_buf\_free](#gac4bd26a85f8abc2006ecf2622669d615) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Free UHC request buffer. |
| int | [uhc\_ep\_enqueue](#ga7a07b598c00d53393e15f6dae5cf1c4a) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer) |
|  | Queue USB host controller transfer. |
| int | [uhc\_ep\_dequeue](#ga7c362cba29e0181ffcc8f70060100e62) (const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer) |
|  | Remove a USB host controller transfers from queue. |
| int | [uhc\_init](#gabfee9100a18fdf67c5d4f8f99928d530) (const struct [device](structdevice.md) \*dev, [uhc\_event\_cb\_t](#ga3cda056094ceef79dd62ad9c6852daf9) event\_cb) |
|  | Initialize USB host controller. |
| int | [uhc\_enable](#gafe94b7f9e32aada9634166ebb2115c2f) (const struct [device](structdevice.md) \*dev) |
|  | Enable USB host controller. |
| int | [uhc\_disable](#ga9ec92df4497588adbf8da6f0777a4afd) (const struct [device](structdevice.md) \*dev) |
|  | Disable USB host controller. |
| int | [uhc\_shutdown](#gac6d1feb9481882a711e58c3e55e915cb) (const struct [device](structdevice.md) \*dev) |
|  | Poweroff USB host controller. |
| static struct [uhc\_device\_caps](structuhc__device__caps.md) | [uhc\_caps](#ga8796569eba96260ce332e611fb520033) (const struct [device](structdevice.md) \*dev) |
|  | Get USB host controller capabilities. |

## Detailed Description

USB host controller (UHC) driver API.

## Macro Definition Documentation

## [◆ ](#ga230e104bd7be1d4b83b2d31ee72ac3c4)UHC\_STATUS\_ENABLED

| #define UHC\_STATUS\_ENABLED   1 |
| --- |

`#include <[uhc.h](uhc_8h.md)>`

Controller is enabled and all API functions are available.

## [◆ ](#ga09ad6fc9251212fa0dffececb767ff9e)UHC\_STATUS\_INITIALIZED

| #define UHC\_STATUS\_INITIALIZED   0 |
| --- |

`#include <[uhc.h](uhc_8h.md)>`

Controller is initialized by [uhc\_init()](#gabfee9100a18fdf67c5d4f8f99928d530).

## Typedef Documentation

## [◆ ](#ga3cda056094ceef79dd62ad9c6852daf9)uhc\_event\_cb\_t

| typedef int(\* uhc\_event\_cb\_t) (const struct [device](structdevice.md) \*dev, const struct [uhc\_event](structuhc__event.md) \*const event) |
| --- |

`#include <[uhc.h](uhc_8h.md)>`

Callback to submit UHC event to higher layer.

At the higher level, the event is to be inserted into a message queue.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | event | Point to event structure |

Returns
:   0 on success, all other values should be treated as error.

## Enumeration Type Documentation

## [◆ ](#gaef9b0703714676c1f7bd1cad57f49bc8)uhc\_control\_stage

| enum [uhc\_control\_stage](#gaef9b0703714676c1f7bd1cad57f49bc8) |
| --- |

`#include <[uhc.h](uhc_8h.md)>`

USB control transfer stage.

| Enumerator | |
| --- | --- |
| UHC\_CONTROL\_STAGE\_SETUP |  |
| UHC\_CONTROL\_STAGE\_DATA |  |
| UHC\_CONTROL\_STAGE\_STATUS |  |

## [◆ ](#gabaf69c1e69fe0fb3d912b92daf8754eb)uhc\_event\_type

| enum [uhc\_event\_type](#gabaf69c1e69fe0fb3d912b92daf8754eb) |
| --- |

`#include <[uhc.h](uhc_8h.md)>`

USB host controller event types.

| Enumerator | |
| --- | --- |
| UHC\_EVT\_DEV\_CONNECTED\_LS | Low speed device connected. |
| UHC\_EVT\_DEV\_CONNECTED\_FS | Full speed device connected. |
| UHC\_EVT\_DEV\_CONNECTED\_HS | High speed device connected. |
| UHC\_EVT\_DEV\_REMOVED | Device (peripheral) removed. |
| UHC\_EVT\_RESETED | Bus reset operation finished. |
| UHC\_EVT\_SUSPENDED | Bus suspend operation finished. |
| UHC\_EVT\_RESUMED | Bus resume operation finished. |
| UHC\_EVT\_RWUP | Remote wakeup signal. |
| UHC\_EVT\_EP\_REQUEST | Endpoint request result event. |
| UHC\_EVT\_ERROR | Non-correctable error event, requires attention from higher levels or application. |

## Function Documentation

## [◆ ](#ga4ceb0400168cd53201f0dde5f596452f)uhc\_bus\_reset()

| | int uhc\_bus\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Reset USB bus.

Perform USB bus reset, controller may emit UHC\_EVT\_RESETED at the end of reset signaling.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EBUSY | if the controller is already performing a bus operation |
    | --- | --- |

## [◆ ](#ga6669bc2ac56395b38292fa796b99bfd9)uhc\_bus\_resume()

| | int uhc\_bus\_resume | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Resume USB bus.

Signal resume for at least 20ms, emit UHC\_EVT\_RESUMED at the end of USB bus resume signaling. The SoF generator should subsequently start within 3ms.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EBUSY | if the controller is already performing a bus operation |
    | --- | --- |

## [◆ ](#ga897081ff02dab4377c68bcba343f492c)uhc\_bus\_suspend()

| | int uhc\_bus\_suspend | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Suspend USB bus.

Disable SOF generator and emit UHC\_EVT\_SUSPENDED event when USB bus is suspended.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EALREADY | if already suspended |
    | --- | --- |

## [◆ ](#ga8796569eba96260ce332e611fb520033)uhc\_caps()

| | struct [uhc\_device\_caps](structuhc__device__caps.md) uhc\_caps | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Get USB host controller capabilities.

Obtain the capabilities of the controller such as high speed (HS), and more.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   USB host controller capabilities.

## [◆ ](#ga9ec92df4497588adbf8da6f0777a4afd)uhc\_disable()

| int uhc\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Disable USB host controller.

Disable enabled USB host controller.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EALREADY | already disabled |
    | --- | --- |

## [◆ ](#gafe94b7f9e32aada9634166ebb2115c2f)uhc\_enable()

| int uhc\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Enable USB host controller.

Enable powered USB host controller and allow host stack to recognize and enumerate devices.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EPERM | controller is not initialized |
    | --- | --- |
    | -EALREADY | already enabled |

## [◆ ](#ga7c362cba29e0181ffcc8f70060100e62)uhc\_ep\_dequeue()

| int uhc\_ep\_dequeue | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [uhc\_transfer](structuhc__transfer.md) \*const | *xfer* ) |

`#include <[uhc.h](uhc_8h.md)>`

Remove a USB host controller transfers from queue.

Not implemented yet.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | xfer | Pointer to UHC transfer |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EPERM | controller is not initialized |
    | --- | --- |

## [◆ ](#ga7a07b598c00d53393e15f6dae5cf1c4a)uhc\_ep\_enqueue()

| int uhc\_ep\_enqueue | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [uhc\_transfer](structuhc__transfer.md) \*const | *xfer* ) |

`#include <[uhc.h](uhc_8h.md)>`

Queue USB host controller transfer.

Add transfer to the queue. If the queue is empty, the transfer can be claimed by the controller immediately.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | xfer | Pointer to UHC transfer |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EPERM | controller is not initialized |
    | --- | --- |

## [◆ ](#gabfee9100a18fdf67c5d4f8f99928d530)uhc\_init()

| int uhc\_init | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uhc\_event\_cb\_t](#ga3cda056094ceef79dd62ad9c6852daf9) | *event\_cb* ) |

`#include <[uhc.h](uhc_8h.md)>`

Initialize USB host controller.

Initialize USB host controller.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | event\_cb | Event callback from the higher layer (USB host stack) |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EINVAL | on parameter error (no callback is passed) |
    | --- | --- |
    | -EALREADY | already initialized |

## [◆ ](#ga09b71dc5c334f09fb92cf37e2ecf51eb)uhc\_is\_enabled()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) uhc\_is\_enabled | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Checks whether the controller is enabled.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   true if controller is enabled, false otherwise

## [◆ ](#ga3251967d36b67169d7892a615323c14e)uhc\_is\_initialized()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) uhc\_is\_initialized | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Checks whether the controller is initialized.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   true if controller is initialized, false otherwise

## [◆ ](#gac6d1feb9481882a711e58c3e55e915cb)uhc\_shutdown()

| int uhc\_shutdown | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Poweroff USB host controller.

Shut down the controller completely to reduce energy consumption or to change the role of the controller.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EALREADY | controller is already uninitialized |
    | --- | --- |

## [◆ ](#gafe55e97cbf31d163b10616c03da39414)uhc\_sof\_enable()

| | int uhc\_sof\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uhc.h](uhc_8h.md)>`

Enable Start of Frame generator.

Enable SOF generator.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EALREADY | if already enabled |
    | --- | --- |

## [◆ ](#ga14a5d093d97fc19c7d8e9ec9f0330eaa)uhc\_xfer\_alloc()

| struct [uhc\_transfer](structuhc__transfer.md) \* uhc\_xfer\_alloc | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attrib*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mps*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *timeout*, |
|  |  | void \*const | *udev*, |
|  |  | void \*const | *cb* ) |

`#include <[uhc.h](uhc_8h.md)>`

Allocate UHC transfer.

Allocate a new transfer from common transfer pool. Transfer has no buffer after allocation, but can be allocated and added from different pools.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | addr | Device (peripheral) address |
    | [in] | ep | Endpoint address |
    | [in] | attrib | Endpoint attributes |
    | [in] | mps | Maximum packet size of the endpoint |
    | [in] | timeout | Timeout in number of frames |
    | [in] | udev | Opaque pointer to USB device |
    | [in] | cb | Transfer completion callback |

Returns
:   pointer to allocated transfer or NULL on error.

## [◆ ](#ga520161e0e390c94b9c745edc83b32816)uhc\_xfer\_alloc\_with\_buf()

| struct [uhc\_transfer](structuhc__transfer.md) \* uhc\_xfer\_alloc\_with\_buf | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attrib*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mps*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *timeout*, |
|  |  | void \*const | *udev*, |
|  |  | void \*const | *cb*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[uhc.h](uhc_8h.md)>`

Allocate UHC transfer with buffer.

Allocate a new transfer from common transfer pool with buffer.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | addr | Device (peripheral) address |
    | [in] | ep | Endpoint address |
    | [in] | attrib | Endpoint attributes |
    | [in] | mps | Maximum packet size of the endpoint |
    | [in] | timeout | Timeout in number of frames |
    | [in] | udev | Opaque pointer to USB device |
    | [in] | cb | Transfer completion callback |
    | [in] | size | Size of the buffer |

Returns
:   pointer to allocated transfer or NULL on error.

## [◆ ](#ga779dbd7ee8ac5fce487e087706791ea7)uhc\_xfer\_buf\_add()

| int uhc\_xfer\_buf\_add | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [uhc\_transfer](structuhc__transfer.md) \*const | *xfer*, |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

`#include <[uhc.h](uhc_8h.md)>`

Add UHC transfer buffer.

Add a previously allocated buffer to the transfer.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | xfer | Pointer to UHC transfer |
    | [in] | buf | Pointer to UHC request buffer |

Returns
:   pointer to allocated request or NULL on error.

## [◆ ](#gab4f7439fab8c57e203862bc408a6e46b)uhc\_xfer\_buf\_alloc()

| struct [net\_buf](structnet__buf.md) \* uhc\_xfer\_buf\_alloc | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[uhc.h](uhc_8h.md)>`

Allocate UHC transfer buffer.

Allocate a new buffer from common request buffer pool and assign it to the transfer if the xfer parameter is not NULL.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | size | Size of the request buffer |

Returns
:   pointer to allocated request or NULL on error.

## [◆ ](#gac4bd26a85f8abc2006ecf2622669d615)uhc\_xfer\_buf\_free()

| void uhc\_xfer\_buf\_free | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \*const | *buf* ) |

`#include <[uhc.h](uhc_8h.md)>`

Free UHC request buffer.

Put the buffer back into the request buffer pool.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | buf | Pointer to UHC request buffer |

## [◆ ](#gab2f6328e8051559edccc05ae3552f4f9)uhc\_xfer\_free()

| int uhc\_xfer\_free | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [uhc\_transfer](structuhc__transfer.md) \*const | *xfer* ) |

`#include <[uhc.h](uhc_8h.md)>`

Free UHC transfer and any buffers.

Free any buffers and put the transfer back into the transfer pool.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | xfer | Pointer to UHC transfer |

Returns
:   0 on success, all other values should be treated as error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
