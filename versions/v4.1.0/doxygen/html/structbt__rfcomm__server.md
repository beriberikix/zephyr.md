---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__rfcomm__server.html
original_path: doxygen/html/structbt__rfcomm__server.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| int(\* | [accept](#ac08708bb8161f787737962f62d3c003f) )(struct bt\_conn \*conn, struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\*dlc) |
|  | Server accept callback. |

## Field Documentation

## [◆ ](#ac08708bb8161f787737962f62d3c003f)accept

| int(\* bt\_rfcomm\_server::accept) (struct bt\_conn \*conn, struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\*dlc) |
| --- |

Server accept callback.

This callback is called whenever a new incoming connection requires authorization.

Parameters
:   | conn | The connection that is requesting authorization |
    | --- | --- |
    | server | Pointer to the server structure this callback relates to |
    | dlc | Pointer to received the allocated dlc |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a30b22ea64c0fdd7130e8aaa79519e776)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_server::channel |
| --- |

Server Channel.

Possible values: 0 A dynamic value will be auto-allocated when [bt\_rfcomm\_server\_register()](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401 "Register RFCOMM server.") is called.

0x01 - 0x1e Dynamically allocated. May be pre-set by the application before server registration (not recommended however), or auto-allocated by the stack if the 0 is passed.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[rfcomm.h](rfcomm_8h_source.md)

- [bt\_rfcomm\_server](structbt__rfcomm__server.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
