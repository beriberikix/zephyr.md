---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__udc__api.html
original_path: doxygen/html/group__udc__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB device controller driver API

[Device Driver APIs](group__io__interfaces.md)

New USB device controller (UDC) driver API.
[More...](#details)

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [udc\_is\_initialized](#ga40e50cf79b40d3792513e8fea3347f59) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is initialized. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [udc\_is\_enabled](#ga2c09f2a1e89c91527a8492019089d13f) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is enabled. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [udc\_is\_suspended](#ga88786eda763fce5c2a51521650ccc9f4) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is suspended. |
| int | [udc\_init](#ga0670bec8b55c013fb607ba53a8634ad4) (const struct [device](structdevice.md) \*dev, [udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a) event\_cb, const void \*const event\_ctx) |
|  | Initialize USB device controller. |
| int | [udc\_enable](#gafbb0dec089f83fd674bd19670a882c65) (const struct [device](structdevice.md) \*dev) |
|  | Enable USB device controller. |
| int | [udc\_disable](#gaa7c2eaa52bdbe1d763b2961124570e8a) (const struct [device](structdevice.md) \*dev) |
|  | Disable USB device controller. |
| int | [udc\_shutdown](#ga59a92eb60575ca80d205cc29b4fb4f21) (const struct [device](structdevice.md) \*dev) |
|  | Poweroff USB device controller. |
| static struct [udc\_device\_caps](structudc__device__caps.md) | [udc\_caps](#ga3ee738bad8e1ee3928d32f57f82bef70) (const struct [device](structdevice.md) \*dev) |
|  | Get USB device controller capabilities. |
| enum [udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b) | [udc\_device\_speed](#gab936f04015b0fee584756bcdf40d2f50) (const struct [device](structdevice.md) \*dev) |
|  | Get actual USB device speed. |
| static int | [udc\_set\_address](#ga6feb32a2263307bdde9acc63d3c2ebb1) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Set USB device address. |
| static int | [udc\_test\_mode](#ga7f575b548833cc1e5109e0d919630b3f) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dryrun) |
|  | Enable Test Mode. |
| static int | [udc\_host\_wakeup](#ga075edc81fb3e39c2b377fc56c8c0915c) (const struct [device](structdevice.md) \*dev) |
|  | Initiate host wakeup procedure. |
| int | [udc\_ep\_try\_config](#ga81307ae4ab17ccd86be64bdf1653df0e) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attributes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const mps, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Try an endpoint configuration. |
| int | [udc\_ep\_enable](#gacc4b5c127532c994406df30bacab5684) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attributes, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Configure and enable endpoint. |
| int | [udc\_ep\_disable](#ga52da2366ac5da1a695caa8826b342cbc) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Disable endpoint. |
| int | [udc\_ep\_set\_halt](#ga19488ec4c93d81592bb5ffccfc1eadc4) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt endpoint. |
| int | [udc\_ep\_clear\_halt](#gadec9c8af89b28984028fd8e0b1a8c776) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear endpoint halt. |
| int | [udc\_ep\_enqueue](#gacb2dc96353f1cffcc3d5e9710133fc0d) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device controller request. |
| int | [udc\_ep\_dequeue](#ga6e6fb62fb8ebceca7e8e6b590c32efc2) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Remove all USB device controller requests from endpoint queue. |
| struct [net\_buf](structnet__buf.md) \* | [udc\_ep\_buf\_alloc](#gad3fb1d64b6e0cf051627011ce673bb1e) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate UDC request buffer. |
| int | [udc\_ep\_buf\_free](#gaedd615defad234b001e74448f89488e1) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Free UDC request buffer. |
| static void | [udc\_ep\_buf\_set\_zlp](#ga50f6bde28b6a5fcab6b685107570e081) (struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Set ZLP flag in requests metadata. |
| static struct [udc\_buf\_info](structudc__buf__info.md) \* | [udc\_get\_buf\_info](#ga073a51222ac639d3c70af7b57970b42a) (const struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Get requests metadata. |
| static const void \* | [udc\_get\_event\_ctx](#ga2d89f013b2e1279d1ec4cbd869e0cae6) (const struct [device](structdevice.md) \*dev) |
|  | Get pointer to higher layer context. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [udc\_mps\_ep\_size](#ga6da3d836e868f2d09fe24854c2d76aeb) (const struct [udc\_ep\_config](structudc__ep__config.md) \*const cfg) |
|  | Get endpoint size from UDC endpoint configuration. |

## Detailed Description

New USB device controller (UDC) driver API.

Since
:   3.3

Version
:   0.1.0

## Function Documentation

## [◆ ](#ga3ee738bad8e1ee3928d32f57f82bef70)udc\_caps()

| | struct [udc\_device\_caps](structudc__device__caps.md) udc\_caps | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Get USB device controller capabilities.

Obtain the capabilities of the controller such as full speed (FS), high speed (HS), and more.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   USB device controller capabilities.

## [◆ ](#gab936f04015b0fee584756bcdf40d2f50)udc\_device\_speed()

| enum [udc\_bus\_speed](udc_8h.md#a32d61ab6dbb734009102b5239a834d1b) udc\_device\_speed | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Get actual USB device speed.

The function should be called after the reset event to determine the actual bus speed.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   USB device controller capabilities.

## [◆ ](#gaa7c2eaa52bdbe1d763b2961124570e8a)udc\_disable()

| int udc\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Disable USB device controller.

Disable enabled USB device controller. The driver should continue to detect power state changes.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EALREADY | already disabled |
    | --- | --- |

## [◆ ](#gafbb0dec089f83fd674bd19670a882c65)udc\_enable()

| int udc\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Enable USB device controller.

Enable powered USB device controller and allow host to recognize and enumerate the device.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EPERM | controller is not initialized |
    | --- | --- |
    | -EALREADY | already enabled |
    | -ETIMEDOUT | enable operation timed out |

## [◆ ](#gad3fb1d64b6e0cf051627011ce673bb1e)udc\_ep\_buf\_alloc()

| struct [net\_buf](structnet__buf.md) \* udc\_ep\_buf\_alloc | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[udc.h](udc_8h.md)>`

Allocate UDC request buffer.

Allocate a new buffer from common request buffer pool.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |
    | [in] | size | Size of the request buffer |

Returns
:   pointer to allocated request or NULL on error.

## [◆ ](#gaedd615defad234b001e74448f89488e1)udc\_ep\_buf\_free()

| int udc\_ep\_buf\_free | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \*const | *buf* ) |

`#include <[udc.h](udc_8h.md)>`

Free UDC request buffer.

Put the buffer back into the request buffer pool.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | buf | Pointer to UDC request buffer |

Returns
:   0 on success, all other values should be treated as error.

## [◆ ](#ga50f6bde28b6a5fcab6b685107570e081)udc\_ep\_buf\_set\_zlp()

| | void udc\_ep\_buf\_set\_zlp | ( | struct [net\_buf](structnet__buf.md) \*const | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Set ZLP flag in requests metadata.

The controller should send a ZLP at the end of the transfer.

Parameters
:   | [in] | buf | Pointer to UDC request buffer |
    | --- | --- | --- |

## [◆ ](#gadec9c8af89b28984028fd8e0b1a8c776)udc\_ep\_clear\_halt()

| int udc\_ep\_clear\_halt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[udc.h](udc_8h.md)>`

Clear endpoint halt.

Valid for all endpoints.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -ENODEV | endpoint configuration not found |
    | --- | --- |
    | -ENOTSUP | not supported (e.g. isochronous endpoint) |
    | -EPERM | controller is not enabled |

## [◆ ](#ga6e6fb62fb8ebceca7e8e6b590c32efc2)udc\_ep\_dequeue()

| int udc\_ep\_dequeue | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[udc.h](udc_8h.md)>`

Remove all USB device controller requests from endpoint queue.

UDC\_EVT\_EP\_REQUEST event will be generated when the driver releases claimed buffer, no new requests will be claimed, all requests in the queue will passed as chained list of the event variable buf. The endpoint queue is empty after that.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -ENODEV | endpoint configuration not found |
    | --- | --- |
    | -EACCES | endpoint is not disabled |
    | -EPERM | controller is not initialized |

## [◆ ](#ga52da2366ac5da1a695caa8826b342cbc)udc\_ep\_disable()

| int udc\_ep\_disable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[udc.h](udc_8h.md)>`

Disable endpoint.

Valid for all endpoints except control IN/OUT.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EINVAL | on wrong parameter (control IN/OUT endpoint) |
    | --- | --- |
    | -ENODEV | endpoint configuration not found |
    | -EALREADY | endpoint is already disabled |
    | -EPERM | controller is not initialized |

## [◆ ](#gacc4b5c127532c994406df30bacab5684)udc\_ep\_enable()

| int udc\_ep\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attributes*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mps*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *interval* ) |

`#include <[udc.h](udc_8h.md)>`

Configure and enable endpoint.

Configure and make an endpoint ready for use. Valid for all endpoints except control IN/OUT.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | ep | Endpoint address (same as bEndpointAddress) |
    | [in] | attributes | Endpoint attributes (same as bmAttributes) |
    | [in] | mps | Maximum packet size (same as wMaxPacketSize) |
    | [in] | interval | Polling interval (same as bInterval) |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EINVAL | on wrong parameter (control IN/OUT endpoint) |
    | --- | --- |
    | -EPERM | controller is not initialized |
    | -ENODEV | endpoint configuration not found |
    | -EALREADY | endpoint is already enabled |

## [◆ ](#gacb2dc96353f1cffcc3d5e9710133fc0d)udc\_ep\_enqueue()

| int udc\_ep\_enqueue | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \*const | *buf* ) |

`#include <[udc.h](udc_8h.md)>`

Queue USB device controller request.

Add request to the queue. If the queue is empty, the request buffer can be claimed by the controller immediately.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | buf | Pointer to UDC request buffer |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -ENODEV | endpoint configuration not found |
    | --- | --- |
    | -EACCES | endpoint is not enabled (TBD) |
    | -EBUSY | request can not be queued |
    | -EPERM | controller is not initialized |

## [◆ ](#ga19488ec4c93d81592bb5ffccfc1eadc4)udc\_ep\_set\_halt()

| int udc\_ep\_set\_halt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[udc.h](udc_8h.md)>`

Halt endpoint.

Valid for all endpoints.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -ENODEV | endpoint configuration not found |
    | --- | --- |
    | -ENOTSUP | not supported (e.g. isochronous endpoint) |
    | -EPERM | controller is not enabled |

## [◆ ](#ga81307ae4ab17ccd86be64bdf1653df0e)udc\_ep\_try\_config()

| int udc\_ep\_try\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attributes*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const | *mps*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *interval* ) |

`#include <[udc.h](udc_8h.md)>`

Try an endpoint configuration.

Try an endpoint configuration based on endpoint descriptor. This function may modify wMaxPacketSize descriptor fields of the endpoint. All properties of the descriptor, such as direction, and transfer type, should be set correctly. If wMaxPacketSize value is zero, it will be updated to maximum buffer size of the endpoint.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | ep | Endpoint address (same as bEndpointAddress) |
    | [in] | attributes | Endpoint attributes (same as bmAttributes) |
    | [in] | mps | Maximum packet size (same as wMaxPacketSize) |
    | [in] | interval | Polling interval (same as bInterval) |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EINVAL | on wrong parameter |
    | --- | --- |
    | -ENOTSUP | endpoint configuration not supported |
    | -ENODEV | no endpoints available |

## [◆ ](#ga073a51222ac639d3c70af7b57970b42a)udc\_get\_buf\_info()

| | struct [udc\_buf\_info](structudc__buf__info.md) \* udc\_get\_buf\_info | ( | const struct [net\_buf](structnet__buf.md) \*const | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Get requests metadata.

Parameters
:   | [in] | buf | Pointer to UDC request buffer |
    | --- | --- | --- |

Returns
:   pointer to metadata structure.

## [◆ ](#ga2d89f013b2e1279d1ec4cbd869e0cae6)udc\_get\_event\_ctx()

| | const void \* udc\_get\_event\_ctx | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Get pointer to higher layer context.

The address of the context is passed as an argument to the [udc\_init()](#ga0670bec8b55c013fb607ba53a8634ad4) function and is stored in the UDC data.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   Opaque pointer to higher layer context

## [◆ ](#ga075edc81fb3e39c2b377fc56c8c0915c)udc\_host\_wakeup()

| | int udc\_host\_wakeup | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Initiate host wakeup procedure.

Initiate host wakeup. Only possible when the bus is suspended.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EPERM | controller is not enabled (or not initialized) |
    | --- | --- |

## [◆ ](#ga0670bec8b55c013fb607ba53a8634ad4)udc\_init()

| int udc\_init | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a) | *event\_cb*, |
|  |  | const void \*const | *event\_ctx* ) |

`#include <[udc.h](udc_8h.md)>`

Initialize USB device controller.

Initialize USB device controller and control IN/OUT endpoint. After initialization controller driver should be able to detect power state of the bus and signal power state changes.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | event\_cb | Event callback from the higher layer (USB device stack) |
    | [in] | event\_ctx | Opaque pointer to higher layer context |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EINVAL | on parameter error (no callback is passed) |
    | --- | --- |
    | -EALREADY | already initialized |

## [◆ ](#ga2c09f2a1e89c91527a8492019089d13f)udc\_is\_enabled()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) udc\_is\_enabled | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Checks whether the controller is enabled.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   true if controller is enabled, false otherwise

## [◆ ](#ga40e50cf79b40d3792513e8fea3347f59)udc\_is\_initialized()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) udc\_is\_initialized | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Checks whether the controller is initialized.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   true if controller is initialized, false otherwise

## [◆ ](#ga88786eda763fce5c2a51521650ccc9f4)udc\_is\_suspended()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) udc\_is\_suspended | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Checks whether the controller is suspended.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   true if controller is suspended, false otherwise

## [◆ ](#ga6da3d836e868f2d09fe24854c2d76aeb)udc\_mps\_ep\_size()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) udc\_mps\_ep\_size | ( | const struct [udc\_ep\_config](structudc__ep__config.md) \*const | *cfg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Get endpoint size from UDC endpoint configuration.

Parameters
:   | [in] | cfg | Pointer to UDC endpoint configuration |
    | --- | --- | --- |

Returns
:   Endpoint size

## [◆ ](#ga6feb32a2263307bdde9acc63d3c2ebb1)udc\_set\_address()

| | int udc\_set\_address | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Set USB device address.

Set address of enabled USB device.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | addr | USB device address |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EPERM | controller is not enabled (or not initialized) |
    | --- | --- |

## [◆ ](#ga59a92eb60575ca80d205cc29b4fb4f21)udc\_shutdown()

| int udc\_shutdown | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Poweroff USB device controller.

Shut down the controller completely to reduce energy consumption or to change the role of the controller.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -EALREADY | controller is not initialized |
    | --- | --- |

## [◆ ](#ga7f575b548833cc1e5109e0d919630b3f)udc\_test\_mode()

| | int udc\_test\_mode | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mode*, | |  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *dryrun* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[udc.h](udc_8h.md)>`

Enable Test Mode.

For compliance testing, high-speed controllers must support test modes. A particular test is enabled by a SetFeature(TEST\_MODE) request. To disable a test mode, device needs to be power cycled.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | mode | Test mode |
    | [in] | dryrun | Verify that a particular mode can be enabled, but do not enable test mode |

Returns
:   0 on success, all other values should be treated as error.

Return values
:   | -ENOTSUP | Test mode is not supported |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
