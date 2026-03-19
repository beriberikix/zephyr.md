---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__hawkbit__autohandler.html
original_path: doxygen/html/group__hawkbit__autohandler.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkBit autohandler API

[Third-party](group__third__party.md) » [hawkBit Firmware Over-the-Air](group__hawkbit.md)

hawkBit autohandler API.
[More...](#details)

| Functions | |
| --- | --- |
| void | [hawkbit\_autohandler](#ga41865255aa3020a34816c23ae7977f20) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) auto\_reschedule) |
|  | Runs hawkBit probe and hawkBit update automatically. |
| enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) | [hawkbit\_autohandler\_wait](#ga6d13b3d7b9a61d06a6eaa346189a08c6) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for the autohandler to finish. |
| int | [hawkbit\_autohandler\_cancel](#gabc27308bb974d6e0b9650476243e5e9a) (void) |
|  | Cancel the run of the hawkBit autohandler. |
| int | [hawkbit\_autohandler\_set\_delay](#ga47fe3e9cd227fd4da332e9eeff81f991) ([k\_timeout\_t](structk__timeout__t.md) timeout, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) if\_bigger) |
|  | Set the delay for the next run of the autohandler. |

## Detailed Description

hawkBit autohandler API.

## Function Documentation

## [◆ ](#ga41865255aa3020a34816c23ae7977f20)hawkbit\_autohandler()

| void hawkbit\_autohandler | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *auto\_reschedule* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[autohandler.h](autohandler_8h.md)>`

Runs hawkBit probe and hawkBit update automatically.

The hawkbit\_autohandler handles the whole process in pre-determined time intervals.

Parameters
:   | auto\_reschedule | If true, the handler will reschedule itself |
    | --- | --- |

## [◆ ](#gabc27308bb974d6e0b9650476243e5e9a)hawkbit\_autohandler\_cancel()

| int hawkbit\_autohandler\_cancel | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[autohandler.h](autohandler_8h.md)>`

Cancel the run of the hawkBit autohandler.

Returns
:   a value from [k\_work\_cancel\_delayable()](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4 "Cancel delayable work.").

## [◆ ](#ga47fe3e9cd227fd4da332e9eeff81f991)hawkbit\_autohandler\_set\_delay()

| int hawkbit\_autohandler\_set\_delay | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *if\_bigger* ) |

`#include <[autohandler.h](autohandler_8h.md)>`

Set the delay for the next run of the autohandler.

This function will only delay the next run of the autohandler. The delay will not persist after the autohandler runs.

Parameters
:   | timeout | The delay to set. |
    | --- | --- |
    | if\_bigger | If true, the delay will be set only if the new delay is bigger than the current one. |

Return values
:   | 0 | if *if\_bigger* was true and the current delay was bigger than the new one. |
    | --- | --- |
    | otherwise,a | value from [k\_work\_reschedule()](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648 "Reschedule a work item to the system work queue after a delay."). |

## [◆ ](#ga6d13b3d7b9a61d06a6eaa346189a08c6)hawkbit\_autohandler\_wait()

| enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) hawkbit\_autohandler\_wait | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[autohandler.h](autohandler_8h.md)>`

Wait for the autohandler to finish.

Parameters
:   | events | Set of desired events on which to wait. Set to [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd) to wait for the autohandler to finish one run, or [BIT()](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") together with a value from [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b "Response message from hawkBit.") to wait for a specific event. |
    | --- | --- |
    | timeout | Waiting period for the desired set of events or one of the special values [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f "Generate null timeout delay.") and [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca "Generate infinite timeout delay."). |

Returns
:   A value from [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b "Response message from hawkBit.").

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
