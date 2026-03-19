---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mb__display.html
original_path: doxygen/html/group__mb__display.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BBC micro:bit display APIs

[Third-party](group__third__party.md)

BBC micro:bit display APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mb\_image](structmb__image.md) |
|  | Representation of a BBC micro:bit display image. [More...](structmb__image.md#details) |

| Macros | |
| --- | --- |
| #define | [MB\_IMAGE](#ga529a5650acaf699b23b4b4234127cf2c)(\_rows...) |
|  | Generate an image object from a given array rows/columns. |

| Enumerations | |
| --- | --- |
| enum | [mb\_display\_mode](#ga750a177cffbb90ab38392d9ebad9a8eb) { [MB\_DISPLAY\_MODE\_DEFAULT](#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5) , [MB\_DISPLAY\_MODE\_SINGLE](#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a) , [MB\_DISPLAY\_MODE\_SCROLL](#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69) , [MB\_DISPLAY\_FLAG\_LOOP](#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc) = BIT(16) } |
|  | Display mode. [More...](#ga750a177cffbb90ab38392d9ebad9a8eb) |

| Functions | |
| --- | --- |
| struct mb\_display \* | [mb\_display\_get](#ga94e3eadd1cf386b8d9494ccfa8afaa40) (void) |
|  | Get a pointer to the BBC micro:bit display object. |
| void | [mb\_display\_image](#ga2a6e20d57d0d65033281dd7c3ea19126) (struct mb\_display \*disp, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration, const struct [mb\_image](structmb__image.md) \*img, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_count) |
|  | Display one or more images on the BBC micro:bit LED display. |
| void | [mb\_display\_print](#ga993a6a0225206f53170d25d9177c1225) (struct mb\_display \*disp, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration, const char \*fmt,...) |
|  | Print a string of characters on the BBC micro:bit LED display. |
| void | [mb\_display\_stop](#gad15b3635993007d8aad9364cbe29311b) (struct mb\_display \*disp) |
|  | Stop the ongoing display of an image. |

## Detailed Description

BBC micro:bit display APIs.

## Macro Definition Documentation

## [◆ ](#ga529a5650acaf699b23b4b4234127cf2c)MB\_IMAGE

| #define MB\_IMAGE | ( |  | *\_rows...* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mb_display.h](mb__display_8h.md)>`

**Value:**

{ .r = { \_rows } }

Generate an image object from a given array rows/columns.

This helper takes an array of 5 rows, each consisting of 5 0/1 values which correspond to the columns of that row. The value 0 means the pixel is disabled whereas a 1 means the pixel is enabled.

The pixels go from left to right and top to bottom, i.e. top-left corner is the first row's first value, top-right is the first rows last value, and bottom-right corner is the last value of the last (5th) row. As an example, the following would create a smiley face image:

```
static const struct [mb_image](structmb__image.md "Representation of a BBC micro:bit display image.") smiley = MB_IMAGE({ 0, 1, 0, 1, 0 },
                                          { 0, 1, 0, 1, 0 },
                                          { 0, 0, 0, 0, 0 },
                                          { 1, 0, 0, 0, 1 },
                                          { 0, 1, 1, 1, 0 });
```

Parameters
:   | \_rows | Each of the 5 rows represented as a 5-value column array. |
    | --- | --- |

Returns
:   Image bitmap that can be passed e.g. to [mb\_display\_image()](#ga2a6e20d57d0d65033281dd7c3ea19126).

## Enumeration Type Documentation

## [◆ ](#ga750a177cffbb90ab38392d9ebad9a8eb)mb\_display\_mode

| enum [mb\_display\_mode](#ga750a177cffbb90ab38392d9ebad9a8eb) |
| --- |

`#include <[mb_display.h](mb__display_8h.md)>`

Display mode.

First 16 bits are reserved for modes, last 16 for flags.

| Enumerator | |
| --- | --- |
| MB\_DISPLAY\_MODE\_DEFAULT | Default mode ("single" for images, "scroll" for text). |
| MB\_DISPLAY\_MODE\_SINGLE | Display images sequentially, one at a time. |
| MB\_DISPLAY\_MODE\_SCROLL | Display images by scrolling. |
| MB\_DISPLAY\_FLAG\_LOOP | Loop back to the beginning when reaching the last image. |

## Function Documentation

## [◆ ](#ga94e3eadd1cf386b8d9494ccfa8afaa40)mb\_display\_get()

| struct mb\_display \* mb\_display\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mb_display.h](mb__display_8h.md)>`

Get a pointer to the BBC micro:bit display object.

Returns
:   Pointer to display object.

## [◆ ](#ga2a6e20d57d0d65033281dd7c3ea19126)mb\_display\_image()

| void mb\_display\_image | ( | struct mb\_display \* | *disp*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mode*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *duration*, |
|  |  | const struct [mb\_image](structmb__image.md) \* | *img*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *img\_count* ) |

`#include <[mb_display.h](mb__display_8h.md)>`

Display one or more images on the BBC micro:bit LED display.

This function takes an array of one or more images and renders them sequentially on the micro:bit display. The call is asynchronous, i.e. the processing of the display happens in the background. If there is another image being displayed it will be canceled and the new one takes over.

Parameters
:   | disp | Display object. |
    | --- | --- |
    | mode | One of the MB\_DISPLAY\_MODE\_\* options. |
    | duration | Duration how long to show each image (in milliseconds), or [SYS\_FOREVER\_MS](group__timeutil__unit__apis.md#ga9f9c4c41f62c7578a30209475201efed "SYS_FOREVER_MS"). |
    | img | Array of image bitmaps (struct [mb\_image](structmb__image.md "Representation of a BBC micro:bit display image.") objects). |
    | img\_count | Number of images in 'img' array. |

## [◆ ](#ga993a6a0225206f53170d25d9177c1225)mb\_display\_print()

| void mb\_display\_print | ( | struct mb\_display \* | *disp*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mode*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *duration*, |
|  |  | const char \* | *fmt*, |
|  |  |  | *...* ) |

`#include <[mb_display.h](mb__display_8h.md)>`

Print a string of characters on the BBC micro:bit LED display.

This function takes a printf-style format string and outputs it in a scrolling fashion to the display.

The call is asynchronous, i.e. the processing of the display happens in the background. If there is another image or string being displayed it will be canceled and the new one takes over.

Parameters
:   | disp | Display object. |
    | --- | --- |
    | mode | One of the MB\_DISPLAY\_MODE\_\* options. |
    | duration | Duration how long to show each character (in milliseconds), or [SYS\_FOREVER\_MS](group__timeutil__unit__apis.md#ga9f9c4c41f62c7578a30209475201efed "SYS_FOREVER_MS"). |
    | fmt | printf-style format string |
    | ... | Optional list of format arguments. |

## [◆ ](#gad15b3635993007d8aad9364cbe29311b)mb\_display\_stop()

| void mb\_display\_stop | ( | struct mb\_display \* | *disp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mb_display.h](mb__display_8h.md)>`

Stop the ongoing display of an image.

Parameters
:   | disp | Display object. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
