---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/autohandler_8h.html
original_path: doxygen/html/autohandler_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

autohandler.h File Reference

hawkBit autohandler header file
[More...](#details)

`#include <[zephyr/mgmt/hawkbit/hawkbit.h](hawkbit_2hawkbit_8h_source.md)>`

[Go to the source code of this file.](autohandler_8h_source.md)

| Functions | |
| --- | --- |
| void | [hawkbit\_autohandler](group__hawkbit__autohandler.md#ga41865255aa3020a34816c23ae7977f20) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) auto\_reschedule) |
|  | Runs hawkBit probe and hawkBit update automatically. |
| enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) | [hawkbit\_autohandler\_wait](group__hawkbit__autohandler.md#ga6d13b3d7b9a61d06a6eaa346189a08c6) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for the autohandler to finish. |
| int | [hawkbit\_autohandler\_cancel](group__hawkbit__autohandler.md#gabc27308bb974d6e0b9650476243e5e9a) (void) |
|  | Cancel the run of the hawkBit autohandler. |
| int | [hawkbit\_autohandler\_set\_delay](group__hawkbit__autohandler.md#ga47fe3e9cd227fd4da332e9eeff81f991) ([k\_timeout\_t](structk__timeout__t.md) timeout, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) if\_bigger) |
|  | Set the delay for the next run of the autohandler. |

## Detailed Description

hawkBit autohandler header file

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit](dir_a48dfaa3f142fb7c063e17169510ae85.md)
- [autohandler.h](autohandler_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
