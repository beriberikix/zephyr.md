---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hci_8h.html
original_path: doxygen/html/hci_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci_types.h](hci__types_8h_source.md)>`

[Go to the source code of this file.](hci_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_hci\_vnd\_evt\_cb\_t](#a061c7eee0b02021da072d9859ef838a6)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback type for vendor handling of HCI Vendor-Specific Events. |

| Functions | |
| --- | --- |
| static const char \* | [bt\_hci\_err\_to\_str](#a31f7876c1a3e5dc7f1e1b2949b08139f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hci\_err) |
|  | Converts a HCI error to string. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_hci\_cmd\_create](#a88da5ec3183ac23bc19ef0ebf66b004b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) param\_len) |
|  | Allocate a HCI command buffer. |
| int | [bt\_hci\_cmd\_send](#af2eed9d93da45185aad9c2edc0001a54) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send a HCI command asynchronously. |
| int | [bt\_hci\_cmd\_send\_sync](#a8d306b5b56afdece1cadbbf0eecfe5a7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, struct [net\_buf](structnet__buf.md) \*buf, struct [net\_buf](structnet__buf.md) \*\*rsp) |
|  | Send a HCI command synchronously. |
| int | [bt\_hci\_get\_conn\_handle](#ac223ac9cddf8696d853c0942f9f148e0) (const struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*conn\_handle) |
|  | Get connection handle for a connection. |
| int | [bt\_hci\_get\_adv\_handle](#a27f6cd853c079e4412adbe4a1b32f8e6) (const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*adv\_handle) |
|  | Get advertising handle for an advertising set. |
| int | [bt\_hci\_get\_adv\_sync\_handle](#a73fa69c6e4faea073433f3f73d327c46) (const struct bt\_le\_per\_adv\_sync \*sync, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*sync\_handle) |
|  | Get periodic advertising sync handle. |
| const char \* | [bt\_hci\_get\_ver\_str](#a9931a6d4e55140e741b78656cb43e88c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) core\_version) |
|  | Obtain the version string given a core version number. |
| int | [bt\_hci\_register\_vnd\_evt\_cb](#ae41be6f3dd87016bbb92f004adeb6ece) ([bt\_hci\_vnd\_evt\_cb\_t](#a061c7eee0b02021da072d9859ef838a6) cb) |
|  | Register user callback for HCI Vendor-Specific Events. |
| int | [bt\_hci\_le\_rand](#a50f4a8808c26a7b4e288e650b2325883) (void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get Random bytes from the LE Controller. |

## Typedef Documentation

## [◆ ](#a061c7eee0b02021da072d9859ef838a6)bt\_hci\_vnd\_evt\_cb\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_hci\_vnd\_evt\_cb\_t(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Callback type for vendor handling of HCI Vendor-Specific Events.

A function of this type is registered with [bt\_hci\_register\_vnd\_evt\_cb()](#ae41be6f3dd87016bbb92f004adeb6ece) and will be called for any HCI Vendor-Specific Event.

Parameters
:   | buf | Buffer containing event parameters. |
    | --- | --- |

Returns
:   true if the function handles the event or false to defer the handling of this event back to the stack.

## Function Documentation

## [◆ ](#a88da5ec3183ac23bc19ef0ebf66b004b)bt\_hci\_cmd\_create()

| struct [net\_buf](structnet__buf.md) \* bt\_hci\_cmd\_create | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *opcode*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *param\_len* ) |

Allocate a HCI command buffer.

This function allocates a new buffer for a HCI command. It is given the OpCode (encoded e.g. using the BT\_OP macro) and the total length of the parameters. Upon successful return the buffer is ready to have the parameters encoded into it.

Parameters
:   | opcode | Command OpCode. |
    | --- | --- |
    | param\_len | Length of command parameters. |

Returns
:   Newly allocated buffer.

## [◆ ](#af2eed9d93da45185aad9c2edc0001a54)bt\_hci\_cmd\_send()

| int bt\_hci\_cmd\_send | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *opcode*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

Send a HCI command asynchronously.

This function is used for sending a HCI command asynchronously. It can either be called for a buffer created using [bt\_hci\_cmd\_create()](#a88da5ec3183ac23bc19ef0ebf66b004b), or if the command has no parameters a NULL can be passed instead. The sending of the command will happen asynchronously, i.e. upon successful return from this function the caller only knows that it was queued successfully.

If synchronous behavior, and retrieval of the Command Complete parameters is desired, the [bt\_hci\_cmd\_send\_sync()](#a8d306b5b56afdece1cadbbf0eecfe5a7) API should be used instead.

Parameters
:   | opcode | Command OpCode. |
    | --- | --- |
    | buf | Command buffer or NULL (if no parameters). |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#a8d306b5b56afdece1cadbbf0eecfe5a7)bt\_hci\_cmd\_send\_sync()

| int bt\_hci\_cmd\_send\_sync | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *opcode*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf*, |
|  |  | struct [net\_buf](structnet__buf.md) \*\* | *rsp* ) |

Send a HCI command synchronously.

This function is used for sending a HCI command synchronously. It can either be called for a buffer created using [bt\_hci\_cmd\_create()](#a88da5ec3183ac23bc19ef0ebf66b004b), or if the command has no parameters a NULL can be passed instead.

The function will block until a Command Status or a Command Complete event is returned. If either of these have a non-zero status the function will return a negative error code and the response reference will not be set. If the command completed successfully and a non-NULL rsp parameter was given, this parameter will be set to point to a buffer containing the response parameters.

Parameters
:   | opcode | Command OpCode. |
    | --- | --- |
    | buf | Command buffer or NULL (if no parameters). |
    | rsp | Place to store a reference to the command response. May be NULL if the caller is not interested in the response parameters. If non-NULL is passed the caller is responsible for calling [net\_buf\_unref()](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273 "Decrements the reference count of a buffer.") on the buffer when done parsing it. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#a31f7876c1a3e5dc7f1e1b2949b08139f)bt\_hci\_err\_to\_str()

| | const char \* bt\_hci\_err\_to\_str | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *hci\_err* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Converts a HCI error to string.

The error codes are described in the Bluetooth Core specification, Vol 1, Part F, Section 2.

The HCI documentation found in Vol 4, Part E, describes when the different error codes are used.

See also the defined BT\_HCI\_ERR\_\* macros.

Returns
:   The string representation of the HCI error code. If `CONFIG_BT_HCI_ERR_TO_STR` is not enabled, this just returns the empty string

## [◆ ](#a27f6cd853c079e4412adbe4a1b32f8e6)bt\_hci\_get\_adv\_handle()

| int bt\_hci\_get\_adv\_handle | ( | const struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *adv\_handle* ) |

Get advertising handle for an advertising set.

Parameters
:   | adv | Advertising set. |
    | --- | --- |
    | adv\_handle | Place to store the advertising handle. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#a73fa69c6e4faea073433f3f73d327c46)bt\_hci\_get\_adv\_sync\_handle()

| int bt\_hci\_get\_adv\_sync\_handle | ( | const struct bt\_le\_per\_adv\_sync \* | *sync*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *sync\_handle* ) |

Get periodic advertising sync handle.

Parameters
:   | sync | Periodic advertising sync set. |
    | --- | --- |
    | sync\_handle | Place to store the periodic advertising sync handle. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ac223ac9cddf8696d853c0942f9f148e0)bt\_hci\_get\_conn\_handle()

| int bt\_hci\_get\_conn\_handle | ( | const struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *conn\_handle* ) |

Get connection handle for a connection.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | conn\_handle | Place to store the Connection handle. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#a9931a6d4e55140e741b78656cb43e88c)bt\_hci\_get\_ver\_str()

| const char \* bt\_hci\_get\_ver\_str | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *core\_version* | ) |  |
| --- | --- | --- | --- | --- | --- |

Obtain the version string given a core version number.

The core version of a controller can be obtained by issuing the HCI Read Local Version Information command.

See also the defines prefixed with BT\_HCI\_VERSION\_.

Parameters
:   | core\_version | The core version. |
    | --- | --- |

Returns
:   Version string corresponding to the core version number.

## [◆ ](#a50f4a8808c26a7b4e288e650b2325883)bt\_hci\_le\_rand()

| int bt\_hci\_le\_rand | ( | void \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

Get Random bytes from the LE Controller.

Send the HCI\_LE\_Rand to the LE Controller as many times as required to fill the provided `buffer`.

Note
:   This function is provided as a helper to gather an arbitrary number of random bytes from an LE Controller using the HCI\_LE\_Rand command.

Parameters
:   | buffer | Buffer to fill with random bytes. |
    | --- | --- |
    | len | Length of the buffer in bytes. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ae41be6f3dd87016bbb92f004adeb6ece)bt\_hci\_register\_vnd\_evt\_cb()

| int bt\_hci\_register\_vnd\_evt\_cb | ( | [bt\_hci\_vnd\_evt\_cb\_t](#a061c7eee0b02021da072d9859ef838a6) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

Register user callback for HCI Vendor-Specific Events.

Parameters
:   | cb | Callback to be called when the stack receives a HCI Vendor-Specific Event. |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci.h](hci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
