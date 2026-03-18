---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__dfd__srv__cb.html
original_path: doxygen/html/structbt__mesh__dfd__srv__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfd\_srv\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Firmware Distribution models](group__bt__mesh__dfd.md) » [Firmware Distribution Server model](group__bt__mesh__dfd__srv.md)

Firmware Distribution Server callbacks:
[More...](#details)

`#include <[dfd_srv.h](dfd__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [recv](#a6d6d991b3a5bd5fe69b1648fea94ebe4) )(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
|  | Slot receive callback. |
| void(\* | [del](#a73f230a76ea32fb1faee15a5d4adb550) )(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot) |
|  | Slot delete callback. |
| int(\* | [send](#a84e14ad78ebe520bad3ad6ee24fbb629) )(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
|  | Slot send callback. |
| void(\* | [phase](#ae72a527cae827e0a234af3277384d07f) )(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, enum [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) phase) |
|  | Phase change callback (Optional). |

## Detailed Description

Firmware Distribution Server callbacks:

## Field Documentation

## [◆ ](#a73f230a76ea32fb1faee15a5d4adb550)del

| void(\* bt\_mesh\_dfd\_srv\_cb::del) (struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot) |
| --- |

Slot delete callback.

Called when the Firmware Distribution Server is about to delete a DFU image slot. All allocated data associated with the firmware slot should be deleted.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |
    | slot | DFU image slot being deleted. |

## [◆ ](#ae72a527cae827e0a234af3277384d07f)phase

| void(\* bt\_mesh\_dfd\_srv\_cb::phase) (struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, enum [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) phase) |
| --- |

Phase change callback (Optional).

Called whenever the phase of the Firmware Distribution Server changes.

Parameters
:   | srv | Firmware Distribution Server model instance. |
    | --- | --- |
    | [phase](#ae72a527cae827e0a234af3277384d07f) | New Firmware Distribution phase. |

## [◆ ](#a6d6d991b3a5bd5fe69b1648fea94ebe4)recv

| int(\* bt\_mesh\_dfd\_srv\_cb::recv) (struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
| --- |

Slot receive callback.

Called at the start of an upload procedure. The callback must fill `io` with a pointer to a writable BLOB stream for the Firmware Distribution Server to write the firmware image to.

Parameters
:   | srv | Firmware Distribution Server model instance. |
    | --- | --- |
    | slot | DFU image slot being received. |
    | io | BLOB stream response pointer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#a84e14ad78ebe520bad3ad6ee24fbb629)send

| int(\* bt\_mesh\_dfd\_srv\_cb::send) (struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
| --- |

Slot send callback.

Called at the start of a distribution procedure. The callback must fill `io` with a pointer to a readable BLOB stream for the Firmware Distribution Server to read the firmware image from.

Parameters
:   | srv | Firmware Distribution Server model instance. |
    | --- | --- |
    | slot | DFU image slot being sent. |
    | io | BLOB stream response pointer. |

Returns
:   0 on success, or (negative) error code otherwise.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfd\_srv.h](dfd__srv_8h_source.md)

- [bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
