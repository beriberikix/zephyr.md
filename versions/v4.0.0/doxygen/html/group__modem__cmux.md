---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__modem__cmux.html
original_path: doxygen/html/group__modem__cmux.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Modem CMUX

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md)

Modem CMUX.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [modem\_cmux\_config](structmodem__cmux__config.md) |
|  | Contains CMUX instance configuration data. [More...](structmodem__cmux__config.md#details) |
| struct | [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) |
|  | CMUX DLCI configuration. [More...](structmodem__cmux__dlci__config.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_cmux\_callback](#ga998b334620c9970ebbb0bcf620ea5923)) (struct modem\_cmux \*cmux, enum [modem\_cmux\_event](#gab60ea756d37bd9ed59f07c6380952d36) event, void \*user\_data) |

| Enumerations | |
| --- | --- |
| enum | [modem\_cmux\_event](#gab60ea756d37bd9ed59f07c6380952d36) { [MODEM\_CMUX\_EVENT\_CONNECTED](#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2) = 0 , [MODEM\_CMUX\_EVENT\_DISCONNECTED](#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21) } |

| Functions | |
| --- | --- |
| void | [modem\_cmux\_init](#gad72973ad82504ae64d184ce11572ab88) (struct modem\_cmux \*cmux, const struct [modem\_cmux\_config](structmodem__cmux__config.md) \*config) |
|  | Initialize CMUX instance. |
| struct modem\_pipe \* | [modem\_cmux\_dlci\_init](#gabfd8e728eb8940b4093ae132b7add7d7) (struct modem\_cmux \*cmux, struct modem\_cmux\_dlci \*dlci, const struct [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) \*config) |
|  | Initialize DLCI instance and register it with CMUX instance. |
| int | [modem\_cmux\_attach](#gab85f5c71a3cf131ff97aa47749197cb3) (struct modem\_cmux \*cmux, struct modem\_pipe \*pipe) |
|  | Attach CMUX instance to pipe. |
| int | [modem\_cmux\_connect](#ga362cd4b2dff122e3bbaee02b378dd226) (struct modem\_cmux \*cmux) |
|  | Connect CMUX instance. |
| int | [modem\_cmux\_connect\_async](#ga9fa4a1cd9cf1e1c253e621c650a611d0) (struct modem\_cmux \*cmux) |
|  | Connect CMUX instance asynchronously. |
| int | [modem\_cmux\_disconnect](#ga482171f67db206780d0b8a2cf5b32a93) (struct modem\_cmux \*cmux) |
|  | Close down and disconnect CMUX instance. |
| int | [modem\_cmux\_disconnect\_async](#ga988c8efbebf63871730918d862b7c490) (struct modem\_cmux \*cmux) |
|  | Close down and disconnect CMUX instance asynchronously. |
| void | [modem\_cmux\_release](#gadc7c6ff92b7ac52717151bd6bf1efdff) (struct modem\_cmux \*cmux) |
|  | Release CMUX instance from pipe. |

## Detailed Description

Modem CMUX.

## Typedef Documentation

## [◆ ](#ga998b334620c9970ebbb0bcf620ea5923)modem\_cmux\_callback

| typedef void(\* modem\_cmux\_callback) (struct modem\_cmux \*cmux, enum [modem\_cmux\_event](#gab60ea756d37bd9ed59f07c6380952d36) event, void \*user\_data) |
| --- |

`#include <[cmux.h](cmux_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gab60ea756d37bd9ed59f07c6380952d36)modem\_cmux\_event

| enum [modem\_cmux\_event](#gab60ea756d37bd9ed59f07c6380952d36) |
| --- |

`#include <[cmux.h](cmux_8h.md)>`

| Enumerator | |
| --- | --- |
| MODEM\_CMUX\_EVENT\_CONNECTED |  |
| MODEM\_CMUX\_EVENT\_DISCONNECTED |  |

## Function Documentation

## [◆ ](#gab85f5c71a3cf131ff97aa47749197cb3)modem\_cmux\_attach()

| int modem\_cmux\_attach | ( | struct modem\_cmux \* | *cmux*, |
| --- | --- | --- | --- |
|  |  | struct modem\_pipe \* | *pipe* ) |

`#include <[cmux.h](cmux_8h.md)>`

Attach CMUX instance to pipe.

Parameters
:   | cmux | CMUX instance |
    | --- | --- |
    | pipe | Pipe instance to attach CMUX instance to |

## [◆ ](#ga362cd4b2dff122e3bbaee02b378dd226)modem\_cmux\_connect()

| int modem\_cmux\_connect | ( | struct modem\_cmux \* | *cmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cmux.h](cmux_8h.md)>`

Connect CMUX instance.

This will send a CMUX connect request to target on the serial bus. If successful, DLCI channels can be now be opened using [modem\_pipe\_open()](group__modem__pipe.md#ga7521ac0aeda8027c47741237e8312bf0 "Open pipe.")

Parameters
:   | cmux | CMUX instance |
    | --- | --- |

Note
:   When connected, the bus pipe must not be used directly

## [◆ ](#ga9fa4a1cd9cf1e1c253e621c650a611d0)modem\_cmux\_connect\_async()

| int modem\_cmux\_connect\_async | ( | struct modem\_cmux \* | *cmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cmux.h](cmux_8h.md)>`

Connect CMUX instance asynchronously.

This will send a CMUX connect request to target on the serial bus. If successful, DLCI channels can be now be opened using [modem\_pipe\_open()](group__modem__pipe.md#ga7521ac0aeda8027c47741237e8312bf0 "Open pipe.").

Parameters
:   | cmux | CMUX instance |
    | --- | --- |

Note
:   When connected, the bus pipe must not be used directly

## [◆ ](#ga482171f67db206780d0b8a2cf5b32a93)modem\_cmux\_disconnect()

| int modem\_cmux\_disconnect | ( | struct modem\_cmux \* | *cmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cmux.h](cmux_8h.md)>`

Close down and disconnect CMUX instance.

This will close all open DLCI channels, and close down the CMUX connection.

Parameters
:   | cmux | CMUX instance |
    | --- | --- |

Note
:   The bus pipe must be released using [modem\_cmux\_release()](#gadc7c6ff92b7ac52717151bd6bf1efdff) after disconnecting before being reused.

## [◆ ](#ga988c8efbebf63871730918d862b7c490)modem\_cmux\_disconnect\_async()

| int modem\_cmux\_disconnect\_async | ( | struct modem\_cmux \* | *cmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cmux.h](cmux_8h.md)>`

Close down and disconnect CMUX instance asynchronously.

This will close all open DLCI channels, and close down the CMUX connection.

Parameters
:   | cmux | CMUX instance |
    | --- | --- |

Note
:   The bus pipe must be released using [modem\_cmux\_release()](#gadc7c6ff92b7ac52717151bd6bf1efdff) after disconnecting before being reused.

## [◆ ](#gabfd8e728eb8940b4093ae132b7add7d7)modem\_cmux\_dlci\_init()

| struct modem\_pipe \* modem\_cmux\_dlci\_init | ( | struct modem\_cmux \* | *cmux*, |
| --- | --- | --- | --- |
|  |  | struct modem\_cmux\_dlci \* | *dlci*, |
|  |  | const struct [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) \* | *config* ) |

`#include <[cmux.h](cmux_8h.md)>`

Initialize DLCI instance and register it with CMUX instance.

Parameters
:   | cmux | CMUX instance which the DLCI will be registered to |
    | --- | --- |
    | dlci | DLCI instance which will be registered and configured |
    | config | Configuration to apply to DLCI instance |

## [◆ ](#gad72973ad82504ae64d184ce11572ab88)modem\_cmux\_init()

| void modem\_cmux\_init | ( | struct modem\_cmux \* | *cmux*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_cmux\_config](structmodem__cmux__config.md) \* | *config* ) |

`#include <[cmux.h](cmux_8h.md)>`

Initialize CMUX instance.

Parameters
:   | cmux | CMUX instance |
    | --- | --- |
    | config | Configuration to apply to CMUX instance |

## [◆ ](#gadc7c6ff92b7ac52717151bd6bf1efdff)modem\_cmux\_release()

| void modem\_cmux\_release | ( | struct modem\_cmux \* | *cmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cmux.h](cmux_8h.md)>`

Release CMUX instance from pipe.

Releases the pipe and hard resets the CMUX instance internally. CMUX should be disconnected using [modem\_cmux\_disconnect()](#ga482171f67db206780d0b8a2cf5b32a93).

Parameters
:   | cmux | CMUX instance |
    | --- | --- |

Note
:   The bus pipe can be used directly again after CMUX instance is released.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
