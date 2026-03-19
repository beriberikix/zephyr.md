---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/auxdisplay_8h.html
original_path: doxygen/html/auxdisplay_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

auxdisplay.h File Reference

Public API for auxiliary (textual/non-graphical) display drivers.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/auxdisplay.h>`

[Go to the source code of this file.](auxdisplay_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [auxdisplay\_light](structauxdisplay__light.md) |
|  | Light levels for brightness and/or backlight. [More...](structauxdisplay__light.md#details) |
| struct | [auxdisplay\_capabilities](structauxdisplay__capabilities.md) |
|  | Structure holding display capabilities. [More...](structauxdisplay__capabilities.md#details) |
| struct | [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) |
|  | Structure for a custom command. [More...](structauxdisplay__custom__data.md#details) |
| struct | [auxdisplay\_character](structauxdisplay__character.md) |
|  | Structure for a custom character. [More...](structauxdisplay__character.md#details) |

| Macros | |
| --- | --- |
| #define | [AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED](group__auxdisplay__interface.md#ga0bd1d97b360f3138887a5e3e4729e01b)   0 |
|  | Used for minimum and maximum brightness/backlight values if not supported. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2) |
|  | Used to describe the mode of an auxiliary (text) display. |

| Enumerations | |
| --- | --- |
| enum | [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) { [AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) = 0 , [AUXDISPLAY\_POSITION\_RELATIVE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28) , [AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558) , [AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23) } |
|  | Used for moving the cursor or display position. [More...](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) |
| enum | [auxdisplay\_direction](group__auxdisplay__interface.md#ga5f95ac69e18091883e7121103014be10) { [AUXDISPLAY\_DIRECTION\_RIGHT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599) = 0 , [AUXDISPLAY\_DIRECTION\_LEFT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352) , [AUXDISPLAY\_DIRECTION\_COUNT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3) } |
|  | Used for setting character append position. [More...](group__auxdisplay__interface.md#ga5f95ac69e18091883e7121103014be10) |

| Functions | |
| --- | --- |
| int | [auxdisplay\_display\_on](group__auxdisplay__interface.md#gaffb3c1c41d810355fe2da3558ebba0c2) (const struct [device](structdevice.md) \*dev) |
|  | Turn display on. |
| int | [auxdisplay\_display\_off](group__auxdisplay__interface.md#ga625f399720417715090793c7f6d63f7e) (const struct [device](structdevice.md) \*dev) |
|  | Turn display off. |
| int | [auxdisplay\_cursor\_set\_enabled](group__auxdisplay__interface.md#ga7191475b362f728cc92eb07cb1f2ed00) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Set cursor enabled status on an auxiliary display. |
| int | [auxdisplay\_position\_blinking\_set\_enabled](group__auxdisplay__interface.md#ga7102ec9941f8b3131a18e4ff7b640241) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Set cursor blinking status on an auxiliary display. |
| int | [auxdisplay\_cursor\_shift\_set](group__auxdisplay__interface.md#gafb18729b4897cea83dbfc1c7241f5b2d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) display\_shift) |
|  | Set cursor shift after character write and display shift. |
| int | [auxdisplay\_cursor\_position\_set](group__auxdisplay__interface.md#ga9c6302789d9cc9e481dd7c54ef370988) (const struct [device](structdevice.md) \*dev, enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y) |
|  | Set cursor (and write position) on an auxiliary display. |
| int | [auxdisplay\_cursor\_position\_get](group__auxdisplay__interface.md#ga37bd5403c876ff294be5ea72292de4b4) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y) |
|  | Get current cursor on an auxiliary display. |
| int | [auxdisplay\_display\_position\_set](group__auxdisplay__interface.md#ga02e8e930203cfb1410752a0ffee9a34e) (const struct [device](structdevice.md) \*dev, enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y) |
|  | Set display position on an auxiliary display. |
| int | [auxdisplay\_display\_position\_get](group__auxdisplay__interface.md#ga1f9e363765d715edb899901a14c54674) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y) |
|  | Get current display position on an auxiliary display. |
| int | [auxdisplay\_capabilities\_get](group__auxdisplay__interface.md#ga4dd5cba56d4b90b77ae8ad02122ef81c) (const struct [device](structdevice.md) \*dev, struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities) |
|  | Fetch capabilities (and details) of auxiliary display. |
| int | [auxdisplay\_clear](group__auxdisplay__interface.md#gaa5a643603353319946c823cc959b74b3) (const struct [device](structdevice.md) \*dev) |
|  | Clear display of auxiliary display and return to home position (note that this does not reset the display configuration, e.g. |
| int | [auxdisplay\_brightness\_get](group__auxdisplay__interface.md#ga1f5be6fefc759607d2859a648a1fb3b8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness) |
|  | Get the current brightness level of an auxiliary display. |
| int | [auxdisplay\_brightness\_set](group__auxdisplay__interface.md#ga34b31b70fdc57e33fc46f1048cc25e1a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness) |
|  | Update the brightness level of an auxiliary display. |
| int | [auxdisplay\_backlight\_get](group__auxdisplay__interface.md#gaf10ebdbe821894ccbeccb35bfa985fea) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight) |
|  | Get the backlight level details of an auxiliary display. |
| int | [auxdisplay\_backlight\_set](group__auxdisplay__interface.md#ga28aef24928543329c706513cc7e5b814) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight) |
|  | Update the backlight level of an auxiliary display. |
| int | [auxdisplay\_is\_busy](group__auxdisplay__interface.md#ga2af115a23f370e0770b3c998ecf0b96b) (const struct [device](structdevice.md) \*dev) |
|  | Check if an auxiliary display driver is busy. |
| int | [auxdisplay\_custom\_character\_set](group__auxdisplay__interface.md#gaf03a1068b0aed1f27ee9e2e61066da08) (const struct [device](structdevice.md) \*dev, struct [auxdisplay\_character](structauxdisplay__character.md) \*character) |
|  | Sets a custom character in the display, the custom character struct must contain the pixel data for the custom character to add and valid custom character index, if successful then the character\_code variable in the struct will be set to the character code that can be used with the [auxdisplay\_write()](group__auxdisplay__interface.md#ga231dd862cda34ea4c0c8870675556f8d "Write data to auxiliary display screen at current position.") function to show it. |
| int | [auxdisplay\_write](group__auxdisplay__interface.md#ga231dd862cda34ea4c0c8870675556f8d) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Write data to auxiliary display screen at current position. |
| int | [auxdisplay\_custom\_command](group__auxdisplay__interface.md#ga87064057ae857f81431e6e9f139a6aaa) (const struct [device](structdevice.md) \*dev, struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*data) |
|  | Send a custom command to the display (if supported by driver). |

## Detailed Description

Public API for auxiliary (textual/non-graphical) display drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [auxdisplay.h](auxdisplay_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
