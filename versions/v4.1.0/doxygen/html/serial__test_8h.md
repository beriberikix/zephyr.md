---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/serial__test_8h.html
original_path: doxygen/html/serial__test_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

serial\_test.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](serial__test_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [serial\_vnd\_write\_cb\_t](#a04f02df85d720ccd5ce02ab9e217dba3)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Callback called after bytes written to the virtual serial port. |

| Functions | |
| --- | --- |
| int | [serial\_vnd\_queue\_in\_data](#a2b7d97302cb3546cfc8f384f4a7c1a4a) (const struct [device](structdevice.md) \*dev, const [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Queues data to be read by the virtual serial port. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [serial\_vnd\_out\_data\_size\_get](#a4275edbc443677d2c0f08100834977a7) (const struct [device](structdevice.md) \*dev) |
|  | Returns size of unread written data. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [serial\_vnd\_read\_out\_data](#ab9b60bf8d62db2be3ad530cd0a78aedd) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Read data written to virtual serial port. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [serial\_vnd\_peek\_out\_data](#a1e2a3d82504b34d5b4590afc67172c9e) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Peek at data written to virtual serial port. |
| void | [serial\_vnd\_set\_callback](#a4908343c26e5846abf977befe2c5dbbe) (const struct [device](structdevice.md) \*dev, [serial\_vnd\_write\_cb\_t](#a04f02df85d720ccd5ce02ab9e217dba3) callback, void \*user\_data) |
|  | Sets the write callback on a virtual serial port. |

## Typedef Documentation

## [◆ ](#a04f02df85d720ccd5ce02ab9e217dba3)serial\_vnd\_write\_cb\_t

| typedef void(\* serial\_vnd\_write\_cb\_t) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
| --- |

Callback called after bytes written to the virtual serial port.

Parameters
:   | dev | Address of virtual serial port. |
    | --- | --- |
    | user\_data | User data. |

## Function Documentation

## [◆ ](#a4275edbc443677d2c0f08100834977a7)serial\_vnd\_out\_data\_size\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) serial\_vnd\_out\_data\_size\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Returns size of unread written data.

Parameters
:   | dev | Address of virtual serial port. |
    | --- | --- |

Returns
:   Output data size (in bytes).

## [◆ ](#a1e2a3d82504b34d5b4590afc67172c9e)serial\_vnd\_peek\_out\_data()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) serial\_vnd\_peek\_out\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

Peek at data written to virtual serial port.

Reads the data without consuming it. Future calls to [serial\_vnd\_peek\_out\_data()](#a1e2a3d82504b34d5b4590afc67172c9e) or [serial\_vnd\_read\_out\_data()](#ab9b60bf8d62db2be3ad530cd0a78aedd) will return this data again. Requires CONFIG\_RING\_BUFFER.

Warning
:   Use cases involving multiple reads of the data must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads.

Parameters
:   | dev | Address of virtual serial port. |
    | --- | --- |
    | data | Address of the output buffer. Cannot be NULL. |
    | size | Data size (in bytes). |

Return values
:   | Number | of bytes written to the output buffer. |
    | --- | --- |

## [◆ ](#a2b7d97302cb3546cfc8f384f4a7c1a4a)serial\_vnd\_queue\_in\_data()

| int serial\_vnd\_queue\_in\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

Queues data to be read by the virtual serial port.

Warning
:   Use cases involving multiple writers virtual serial port must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes.

Parameters
:   | dev | Address of virtual serial port. |
    | --- | --- |
    | data | Address of data. |
    | size | Data size (in bytes). |

Return values
:   | Number | of bytes written. |
    | --- | --- |

## [◆ ](#ab9b60bf8d62db2be3ad530cd0a78aedd)serial\_vnd\_read\_out\_data()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) serial\_vnd\_read\_out\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

Read data written to virtual serial port.

Consumes the data, such that future calls to [serial\_vnd\_read\_out\_data()](#ab9b60bf8d62db2be3ad530cd0a78aedd) will not include this data. Requires CONFIG\_RING\_BUFFER.

Warning
:   Use cases involving multiple reads of the data must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads.

Parameters
:   | dev | Address of virtual serial port. |
    | --- | --- |
    | data | Address of the output buffer. Can be NULL to discard data. |
    | size | Data size (in bytes). |

Return values
:   | Number | of bytes written to the output buffer. |
    | --- | --- |

## [◆ ](#a4908343c26e5846abf977befe2c5dbbe)serial\_vnd\_set\_callback()

| void serial\_vnd\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [serial\_vnd\_write\_cb\_t](#a04f02df85d720ccd5ce02ab9e217dba3) | *callback*, |
|  |  | void \* | *user\_data* ) |

Sets the write callback on a virtual serial port.

Parameters
:   | dev | Address of virtual serial port. |
    | --- | --- |
    | callback | Function to call after each write to the port. |
    | user\_data | Opaque data to pass to the callback. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart](dir_eceb547fc512cd90b0f2ab20ab1dbc9a.md)
- [serial\_test.h](serial__test_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
