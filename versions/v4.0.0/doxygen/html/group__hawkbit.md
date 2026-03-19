---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__hawkbit.html
original_path: doxygen/html/group__hawkbit.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkBit Firmware Over-the-Air

[Third-party](group__third__party.md)

hawkBit Firmware Over-the-Air for Zephyr Project.
[More...](#details)

| Topics | |
| --- | --- |
|  | [hawkBit autohandler API](group__hawkbit__autohandler.md) |
|  | hawkBit autohandler API. |
|  | [hawkBit configuration API](group__hawkbit__config.md) |
|  | hawkBit configuration API. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [hawkbit\_config\_device\_data\_cb\_handler\_t](#ga2774769ec44f2793895b5d783b4dceda)) (const char \*device\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Callback to provide the custom data to the hawkBit server. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [hawkbit\_get\_device\_identity\_cb\_handler\_t](#ga154220c632a7594c0630cdcd79385055)) (char \*id, int id\_max\_len) |
|  | Callback to get the device identity. |

| Enumerations | |
| --- | --- |
| enum | [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) {     [HAWKBIT\_NO\_RESPONSE](#gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9) , [HAWKBIT\_NETWORKING\_ERROR](#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) , [HAWKBIT\_UNCONFIRMED\_IMAGE](#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) , [HAWKBIT\_PERMISSION\_ERROR](#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) ,     [HAWKBIT\_METADATA\_ERROR](#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) , [HAWKBIT\_DOWNLOAD\_ERROR](#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) , [HAWKBIT\_OK](#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3) , [HAWKBIT\_UPDATE\_INSTALLED](#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) ,     [HAWKBIT\_NO\_UPDATE](#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) , [HAWKBIT\_CANCEL\_UPDATE](#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f) , [HAWKBIT\_NOT\_INITIALIZED](#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708) , [HAWKBIT\_PROBE\_IN\_PROGRESS](#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)   } |
|  | Response message from hawkBit. [More...](#ga96c59c754178451d8dbd08b32813220b) |

| Functions | |
| --- | --- |
| int | [hawkbit\_set\_custom\_data\_cb](#gad8e83255a969eb61244b1edfd0b95e5d) ([hawkbit\_config\_device\_data\_cb\_handler\_t](#ga2774769ec44f2793895b5d783b4dceda) cb) |
|  | Set the custom data callback. |
| int | [hawkbit\_init](#ga0ef6151f205088405de242e012984ca6) (void) |
|  | Init the flash partition. |
| enum [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) | [hawkbit\_probe](#ga525173f0c3d0ca4e26124a34d098d0b9) (void) |
|  | The hawkBit probe verify if there is some update to be performed. |
| void | [hawkbit\_reboot](#ga03631b12a4107d660bac14bfd33bfebd) (void) |
|  | Request system to reboot. |
| int | [hawkbit\_set\_device\_identity\_cb](#ga4ce085b8f2bb46af2c2e9f3f2879d633) ([hawkbit\_get\_device\_identity\_cb\_handler\_t](#ga154220c632a7594c0630cdcd79385055) cb) |
|  | Set the device identity callback. |
| int | [hawkbit\_reset\_action\_id](#ga26f0066c87c57b500170ac377b560bb4) (void) |
|  | Resets the hawkBit action id, that is saved in settings. |

## Detailed Description

hawkBit Firmware Over-the-Air for Zephyr Project.

## Typedef Documentation

## [◆ ](#ga2774769ec44f2793895b5d783b4dceda)hawkbit\_config\_device\_data\_cb\_handler\_t

| typedef int(\* hawkbit\_config\_device\_data\_cb\_handler\_t) (const char \*device\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
| --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Callback to provide the custom data to the hawkBit server.

This callback is used to provide the custom data to the hawkBit server. The custom data is used to provide the hawkBit server with the device specific data.

Parameters
:   | device\_id | The device ID. |
    | --- | --- |
    | buffer | The buffer to store the json. |
    | buffer\_size | The size of the buffer. |

## [◆ ](#ga154220c632a7594c0630cdcd79385055)hawkbit\_get\_device\_identity\_cb\_handler\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* hawkbit\_get\_device\_identity\_cb\_handler\_t) (char \*id, int id\_max\_len) |
| --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Callback to get the device identity.

Parameters
:   | id | Pointer to the buffer to store the device identity |
    | --- | --- |
    | id\_max\_len | The maximum length of the buffer |

## Enumeration Type Documentation

## [◆ ](#ga96c59c754178451d8dbd08b32813220b)hawkbit\_response

| enum [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) |
| --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Response message from hawkBit.

These messages are used to inform the server and the user about the process status of the hawkBit and also used to standardize the errors that may occur.

| Enumerator | |
| --- | --- |
| HAWKBIT\_NO\_RESPONSE | matching events were not received within the specified time |
| HAWKBIT\_NETWORKING\_ERROR | fail to connect to the hawkBit server |
| HAWKBIT\_UNCONFIRMED\_IMAGE | image is unconfirmed |
| HAWKBIT\_PERMISSION\_ERROR | fail to get the permission to access the hawkBit server |
| HAWKBIT\_METADATA\_ERROR | fail to parse or to encode the metadata |
| HAWKBIT\_DOWNLOAD\_ERROR | fail while downloading the update package |
| HAWKBIT\_OK | image was already updated |
| HAWKBIT\_UPDATE\_INSTALLED | an update was installed.  Reboot is required to apply it |
| HAWKBIT\_NO\_UPDATE | no update was available |
| HAWKBIT\_CANCEL\_UPDATE | update was cancelled by the server |
| HAWKBIT\_NOT\_INITIALIZED | hawkBit is not initialized |
| HAWKBIT\_PROBE\_IN\_PROGRESS | probe is currently running |

## Function Documentation

## [◆ ](#ga0ef6151f205088405de242e012984ca6)hawkbit\_init()

| int hawkbit\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Init the flash partition.

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | if init fails. |

## [◆ ](#ga525173f0c3d0ca4e26124a34d098d0b9)hawkbit\_probe()

| enum [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) hawkbit\_probe | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

The hawkBit probe verify if there is some update to be performed.

Returns
:   A value from [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b).

## [◆ ](#ga03631b12a4107d660bac14bfd33bfebd)hawkbit\_reboot()

| void hawkbit\_reboot | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Request system to reboot.

## [◆ ](#ga26f0066c87c57b500170ac377b560bb4)hawkbit\_reset\_action\_id()

| int hawkbit\_reset\_action\_id | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Resets the hawkBit action id, that is saved in settings.

This should be done after changing the hawkBit server.

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EAGAIN | if probe is currently running. |
    | -EIO | if the action id could not be reset. |

## [◆ ](#gad8e83255a969eb61244b1edfd0b95e5d)hawkbit\_set\_custom\_data\_cb()

| int hawkbit\_set\_custom\_data\_cb | ( | [hawkbit\_config\_device\_data\_cb\_handler\_t](#ga2774769ec44f2793895b5d783b4dceda) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Set the custom data callback.

This function is used to set the custom data callback. The callback is used to provide the custom data to the hawkBit server.

Parameters
:   | cb | The callback function. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | if the callback is NULL. |

## [◆ ](#ga4ce085b8f2bb46af2c2e9f3f2879d633)hawkbit\_set\_device\_identity\_cb()

| int hawkbit\_set\_device\_identity\_cb | ( | [hawkbit\_get\_device\_identity\_cb\_handler\_t](#ga154220c632a7594c0630cdcd79385055) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_2hawkbit_8h.md)>`

Set the device identity callback.

This function is used to set a custom device identity callback.

Parameters
:   | cb | The callback function. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | if the callback is NULL. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
