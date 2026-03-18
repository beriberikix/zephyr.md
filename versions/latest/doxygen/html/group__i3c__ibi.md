---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__i3c__ibi.html
original_path: doxygen/html/group__i3c__ibi.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C In-Band Interrupts

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

I3C In-Band Interrupts.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [i3c\_ibi](structi3c__ibi.md) |
|  | Struct for IBI request. [More...](structi3c__ibi.md#details) |
| struct | [i3c\_ibi\_payload](structi3c__ibi__payload.md) |
|  | Structure of payload buffer for IBI. [More...](structi3c__ibi__payload.md#details) |
| struct | [i3c\_ibi\_work](structi3c__ibi__work.md) |
|  | Node about a queued IBI. [More...](structi3c__ibi__work.md#details) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE](#ga7bbbff351dc33d1c00abf6c22bbd50d4)   0 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [i3c\_target\_ibi\_cb\_t](#ga814cf622b240808216ce4e87802e965c)) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ibi\_payload](structi3c__ibi__payload.md) \*payload) |
|  | Function called when In-Band Interrupt received from target device. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_ibi\_type](#gaf4be72fc9c862d996d860c0b7fbc862b) {     [I3C\_IBI\_TARGET\_INTR](#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d) , [I3C\_IBI\_CONTROLLER\_ROLE\_REQUEST](#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815) , [I3C\_IBI\_HOTJOIN](#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f) , [I3C\_IBI\_TYPE\_MAX](#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee) = I3C\_IBI\_HOTJOIN ,     [I3C\_IBI\_WORKQUEUE\_CB](#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c)   } |
|  | IBI Types. [More...](#gaf4be72fc9c862d996d860c0b7fbc862b) |

| Functions | |
| --- | --- |
| static int | [i3c\_ibi\_raise](#ga516c656231efd07429402c37643eca66) (const struct [device](structdevice.md) \*dev, struct [i3c\_ibi](structi3c__ibi.md) \*request) |
|  | Raise an In-Band Interrupt (IBI). |
| static int | [i3c\_ibi\_enable](#ga7625ef0313ded1f638a6eb44395b02c0) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Enable IBI of a target device. |
| static int | [i3c\_ibi\_disable](#ga037e156404324262694b4a5403821adc) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Disable IBI of a target device. |
| static int | [i3c\_ibi\_has\_payload](#ga1a23e2ca2afb7cf371f523dcbcd7724f) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Check if target's IBI has payload. |
| static int | [i3c\_device\_is\_ibi\_capable](#ga6c09d19ab1c7c19db4d085a30066345e) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Check if device is IBI capable. |
| int | [i3c\_ibi\_work\_enqueue](#gaafc2fdf9f2402691c3ebe11d06106840) (struct [i3c\_ibi\_work](structi3c__ibi__work.md) \*ibi\_work) |
|  | Queue an IBI work item for future processing. |
| int | [i3c\_ibi\_work\_enqueue\_target\_irq](#ga7fbf838ea07516849dc1296d48af65d1) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) payload\_len) |
|  | Queue a target interrupt IBI for future processing. |
| int | [i3c\_ibi\_work\_enqueue\_hotjoin](#gab135cb893efd50c7db16c1734b6a0bab) (const struct [device](structdevice.md) \*dev) |
|  | Queue a hot join IBI for future processing. |
| int | [i3c\_ibi\_work\_enqueue\_cb](#ga4c6f4516e55d0ab6c539fb800d7ec45a) (const struct [device](structdevice.md) \*dev, [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) work\_cb) |
|  | Queue a generic callback for future processing. |

## Detailed Description

I3C In-Band Interrupts.

## Macro Definition Documentation

## [◆ ](#ga7bbbff351dc33d1c00abf6c22bbd50d4)CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE

| #define CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE   0 |
| --- |

`#include <[ibi.h](ibi_8h.md)>`

## Typedef Documentation

## [◆ ](#ga814cf622b240808216ce4e87802e965c)i3c\_target\_ibi\_cb\_t

| typedef int(\* i3c\_target\_ibi\_cb\_t) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ibi\_payload](structi3c__ibi__payload.md) \*payload) |
| --- |

`#include <[ibi.h](ibi_8h.md)>`

Function called when In-Band Interrupt received from target device.

This function is invoked by the controller when the controller receives an In-Band Interrupt from the target device.

A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

Parameters
:   | target | the device description structure associated with the device to which the operation is addressed. |
    | --- | --- |
    | payload | Payload associated with the IBI. NULL if there is no payload. |

Returns
:   0 if the IBI is accepted, or a negative error code.

## Enumeration Type Documentation

## [◆ ](#gaf4be72fc9c862d996d860c0b7fbc862b)i3c\_ibi\_type

| enum [i3c\_ibi\_type](#gaf4be72fc9c862d996d860c0b7fbc862b) |
| --- |

`#include <[ibi.h](ibi_8h.md)>`

IBI Types.

| Enumerator | |
| --- | --- |
| I3C\_IBI\_TARGET\_INTR | Target interrupt. |
| I3C\_IBI\_CONTROLLER\_ROLE\_REQUEST | Controller Role Request. |
| I3C\_IBI\_HOTJOIN | Hot Join Request. |
| I3C\_IBI\_TYPE\_MAX |  |
| I3C\_IBI\_WORKQUEUE\_CB | Not an actual IBI type, but simply used by the IBI workq for generic callbacks. |

## Function Documentation

## [◆ ](#ga6c09d19ab1c7c19db4d085a30066345e)i3c\_device\_is\_ibi\_capable()

| | int i3c\_device\_is\_ibi\_capable | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Check if device is IBI capable.

This reads the BCR from the device descriptor struct to determine whether device is capable of IBI.

Note that BCR must have been obtained from device and

See also
:   [i3c\_device\_desc::bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21 "Bus Characteristic Register (BCR).") must be set.

Returns
:   True if IBI has payload, false otherwise.

## [◆ ](#ga037e156404324262694b4a5403821adc)i3c\_ibi\_disable()

| | int i3c\_ibi\_disable | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Disable IBI of a target device.

This enables IBI of a target device where the IBI has already been request.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General Input / output error. |
    | -ENODEV | If IBI is not previously enabled for `target`. |

## [◆ ](#ga7625ef0313ded1f638a6eb44395b02c0)i3c\_ibi\_enable()

| | int i3c\_ibi\_enable | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Enable IBI of a target device.

This enables IBI of a target device where the IBI has already been request.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General Input / output error. |
    | -ENOMEM | If these is no more empty entries in the controller's IBI table (if the controller uses such table). |

## [◆ ](#ga1a23e2ca2afb7cf371f523dcbcd7724f)i3c\_ibi\_has\_payload()

| | int i3c\_ibi\_has\_payload | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Check if target's IBI has payload.

This reads the BCR from the device descriptor struct to determine whether IBI from device has payload.

Note that BCR must have been obtained from device and

See also
:   [i3c\_device\_desc::bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21 "Bus Characteristic Register (BCR).") must be set.

Returns
:   True if IBI has payload, false otherwise.

## [◆ ](#ga516c656231efd07429402c37643eca66)i3c\_ibi\_raise()

| | int i3c\_ibi\_raise | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i3c\_ibi](structi3c__ibi.md) \* | *request* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Raise an In-Band Interrupt (IBI).

This raises an In-Band Interrupt (IBI) to the active controller.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | request | Pointer to the IBI request struct. |

Return values
:   | 0 | if operation is successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#gaafc2fdf9f2402691c3ebe11d06106840)i3c\_ibi\_work\_enqueue()

| int i3c\_ibi\_work\_enqueue | ( | struct [i3c\_ibi\_work](structi3c__ibi__work.md) \* | *ibi\_work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ibi.h](ibi_8h.md)>`

Queue an IBI work item for future processing.

This queues up an IBI work item in the IBI workqueue for future processing.

Note that this will copy the `ibi_work` struct into internal structure. If there is not enough space to copy the `ibi_work` struct, this returns -ENOMEM.

Parameters
:   | ibi\_work | Pointer to the IBI work item struct. |
    | --- | --- |

Return values
:   | 0 | If work item is successfully queued. |
    | --- | --- |
    | -ENOMEM | If no more free internal node to store IBI work item. |
    | Others |  |

See also
:   [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c "Submit a work item to a queue.")

## [◆ ](#ga4c6f4516e55d0ab6c539fb800d7ec45a)i3c\_ibi\_work\_enqueue\_cb()

| int i3c\_ibi\_work\_enqueue\_cb | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) | *work\_cb* ) |

`#include <[ibi.h](ibi_8h.md)>`

Queue a generic callback for future processing.

This queues up a generic callback in the IBI workqueue for future processing.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | work\_cb | Callback function. |

Return values
:   | 0 | If work item is successfully queued. |
    | --- | --- |
    | -ENOMEM | If no more free internal node to store IBI work item. |
    | Others |  |

See also
:   [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c "Submit a work item to a queue.")

## [◆ ](#gab135cb893efd50c7db16c1734b6a0bab)i3c\_ibi\_work\_enqueue\_hotjoin()

| int i3c\_ibi\_work\_enqueue\_hotjoin | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ibi.h](ibi_8h.md)>`

Queue a hot join IBI for future processing.

This queues up a hot join IBI in the IBI workqueue for future processing.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |

Return values
:   | 0 | If work item is successfully queued. |
    | --- | --- |
    | -ENOMEM | If no more free internal node to store IBI work item. |
    | Others |  |

See also
:   [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c "Submit a work item to a queue.")

## [◆ ](#ga7fbf838ea07516849dc1296d48af65d1)i3c\_ibi\_work\_enqueue\_target\_irq()

| int i3c\_ibi\_work\_enqueue\_target\_irq | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *payload*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *payload\_len* ) |

`#include <[ibi.h](ibi_8h.md)>`

Queue a target interrupt IBI for future processing.

This queues up a target interrupt IBI in the IBI workqueue for future processing.

Parameters
:   | target | Pointer to target device descriptor. |
    | --- | --- |
    | payload | Pointer to IBI payload byte array. |
    | payload\_len | Length of payload byte array. |

Return values
:   | 0 | If work item is successfully queued. |
    | --- | --- |
    | -ENOMEM | If no more free internal node to store IBI work item. |
    | Others |  |

See also
:   [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c "Submit a work item to a queue.")

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
