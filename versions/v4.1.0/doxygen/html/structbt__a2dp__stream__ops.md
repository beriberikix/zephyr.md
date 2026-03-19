---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__a2dp__stream__ops.html
original_path: doxygen/html/structbt__a2dp__stream__ops.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_stream\_ops Struct Reference

The stream endpoint related operations.
[More...](#details)

`#include <[a2dp.h](a2dp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [configured](#a146f907aa60ae130b3248da7475db0cb) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | Stream configured callback. |
| void(\* | [established](#a88d7a0598a5af6740747eb575b8b57df) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | Stream establishment callback. |
| void(\* | [released](#acaa2c8b7e59a0b0bb652c9801110234b) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | Stream release callback. |
| void(\* | [started](#a292e604e7db2faca1915533eab76830e) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | Stream start callback. |
| void(\* | [suspended](#af839ecbcb131cb68165c516c2e049fe5) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | Stream suspend callback. |
| void(\* | [aborted](#ab45e951ee0854e1f937816ab6115343f) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
|  | Stream abort callback. |

## Detailed Description

The stream endpoint related operations.

## Field Documentation

## [◆ ](#ab45e951ee0854e1f937816ab6115343f)aborted

| void(\* bt\_a2dp\_stream\_ops::aborted) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
| --- |

Stream abort callback.

The callback is called whenever an Audio Stream has been aborted. After aborted, the stream becomes invalid.

Parameters
:   | stream | Stream object that has been aborted. |
    | --- | --- |

## [◆ ](#a146f907aa60ae130b3248da7475db0cb)configured

| void(\* bt\_a2dp\_stream\_ops::configured) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
| --- |

Stream configured callback.

The callback is called whenever an Audio Stream has been configured or reconfigured.

Parameters
:   | stream | Stream object that has been configured. |
    | --- | --- |

## [◆ ](#a88d7a0598a5af6740747eb575b8b57df)established

| void(\* bt\_a2dp\_stream\_ops::established) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
| --- |

Stream establishment callback.

The callback is called whenever an Audio Stream has been established.

Parameters
:   | stream | Stream object that has been established. |
    | --- | --- |

## [◆ ](#acaa2c8b7e59a0b0bb652c9801110234b)released

| void(\* bt\_a2dp\_stream\_ops::released) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
| --- |

Stream release callback.

The callback is called whenever an Audio Stream has been released. After released, the stream becomes invalid.

Parameters
:   | stream | Stream object that has been released. |
    | --- | --- |

## [◆ ](#a292e604e7db2faca1915533eab76830e)started

| void(\* bt\_a2dp\_stream\_ops::started) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
| --- |

Stream start callback.

The callback is called whenever an Audio Stream has been started.

Parameters
:   | stream | Stream object that has been started. |
    | --- | --- |

## [◆ ](#af839ecbcb131cb68165c516c2e049fe5)suspended

| void(\* bt\_a2dp\_stream\_ops::suspended) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream) |
| --- |

Stream suspend callback.

The callback is called whenever an Audio Stream has been suspended.

Parameters
:   | stream | Stream object that has been suspended. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[a2dp.h](a2dp_8h_source.md)

- [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
