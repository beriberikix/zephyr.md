---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__auxdisplay__interface.html
original_path: doxygen/html/group__auxdisplay__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Text Display Interface

[Device Driver APIs](group__io__interfaces.md)

Auxiliary (Text) Display Interface.
[More...](#details)

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
| #define | [AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED](#ga0bd1d97b360f3138887a5e3e4729e01b)   0 |
|  | Used for minimum and maximum brightness/backlight values if not supported. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [auxdisplay\_mode\_t](#ga78861a5414ac95e9ca77436c0b82acc2) |
|  | Used to describe the mode of an auxiliary (text) display. |

| Enumerations | |
| --- | --- |
| enum | [auxdisplay\_position](#ga98b0be37fc76df0ae4dec0bef6c94504) { [AUXDISPLAY\_POSITION\_ABSOLUTE](#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) = 0 , [AUXDISPLAY\_POSITION\_RELATIVE](#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28) , [AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION](#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558) , [AUXDISPLAY\_POSITION\_COUNT](#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23) } |
|  | Used for moving the cursor or display position. [More...](#ga98b0be37fc76df0ae4dec0bef6c94504) |
| enum | [auxdisplay\_direction](#ga5f95ac69e18091883e7121103014be10) { [AUXDISPLAY\_DIRECTION\_RIGHT](#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599) = 0 , [AUXDISPLAY\_DIRECTION\_LEFT](#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352) , [AUXDISPLAY\_DIRECTION\_COUNT](#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3) } |
|  | Used for setting character append position. [More...](#ga5f95ac69e18091883e7121103014be10) |

| Functions | |
| --- | --- |
| int | [auxdisplay\_display\_on](#gaffb3c1c41d810355fe2da3558ebba0c2) (const struct [device](structdevice.md) \*dev) |
|  | Turn display on. |
| int | [auxdisplay\_display\_off](#ga625f399720417715090793c7f6d63f7e) (const struct [device](structdevice.md) \*dev) |
|  | Turn display off. |
| int | [auxdisplay\_cursor\_set\_enabled](#ga7191475b362f728cc92eb07cb1f2ed00) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Set cursor enabled status on an auxiliary display. |
| int | [auxdisplay\_position\_blinking\_set\_enabled](#ga7102ec9941f8b3131a18e4ff7b640241) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Set cursor blinking status on an auxiliary display. |
| int | [auxdisplay\_cursor\_shift\_set](#gafb18729b4897cea83dbfc1c7241f5b2d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) display\_shift) |
|  | Set cursor shift after character write and display shift. |
| int | [auxdisplay\_cursor\_position\_set](#ga9c6302789d9cc9e481dd7c54ef370988) (const struct [device](structdevice.md) \*dev, enum [auxdisplay\_position](#ga98b0be37fc76df0ae4dec0bef6c94504) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y) |
|  | Set cursor (and write position) on an auxiliary display. |
| int | [auxdisplay\_cursor\_position\_get](#ga37bd5403c876ff294be5ea72292de4b4) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y) |
|  | Get current cursor on an auxiliary display. |
| int | [auxdisplay\_display\_position\_set](#ga02e8e930203cfb1410752a0ffee9a34e) (const struct [device](structdevice.md) \*dev, enum [auxdisplay\_position](#ga98b0be37fc76df0ae4dec0bef6c94504) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y) |
|  | Set display position on an auxiliary display. |
| int | [auxdisplay\_display\_position\_get](#ga1f9e363765d715edb899901a14c54674) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y) |
|  | Get current display position on an auxiliary display. |
| int | [auxdisplay\_capabilities\_get](#ga4dd5cba56d4b90b77ae8ad02122ef81c) (const struct [device](structdevice.md) \*dev, struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities) |
|  | Fetch capabilities (and details) of auxiliary display. |
| int | [auxdisplay\_clear](#gaa5a643603353319946c823cc959b74b3) (const struct [device](structdevice.md) \*dev) |
|  | Clear display of auxiliary display and return to home position (note that this does not reset the display configuration, e.g. |
| int | [auxdisplay\_brightness\_get](#ga1f5be6fefc759607d2859a648a1fb3b8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness) |
|  | Get the current brightness level of an auxiliary display. |
| int | [auxdisplay\_brightness\_set](#ga34b31b70fdc57e33fc46f1048cc25e1a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness) |
|  | Update the brightness level of an auxiliary display. |
| int | [auxdisplay\_backlight\_get](#gaf10ebdbe821894ccbeccb35bfa985fea) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight) |
|  | Get the backlight level details of an auxiliary display. |
| int | [auxdisplay\_backlight\_set](#ga28aef24928543329c706513cc7e5b814) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight) |
|  | Update the backlight level of an auxiliary display. |
| int | [auxdisplay\_is\_busy](#ga2af115a23f370e0770b3c998ecf0b96b) (const struct [device](structdevice.md) \*dev) |
|  | Check if an auxiliary display driver is busy. |
| int | [auxdisplay\_custom\_character\_set](#gaf03a1068b0aed1f27ee9e2e61066da08) (const struct [device](structdevice.md) \*dev, struct [auxdisplay\_character](structauxdisplay__character.md) \*character) |
|  | Sets a custom character in the display, the custom character struct must contain the pixel data for the custom character to add and valid custom character index, if successful then the character\_code variable in the struct will be set to the character code that can be used with the [auxdisplay\_write()](#ga231dd862cda34ea4c0c8870675556f8d) function to show it. |
| int | [auxdisplay\_write](#ga231dd862cda34ea4c0c8870675556f8d) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Write data to auxiliary display screen at current position. |
| int | [auxdisplay\_custom\_command](#ga87064057ae857f81431e6e9f139a6aaa) (const struct [device](structdevice.md) \*dev, struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*data) |
|  | Send a custom command to the display (if supported by driver). |

## Detailed Description

Auxiliary (Text) Display Interface.

Since
:   3.4

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga0bd1d97b360f3138887a5e3e4729e01b)AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED

| #define AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED   0 |
| --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Used for minimum and maximum brightness/backlight values if not supported.

## Typedef Documentation

## [◆ ](#ga78861a5414ac95e9ca77436c0b82acc2)auxdisplay\_mode\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [auxdisplay\_mode\_t](#ga78861a5414ac95e9ca77436c0b82acc2) |
| --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Used to describe the mode of an auxiliary (text) display.

## Enumeration Type Documentation

## [◆ ](#ga5f95ac69e18091883e7121103014be10)auxdisplay\_direction

| enum [auxdisplay\_direction](#ga5f95ac69e18091883e7121103014be10) |
| --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Used for setting character append position.

| Enumerator | |
| --- | --- |
| AUXDISPLAY\_DIRECTION\_RIGHT | Each character will be placed to the right of existing characters. |
| AUXDISPLAY\_DIRECTION\_LEFT | Each character will be placed to the left of existing characters. |
| AUXDISPLAY\_DIRECTION\_COUNT |  |

## [◆ ](#ga98b0be37fc76df0ae4dec0bef6c94504)auxdisplay\_position

| enum [auxdisplay\_position](#ga98b0be37fc76df0ae4dec0bef6c94504) |
| --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Used for moving the cursor or display position.

| Enumerator | |
| --- | --- |
| AUXDISPLAY\_POSITION\_ABSOLUTE | Moves to specified X,Y position. |
| AUXDISPLAY\_POSITION\_RELATIVE | Shifts current position by +/- X,Y position, does not take display direction into consideration. |
| AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION | Shifts current position by +/- X,Y position, takes display direction into consideration. |
| AUXDISPLAY\_POSITION\_COUNT |  |

## Function Documentation

## [◆ ](#gaf10ebdbe821894ccbeccb35bfa985fea)auxdisplay\_backlight\_get()

| int auxdisplay\_backlight\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *backlight* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Get the backlight level details of an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | backlight | Will be updated with the current backlight level |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga28aef24928543329c706513cc7e5b814)auxdisplay\_backlight\_set()

| int auxdisplay\_backlight\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *backlight* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Update the backlight level of an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | backlight | The backlight level to set |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga1f5be6fefc759607d2859a648a1fb3b8)auxdisplay\_brightness\_get()

| int auxdisplay\_brightness\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *brightness* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Get the current brightness level of an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | brightness | Will be updated with the current brightness |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga34b31b70fdc57e33fc46f1048cc25e1a)auxdisplay\_brightness\_set()

| int auxdisplay\_brightness\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *brightness* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Update the brightness level of an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | brightness | The brightness level to set |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga4dd5cba56d4b90b77ae8ad02122ef81c)auxdisplay\_capabilities\_get()

| int auxdisplay\_capabilities\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \* | *capabilities* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Fetch capabilities (and details) of auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | capabilities | Will be updated with the details of the auxiliary display |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | Negative errno code on other failure. |

## [◆ ](#gaa5a643603353319946c823cc959b74b3)auxdisplay\_clear()

| int auxdisplay\_clear | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Clear display of auxiliary display and return to home position (note that this does not reset the display configuration, e.g.

custom characters and display mode will persist).

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga37bd5403c876ff294be5ea72292de4b4)auxdisplay\_cursor\_position\_get()

| int auxdisplay\_cursor\_position\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \* | *x*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \* | *y* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Get current cursor on an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | x | Will be updated with the exact X position |
    | y | Will be updated with the exact Y position |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga9c6302789d9cc9e481dd7c54ef370988)auxdisplay\_cursor\_position\_set()

| int auxdisplay\_cursor\_position\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [auxdisplay\_position](#ga98b0be37fc76df0ae4dec0bef6c94504) | *type*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *x*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *y* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Set cursor (and write position) on an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | type | Type of move, absolute or offset |
    | x | Exact or offset X position |
    | y | Exact or offset Y position |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga7191475b362f728cc92eb07cb1f2ed00)auxdisplay\_cursor\_set\_enabled()

| int auxdisplay\_cursor\_set\_enabled | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enabled* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Set cursor enabled status on an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | enabled | True to enable cursor, false to disable |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#gafb18729b4897cea83dbfc1c7241f5b2d)auxdisplay\_cursor\_shift\_set()

| int auxdisplay\_cursor\_shift\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *direction*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *display\_shift* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Set cursor shift after character write and display shift.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | direction | Sets the direction of the display when characters are written |
    | display\_shift | If true, will shift the display when characters are written (which makes it look like the display is moving, not the cursor) |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#gaf03a1068b0aed1f27ee9e2e61066da08)auxdisplay\_custom\_character\_set()

| int auxdisplay\_custom\_character\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [auxdisplay\_character](structauxdisplay__character.md) \* | *character* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Sets a custom character in the display, the custom character struct must contain the pixel data for the custom character to add and valid custom character index, if successful then the character\_code variable in the struct will be set to the character code that can be used with the [auxdisplay\_write()](#ga231dd862cda34ea4c0c8870675556f8d) function to show it.

A character must be valid for a display consisting of a uint8 array of size character width by character height, values should be 0x00 for pixel off or 0xff for pixel on, if a display supports shades then values between 0x00 and 0xff may be used (display driver dependent).

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | character | Pointer to custom character structure |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga87064057ae857f81431e6e9f139a6aaa)auxdisplay\_custom\_command()

| int auxdisplay\_custom\_command | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \* | *data* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Send a custom command to the display (if supported by driver).

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | data | Custom command structure (this may be extended by specific drivers) |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga625f399720417715090793c7f6d63f7e)auxdisplay\_display\_off()

| int auxdisplay\_display\_off | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Turn display off.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#gaffb3c1c41d810355fe2da3558ebba0c2)auxdisplay\_display\_on()

| int auxdisplay\_display\_on | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Turn display on.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga1f9e363765d715edb899901a14c54674)auxdisplay\_display\_position\_get()

| int auxdisplay\_display\_position\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \* | *x*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \* | *y* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Get current display position on an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | x | Will be updated with the exact X position |
    | y | Will be updated with the exact Y position |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga02e8e930203cfb1410752a0ffee9a34e)auxdisplay\_display\_position\_set()

| int auxdisplay\_display\_position\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [auxdisplay\_position](#ga98b0be37fc76df0ae4dec0bef6c94504) | *type*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *x*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *y* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Set display position on an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | type | Type of move, absolute or offset |
    | x | Exact or offset X position |
    | y | Exact or offset Y position |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga2af115a23f370e0770b3c998ecf0b96b)auxdisplay\_is\_busy()

| int auxdisplay\_is\_busy | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Check if an auxiliary display driver is busy.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |

Return values
:   | 1 | on success and display busy. |
    | --- | --- |
    | 0 | on success and display not busy. |
    | -ENOSYS | if not supported/implemented. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga7102ec9941f8b3131a18e4ff7b640241)auxdisplay\_position\_blinking\_set\_enabled()

| int auxdisplay\_position\_blinking\_set\_enabled | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enabled* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Set cursor blinking status on an auxiliary display.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | enabled | Set to true to enable blinking position, false to disable |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOSYS | if not supported/implemented. |
    | -errno | Negative errno code on other failure. |

## [◆ ](#ga231dd862cda34ea4c0c8870675556f8d)auxdisplay\_write()

| int auxdisplay\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[auxdisplay.h](auxdisplay_8h.md)>`

Write data to auxiliary display screen at current position.

Parameters
:   | dev | Auxiliary display device instance |
    | --- | --- |
    | data | Text data to write |
    | len | Length of text data to write |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | if provided argument is invalid. |
    | -errno | Negative errno code on other failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
