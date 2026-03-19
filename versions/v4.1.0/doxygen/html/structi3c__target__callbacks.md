---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__target__callbacks.html
original_path: doxygen/html/structi3c__target__callbacks.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_target\_callbacks Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Target Device API](group__i3c__target__device.md)

`#include <[target_device.h](target__device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [write\_requested\_cb](#ad9e51587a8f86f08d065071d28241ee2) )(struct [i3c\_target\_config](structi3c__target__config.md) \*config) |
|  | Function called when a write to the device is initiated. |
| int(\* | [write\_received\_cb](#a7288f143d19ad306616e25e68ffedc03) )(struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Function called when a write to the device is continued. |
| int(\* | [read\_requested\_cb](#ac72e0bab1eeff6995983f90f6d934749) )(struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Function called when a read from the device is initiated. |
| int(\* | [read\_processed\_cb](#ae53661cfa98a3b58a9702fef28234c30) )(struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Function called when a read from the device is continued. |
| int(\* | [stop\_cb](#a15a1bacdd10c0d6803fbd24f1a1a3323) )(struct [i3c\_target\_config](structi3c__target__config.md) \*config) |
|  | Function called when a stop condition is observed after a start condition addressed to a particular device. |
| int(\* | [controller\_handoff\_cb](#a1e92d1a9bd94b0ef3930bc692764721f) )(struct [i3c\_target\_config](structi3c__target__config.md) \*config) |
|  | Function called when an active controller handoffs controlership to this target. |

## Field Documentation

## [◆ ](#a1e92d1a9bd94b0ef3930bc692764721f)controller\_handoff\_cb

| int(\* i3c\_target\_callbacks::controller\_handoff\_cb) (struct [i3c\_target\_config](structi3c__target__config.md) \*config) |
| --- |

Function called when an active controller handoffs controlership to this target.

This function is invoked by the active controller when it handoffs controllership to this target. This can happen wither the target has requested it or if the active controller chooses to handoff to the controller capable target.

Parameters
:   | config | Configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |

Returns
:   Ignored.

## [◆ ](#ae53661cfa98a3b58a9702fef28234c30)read\_processed\_cb

| int(\* i3c\_target\_callbacks::read\_processed\_cb) (struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
| --- |

Function called when a read from the device is continued.

This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device.

The value returned in `val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

Parameters
:   | config | Configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |
    | val | Pointer to storage for the next byte of data to return for the read request. |

Returns
:   0 if data has been provided, or a negative error code.

## [◆ ](#ac72e0bab1eeff6995983f90f6d934749)read\_requested\_cb

| int(\* i3c\_target\_callbacks::read\_requested\_cb) (struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
| --- |

Function called when a read from the device is initiated.

This function is invoked by the controller when the bus completes a start condition for a read operation from the address associated with a particular device.

The value returned in `val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

Parameters
:   | config | Configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |
    | val | Pointer to storage for the first byte of data to return for the read request. |

Returns
:   0 if more data can be requested, or a negative error code.

## [◆ ](#a15a1bacdd10c0d6803fbd24f1a1a3323)stop\_cb

| int(\* i3c\_target\_callbacks::stop\_cb) (struct [i3c\_target\_config](structi3c__target__config.md) \*config) |
| --- |

Function called when a stop condition is observed after a start condition addressed to a particular device.

This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device. After the function returns the controller shall enter a state where it is ready to react to new start conditions.

Parameters
:   | config | Configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |

Returns
:   Ignored.

## [◆ ](#a7288f143d19ad306616e25e68ffedc03)write\_received\_cb

| int(\* i3c\_target\_callbacks::write\_received\_cb) (struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
| --- |

Function called when a write to the device is continued.

This function is invoked by the controller when it completes reception of a byte of data in an ongoing write operation to the device.

A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

Parameters
:   | config | Configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |
    | val | the byte received by the controller. |

Returns
:   0 if more data can be accepted, or a negative error code.

## [◆ ](#ad9e51587a8f86f08d065071d28241ee2)write\_requested\_cb

| int(\* i3c\_target\_callbacks::write\_requested\_cb) (struct [i3c\_target\_config](structi3c__target__config.md) \*config) |
| --- |

Function called when a write to the device is initiated.

This function is invoked by the controller when the bus completes a start condition for a write operation to the address associated with a particular device.

A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

Parameters
:   | config | Configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |

Returns
:   0 if the write is accepted, or a negative error code.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[target\_device.h](target__device_8h_source.md)

- [i3c\_target\_callbacks](structi3c__target__callbacks.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
