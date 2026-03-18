---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__updatehub.html
original_path: doxygen/html/group__updatehub.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

UpdateHub Firmware Over-the-Air

[Third-party](group__third__party.md)

UpdateHub Firmware Over-the-Air for Zephyr Project.
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [updatehub\_response](#ga6e6eb49b1e4b558cd8be0da8b45a07b8) {     [UPDATEHUB\_NETWORKING\_ERROR](#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a) = 0 , [UPDATEHUB\_INCOMPATIBLE\_HARDWARE](#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76) , [UPDATEHUB\_UNCONFIRMED\_IMAGE](#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037) , [UPDATEHUB\_METADATA\_ERROR](#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171) ,     [UPDATEHUB\_DOWNLOAD\_ERROR](#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f) , [UPDATEHUB\_INSTALL\_ERROR](#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f) , [UPDATEHUB\_FLASH\_INIT\_ERROR](#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2) , [UPDATEHUB\_OK](#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43) ,     [UPDATEHUB\_HAS\_UPDATE](#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c) , [UPDATEHUB\_NO\_UPDATE](#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730)   } |
|  | Responses messages from UpdateHub. [More...](#ga6e6eb49b1e4b558cd8be0da8b45a07b8) |

| Functions | |
| --- | --- |
| void | [updatehub\_autohandler](#ga2a1665a1fe1b191bbc7d80c4bbaa4299) (void) |
|  | Runs UpdateHub probe and UpdateHub update automatically. |
| enum [updatehub\_response](#ga6e6eb49b1e4b558cd8be0da8b45a07b8) | [updatehub\_probe](#ga89d1715033200c89a7587dd229944a23) (void) |
|  | The UpdateHub probe verify if there is some update to be performed. |
| enum [updatehub\_response](#ga6e6eb49b1e4b558cd8be0da8b45a07b8) | [updatehub\_update](#gabb00cf9b63ce13554c26286c0c37fa8a) (void) |
|  | Apply the update package. |
| int | [updatehub\_confirm](#gad1a3f6b1d91a7c9969a3411e0fd74f72) (void) |
|  | Confirm that image is running as expected. |
| int | [updatehub\_reboot](#gac433e995a18418771cac9fe4559ce84b) (void) |
|  | Request system to reboot. |

## Detailed Description

UpdateHub Firmware Over-the-Air for Zephyr Project.

## Enumeration Type Documentation

## [◆ ](#ga6e6eb49b1e4b558cd8be0da8b45a07b8)updatehub\_response

| enum [updatehub\_response](#ga6e6eb49b1e4b558cd8be0da8b45a07b8) |
| --- |

`#include <[updatehub.h](updatehub_8h.md)>`

Responses messages from UpdateHub.

These messages are used to inform the server and the user about the process status of the UpdateHub and also used to standardize the errors that may occur.

| Enumerator | |
| --- | --- |
| UPDATEHUB\_NETWORKING\_ERROR |  |
| UPDATEHUB\_INCOMPATIBLE\_HARDWARE |  |
| UPDATEHUB\_UNCONFIRMED\_IMAGE |  |
| UPDATEHUB\_METADATA\_ERROR |  |
| UPDATEHUB\_DOWNLOAD\_ERROR |  |
| UPDATEHUB\_INSTALL\_ERROR |  |
| UPDATEHUB\_FLASH\_INIT\_ERROR |  |
| UPDATEHUB\_OK |  |
| UPDATEHUB\_HAS\_UPDATE |  |
| UPDATEHUB\_NO\_UPDATE |  |

## Function Documentation

## [◆ ](#ga2a1665a1fe1b191bbc7d80c4bbaa4299)updatehub\_autohandler()

| void updatehub\_autohandler | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[updatehub.h](updatehub_8h.md)>`

Runs UpdateHub probe and UpdateHub update automatically.

The updatehub\_autohandler handles the whole process in pre-determined time intervals.

## [◆ ](#gad1a3f6b1d91a7c9969a3411e0fd74f72)updatehub\_confirm()

| int updatehub\_confirm | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[updatehub.h](updatehub_8h.md)>`

Confirm that image is running as expected.

Must be used before the UpdateHub probe. It should be one of first actions after reboot.

Returns
:   Return 0 if success otherwise a negative 'errno' value.

## [◆ ](#ga89d1715033200c89a7587dd229944a23)updatehub\_probe()

| enum [updatehub\_response](#ga6e6eb49b1e4b558cd8be0da8b45a07b8) updatehub\_probe | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[updatehub.h](updatehub_8h.md)>`

The UpdateHub probe verify if there is some update to be performed.

Returns
:   UPDATEHUB\_HAS\_UPDATE has an update available.
:   UPDATEHUB\_NO\_UPDATE no update available.
:   UPDATEHUB\_NETWORKING\_ERROR fail to connect to the UpdateHub server.
:   UPDATEHUB\_INCOMPATIBLE\_HARDWARE if Incompatible hardware.
:   UPDATEHUB\_METADATA\_ERROR fail to parse or to encode the metadata.

## [◆ ](#gac433e995a18418771cac9fe4559ce84b)updatehub\_reboot()

| int updatehub\_reboot | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[updatehub.h](updatehub_8h.md)>`

Request system to reboot.

Returns
:   Return 0 if success otherwise a negative 'errno' value.

## [◆ ](#gabb00cf9b63ce13554c26286c0c37fa8a)updatehub\_update()

| enum [updatehub\_response](#ga6e6eb49b1e4b558cd8be0da8b45a07b8) updatehub\_update | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[updatehub.h](updatehub_8h.md)>`

Apply the update package.

Must be used after the UpdateHub probe, if you have updates to be made, will perform the installation of the new image and the hardware will rebooting.

Returns
:   Return UPDATEHUB\_OK if success
:   UPDATEHUB\_NETWORKING\_ERROR if fail to connect to the server.
:   UPDATEHUB\_DOWNLOAD\_ERROR fail while downloading the update package.
:   UPDATEHUB\_INSTALL\_ERROR fail while installing the update package.
:   UPDATEHUB\_FLASH\_INIT\_ERROR fail to initialize the flash.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
