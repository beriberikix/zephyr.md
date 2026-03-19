---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__dfu__srv__cb.html
original_path: doxygen/html/structbt__mesh__dfu__srv__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_srv\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Update Server model](group__bt__mesh__dfu__srv.md)

Firmware Update Server event callbacks.
[More...](#details)

`#include <[dfu_srv.h](dfu__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [check](#afbde918804e66160ffa176c206540027) )(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, struct [net\_buf\_simple](structnet__buf__simple.md) \*metadata, enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) \*effect) |
|  | Transfer check callback. |
| int(\* | [start](#adaefef5067cf3ea273f1db95ca536254) )(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, struct [net\_buf\_simple](structnet__buf__simple.md) \*metadata, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
|  | Transfer start callback. |
| void(\* | [end](#a822ed15f15286ad4c5ce69009349f6cf) )(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) success) |
|  | Transfer end callback. |
| int(\* | [recover](#a3fec449cebe43dd2d8e6ecf3c148234d) )(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
|  | Transfer recovery callback. |
| int(\* | [apply](#afe4b6ca9f56938695addba6ecc18bb4b) )(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img) |
|  | Transfer apply callback. |

## Detailed Description

Firmware Update Server event callbacks.

## Field Documentation

## [◆ ](#afe4b6ca9f56938695addba6ecc18bb4b)apply

| int(\* bt\_mesh\_dfu\_srv\_cb::apply) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img) |
| --- |

Transfer apply callback.

Called after a transfer has been validated, and the updater sends an apply message to the Target nodes.

This handler is optional.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |
    | img | DFU image that should be applied. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#afbde918804e66160ffa176c206540027)check

| int(\* bt\_mesh\_dfu\_srv\_cb::check) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, struct [net\_buf\_simple](structnet__buf__simple.md) \*metadata, enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) \*effect) |
| --- |

Transfer check callback.

The transfer check can be used to validate the incoming transfer before it starts. The contents of the metadata is implementation specific, and should contain all the information the application needs to determine whether this image should be accepted, and what the effect of the transfer would be.

If applying the image will have an effect on the provisioning state of the mesh stack, this can be communicated through the `effect` return parameter.

The metadata check can be performed both as part of starting a new transfer and as a separate procedure.

This handler is optional.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |
    | img | DFU image the metadata check is performed on. |
    | metadata | Image metadata. |
    | effect | Return parameter for the image effect on the provisioning state of the mesh stack. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#a822ed15f15286ad4c5ce69009349f6cf)end

| void(\* bt\_mesh\_dfu\_srv\_cb::end) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) success) |
| --- |

Transfer end callback.

This handler is optional.

If the transfer is successful, the application should verify the firmware image, and call either [bt\_mesh\_dfu\_srv\_verified](group__bt__mesh__dfu__srv.md#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac "bt_mesh_dfu_srv_verified") or [bt\_mesh\_dfu\_srv\_rejected](group__bt__mesh__dfu__srv.md#ga77142a1f3cfe2ff1d53332114f977b38 "bt_mesh_dfu_srv_rejected") depending on the outcome.

If the transfer fails, the Firmware Update Server will be available for new transfers immediately after this function returns.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |
    | img | DFU image that failed the update. |
    | success | Whether the DFU transfer was successful. |

## [◆ ](#a3fec449cebe43dd2d8e6ecf3c148234d)recover

| int(\* bt\_mesh\_dfu\_srv\_cb::recover) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
| --- |

Transfer recovery callback.

If the device reboots in the middle of a transfer, the Firmware Update Server calls this function when the Bluetooth Mesh subsystem is started.

This callback is optional, but transfers will not be recovered after a reboot without it.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |
    | img | DFU image being updated. |
    | io | BLOB stream return parameter. Must be set to a valid BLOB stream by the callback. |

Returns
:   0 on success, or (negative) error code to abandon the transfer.

## [◆ ](#adaefef5067cf3ea273f1db95ca536254)start

| int(\* bt\_mesh\_dfu\_srv\_cb::start) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, struct [net\_buf\_simple](structnet__buf__simple.md) \*metadata, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io) |
| --- |

Transfer start callback.

Called when the Firmware Update Server is ready to start a new DFU transfer. The application must provide an initialized BLOB stream to be used during the DFU transfer.

The following error codes are treated specially, and should be used to communicate these issues:

- `-ENOMEM:` The device cannot fit this image.
- `-EBUSY:` The application is temporarily unable to accept the transfer.
- `-EALREADY:` The device has already received and verified this image, and there's no need to transfer it again. The Firmware Update model will skip the transfer phase, and mark the image as verified.

This handler is mandatory.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |
    | img | DFU image being updated. |
    | metadata | Image metadata. |
    | io | BLOB stream return parameter. Must be set to a valid BLOB stream by the callback. |

Returns
:   0 on success, or (negative) error code otherwise. Return codes `-ENOMEM`, `-EBUSY` `-EALREADY` will be passed to the updater, other error codes are reported as internal errors.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_srv.h](dfu__srv_8h_source.md)

- [bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
