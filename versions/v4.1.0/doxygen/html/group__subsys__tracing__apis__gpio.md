---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__tracing__apis__gpio.html
original_path: doxygen/html/group__subsys__tracing__apis__gpio.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

GPIO Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

GPIO Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_enter](#ga136247e36d2f518d15bf332d8ba5d035)(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace GPIO pin interrupt configure enter call. |
| #define | [sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_exit](#ga78b6201756dc8889aed4dbe2f5e5df08)(port, pin, ret) |
|  | Trace GPIO pin interrupt configure exit call. |
| #define | [sys\_port\_trace\_gpio\_pin\_configure\_enter](#ga9975f3c53f4cfa2fb4b699691811289d)(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace GPIO single pin configure enter call. |
| #define | [sys\_port\_trace\_gpio\_pin\_configure\_exit](#gad116e0fee008064fa859fcb660735420)(port, pin, ret) |
|  | Trace GPIO single pin configure exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_direction\_enter](#ga20672a060ed09777729bc417eb4ac726)(port, map, inputs, outputs) |
|  | Trace GPIO port get direction enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_direction\_exit](#gade6194699050e060dc48fa0de50fc930)(port, ret) |
|  | Trace GPIO port get direction exit call. |
| #define | [sys\_port\_trace\_gpio\_pin\_get\_config\_enter](#gac5592dce31daf0c8cfcfa09db50fc9e4)(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace GPIO pin gent config enter call. |
| #define | [sys\_port\_trace\_gpio\_pin\_get\_config\_exit](#ga92ada0c9043f9b00803e33c5537abe05)(port, pin, ret) |
|  | Trace GPIO pin get config exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_raw\_enter](#gabeea324bb6ee389a6f4f739918e43328)(port, value) |
|  | Trace GPIO port get raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_raw\_exit](#ga1cbebfa0804f10c410622bb17c02bdb5)(port, ret) |
|  | Trace GPIO port get raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_enter](#ga6ddcc9a973b2c938fa67ba9d9de90b43)(port, mask, value) |
|  | Trace GPIO port set masked raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_exit](#gacc4328675df61fc4d6aea6406328fec6)(port, ret) |
|  | Trace GPIO port set masked raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_enter](#gae312b54e7983e48519e60be101d2f6cb)(port, pins) |
|  | Trace GPIO port set bits raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_exit](#ga273a91c09bb777d3f436eab91ae69969)(port, ret) |
|  | Trace GPIO port set bits raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_enter](#ga8873f6d6af038b43a9f37c0912775608)(port, pins) |
|  | Trace GPIO port clear bits raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_exit](#ga4a4b88d5a585c0f772dbc8892b801efd)(port, ret) |
|  | Trace GPIO port clear bits raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_toggle\_bits\_enter](#gaf5d4ac1b95410aa6ba7e543868e59928)(port, pins) |
|  | Trace GPIO port toggle bits enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_toggle\_bits\_exit](#ga70f76ddf530aafa81488ca30d6ea4fb7)(port, ret) |
|  | Trace GPIO port toggle bits exit call. |
| #define | [sys\_port\_trace\_gpio\_init\_callback\_enter](#ga3c173c0b612671a9f44fd54efd288ac2)(callback, handler, pin\_mask) |
|  | Trace GPIO init callback enter call. |
| #define | [sys\_port\_trace\_gpio\_init\_callback\_exit](#ga4c130cd12803687e6b8dde1d82aa1d37)(callback) |
|  | Trace GPIO init callback exit call. |
| #define | [sys\_port\_trace\_gpio\_add\_callback\_enter](#ga70cacc72e4696340ed8d53578a13a325)(port, callback) |
|  | Trace GPIO add callback enter call. |
| #define | [sys\_port\_trace\_gpio\_add\_callback\_exit](#gaadca093d8a88c53f7f23ef80300b455a)(port, ret) |
|  | Trace GPIO add callback exit call. |
| #define | [sys\_port\_trace\_gpio\_remove\_callback\_enter](#ga2a756f3d1c60c51708492cbb08c9c3b3)(port, callback) |
|  | Trace GPIO remove callback enter call. |
| #define | [sys\_port\_trace\_gpio\_remove\_callback\_exit](#gaa7cb1d5a8b2205e610df66ee51dee39b)(port, ret) |
|  | Trace GPIO remove callback exit call. |
| #define | [sys\_port\_trace\_gpio\_get\_pending\_int\_enter](#ga29d20db6e85ac27181b697eeff1a405c)(dev) |
|  | Trace GPIO get pending interrupt enter call. |
| #define | [sys\_port\_trace\_gpio\_get\_pending\_int\_exit](#ga118077a21a3037e353fa9ff4ba404be6)(dev, ret) |
|  | Trace GPIO get pending interrupt exit call. |
| #define | [sys\_port\_trace\_gpio\_fire\_callbacks\_enter](#ga9cf081771e5f4724b02de3a89eec339c)(list, port, pins) |
| #define | [sys\_port\_trace\_gpio\_fire\_callback](#gaed3026e592853a9a97c0900a0687974b)(port, callback) |

## Detailed Description

GPIO Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga70cacc72e4696340ed8d53578a13a325)sys\_port\_trace\_gpio\_add\_callback\_enter

| #define sys\_port\_trace\_gpio\_add\_callback\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *callback* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO add callback enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | callback | A valid application's callback structure pointer |

## [◆ ](#gaadca093d8a88c53f7f23ef80300b455a)sys\_port\_trace\_gpio\_add\_callback\_exit

| #define sys\_port\_trace\_gpio\_add\_callback\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO add callback exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaed3026e592853a9a97c0900a0687974b)sys\_port\_trace\_gpio\_fire\_callback

| #define sys\_port\_trace\_gpio\_fire\_callback | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *callback* ) |

`#include <[tracing.h](tracing_8h.md)>`

Parameters
:   | port | [device](structdevice.md "device") representing the GPIO port |
    | --- | --- |
    | callback | [gpio\_callback](structgpio__callback.md "gpio_callback") a valid Application's callback structure pointer |

## [◆ ](#ga9cf081771e5f4724b02de3a89eec339c)sys\_port\_trace\_gpio\_fire\_callbacks\_enter

| #define sys\_port\_trace\_gpio\_fire\_callbacks\_enter | ( |  | *list*, |
| --- | --- | --- | --- |
|  |  |  | *port*, |
|  |  |  | *pins* ) |

`#include <[tracing.h](tracing_8h.md)>`

Parameters
:   | list | [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "sys_slist_t") representing [gpio\_callback](structgpio__callback.md "GPIO callback structure.") pointers |
    | --- | --- |
    | port | [device](structdevice.md "device") representing the GPIO port |
    | pins | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34 "gpio_pin_t") representing the pins |

## [◆ ](#ga29d20db6e85ac27181b697eeff1a405c)sys\_port\_trace\_gpio\_get\_pending\_int\_enter

| #define sys\_port\_trace\_gpio\_get\_pending\_int\_enter | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO get pending interrupt enter call.

Parameters
:   | dev | Pointer to the device structure for the device instance |
    | --- | --- |

## [◆ ](#ga118077a21a3037e353fa9ff4ba404be6)sys\_port\_trace\_gpio\_get\_pending\_int\_exit

| #define sys\_port\_trace\_gpio\_get\_pending\_int\_exit | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO get pending interrupt exit call.

Parameters
:   | dev | Pointer to the device structure for the device instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga3c173c0b612671a9f44fd54efd288ac2)sys\_port\_trace\_gpio\_init\_callback\_enter

| #define sys\_port\_trace\_gpio\_init\_callback\_enter | ( |  | *callback*, |
| --- | --- | --- | --- |
|  |  |  | *handler*, |
|  |  |  | *pin\_mask* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO init callback enter call.

Parameters
:   | callback | A valid application's callback structure pointer |
    | --- | --- |
    | handler | A valid handler function pointer |
    | pin\_mask | A bit mask of relevant pins for the handler |

## [◆ ](#ga4c130cd12803687e6b8dde1d82aa1d37)sys\_port\_trace\_gpio\_init\_callback\_exit

| #define sys\_port\_trace\_gpio\_init\_callback\_exit | ( |  | *callback* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO init callback exit call.

Parameters
:   | callback | A valid application's callback structure pointer |
    | --- | --- |

## [◆ ](#ga9975f3c53f4cfa2fb4b699691811289d)sys\_port\_trace\_gpio\_pin\_configure\_enter

| #define sys\_port\_trace\_gpio\_pin\_configure\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO single pin configure enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pin | GPIO pin number to configure |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | GPIO pin configuration flags |

## [◆ ](#gad116e0fee008064fa859fcb660735420)sys\_port\_trace\_gpio\_pin\_configure\_exit

| #define sys\_port\_trace\_gpio\_pin\_configure\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO single pin configure exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pin | GPIO pin number to configure |
    | ret | Return value |

## [◆ ](#gac5592dce31daf0c8cfcfa09db50fc9e4)sys\_port\_trace\_gpio\_pin\_get\_config\_enter

| #define sys\_port\_trace\_gpio\_pin\_get\_config\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO pin gent config enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pin | GPIO pin number to configure |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | GPIO pin configuration flags |

## [◆ ](#ga92ada0c9043f9b00803e33c5537abe05)sys\_port\_trace\_gpio\_pin\_get\_config\_exit

| #define sys\_port\_trace\_gpio\_pin\_get\_config\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO pin get config exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pin | GPIO pin number to configure |
    | ret | Return value |

## [◆ ](#ga136247e36d2f518d15bf332d8ba5d035)sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_enter

| #define sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO pin interrupt configure enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pin | GPIO pin number |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Interrupt configuration flags as defined by GPIO\_INT\_\* |

## [◆ ](#ga78b6201756dc8889aed4dbe2f5e5df08)sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_exit

| #define sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO pin interrupt configure exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pin | GPIO pin number |
    | ret | Return value |

## [◆ ](#ga8873f6d6af038b43a9f37c0912775608)sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_enter

| #define sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pins* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port clear bits raw enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pins | Value indicating which pins will be modified |

## [◆ ](#ga4a4b88d5a585c0f772dbc8892b801efd)sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_exit

| #define sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port clear bits raw exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga20672a060ed09777729bc417eb4ac726)sys\_port\_trace\_gpio\_port\_get\_direction\_enter

| #define sys\_port\_trace\_gpio\_port\_get\_direction\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *map*, |
|  |  |  | *inputs*, |
|  |  |  | *outputs* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port get direction enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | map | Bitmap of pin directions to query |
    | inputs | Pointer to a variable where input directions will be stored |
    | outputs | Pointer to a variable where output directions will be stored |

## [◆ ](#gade6194699050e060dc48fa0de50fc930)sys\_port\_trace\_gpio\_port\_get\_direction\_exit

| #define sys\_port\_trace\_gpio\_port\_get\_direction\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port get direction exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gabeea324bb6ee389a6f4f739918e43328)sys\_port\_trace\_gpio\_port\_get\_raw\_enter

| #define sys\_port\_trace\_gpio\_port\_get\_raw\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *value* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port get raw enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | value | Pointer to a variable where the raw value will be stored |

## [◆ ](#ga1cbebfa0804f10c410622bb17c02bdb5)sys\_port\_trace\_gpio\_port\_get\_raw\_exit

| #define sys\_port\_trace\_gpio\_port\_get\_raw\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port get raw exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gae312b54e7983e48519e60be101d2f6cb)sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_enter

| #define sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pins* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port set bits raw enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pins | Value indicating which pins will be modified |

## [◆ ](#ga273a91c09bb777d3f436eab91ae69969)sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_exit

| #define sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port set bits raw exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga6ddcc9a973b2c938fa67ba9d9de90b43)sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_enter

| #define sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *mask*, |
|  |  |  | *value* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port set masked raw enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | mask | Mask indicating which pins will be modified |
    | value | Value to be written to the output pins |

## [◆ ](#gacc4328675df61fc4d6aea6406328fec6)sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_exit

| #define sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port set masked raw exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaf5d4ac1b95410aa6ba7e543868e59928)sys\_port\_trace\_gpio\_port\_toggle\_bits\_enter

| #define sys\_port\_trace\_gpio\_port\_toggle\_bits\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pins* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port toggle bits enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | pins | Value indicating which pins will be modified |

## [◆ ](#ga70f76ddf530aafa81488ca30d6ea4fb7)sys\_port\_trace\_gpio\_port\_toggle\_bits\_exit

| #define sys\_port\_trace\_gpio\_port\_toggle\_bits\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO port toggle bits exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga2a756f3d1c60c51708492cbb08c9c3b3)sys\_port\_trace\_gpio\_remove\_callback\_enter

| #define sys\_port\_trace\_gpio\_remove\_callback\_enter | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *callback* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO remove callback enter call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | callback | A valid application's callback structure pointer |

## [◆ ](#gaa7cb1d5a8b2205e610df66ee51dee39b)sys\_port\_trace\_gpio\_remove\_callback\_exit

| #define sys\_port\_trace\_gpio\_remove\_callback\_exit | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace GPIO remove callback exit call.

Parameters
:   | port | Pointer to device structure for the driver instance |
    | --- | --- |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
