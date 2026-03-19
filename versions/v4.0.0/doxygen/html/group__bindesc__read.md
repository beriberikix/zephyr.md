---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bindesc__read.html
original_path: doxygen/html/group__bindesc__read.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bindesc Read

[Operating System Services](group__os__services.md)

Reading Binary Descriptors of other images.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef int(\* | [bindesc\_callback\_t](#ga6f02f63064e53a0d85150982cc529519)) (const struct [bindesc\_entry](structbindesc__entry.md) \*entry, void \*user\_data) |
|  | Callback type to be called on descriptors found during a walk. |

| Functions | |
| --- | --- |
| int | [bindesc\_open\_memory\_mapped\_flash](#ga3ed93a855c2ee2981f2ca76450c57d99) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Open an image's binary descriptors for reading, from a memory mapped flash. |
| int | [bindesc\_open\_ram](#gadec0f4f828c1e4cdcef63b67c0fbafcf) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*address, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_size) |
|  | Open an image's binary descriptors for reading, from RAM. |
| int | [bindesc\_open\_flash](#ga724d940fecd648523c3d3bd840785498) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, const struct [device](structdevice.md) \*flash\_device) |
|  | Open an image's binary descriptors for reading, from flash. |
| int | [bindesc\_foreach](#ga8d7f293d620a80b49797d4c1d6d2998f) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [bindesc\_callback\_t](#ga6f02f63064e53a0d85150982cc529519) callback, void \*user\_data) |
|  | Walk the binary descriptors and run a user defined callback on each of them. |
| int | [bindesc\_find\_str](#ga422708cc9ffb1a911b4990eff0270e76) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const char \*\*result) |
|  | Find a specific descriptor of type string. |
| int | [bindesc\_find\_uint](#gad3ae2bde011c2115a33c836caff37811) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*result) |
|  | Find a specific descriptor of type uint. |
| int | [bindesc\_find\_bytes](#gaf8b8b3a883f5c835d5a0581768d801d4) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*result, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result\_size) |
|  | Find a specific descriptor of type bytes. |
| int | [bindesc\_get\_size](#ga7df52ef12aa9572d3a2ff4245529d8fd) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
|  | Get the size of an image's binary descriptors. |

## Detailed Description

Reading Binary Descriptors of other images.

## Typedef Documentation

## [◆ ](#ga6f02f63064e53a0d85150982cc529519)bindesc\_callback\_t

| typedef int(\* bindesc\_callback\_t) (const struct [bindesc\_entry](structbindesc__entry.md) \*entry, void \*user\_data) |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

Callback type to be called on descriptors found during a walk.

Parameters
:   | entry | Current descriptor |
    | --- | --- |
    | user\_data | The user\_data given to [bindesc\_foreach](#ga8d7f293d620a80b49797d4c1d6d2998f) |

Returns
:   Any non zero value will halt the walk

## Function Documentation

## [◆ ](#gaf8b8b3a883f5c835d5a0581768d801d4)bindesc\_find\_bytes()

| int bindesc\_find\_bytes | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *result*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *result\_size* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Find a specific descriptor of type bytes.

Warning
:   When using the flash backend, result will be invalidated by the next call to any bindesc API. Use the value immediately or copy it elsewhere.

Parameters
:   | handle | An initialized bindesc handle |
    | --- | --- |
    | id | ID to search for |
    | result | Pointer to the found bytes |
    | result\_size | Size of the found bytes |

Return values
:   | 0 | If the descriptor was found |
    | --- | --- |
    | -ENOENT | If the descriptor was not found |

## [◆ ](#ga422708cc9ffb1a911b4990eff0270e76)bindesc\_find\_str()

| int bindesc\_find\_str | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | const char \*\* | *result* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Find a specific descriptor of type string.

Warning
:   When using the flash backend, result will be invalidated by the next call to any bindesc API. Use the value immediately or copy it elsewhere.

Parameters
:   | handle | An initialized bindesc handle |
    | --- | --- |
    | id | ID to search for |
    | result | Pointer to the found string |

Return values
:   | 0 | If the descriptor was found |
    | --- | --- |
    | -ENOENT | If the descriptor was not found |

## [◆ ](#gad3ae2bde011c2115a33c836caff37811)bindesc\_find\_uint()

| int bindesc\_find\_uint | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\* | *result* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Find a specific descriptor of type uint.

Warning
:   When using the flash backend, result will be invalidated by the next call to any bindesc API. Use the value immediately or copy it elsewhere.

Parameters
:   | handle | An initialized bindesc handle |
    | --- | --- |
    | id | ID to search for |
    | result | Pointer to the found uint |

Return values
:   | 0 | If the descriptor was found |
    | --- | --- |
    | -ENOENT | If the descriptor was not found |

## [◆ ](#ga8d7f293d620a80b49797d4c1d6d2998f)bindesc\_foreach()

| int bindesc\_foreach | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [bindesc\_callback\_t](#ga6f02f63064e53a0d85150982cc529519) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Walk the binary descriptors and run a user defined callback on each of them.

Note
:   If the callback returns a non zero value, the walk stops.

Parameters
:   | handle | An initialized bindesc handle |
    | --- | --- |
    | callback | A user defined callback to be called on each descriptor |
    | user\_data | User defined data to be given to the callback |

Returns
:   If the walk was finished prematurely by the callback, return the callback's retval, zero otherwise

## [◆ ](#ga7df52ef12aa9572d3a2ff4245529d8fd)bindesc\_get\_size()

| int bindesc\_get\_size | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *result* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Get the size of an image's binary descriptors.

Walks the binary descriptor structure to caluculate the total size of the structure in bytes. This is useful, for instance, if the whole structure is to be copied to RAM.

Parameters
:   | handle | An initialized bindesc handle |
    | --- | --- |
    | result | Pointer to write result to |

Returns
:   0 On success, negative errno otherwise

## [◆ ](#ga724d940fecd648523c3d3bd840785498)bindesc\_open\_flash()

| int bindesc\_open\_flash | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | const struct [device](structdevice.md) \* | *flash\_device* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Open an image's binary descriptors for reading, from flash.

Initializes a bindesc handle for subsequent calls to bindesc API. As opposed to reading bindesc from RAM or memory mapped flash, this backend requires reading the data from flash to an internal buffer using the flash API

Parameters
:   | handle | Bindesc handle to be given to subsequent calls |
    | --- | --- |
    | offset | The offset from the beginning of the flash that the bindesc magic can be found at |
    | flash\_device | Flash device to read descriptors from |

Return values
:   | 0 | On success |
    | --- | --- |
    | -ENOENT | If no bindesc magic was found at the given offset |

## [◆ ](#ga3ed93a855c2ee2981f2ca76450c57d99)bindesc\_open\_memory\_mapped\_flash()

| int bindesc\_open\_memory\_mapped\_flash | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Open an image's binary descriptors for reading, from a memory mapped flash.

Initializes a bindesc handle for subsequent calls to bindesc API. Memory mapped flash is any flash that can be directly accessed by the CPU, without needing to use the flash API for copying the data to RAM.

Parameters
:   | handle | Bindesc handle to be given to subsequent calls |
    | --- | --- |
    | offset | The offset from the beginning of the flash that the bindesc magic can be found at |

Return values
:   | 0 | On success |
    | --- | --- |
    | -ENOENT | If no bindesc magic was found at the given offset |

## [◆ ](#gadec0f4f828c1e4cdcef63b67c0fbafcf)bindesc\_open\_ram()

| int bindesc\_open\_ram | ( | struct [bindesc\_handle](structbindesc__handle.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *address*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_size* ) |

`#include <[bindesc.h](bindesc_8h.md)>`

Open an image's binary descriptors for reading, from RAM.

Initializes a bindesc handle for subsequent calls to bindesc API. It's assumed that the whole bindesc context was copied to RAM prior to calling this function, either by the user or by a bootloader.

Note
:   The given address must be aligned to BINDESC\_ALIGNMENT

Parameters
:   | handle | Bindesc handle to be given to subsequent calls |
    | --- | --- |
    | address | The address that the bindesc magic can be found at |
    | max\_size | Maximum size of the given buffer |

Return values
:   | 0 | On success |
    | --- | --- |
    | -ENOENT | If no bindesc magic was found at the given address |
    | -EINVAL | If the given address is not aligned |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
