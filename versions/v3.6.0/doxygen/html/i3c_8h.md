---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/i3c_8h.html
original_path: doxygen/html/i3c_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/i3c/addresses.h](addresses_8h_source.md)>`  
`#include <[zephyr/drivers/i3c/ccc.h](ccc_8h_source.md)>`  
`#include <[zephyr/drivers/i3c/devicetree.h](drivers_2i3c_2devicetree_8h_source.md)>`  
`#include <[zephyr/drivers/i3c/ibi.h](ibi_8h_source.md)>`  
`#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h_source.md)>`  
`#include <[zephyr/drivers/i3c/target_device.h](target__device_8h_source.md)>`  
`#include <syscalls/i3c.h>`

[Go to the source code of this file.](i3c_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i3c\_msg](structi3c__msg.md) |
|  | One I3C Message. [More...](structi3c__msg.md#details) |
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

| Macros | |
| --- | --- |
| #define | [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)   (0U << 0U) |
|  | Write message to I3C bus. |
| #define | [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Read message from I3C bus. |
| #define | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Send STOP after this message. |
| #define | [I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | RESTART I3C transaction for this message. |
| #define | [I3C\_MSG\_HDR](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Transfer use HDR mode. |
| #define | [I3C\_MSG\_NBCH](group__i3c__transfer__api.md#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Skip I3C broadcast header. |
| #define | [I3C\_MSG\_HDR\_MODE0](group__i3c__transfer__api.md#ga18aac0862826869f94e5a71670debcb0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | I3C HDR Mode 0. |
| #define | [I3C\_MSG\_HDR\_MODE1](group__i3c__transfer__api.md#ga8eb3dc48237dfdb25fde40a1efa03241)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | I3C HDR Mode 1. |
| #define | [I3C\_MSG\_HDR\_MODE2](group__i3c__transfer__api.md#ga15cbd61e7d509c28b22fbc9e0844cb23)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | I3C HDR Mode 2. |
| #define | [I3C\_MSG\_HDR\_MODE3](group__i3c__transfer__api.md#ga162fb9ab0e4ed7f8feb0e91d183a88e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | I3C HDR Mode 3. |
| #define | [I3C\_MSG\_HDR\_MODE4](group__i3c__transfer__api.md#gabe45532238bc15672f6454dac70d20cf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | I3C HDR Mode 4. |
| #define | [I3C\_MSG\_HDR\_MODE5](group__i3c__transfer__api.md#gac712daa606d0c51ce523d7a687821282)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | I3C HDR Mode 5. |
| #define | [I3C\_MSG\_HDR\_MODE6](group__i3c__transfer__api.md#ga7654c1947e13c019c24bf12712b0773b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | I3C HDR Mode 6. |
| #define | [I3C\_MSG\_HDR\_MODE7](group__i3c__transfer__api.md#ga08df1d8df82226d1f23b4cc923584672)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | I3C HDR Mode 7. |
| #define | [I3C\_MSG\_HDR\_DDR](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a)   [I3C\_MSG\_HDR\_MODE0](group__i3c__transfer__api.md#ga18aac0862826869f94e5a71670debcb0) |
|  | I3C HDR-DDR (Double Data Rate). |
| #define | [I3C\_MSG\_HDR\_TSP](group__i3c__transfer__api.md#gaa61322f770db296b5ab718c48ab960d3)   [I3C\_MSG\_HDR\_MODE1](group__i3c__transfer__api.md#ga8eb3dc48237dfdb25fde40a1efa03241) |
|  | I3C HDR-TSP (Ternary Symbol Pure-bus). |
| #define | [I3C\_MSG\_HDR\_TSL](group__i3c__transfer__api.md#gac43a2d266f3a23fd6dfa11405f3fd6f3)   [I3C\_MSG\_HDR\_MODE2](group__i3c__transfer__api.md#ga15cbd61e7d509c28b22fbc9e0844cb23) |
|  | I3C HDR-TSL (Ternary Symbol Legacy-inclusive-bus). |
| #define | [I3C\_MSG\_HDR\_BT](group__i3c__transfer__api.md#ga8b2fdcb827cbd3325f124a1c615698e7)   [I3C\_MSG\_HDR\_MODE3](group__i3c__transfer__api.md#ga162fb9ab0e4ed7f8feb0e91d183a88e7) |
|  | I3C HDR-BT (Bulk Transport). |
| #define | [I3C\_DEVICE\_ID](group__i3c__interface.md#gaed0df9802cc9b268abcfe4e877ebf498)(pid) |
|  | Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from PID. |
| Bus Characteristic Register (BCR) | |
| - BCR[7:6]: Device Role   - 0: I3C Target   - 1: I3C Controller capable   - 2: Reserved   - 3: Reserved - BCR[5]: Advanced Capabilities   - 0: Does not support optional advanced capabilities.   - 1: Supports optional advanced capabilities which can be viewed via GETCAPS CCC. - BCR[4]: Virtual Target Support   - 0: Is not a virtual target.   - 1: Is a virtual target. - BCR[3]: Offline Capable   - 0: Will always response to I3C commands.   - 1: Will not always response to I3C commands. - BCR[2]: IBI Payload   - 0: No data bytes following the accepted IBI.   - 1: One data byte (MDB, Mandatory Data Byte) follows the accepted IBI. Additional data bytes may also follows. - BCR[1]: IBI Request Capable   - 0: Not capable   - 1: Capable - BCR[0]: Max Data Speed Limitation   - 0: No Limitation   - 1: Limitation obtained via GETMXDS CCC. | |
| #define | [I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT](group__i3c__interface.md#ga91ebe41a421dc05ae7f1de1ce2dd314f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Max Data Speed Limitation bit. |
| #define | [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | IBI Request Capable bit. |
| #define | [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | IBI Payload bit. |
| #define | [I3C\_BCR\_OFFLINE\_CAPABLE](group__i3c__interface.md#ga7b9fea89457022d8012ac25133bf63db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Offline Capable bit. |
| #define | [I3C\_BCR\_VIRTUAL\_TARGET](group__i3c__interface.md#ga69dc4a5004da568684a3c72046bba870)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Virtual Target Support bit. |
| #define | [I3C\_BCR\_ADV\_CAPABILITIES](group__i3c__interface.md#ga07018705794753d0d0d65131f011e097)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Advanced Capabilities bit. |
| #define | [I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET](group__i3c__interface.md#ga867b4b12b23c803b86b57dcc86b9e604)   0U |
|  | Device Role - I3C Target. |
| #define | [I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852)   1U |
|  | Device Role - I3C Controller Capable. |
| #define | [I3C\_BCR\_DEVICE\_ROLE\_SHIFT](group__i3c__interface.md#ga09bda29f6c4b71cd4d5d7ba98c677706)   6U |
|  | Device Role bit shift value. |
| #define | [I3C\_BCR\_DEVICE\_ROLE\_MASK](group__i3c__interface.md#ga25721c9963040c84b7f5bbb48bb87b44)   (0x03U << [I3C\_BCR\_DEVICE\_ROLE\_SHIFT](group__i3c__interface.md#ga09bda29f6c4b71cd4d5d7ba98c677706)) |
|  | Device Role bit shift mask. |
| #define | [I3C\_BCR\_DEVICE\_ROLE](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)(bcr) |
|  | Device Role. |
| Legacy Virtual Register (LVR) | |
| Legacy Virtual Register (LVR)   - LVR[7:5]: I2C device index:   - 0: I2C device has a 50 ns spike filter where it is not affected by high frequency on SCL.   - 1: I2C device does not have a 50 ns spike filter but can work with high frequency on SCL.   - 2: I2C device does not have a 50 ns spike filter and cannot work with high frequency on SCL. - LVR[4]: I2C mode indicator:   - 0: FM+ mode   - 1: FM mode - LVR[3:0]: Reserved. | |
| #define | [I3C\_LVR\_I2C\_FM\_PLUS\_MODE](group__i3c__interface.md#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)   0 |
|  | I2C FM+ Mode. |
| #define | [I3C\_LVR\_I2C\_FM\_MODE](group__i3c__interface.md#ga053945f5f67ee3c681de2c9362e69c39)   1 |
|  | I2C FM Mode. |
| #define | [I3C\_LVR\_I2C\_MODE\_SHIFT](group__i3c__interface.md#gafc35b1fdf105ebd3bc1835ad38fa4229)   4 |
|  | I2C Mode Indicator bit shift value. |
| #define | [I3C\_LVR\_I2C\_MODE\_MASK](group__i3c__interface.md#gaf073cc9ea1a68c57663c36de12554876)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | I2C Mode Indicator bitmask. |
| #define | [I3C\_LVR\_I2C\_MODE](group__i3c__interface.md#gaaf759805bb5824a89612b292a4439982)(lvr) |
|  | I2C Mode. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_0](group__i3c__interface.md#ga4319835ddb6b5984b21f5a5a2f14ae75)   0 |
|  | I2C Device Index 0. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_1](group__i3c__interface.md#ga02a21af4c679a81b8290beea30c8ef40)   1 |
|  | I2C Device Index 1. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_2](group__i3c__interface.md#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)   2 |
|  | I2C Device Index 2. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_SHIFT](group__i3c__interface.md#gadb583c049cb0b212836115b6cfa5a569)   5 |
|  | I2C Device Index bit shift value. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX\_MASK](group__i3c__interface.md#ga50fa249b36b91d56e49004548a1c7520)   (0x07U << [I3C\_LVR\_I2C\_DEV\_IDX\_SHIFT](group__i3c__interface.md#gadb583c049cb0b212836115b6cfa5a569)) |
|  | I2C Device Index bitmask. |
| #define | [I3C\_LVR\_I2C\_DEV\_IDX](group__i3c__interface.md#gae7afa509b1d63374c551bcdaf84c5dd1)(lvr) |
|  | I2C Device Index. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_bus\_mode](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90) {     [I3C\_BUS\_MODE\_PURE](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445) , [I3C\_BUS\_MODE\_MIXED\_FAST](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434) , [I3C\_BUS\_MODE\_MIXED\_LIMITED](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722) , [I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a) ,     [I3C\_BUS\_MODE\_MAX](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) = I3C\_BUS\_MODE\_MIXED\_SLOW , [I3C\_BUS\_MODE\_INVALID](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c)   } |
|  | I3C bus mode. [More...](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90) |
| enum | [i3c\_i2c\_speed\_type](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6) { [I3C\_I2C\_SPEED\_FM](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1) , [I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea) , [I3C\_I2C\_SPEED\_MAX](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) = I3C\_I2C\_SPEED\_FMPLUS , [I3C\_I2C\_SPEED\_INVALID](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4) } |
|  | I2C bus speed under I3C bus. [More...](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6) |
| enum | [i3c\_data\_rate](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073) {     [I3C\_DATA\_RATE\_SDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9) , [I3C\_DATA\_RATE\_HDR\_DDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301) , [I3C\_DATA\_RATE\_HDR\_TSL](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590) , [I3C\_DATA\_RATE\_HDR\_TSP](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d) ,     [I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed) , [I3C\_DATA\_RATE\_MAX](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) = I3C\_DATA\_RATE\_HDR\_BT , [I3C\_DATA\_RATE\_INVALID](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a)   } |
|  | I3C data rate. [More...](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073) |
| enum | [i3c\_sdr\_controller\_error\_codes](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870) {     [I3C\_ERROR\_CE0](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a29a9faf9402dbad479d7c72af3074282) , [I3C\_ERROR\_CE1](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ae60ebbf70623d022df65ce8837a5bddb) , [I3C\_ERROR\_CE2](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a46fdc1719e801fbb6a61db7b7675a574) , [I3C\_ERROR\_CE3](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ac18dd1126126aed36d7c4ca399133e1f) ,     [I3C\_ERROR\_CE\_UNKNOWN](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502) , [I3C\_ERROR\_CE\_NONE](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870af8c1a2219f28b91b11206f7fafd12707) , [I3C\_ERROR\_CE\_MAX](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a8dfdbe43a58837e87eb08da228c462e7) = I3C\_ERROR\_CE\_UNKNOWN , [I3C\_ERROR\_CE\_INVALID](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a72a987f540981d0c0ef973cf835707a0)   } |
|  | I3C SDR Controller Error Codes. [More...](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870) |
| enum | [i3c\_sdr\_target\_error\_codes](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c) {     [I3C\_ERROR\_TE0](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cae9d64998fe25f44268fc35944e23661a) , [I3C\_ERROR\_TE1](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144caa79f8166d1c6bf18311adf11e6c612fe) , [I3C\_ERROR\_TE2](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab6d0cb581f823ba39934c835eed7207e) , [I3C\_ERROR\_TE3](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca4d5a837d35c5a752fee2cb4cdf761cd3) ,     [I3C\_ERROR\_TE4](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3fd9d3a819fb1f3d79e53757aaa03dfd) , [I3C\_ERROR\_TE5](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab014ca57d29162e7cf3116be36693c8f) , [I3C\_ERROR\_TE6](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3f5f0fe6d716fd7df84b99df707c2a8e) , [I3C\_ERROR\_DBR](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab02aee605de8820b586908bafcd8e285) ,     [I3C\_ERROR\_TE\_UNKNOWN](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791) , [I3C\_ERROR\_TE\_NONE](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca5bc59253e371b88471b5d9bc15cd9c3a) , [I3C\_ERROR\_TE\_MAX](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca7e6c2b9e56fc594ca57501adb09b26c7) = I3C\_ERROR\_TE\_UNKNOWN , [I3C\_ERROR\_TE\_INVALID](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cadb9cd0b5e4c5e0ae96f941d39a4af23a)   } |
|  | I3C SDR Target Error Codes. [More...](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c) |
| enum | [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) { [I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5) , [I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00) , [I3C\_CONFIG\_CUSTOM](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017) } |
|  | Type of configuration being passed to configure function. [More...](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) |

| Functions | |
| --- | --- |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_dev\_list\_find](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89) (const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list, const struct [i3c\_device\_id](structi3c__device__id.md) \*id) |
|  | Find a I3C target device descriptor by ID. |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_dev\_list\_i3c\_addr\_find](group__i3c__interface.md#gaa9d6c8bcded72a85b80a98a019d90461) (struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) \*dev\_list, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Find a I3C target device descriptor by dynamic address. |
| struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* | [i3c\_dev\_list\_i2c\_addr\_find](group__i3c__interface.md#ga959da8f875822bb94c9c5e72fdc9fbdb) (struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) \*dev\_list, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Find a I2C target device descriptor by address. |
| int | [i3c\_determine\_default\_addr](group__i3c__interface.md#ga61bed94233fd977f539f1f51c75e98a6) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr) |
|  | Helper function to find the default address an i3c device is attached with. |
| int | [i3c\_dev\_list\_daa\_addr\_helper](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pid, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) must\_match, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) assigned\_okay, struct [i3c\_device\_desc](structi3c__device__desc.md) \*\*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr) |
|  | Helper function to find a usable address during ENTDAA. |
| static int | [i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352) (const struct [device](structdevice.md) \*dev, enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config) |
|  | Configure the I3C hardware. |
| static int | [i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d) (const struct [device](structdevice.md) \*dev, enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config) |
|  | Get configuration of the I3C hardware. |
| static int | [i3c\_recover\_bus](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25) (const struct [device](structdevice.md) \*dev) |
|  | Attempt bus recovery on the I3C bus. |
| int | [i3c\_attach\_i3c\_device](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Attach an I3C device. |
| int | [i3c\_reattach\_i3c\_device](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr) |
|  | Reattach I3C device. |
| int | [i3c\_detach\_i3c\_device](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Detach I3C Device. |
| int | [i3c\_attach\_i2c\_device](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20) (struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target) |
|  | Attach an I2C device. |
| int | [i3c\_detach\_i2c\_device](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7) (struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target) |
|  | Detach I2C Device. |
| static int | [i3c\_do\_daa](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6) (const struct [device](structdevice.md) \*dev) |
|  | Perform Dynamic Address Assignment on the I3C bus. |
| int | [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862) (const struct [device](structdevice.md) \*dev, struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload) |
|  | Send CCC to the bus. |
| int | [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Perform data transfer from the controller to a I3C target device. |
| static struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_device\_find](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b) (const struct [device](structdevice.md) \*dev, const struct [i3c\_device\_id](structi3c__device__id.md) \*id) |
|  | Find a registered I3C target device. |
| static int | [i3c\_ibi\_raise](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66) (const struct [device](structdevice.md) \*dev, struct [i3c\_ibi](structi3c__ibi.md) \*request) |
|  | Raise an In-Band Interrupt (IBI). |
| static int | [i3c\_ibi\_enable](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Enable IBI of a target device. |
| static int | [i3c\_ibi\_disable](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Disable IBI of a target device. |
| static int | [i3c\_ibi\_has\_payload](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Check if target's IBI has payload. |
| static int | [i3c\_device\_is\_ibi\_capable](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Check if device is IBI capable. |
| static int | [i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write a set amount of data to an I3C target device. |
| static int | [i3c\_read](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read a set amount of data from an I3C target device. |
| static int | [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read) |
|  | Write then read data from an I3C target device. |
| static int | [i3c\_burst\_read](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read multiple bytes from an internal address of an I3C target device. |
| static int | [i3c\_burst\_write](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write multiple bytes to an internal address of an I3C target device. |
| static int | [i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read internal register of an I3C target device. |
| static int | [i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write internal register of an I3C target device. |
| static int | [i3c\_reg\_update\_byte](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Update internal register of an I3C target device. |
| void | [i3c\_dump\_msgs](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348) (const char \*name, const struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Dump out an I3C message. |
| int | [i3c\_bus\_init](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d) (const struct [device](structdevice.md) \*dev, const struct [i3c\_dev\_list](structi3c__dev__list.md) \*[i3c\_dev\_list](structi3c__dev__list.md)) |
|  | Generic helper function to perform bus initialization. |
| int | [i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Get basic information from device and update device descriptor. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c.h](i3c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
