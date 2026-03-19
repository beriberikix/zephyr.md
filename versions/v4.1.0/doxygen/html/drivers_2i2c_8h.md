---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2i2c_8h.html
original_path: doxygen/html/drivers_2i2c_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c.h File Reference

Public APIs for the I2C drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h_source.md)>`  
`#include <[zephyr/stats/stats.h](stats_2stats_8h_source.md)>`  
`#include <zephyr/syscalls/i2c.h>`

[Go to the source code of this file.](drivers_2i2c_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i2c\_dt\_spec](structi2c__dt__spec.md) |
|  | Complete I2C DT information. [More...](structi2c__dt__spec.md#details) |
| struct | [i2c\_msg](structi2c__msg.md) |
|  | One I2C Message. [More...](structi2c__msg.md#details) |
| struct | [i2c\_target\_callbacks](structi2c__target__callbacks.md) |
|  | Structure providing callbacks to be implemented for devices that supports the I2C target API. [More...](structi2c__target__callbacks.md#details) |
| struct | [i2c\_target\_config](structi2c__target__config.md) |
|  | Structure describing a device that supports the I2C target API. [More...](structi2c__target__config.md#details) |
| struct | [i2c\_device\_state](structi2c__device__state.md) |
|  | I2C specific device state which allows for i2c device class specific additions. [More...](structi2c__device__state.md#details) |

| Macros | |
| --- | --- |
| #define | [I2C\_SPEED\_STANDARD](group__i2c__interface.md#ga5ca8c5fbb2caa99ab0b7007ce2c11633)   (0x1U) |
|  | I2C Standard Speed: 100 kHz. |
| #define | [I2C\_SPEED\_FAST](group__i2c__interface.md#gaef9d097ed2b58676498a33f3cf76f38d)   (0x2U) |
|  | I2C Fast Speed: 400 kHz. |
| #define | [I2C\_SPEED\_FAST\_PLUS](group__i2c__interface.md#ga9c867195c4a99615ed9c0011293a2155)   (0x3U) |
|  | I2C Fast Plus Speed: 1 MHz. |
| #define | [I2C\_SPEED\_HIGH](group__i2c__interface.md#gac7bce1bbfb422a123d3228e97e2cbb71)   (0x4U) |
|  | I2C High Speed: 3.4 MHz. |
| #define | [I2C\_SPEED\_ULTRA](group__i2c__interface.md#ga213468d14d1241632c957873cf2d9628)   (0x5U) |
|  | I2C Ultra Fast Speed: 5 MHz. |
| #define | [I2C\_SPEED\_DT](group__i2c__interface.md#gad38207f2e64b6ef3c08b17c8ccb3a836)   (0x7U) |
|  | Device Tree specified speed. |
| #define | [I2C\_SPEED\_SHIFT](group__i2c__interface.md#ga6d0aaaec30d1e64e1b4ad674423d131f)   (1U) |
| #define | [I2C\_SPEED\_SET](group__i2c__interface.md#ga6d64fdac5a2d9008e7856e670b3c4305)(speed) |
| #define | [I2C\_SPEED\_MASK](group__i2c__interface.md#gade41614d9cb3efd61b22eda9c1715e4c)   (0x7U << [I2C\_SPEED\_SHIFT](group__i2c__interface.md#ga6d0aaaec30d1e64e1b4ad674423d131f)) /\* 3 bits \*/ |
| #define | [I2C\_SPEED\_GET](group__i2c__interface.md#ga0eda328bb70285895d09154f9a828040)(cfg) |
| #define | [I2C\_ADDR\_10\_BITS](group__i2c__interface.md#ga66836d37196ce866681f506c44c8766d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Use 10-bit addressing. |
| #define | [I2C\_MODE\_CONTROLLER](group__i2c__interface.md#ga6b03c8a7668528e2902073ffaa1d3a13)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Peripheral to act as Controller. |
| #define | [I2C\_DT\_SPEC\_GET\_ON\_I3C](group__i2c__interface.md#ga6479e2c8f807fc8c92646a87d1dcca84)(node\_id) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree (on I3C bus). |
| #define | [I2C\_DT\_SPEC\_GET\_ON\_I2C](group__i2c__interface.md#gafa81ab3407e8a1da368b729b31471af8)(node\_id) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree (on I2C bus). |
| #define | [I2C\_DT\_SPEC\_GET](group__i2c__interface.md#gabb3ae5225cea677f3f3b36e4477ed045)(node\_id) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree. |
| #define | [I2C\_DT\_SPEC\_INST\_GET](group__i2c__interface.md#ga2197cbc5122f0d8b2e0788113bcb5963)(inst) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree instance. |
| #define | [I2C\_MSG\_WRITE](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732)   (0U << 0U) |
|  | Write message to I2C bus. |
| #define | [I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Read message from I2C bus. |
| #define | [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Send STOP after this message. |
| #define | [I2C\_MSG\_RESTART](group__i2c__interface.md#ga8c6cf7be2a04979fdb9d0b7dd9c4f831)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | RESTART I2C transaction for this message. |
| #define | [I2C\_MSG\_ADDR\_10\_BITS](group__i2c__interface.md#ga5569e8a3e4f6660928dfe443067c472c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Use 10-bit addressing for this message. |
| #define | [I2C\_TARGET\_FLAGS\_ADDR\_10\_BITS](group__i2c__interface.md#ga9031b418a053f4fe0ace72fea91dec3d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Target device responds to 10-bit addressing. |
| #define | [I2C\_DEVICE\_DT\_DEFINE](group__i2c__interface.md#ga47b9d476cc85d6f5b8081c73dd87064f)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with I2C specifics. |
| #define | [I2C\_DEVICE\_DT\_INST\_DEFINE](group__i2c__interface.md#gabfd94bccb99bd1a958cd8d7902b2072a)(inst, ...) |
|  | Like [I2C\_DEVICE\_DT\_DEFINE()](group__i2c__interface.md#ga47b9d476cc85d6f5b8081c73dd87064f "Like DEVICE_DT_DEFINE() with I2C specifics.") for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [I2C\_DT\_IODEV\_DEFINE](group__i2c__interface.md#ga304d3b906b5222a9b704f5b35641143d)(name, node\_id) |
|  | Define an iodev for a given dt node on the bus. |
| #define | [I2C\_IODEV\_DEFINE](group__i2c__interface.md#ga451d0877ad5f4c2e9601dc2db8644924)(name, \_bus, \_addr) |
|  | Define an iodev for a given i2c device on a bus. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc)) (const struct [device](structdevice.md) \*dev, int result, void \*data) |
|  | I2C callback for asynchronous transfer requests. |
| typedef int(\* | [i2c\_target\_write\_requested\_cb\_t](group__i2c__interface.md#ga4cd9be521a6c7d088f15b88400624e4e)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config) |
|  | Function called when a write to the device is initiated. |
| typedef int(\* | [i2c\_target\_write\_received\_cb\_t](group__i2c__interface.md#ga619db7eea1c4400adcbea5dddf5cf2c5)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Function called when a write to the device is continued. |
| typedef int(\* | [i2c\_target\_read\_requested\_cb\_t](group__i2c__interface.md#ga244264ecdbd51210728ee92dcbebbc87)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Function called when a read from the device is initiated. |
| typedef int(\* | [i2c\_target\_read\_processed\_cb\_t](group__i2c__interface.md#ga4cb0ae2cf41fc2105d1baa5e496e5dae)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Function called when a read from the device is continued. |
| typedef int(\* | [i2c\_target\_stop\_cb\_t](group__i2c__interface.md#ga3c898d0bef364461a3502037cf3d40b0)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config) |
|  | Function called when a stop condition is observed after a start condition addressed to a particular device. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_is\_ready\_dt](group__i2c__interface.md#gafc6799ac7a95eaa8e186cbe6981b1548) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec) |
|  | Validate that I2C bus is ready. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_is\_read\_op](group__i2c__interface.md#ga99288e3e995f8cdaebcbd3a38d22b2dc) (const struct [i2c\_msg](structi2c__msg.md) \*msg) |
|  | Check if the current message is a read operation. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_is\_stop\_op](group__i2c__interface.md#ga3b43a14edbb1fa3918fb89195f6df91a) (const struct [i2c\_msg](structi2c__msg.md) \*msg) |
|  | Check if the current message includes a stop. |
| void | [i2c\_dump\_msgs\_rw](group__i2c__interface.md#ga2117056d6f6523627dda68f8ba32541e) (const struct [device](structdevice.md) \*dev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dump\_read) |
|  | Dump out an I2C message. |
| static void | [i2c\_dump\_msgs](group__i2c__interface.md#gab305de2c97bb9aa3b6a8346a0210e7db) (const struct [device](structdevice.md) \*dev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Dump out an I2C message, before it is executed. |
| static void | [i2c\_xfer\_stats](group__i2c__interface.md#gab2a84398805e2be7662e9ae9cd4f9299) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Updates the i2c stats for i2c transfers. |
| int | [i2c\_configure](group__i2c__interface.md#ga75326a6f38c011d35df9f3e72f2259e9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config) |
|  | Configure operation of a host controller. |
| int | [i2c\_get\_config](group__i2c__interface.md#ga6858e0f1a942b22964105135c334baed) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config) |
|  | Get configuration of a host controller. |
| int | [i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Perform data transfer to another I2C device in controller mode. |
| static int | [i2c\_transfer\_cb](group__i2c__interface.md#gaab152d5d68b6542019b77b244c239fee) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Perform data transfer to another I2C device in controller mode. |
| static int | [i2c\_transfer\_cb\_dt](group__i2c__interface.md#ga08618803640f5520e0e4af4c31b122f5) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Perform data transfer to another I2C device in master mode asynchronously. |
| static int | [i2c\_write\_read\_cb](group__i2c__interface.md#ga39d1aa15d2f0fd03fc7e6cbaae26048c) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read, [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Write then read data from an I2C device asynchronously. |
| static int | [i2c\_write\_read\_cb\_dt](group__i2c__interface.md#ga837a2fd46243940ebd86b08d9d656571) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read, [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Write then read data from an I2C device asynchronously. |
| static int | [i2c\_transfer\_signal](group__i2c__interface.md#gac02fcbebaef5368dbdae21407012e78e) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Perform data transfer to another I2C device in controller mode. |
| void | [i2c\_iodev\_submit\_fallback](group__i2c__interface.md#ga4e01759396817ca46244e6abd5186673) (const struct [device](structdevice.md) \*dev, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Fallback submit implementation. |
| static void | [i2c\_iodev\_submit](group__i2c__interface.md#ga1d6d1d28f56a9c7c8fde1e6eb056e128) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit request(s) to an I2C device with RTIO. |
| struct [rtio\_sqe](structrtio__sqe.md) \* | [i2c\_rtio\_copy](group__i2c__interface.md#ga1fc6344eba89f6121c61172698c19093) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Copy the i2c\_msgs into a set of RTIO requests. |
| static int | [i2c\_transfer\_dt](group__i2c__interface.md#ga8dce931e2dd637d811ff651062cec17b) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Perform data transfer to another I2C device in controller mode. |
| int | [i2c\_recover\_bus](group__i2c__interface.md#ga93117c531c39259d89ab69d52bbde85c) (const struct [device](structdevice.md) \*dev) |
|  | Recover the I2C bus. |
| static int | [i2c\_target\_register](group__i2c__interface.md#gaa47c3fde397188fa126dcaa4a6e85b47) (const struct [device](structdevice.md) \*dev, struct [i2c\_target\_config](structi2c__target__config.md) \*cfg) |
|  | Registers the provided config as Target device of a controller. |
| static int | [i2c\_target\_unregister](group__i2c__interface.md#ga11eada869173f6bd91db39c794dc8979) (const struct [device](structdevice.md) \*dev, struct [i2c\_target\_config](structi2c__target__config.md) \*cfg) |
|  | Unregisters the provided config as Target device. |
| int | [i2c\_target\_driver\_register](group__i2c__interface.md#ga1ba4520e0c2a3ef19fcc52ba091d97d4) (const struct [device](structdevice.md) \*dev) |
|  | Instructs the I2C Target device to register itself to the I2C Controller. |
| int | [i2c\_target\_driver\_unregister](group__i2c__interface.md#ga099580e56cfaf800e14f23066db70515) (const struct [device](structdevice.md) \*dev) |
|  | Instructs the I2C Target device to unregister itself from the I2C Controller. |
| static int | [i2c\_write](group__i2c__interface.md#ga2cc5f49493dce89e128ccbfa9d6149a0) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Write a set amount of data to an I2C device. |
| static int | [i2c\_write\_dt](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write a set amount of data to an I2C device. |
| static int | [i2c\_read](group__i2c__interface.md#ga935d1fdcbf9a40c9a673aa8977048ee7) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Read a set amount of data from an I2C device. |
| static int | [i2c\_read\_dt](group__i2c__interface.md#ga5cf80d20dca0d5f1d16e16c151f57ef6) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read a set amount of data from an I2C device. |
| static int | [i2c\_write\_read](group__i2c__interface.md#ga1273a9f8bdb002e0d6ece3a8c893a709) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read) |
|  | Write then read data from an I2C device. |
| static int | [i2c\_write\_read\_dt](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read) |
|  | Write then read data from an I2C device. |
| static int | [i2c\_burst\_read](group__i2c__interface.md#ga4bbb79898f53d0a2fad1bd302369ae9e) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read multiple bytes from an internal address of an I2C device. |
| static int | [i2c\_burst\_read\_dt](group__i2c__interface.md#ga9d2654bbf80f4d253532adaec8566fc3) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read multiple bytes from an internal address of an I2C device. |
| static int | [i2c\_burst\_write](group__i2c__interface.md#gaf995812f31e7bf1ea7f203905db13822) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write multiple bytes to an internal address of an I2C device. |
| static int | [i2c\_burst\_write\_dt](group__i2c__interface.md#ga0e590c99d3b9c1a7dd8174a318ee5a7d) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write multiple bytes to an internal address of an I2C device. |
| static int | [i2c\_reg\_read\_byte](group__i2c__interface.md#gaf8d1722ff4ebe97122293aef6ccf332a) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read internal register of an I2C device. |
| static int | [i2c\_reg\_read\_byte\_dt](group__i2c__interface.md#ga6fc14d75c41b8c8d9dd2f77c59533640) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read internal register of an I2C device. |
| static int | [i2c\_reg\_write\_byte](group__i2c__interface.md#ga687a0da74c22b299b66db8198c6fdcb1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write internal register of an I2C device. |
| static int | [i2c\_reg\_write\_byte\_dt](group__i2c__interface.md#ga664cd76bf4fae0dba848f5c284699a04) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write internal register of an I2C device. |
| static int | [i2c\_reg\_update\_byte](group__i2c__interface.md#gad07710d37bf6bd4fa6ccfe62be625eb4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Update internal register of an I2C device. |
| static int | [i2c\_reg\_update\_byte\_dt](group__i2c__interface.md#ga5000c5e49eabe712b5fd532d3842c3f5) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Update internal register of an I2C device. |

| Variables | |
| --- | --- |
| const struct [rtio\_iodev\_api](structrtio__iodev__api.md) | [i2c\_iodev\_api](group__i2c__interface.md#gaea8f7eeb3ed41c260d7a6c3cf078c3ec) |

## Detailed Description

Public APIs for the I2C drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c.h](drivers_2i2c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
