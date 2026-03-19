---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__tracing__apis__pm__device__runtime.html
original_path: doxygen/html/group__subsys__tracing__apis__pm__device__runtime.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PM Device Runtime Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

PM Device Runtime Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_get\_enter](#ga31c463cfc6794a9d454adbe19c0eff96)(dev) |
|  | Trace getting a device call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_get\_exit](#ga6f9dfe29417ecc3c80b457b3b1ca5ad2)(dev, ret) |
|  | Trace getting a device call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_enter](#gae077ffd9acdc7f4a9b8eff7edca7c5fe)(dev) |
|  | Trace putting a device call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_exit](#ga5670d2d13a291224a8600de54ca475dd)(dev, ret) |
|  | Trace putting a device call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_async\_enter](#gab25dc434aa5ce819f295256effa4cd1a)(dev, delay) |
|  | Trace putting a device (asynchronously) call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_async\_exit](#gae2cb1246d1028a962282c28611c6df11)(dev, delay, ret) |
|  | Trace putting a device (asynchronously) call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_enable\_enter](#ga6653c737e964963541a60aec29120ac0)(dev) |
|  | Trace enabling device runtime PM call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_enable\_exit](#ga0ade92830387457ccc60661325d3f426)(dev, ret) |
|  | Trace enabling device runtime PM call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_disable\_enter](#gaeb479059715af42498f1b1936561f207)(dev) |
|  | Trace disabling device runtime PM call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_disable\_exit](#ga88606e2073fb35283b06500743ebfeb0)(dev, ret) |
|  | Trace disabling device runtime PM call exit. |

## Detailed Description

PM Device Runtime Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gaeb479059715af42498f1b1936561f207)sys\_port\_trace\_pm\_device\_runtime\_disable\_enter

| #define sys\_port\_trace\_pm\_device\_runtime\_disable\_enter | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace disabling device runtime PM call entry.

Parameters
:   | dev | Device instance. |
    | --- | --- |

## [◆ ](#ga88606e2073fb35283b06500743ebfeb0)sys\_port\_trace\_pm\_device\_runtime\_disable\_exit

| #define sys\_port\_trace\_pm\_device\_runtime\_disable\_exit | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace disabling device runtime PM call exit.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | ret | Return value. |

## [◆ ](#ga6653c737e964963541a60aec29120ac0)sys\_port\_trace\_pm\_device\_runtime\_enable\_enter

| #define sys\_port\_trace\_pm\_device\_runtime\_enable\_enter | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace enabling device runtime PM call entry.

Parameters
:   | dev | Device instance. |
    | --- | --- |

## [◆ ](#ga0ade92830387457ccc60661325d3f426)sys\_port\_trace\_pm\_device\_runtime\_enable\_exit

| #define sys\_port\_trace\_pm\_device\_runtime\_enable\_exit | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace enabling device runtime PM call exit.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | ret | Return value. |

## [◆ ](#ga31c463cfc6794a9d454adbe19c0eff96)sys\_port\_trace\_pm\_device\_runtime\_get\_enter

| #define sys\_port\_trace\_pm\_device\_runtime\_get\_enter | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace getting a device call entry.

Parameters
:   | dev | Device instance. |
    | --- | --- |

## [◆ ](#ga6f9dfe29417ecc3c80b457b3b1ca5ad2)sys\_port\_trace\_pm\_device\_runtime\_get\_exit

| #define sys\_port\_trace\_pm\_device\_runtime\_get\_exit | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace getting a device call exit.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | ret | Return value. |

## [◆ ](#gab25dc434aa5ce819f295256effa4cd1a)sys\_port\_trace\_pm\_device\_runtime\_put\_async\_enter

| #define sys\_port\_trace\_pm\_device\_runtime\_put\_async\_enter | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *delay* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace putting a device (asynchronously) call entry.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | delay | Time to delay the operation |

## [◆ ](#gae2cb1246d1028a962282c28611c6df11)sys\_port\_trace\_pm\_device\_runtime\_put\_async\_exit

| #define sys\_port\_trace\_pm\_device\_runtime\_put\_async\_exit | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *delay*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace putting a device (asynchronously) call exit.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | delay | Time to delay the operation. |
    | ret | Return value. |

## [◆ ](#gae077ffd9acdc7f4a9b8eff7edca7c5fe)sys\_port\_trace\_pm\_device\_runtime\_put\_enter

| #define sys\_port\_trace\_pm\_device\_runtime\_put\_enter | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace putting a device call entry.

Parameters
:   | dev | Device instance. |
    | --- | --- |

## [◆ ](#ga5670d2d13a291224a8600de54ca475dd)sys\_port\_trace\_pm\_device\_runtime\_put\_exit

| #define sys\_port\_trace\_pm\_device\_runtime\_put\_exit | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace putting a device call exit.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | ret | Return value. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
