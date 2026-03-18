---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__edac.html
original_path: doxygen/html/group__edac.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

EDAC API

[Device Driver APIs](group__io__interfaces.md)

| Enumerations | |
| --- | --- |
| enum | [edac\_error\_type](#ga3eb3da4d056d8e6167083301eb1276d6) { [EDAC\_ERROR\_TYPE\_DRAM\_COR](#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02) = BIT(0) , [EDAC\_ERROR\_TYPE\_DRAM\_UC](#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f) = BIT(1) } |
|  | EDAC error type. [More...](#ga3eb3da4d056d8e6167083301eb1276d6) |

| Optional interfaces | |
| --- | --- |
| EDAC Optional Interfaces | |
| static int | [edac\_inject\_set\_param1](#gad058d74c811e77b00730e25f2060cce5) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set injection parameter param1. |
| static int | [edac\_inject\_get\_param1](#ga9817f47eeaf532e3789816e412eb5077) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get injection parameter param1. |
| static int | [edac\_inject\_set\_param2](#ga9ed608245ba68aee6b235752a87a5c39) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set injection parameter param2. |
| static int | [edac\_inject\_get\_param2](#ga37e097d550f91072b890d6c2d4b215fa) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get injection parameter param2. |
| static int | [edac\_inject\_set\_error\_type](#ga2b0ea084501faf52aeec5af33a1ca97b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) error\_type) |
|  | Set error type value. |
| static int | [edac\_inject\_get\_error\_type](#gafb0cbc5082e88250a1e5955dd7d1770c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*error\_type) |
|  | Get error type value. |
| static int | [edac\_inject\_error\_trigger](#gaf02830c2e621e73a7c4add38a92f6d7c) (const struct [device](structdevice.md) \*dev) |
|  | Set injection control. |

| Mandatory interfaces | |
| --- | --- |
| EDAC Mandatory Interfaces | |
| static int | [edac\_ecc\_error\_log\_get](#ga905539bb96ff8c9f6f6a9fde6b3928e2) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get ECC Error Log. |
| static int | [edac\_ecc\_error\_log\_clear](#gaa8c798b60b3b99ae6b8f8358253d1385) (const struct [device](structdevice.md) \*dev) |
|  | Clear ECC Error Log. |
| static int | [edac\_parity\_error\_log\_get](#gaa6cba09e19de241ed045387c85cc3f1c) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get Parity Error Log. |
| static int | [edac\_parity\_error\_log\_clear](#gab60aa37ba86e2038fe979481cc6134c2) (const struct [device](structdevice.md) \*dev) |
|  | Clear Parity Error Log. |
| static int | [edac\_errors\_cor\_get](#gaea2915b6c3c4eef2c94c6f60e788dcfe) (const struct [device](structdevice.md) \*dev) |
|  | Get number of correctable errors. |
| static int | [edac\_errors\_uc\_get](#gaec79969648e56e98031d46abe73c2b82) (const struct [device](structdevice.md) \*dev) |
|  | Get number of uncorrectable errors. |
| static int | [edac\_notify\_callback\_set](#ga2def500f72a06271d9a10243bfdf6527) (const struct [device](structdevice.md) \*dev, edac\_notify\_callback\_f cb) |
|  | Register callback function for memory error exception. |

## Detailed Description

Since
:   2.5

Version
:   0.8.0

## Enumeration Type Documentation

## [◆ ](#ga3eb3da4d056d8e6167083301eb1276d6)edac\_error\_type

| enum [edac\_error\_type](#ga3eb3da4d056d8e6167083301eb1276d6) |
| --- |

`#include <[edac.h](edac_8h.md)>`

EDAC error type.

| Enumerator | |
| --- | --- |
| EDAC\_ERROR\_TYPE\_DRAM\_COR | Correctable error type. |
| EDAC\_ERROR\_TYPE\_DRAM\_UC | Uncorrectable error type. |

## Function Documentation

## [◆ ](#gaa8c798b60b3b99ae6b8f8358253d1385)edac\_ecc\_error\_log\_clear()

| | int edac\_ecc\_error\_log\_clear | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Clear ECC Error Log.

Clear value of ECC Error Log.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |

Return values
:   | 0 | on success, error code otherwise |
    | --- | --- |
    | -ENOSYS | if the mandatory interface is not implemented |

## [◆ ](#ga905539bb96ff8c9f6f6a9fde6b3928e2)edac\_ecc\_error\_log\_get()

| | int edac\_ecc\_error\_log\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Get ECC Error Log.

Read value of ECC Error Log.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | value | Pointer to the ECC Error Log value |

Return values
:   | 0 | on success, error code otherwise |
    | --- | --- |
    | -ENOSYS | if the mandatory interface is not implemented |

## [◆ ](#gaea2915b6c3c4eef2c94c6f60e788dcfe)edac\_errors\_cor\_get()

| | int edac\_errors\_cor\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Get number of correctable errors.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |

Return values
:   | num | Number of correctable errors |
    | --- | --- |
    | -ENOSYS | if the mandatory interface is not implemented |

## [◆ ](#gaec79969648e56e98031d46abe73c2b82)edac\_errors\_uc\_get()

| | int edac\_errors\_uc\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Get number of uncorrectable errors.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |

Return values
:   | num | Number of uncorrectable errors |
    | --- | --- |
    | -ENOSYS | if the mandatory interface is not implemented |

## [◆ ](#gaf02830c2e621e73a7c4add38a92f6d7c)edac\_inject\_error\_trigger()

| | int edac\_inject\_error\_trigger | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Set injection control.

Trigger error injection.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |

Return values
:   | -ENOSYS | if the optional interface is not implemented |
    | --- | --- |
    | 0 | on success, error code otherwise |

## [◆ ](#gafb0cbc5082e88250a1e5955dd7d1770c)edac\_inject\_get\_error\_type()

| | int edac\_inject\_get\_error\_type | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *error\_type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Get error type value.

Get the value of error type to be injected

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | error\_type | Pointer to error type value |

Return values
:   | -ENOSYS | if the optional interface is not implemented |
    | --- | --- |
    | 0 | on success, error code otherwise |

## [◆ ](#ga9817f47eeaf532e3789816e412eb5077)edac\_inject\_get\_param1()

| | int edac\_inject\_get\_param1 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Get injection parameter param1.

Get first error injection parameter value.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | value | Pointer to the first injection parameter |

Return values
:   | -ENOSYS | if the optional interface is not implemented |
    | --- | --- |
    | 0 | on success, error code otherwise |

## [◆ ](#ga37e097d550f91072b890d6c2d4b215fa)edac\_inject\_get\_param2()

| | int edac\_inject\_get\_param2 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Get injection parameter param2.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | value | Pointer to the second injection parameter |

Return values
:   | -ENOSYS | if the optional interface is not implemented |
    | --- | --- |
    | 0 | on success, error code otherwise |

## [◆ ](#ga2b0ea084501faf52aeec5af33a1ca97b)edac\_inject\_set\_error\_type()

| | int edac\_inject\_set\_error\_type | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *error\_type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Set error type value.

Set the value of error type to be injected

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | error\_type | Error type value |

Return values
:   | -ENOSYS | if the optional interface is not implemented |
    | --- | --- |
    | 0 | on success, error code otherwise |

## [◆ ](#gad058d74c811e77b00730e25f2060cce5)edac\_inject\_set\_param1()

| | int edac\_inject\_set\_param1 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Set injection parameter param1.

Set first error injection parameter value.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | value | First injection parameter |

Return values
:   | -ENOSYS | if the optional interface is not implemented |
    | --- | --- |
    | 0 | on success, other error code otherwise |

## [◆ ](#ga9ed608245ba68aee6b235752a87a5c39)edac\_inject\_set\_param2()

| | int edac\_inject\_set\_param2 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Set injection parameter param2.

Set second error injection parameter value.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | value | Second injection parameter |

Return values
:   | -ENOSYS | if the optional interface is not implemented |
    | --- | --- |
    | 0 | on success, error code otherwise |

## [◆ ](#ga2def500f72a06271d9a10243bfdf6527)edac\_notify\_callback\_set()

| | int edac\_notify\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | edac\_notify\_callback\_f | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Register callback function for memory error exception.

This callback runs in interrupt context

Parameters
:   | dev | EDAC driver device to install callback |
    | --- | --- |
    | cb | Callback function pointer |

Return values
:   | 0 | on success, error code otherwise |
    | --- | --- |
    | -ENOSYS | if the mandatory interface is not implemented |

## [◆ ](#gab60aa37ba86e2038fe979481cc6134c2)edac\_parity\_error\_log\_clear()

| | int edac\_parity\_error\_log\_clear | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Clear Parity Error Log.

Clear value of Parity Error Log.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |

Return values
:   | 0 | on success, error code otherwise |
    | --- | --- |
    | -ENOSYS | if the mandatory interface is not implemented |

## [◆ ](#gaa6cba09e19de241ed045387c85cc3f1c)edac\_parity\_error\_log\_get()

| | int edac\_parity\_error\_log\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[edac.h](edac_8h.md)>`

Get Parity Error Log.

Read value of Parity Error Log.

Parameters
:   | dev | Pointer to the device structure |
    | --- | --- |
    | value | Pointer to the parity Error Log value |

Return values
:   | 0 | on success, error code otherwise |
    | --- | --- |
    | -ENOSYS | if the mandatory interface is not implemented |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
