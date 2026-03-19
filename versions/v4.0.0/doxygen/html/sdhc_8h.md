---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sdhc_8h.html
original_path: doxygen/html/sdhc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc.h File Reference

SD Host Controller public API header file.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sd/sd_spec.h](sd__spec_8h_source.md)>`  
`#include <zephyr/syscalls/sdhc.h>`

[Go to the source code of this file.](sdhc_8h_source.md)

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
| #define | [SDHC\_NATIVE\_RESPONSE\_MASK](group__sdhc__interface.md#gaff462431ff5c38c74c24772cfbccc1fd)   0xF |
| #define | [SDHC\_SPI\_RESPONSE\_TYPE\_MASK](group__sdhc__interface.md#ga48071d79eddd5178f4b36756a19a21b2)   0xF0 |
| SD command timeouts | |
| #define | [SDHC\_TIMEOUT\_FOREVER](group__sdhc__interface.md#gaacc4249f628bcd8967f16713a7def8ae)   (-1) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe)) (const struct [device](structdevice.md) \*dev, int reason, const void \*user\_data) |
|  | SDHC card interrupt callback prototype. |

| Enumerations | |
| --- | --- |
| enum | [sdhc\_bus\_mode](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8) { [SDHC\_BUSMODE\_OPENDRAIN](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a) = 1 , [SDHC\_BUSMODE\_PUSHPULL](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959) = 2 } |
|  | SD bus mode. [More...](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8) |
| enum | [sdhc\_power](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9) { [SDHC\_POWER\_OFF](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07) = 1 , [SDHC\_POWER\_ON](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604) = 2 } |
|  | SD host controller power. [More...](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9) |
| enum | [sdhc\_bus\_width](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448) { [SDHC\_BUS\_WIDTH1BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0) = 1U , [SDHC\_BUS\_WIDTH4BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6) = 4U , [SDHC\_BUS\_WIDTH8BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156) = 8U } |
|  | SD host controller bus width. [More...](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448) |
| enum | [sdhc\_timing\_mode](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) {     [SDHC\_TIMING\_LEGACY](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55) = 1U , [SDHC\_TIMING\_HS](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b) = 2U , [SDHC\_TIMING\_SDR12](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86) = 3U , [SDHC\_TIMING\_SDR25](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016) = 4U ,     [SDHC\_TIMING\_SDR50](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94) = 5U , [SDHC\_TIMING\_SDR104](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1) = 6U , [SDHC\_TIMING\_DDR50](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa) = 7U , [SDHC\_TIMING\_DDR52](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692) = 8U ,     [SDHC\_TIMING\_HS200](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145) = 9U , [SDHC\_TIMING\_HS400](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc) = 10U   } |
|  | SD host controller timing mode. [More...](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) |
| enum | [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) { [SD\_VOL\_3\_3\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d) = 1U , [SD\_VOL\_3\_0\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11) = 2U , [SD\_VOL\_1\_8\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d) = 3U , [SD\_VOL\_1\_2\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af) = 4U } |
|  | SD voltage. [More...](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) |
| enum | [sdhc\_interrupt\_source](group__sdhc__interface.md#gab449b2f6b41e791d327f7d92b2b58c2d) { [SDHC\_INT\_SDIO](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59) = BIT(0) , [SDHC\_INT\_INSERTED](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87) = BIT(1) , [SDHC\_INT\_REMOVED](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c) = BIT(2) } |
|  | SD host controller interrupt sources. [More...](group__sdhc__interface.md#gab449b2f6b41e791d327f7d92b2b58c2d) |

| Functions | |
| --- | --- |
| int | [sdhc\_hw\_reset](group__sdhc__interface.md#gad6b082a75f1272620b79a7d3a08862f7) (const struct [device](structdevice.md) \*dev) |
|  | reset SDHC controller state |
| int | [sdhc\_request](group__sdhc__interface.md#gac708d55e92a7705f92b90ee6baa65f74) (const struct [device](structdevice.md) \*dev, struct [sdhc\_command](structsdhc__command.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), struct [sdhc\_data](structsdhc__data.md) \*data) |
|  | Send command to SDHC. |
| int | [sdhc\_set\_io](group__sdhc__interface.md#ga0e6d8259cca442bd1356d00f668d35c4) (const struct [device](structdevice.md) \*dev, struct [sdhc\_io](structsdhc__io.md) \*io) |
|  | set I/O properties of SDHC |
| int | [sdhc\_card\_present](group__sdhc__interface.md#ga85184688da845759dbfb706aac5eac7d) (const struct [device](structdevice.md) \*dev) |
|  | check for SDHC card presence |
| int | [sdhc\_execute\_tuning](group__sdhc__interface.md#gab5c2711c99573e031938faaa41862971) (const struct [device](structdevice.md) \*dev) |
|  | run SDHC tuning |
| int | [sdhc\_card\_busy](group__sdhc__interface.md#ga91acdc4a6bc2aecc988fdde6ee61ed46) (const struct [device](structdevice.md) \*dev) |
|  | check if SD card is busy |
| int | [sdhc\_get\_host\_props](group__sdhc__interface.md#gab55cf88ae79e5aa9e2110b298048df8e) (const struct [device](structdevice.md) \*dev, struct [sdhc\_host\_props](structsdhc__host__props.md) \*props) |
|  | Get SD host controller properties. |
| int | [sdhc\_enable\_interrupt](group__sdhc__interface.md#ga8e4beb1135aa5c0d32f999ca953224d2) (const struct [device](structdevice.md) \*dev, [sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe) callback, int sources, void \*user\_data) |
|  | Enable SDHC interrupt sources. |
| int | [sdhc\_disable\_interrupt](group__sdhc__interface.md#ga6264f62c6427973749c8d49fb908f569) (const struct [device](structdevice.md) \*dev, int sources) |
|  | Disable SDHC interrupt sources. |

## Detailed Description

SD Host Controller public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sdhc.h](sdhc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
