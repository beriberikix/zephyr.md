---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__i3c__interface.html
original_path: doxygen/html/group__i3c__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C Interface

[Device Driver APIs](group__io__interfaces.md)

I3C Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [I3C Address-related Helper Code](group__i3c__addresses.md) |
|  | I3C Address-related Helper Code. |
|  | [I3C Common Command Codes](group__i3c__ccc.md) |
|  | I3C Common Command Codes. |
|  | [I3C Devicetree related bits](group__i3c__devicetree.md) |
|  | I3C Devicetree related bits. |
|  | [I3C HDR DDR API](group__i3c__hdr__ddr.md) |
|  | I3C HDR DDR API. |
|  | [I3C In-Band Interrupts](group__i3c__ibi.md) |
|  | I3C In-Band Interrupts. |
|  | [I3C Target Device API](group__i3c__target__device.md) |
|  | I3C Target Device API. |
|  | [I3C Transfer API](group__i3c__transfer__api.md) |
|  | I3C Transfer API. |

| Data Structures | |
| --- | --- |
| struct | [i3c\_config\_controller](structi3c__config__controller.md) |
|  | Configuration parameters for I3C hardware to act as controller. [More...](structi3c__config__controller.md#details) |
| struct | [i3c\_config\_custom](structi3c__config__custom.md) |
|  | Custom I3C configuration parameters. [More...](structi3c__config__custom.md#details) |
| struct | [i3c\_device\_id](structi3c__device__id.md) |
|  | Structure used for matching I3C devices. [More...](structi3c__device__id.md#details) |
| struct | [i3c\_device\_desc](structi3c__device__desc.md) |
|  | Structure describing a I3C target device. [More...](structi3c__device__desc.md#details) |
| struct | [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) |
|  | Structure describing a I2C device on I3C bus. [More...](structi3c__i2c__device__desc.md#details) |
| struct | [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) |
|  | Structure for describing attached devices for a controller. [More...](structi3c__dev__attached__list.md#details) |
| struct | [i3c\_dev\_list](structi3c__dev__list.md) |
|  | Structure for describing known devices for a controller. [More...](structi3c__dev__list.md#details) |
| struct | [i3c\_driver\_config](structi3c__driver__config.md) |
|  | This structure is common to all I3C drivers and is expected to be the first element in the object pointed to by the config field in the device structure. [More...](structi3c__driver__config.md#details) |
| struct | [i3c\_driver\_data](structi3c__driver__data.md) |
|  | This structure is common to all I3C drivers and is expected to be the first element in the driver's struct driver\_data declaration. [More...](structi3c__driver__data.md#details) |
| struct | [i3c\_iodev\_data](structi3c__iodev__data.md) |

| Macros | |
| --- | --- |
| #define | [I3C\_DEVICE\_ID](#gaed0df9802cc9b268abcfe4e877ebf498)(pid) |
|  | Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from PID. |
| #define | [I3C\_BUS\_FOR\_EACH\_I3CDEV](#ga42cb4edf6a099d586df14456fd98c873)(bus, desc) |
|  | iterate over all I3C devices present on the bus |
| #define | [I3C\_BUS\_FOR\_EACH\_I2CDEV](#ga450ba9021d1080f890c32624f20ba2b8)(bus, desc) |
|  | iterate over all I2C devices present on the bus |
| #define | [I3C\_DT\_IODEV\_DEFINE](#gabec5796b92d4582761bc3de456f1df27)(name, node\_id) |
|  | Define an iodev for a given dt node on the bus. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_bus\_mode](#ga7a0d66ab45f618ca055422e2b69abe90) {     [I3C\_BUS\_MODE\_PURE](#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445) , [I3C\_BUS\_MODE\_MIXED\_FAST](#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434) , [I3C\_BUS\_MODE\_MIXED\_LIMITED](#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722) , [I3C\_BUS\_MODE\_MIXED\_SLOW](#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a) ,     [I3C\_BUS\_MODE\_MAX](#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) = I3C\_BUS\_MODE\_MIXED\_SLOW , [I3C\_BUS\_MODE\_INVALID](#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c)   } |
|  | I3C bus mode. [More...](#ga7a0d66ab45f618ca055422e2b69abe90) |
| enum | [i3c\_i2c\_speed\_type](#ga67686f0a5d83697361c655c3fd6e61c6) { [I3C\_I2C\_SPEED\_FM](#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1) , [I3C\_I2C\_SPEED\_FMPLUS](#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea) , [I3C\_I2C\_SPEED\_MAX](#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) = I3C\_I2C\_SPEED\_FMPLUS , [I3C\_I2C\_SPEED\_INVALID](#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4) } |
|  | I2C bus speed under I3C bus. [More...](#ga67686f0a5d83697361c655c3fd6e61c6) |
| enum | [i3c\_data\_rate](#gae9d98642c6f249ee0e6ea0dc491b5073) {     [I3C\_DATA\_RATE\_SDR](#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9) , [I3C\_DATA\_RATE\_HDR\_DDR](#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301) , [I3C\_DATA\_RATE\_HDR\_TSL](#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590) , [I3C\_DATA\_RATE\_HDR\_TSP](#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d) ,     [I3C\_DATA\_RATE\_HDR\_BT](#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed) , [I3C\_DATA\_RATE\_MAX](#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) = I3C\_DATA\_RATE\_HDR\_BT , [I3C\_DATA\_RATE\_INVALID](#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a)   } |
|  | I3C data rate. [More...](#gae9d98642c6f249ee0e6ea0dc491b5073) |
| enum | [i3c\_config\_type](#ga5b111bc8fa8c3bee052e621d26dcc54a) { [I3C\_CONFIG\_CONTROLLER](#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5) , [I3C\_CONFIG\_TARGET](#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00) , [I3C\_CONFIG\_CUSTOM](#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017) } |
|  | Type of configuration being passed to configure function. [More...](#ga5b111bc8fa8c3bee052e621d26dcc54a) |

| Functions | |
| --- | --- |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_dev\_list\_find](#ga9a451379bef381c6a264a22a2282fa89) (const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list, const struct [i3c\_device\_id](structi3c__device__id.md) \*id) |
|  | Find a I3C target device descriptor by ID. |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_dev\_list\_i3c\_addr\_find](#ga0e83c5a26b18acfbe7d532825a8fd54c) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Find a I3C target device descriptor by dynamic address. |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_dev\_list\_i3c\_static\_addr\_find](#gaecbb16ce8edcd9ad7a7afcfb1251aa76) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Find a I3C target device descriptor by static address. |
| struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* | [i3c\_dev\_list\_i2c\_addr\_find](#gafac78dca571ff7daa34fca0cfa7cc3b1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Find a I2C target device descriptor by address. |
| int | [i3c\_dev\_list\_daa\_addr\_helper](#ga3a4dac6aa35249e6e277da8075b596a8) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pid, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) must\_match, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) assigned\_okay, struct [i3c\_device\_desc](structi3c__device__desc.md) \*\*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr) |
|  | Helper function to find a usable address during ENTDAA. |
| static int | [i3c\_configure](#ga2f176f8440d86f4ec6c94a8911a75352) (const struct [device](structdevice.md) \*dev, enum [i3c\_config\_type](#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config) |
|  | Configure the I3C hardware. |
| static int | [i3c\_config\_get](#ga807877923755aeb5a065e054fb42946d) (const struct [device](structdevice.md) \*dev, enum [i3c\_config\_type](#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config) |
|  | Get configuration of the I3C hardware. |
| static int | [i3c\_recover\_bus](#ga7b23e08b10a09bde4e87328d6915aa25) (const struct [device](structdevice.md) \*dev) |
|  | Attempt bus recovery on the I3C bus. |
| int | [i3c\_attach\_i3c\_device](#ga042d1a3315f040562534ce08306b329c) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Attach an I3C device. |
| int | [i3c\_reattach\_i3c\_device](#gae6c8e8612368808117f4fce960e43769) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr) |
|  | Reattach I3C device. |
| int | [i3c\_detach\_i3c\_device](#ga6db9688cc7e9d34404717ae753751579) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Detach I3C Device. |
| int | [i3c\_attach\_i2c\_device](#ga5e69aaed50f99418c7123f652555ae20) (struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target) |
|  | Attach an I2C device. |
| int | [i3c\_detach\_i2c\_device](#ga8e8de45499bff02cac4c59c1758ec0a7) (struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target) |
|  | Detach I2C Device. |
| static int | [i3c\_do\_daa](#gabb54c0e85d0f5e8585391f9e5c20d4b6) (const struct [device](structdevice.md) \*dev) |
|  | Perform Dynamic Address Assignment on the I3C bus. |
| int | [i3c\_do\_ccc](#gaa6d5445489bfc8611c98b93f49305862) (const struct [device](structdevice.md) \*dev, struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload) |
|  | Send CCC to the bus. |
| static struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_device\_find](#ga10a3963b749cc667a03975889d618d1b) (const struct [device](structdevice.md) \*dev, const struct [i3c\_device\_id](structi3c__device__id.md) \*id) |
|  | Find a registered I3C target device. |
| int | [i3c\_bus\_init](#ga9af9191a5ab2e5e2ea0478520721171d) (const struct [device](structdevice.md) \*dev, const struct [i3c\_dev\_list](structi3c__dev__list.md) \*[i3c\_dev\_list](structi3c__dev__list.md)) |
|  | Generic helper function to perform bus initialization. |
| int | [i3c\_device\_basic\_info\_get](#gaac5d10b8f42a6a069e0ac15cc7263db8) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Get basic information from device and update device descriptor. |
| int | [i3c\_device\_adv\_info\_get](#ga4e4a7e9408bd2f43602367bc9fe4f81e) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Get advanced information from device and update device descriptor. |
| static int | [i3c\_device\_info\_get](#ga39a760d8ba759f9443689fc954eb3d4b) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Get all information from device and update device descriptor. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_bus\_has\_sec\_controller](#ga149d70b1c2e02e19782aa21a94b13684) (const struct [device](structdevice.md) \*dev) |
|  | Check if the bus has a secondary controller. |
| int | [i3c\_bus\_deftgts](#ga554e0c4fa3e6855f431521ae42313216) (const struct [device](structdevice.md) \*dev) |
|  | Send the CCC DEFTGTS. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [i3c\_odd\_parity](#gaaf7736a8895de826f7fac1a9ecf0d7ea) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) p) |
|  | Calculate odd parity. |
| int | [i3c\_device\_controller\_handoff](#ga22857e3c19dbd5d93f3aed120fa32c84) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) requested) |
|  | Perform Controller Handoff. |
| static struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_device\_desc\_alloc](#ga0432131f4bdd02867cd4139dd04c30e2) (void) |
| static void | [i3c\_device\_desc\_free](#ga473dd9ba2f10b74443b849ad110a4129) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_device\_desc\_in\_pool](#ga214dddc181748b2edd4f5aedd92e60cf) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc) |
| static struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* | [i3c\_i2c\_device\_desc\_alloc](#ga353db1ca445310c3ce6df61ed53c4bc9) (void) |
| static void | [i3c\_i2c\_device\_desc\_free](#gaf7d635d3be9821fbd00cf8ef7b0ca510) (struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*desc) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_i2c\_device\_desc\_in\_pool](#ga08398aae55aa7f06a18d7f2e5e37bc98) (struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*desc) |
| void | [i3c\_iodev\_submit\_fallback](#ga909d531941cd81850f4a05c51646690d) (const struct [device](structdevice.md) \*dev, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Fallback submit implementation. |
| static void | [i3c\_iodev\_submit](#ga3b612267e71202094fb4adab64ffd61c) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit request(s) to an I3C device with RTIO. |
| struct [rtio\_sqe](structrtio__sqe.md) \* | [i3c\_rtio\_copy](#gab46a231442a7bf60e7e28ca2f52d25fc) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Copy the i3c\_msgs into a set of RTIO requests. |

| Variables | |
| --- | --- |
| const struct [rtio\_iodev\_api](structrtio__iodev__api.md) | [i3c\_iodev\_api](#gace1f8f10af2d87bb5a17441645030833) |

| Bus Characteristic Register (BCR) | |
| --- | --- |
| - BCR[7:6]: Device Role   - 0: I3C Target   - 1: I3C Controller capable   - 2: Reserved   - 3: Reserved - BCR[5]: Advanced Capabilities   - 0: Does not support optional advanced capabilities.   - 1: Supports optional advanced capabilities which can be viewed via GETCAPS CCC. - BCR[4]: Virtual Target Support   - 0: Is not a virtual target.   - 1: Is a virtual target. - BCR[3]: Offline Capable   - 0: Will always response to I3C commands.   - 1: Will not always response to I3C commands. - BCR[2]: IBI Payload   - 0: No data bytes following the accepted IBI.   - 1: One data byte (MDB, Mandatory Data Byte) follows the accepted IBI. Additional data bytes may also follows. - BCR[1]: IBI Request Capable   - 0: Not capable   - 1: Capable - BCR[0]: Max Data Speed Limitation   - 0: No Limitation   - 1: Limitation obtained via GETMXDS CCC. | |
| #define | [I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT](#ga91ebe41a421dc05ae7f1de1ce2dd314f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Max Data Speed Limitation bit. |
| #define | [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](#ga0c09de8a18ea1586e37d35e073ae641f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | IBI Request Capable bit. |
| #define | [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](#gae119c230097cb8e1eab9fc45cafde838)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | IBI Payload bit. |
| #define | [I3C\_BCR\_OFFLINE\_CAPABLE](#ga7b9fea89457022d8012ac25133bf63db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Offline Capable bit. |
| #define | [I3C\_BCR\_VIRTUAL\_TARGET](#ga69dc4a5004da568684a3c72046bba870)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Virtual Target Support bit. |
| #define | [I3C\_BCR\_ADV\_CAPABILITIES](#ga07018705794753d0d0d65131f011e097)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Advanced Capabilities bit. |
| #define | [I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET](#ga867b4b12b23c803b86b57dcc86b9e604)   0U |
|  | Device Role - I3C Target. |
| #define | [I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE](#ga0e64c8aa6717b96bcf9dad6c9ec7f852)   1U |
|  | Device Role - I3C Controller Capable. |
| #define | [I3C\_BCR\_DEVICE\_ROLE\_MASK](#ga25721c9963040c84b7f5bbb48bb87b44)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7U, 6U) |
|  | Device Role bit shift mask. |
| #define | [I3C\_BCR\_DEVICE\_ROLE](#ga90988b26dc2f388ec7c65387a24f05af)(bcr) |
|  | Device Role. |

| Legacy Virtual Register (LVR) | |
| --- | --- |
| Legacy Virtual Register (LVR)   - LVR[7:5]: I2C device index:   - 0: I2C device has a 50 ns spike filter where it is not affected by high frequency on SCL.   - 1: I2C device does not have a 50 ns spike filter but can work with high frequency on SCL.   - 2: I2C device does not have a 50 ns spike filter and cannot work with high frequency on SCL. - LVR[4]: I2C mode indicator:   - 0: FM+ mode   - 1: FM mode - LVR[3:0]: Reserved. | |
| #define | [I3C\_LVR\_I2C\_FM\_PLUS\_MODE](#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)   0 |
|  | I2C FM+ Mode. |
| #define | [I3C\_LVR\_I2C\_FM\_MODE](#ga053945f5f67ee3c681de2c9362e69c39)   1 |
|  | I2C FM Mode. |
| #define | [I3C\_LVR\_I2C\_MODE\_MASK](#gaf073cc9ea1a68c57663c36de12554876)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | I2C Mode Indicator bitmask. |
| #define | [I3C\_LVR\_I2C\_MODE](#gaaf759805bb5824a89612b292a4439982)(lvr) |
|  | I2C Mode. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_0](#ga4319835ddb6b5984b21f5a5a2f14ae75)   0 |
|  | I2C Device Index 0. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_1](#ga02a21af4c679a81b8290beea30c8ef40)   1 |
|  | I2C Device Index 1. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_2](#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)   2 |
|  | I2C Device Index 2. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_MASK](#ga50fa249b36b91d56e49004548a1c7520)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7U, 5U) |
|  | I2C Device Index bitmask. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX](#gae7afa509b1d63374c551bcdaf84c5dd1)(lvr) |
|  | I2C Device Index. |

## Detailed Description

I3C Interface.

Since
:   3.2

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga07018705794753d0d0d65131f011e097)I3C\_BCR\_ADV\_CAPABILITIES

| #define I3C\_BCR\_ADV\_CAPABILITIES   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Advanced Capabilities bit.

0 - Does not support optional advanced capabilities. 1 - Supports optional advanced capabilities which can be viewed via GETCAPS CCC.

## [◆ ](#ga90988b26dc2f388ec7c65387a24f05af)I3C\_BCR\_DEVICE\_ROLE

| #define I3C\_BCR\_DEVICE\_ROLE | ( |  | *bcr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([I3C\_BCR\_DEVICE\_ROLE\_MASK](#ga25721c9963040c84b7f5bbb48bb87b44), (bcr))

[I3C\_BCR\_DEVICE\_ROLE\_MASK](#ga25721c9963040c84b7f5bbb48bb87b44)

#define I3C\_BCR\_DEVICE\_ROLE\_MASK

Device Role bit shift mask.

**Definition** i3c.h:132

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)

#define FIELD\_GET(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:14

Device Role.

Obtain Device Role value from the BCR value obtained via GETBCR.

Parameters
:   | bcr | BCR value |
    | --- | --- |

## [◆ ](#ga0e64c8aa6717b96bcf9dad6c9ec7f852)I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE

| #define I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE   1U |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Device Role - I3C Controller Capable.

## [◆ ](#ga867b4b12b23c803b86b57dcc86b9e604)I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET

| #define I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET   0U |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Device Role - I3C Target.

## [◆ ](#ga25721c9963040c84b7f5bbb48bb87b44)I3C\_BCR\_DEVICE\_ROLE\_MASK

| #define I3C\_BCR\_DEVICE\_ROLE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7U, 6U) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Device Role bit shift mask.

## [◆ ](#gae119c230097cb8e1eab9fc45cafde838)I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE

| #define I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

IBI Payload bit.

0 - No data bytes following the accepted IBI. 1 - One data byte (MDB, Mandatory Data Byte) follows the accepted IBI. Additional data bytes may also follows.

## [◆ ](#ga0c09de8a18ea1586e37d35e073ae641f)I3C\_BCR\_IBI\_REQUEST\_CAPABLE

| #define I3C\_BCR\_IBI\_REQUEST\_CAPABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

IBI Request Capable bit.

## [◆ ](#ga91ebe41a421dc05ae7f1de1ce2dd314f)I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT

| #define I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Max Data Speed Limitation bit.

0 - No Limitation. 1 - Limitation obtained via GETMXDS CCC.

## [◆ ](#ga7b9fea89457022d8012ac25133bf63db)I3C\_BCR\_OFFLINE\_CAPABLE

| #define I3C\_BCR\_OFFLINE\_CAPABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Offline Capable bit.

0 - Will always respond to I3C commands. 1 - Will not always respond to I3C commands.

## [◆ ](#ga69dc4a5004da568684a3c72046bba870)I3C\_BCR\_VIRTUAL\_TARGET

| #define I3C\_BCR\_VIRTUAL\_TARGET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Virtual Target Support bit.

0 - Is not a virtual target. 1 - Is a virtual target.

## [◆ ](#ga450ba9021d1080f890c32624f20ba2b8)I3C\_BUS\_FOR\_EACH\_I2CDEV

| #define I3C\_BUS\_FOR\_EACH\_I2CDEV | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *desc* ) |

`#include <[i3c.h](i3c_8h.md)>`

**Value:**

[SYS\_SLIST\_FOR\_EACH\_CONTAINER](group__single-linked-list__apis.md#gacd97d2f1044c0560d96c9f9a6f26d2f6)( \

&((struct [i3c\_driver\_data](structi3c__driver__data.md) \*)(bus->data))->attached\_dev.devices.i2c, desc, node)

[SYS\_SLIST\_FOR\_EACH\_CONTAINER](group__single-linked-list__apis.md#gacd97d2f1044c0560d96c9f9a6f26d2f6)

#define SYS\_SLIST\_FOR\_EACH\_CONTAINER(\_\_sl, \_\_cn, \_\_n)

Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn s...

**Definition** slist.h:165

[i3c\_driver\_data](structi3c__driver__data.md)

This structure is common to all I3C drivers and is expected to be the first element in the driver's s...

**Definition** i3c.h:1200

iterate over all I2C devices present on the bus

Parameters
:   | bus | the I3C bus device pointer |
    | --- | --- |
    | desc | an I2C device descriptor pointer updated to point to the current slot at each iteration of the loop |

## [◆ ](#ga42cb4edf6a099d586df14456fd98c873)I3C\_BUS\_FOR\_EACH\_I3CDEV

| #define I3C\_BUS\_FOR\_EACH\_I3CDEV | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *desc* ) |

`#include <[i3c.h](i3c_8h.md)>`

**Value:**

[SYS\_SLIST\_FOR\_EACH\_CONTAINER](group__single-linked-list__apis.md#gacd97d2f1044c0560d96c9f9a6f26d2f6)( \

&((struct [i3c\_driver\_data](structi3c__driver__data.md) \*)(bus->data))->attached\_dev.devices.i3c, desc, node)

iterate over all I3C devices present on the bus

Parameters
:   | bus | the I3C bus device pointer |
    | --- | --- |
    | desc | an I3C device descriptor pointer updated to point to the current slot at each iteration of the loop |

## [◆ ](#gaed0df9802cc9b268abcfe4e877ebf498)I3C\_DEVICE\_ID

| #define I3C\_DEVICE\_ID | ( |  | *pid* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

**Value:**

{ \

.pid = pid \

}

Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from PID.

This helper macro expands to a static initializer for a [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") by populating the PID (Provisioned ID) field.

Parameters
:   | pid | Provisioned ID. |
    | --- | --- |

## [◆ ](#gabec5796b92d4582761bc3de456f1df27)I3C\_DT\_IODEV\_DEFINE

| #define I3C\_DT\_IODEV\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

`#include <[i3c.h](i3c_8h.md)>`

**Value:**

const struct [i3c\_iodev\_data](structi3c__iodev__data.md) \_i3c\_iodev\_data\_##name = { \

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.dev\_id = [I3C\_DEVICE\_ID\_DT](group__i3c__devicetree.md#ga917b45ec38e08d0c464cebe3372b682e)(node\_id), \

}; \

RTIO\_IODEV\_DEFINE(name, &[i3c\_iodev\_api](#gace1f8f10af2d87bb5a17441645030833), (void \*)&\_i3c\_iodev\_data\_##name)

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:280

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3861

[I3C\_DEVICE\_ID\_DT](group__i3c__devicetree.md#ga917b45ec38e08d0c464cebe3372b682e)

#define I3C\_DEVICE\_ID\_DT(node\_id)

Structure initializer for i3c\_device\_id from devicetree.

**Definition** devicetree.h:36

[i3c\_iodev\_api](#gace1f8f10af2d87bb5a17441645030833)

const struct rtio\_iodev\_api i3c\_iodev\_api

[i3c\_iodev\_data](structi3c__iodev__data.md)

**Definition** i3c.h:2383

Define an iodev for a given dt node on the bus.

These do not need to be shared globally but doing so will save a small amount of memory.

Parameters
:   | name | Symbolic name of the iodev to define |
    | --- | --- |
    | node\_id | Devicetree node identifier |

## [◆ ](#gae7afa509b1d63374c551bcdaf84c5dd1)I3C\_LVR\_I2C\_DEV\_IDX

| #define I3C\_LVR\_I2C\_DEV\_IDX | ( |  | *lvr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([I3C\_LVR\_I2C\_DEV\_IDX\_MASK](#ga50fa249b36b91d56e49004548a1c7520), (lvr))

[I3C\_LVR\_I2C\_DEV\_IDX\_MASK](#ga50fa249b36b91d56e49004548a1c7520)

#define I3C\_LVR\_I2C\_DEV\_IDX\_MASK

I2C Device Index bitmask.

**Definition** i3c.h:210

I2C Device Index.

Obtain I2C Device Index value from the LVR value.

Parameters
:   | lvr | LVR value |
    | --- | --- |

## [◆ ](#ga4319835ddb6b5984b21f5a5a2f14ae75)I3C\_LVR\_I2C\_DEV\_IDX\_0

| #define I3C\_LVR\_I2C\_DEV\_IDX\_0   0 |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C Device Index 0.

I2C device has a 50 ns spike filter where it is not affected by high frequency on SCL.

## [◆ ](#ga02a21af4c679a81b8290beea30c8ef40)I3C\_LVR\_I2C\_DEV\_IDX\_1

| #define I3C\_LVR\_I2C\_DEV\_IDX\_1   1 |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C Device Index 1.

I2C device does not have a 50 ns spike filter but can work with high frequency on SCL.

## [◆ ](#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)I3C\_LVR\_I2C\_DEV\_IDX\_2

| #define I3C\_LVR\_I2C\_DEV\_IDX\_2   2 |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C Device Index 2.

I2C device does not have a 50 ns spike filter and cannot work with high frequency on SCL.

## [◆ ](#ga50fa249b36b91d56e49004548a1c7520)I3C\_LVR\_I2C\_DEV\_IDX\_MASK

| #define I3C\_LVR\_I2C\_DEV\_IDX\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7U, 5U) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C Device Index bitmask.

## [◆ ](#ga053945f5f67ee3c681de2c9362e69c39)I3C\_LVR\_I2C\_FM\_MODE

| #define I3C\_LVR\_I2C\_FM\_MODE   1 |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C FM Mode.

## [◆ ](#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)I3C\_LVR\_I2C\_FM\_PLUS\_MODE

| #define I3C\_LVR\_I2C\_FM\_PLUS\_MODE   0 |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C FM+ Mode.

## [◆ ](#gaaf759805bb5824a89612b292a4439982)I3C\_LVR\_I2C\_MODE

| #define I3C\_LVR\_I2C\_MODE | ( |  | *lvr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([I3C\_LVR\_I2C\_MODE\_MASK](#gaf073cc9ea1a68c57663c36de12554876), (lvr))

[I3C\_LVR\_I2C\_MODE\_MASK](#gaf073cc9ea1a68c57663c36de12554876)

#define I3C\_LVR\_I2C\_MODE\_MASK

I2C Mode Indicator bitmask.

**Definition** i3c.h:173

I2C Mode.

Obtain I2C Mode value from the LVR value.

Parameters
:   | lvr | LVR value |
    | --- | --- |

## [◆ ](#gaf073cc9ea1a68c57663c36de12554876)I3C\_LVR\_I2C\_MODE\_MASK

| #define I3C\_LVR\_I2C\_MODE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C Mode Indicator bitmask.

## Enumeration Type Documentation

## [◆ ](#ga7a0d66ab45f618ca055422e2b69abe90)i3c\_bus\_mode

| enum [i3c\_bus\_mode](#ga7a0d66ab45f618ca055422e2b69abe90) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C bus mode.

| Enumerator | |
| --- | --- |
| I3C\_BUS\_MODE\_PURE | Only I3C devices are on the bus. |
| I3C\_BUS\_MODE\_MIXED\_FAST | Both I3C and legacy I2C devices are on the bus.  The I2C devices have 50ns spike filter on SCL. |
| I3C\_BUS\_MODE\_MIXED\_LIMITED | Both I3C and legacy I2C devices are on the bus.  The I2C devices do not have 50ns spike filter on SCL and can tolerate maximum SDR SCL clock frequency. |
| I3C\_BUS\_MODE\_MIXED\_SLOW | Both I3C and legacy I2C devices are on the bus.  The I2C devices do not have 50ns spike filter on SCL but cannot tolerate maximum SDR SCL clock frequency. |
| I3C\_BUS\_MODE\_MAX |  |
| I3C\_BUS\_MODE\_INVALID |  |

## [◆ ](#ga5b111bc8fa8c3bee052e621d26dcc54a)i3c\_config\_type

| enum [i3c\_config\_type](#ga5b111bc8fa8c3bee052e621d26dcc54a) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Type of configuration being passed to configure function.

| Enumerator | |
| --- | --- |
| I3C\_CONFIG\_CONTROLLER |  |
| I3C\_CONFIG\_TARGET |  |
| I3C\_CONFIG\_CUSTOM |  |

## [◆ ](#gae9d98642c6f249ee0e6ea0dc491b5073)i3c\_data\_rate

| enum [i3c\_data\_rate](#gae9d98642c6f249ee0e6ea0dc491b5073) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C data rate.

I3C data transfer rate defined by the I3C specification.

| Enumerator | |
| --- | --- |
| I3C\_DATA\_RATE\_SDR | Single Data Rate messaging. |
| I3C\_DATA\_RATE\_HDR\_DDR | High Data Rate - Double Data Rate messaging. |
| I3C\_DATA\_RATE\_HDR\_TSL | High Data Rate - Ternary Symbol Legacy-inclusive-Bus. |
| I3C\_DATA\_RATE\_HDR\_TSP | High Data Rate - Ternary Symbol for Pure Bus. |
| I3C\_DATA\_RATE\_HDR\_BT | High Data Rate - Bulk Transport. |
| I3C\_DATA\_RATE\_MAX |  |
| I3C\_DATA\_RATE\_INVALID |  |

## [◆ ](#ga67686f0a5d83697361c655c3fd6e61c6)i3c\_i2c\_speed\_type

| enum [i3c\_i2c\_speed\_type](#ga67686f0a5d83697361c655c3fd6e61c6) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I2C bus speed under I3C bus.

Only FM and FM+ modes are supported for I2C devices under I3C bus.

| Enumerator | |
| --- | --- |
| I3C\_I2C\_SPEED\_FM | I2C FM mode. |
| I3C\_I2C\_SPEED\_FMPLUS | I2C FM+ mode. |
| I3C\_I2C\_SPEED\_MAX |  |
| I3C\_I2C\_SPEED\_INVALID |  |

## Function Documentation

## [◆ ](#ga5e69aaed50f99418c7123f652555ae20)i3c\_attach\_i2c\_device()

| int i3c\_attach\_i2c\_device | ( | struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Attach an I2C device.

Called to attach a I2C device to the addresses. This will also call the optional api to update any registers within the driver if implemented.

Warning
:   Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

Parameters
:   | target | Pointer to the target device descriptor |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If address is not available or if the device has already been attached before |

## [◆ ](#ga042d1a3315f040562534ce08306b329c)i3c\_attach\_i3c\_device()

| int i3c\_attach\_i3c\_device | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Attach an I3C device.

Called to attach a I3C device to the addresses. This is typically called before a SETDASA or ENTDAA to reserve the addresses. This will also call the optional api to update any registers within the driver if implemented.

Warning
:   Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

Parameters
:   | target | Pointer to the target device descriptor |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If address is not available or if the device has already been attached before |

## [◆ ](#ga554e0c4fa3e6855f431521ae42313216)i3c\_bus\_deftgts()

| int i3c\_bus\_deftgts | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Send the CCC DEFTGTS.

This builds the payload required for DEFTGTS and transmits it out

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -ENOMEM | No memory to build the payload. |
    | -EIO | General Input/Output error. |

## [◆ ](#ga149d70b1c2e02e19782aa21a94b13684)i3c\_bus\_has\_sec\_controller()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_bus\_has\_sec\_controller | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Check if the bus has a secondary controller.

This reads the BCR from the device descriptor struct of all targets to determine whether a device is a secondary controller.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |

Returns
:   True if the bus has a secondary controller, false otherwise.

## [◆ ](#ga9af9191a5ab2e5e2ea0478520721171d)i3c\_bus\_init()

| int i3c\_bus\_init | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_dev\_list](structi3c__dev__list.md) \* | *i3c\_dev\_list* ) |

`#include <[i3c.h](i3c_8h.md)>`

Generic helper function to perform bus initialization.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | [i3c\_dev\_list](structi3c__dev__list.md "Structure for describing known devices for a controller.") | Pointer to I3C device list. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |
    | -ENODEV | If a provisioned ID does not match to any target devices in the registered device list. |
    | -ENOSPC | No more free addresses can be assigned to target. |
    | -ENOSYS | Dynamic address assignment is not supported by the controller driver. |

## [◆ ](#ga807877923755aeb5a065e054fb42946d)i3c\_config\_get()

| | int i3c\_config\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [i3c\_config\_type](#ga5b111bc8fa8c3bee052e621d26dcc54a) | *type*, | |  |  | void \* | *config* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Get configuration of the I3C hardware.

This provides a way to get the current configuration of the I3C hardware.

This can return cached config or probed hardware parameters, but it has to be up to date with current configuration.

Parameters
:   | [in] | dev | Pointer to controller device driver instance. |
    | --- | --- | --- |
    | [in] | type | Type of configuration parameters being passed in `config`. |
    | [in,out] | config | Pointer to the configuration parameters. |

Note that if `type` is [I3C\_CONFIG\_CUSTOM](#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017), `config` must contain the ID of the parameter to be retrieved.

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General Input/Output errors. |
    | -ENOSYS | If not implemented. |

## [◆ ](#ga2f176f8440d86f4ec6c94a8911a75352)i3c\_configure()

| | int i3c\_configure | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [i3c\_config\_type](#ga5b111bc8fa8c3bee052e621d26dcc54a) | *type*, | |  |  | void \* | *config* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Configure the I3C hardware.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | type | Type of configuration parameters being passed in `config`. |
    | config | Pointer to the configuration parameters. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If invalid configure parameters. |
    | -EIO | General Input/Output errors. |
    | -ENOSYS | If not implemented. |

## [◆ ](#ga8e8de45499bff02cac4c59c1758ec0a7)i3c\_detach\_i2c\_device()

| int i3c\_detach\_i2c\_device | ( | struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Detach I2C Device.

called to remove an I2C device and to free up the address that it used. This will also call the optional api to update any registers within the driver if implemented.

Warning
:   Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

Parameters
:   | target | Pointer to the target device descriptor |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If device is already detached |

## [◆ ](#ga6db9688cc7e9d34404717ae753751579)i3c\_detach\_i3c\_device()

| int i3c\_detach\_i3c\_device | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Detach I3C Device.

called to remove an I3C device and to free up the address that it used. If it's dynamic address was not set, then it assumed that SETDASA failed and will free it's static addr. This will also call the optional api to update any registers within the driver if implemented.

Warning
:   Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

Parameters
:   | target | Pointer to the target device descriptor |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If device is already detached |

## [◆ ](#ga3a4dac6aa35249e6e277da8075b596a8)i3c\_dev\_list\_daa\_addr\_helper()

| int i3c\_dev\_list\_daa\_addr\_helper | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *addr\_slots*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_dev\_list](structi3c__dev__list.md) \* | *dev\_list*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *pid*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *must\_match*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *assigned\_okay*, |
|  |  | struct [i3c\_device\_desc](structi3c__device__desc.md) \*\* | *target*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr* ) |

`#include <[i3c.h](i3c_8h.md)>`

Helper function to find a usable address during ENTDAA.

This is a helper function to find a usable address during Dynamic Address Assignment. Given the PID (`pid`), it will search through the device list for the matching device descriptor. If the device descriptor indicates that there is a preferred address (i.e. assigned-address in device tree, [i3c\_device\_desc::init\_dynamic\_addr](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5 "Initial dynamic address.")), this preferred address will be returned if this address is still available. If it is not available, another free address will be returned.

If `must_match` is true, the PID (`pid`) must match one of the device in the device list.

If `must_match` is false, this will return an arbitrary address. This is useful when not all devices are described in device tree. Or else, the DAA process cannot proceed since there is no address to be assigned.

If `assigned_okay` is true, it will return the same address already assigned to the device ([i3c\_device\_desc::dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0 "Dynamic Address for this target device used for communication.")). If no address has been assigned, it behaves as if `assigned_okay` is false. This is useful for assigning the same address to the same device (for example, hot-join after device coming back from suspend).

If `assigned_okay` is false, the device cannot have an address assigned already (that [i3c\_device\_desc::dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0 "Dynamic Address for this target device used for communication.") is not zero). This is mainly used during the initial DAA.

Parameters
:   | [in] | addr\_slots | Pointer to address slots struct. |
    | --- | --- | --- |
    | [in] | dev\_list | Pointer to the device list struct. |
    | [in] | pid | Provisioned ID of device to be assigned address. |
    | [in] | must\_match | True if PID must match devices in the device list. False otherwise. |
    | [in] | assigned\_okay | True if it is okay to return the address already assigned to the target matching the PID (`pid`). |
    | [out] | target | Store the pointer of the device descriptor if it matches the incoming PID (`pid`). |
    | [out] | addr | Address to be assigned to target device. |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -ENODEV | if no device matches the PID (`pid`) in the device list and `must_match` is true. |
    | -EINVAL | if the device matching PID (`pid`) already has an address assigned or invalid function arguments. |

## [◆ ](#ga9a451379bef381c6a264a22a2282fa89)i3c\_dev\_list\_find()

| struct [i3c\_device\_desc](structi3c__device__desc.md) \* i3c\_dev\_list\_find | ( | const struct [i3c\_dev\_list](structi3c__dev__list.md) \* | *dev\_list*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_device\_id](structi3c__device__id.md) \* | *id* ) |

`#include <[i3c.h](i3c_8h.md)>`

Find a I3C target device descriptor by ID.

This finds the I3C target device descriptor in the device list matching the provided ID struct (`id`).

Parameters
:   | dev\_list | Pointer to the device list struct. |
    | --- | --- |
    | id | Pointer to I3C device ID struct. |

Returns
:   Pointer to the I3C target device descriptor, or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if none is found.

## [◆ ](#gafac78dca571ff7daa34fca0cfa7cc3b1)i3c\_dev\_list\_i2c\_addr\_find()

| struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* i3c\_dev\_list\_i2c\_addr\_find | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* ) |

`#include <[i3c.h](i3c_8h.md)>`

Find a I2C target device descriptor by address.

This finds the I2C target device descriptor in the attached device list matching the address (`addr`)

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | addr | Address to be matched. |

Returns
:   Pointer to the I2C target device descriptor, or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if none is found.

## [◆ ](#ga0e83c5a26b18acfbe7d532825a8fd54c)i3c\_dev\_list\_i3c\_addr\_find()

| struct [i3c\_device\_desc](structi3c__device__desc.md) \* i3c\_dev\_list\_i3c\_addr\_find | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) |

`#include <[i3c.h](i3c_8h.md)>`

Find a I3C target device descriptor by dynamic address.

This finds the I3C target device descriptor in the attached device list matching the dynamic address (`addr`)

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | addr | Dynamic address to be matched. |

Returns
:   Pointer to the I3C target device descriptor, or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if none is found.

## [◆ ](#gaecbb16ce8edcd9ad7a7afcfb1251aa76)i3c\_dev\_list\_i3c\_static\_addr\_find()

| struct [i3c\_device\_desc](structi3c__device__desc.md) \* i3c\_dev\_list\_i3c\_static\_addr\_find | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) |

`#include <[i3c.h](i3c_8h.md)>`

Find a I3C target device descriptor by static address.

This finds the I3C target device descriptor in the attached device list matching the static address (`addr`)

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | addr | static address to be matched. |

Returns
:   Pointer to the I3C target device descriptor, or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if none is found.

## [◆ ](#ga4e4a7e9408bd2f43602367bc9fe4f81e)i3c\_device\_adv\_info\_get()

| int i3c\_device\_adv\_info\_get | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Get advanced information from device and update device descriptor.

This retrieves some information:

- Max Read Length (GETMRL)
- Max Write Length (GETMWL)
- Get Capabilities (GETCAPS)
- Max Device Speed (GETMXDS) (if applicable) from the device and update the corresponding fields of the device descriptor.

This only updates the field(s) in device descriptor only if CCC operations succeed.

Note
:   This should only be called after [i3c\_device\_basic\_info\_get()](#gaac5d10b8f42a6a069e0ac15cc7263db8) or if the BCR was already obtained through ENTDAA, DEFTGTS, or GETBCR.

Parameters
:   | [in,out] | target | I3C target device descriptor. |
    | --- | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EIO | General Input/Output error. |

## [◆ ](#gaac5d10b8f42a6a069e0ac15cc7263db8)i3c\_device\_basic\_info\_get()

| int i3c\_device\_basic\_info\_get | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Get basic information from device and update device descriptor.

This retrieves some basic information:

- Bus Characteristics Register (GETBCR)
- Device Characteristics Register (GETDCR) from the device and update the corresponding fields of the device descriptor.

This only updates the field(s) in device descriptor only if CCC operations succeed.

Parameters
:   | [in,out] | target | I3C target device descriptor. |
    | --- | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EIO | General Input/Output error. |

## [◆ ](#ga22857e3c19dbd5d93f3aed120fa32c84)i3c\_device\_controller\_handoff()

| int i3c\_device\_controller\_handoff | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *requested* ) |

`#include <[i3c.h](i3c_8h.md)>`

Perform Controller Handoff.

This performs the controller handoff according to 5.1.7.1 of I3C v1.1.1 Specification.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | requested | True if the target requested the Handoff, False if the active controller is passing it to a secondary controller |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EIO | General Input/Output error. |
    | -EBUSY | Target cannot accept Controller Handoff |

## [◆ ](#ga0432131f4bdd02867cd4139dd04c30e2)i3c\_device\_desc\_alloc()

| | struct [i3c\_device\_desc](structi3c__device__desc.md) \* i3c\_device\_desc\_alloc | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

## [◆ ](#ga473dd9ba2f10b74443b849ad110a4129)i3c\_device\_desc\_free()

| | void i3c\_device\_desc\_free | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *desc* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

## [◆ ](#ga214dddc181748b2edd4f5aedd92e60cf)i3c\_device\_desc\_in\_pool()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_device\_desc\_in\_pool | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *desc* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

## [◆ ](#ga10a3963b749cc667a03975889d618d1b)i3c\_device\_find()

| | struct [i3c\_device\_desc](structi3c__device__desc.md) \* i3c\_device\_find | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [i3c\_device\_id](structi3c__device__id.md) \* | *id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Find a registered I3C target device.

Controller only API.

This returns the I3C device descriptor of the I3C device matching the incoming `id`.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |
    | id | Pointer to I3C device ID. |

Returns
:   Pointer to I3C device descriptor, or [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if no I3C device found matching incoming `id`.

## [◆ ](#ga39a760d8ba759f9443689fc954eb3d4b)i3c\_device\_info\_get()

| | int i3c\_device\_info\_get | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Get all information from device and update device descriptor.

This retrieves all information:

- Bus Characteristics Register (GETBCR)
- Device Characteristics Register (GETDCR)
- Max Read Length (GETMRL)
- Max Write Length (GETMWL)
- Get Capabilities (GETCAPS)
- Max Device Speed (GETMXDS) (if applicable) from the device and update the corresponding fields of the device descriptor.

This only updates the field(s) in device descriptor only if CCC operations succeed.

Parameters
:   | [in,out] | target | I3C target device descriptor. |
    | --- | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EIO | General Input/Output error. |

## [◆ ](#gaa6d5445489bfc8611c98b93f49305862)i3c\_do\_ccc()

| int i3c\_do\_ccc | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \* | *payload* ) |

`#include <[i3c.h](i3c_8h.md)>`

Send CCC to the bus.

Parameters
:   | dev | Pointer to the device structure for the controller driver instance. |
    | --- | --- |
    | payload | Pointer to the structure describing the CCC payload. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General Input / output error. |
    | -EINVAL | Invalid valid set in the payload structure. |
    | -ENOSYS | Not implemented. |

## [◆ ](#gabb54c0e85d0f5e8585391f9e5c20d4b6)i3c\_do\_daa()

| | int i3c\_do\_daa | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Perform Dynamic Address Assignment on the I3C bus.

This routine asks the controller to perform dynamic address assignment where the controller belongs. Only the active controller of the bus should do this.

Note
:   For controller driver implementation, the controller should perform SETDASA to allow static addresses to be the dynamic addresses before actually doing ENTDAA.

Parameters
:   | dev | Pointer to the device structure for the controller driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |
    | -ENODEV | If a provisioned ID does not match to any target devices in the registered device list. |
    | -ENOSPC | No more free addresses can be assigned to target. |
    | -ENOSYS | Dynamic address assignment is not supported by the controller driver. |

## [◆ ](#ga353db1ca445310c3ce6df61ed53c4bc9)i3c\_i2c\_device\_desc\_alloc()

| | struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* i3c\_i2c\_device\_desc\_alloc | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

## [◆ ](#gaf7d635d3be9821fbd00cf8ef7b0ca510)i3c\_i2c\_device\_desc\_free()

| | void i3c\_i2c\_device\_desc\_free | ( | struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* | *desc* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

## [◆ ](#ga08398aae55aa7f06a18d7f2e5e37bc98)i3c\_i2c\_device\_desc\_in\_pool()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_i2c\_device\_desc\_in\_pool | ( | struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* | *desc* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

## [◆ ](#ga3b612267e71202094fb4adab64ffd61c)i3c\_iodev\_submit()

| | void i3c\_iodev\_submit | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Submit request(s) to an I3C device with RTIO.

Parameters
:   | iodev\_sqe | Prepared submissions queue entry connected to an iodev defined by I3C\_DT\_IODEV\_DEFINE. |
    | --- | --- |

## [◆ ](#ga909d531941cd81850f4a05c51646690d)i3c\_iodev\_submit\_fallback()

| void i3c\_iodev\_submit\_fallback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* ) |

`#include <[i3c.h](i3c_8h.md)>`

Fallback submit implementation.

This implementation will schedule a blocking I3C transaction on the bus via the RTIO work queue. It is only used if the I3C driver did not implement the iodev\_submit function.

Parameters
:   | dev | Pointer to the device structure for an I3C controller driver. |
    | --- | --- |
    | iodev\_sqe | Prepared submissions queue entry connected to an iodev defined by I3C\_DT\_IODEV\_DEFINE. |

## [◆ ](#gaaf7736a8895de826f7fac1a9ecf0d7ea)i3c\_odd\_parity()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_odd\_parity | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Calculate odd parity.

Calculate the Odd Parity of a Target Address.

Parameters
:   | p | The 7b target dynamic address |
    | --- | --- |

Returns
:   The odd parity bit

## [◆ ](#gae6c8e8612368808117f4fce960e43769)i3c\_reattach\_i3c\_device()

| int i3c\_reattach\_i3c\_device | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *old\_dyn\_addr* ) |

`#include <[i3c.h](i3c_8h.md)>`

Reattach I3C device.

called after every time an I3C device has its address changed. It can be because the device has been powered down and has lost its address, or it can happen when a device had a static address and has been assigned a dynamic address with SETDASA or a dynamic address has been updated with SETNEWDA. This will also call the optional api to update any registers within the driver if implemented.

Warning
:   Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

Parameters
:   | target | Pointer to the target device descriptor |
    | --- | --- |
    | old\_dyn\_addr | The old dynamic address of target device, 0 if there was no old dynamic address |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If address is not available |

## [◆ ](#ga7b23e08b10a09bde4e87328d6915aa25)i3c\_recover\_bus()

| | int i3c\_recover\_bus | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Attempt bus recovery on the I3C bus.

This routine asks the controller to attempt bus recovery.

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | If bus recovery fails. |
    | -EIO | General input / output error. |
    | -ENOSYS | Bus recovery is not supported by the controller driver. |

## [◆ ](#gab46a231442a7bf60e7e28ca2f52d25fc)i3c\_rtio\_copy()

| struct [rtio\_sqe](structrtio__sqe.md) \* i3c\_rtio\_copy | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, |
|  |  | const struct [i3c\_msg](structi3c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs* ) |

`#include <[i3c.h](i3c_8h.md)>`

Copy the i3c\_msgs into a set of RTIO requests.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | iodev | RTIO IODev to target for the submissions |
    | msgs | Array of messages |
    | num\_msgs | Number of i3c msgs in array |

Return values
:   | sqe | Last submission in the queue added |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | Not enough memory in the context to copy the requests |

## Variable Documentation

## [◆ ](#gace1f8f10af2d87bb5a17441645030833)i3c\_iodev\_api

| | const struct [rtio\_iodev\_api](structrtio__iodev__api.md) i3c\_iodev\_api | | --- | | extern |
| --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
