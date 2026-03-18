---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__spi__interface.html
original_path: doxygen/html/group__spi__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
|  | SPI buffer array structure. [More...](structspi__buf__set.md#details) |
| struct | [spi\_driver\_api](structspi__driver__api.md) |
|  | SPI driver API This is the mandatory API any SPI driver needs to expose. [More...](structspi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)(spi\_dev) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin. |
| #define | [SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET](#ga88fefbfadb8184806123e1f935a4ff7c)(inst) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a SPI device's chip select pin. |
| #define | [SPI\_CS\_CONTROL\_INIT](#ga4a2bce02956d8121da7b6099f6c097b9)(node\_id, delay\_) |
|  | Initialize and get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node identifier. |
| #define | [SPI\_CS\_CONTROL\_INIT\_INST](#ga239bda66980ed0a349b7177100f7752c)(inst, delay\_) |
|  | Get a pointer to a `[spi_cs_control](structspi__cs__control.md "SPI Chip Select control structure.")` from a devicetree node. |
| #define | [SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)(node\_id, operation\_, delay\_) |
|  | Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree. |
| #define | [SPI\_CONFIG\_DT\_INST](#gadc1e7de7925603adfedbac35fdabc78a)(inst, operation\_, delay\_) |
|  | Structure initializer for [spi\_config](structspi__config.md "SPI controller configuration structure.") from devicetree instance. |
| #define | [SPI\_DT\_SPEC\_GET](#gaec6a8fde1c3ec6349a601a2d5f7af785)(node\_id, operation\_, delay\_) |
|  | Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree. |
| #define | [SPI\_DT\_SPEC\_INST\_GET](#ga91c595b7567af23b447c755d898608f3)(inst, operation\_, delay\_) |
|  | Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree instance. |
| #define | [SPI\_DEVICE\_DT\_DEFINE](#ga27af5f053c5fd4e9eef0900406fbf854)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
| #define | [SPI\_STATS\_RX\_BYTES\_INC](#ga83fa04d1e9f281cd566ee32cf807325e)(dev\_) |
| #define | [SPI\_STATS\_TX\_BYTES\_INC](#gadd3b82af2396b91930ece09fa79fc4e2)(dev\_) |
| #define | [SPI\_STATS\_TRANSFER\_ERROR\_INC](#ga6f69e68a79afbbe016aecc515f14de3a)(dev\_) |
| #define | [spi\_transceive\_stats](#gad7d1058f600d6aef4fc4e2bdff5d55f3)(dev, error, tx\_bufs, rx\_bufs) |
| #define | [SPI\_DT\_IODEV\_DEFINE](#ga1e9f5fe389d53c280639f23ea134e18c)(name, node\_id, operation\_, delay\_) |
|  | Define an iodev for a given dt node on the bus. |

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
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_is\_ready](#ga7d5fcb15e3a1082ea63203b185c6a207) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Validate that SPI bus is ready. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_is\_ready\_dt](#ga37b4e5079ed18b70b0c5a260f4c36403) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Validate that SPI bus (and CS gpio if defined) is ready. |
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
| static int | [spi\_transceive\_cb](#ga6114e63ca23b82f9be0ac70e372b878b) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d) callback, void \*userdata) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_transceive\_signal](#ga41b8a541257c0d45575fdc4593417edc) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Read/write the specified amount of data from the SPI driver. |
| static int | [spi\_transceive\_async](#gacc26ab19d1211508691691308744350f) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Alias for spi\_transceive\_signal for backwards compatibility. |
| static int | [spi\_read\_signal](#ga9a1ceadb217368232af5b688c12169c5) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Read the specified amount of data from the SPI driver. |
| static int | [spi\_read\_async](#ga5185c52f0c8e2e3419a16c6e24af55e1) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Alias for spi\_read\_signal for backwards compatibility. |
| static int | [spi\_write\_signal](#gadcb19d43461ef88e31f6b382cc87fd0b) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Write the specified amount of data from the SPI driver. |
| static int | [spi\_write\_async](#ga37d17fa9ae3909529762c43f9409d0f0) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Alias for spi\_write\_signal for backwards compatibility. |
| static void | [spi\_iodev\_submit](#ga8b23855bdc7dab7d02b8f7daa7db651b) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit a SPI device with a request. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_is\_ready\_iodev](#gafea78af1fe1fa49fdc5459ab3a2d5f73) (const struct [rtio\_iodev](structrtio__iodev.md) \*spi\_iodev) |
|  | Validate that SPI bus (and CS gpio if defined) is ready. |
| static int | [spi\_rtio\_copy](#ga812818433d437829fe6ab4fcff0ed38b) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [rtio\_sqe](structrtio__sqe.md) \*\*last\_sqe) |
|  | Copy the tx\_bufs and rx\_bufs into a set of RTIO requests. |
| int | [spi\_release](#ga0c4f4f0a93bb83a4f58d551a7491164e) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config) |
|  | Release the SPI device locked on and/or the CS by the current config. |
| static int | [spi\_release\_dt](#ga829b59767c51b20b546eee8a9cc84b69) (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec) |
|  | Release the SPI device specified in `[spi_dt_spec](structspi__dt__spec.md "Complete SPI DT information.")`. |

| Variables | |
| --- | --- |
| const struct [rtio\_iodev\_api](structrtio__iodev__api.md) | [spi\_iodev\_api](#gacd22d734b1b2729e09862065d44b8ce9) |

| SPI operational mode | |
| --- | --- |
| #define | [SPI\_OP\_MODE\_MASTER](#ga5b9d40fa0f455b1e63f8040b3316b0da)   0U |
|  | Master mode. |
| #define | [SPI\_OP\_MODE\_SLAVE](#ga1c3310d3711cb99cdb78fa9d1c970779)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Slave mode. |
| #define | [SPI\_OP\_MODE\_GET](#ga6dd4395e027407a7b3b92cff2abcc8b3)(\_operation\_) |
|  | Get SPI operational mode. |

| SPI Polarity & Phase Modes | |
| --- | --- |
| #define | [SPI\_MODE\_CPOL](#ga5a2be1003873beaa0ade10e7218d67d5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Clock Polarity: if set, clock idle state will be 1 and active state will be 0. |
| #define | [SPI\_MODE\_CPHA](#ga35e98b37e3ec4889a90100abe884590f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Clock Phase: this dictates when is the data captured, and depends clock's polarity. |
| #define | [SPI\_MODE\_LOOP](#ga8619b297de563eca6852af34c79daa62)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Whatever data is transmitted is looped-back to the receiving buffer of the controller. |
| #define | [SPI\_MODE\_GET](#gaa3582b96ff42dba0b0ad815c727d5e42)(\_mode\_) |
|  | Get SPI polarity and phase mode bits. |

| SPI Transfer modes (host controller dependent) | |
| --- | --- |
| #define | [SPI\_TRANSFER\_MSB](#ga7761f42c6241cf396fc02d0de8617e46)   (0U) |
|  | Most significant bit first. |
| #define | [SPI\_TRANSFER\_LSB](#ga93504a76a265bedbe781c107beebc9dc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Least significant bit first. |

| SPI word size | |
| --- | --- |
| #define | [SPI\_WORD\_SIZE\_GET](#ga7386c70bd669142bb7558526175765cc)(\_operation\_) |
|  | Get SPI word size. |
| #define | [SPI\_WORD\_SET](#gaaea60640bb9223bbaf94338d07d9d07c)(\_word\_size\_) |
|  | Set SPI word size. |

| Specific SPI devices control bits | |
| --- | --- |
| #define | [SPI\_HOLD\_ON\_CS](#gae917312adef283b4bf67cdb53566e4bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Requests - if possible - to keep CS asserted after the transaction. |
| #define | [SPI\_LOCK\_ON](#gafe8dc164d6fc0a0f93f2ff9d5381af14)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Keep the device locked after the transaction for the current config. |
| #define | [SPI\_CS\_ACTIVE\_HIGH](#ga44076fa14703997f7e3aefb2bfccd801)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Active high logic on CS. |

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

## Macro Definition Documentation

## [◆ ](#ga822af066ee0829aee405c034bb967463)SPI\_CONFIG\_DT

| #define SPI\_CONFIG\_DT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[spi.h](drivers_2spi_8h.md)>`

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

**Definition** devicetree.h:615

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2214

[SPI\_MODE\_CPHA](#ga35e98b37e3ec4889a90100abe884590f)

#define SPI\_MODE\_CPHA

Clock Phase: this dictates when is the data captured, and depends clock's polarity.

**Definition** spi.h:68

[SPI\_CS\_CONTROL\_INIT](#ga4a2bce02956d8121da7b6099f6c097b9)

#define SPI\_CS\_CONTROL\_INIT(node\_id, delay\_)

Initialize and get a pointer to a spi\_cs\_control from a devicetree node identifier.

**Definition** spi.h:264

[SPI\_MODE\_CPOL](#ga5a2be1003873beaa0ade10e7218d67d5)

#define SPI\_MODE\_CPOL

Clock Polarity: if set, clock idle state will be 1 and active state will be 0.

**Definition** spi.h:59

[SPI\_HOLD\_ON\_CS](#gae917312adef283b4bf67cdb53566e4bb)

#define SPI\_HOLD\_ON\_CS

Requests - if possible - to keep CS asserted after the transaction.

**Definition** spi.h:114

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

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), operation\_, delay\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)

#define SPI\_CONFIG\_DT(node\_id, operation\_, delay\_)

Structure initializer for spi\_config from devicetree.

**Definition** spi.h:345

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

`#include <[spi.h](drivers_2spi_8h.md)>`

Active high logic on CS.

Usually, and by default, CS logic is active low. However, some devices may require the reverse logic: active high. This bit will request the controller to use that logic. Note that not all controllers are able to handle that natively. In this case deferring the CS control to a gpio line through struct [spi\_cs\_control](structspi__cs__control.md "SPI Chip Select control structure.") would be the solution.

## [◆ ](#ga4a2bce02956d8121da7b6099f6c097b9)SPI\_CS\_CONTROL\_INIT

| #define SPI\_CS\_CONTROL\_INIT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *delay\_* ) |

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

{ \

.gpio = [SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)(node\_id), \

.delay = (delay\_), \

}

[SPI\_CS\_GPIOS\_DT\_SPEC\_GET](#ga48aa19f45413d56b03596d10b72c732e)

#define SPI\_CS\_GPIOS\_DT\_SPEC\_GET(spi\_dev)

Get a struct gpio\_dt\_spec for a SPI device's chip select pin.

**Definition** spi.h:210

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

**Definition** devicetree.h:198

[spi\_cs\_control](structspi__cs__control.md)

SPI Chip Select control structure.

**Definition** spi.h:157

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

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(spi\_dev), cs\_gpios, \

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(spi\_dev), {})

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3362

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value)

Like GPIO\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** gpio.h:353

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

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), init\_fn, pm, data, config, \

level, prio, api, \

&Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

\_\_VA\_ARGS\_\_)

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:149

## [◆ ](#ga1e9f5fe389d53c280639f23ea134e18c)SPI\_DT\_IODEV\_DEFINE

| #define SPI\_DT\_IODEV\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id*, |
|  |  |  | *operation\_*, |
|  |  |  | *delay\_* ) |

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

const struct [spi\_dt\_spec](structspi__dt__spec.md) \_spi\_dt\_spec\_##name = \

SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_); \

RTIO\_IODEV\_DEFINE(name, &[spi\_iodev\_api](#gacd22d734b1b2729e09862065d44b8ce9), (void \*)&\_spi\_dt\_spec\_##name)

[spi\_iodev\_api](#gacd22d734b1b2729e09862065d44b8ce9)

const struct rtio\_iodev\_api spi\_iodev\_api

[spi\_dt\_spec](structspi__dt__spec.md)

Complete SPI DT information.

**Definition** spi.h:375

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

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

{ \

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.config = [SPI\_CONFIG\_DT](#ga822af066ee0829aee405c034bb967463)(node\_id, operation\_, delay\_) \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

Structure initializer for [spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") from devicetree.

This helper macro expands to a static initializer for a struct
[spi\_dt\_spec](structspi__dt__spec.md "Complete SPI DT information.") by reading the relevant bus, frequency, slave, and cs data from the devicetree.

Important: multiple fields are automatically constructed by this macro which must be checked before use. [spi\_is\_ready](#ga7d5fcb15e3a1082ea63203b185c6a207) performs the required [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb "device_is_ready") checks.

**[Deprecated](deprecated.md#_deprecated000004)**
:   Use [spi\_is\_ready\_dt](#ga37b4e5079ed18b70b0c5a260f4c36403) instead.

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

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

[SPI\_DT\_SPEC\_GET](#gaec6a8fde1c3ec6349a601a2d5f7af785)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), operation\_, delay\_)

[SPI\_DT\_SPEC\_GET](#gaec6a8fde1c3ec6349a601a2d5f7af785)

#define SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_)

Structure initializer for spi\_dt\_spec from devicetree.

**Definition** spi.h:400

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

`#include <[spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#ga22801357a9682371e3d8a10e522de388)SPI\_FRAME\_FORMAT\_TI

| #define SPI\_FRAME\_FORMAT\_TI   (1U << 15) |
| --- |

`#include <[spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#ga5585d5e81dec606b605f31b6745c35d3)SPI\_FULL\_DUPLEX

| #define SPI\_FULL\_DUPLEX   (0U << 11) |
| --- |

`#include <[spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#ga602a7804b7434d7ebc1ebe6cb9b47a2f)SPI\_HALF\_DUPLEX

| #define SPI\_HALF\_DUPLEX   (1U << 11) |
| --- |

`#include <[spi.h](dt-bindings_2spi_2spi_8h.md)>`

## [◆ ](#gae917312adef283b4bf67cdb53566e4bb)SPI\_HOLD\_ON\_CS

| #define SPI\_HOLD\_ON\_CS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Requests - if possible - to keep CS asserted after the transaction.

## [◆ ](#ga120ab60329d664d5d6e828f90251a98a)SPI\_LINES\_DUAL

| #define SPI\_LINES\_DUAL   (1U << 16) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Dual lines.

## [◆ ](#gadc79f986c4b30fe5b263841cd8bb5676)SPI\_LINES\_MASK

| #define SPI\_LINES\_MASK   (0x3U << 16) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Mask for MISO lines in [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a).

## [◆ ](#ga512d76085e600886654b8541aab31cf7)SPI\_LINES\_OCTAL

| #define SPI\_LINES\_OCTAL   (3U << 16) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Octal lines.

## [◆ ](#ga30866b948e995224de854e10a428bda5)SPI\_LINES\_QUAD

| #define SPI\_LINES\_QUAD   (2U << 16) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Quad lines.

## [◆ ](#ga7a183f157e8cb8b437857a0babbd923b)SPI\_LINES\_SINGLE

| #define SPI\_LINES\_SINGLE   (0U << 16) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Single line.

## [◆ ](#gafe8dc164d6fc0a0f93f2ff9d5381af14)SPI\_LOCK\_ON

| #define SPI\_LOCK\_ON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Keep the device locked after the transaction for the current config.

Use this with extreme caution (see [spi\_release()](#ga0c4f4f0a93bb83a4f58d551a7491164e) below) as it will prevent other callers to access the SPI device until [spi\_release()](#ga0c4f4f0a93bb83a4f58d551a7491164e) is properly called.

## [◆ ](#ga35e98b37e3ec4889a90100abe884590f)SPI\_MODE\_CPHA

| #define SPI\_MODE\_CPHA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Clock Phase: this dictates when is the data captured, and depends clock's polarity.

When SPI\_MODE\_CPOL is set and this bit as well, capture will occur on low to high transition and high to low if this bit is not set (default). This is fully reversed if CPOL is not set.

## [◆ ](#ga5a2be1003873beaa0ade10e7218d67d5)SPI\_MODE\_CPOL

| #define SPI\_MODE\_CPOL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Clock Polarity: if set, clock idle state will be 1 and active state will be 0.

If untouched, the inverse will be true which is the default.

## [◆ ](#gaa3582b96ff42dba0b0ad815c727d5e42)SPI\_MODE\_GET

| #define SPI\_MODE\_GET | ( |  | *\_mode\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

((\_mode\_) & SPI\_MODE\_MASK)

Get SPI polarity and phase mode bits.

## [◆ ](#ga8619b297de563eca6852af34c79daa62)SPI\_MODE\_LOOP

| #define SPI\_MODE\_LOOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Whatever data is transmitted is looped-back to the receiving buffer of the controller.

This is fully controller dependent as some may not support this, and can be used for testing purposes only.

## [◆ ](#ga6dd4395e027407a7b3b92cff2abcc8b3)SPI\_OP\_MODE\_GET

| #define SPI\_OP\_MODE\_GET | ( |  | *\_operation\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

((\_operation\_) & SPI\_OP\_MODE\_MASK)

Get SPI operational mode.

## [◆ ](#ga5b9d40fa0f455b1e63f8040b3316b0da)SPI\_OP\_MODE\_MASTER

| #define SPI\_OP\_MODE\_MASTER   0U |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Master mode.

## [◆ ](#ga1c3310d3711cb99cdb78fa9d1c970779)SPI\_OP\_MODE\_SLAVE

| #define SPI\_OP\_MODE\_SLAVE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Slave mode.

## [◆ ](#ga83fa04d1e9f281cd566ee32cf807325e)SPI\_STATS\_RX\_BYTES\_INC

| #define SPI\_STATS\_RX\_BYTES\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

## [◆ ](#ga6f69e68a79afbbe016aecc515f14de3a)SPI\_STATS\_TRANSFER\_ERROR\_INC

| #define SPI\_STATS\_TRANSFER\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

## [◆ ](#gadd3b82af2396b91930ece09fa79fc4e2)SPI\_STATS\_TX\_BYTES\_INC

| #define SPI\_STATS\_TX\_BYTES\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

## [◆ ](#gad7d1058f600d6aef4fc4e2bdff5d55f3)spi\_transceive\_stats

| #define spi\_transceive\_stats | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *error*, |
|  |  |  | *tx\_bufs*, |
|  |  |  | *rx\_bufs* ) |

`#include <[spi.h](drivers_2spi_8h.md)>`

## [◆ ](#ga93504a76a265bedbe781c107beebc9dc)SPI\_TRANSFER\_LSB

| #define SPI\_TRANSFER\_LSB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Least significant bit first.

## [◆ ](#ga7761f42c6241cf396fc02d0de8617e46)SPI\_TRANSFER\_MSB

| #define SPI\_TRANSFER\_MSB   (0U) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Most significant bit first.

## [◆ ](#gaaea60640bb9223bbaf94338d07d9d07c)SPI\_WORD\_SET

| #define SPI\_WORD\_SET | ( |  | *\_word\_size\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

((\_word\_size\_) << SPI\_WORD\_SIZE\_SHIFT)

Set SPI word size.

## [◆ ](#ga7386c70bd669142bb7558526175765cc)SPI\_WORD\_SIZE\_GET

| #define SPI\_WORD\_SIZE\_GET | ( |  | *\_operation\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

**Value:**

(((\_operation\_) & SPI\_WORD\_SIZE\_MASK) >> SPI\_WORD\_SIZE\_SHIFT)

Get SPI word size.

## Typedef Documentation

## [◆ ](#ga3fc669f866b03cfdad98754de69cda13)spi\_api\_io

| typedef int(\* spi\_api\_io) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Callback API for I/O See [spi\_transceive()](#gad51054c1ba259db5a64619788506a6f5) for argument descriptions.

Callback API for asynchronous I/O See [spi\_transceive\_async()](#gacc26ab19d1211508691691308744350f) for argument descriptions.

## [◆ ](#ga03be7f33032ac479153616bbe26848e7)spi\_api\_io\_async

| typedef int(\* spi\_api\_io\_async) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d) cb, void \*userdata) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

## [◆ ](#gac651ff7cd3dde7abe2525e20ef2e9e7d)spi\_api\_release

| typedef int(\* spi\_api\_release) (const struct [device](structdevice.md) \*dev, const struct [spi\_config](structspi__config.md) \*config) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Callback API for unlocking SPI device.

See [spi\_release()](#ga0c4f4f0a93bb83a4f58d551a7491164e) for argument descriptions

## [◆ ](#ga1db2a410f482d0f26c49f96352aa606d)spi\_callback\_t

| typedef void(\* spi\_callback\_t) (const struct [device](structdevice.md) \*dev, int result, void \*data) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

SPI callback for asynchronous transfer requests.

Parameters
:   | dev | SPI device which is notifying of transfer completion or error |
    | --- | --- |
    | result | Result code of the transfer request. 0 is success, -errno for failure. |
    | data | Transfer requester supplied data which is passed along to the callback. |

## [◆ ](#ga398a8ae1c4799e77fb6c067b6d47294a)spi\_operation\_t

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [spi\_operation\_t](#ga398a8ae1c4799e77fb6c067b6d47294a) |
| --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Opaque type to hold the SPI operation flags.

## Function Documentation

## [◆ ](#gae1156a4ee1b5909c321811045566d888)spi\_cs\_is\_gpio()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_cs\_is\_gpio | ( | const struct [spi\_config](structspi__config.md) \* | *config* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

Submit a SPI device with a request.

Parameters
:   | iodev\_sqe | Prepared submissions queue entry connected to an iodev defined by SPI\_IODEV\_DEFINE. Must live as long as the request is in flight. |
    | --- | --- |

## [◆ ](#ga7d5fcb15e3a1082ea63203b185c6a207)spi\_is\_ready()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_is\_ready | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Validate that SPI bus is ready.

Parameters
:   | spec | SPI specification from devicetree |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the SPI bus is ready for use. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the SPI bus is not ready for use. |

## [◆ ](#ga37b4e5079ed18b70b0c5a260f4c36403)spi\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_is\_ready\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

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
    | -errno | Negative errno code on failure. |

## [◆ ](#ga5185c52f0c8e2e3419a16c6e24af55e1)spi\_read\_async()

| | int spi\_read\_async | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Alias for spi\_read\_signal for backwards compatibility.

**[Deprecated](deprecated.md#_deprecated000006)**
:   Use [spi\_read\_signal](#ga9a1ceadb217368232af5b688c12169c5) instead.

## [◆ ](#ga7a1d7ebd37d2861b169c265cb90015bf)spi\_read\_dt()

| | int spi\_read\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

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
    | -errno | Negative errno code on failure. |

## [◆ ](#ga0c4f4f0a93bb83a4f58d551a7491164e)spi\_release()

| int spi\_release | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [spi\_config](structspi__config.md) \* | *config* ) |

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

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

## [◆ ](#ga812818433d437829fe6ab4fcff0ed38b)spi\_rtio\_copy()

| | int spi\_rtio\_copy | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, | |  |  | struct [rtio\_sqe](structrtio__sqe.md) \*\* | *last\_sqe* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Copy the tx\_bufs and rx\_bufs into a set of RTIO requests.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | rtio context |
    | --- | --- | --- |
    | [in] | iodev | iodev to transceive with |
    | [in] | tx\_bufs | transmit buffer set |
    | [in] | rx\_bufs | receive buffer set |
    | [out] | last\_sqe | last sqe submitted, NULL if not enough memory |

Return values
:   | Number | of submission queue entries |
    | --- | --- |
    | -ENOMEM | out of memory |

## [◆ ](#gad51054c1ba259db5a64619788506a6f5)spi\_transceive()

| int spi\_transceive | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [spi\_config](structspi__config.md) \* | *config*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) |

`#include <[spi.h](drivers_2spi_8h.md)>`

Read/write the specified amount of data from the SPI driver.

Note
:   This function is synchronous.

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
    | -errno | Negative errno code on failure. |

## [◆ ](#gacc26ab19d1211508691691308744350f)spi\_transceive\_async()

| | int spi\_transceive\_async | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Alias for spi\_transceive\_signal for backwards compatibility.

**[Deprecated](deprecated.md#_deprecated000005)**
:   Use [spi\_transceive\_signal](#ga41b8a541257c0d45575fdc4593417edc) instead.

## [◆ ](#ga6114e63ca23b82f9be0ac70e372b878b)spi\_transceive\_cb()

| | int spi\_transceive\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, | |  |  | [spi\_callback\_t](#ga1db2a410f482d0f26c49f96352aa606d) | *callback*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Read/write the specified amount of data from the SPI driver.

Note
:   This function is asynchronous.
:   This function is available only if `CONFIG_SPI_ASYNC` is selected.

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
    | -errno | Negative errno code on failure. |

## [◆ ](#ga52c017066736414b31ff709ddc67c4ff)spi\_transceive\_dt()

| | int spi\_transceive\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

Read/write the specified amount of data from the SPI driver.

Note
:   This function is asynchronous.
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
    | -errno | Negative errno code on failure. |

## [◆ ](#ga7e7c4460670ec1c0433ba19accd97796)spi\_write()

| | int spi\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

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
    | -errno | Negative errno code on failure. |

## [◆ ](#ga37d17fa9ae3909529762c43f9409d0f0)spi\_write\_async()

| | int spi\_write\_async | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [spi\_config](structspi__config.md) \* | *config*, | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

Alias for spi\_write\_signal for backwards compatibility.

**[Deprecated](deprecated.md#_deprecated000007)**
:   Use [spi\_write\_signal](#gadcb19d43461ef88e31f6b382cc87fd0b) instead.

## [◆ ](#ga292d6d1fe82f3f1ce0d9a2aa5437201b)spi\_write\_dt()

| | int spi\_write\_dt | ( | const struct [spi\_dt\_spec](structspi__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

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

`#include <[spi.h](drivers_2spi_8h.md)>`

Write the specified amount of data from the SPI driver.

Note
:   This function is asynchronous.
:   This function is a helper function calling spi\_transceive\_async.
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
    | -errno | Negative errno code on failure. |

## Variable Documentation

## [◆ ](#gacd22d734b1b2729e09862065d44b8ce9)spi\_iodev\_api

| | const struct [rtio\_iodev\_api](structrtio__iodev__api.md) spi\_iodev\_api | | --- | | extern |
| --- | --- | --- |

`#include <[spi.h](drivers_2spi_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
