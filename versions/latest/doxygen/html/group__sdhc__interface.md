---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__sdhc__interface.html
original_path: doxygen/html/group__sdhc__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SDHC interface

[Device Driver APIs](group__io__interfaces.md)

SDHC interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [sdhc\_command](structsdhc__command.md) |
|  | SD host controller command structure. [More...](structsdhc__command.md#details) |
| struct | [sdhc\_data](structsdhc__data.md) |
|  | SD host controller data structure. [More...](structsdhc__data.md#details) |
| struct | [sdhc\_host\_caps](structsdhc__host__caps.md) |
|  | SD host controller capabilities. [More...](structsdhc__host__caps.md#details) |
| struct | [sdhc\_io](structsdhc__io.md) |
|  | SD host controller I/O control structure. [More...](structsdhc__io.md#details) |
| struct | [sdhc\_host\_props](structsdhc__host__props.md) |
|  | SD host controller properties. [More...](structsdhc__host__props.md#details) |
| struct | [sdhc\_driver\_api](structsdhc__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [SDHC\_NATIVE\_RESPONSE\_MASK](#gaff462431ff5c38c74c24772cfbccc1fd)   0xF |
| #define | [SDHC\_SPI\_RESPONSE\_TYPE\_MASK](#ga48071d79eddd5178f4b36756a19a21b2)   0xF0 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sdhc\_interrupt\_cb\_t](#ga5d207e3b3d76ed9dbfa7d68a92755cbe)) (const struct [device](structdevice.md) \*dev, int reason, const void \*user\_data) |
|  | SDHC card interrupt callback prototype. |

| Enumerations | |
| --- | --- |
| enum | [sdhc\_bus\_mode](#gaf26909ae9fffdc6ac02abd8094d16dc8) { [SDHC\_BUSMODE\_OPENDRAIN](#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a) = 1 , [SDHC\_BUSMODE\_PUSHPULL](#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959) = 2 } |
|  | SD bus mode. [More...](#gaf26909ae9fffdc6ac02abd8094d16dc8) |
| enum | [sdhc\_power](#gad63742820bb18ca18cd2f96547e12eb9) { [SDHC\_POWER\_OFF](#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07) = 1 , [SDHC\_POWER\_ON](#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604) = 2 } |
|  | SD host controller power. [More...](#gad63742820bb18ca18cd2f96547e12eb9) |
| enum | [sdhc\_bus\_width](#gad8bab66ec505c8356fac7785a8955448) { [SDHC\_BUS\_WIDTH1BIT](#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0) = 1U , [SDHC\_BUS\_WIDTH4BIT](#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6) = 4U , [SDHC\_BUS\_WIDTH8BIT](#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156) = 8U } |
|  | SD host controller bus width. [More...](#gad8bab66ec505c8356fac7785a8955448) |
| enum | [sdhc\_timing\_mode](#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) {     [SDHC\_TIMING\_LEGACY](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55) = 1U , [SDHC\_TIMING\_HS](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b) = 2U , [SDHC\_TIMING\_SDR12](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86) = 3U , [SDHC\_TIMING\_SDR25](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016) = 4U ,     [SDHC\_TIMING\_SDR50](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94) = 5U , [SDHC\_TIMING\_SDR104](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1) = 6U , [SDHC\_TIMING\_DDR50](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa) = 7U , [SDHC\_TIMING\_DDR52](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692) = 8U ,     [SDHC\_TIMING\_HS200](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145) = 9U , [SDHC\_TIMING\_HS400](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc) = 10U   } |
|  | SD host controller timing mode. [More...](#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) |
| enum | [sd\_voltage](#ga34041edf280f125b8500809226b3de5d) { [SD\_VOL\_3\_3\_V](#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d) = 1U , [SD\_VOL\_3\_0\_V](#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11) = 2U , [SD\_VOL\_1\_8\_V](#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d) = 3U , [SD\_VOL\_1\_2\_V](#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af) = 4U } |
|  | SD voltage. [More...](#ga34041edf280f125b8500809226b3de5d) |
| enum | [sdhc\_interrupt\_source](#gab449b2f6b41e791d327f7d92b2b58c2d) { [SDHC\_INT\_SDIO](#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59) = BIT(0) , [SDHC\_INT\_INSERTED](#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87) = BIT(1) , [SDHC\_INT\_REMOVED](#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c) = BIT(2) } |
|  | SD host controller interrupt sources. [More...](#gab449b2f6b41e791d327f7d92b2b58c2d) |

| Functions | |
| --- | --- |
| int | [sdhc\_hw\_reset](#gad6b082a75f1272620b79a7d3a08862f7) (const struct [device](structdevice.md) \*dev) |
|  | reset SDHC controller state |
| int | [sdhc\_request](#gac708d55e92a7705f92b90ee6baa65f74) (const struct [device](structdevice.md) \*dev, struct [sdhc\_command](structsdhc__command.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), struct [sdhc\_data](structsdhc__data.md) \*data) |
|  | Send command to SDHC. |
| int | [sdhc\_set\_io](#ga0e6d8259cca442bd1356d00f668d35c4) (const struct [device](structdevice.md) \*dev, struct [sdhc\_io](structsdhc__io.md) \*io) |
|  | set I/O properties of SDHC |
| int | [sdhc\_card\_present](#ga85184688da845759dbfb706aac5eac7d) (const struct [device](structdevice.md) \*dev) |
|  | check for SDHC card presence |
| int | [sdhc\_execute\_tuning](#gab5c2711c99573e031938faaa41862971) (const struct [device](structdevice.md) \*dev) |
|  | run SDHC tuning |
| int | [sdhc\_card\_busy](#ga91acdc4a6bc2aecc988fdde6ee61ed46) (const struct [device](structdevice.md) \*dev) |
|  | check if SD card is busy |
| int | [sdhc\_get\_host\_props](#gab55cf88ae79e5aa9e2110b298048df8e) (const struct [device](structdevice.md) \*dev, struct [sdhc\_host\_props](structsdhc__host__props.md) \*props) |
|  | Get SD host controller properties. |
| int | [sdhc\_enable\_interrupt](#ga8e4beb1135aa5c0d32f999ca953224d2) (const struct [device](structdevice.md) \*dev, [sdhc\_interrupt\_cb\_t](#ga5d207e3b3d76ed9dbfa7d68a92755cbe) callback, int sources, void \*user\_data) |
|  | Enable SDHC interrupt sources. |
| int | [sdhc\_disable\_interrupt](#ga6264f62c6427973749c8d49fb908f569) (const struct [device](structdevice.md) \*dev, int sources) |
|  | Disable SDHC interrupt sources. |

| SD command timeouts | |
| --- | --- |
| #define | [SDHC\_TIMEOUT\_FOREVER](#gaacc4249f628bcd8967f16713a7def8ae)   (-1) |

## Detailed Description

SDHC interface.

## Macro Definition Documentation

## [◆ ](#gaff462431ff5c38c74c24772cfbccc1fd)SDHC\_NATIVE\_RESPONSE\_MASK

| #define SDHC\_NATIVE\_RESPONSE\_MASK   0xF |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

## [◆ ](#ga48071d79eddd5178f4b36756a19a21b2)SDHC\_SPI\_RESPONSE\_TYPE\_MASK

| #define SDHC\_SPI\_RESPONSE\_TYPE\_MASK   0xF0 |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

## [◆ ](#gaacc4249f628bcd8967f16713a7def8ae)SDHC\_TIMEOUT\_FOREVER

| #define SDHC\_TIMEOUT\_FOREVER   (-1) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

## Typedef Documentation

## [◆ ](#ga5d207e3b3d76ed9dbfa7d68a92755cbe)sdhc\_interrupt\_cb\_t

| typedef void(\* sdhc\_interrupt\_cb\_t) (const struct [device](structdevice.md) \*dev, int reason, const void \*user\_data) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

SDHC card interrupt callback prototype.

Function prototype for SDHC card interrupt callback.

Parameters
:   | dev | SDHC device that produced interrupt |
    | --- | --- |
    | reason | one of [sdhc\_interrupt\_source](#gab449b2f6b41e791d327f7d92b2b58c2d) values. |
    | user\_data | User data, set via [sdhc\_enable\_interrupt](#ga8e4beb1135aa5c0d32f999ca953224d2) |

## Enumeration Type Documentation

## [◆ ](#ga34041edf280f125b8500809226b3de5d)sd\_voltage

| enum [sd\_voltage](#ga34041edf280f125b8500809226b3de5d) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

SD voltage.

UHS cards can run with 1.8V signalling for improved power consumption. Legacy cards may support 3.0V signalling, and all cards start at 3.3V. Only relevant for SD controllers, not SPI ones.

| Enumerator | |
| --- | --- |
| SD\_VOL\_3\_3\_V | card operation voltage around 3.3v |
| SD\_VOL\_3\_0\_V | card operation voltage around 3.0v |
| SD\_VOL\_1\_8\_V | card operation voltage around 1.8v |
| SD\_VOL\_1\_2\_V | card operation voltage around 1.2v |

## [◆ ](#gaf26909ae9fffdc6ac02abd8094d16dc8)sdhc\_bus\_mode

| enum [sdhc\_bus\_mode](#gaf26909ae9fffdc6ac02abd8094d16dc8) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

SD bus mode.

Most controllers will use push/pull, including spi, but SDHC controllers that implement SD host specification can support open drain mode

| Enumerator | |
| --- | --- |
| SDHC\_BUSMODE\_OPENDRAIN |  |
| SDHC\_BUSMODE\_PUSHPULL |  |

## [◆ ](#gad8bab66ec505c8356fac7785a8955448)sdhc\_bus\_width

| enum [sdhc\_bus\_width](#gad8bab66ec505c8356fac7785a8955448) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

SD host controller bus width.

Only relevant in SD mode, SPI does not support bus width. UHS cards will use 4 bit data bus, all cards start in 1 bit mode

| Enumerator | |
| --- | --- |
| SDHC\_BUS\_WIDTH1BIT |  |
| SDHC\_BUS\_WIDTH4BIT |  |
| SDHC\_BUS\_WIDTH8BIT |  |

## [◆ ](#gab449b2f6b41e791d327f7d92b2b58c2d)sdhc\_interrupt\_source

| enum [sdhc\_interrupt\_source](#gab449b2f6b41e791d327f7d92b2b58c2d) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

SD host controller interrupt sources.

Interrupt sources for SD host controller.

| Enumerator | |
| --- | --- |
| SDHC\_INT\_SDIO | Card interrupt, used by SDIO cards. |
| SDHC\_INT\_INSERTED | Card was inserted into slot. |
| SDHC\_INT\_REMOVED | Card was removed from slot. |

## [◆ ](#gad63742820bb18ca18cd2f96547e12eb9)sdhc\_power

| enum [sdhc\_power](#gad63742820bb18ca18cd2f96547e12eb9) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

SD host controller power.

Many host controllers can control power to attached SD cards. This enum allows applications to request the host controller power off the SD card.

| Enumerator | |
| --- | --- |
| SDHC\_POWER\_OFF |  |
| SDHC\_POWER\_ON |  |

## [◆ ](#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)sdhc\_timing\_mode

| enum [sdhc\_timing\_mode](#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) |
| --- |

`#include <[sdhc.h](sdhc_8h.md)>`

SD host controller timing mode.

Used by SD host controller to determine the timing of the cards attached to the bus. Cards start with legacy timing, but UHS-II cards can go up to SDR104.

| Enumerator | |
| --- | --- |
| SDHC\_TIMING\_LEGACY | Legacy 3.3V Mode. |
| SDHC\_TIMING\_HS | Legacy High speed mode (3.3V). |
| SDHC\_TIMING\_SDR12 | Identification mode & SDR12. |
| SDHC\_TIMING\_SDR25 | High speed mode & SDR25. |
| SDHC\_TIMING\_SDR50 | SDR49 mode. |
| SDHC\_TIMING\_SDR104 | SDR104 mode. |
| SDHC\_TIMING\_DDR50 | DDR50 mode. |
| SDHC\_TIMING\_DDR52 | DDR52 mode. |
| SDHC\_TIMING\_HS200 | HS200 mode. |
| SDHC\_TIMING\_HS400 | HS400 mode. |

## Function Documentation

## [◆ ](#ga91acdc4a6bc2aecc988fdde6ee61ed46)sdhc\_card\_busy()

| int sdhc\_card\_busy | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdhc.h](sdhc_8h.md)>`

check if SD card is busy

This check should generally be implemented as checking the line level of the DAT[0:3] lines of the SD bus. No SD commands need to be sent, the controller simply needs to report the status of the SD bus.

Parameters
:   | dev | SDHC device |
    | --- | --- |

Return values
:   | 0 | card is not busy |
    | --- | --- |
    | 1 | card is busy |
    | -EIO | I/O error |

## [◆ ](#ga85184688da845759dbfb706aac5eac7d)sdhc\_card\_present()

| int sdhc\_card\_present | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdhc.h](sdhc_8h.md)>`

check for SDHC card presence

Checks if card is present on the SD bus. Note that if a controller requires cards be powered up to detect presence, it should do so in this function.

Parameters
:   | dev | SDHC device |
    | --- | --- |

Return values
:   | 1 | card is present |
    | --- | --- |
    | 0 | card is not present |
    | -EIO | I/O error |

## [◆ ](#ga6264f62c6427973749c8d49fb908f569)sdhc\_disable\_interrupt()

| int sdhc\_disable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *sources* ) |

`#include <[sdhc.h](sdhc_8h.md)>`

Disable SDHC interrupt sources.

Disables SDHC interrupt sources. If multiple sources are enabled, only the ones specified in "sources" will be masked.

Parameters
:   | dev | SDHC device |
    | --- | --- |
    | sources | bitmask of [sdhc\_interrupt\_source](#gab449b2f6b41e791d327f7d92b2b58c2d) values indicating which interrupts should be disabled. |

Return values
:   | 0 | interrupts were disabled |
    | --- | --- |
    | -ENOTSUP | controller does not support this function |
    | -EIO | I/O error |

## [◆ ](#ga8e4beb1135aa5c0d32f999ca953224d2)sdhc\_enable\_interrupt()

| int sdhc\_enable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [sdhc\_interrupt\_cb\_t](#ga5d207e3b3d76ed9dbfa7d68a92755cbe) | *callback*, |
|  |  | int | *sources*, |
|  |  | void \* | *user\_data* ) |

`#include <[sdhc.h](sdhc_8h.md)>`

Enable SDHC interrupt sources.

Enables SDHC interrupt sources. Each subsequent call of this function should replace the previous callback set, and leave only the interrupts specified in the "sources" argument enabled.

Parameters
:   | dev | SDHC device |
    | --- | --- |
    | callback | Callback called when interrupt occurs |
    | sources | bitmask of [sdhc\_interrupt\_source](#gab449b2f6b41e791d327f7d92b2b58c2d) values indicating which interrupts should produce a callback |
    | user\_data | parameter that will be passed to callback function |

Return values
:   | 0 | interrupts were enabled, and callback was installed |
    | --- | --- |
    | -ENOTSUP | controller does not support this function |
    | -EIO | I/O error |

## [◆ ](#gab5c2711c99573e031938faaa41862971)sdhc\_execute\_tuning()

| int sdhc\_execute\_tuning | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdhc.h](sdhc_8h.md)>`

run SDHC tuning

SD cards require signal tuning for UHS modes SDR104 and SDR50. This function allows an application to request the SD host controller to tune the card.

Parameters
:   | dev | SDHC device |
    | --- | --- |

Return values
:   | 0 | tuning succeeded, card is ready for commands |
    | --- | --- |
    | -ETIMEDOUT | tuning failed after timeout |
    | -ENOTSUP | controller does not support tuning |
    | -EIO | I/O error while tuning |

## [◆ ](#gab55cf88ae79e5aa9e2110b298048df8e)sdhc\_get\_host\_props()

| int sdhc\_get\_host\_props | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [sdhc\_host\_props](structsdhc__host__props.md) \* | *props* ) |

`#include <[sdhc.h](sdhc_8h.md)>`

Get SD host controller properties.

Gets host properties from the host controller. Host controller should initialize all values in the [sdhc\_host\_props](structsdhc__host__props.md "sdhc_host_props") structure provided.

Parameters
:   | dev | SDHC device |
    | --- | --- |
    | props | property structure to be filled by sdhc driver |

Return values
:   | 0 | function succeeded. |
    | --- | --- |
    | -ENOTSUP | host controller does not support this call |

## [◆ ](#gad6b082a75f1272620b79a7d3a08862f7)sdhc\_hw\_reset()

| int sdhc\_hw\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdhc.h](sdhc_8h.md)>`

reset SDHC controller state

Used when the SDHC has encountered an error. Resetting the SDHC controller should clear all errors on the SDHC, but does not necessarily reset I/O settings to boot (this can be done with [sdhc\_set\_io](#ga0e6d8259cca442bd1356d00f668d35c4))

Parameters
:   | dev | SD host controller device |
    | --- | --- |

Return values
:   | 0 | reset succeeded |
    | --- | --- |
    | -ETIMEDOUT | controller reset timed out |
    | -EIO | reset failed |

## [◆ ](#gac708d55e92a7705f92b90ee6baa65f74)sdhc\_request()

| int sdhc\_request | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [sdhc\_command](structsdhc__command.md) \* | *cmd*, |
|  |  | struct [sdhc\_data](structsdhc__data.md) \* | *data* ) |

`#include <[sdhc.h](sdhc_8h.md)>`

Send command to SDHC.

Sends a command to the SD host controller, which will send this command to attached SD cards.

Parameters
:   | dev | SDHC device |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | SDHC command |
    | data | SDHC data. Leave NULL to send SD command without data. |

Return values
:   | 0 | command was sent successfully |
    | --- | --- |
    | -ETIMEDOUT | command timed out while sending |
    | -ENOTSUP | host controller does not support command |
    | -EIO | I/O error |

## [◆ ](#ga0e6d8259cca442bd1356d00f668d35c4)sdhc\_set\_io()

| int sdhc\_set\_io | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [sdhc\_io](structsdhc__io.md) \* | *io* ) |

`#include <[sdhc.h](sdhc_8h.md)>`

set I/O properties of SDHC

I/O properties should be reconfigured when the card has been sent a command to change its own SD settings. This function can also be used to toggle power to the SD card.

Parameters
:   | dev | SDHC device |
    | --- | --- |
    | io | I/O properties |

Returns
:   0 I/O was configured correctly
:   -ENOTSUP controller does not support these I/O settings
:   -EIO controller could not configure I/O settings

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
