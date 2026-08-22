---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__spi__interface.html
original_path: doxygen/html/group__spi__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SPI Interface

[Device Driver APIs](group__io__interfaces.md)

SPI Interface.
[More...](#details)

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
|  | SPI scatter-gather buffer array structure. [More...](structspi__buf__set.md#details) |
| struct | [spi\_driver\_api](structspi__driver__api.md) |
|  | SPI driver API This is the mandatory API any SPI driver needs to expose. [More...](structspi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)(node\_id, operation\_, delay\_) |
|  | Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree. |
| #define | [SPI\_CONFIG\_DT\_INST](#gadc1e7de7925603adfedbac35fdabc78a)(inst, operation\_, delay\_) |
|  | Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree instance. |
| #define | [SPI\_DT\_SPEC\_GET](#gaec6a8fde1c3ec6349a601a2d5f7af785)(node\_id, operation\_, delay\_) |
|  | Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree. |
| #define | [SPI\_DT\_SPEC\_INST\_GET](#ga91c595b7567af23b447c755d898608f3)(inst, operation\_, delay\_) |
|  | Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree instance. |
| #define | [SPI\_MOSI\_OVERRUN\_UNKNOWN](#ga15b5fa509a3b7dc87bfd451af5a11917)   0x100 |
|  | Value that will never compare true with any valid overrun character. |
| #define | [SPI\_MOSI\_OVERRUN\_DT](#gaa9621b033dfaf128602b1432927a67fe)(node\_id) |
|  | The value sent on MOSI when all TX bytes are sent, but RX continues. |
| #define | [SPI\_MOSI\_OVERRUN\_DT\_INST](#ga24c7416a98421e353a8892151f34122c)(inst) |
|  | The value sent on MOSI when all TX bytes are sent, but RX continues. |
| #define | [SPI\_STATS\_RX\_BYTES\_INC](#ga83fa04d1e9f281cd566ee32cf807325e)(dev\_) |
| #define | [SPI\_STATS\_TX\_BYTES\_INC](#gadd3b82af2396b91930ece09fa79fc4e2)(dev\_) |
| #define | [SPI\_STATS\_TRANSFER\_ERROR\_INC](#ga6f69e68a79afbbe016aecc515f14de3a)(dev\_) |
| #define | [spi\_transceive\_stats](#gad7d1058f600d6aef4fc4e2bdff5d55f3)(dev, error, tx\_bufs, rx\_bufs) |
| #define | [SPI\_DEVICE\_DT\_DEFINE](#ga27af5f053c5fd4e9eef0900406fbf854)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEINIT\_DEFINE()](group__device__model.md#gaa53f7267950569df898b0e5362e6f583 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") without deinit function. |
| #define | [SPI\_DEVICE\_DT\_INST\_DEINIT\_DEFINE](#ga50cbb6845d230033f192f1e716fd9f2b)(inst, ...) |
|  | Like [SPI\_DEVICE\_DT\_DEINIT\_DEFINE()](#gaf98b0cb38cb316b9fe05146bba34126d), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier. |
| #define | [SPI\_DEVICE\_DT\_INST\_DEFINE](#ga84811e0fdd574477c8569d559f773dae)(inst, ...) |
|  | Like [SPI\_DEVICE\_DT\_DEFINE()](#ga27af5f053c5fd4e9eef0900406fbf854), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier. |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a) |
|  | Opaque type to hold the SPI operation flags. |
| typedef int(\* | [spi\_api\_io](#ga3fc669f866b03cfdad98754de69cda13)) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Callback API for I/O See [spi\_transceive()](#gad51054c1ba259db5a64619788506a6f5) for argument descriptions. |
| typedef void(\* | [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d)) (const struct [device](structdevice.md) \*dev, int result, void \*data) |
|  | SPI callback for asynchronous transfer requests. |
| typedef int(\* | [spi\_api\_io\_async](#ga03be7f33032ac479153616bbe26848e7)) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d) cb, void \*userdata) |
| typedef int(\* | [spi\_api\_release](#gac651ff7cd3dde7abe2525e20ef2e9e7d)) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config) |
|  | Callback API for unlocking SPI device. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_cs\_is\_gpio](#gae1156a4ee1b5909c321811045566d888) (const struct [spi\_config](structspi__config.md) \*config) |
|  | Check if SPI CS is controlled using a GPIO. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_cs\_is\_gpio\_dt](#gaa13f0da1f28cffa0da4677987db0c9c5) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Check if SPI CS in [spi\_dt\_spec](structspi__dt__spec.md "spi_dt_spec") is controlled using a GPIO. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_is\_ready\_dt](#ga37b4e5079ed18b70b0c5a260f4c36403) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Validate that SPI bus (and CS gpio if defined) is ready. |
| int | [spi\_release](#ga0c4f4f0a93bb83a4f58d551a7491164e) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config) |
|  | Release the SPI device locked on and/or the CS by the current config. |
| static int | [spi\_release\_dt](#ga829b59767c51b20b546eee8a9cc84b69) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Release the SPI device specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |

| SPI Synchronous Transfer Functions | |
| --- | --- |
| These functions will not return until transfer is complete | |
| int | [spi\_transceive](#gad51054c1ba259db5a64619788506a6f5) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_transceive\_dt](#ga52c017066736414b31ff709ddc67c4ff) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read/write data from an SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |
| static int | [spi\_read](#ga41f771785a4fa9ca0954125d1e97959e) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read the specified amount of data from the SPI driver. |
| static int | [spi\_read\_dt](#ga7a1d7ebd37d2861b169c265cb90015bf) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Read data from a SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |
| static int | [spi\_write](#ga7e7c4460670ec1c0433ba19accd97796) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs) |
|  | Write the specified amount of data from the SPI driver. |
| static int | [spi\_write\_dt](#ga292d6d1fe82f3f1ce0d9a2aa5437201b) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs) |
|  | Write data to a SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |

| SPI Asynchronous Transfer Functions | |
| --- | --- |
| With this API the transfer function will return after the transfer is started and report completion through a notification mechanism: callback or signal.  Note  Note that asynchronous API calls can still be blocking if the bus is already busy. The functions will block until the bus is available to start the requested transfer. | |
| static int | [spi\_transceive\_cb](#ga6114e63ca23b82f9be0ac70e372b878b) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d) callback, void \*userdata) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_transceive\_signal](#ga41b8a541257c0d45575fdc4593417edc) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_read\_signal](#ga9a1ceadb217368232af5b688c12169c5) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Read the specified amount of data from the SPI driver. |
| static int | [spi\_write\_signal](#gadcb19d43461ef88e31f6b382cc87fd0b) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Write the specified amount of data from the SPI driver. |

| SPI RTIO API | |
| --- | --- |
| Theses functions are for using the SPI driver class through an RTIO-based API | |
| static void | [spi\_iodev\_submit](#ga8b23855bdc7dab7d02b8f7daa7db651b) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit a SPI device with a request. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_is\_ready\_iodev](#gafea78af1fe1fa49fdc5459ab3a2d5f73) (const struct [rtio\_iodev](structrtio__iodev.md) \*spi\_iodev) |
|  | Validate that SPI bus (and CS gpio if defined) is ready. |
| #define | [SPI\_DT\_IODEV\_DEFINE](#ga1e9f5fe389d53c280639f23ea134e18c)(name, node\_id, operation\_, delay\_) |
|  | Define an iodev for a given dt node on the bus. |

| SPI operational mode | |
| --- | --- |
| #define | [SPI\_OP\_MODE\_MASTER](#ga5b9d40fa0f455b1e63f8040b3316b0da)   0U |
|  | Master (controller) mode. |
| #define | [SPI\_OP\_MODE\_SLAVE](#ga1c3310d3711cb99cdb78fa9d1c970779)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Slave (peripheral) mode. |
| #define | [SPI\_OP\_MODE\_GET](#ga6dd4395e027407a7b3b92cff2abcc8b3)(\_operation\_) |
|  | Get SPI Operational mode bitmask from a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a). |

| SPI Clock Modes | |
| --- | --- |
| #define | [SPI\_MODE\_CPOL](#ga5a2be1003873beaa0ade10e7218d67d5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Clock Polarity (Clock Idle State). |
| #define | [SPI\_MODE\_CPHA](#ga35e98b37e3ec4889a90100abe884590f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Clock Phase (Clock data capture edge). |
| #define | [SPI\_MODE\_LOOP](#ga8619b297de563eca6852af34c79daa62)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Controller loopback mode. |
| #define | [SPI\_MODE\_GET](#gaa3582b96ff42dba0b0ad815c727d5e42)(\_mode\_) |
|  | Get SPI clock polarity and phase mode bitmask from a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a). |

| SPI Data Word Configurations | |
| --- | --- |
| A SPI Data word is a value that is shifted in/out of the controller's hardware FIFO and is the atomic unit of communication on the spi bus.  A word is also called a "data frame" in this API. A transfer is made up of an arbitrary number of words. The following options specify configurations of the SPI word for the operation. | |
| #define | [SPI\_TRANSFER\_MSB](#ga7761f42c6241cf396fc02d0de8617e46)   (0U) |
|  | Words are most significant bit first, used for [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a). |
| #define | [SPI\_TRANSFER\_LSB](#ga93504a76a265bedbe781c107beebc9dc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Words are least significant bit first, used for [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a). |
| #define | [SPI\_WORD\_SIZE\_GET](#gacd7edd9ce02bd8351f8eebe5b5c07c7a)(operation) |
|  | Get SPI word size in bits from a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a). |
| #define | [SPI\_WORD\_SET](#gac1115bf80134efd38d88161e3f5e3e1a)(word\_size) |
|  | Get a bitmask to set the word size in a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a). |

| SPI Transfer control flags | |
| --- | --- |
| #define | [SPI\_HOLD\_ON\_CS](#gae917312adef283b4bf67cdb53566e4bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Keep chip select active after transaction. |
| #define | [SPI\_LOCK\_ON](#gafe8dc164d6fc0a0f93f2ff9d5381af14)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Retain ownership of the spi device. |
| #define | [SPI\_CS\_ACTIVE\_HIGH](#ga44076fa14703997f7e3aefb2bfccd801)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Chip select active state configuration. |

| SPI MISO lines | |
| --- | --- |
| Some controllers support dual, quad or octal MISO lines connected to slaves.  Default is single, which is the case most of the time. Without `CONFIG_SPI_EXTENDED_MODES` being enabled, single is the only supported one. | |
| #define | [SPI\_LINES\_SINGLE](#ga7a183f157e8cb8b437857a0babbd923b)   (0U << 16) |
|  | Single line. |
| #define | [SPI\_LINES\_DUAL](#ga120ab60329d664d5d6e828f90251a98a)   (1U << 16) |
|  | Dual lines. |
| #define | [SPI\_LINES\_QUAD](#ga30866b948e995224de854e10a428bda5)   (2U << 16) |
|  | Quad lines. |
| #define | [SPI\_LINES\_OCTAL](#ga512d76085e600886654b8541aab31cf7)   (3U << 16) |
|  | Octal lines. |
| #define | [SPI\_LINES\_MASK](#gadc79f986c4b30fe5b263841cd8bb5676)   (0x3U << 16) |
|  | Mask for MISO lines in [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a). |

| SPI GPIO Chip Select control | |
| --- | --- |
| #define | [SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)(spi\_dev) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin. |
| #define | [SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET](#ga88fefbfadb8184806123e1f935a4ff7c)(inst) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin. |
| #define | [SPI\_CS\_CONTROL\_INIT](#ga4a2bce02956d8121da7b6099f6c097b9)(node\_id, delay\_) |
|  | Initialize and get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node identifier. |
| #define | [SPI\_CS\_CONTROL\_INIT\_INST](#ga239bda66980ed0a349b7177100f7752c)(inst, delay\_) |
|  | Get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node. |

| SPI DT Device Macros | |
| --- | --- |
| #define | [SPI\_DEVICE\_DT\_DEINIT\_DEFINE](#gaf98b0cb38cb316b9fe05146bba34126d)(node\_id, init\_fn, deinit\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEINIT\_DEFINE()](group__device__model.md#gaa53f7267950569df898b0e5362e6f583 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with SPI specifics. |

| SPI duplex mode | |
| --- | --- |
| Some controllers support half duplex transfer, which results in 3-wire usage.  By default, full duplex will prevail. | |
| #define | [SPI\_FULL\_DUPLEX](#ga5585d5e81dec606b605f31b6745c35d3)   (0U << 11) |
| #define | [SPI\_HALF\_DUPLEX](#ga602a7804b7434d7ebc1ebe6cb9b47a2f)   (1U << 11) |

| SPI Frame Format | |
| --- | --- |
| 2 frame formats are exposed: Motorola and TI.  The main difference is the behavior of the CS line. In Motorola it stays active the whole transfer. In TI, it's active only one serial clock period prior to actually make the transfer, it is thus inactive during the transfer, which ends when the clocks ends as well. By default, as it is the most commonly used, the Motorola frame format will prevail. | |
| #define | [SPI\_FRAME\_FORMAT\_MOTOROLA](#ga6a1b4ba33900165b6e09706903a6e6ee)   (0U << 15) |
| #define | [SPI\_FRAME\_FORMAT\_TI](#ga22801357a9682371e3d8a10e522de388)   (1U << 15) |

## Detailed Description

SPI Interface.

Since
:   1.0

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga822af066ee0829aee405c034bb967463)SPI\_CONFIG\_DT

| #define SPI\_CONFIG\_DT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

{ \

.frequency = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, spi\_max\_frequency), \

.operation = (operation\_) | \

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, duplex) | \

DT\_PROP(node\_id, frame\_format) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, spi\_cpol), [SPI\_MODE\_CPOL](#ga5a2be1003873beaa0ade10e7218d67d5), (0)) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, spi\_cpha), [SPI\_MODE\_CPHA](#ga35e98b37e3ec4889a90100abe884590f), (0)) | \

COND\_CODE\_1([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, spi\_hold\_cs), [SPI\_HOLD\_ON\_CS](#gae917312adef283b4bf67cdb53566e4bb), (0)), \

.slave = [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id), \

.cs = [SPI\_CS\_CONTROL\_INIT](#ga4a2bce02956d8121da7b6099f6c097b9)(node\_id, delay\_), \

}

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2461

[SPI\_MODE\_CPHA](#ga35e98b37e3ec4889a90100abe884590f)

#define SPI\_MODE\_CPHA

Clock Phase (Clock data capture edge).

**Definition** spi.h:98

[SPI\_CS\_CONTROL\_INIT](#ga4a2bce02956d8121da7b6099f6c097b9)

#define SPI\_CS\_CONTROL\_INIT(node\_id, delay\_)

Initialize and get a pointer to a spi\_cs\_control from a devicetree node identifier.

**Definition** spi.h:349

[SPI\_MODE\_CPOL](#ga5a2be1003873beaa0ade10e7218d67d5)

#define SPI\_MODE\_CPOL

Clock Polarity (Clock Idle State).

**Definition** spi.h:87

[SPI\_HOLD\_ON\_CS](#gae917312adef283b4bf67cdb53566e4bb)

#define SPI\_HOLD\_ON\_CS

Keep chip select active after transaction.

**Definition** spi.h:179

Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree.

This helper macro expands to a static initializer for a struct
[spi\_config](structspi__config.md "SPI controller configuration structure.") by reading the relevant `frequency`, `slave`, and `cs` data from the devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the SPI device whose struct [spi\_config](structspi__config.md "SPI controller configuration structure.") to create an initializer for |
    | --- | --- |
    | operation\_ | the desired `operation` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired `delay` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## [◆ ](#gadc1e7de7925603adfedbac35fdabc78a)SPI\_CONFIG\_DT\_INST

| #define SPI\_CONFIG\_DT\_INST | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), operation\_, delay\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

[SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)

#define SPI\_CONFIG\_DT(node\_id, operation\_, delay\_)

Structure initializer for spi\_config from devicetree.

**Definition** spi.h:436

Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree instance.

This is equivalent to [SPI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)](#ga822af066ee0829aee405c034bb967463).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |
    | operation\_ | the desired `operation` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired `delay` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## [◆ ](#ga44076fa14703997f7e3aefb2bfccd801)SPI\_CS\_ACTIVE\_HIGH

| #define SPI\_CS\_ACTIVE\_HIGH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Chip select active state configuration.

If this flag is set, the CS will be active high. If this flag is unset, the CS will be active low.

Default is active low (unset) as that is most common for spi peripherals.

Not all controllers are able to handle this natively, in which case a gpio can still be used to control the CS through software with a [spi\_cs\_control](structspi__cs__control.md "spi_cs_control")

## [◆ ](#ga4a2bce02956d8121da7b6099f6c097b9)SPI\_CS\_CONTROL\_INIT

| #define SPI\_CS\_CONTROL\_INIT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *delay\_* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

{ \

.gpio = [SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)(node\_id), \

.delay = (delay\_), \

}

[SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)

#define SPI\_CS\_GPIOS\_DT\_SPEC\_GET(spi\_dev)

Get a struct gpio\_dt\_spec for a SPI device's chip select pin.

**Definition** spi.h:295

Initialize and get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node identifier.

This helper is useful for initializing a device on a SPI bus. It initializes a struct [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure.") and returns a pointer to it. Here, `node_id` is a node identifier for a SPI device, not a SPI controller.

Example devicetree fragment:

spi@abcd0001 {

cs-gpios = <&gpio0 1 GPIO\_ACTIVE\_LOW>;

spidev: spi-device@0 { ... };

};

Example usage:

struct [spi\_cs\_control](structspi__cs__control.md) ctrl =

[SPI\_CS\_CONTROL\_INIT](#ga4a2bce02956d8121da7b6099f6c097b9)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(spidev), 2);

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[spi\_cs\_control](structspi__cs__control.md)

SPI Chip Select control structure.

**Definition** spi.h:242

This example is equivalent to:

struct [spi\_cs\_control](structspi__cs__control.md) ctrl = {

.gpio = [SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(spidev)),

.delay = 2,

};

Parameters
:   | node\_id | Devicetree node identifier for a device on a SPI bus |
    | --- | --- |
    | delay\_ | The `delay` field to set in the `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` |

Returns
:   a pointer to the `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` structure

## [◆ ](#ga239bda66980ed0a349b7177100f7752c)SPI\_CS\_CONTROL\_INIT\_INST

| #define SPI\_CS\_CONTROL\_INIT\_INST | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *delay\_* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_CS\_CONTROL\_INIT](#ga4a2bce02956d8121da7b6099f6c097b9)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), delay\_)

Get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node.

This is equivalent to [SPI\_CS\_CONTROL\_INIT(DT\_DRV\_INST(inst), delay)](#ga4a2bce02956d8121da7b6099f6c097b9).

Therefore, `DT_DRV_COMPAT` must already be defined before using this macro.

Parameters
:   | inst | Devicetree node instance number |
    | --- | --- |
    | delay\_ | The `delay` field to set in the `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` |

Returns
:   a pointer to the `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` structure

## [◆ ](#ga48aa19f45413d56b03596d10b72c732e)SPI\_CS\_GPIOS\_DT\_SPEC\_GET

| #define SPI\_CS\_GPIOS\_DT\_SPEC\_GET | ( |  | *spi\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(spi\_dev), cs\_gpios, \

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(spi\_dev), {})

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3861

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)

#define DT\_REG\_ADDR\_RAW(node\_id)

Get a node's (only) register block raw address.

**Definition** devicetree.h:2428

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value)

Like GPIO\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** gpio.h:356

Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin.

Example devicetree fragment:

gpio1: gpio@abcd0001 { ... };

gpio2: gpio@abcd0002 { ... };

spi@abcd0003 {

compatible = "vnd,spi";

cs-gpios = <&gpio1 10 GPIO\_ACTIVE\_LOW>,

<&gpio2 20 GPIO\_ACTIVE\_LOW>;

a: spi-dev-a@0 {

reg = <0>;

};

b: spi-dev-b@1 {

reg = <1>;

};

};

Example usage:

[SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(a)) \

// { DEVICE\_DT\_GET(DT\_NODELABEL(gpio1)), 10, GPIO\_ACTIVE\_LOW }

[SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(b)) \

// { DEVICE\_DT\_GET(DT\_NODELABEL(gpio2)), 20, GPIO\_ACTIVE\_LOW }

Parameters
:   | spi\_dev | a SPI device node identifier |
    | --- | --- |

Returns
:   [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") struct corresponding with spi\_dev's chip select

## [◆ ](#ga88fefbfadb8184806123e1f935a4ff7c)SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET

| #define SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin.

This is equivalent to [SPI\_CS\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))](#ga48aa19f45413d56b03596d10b72c732e).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

Returns
:   [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") struct corresponding with spi\_dev's chip select

## [◆ ](#ga27af5f053c5fd4e9eef0900406fbf854)SPI\_DEVICE\_DT\_DEFINE

| #define SPI\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | ... ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_DEVICE\_DT\_DEINIT\_DEFINE](#gaf98b0cb38cb316b9fe05146bba34126d)(node\_id, init\_fn, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), pm, data, config, \

level, prio, api, \_\_VA\_ARGS\_\_)

[SPI\_DEVICE\_DT\_DEINIT\_DEFINE](#gaf98b0cb38cb316b9fe05146bba34126d)

#define SPI\_DEVICE\_DT\_DEINIT\_DEFINE(node\_id, init\_fn, deinit\_fn, pm, data, config, level, prio, api,...)

Like DEVICE\_DT\_DEINIT\_DEFINE() with SPI specifics.

**Definition** spi.h:724

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Like [DEVICE\_DT\_DEINIT\_DEFINE()](group__device__model.md#gaa53f7267950569df898b0e5362e6f583 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") without deinit function.

Defines a device which implements the SPI API. May generate a custom [device\_state](structdevice__state.md "Runtime device dynamic structure (in RAM) per driver instance.") container struct and init\_fn wrapper when needed depending on SPI `CONFIG_SPI_STATS`.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Name of the init function of the driver. |
    | pm | PM device resources reference (NULL if device does not use PM). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#gaf98b0cb38cb316b9fe05146bba34126d)SPI\_DEVICE\_DT\_DEINIT\_DEFINE

| #define SPI\_DEVICE\_DT\_DEINIT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *deinit\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | ... ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), init\_fn, deinit\_fn, \

Z\_DEVICE\_DT\_FLAGS(node\_id), pm, data, config, \

level, prio, api, \

&Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

\_\_VA\_ARGS\_\_)

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:201

Like [DEVICE\_DT\_DEINIT\_DEFINE()](group__device__model.md#gaa53f7267950569df898b0e5362e6f583 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with SPI specifics.

Defines a device which implements the SPI API. May generate a custom [device\_state](structdevice__state.md "Runtime device dynamic structure (in RAM) per driver instance.") container struct and init\_fn wrapper when needed depending on SPI `CONFIG_SPI_STATS`.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Name of the init function of the driver. |
    | deinit\_fn | Name of the deinit function of the driver. |
    | pm | PM device resources reference (NULL if device does not use PM). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#ga84811e0fdd574477c8569d559f773dae)SPI\_DEVICE\_DT\_INST\_DEFINE

| #define SPI\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_DEVICE\_DT\_DEFINE](#ga27af5f053c5fd4e9eef0900406fbf854)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[SPI\_DEVICE\_DT\_DEFINE](#ga27af5f053c5fd4e9eef0900406fbf854)

#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api,...)

Like DEVICE\_DT\_DEINIT\_DEFINE() without deinit function.

**Definition** spi.h:763

Like [SPI\_DEVICE\_DT\_DEFINE()](#ga27af5f053c5fd4e9eef0900406fbf854), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier.

Parameters
:   | inst | Instance number. The node\_id argument to [SPI\_DEVICE\_DT\_DEFINE()](#ga27af5f053c5fd4e9eef0900406fbf854) is set to [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible."). |
    | --- | --- |
    | ... | Other parameters as expected by [SPI\_DEVICE\_DT\_DEFINE()](#ga27af5f053c5fd4e9eef0900406fbf854). |

## [◆ ](#ga50cbb6845d230033f192f1e716fd9f2b)SPI\_DEVICE\_DT\_INST\_DEINIT\_DEFINE

| #define SPI\_DEVICE\_DT\_INST\_DEINIT\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_DEVICE\_DT\_DEINIT\_DEFINE](#gaf98b0cb38cb316b9fe05146bba34126d)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

Like [SPI\_DEVICE\_DT\_DEINIT\_DEFINE()](#gaf98b0cb38cb316b9fe05146bba34126d), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier.

Parameters
:   | inst | Instance number. The node\_id argument to [SPI\_DEVICE\_DT\_DEINIT\_DEFINE()](#gaf98b0cb38cb316b9fe05146bba34126d) is set to [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible."). |
    | --- | --- |
    | ... | Other parameters as expected by [SPI\_DEVICE\_DT\_DEFINE()](#ga27af5f053c5fd4e9eef0900406fbf854). |

## [◆ ](#ga1e9f5fe389d53c280639f23ea134e18c)SPI\_DT\_IODEV\_DEFINE

| #define SPI\_DT\_IODEV\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id*, |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

const struct [spi\_dt\_spec](structspi__dt__spec.md) \_spi\_dt\_spec\_##name = \

SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_); \

RTIO\_IODEV\_DEFINE(name, &spi\_iodev\_api, (void \*)&\_spi\_dt\_spec\_##name)

[spi\_dt\_spec](structspi__dt__spec.md)

Complete SPI DT information.

**Definition** spi.h:466

Define an iodev for a given dt node on the bus.

These do not need to be shared globally but doing so will save a small amount of memory.

Parameters
:   | name | Symbolic name to use for defining the iodev |
    | --- | --- |
    | node\_id | Devicetree node identifier |
    | operation\_ | SPI operational mode |
    | delay\_ | Chip select delay in microseconds |

## [◆ ](#gaec6a8fde1c3ec6349a601a2d5f7af785)SPI\_DT\_SPEC\_GET

| #define SPI\_DT\_SPEC\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

{ \

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.config = [SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)(node\_id, operation\_, delay\_) \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:314

Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree.

This helper macro expands to a static initializer for a struct
[spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") by reading the relevant bus, frequency, slave, and cs data from the devicetree.

Important: multiple fields are automatically constructed by this macro which must be checked before use. [spi\_is\_ready\_dt](#ga37b4e5079ed18b70b0c5a260f4c36403) performs the required [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb "device_is_ready") checks.

Parameters
:   | node\_id | Devicetree node identifier for the SPI device whose struct [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") to create an initializer for |
    | --- | --- |
    | operation\_ | the desired `operation` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired `delay` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## [◆ ](#ga91c595b7567af23b447c755d898608f3)SPI\_DT\_SPEC\_INST\_GET

| #define SPI\_DT\_SPEC\_INST\_GET | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_DT\_SPEC\_GET](#gaec6a8fde1c3ec6349a601a2d5f7af785)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), operation\_, delay\_)

[SPI\_DT\_SPEC\_GET](#gaec6a8fde1c3ec6349a601a2d5f7af785)

#define SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_)

Structure initializer for spi\_dt\_spec from devicetree.

**Definition** spi.h:490

Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree instance.

This is equivalent to [SPI\_DT\_SPEC\_GET(DT\_DRV\_INST(inst), operation\_, delay\_)](#gaec6a8fde1c3ec6349a601a2d5f7af785).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |
    | operation\_ | the desired `operation` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.") |
    | delay\_ | the desired `delay` field in the struct [spi\_config](structspi__config.md "SPI controller configuration structure.")'s [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure."), if there is one |

## [◆ ](#ga6a1b4ba33900165b6e09706903a6e6ee)SPI\_FRAME\_FORMAT\_MOTOROLA

| #define SPI\_FRAME\_FORMAT\_MOTOROLA   (0U << 15) |
| --- |

`#include <[zephyr/dt-bindings/spi/spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#ga22801357a9682371e3d8a10e522de388)SPI\_FRAME\_FORMAT\_TI

| #define SPI\_FRAME\_FORMAT\_TI   (1U << 15) |
| --- |

`#include <[zephyr/dt-bindings/spi/spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#ga5585d5e81dec606b605f31b6745c35d3)SPI\_FULL\_DUPLEX

| #define SPI\_FULL\_DUPLEX   (0U << 11) |
| --- |

`#include <[zephyr/dt-bindings/spi/spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#ga602a7804b7434d7ebc1ebe6cb9b47a2f)SPI\_HALF\_DUPLEX

| #define SPI\_HALF\_DUPLEX   (1U << 11) |
| --- |

`#include <[zephyr/dt-bindings/spi/spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#gae917312adef283b4bf67cdb53566e4bb)SPI\_HOLD\_ON\_CS

| #define SPI\_HOLD\_ON\_CS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Keep chip select active after transaction.

After one of the spi transceive calls described in this API, if this flag is set in the spi config operation, then attempt to keep the CS active after the call, if supported and possible.

## [◆ ](#ga120ab60329d664d5d6e828f90251a98a)SPI\_LINES\_DUAL

| #define SPI\_LINES\_DUAL   (1U << 16) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Dual lines.

## [◆ ](#gadc79f986c4b30fe5b263841cd8bb5676)SPI\_LINES\_MASK

| #define SPI\_LINES\_MASK   (0x3U << 16) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Mask for MISO lines in [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

## [◆ ](#ga512d76085e600886654b8541aab31cf7)SPI\_LINES\_OCTAL

| #define SPI\_LINES\_OCTAL   (3U << 16) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Octal lines.

## [◆ ](#ga30866b948e995224de854e10a428bda5)SPI\_LINES\_QUAD

| #define SPI\_LINES\_QUAD   (2U << 16) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Quad lines.

## [◆ ](#ga7a183f157e8cb8b437857a0babbd923b)SPI\_LINES\_SINGLE

| #define SPI\_LINES\_SINGLE   (0U << 16) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Single line.

## [◆ ](#gafe8dc164d6fc0a0f93f2ff9d5381af14)SPI\_LOCK\_ON

| #define SPI\_LOCK\_ON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Retain ownership of the spi device.

This is a software control parameter that will prevent the spi device from being accessed by other API callers after the transaction, and therefore should be used with caution.

The identifying piece of information for who "locks" the device is the [spi\_config](structspi__config.md "SPI controller configuration structure.") pointer given to the transaction API, so this same config should be re-used to do another transaction or release the lock.

See [spi\_release](#ga0c4f4f0a93bb83a4f58d551a7491164e) for how to release the lock.

## [◆ ](#ga35e98b37e3ec4889a90100abe884590f)SPI\_MODE\_CPHA

| #define SPI\_MODE\_CPHA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Clock Phase (Clock data capture edge).

Used in [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a) definition. If set, data is captured on transition from active to idle CLK state. If unset, data is captured on transition from idle to active state. Unset is the default.

## [◆ ](#ga5a2be1003873beaa0ade10e7218d67d5)SPI\_MODE\_CPOL

| #define SPI\_MODE\_CPOL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Clock Polarity (Clock Idle State).

Used in [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a) definition. If set, clock idle state will be 1 and active state will be 0. If unset, clock idle state will be 0 and active state will be 1. Unset is the default.

## [◆ ](#gaa3582b96ff42dba0b0ad815c727d5e42)SPI\_MODE\_GET

| #define SPI\_MODE\_GET | ( |  | *\_mode\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

((\_mode\_) & SPI\_MODE\_MASK)

Get SPI clock polarity and phase mode bitmask from a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

## [◆ ](#ga8619b297de563eca6852af34c79daa62)SPI\_MODE\_LOOP

| #define SPI\_MODE\_LOOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Controller loopback mode.

For testing purposes, enable hardware loopback, which means that transmit data is fed back to the receiver of the same controller.

Not all controllers support this feature.

## [◆ ](#gaa9621b033dfaf128602b1432927a67fe)SPI\_MOSI\_OVERRUN\_DT

| #define SPI\_MOSI\_OVERRUN\_DT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, overrun\_character, [SPI\_MOSI\_OVERRUN\_UNKNOWN](#ga15b5fa509a3b7dc87bfd451af5a11917))

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:935

[SPI\_MOSI\_OVERRUN\_UNKNOWN](#ga15b5fa509a3b7dc87bfd451af5a11917)

#define SPI\_MOSI\_OVERRUN\_UNKNOWN

Value that will never compare true with any valid overrun character.

**Definition** spi.h:513

The value sent on MOSI when all TX bytes are sent, but RX continues.

For drivers where the MOSI line state when receiving is important, this value can be queried at compile-time to determine whether allocating a constant array is necessary.

Parameters
:   | node\_id | Devicetree node identifier for the SPI device to query |
    | --- | --- |

Return values
:   | [SPI\_MOSI\_OVERRUN\_UNKNOWN](#ga15b5fa509a3b7dc87bfd451af5a11917) | if controller does not export the value |
    | --- | --- |
    | byte | default MOSI value otherwise |

## [◆ ](#ga24c7416a98421e353a8892151f34122c)SPI\_MOSI\_OVERRUN\_DT\_INST

| #define SPI\_MOSI\_OVERRUN\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

[DT\_INST\_PROP\_OR](group__devicetree-inst.md#gaa51bd8f5b016244e0256b3ed9aceee7f)(inst, overrun\_character, [SPI\_MOSI\_OVERRUN\_UNKNOWN](#ga15b5fa509a3b7dc87bfd451af5a11917))

[DT\_INST\_PROP\_OR](group__devicetree-inst.md#gaa51bd8f5b016244e0256b3ed9aceee7f)

#define DT\_INST\_PROP\_OR(inst, prop, default\_value)

Like DT\_INST\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:4237

The value sent on MOSI when all TX bytes are sent, but RX continues.

This is equivalent to [SPI\_MOSI\_OVERRUN\_DT(DT\_DRV\_INST(inst))](#gaa9621b033dfaf128602b1432927a67fe).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

Return values
:   | [SPI\_MOSI\_OVERRUN\_UNKNOWN](#ga15b5fa509a3b7dc87bfd451af5a11917) | if controller does not export the value |
    | --- | --- |
    | byte | default MOSI value otherwise |

## [◆ ](#ga15b5fa509a3b7dc87bfd451af5a11917)SPI\_MOSI\_OVERRUN\_UNKNOWN

| #define SPI\_MOSI\_OVERRUN\_UNKNOWN   0x100 |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Value that will never compare true with any valid overrun character.

## [◆ ](#ga6dd4395e027407a7b3b92cff2abcc8b3)SPI\_OP\_MODE\_GET

| #define SPI\_OP\_MODE\_GET | ( |  | *\_operation\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

((\_operation\_) & SPI\_OP\_MODE\_MASK)

Get SPI Operational mode bitmask from a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

## [◆ ](#ga5b9d40fa0f455b1e63f8040b3316b0da)SPI\_OP\_MODE\_MASTER

| #define SPI\_OP\_MODE\_MASTER   0U |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Master (controller) mode.

In this case the device used with the API will function as a controller, meaning it will control the CLK line on the SPI bus and the chip select, and therefore have full control over the timing of the transaction.

## [◆ ](#ga1c3310d3711cb99cdb78fa9d1c970779)SPI\_OP\_MODE\_SLAVE

| #define SPI\_OP\_MODE\_SLAVE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Slave (peripheral) mode.

With this mode, the device will function as a peripheral, meaning it will need to wait for it's select line to be asserted, and will be need to be subject to pacing by a controller's clock in order to send and receive data during a transaction. Slave mode.

## [◆ ](#ga83fa04d1e9f281cd566ee32cf807325e)SPI\_STATS\_RX\_BYTES\_INC

| #define SPI\_STATS\_RX\_BYTES\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

## [◆ ](#ga6f69e68a79afbbe016aecc515f14de3a)SPI\_STATS\_TRANSFER\_ERROR\_INC

| #define SPI\_STATS\_TRANSFER\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

## [◆ ](#gadd3b82af2396b91930ece09fa79fc4e2)SPI\_STATS\_TX\_BYTES\_INC

| #define SPI\_STATS\_TX\_BYTES\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

## [◆ ](#gad7d1058f600d6aef4fc4e2bdff5d55f3)spi\_transceive\_stats

| #define spi\_transceive\_stats | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *error*, |
|  |  |  | *tx\_bufs*, |
|  |  |  | *rx\_bufs* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

## [◆ ](#ga93504a76a265bedbe781c107beebc9dc)SPI\_TRANSFER\_LSB

| #define SPI\_TRANSFER\_LSB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Words are least significant bit first, used for [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

## [◆ ](#ga7761f42c6241cf396fc02d0de8617e46)SPI\_TRANSFER\_MSB

| #define SPI\_TRANSFER\_MSB   (0U) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Words are most significant bit first, used for [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

## [◆ ](#gac1115bf80134efd38d88161e3f5e3e1a)SPI\_WORD\_SET

| #define SPI\_WORD\_SET | ( |  | *word\_size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

((word\_size) << SPI\_WORD\_SIZE\_SHIFT)

Get a bitmask to set the word size in a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

Parameters
:   | word\_size | The size of a SPI data frame in bits. |
    | --- | --- |

Return values
:   | A | bitmask to apply to a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a) |
    | --- | --- |

## [◆ ](#gacd7edd9ce02bd8351f8eebe5b5c07c7a)SPI\_WORD\_SIZE\_GET

| #define SPI\_WORD\_SIZE\_GET | ( |  | *operation* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

**Value:**

(((operation) & SPI\_WORD\_SIZE\_MASK) >> SPI\_WORD\_SIZE\_SHIFT)

Get SPI word size in bits from a [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

Parameters
:   | operation | A [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a) from which to get the configured word size. |
    | --- | --- |

Return values
:   | The | size (in bits) of a spi word for the operation. |
    | --- | --- |

## Typedef Documentation

## [◆ ](#ga3fc669f866b03cfdad98754de69cda13)spi\_api\_io

| typedef int(\* spi\_api\_io) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Callback API for I/O See [spi\_transceive()](#gad51054c1ba259db5a64619788506a6f5) for argument descriptions.

Callback API for asynchronous I/O See [spi\_transceive\_signal()](#ga41b8a541257c0d45575fdc4593417edc) for argument descriptions.

## [◆ ](#ga03be7f33032ac479153616bbe26848e7)spi\_api\_io\_async

| typedef int(\* spi\_api\_io\_async) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d) cb, void \*userdata) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

## [◆ ](#gac651ff7cd3dde7abe2525e20ef2e9e7d)spi\_api\_release

| typedef int(\* spi\_api\_release) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Callback API for unlocking SPI device.

See [spi\_release()](#ga0c4f4f0a93bb83a4f58d551a7491164e) for argument descriptions

## [◆ ](#ga1db2a410f482d0f26c49f96352aa606d)spi\_callback\_t

| typedef void(\* spi\_callback\_t) (const struct [device](structdevice.md) \*dev, int result, void \*data) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

SPI callback for asynchronous transfer requests.

Parameters
:   | dev | SPI device which is notifying of transfer completion or error |
    | --- | --- |
    | result | Result code of the transfer request. 0 is success, -errno for failure. |
    | data | Transfer requester supplied data which is passed along to the callback. |

## [◆ ](#ga398a8ae1c4799e77fb6c067b6d47294a)spi\_operation\_t

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a) |
| --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Opaque type to hold the SPI operation flags.

## Function Documentation

## [◆ ](#gae1156a4ee1b5909c321811045566d888)spi\_cs\_is\_gpio()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_cs\_is\_gpio | ( | const struct [spi\_config](structspi__config.md) \* | *config* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Check if SPI CS is controlled using a GPIO.

Parameters
:   | config | SPI configuration. |
    | --- | --- |

Returns
:   true If CS is controlled using a GPIO.
:   false If CS is controlled by hardware or any other means.

## [◆ ](#gaa13f0da1f28cffa0da4677987db0c9c5)spi\_cs\_is\_gpio\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_cs\_is\_gpio\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Check if SPI CS in [spi\_dt\_spec](structspi__dt__spec.md "spi_dt_spec") is controlled using a GPIO.

Parameters
:   | spec | SPI specification from devicetree. |
    | --- | --- |

Returns
:   true If CS is controlled using a GPIO.
:   false If CS is controlled by hardware or any other means.

## [◆ ](#ga8b23855bdc7dab7d02b8f7daa7db651b)spi\_iodev\_submit()

| | void spi\_iodev\_submit | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Submit a SPI device with a request.

Parameters
:   | iodev\_sqe | Prepared submissions queue entry connected to an iodev defined by SPI\_IODEV\_DEFINE. Must live as long as the request is in flight. |
    | --- | --- |

## [◆ ](#ga37b4e5079ed18b70b0c5a260f4c36403)spi\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_is\_ready\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Validate that SPI bus (and CS gpio if defined) is ready.

Parameters
:   | spec | SPI specification from devicetree |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the SPI bus is ready for use. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the SPI bus (or the CS gpio defined) is not ready for use. |

## [◆ ](#gafea78af1fe1fa49fdc5459ab3a2d5f73)spi\_is\_ready\_iodev()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_is\_ready\_iodev | ( | const struct [rtio\_iodev](structrtio__iodev.md) \* | *spi\_iodev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Validate that SPI bus (and CS gpio if defined) is ready.

Parameters
:   | spi\_iodev | SPI iodev defined with SPI\_DT\_IODEV\_DEFINE |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the SPI bus is ready for use. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the SPI bus (or the CS gpio defined) is not ready for use. |

## [◆ ](#ga41f771785a4fa9ca0954125d1e97959e)spi\_read()

| | int spi\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Read the specified amount of data from the SPI driver.

Note
:   This function is synchronous.
:   This function is a helper function calling spi\_transceive.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | rx\_bufs | Buffer array where data to be read will be written to. |

Return values
:   | frames | Positive number of frames received in slave mode. |
    | --- | --- |
    | 0 | If successful. |
    | -ENOTSUP | means some part of the spi config is not supported either by the device hardware or the driver software. |
    | -EINVAL | means that some parameter of the [spi\_config](structspi__config.md "SPI controller configuration structure.") is invalid. |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga7a1d7ebd37d2861b169c265cb90015bf)spi\_read\_dt()

| | int spi\_read\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Read data from a SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`.

This is equivalent to:

```
spi_read(spec->bus, &spec->config, rx_bufs);
```

Parameters
:   | spec | SPI specification from devicetree |
    | --- | --- |
    | rx\_bufs | Buffer array where data to be read will be written to. |

Returns
:   a value from [spi\_read()](#ga41f771785a4fa9ca0954125d1e97959e).

## [◆ ](#ga9a1ceadb217368232af5b688c12169c5)spi\_read\_signal()

| | int spi\_read\_signal | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Read the specified amount of data from the SPI driver.

Note
:   This function is asynchronous.
:   This function is a helper function calling spi\_transceive\_signal.
:   This function is available only if `CONFIG_SPI_ASYNC` and `CONFIG_POLL` are selected.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | rx\_bufs | Buffer array where data to be read will be written to. |
    | sig | A pointer to a valid and ready to be signaled struct [k\_poll\_signal](structk__poll__signal.md). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not). |

Return values
:   | frames | Positive number of frames received in slave mode. |
    | --- | --- |
    | 0 | If successful |
    | -ENOTSUP | means some part of the spi config is not supported either by the device hardware or the driver software. |
    | -EINVAL | means that some parameter of the [spi\_config](structspi__config.md "SPI controller configuration structure.") is invalid. |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga0c4f4f0a93bb83a4f58d551a7491164e)spi\_release()

| int spi\_release | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [spi\_config](structspi__config.md) \* | *config* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Release the SPI device locked on and/or the CS by the current config.

Note: This synchronous function is used to release either the lock on the SPI device and/or the CS line that was kept if, and if only, given config parameter was the last one to be used (in any of the above functions) and if it has the SPI\_LOCK\_ON bit set and/or the SPI\_HOLD\_ON\_CS bit set into its operation bits field. This can be used if the caller needs to keep its hand on the SPI device for consecutive transactions and/or if it needs the device to stay selected. Usually both bits will be used along each other, so the the device is locked and stays on until another operation is necessary or until it gets released with the present function.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga829b59767c51b20b546eee8a9cc84b69)spi\_release\_dt()

| | int spi\_release\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Release the SPI device specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`.

This is equivalent to:

```
spi_release(spec->bus, &spec->config);
```

Parameters
:   | spec | SPI specification from devicetree |
    | --- | --- |

Returns
:   a value from [spi\_release()](#ga0c4f4f0a93bb83a4f58d551a7491164e).

## [◆ ](#gad51054c1ba259db5a64619788506a6f5)spi\_transceive()

| int spi\_transceive | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [spi\_config](structspi__config.md) \* | *config*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Read/write the specified amount of data from the SPI driver.

Note
:   This function is synchronous.
:   In master mode, the chip select line will remain asserted (active) for the entire duration of the transfer of all buffers in the provided buf sets. Only after all buffers have been transferred will CS be deasserted.
:   In peripheral mode, data transfer happens when the master asserts CS and provides the clock. The function will wait for the master to complete the transfer before returning. The CS is controlled by master and therefore may not be continuously asserted for the whole transfer.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | tx\_bufs | Buffer array where data to be sent originates from, or NULL if none. |
    | rx\_bufs | Buffer array where data to be read will be written to, or NULL if none. |

Return values
:   | frames | Positive number of frames received in slave mode. |
    | --- | --- |
    | 0 | If successful in master mode. |
    | -ENOTSUP | means some part of the spi config is not supported either by the device hardware or the driver software. |
    | -EINVAL | means that some parameter of the [spi\_config](structspi__config.md "SPI controller configuration structure.") is invalid. |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga6114e63ca23b82f9be0ac70e372b878b)spi\_transceive\_cb()

| | int spi\_transceive\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, | |  |  | [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d) | *callback*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Read/write the specified amount of data from the SPI driver.

Note
:   This function is asynchronous.
:   This function is available only if `CONFIG_SPI_ASYNC` is selected.
:   The chip select behavior as described by [spi\_transceive](#gad51054c1ba259db5a64619788506a6f5) and the function of controller/peripheral modes is the same.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | tx\_bufs | Buffer array where data to be sent originates from, or NULL if none. |
    | rx\_bufs | Buffer array where data to be read will be written to, or NULL if none. |
    | callback | Function pointer to completion callback. (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not). |
    | userdata | Userdata passed to callback |

Return values
:   | frames | Positive number of frames received in slave mode. |
    | --- | --- |
    | 0 | If successful in master mode. |
    | -ENOTSUP | means some part of the spi config is not supported either by the device hardware or the driver software. |
    | -EINVAL | means that some parameter of the [spi\_config](structspi__config.md "SPI controller configuration structure.") is invalid. |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga52c017066736414b31ff709ddc67c4ff)spi\_transceive\_dt()

| | int spi\_transceive\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Read/write data from an SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`.

This is equivalent to:

```
spi_transceive(spec->bus, &spec->config, tx_bufs, rx_bufs);
```

Parameters
:   | spec | SPI specification from devicetree |
    | --- | --- |
    | tx\_bufs | Buffer array where data to be sent originates from, or NULL if none. |
    | rx\_bufs | Buffer array where data to be read will be written to, or NULL if none. |

Returns
:   a value from [spi\_transceive()](#gad51054c1ba259db5a64619788506a6f5).

## [◆ ](#ga41b8a541257c0d45575fdc4593417edc)spi\_transceive\_signal()

| | int spi\_transceive\_signal | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Read/write the specified amount of data from the SPI driver.

Note
:   This function is asynchronous.
:   The chip select behavior as described by [spi\_transceive](#gad51054c1ba259db5a64619788506a6f5) and the function of controller/peripheral modes is the same.
:   This function is available only if `CONFIG_SPI_ASYNC` and `CONFIG_POLL` are selected.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | tx\_bufs | Buffer array where data to be sent originates from, or NULL if none. |
    | rx\_bufs | Buffer array where data to be read will be written to, or NULL if none. |
    | sig | A pointer to a valid and ready to be signaled struct [k\_poll\_signal](structk__poll__signal.md). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not). |

Return values
:   | frames | Positive number of frames received in slave mode. |
    | --- | --- |
    | 0 | If successful in master mode. |
    | -ENOTSUP | means some part of the spi config is not supported either by the device hardware or the driver software. |
    | -EINVAL | means that some parameter of the [spi\_config](structspi__config.md "SPI controller configuration structure.") is invalid. |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga7e7c4460670ec1c0433ba19accd97796)spi\_write()

| | int spi\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Write the specified amount of data from the SPI driver.

Note
:   This function is synchronous.
:   This function is a helper function calling spi\_transceive.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | tx\_bufs | Buffer array where data to be sent originates from. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | means some part of the spi config is not supported either by the device hardware or the driver software. |
    | -EINVAL | means that some parameter of the [spi\_config](structspi__config.md "SPI controller configuration structure.") is invalid. |
    | -errno | Negative errno code on failure. |

## [◆ ](#ga292d6d1fe82f3f1ce0d9a2aa5437201b)spi\_write\_dt()

| | int spi\_write\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Write data to a SPI bus specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`.

This is equivalent to:

```
spi_write(spec->bus, &spec->config, tx_bufs);
```

Parameters
:   | spec | SPI specification from devicetree |
    | --- | --- |
    | tx\_bufs | Buffer array where data to be sent originates from. |

Returns
:   a value from [spi\_write()](#ga7e7c4460670ec1c0433ba19accd97796).

## [◆ ](#gadcb19d43461ef88e31f6b382cc87fd0b)spi\_write\_signal()

| | int spi\_write\_signal | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>`

Write the specified amount of data from the SPI driver.

Note
:   This function is asynchronous.
:   This function is a helper function calling spi\_transceive\_signal.
:   This function is available only if `CONFIG_SPI_ASYNC` and `CONFIG_POLL` are selected.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | tx\_bufs | Buffer array where data to be sent originates from. |
    | sig | A pointer to a valid and ready to be signaled struct [k\_poll\_signal](structk__poll__signal.md). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not). |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | means some part of the spi config is not supported either by the device hardware or the driver software. |
    | -EINVAL | means that some parameter of the [spi\_config](structspi__config.md "SPI controller configuration structure.") is invalid. |
    | -errno | Negative errno code on failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
