---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2spi_8h.html
original_path: doxygen/html/drivers_2spi_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi.h File Reference

Public API for SPI drivers and applications.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/dt-bindings/spi/spi.h](dt-bindings_2spi_2spi_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h_source.md)>`  
`#include <[zephyr/stats/stats.h](stats_2stats_8h_source.md)>`  
`#include <zephyr/syscalls/spi.h>`

[Go to the source code of this file.](drivers_2spi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [spi\_cs\_control](structspi__cs__control.md) |
|  | SPI Chip Select control structure. [More...](structspi__cs__control.md#details) |
| struct | [spi\_config](structspi__config.md) |
|  | SPI controller configuration structure. [More...](structspi__config.md#details) |
| struct | [spi\_dt\_spec](structspi__dt__spec.md) |
|  | Complete SPI DT information. [More...](structspi__dt__spec.md#details) |
| struct | [spi\_buf](structspi__buf.md) |
|  | SPI buffer structure. [More...](structspi__buf.md#details) |
| struct | [spi\_buf\_set](structspi__buf__set.md) |
|  | SPI buffer array structure. [More...](structspi__buf__set.md#details) |
| struct | [spi\_driver\_api](structspi__driver__api.md) |
|  | SPI driver API This is the mandatory API any SPI driver needs to expose. [More...](structspi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [SPI\_CS\_GPIOS\_DT\_SPEC\_GET](group__spi__interface.md#ga48aa19f45413d56b03596d10b72c732e)(spi\_dev) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin. |
| #define | [SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET](group__spi__interface.md#ga88fefbfadb8184806123e1f935a4ff7c)(inst) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin. |
| #define | [SPI\_CS\_CONTROL\_INIT](group__spi__interface.md#ga4a2bce02956d8121da7b6099f6c097b9)(node\_id, delay\_) |
|  | Initialize and get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node identifier. |
| #define | [SPI\_CS\_CONTROL\_INIT\_INST](group__spi__interface.md#ga239bda66980ed0a349b7177100f7752c)(inst, delay\_) |
|  | Get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node. |
| #define | [SPI\_CONFIG\_DT](group__spi__interface.md#ga822af066ee0829aee405c034bb967463)(node\_id, operation\_, delay\_) |
|  | Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree. |
| #define | [SPI\_CONFIG\_DT\_INST](group__spi__interface.md#gadc1e7de7925603adfedbac35fdabc78a)(inst, operation\_, delay\_) |
|  | Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree instance. |
| #define | [SPI\_DT\_SPEC\_GET](group__spi__interface.md#gaec6a8fde1c3ec6349a601a2d5f7af785)(node\_id, operation\_, delay\_) |
|  | Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree. |
| #define | [SPI\_DT\_SPEC\_INST\_GET](group__spi__interface.md#ga91c595b7567af23b447c755d898608f3)(inst, operation\_, delay\_) |
|  | Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree instance. |
| #define | [SPI\_DEVICE\_DT\_DEFINE](group__spi__interface.md#ga27af5f053c5fd4e9eef0900406fbf854)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
| #define | [SPI\_STATS\_RX\_BYTES\_INC](group__spi__interface.md#ga83fa04d1e9f281cd566ee32cf807325e)(dev\_) |
| #define | [SPI\_STATS\_TX\_BYTES\_INC](group__spi__interface.md#gadd3b82af2396b91930ece09fa79fc4e2)(dev\_) |
| #define | [SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)(dev\_) |
| #define | [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(dev, error, tx\_bufs, rx\_bufs) |
| #define | [SPI\_DT\_IODEV\_DEFINE](group__spi__interface.md#ga1e9f5fe389d53c280639f23ea134e18c)(name, node\_id, operation\_, delay\_) |
|  | Define an iodev for a given dt node on the bus. |
| SPI operational mode | |
| #define | [SPI\_OP\_MODE\_MASTER](group__spi__interface.md#ga5b9d40fa0f455b1e63f8040b3316b0da)   0U |
|  | Master mode. |
| #define | [SPI\_OP\_MODE\_SLAVE](group__spi__interface.md#ga1c3310d3711cb99cdb78fa9d1c970779)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Slave mode. |
| #define | [SPI\_OP\_MODE\_GET](group__spi__interface.md#ga6dd4395e027407a7b3b92cff2abcc8b3)(\_operation\_) |
|  | Get SPI operational mode. |
| SPI Polarity & Phase Modes | |
| #define | [SPI\_MODE\_CPOL](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Clock Polarity: if set, clock idle state will be 1 and active state will be 0. |
| #define | [SPI\_MODE\_CPHA](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Clock Phase: this dictates when is the data captured, and depends clock's polarity. |
| #define | [SPI\_MODE\_LOOP](group__spi__interface.md#ga8619b297de563eca6852af34c79daa62)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Whatever data is transmitted is looped-back to the receiving buffer of the controller. |
| #define | [SPI\_MODE\_GET](group__spi__interface.md#gaa3582b96ff42dba0b0ad815c727d5e42)(\_mode\_) |
|  | Get SPI polarity and phase mode bits. |
| SPI Transfer modes (host controller dependent) | |
| #define | [SPI\_TRANSFER\_MSB](group__spi__interface.md#ga7761f42c6241cf396fc02d0de8617e46)   (0U) |
|  | Most significant bit first. |
| #define | [SPI\_TRANSFER\_LSB](group__spi__interface.md#ga93504a76a265bedbe781c107beebc9dc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Least significant bit first. |
| SPI word size | |
| #define | [SPI\_WORD\_SIZE\_GET](group__spi__interface.md#ga7386c70bd669142bb7558526175765cc)(\_operation\_) |
|  | Get SPI word size. |
| #define | [SPI\_WORD\_SET](group__spi__interface.md#gaaea60640bb9223bbaf94338d07d9d07c)(\_word\_size\_) |
|  | Set SPI word size. |
| Specific SPI devices control bits | |
| #define | [SPI\_HOLD\_ON\_CS](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Requests - if possible - to keep CS asserted after the transaction. |
| #define | [SPI\_LOCK\_ON](group__spi__interface.md#gafe8dc164d6fc0a0f93f2ff9d5381af14)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Keep the device locked after the transaction for the current config. |
| #define | [SPI\_CS\_ACTIVE\_HIGH](group__spi__interface.md#ga44076fa14703997f7e3aefb2bfccd801)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Active high logic on CS. |
| SPI MISO lines | |
| Some controllers support dual, quad or octal MISO lines connected to slaves.  Default is single, which is the case most of the time. Without `CONFIG_SPI_EXTENDED_MODES` being enabled, single is the only supported one. | |
| #define | [SPI\_LINES\_SINGLE](group__spi__interface.md#ga7a183f157e8cb8b437857a0babbd923b)   (0U << 16) |
|  | Single line. |
| #define | [SPI\_LINES\_DUAL](group__spi__interface.md#ga120ab60329d664d5d6e828f90251a98a)   (1U << 16) |
|  | Dual lines. |
| #define | [SPI\_LINES\_QUAD](group__spi__interface.md#ga30866b948e995224de854e10a428bda5)   (2U << 16) |
|  | Quad lines. |
| #define | [SPI\_LINES\_OCTAL](group__spi__interface.md#ga512d76085e600886654b8541aab31cf7)   (3U << 16) |
|  | Octal lines. |
| #define | [SPI\_LINES\_MASK](group__spi__interface.md#gadc79f986c4b30fe5b263841cd8bb5676)   (0x3U << 16) |
|  | Mask for MISO lines in [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a "Opaque type to hold the SPI operation flags."). |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a) |
|  | Opaque type to hold the SPI operation flags. |
| typedef int(\* | [spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Callback API for I/O See [spi\_transceive()](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5 "Read/write the specified amount of data from the SPI driver.") for argument descriptions. |
| typedef void(\* | [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)) (const struct [device](structdevice.md) \*dev, int result, void \*data) |
|  | SPI callback for asynchronous transfer requests. |
| typedef int(\* | [spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb, void \*userdata) |
| typedef int(\* | [spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config) |
|  | Callback API for unlocking SPI device. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888) (const struct [spi\_config](structspi__config.md) \*config) |
|  | Check if SPI CS is controlled using a GPIO. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Check if SPI CS in [spi\_dt\_spec](structspi__dt__spec.md "spi_dt_spec") is controlled using a GPIO. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Validate that SPI bus (and CS gpio if defined) is ready. |
| int | [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read/write data from an SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |
| static int | [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read the specified amount of data from the SPI driver. |
| static int | [spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read data from a SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |
| static int | [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs) |
|  | Write the specified amount of data from the SPI driver. |
| static int | [spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs) |
|  | Write data to a SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |
| static int | [spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) callback, void \*userdata) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Read the specified amount of data from the SPI driver. |
| static int | [spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Write the specified amount of data from the SPI driver. |
| static void | [spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit a SPI device with a request. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73) (const struct [rtio\_iodev](structrtio__iodev.md) \*spi\_iodev) |
|  | Validate that SPI bus (and CS gpio if defined) is ready. |
| static int | [spi\_rtio\_copy](group__spi__interface.md#ga812818433d437829fe6ab4fcff0ed38b) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [rtio\_sqe](structrtio__sqe.md) \*\*last\_sqe) |
|  | Copy the tx\_bufs and rx\_bufs into a set of RTIO requests. |
| int | [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config) |
|  | Release the SPI device locked on and/or the CS by the current config. |
| static int | [spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Release the SPI device specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |

| Variables | |
| --- | --- |
| const struct [rtio\_iodev\_api](structrtio__iodev__api.md) | [spi\_iodev\_api](group__spi__interface.md#gacd22d734b1b2729e09862065d44b8ce9) |

## Detailed Description

Public API for SPI drivers and applications.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi.h](drivers_2spi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
