---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__hawkbit.html
original_path: doxygen/html/group__hawkbit.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkBit Firmware Over-the-Air

[Third-party](group__third__party.md)

hawkBit Firmware Over-the-Air for Zephyr Project.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [HAWKBIT\_JSON\_URL](#gae2550864ddf596fe544052af73dc1dba)   "/default/controller/v1" |

| Enumerations | |
| --- | --- |
| enum | [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) {     [HAWKBIT\_NETWORKING\_ERROR](#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) , [HAWKBIT\_UNCONFIRMED\_IMAGE](#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) , [HAWKBIT\_PERMISSION\_ERROR](#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) , [HAWKBIT\_METADATA\_ERROR](#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) ,     [HAWKBIT\_DOWNLOAD\_ERROR](#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) , [HAWKBIT\_OK](#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3) , [HAWKBIT\_UPDATE\_INSTALLED](#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) , [HAWKBIT\_NO\_UPDATE](#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) ,     [HAWKBIT\_CANCEL\_UPDATE](#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f) , [HAWKBIT\_PROBE\_IN\_PROGRESS](#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)   } |
|  | Response message from hawkBit. [More...](#ga96c59c754178451d8dbd08b32813220b) |

| Functions | |
| --- | --- |
| int | [hawkbit\_init](#ga0ef6151f205088405de242e012984ca6) (void) |
|  | Init the flash partition. |
| void | [hawkbit\_autohandler](#gac077f546d8947d6b55dcb9276ce98283) (void) |
|  | Runs hawkBit probe and hawkBit update automatically. |
| enum [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) | [hawkbit\_probe](#ga525173f0c3d0ca4e26124a34d098d0b9) (void) |
|  | The hawkBit probe verify if there is some update to be performed. |

## Detailed Description

hawkBit Firmware Over-the-Air for Zephyr Project.

## Macro Definition Documentation

## [◆ ](#gae2550864ddf596fe544052af73dc1dba)HAWKBIT\_JSON\_URL

| #define HAWKBIT\_JSON\_URL   "/default/controller/v1" |
| --- |

`#include <[hawkbit.h](hawkbit_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga96c59c754178451d8dbd08b32813220b)hawkbit\_response

| enum [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) |
| --- |

`#include <[hawkbit.h](hawkbit_8h.md)>`

Response message from hawkBit.

These messages are used to inform the server and the user about the process status of the hawkBit and also used to standardize the errors that may occur.

| Enumerator | |
| --- | --- |
| HAWKBIT\_NETWORKING\_ERROR |  |
| HAWKBIT\_UNCONFIRMED\_IMAGE |  |
| HAWKBIT\_PERMISSION\_ERROR |  |
| HAWKBIT\_METADATA\_ERROR |  |
| HAWKBIT\_DOWNLOAD\_ERROR |  |
| HAWKBIT\_OK |  |
| HAWKBIT\_UPDATE\_INSTALLED |  |
| HAWKBIT\_NO\_UPDATE |  |
| HAWKBIT\_CANCEL\_UPDATE |  |
| HAWKBIT\_PROBE\_IN\_PROGRESS |  |

## Function Documentation

## [◆ ](#gac077f546d8947d6b55dcb9276ce98283)hawkbit\_autohandler()

| void hawkbit\_autohandler | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_8h.md)>`

Runs hawkBit probe and hawkBit update automatically.

The hawkbit\_autohandler handles the whole process in pre-determined time intervals.

## [◆ ](#ga0ef6151f205088405de242e012984ca6)hawkbit\_init()

| int hawkbit\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_8h.md)>`

Init the flash partition.

Returns
:   0 on success, negative on error.

## [◆ ](#ga525173f0c3d0ca4e26124a34d098d0b9)hawkbit\_probe()

| enum [hawkbit\_response](#ga96c59c754178451d8dbd08b32813220b) hawkbit\_probe | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hawkbit.h](hawkbit_8h.md)>`

The hawkBit probe verify if there is some update to be performed.

Returns
:   HAWKBIT\_UPDATE\_INSTALLED has an update available.
:   HAWKBIT\_NO\_UPDATE no update available.
:   HAWKBIT\_NETWORKING\_ERROR fail to connect to the hawkBit server.
:   HAWKBIT\_METADATA\_ERROR fail to parse or to encode the metadata.
:   HAWKBIT\_OK if success.
:   HAWKBIT\_DOWNLOAD\_ERROR fail while downloading the update package.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
