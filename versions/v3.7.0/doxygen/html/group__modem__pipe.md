---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__modem__pipe.html
original_path: doxygen/html/group__modem__pipe.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Modem Pipe

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md)

Modem Pipe.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_pipe\_api\_callback](#gaf64941177c179cb9086a5736d1ea56f1)) (struct modem\_pipe \*pipe, enum [modem\_pipe\_event](#gab9dd98d92d6446dd43852d280574f67a) event, void \*user\_data) |

| Enumerations | |
| --- | --- |
| enum | [modem\_pipe\_event](#gab9dd98d92d6446dd43852d280574f67a) { [MODEM\_PIPE\_EVENT\_OPENED](#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891) = 0 , [MODEM\_PIPE\_EVENT\_RECEIVE\_READY](#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4) , [MODEM\_PIPE\_EVENT\_TRANSMIT\_IDLE](#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4) , [MODEM\_PIPE\_EVENT\_CLOSED](#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f) } |
|  | Modem pipe event. [More...](#gab9dd98d92d6446dd43852d280574f67a) |

| Functions | |
| --- | --- |
| int | [modem\_pipe\_open](#gad53acf3b0641bcc1779d85d5af6fb412) (struct modem\_pipe \*pipe) |
|  | Open pipe. |
| int | [modem\_pipe\_open\_async](#ga0a7312eadaa76b433fe8a319d8c9ec74) (struct modem\_pipe \*pipe) |
|  | Open pipe asynchronously. |
| void | [modem\_pipe\_attach](#ga68674becf672b1009d629813c041b868) (struct modem\_pipe \*pipe, [modem\_pipe\_api\_callback](#gaf64941177c179cb9086a5736d1ea56f1) callback, void \*user\_data) |
|  | Attach pipe to callback. |
| int | [modem\_pipe\_transmit](#ga72311fcb03f138d57e230af60340c9f6) (struct modem\_pipe \*pipe, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Transmit data through pipe. |
| int | [modem\_pipe\_receive](#gab030b4040725ad4dab2399840ef73fde) (struct modem\_pipe \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Receive data through pipe. |
| void | [modem\_pipe\_release](#gad1a9fa3dba49a86c187328b7ee022293) (struct modem\_pipe \*pipe) |
|  | Clear callback. |
| int | [modem\_pipe\_close](#ga43d885be0f284cc580e66572b4bab065) (struct modem\_pipe \*pipe) |
|  | Close pipe. |
| int | [modem\_pipe\_close\_async](#ga9814c9a1a5da33b2787ac058a6a037f5) (struct modem\_pipe \*pipe) |
|  | Close pipe asynchronously. |

## Detailed Description

Modem Pipe.

## Typedef Documentation

## [◆ ](#gaf64941177c179cb9086a5736d1ea56f1)modem\_pipe\_api\_callback

| typedef void(\* modem\_pipe\_api\_callback) (struct modem\_pipe \*pipe, enum [modem\_pipe\_event](#gab9dd98d92d6446dd43852d280574f67a) event, void \*user\_data) |
| --- |

`#include <[pipe.h](pipe_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gab9dd98d92d6446dd43852d280574f67a)modem\_pipe\_event

| enum [modem\_pipe\_event](#gab9dd98d92d6446dd43852d280574f67a) |
| --- |

`#include <[pipe.h](pipe_8h.md)>`

Modem pipe event.

| Enumerator | |
| --- | --- |
| MODEM\_PIPE\_EVENT\_OPENED |  |
| MODEM\_PIPE\_EVENT\_RECEIVE\_READY |  |
| MODEM\_PIPE\_EVENT\_TRANSMIT\_IDLE |  |
| MODEM\_PIPE\_EVENT\_CLOSED |  |

## Function Documentation

## [◆ ](#ga68674becf672b1009d629813c041b868)modem\_pipe\_attach()

| void modem\_pipe\_attach | ( | struct modem\_pipe \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | [modem\_pipe\_api\_callback](#gaf64941177c179cb9086a5736d1ea56f1) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[pipe.h](pipe_8h.md)>`

Attach pipe to callback.

Parameters
:   | pipe | Pipe instance |
    | --- | --- |
    | callback | Callback called when pipe event occurs |
    | user\_data | Free to use user data passed with callback |

Note
:   The MODEM\_PIPE\_EVENT\_RECEIVE\_READY event is invoked immediately if pipe has pending data ready to receive.

## [◆ ](#ga43d885be0f284cc580e66572b4bab065)modem\_pipe\_close()

| int modem\_pipe\_close | ( | struct modem\_pipe \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipe.h](pipe_8h.md)>`

Close pipe.

Parameters
:   | pipe | Pipe instance |
    | --- | --- |

Return values
:   | 0 | if pipe open was called closed or pipe was already closed |
    | --- | --- |
    | -errno | code otherwise |

Warning
:   Be cautious when using this synchronous version of the call. It may block the calling thread, which in the case of the system workqueue can result in a deadlock until this call times out waiting for the pipe to be closed.

## [◆ ](#ga9814c9a1a5da33b2787ac058a6a037f5)modem\_pipe\_close\_async()

| int modem\_pipe\_close\_async | ( | struct modem\_pipe \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipe.h](pipe_8h.md)>`

Close pipe asynchronously.

Parameters
:   | pipe | Pipe instance |
    | --- | --- |

Note
:   The MODEM\_PIPE\_EVENT\_CLOSED event is invoked immediately if pipe is already closed.

Return values
:   | 0 | if pipe close was called successfully or pipe was already closed |
    | --- | --- |
    | -errno | code otherwise |

## [◆ ](#gad53acf3b0641bcc1779d85d5af6fb412)modem\_pipe\_open()

| int modem\_pipe\_open | ( | struct modem\_pipe \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipe.h](pipe_8h.md)>`

Open pipe.

Parameters
:   | pipe | Pipe instance |
    | --- | --- |

Return values
:   | 0 | if pipe was successfully opened or was already open |
    | --- | --- |
    | -errno | code otherwise |

Warning
:   Be cautious when using this synchronous version of the call. It may block the calling thread, which in the case of the system workqueue can result in a deadlock until this call times out waiting for the pipe to be open.

## [◆ ](#ga0a7312eadaa76b433fe8a319d8c9ec74)modem\_pipe\_open\_async()

| int modem\_pipe\_open\_async | ( | struct modem\_pipe \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipe.h](pipe_8h.md)>`

Open pipe asynchronously.

Parameters
:   | pipe | Pipe instance |
    | --- | --- |

Note
:   The MODEM\_PIPE\_EVENT\_OPENED event is invoked immediately if pipe is already opened.

Return values
:   | 0 | if pipe open was called successfully or pipe was already open |
    | --- | --- |
    | -errno | code otherwise |

## [◆ ](#gab030b4040725ad4dab2399840ef73fde)modem\_pipe\_receive()

| int modem\_pipe\_receive | ( | struct modem\_pipe \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[pipe.h](pipe_8h.md)>`

Receive data through pipe.

Parameters
:   | pipe | Pipe to receive from |
    | --- | --- |
    | buf | Destination for received data; must not be already in use in a modem module. |
    | size | Capacity of destination for received data |

Return values
:   | Number | of bytes received from pipe |
    | --- | --- |
    | -EPERM | if pipe is closed |
    | -errno | code on error |

Warning
:   This call must be non-blocking

## [◆ ](#gad1a9fa3dba49a86c187328b7ee022293)modem\_pipe\_release()

| void modem\_pipe\_release | ( | struct modem\_pipe \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pipe.h](pipe_8h.md)>`

Clear callback.

Parameters
:   | pipe | Pipe instance |
    | --- | --- |

## [◆ ](#ga72311fcb03f138d57e230af60340c9f6)modem\_pipe\_transmit()

| int modem\_pipe\_transmit | ( | struct modem\_pipe \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[pipe.h](pipe_8h.md)>`

Transmit data through pipe.

Parameters
:   | pipe | Pipe to transmit through |
    | --- | --- |
    | buf | Data to transmit |
    | size | Number of bytes to transmit |

Return values
:   | Number | of bytes placed in pipe |
    | --- | --- |
    | -EPERM | if pipe is closed |
    | -errno | code on error |

Warning
:   This call must be non-blocking

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
