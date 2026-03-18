---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__rfcomm__server.html
original_path: doxygen/html/structbt__rfcomm__server.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_rfcomm\_server Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [RFCOMM](group__bt__rfcomm.md)

`#include <[rfcomm.h](rfcomm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#a30b22ea64c0fdd7130e8aaa79519e776) |
|  | Server Channel. |
| int(\* | [accept](#a7bcb6da4cd4265c9c3b6439ec8e3a957) )(struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\*dlc) |
|  | Server accept callback. |

## Field Documentation

## [◆ ](#a7bcb6da4cd4265c9c3b6439ec8e3a957)accept

| int(\* bt\_rfcomm\_server::accept) (struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\*dlc) |
| --- |

Server accept callback.

This callback is called whenever a new incoming connection requires authorization.

Parameters
:   | conn | The connection that is requesting authorization |
    | --- | --- |
    | dlc | Pointer to received the allocated dlc |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a30b22ea64c0fdd7130e8aaa79519e776)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_server::channel |
| --- |

Server Channel.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[rfcomm.h](rfcomm_8h_source.md)

- [bt\_rfcomm\_server](structbt__rfcomm__server.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
