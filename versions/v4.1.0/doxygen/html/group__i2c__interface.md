---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__i2c__interface.html
original_path: doxygen/html/group__i2c__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I2C Interface

[Device Driver APIs](group__io__interfaces.md)

I2C Interface.
[More...](#details)

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
| #define | [I2C\_SPEED\_STANDARD](#ga5ca8c5fbb2caa99ab0b7007ce2c11633)   (0x1U) |
|  | I2C Standard Speed: 100 kHz. |
| #define | [I2C\_SPEED\_FAST](#gaef9d097ed2b58676498a33f3cf76f38d)   (0x2U) |
|  | I2C Fast Speed: 400 kHz. |
| #define | [I2C\_SPEED\_FAST\_PLUS](#ga9c867195c4a99615ed9c0011293a2155)   (0x3U) |
|  | I2C Fast Plus Speed: 1 MHz. |
| #define | [I2C\_SPEED\_HIGH](#gac7bce1bbfb422a123d3228e97e2cbb71)   (0x4U) |
|  | I2C High Speed: 3.4 MHz. |
| #define | [I2C\_SPEED\_ULTRA](#ga213468d14d1241632c957873cf2d9628)   (0x5U) |
|  | I2C Ultra Fast Speed: 5 MHz. |
| #define | [I2C\_SPEED\_DT](#gad38207f2e64b6ef3c08b17c8ccb3a836)   (0x7U) |
|  | Device Tree specified speed. |
| #define | [I2C\_SPEED\_SHIFT](#ga6d0aaaec30d1e64e1b4ad674423d131f)   (1U) |
| #define | [I2C\_SPEED\_SET](#ga6d64fdac5a2d9008e7856e670b3c4305)(speed) |
| #define | [I2C\_SPEED\_MASK](#gade41614d9cb3efd61b22eda9c1715e4c)   (0x7U << [I2C\_SPEED\_SHIFT](#ga6d0aaaec30d1e64e1b4ad674423d131f)) /\* 3 bits \*/ |
| #define | [I2C\_SPEED\_GET](#ga0eda328bb70285895d09154f9a828040)(cfg) |
| #define | [I2C\_ADDR\_10\_BITS](#ga66836d37196ce866681f506c44c8766d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Use 10-bit addressing. |
| #define | [I2C\_MODE\_CONTROLLER](#ga6b03c8a7668528e2902073ffaa1d3a13)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Peripheral to act as Controller. |
| #define | [I2C\_DT\_SPEC\_GET\_ON\_I3C](#ga6479e2c8f807fc8c92646a87d1dcca84)(node\_id) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree (on I3C bus). |
| #define | [I2C\_DT\_SPEC\_GET\_ON\_I2C](#gafa81ab3407e8a1da368b729b31471af8)(node\_id) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree (on I2C bus). |
| #define | [I2C\_DT\_SPEC\_GET](#gabb3ae5225cea677f3f3b36e4477ed045)(node\_id) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree. |
| #define | [I2C\_DT\_SPEC\_INST\_GET](#ga2197cbc5122f0d8b2e0788113bcb5963)(inst) |
|  | Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree instance. |
| #define | [I2C\_MSG\_WRITE](#gaf622d3c4aa1c832f90fff7200bb33732)   (0U << 0U) |
|  | Write message to I2C bus. |
| #define | [I2C\_MSG\_READ](#ga6c3042e882e6a817a6498b7a4e1f0a95)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Read message from I2C bus. |
| #define | [I2C\_MSG\_STOP](#gaad55262ad277ee60b786372c71f217aa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Send STOP after this message. |
| #define | [I2C\_MSG\_RESTART](#ga8c6cf7be2a04979fdb9d0b7dd9c4f831)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | RESTART I2C transaction for this message. |
| #define | [I2C\_MSG\_ADDR\_10\_BITS](#ga5569e8a3e4f6660928dfe443067c472c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Use 10-bit addressing for this message. |
| #define | [I2C\_TARGET\_FLAGS\_ADDR\_10\_BITS](#ga9031b418a053f4fe0ace72fea91dec3d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Target device responds to 10-bit addressing. |
| #define | [I2C\_DEVICE\_DT\_DEFINE](#ga47b9d476cc85d6f5b8081c73dd87064f)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with I2C specifics. |
| #define | [I2C\_DEVICE\_DT\_INST\_DEFINE](#gabfd94bccb99bd1a958cd8d7902b2072a)(inst, ...) |
|  | Like [I2C\_DEVICE\_DT\_DEFINE()](#ga47b9d476cc85d6f5b8081c73dd87064f) for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [I2C\_DT\_IODEV\_DEFINE](#ga304d3b906b5222a9b704f5b35641143d)(name, node\_id) |
|  | Define an iodev for a given dt node on the bus. |
| #define | [I2C\_IODEV\_DEFINE](#ga451d0877ad5f4c2e9601dc2db8644924)(name, \_bus, \_addr) |
|  | Define an iodev for a given i2c device on a bus. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc)) (const struct [device](structdevice.md) \*dev, int result, void \*data) |
|  | I2C callback for asynchronous transfer requests. |
| typedef int(\* | [i2c\_target\_write\_requested\_cb\_t](#ga4cd9be521a6c7d088f15b88400624e4e)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config) |
|  | Function called when a write to the device is initiated. |
| typedef int(\* | [i2c\_target\_write\_received\_cb\_t](#ga619db7eea1c4400adcbea5dddf5cf2c5)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Function called when a write to the device is continued. |
| typedef int(\* | [i2c\_target\_read\_requested\_cb\_t](#ga244264ecdbd51210728ee92dcbebbc87)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Function called when a read from the device is initiated. |
| typedef int(\* | [i2c\_target\_read\_processed\_cb\_t](#ga4cb0ae2cf41fc2105d1baa5e496e5dae)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Function called when a read from the device is continued. |
| typedef int(\* | [i2c\_target\_stop\_cb\_t](#ga3c898d0bef364461a3502037cf3d40b0)) (struct [i2c\_target\_config](structi2c__target__config.md) \*config) |
|  | Function called when a stop condition is observed after a start condition addressed to a particular device. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_is\_ready\_dt](#gafc6799ac7a95eaa8e186cbe6981b1548) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec) |
|  | Validate that I2C bus is ready. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_is\_read\_op](#ga99288e3e995f8cdaebcbd3a38d22b2dc) (const struct [i2c\_msg](structi2c__msg.md) \*msg) |
|  | Check if the current message is a read operation. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_is\_stop\_op](#ga3b43a14edbb1fa3918fb89195f6df91a) (const struct [i2c\_msg](structi2c__msg.md) \*msg) |
|  | Check if the current message includes a stop. |
| void | [i2c\_dump\_msgs\_rw](#ga2117056d6f6523627dda68f8ba32541e) (const struct [device](structdevice.md) \*dev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dump\_read) |
|  | Dump out an I2C message. |
| static void | [i2c\_dump\_msgs](#gab305de2c97bb9aa3b6a8346a0210e7db) (const struct [device](structdevice.md) \*dev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Dump out an I2C message, before it is executed. |
| static void | [i2c\_xfer\_stats](#gab2a84398805e2be7662e9ae9cd4f9299) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Updates the i2c stats for i2c transfers. |
| int | [i2c\_configure](#ga75326a6f38c011d35df9f3e72f2259e9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config) |
|  | Configure operation of a host controller. |
| int | [i2c\_get\_config](#ga6858e0f1a942b22964105135c334baed) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config) |
|  | Get configuration of a host controller. |
| int | [i2c\_transfer](#ga2958e6fe92ffb17851052d5c9a5c058e) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Perform data transfer to another I2C device in controller mode. |
| static int | [i2c\_transfer\_cb](#gaab152d5d68b6542019b77b244c239fee) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Perform data transfer to another I2C device in controller mode. |
| static int | [i2c\_transfer\_cb\_dt](#ga08618803640f5520e0e4af4c31b122f5) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Perform data transfer to another I2C device in master mode asynchronously. |
| static int | [i2c\_write\_read\_cb](#ga39d1aa15d2f0fd03fc7e6cbaae26048c) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read, [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Write then read data from an I2C device asynchronously. |
| static int | [i2c\_write\_read\_cb\_dt](#ga837a2fd46243940ebd86b08d9d656571) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read, [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata) |
|  | Write then read data from an I2C device asynchronously. |
| static int | [i2c\_transfer\_signal](#gac02fcbebaef5368dbdae21407012e78e) (const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Perform data transfer to another I2C device in controller mode. |
| void | [i2c\_iodev\_submit\_fallback](#ga4e01759396817ca46244e6abd5186673) (const struct [device](structdevice.md) \*dev, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Fallback submit implementation. |
| static void | [i2c\_iodev\_submit](#ga1d6d1d28f56a9c7c8fde1e6eb056e128) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit request(s) to an I2C device with RTIO. |
| struct [rtio\_sqe](structrtio__sqe.md) \* | [i2c\_rtio\_copy](#ga1fc6344eba89f6121c61172698c19093) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Copy the i2c\_msgs into a set of RTIO requests. |
| static int | [i2c\_transfer\_dt](#ga8dce931e2dd637d811ff651062cec17b) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Perform data transfer to another I2C device in controller mode. |
| int | [i2c\_recover\_bus](#ga93117c531c39259d89ab69d52bbde85c) (const struct [device](structdevice.md) \*dev) |
|  | Recover the I2C bus. |
| static int | [i2c\_target\_register](#gaa47c3fde397188fa126dcaa4a6e85b47) (const struct [device](structdevice.md) \*dev, struct [i2c\_target\_config](structi2c__target__config.md) \*cfg) |
|  | Registers the provided config as Target device of a controller. |
| static int | [i2c\_target\_unregister](#ga11eada869173f6bd91db39c794dc8979) (const struct [device](structdevice.md) \*dev, struct [i2c\_target\_config](structi2c__target__config.md) \*cfg) |
|  | Unregisters the provided config as Target device. |
| int | [i2c\_target\_driver\_register](#ga1ba4520e0c2a3ef19fcc52ba091d97d4) (const struct [device](structdevice.md) \*dev) |
|  | Instructs the I2C Target device to register itself to the I2C Controller. |
| int | [i2c\_target\_driver\_unregister](#ga099580e56cfaf800e14f23066db70515) (const struct [device](structdevice.md) \*dev) |
|  | Instructs the I2C Target device to unregister itself from the I2C Controller. |
| static int | [i2c\_write](#ga2cc5f49493dce89e128ccbfa9d6149a0) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Write a set amount of data to an I2C device. |
| static int | [i2c\_write\_dt](#ga2d17b714ba6ebe47d7bdfcb1cf97e44f) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write a set amount of data to an I2C device. |
| static int | [i2c\_read](#ga935d1fdcbf9a40c9a673aa8977048ee7) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Read a set amount of data from an I2C device. |
| static int | [i2c\_read\_dt](#ga5cf80d20dca0d5f1d16e16c151f57ef6) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read a set amount of data from an I2C device. |
| static int | [i2c\_write\_read](#ga1273a9f8bdb002e0d6ece3a8c893a709) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read) |
|  | Write then read data from an I2C device. |
| static int | [i2c\_write\_read\_dt](#ga301733586dcc2a353bdf149b49df5758) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read) |
|  | Write then read data from an I2C device. |
| static int | [i2c\_burst\_read](#ga4bbb79898f53d0a2fad1bd302369ae9e) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read multiple bytes from an internal address of an I2C device. |
| static int | [i2c\_burst\_read\_dt](#ga9d2654bbf80f4d253532adaec8566fc3) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read multiple bytes from an internal address of an I2C device. |
| static int | [i2c\_burst\_write](#gaf995812f31e7bf1ea7f203905db13822) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write multiple bytes to an internal address of an I2C device. |
| static int | [i2c\_burst\_write\_dt](#ga0e590c99d3b9c1a7dd8174a318ee5a7d) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write multiple bytes to an internal address of an I2C device. |
| static int | [i2c\_reg\_read\_byte](#gaf8d1722ff4ebe97122293aef6ccf332a) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read internal register of an I2C device. |
| static int | [i2c\_reg\_read\_byte\_dt](#ga6fc14d75c41b8c8d9dd2f77c59533640) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read internal register of an I2C device. |
| static int | [i2c\_reg\_write\_byte](#ga687a0da74c22b299b66db8198c6fdcb1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write internal register of an I2C device. |
| static int | [i2c\_reg\_write\_byte\_dt](#ga664cd76bf4fae0dba848f5c284699a04) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write internal register of an I2C device. |
| static int | [i2c\_reg\_update\_byte](#gad07710d37bf6bd4fa6ccfe62be625eb4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Update internal register of an I2C device. |
| static int | [i2c\_reg\_update\_byte\_dt](#ga5000c5e49eabe712b5fd532d3842c3f5) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Update internal register of an I2C device. |

| Variables | |
| --- | --- |
| const struct [rtio\_iodev\_api](structrtio__iodev__api.md) | [i2c\_iodev\_api](#gaea8f7eeb3ed41c260d7a6c3cf078c3ec) |

## Detailed Description

I2C Interface.

Since
:   1.0

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga66836d37196ce866681f506c44c8766d)I2C\_ADDR\_10\_BITS

| #define I2C\_ADDR\_10\_BITS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Use 10-bit addressing.

DEPRECATED - Use I2C\_MSG\_ADDR\_10\_BITS instead.

## [◆ ](#ga47b9d476cc85d6f5b8081c73dd87064f)I2C\_DEVICE\_DT\_DEFINE

| #define I2C\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | ... ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

Z\_I2C\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

Z\_I2C\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), \

&[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

pm, data, config, level, prio, api, \

&(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

\_\_VA\_ARGS\_\_)

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:185

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with I2C specifics.

Defines a device which implements the I2C API. May generate a custom [device\_state](structdevice__state.md "Runtime device dynamic structure (in RAM) per driver instance.") container struct and init\_fn wrapper when needed depending on I2C `CONFIG_I2C_STATS`.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Name of the init function of the driver. Can be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4). |
    | pm | PM device resources reference (NULL if device does not use PM). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#gabfd94bccb99bd1a958cd8d7902b2072a)I2C\_DEVICE\_DT\_INST\_DEFINE

| #define I2C\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

[I2C\_DEVICE\_DT\_DEFINE](#ga47b9d476cc85d6f5b8081c73dd87064f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

[I2C\_DEVICE\_DT\_DEFINE](#ga47b9d476cc85d6f5b8081c73dd87064f)

#define I2C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api,...)

Like DEVICE\_DT\_DEFINE() with I2C specifics.

**Definition** i2c.h:664

Like [I2C\_DEVICE\_DT\_DEFINE()](#ga47b9d476cc85d6f5b8081c73dd87064f) for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to [I2C\_DEVICE\_DT\_DEFINE()](#ga47b9d476cc85d6f5b8081c73dd87064f). |
    | --- | --- |
    | ... | other parameters as expected by [I2C\_DEVICE\_DT\_DEFINE()](#ga47b9d476cc85d6f5b8081c73dd87064f). |

## [◆ ](#ga304d3b906b5222a9b704f5b35641143d)I2C\_DT\_IODEV\_DEFINE

| #define I2C\_DT\_IODEV\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \_i2c\_dt\_spec\_##name = \

I2C\_DT\_SPEC\_GET(node\_id); \

RTIO\_IODEV\_DEFINE(name, &[i2c\_iodev\_api](#gaea8f7eeb3ed41c260d7a6c3cf078c3ec), (void \*)&\_i2c\_dt\_spec\_##name)

[i2c\_iodev\_api](#gaea8f7eeb3ed41c260d7a6c3cf078c3ec)

const struct rtio\_iodev\_api i2c\_iodev\_api

[i2c\_dt\_spec](structi2c__dt__spec.md)

Complete I2C DT information.

**Definition** i2c.h:77

Define an iodev for a given dt node on the bus.

These do not need to be shared globally but doing so will save a small amount of memory.

Parameters
:   | name | Symbolic name of the iodev to define |
    | --- | --- |
    | node\_id | Devicetree node identifier |

## [◆ ](#gabb3ae5225cea677f3f3b36e4477ed045)I2C\_DT\_SPEC\_GET

| #define I2C\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

{ \

COND\_CODE\_1([DT\_ON\_BUS](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)(node\_id, i3c), \

([I2C\_DT\_SPEC\_GET\_ON\_I3C](#ga6479e2c8f807fc8c92646a87d1dcca84)(node\_id)), \

([I2C\_DT\_SPEC\_GET\_ON\_I2C](#gafa81ab3407e8a1da368b729b31471af8)(node\_id))) \

}

[DT\_ON\_BUS](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)

#define DT\_ON\_BUS(node\_id, bus)

Is a node on a bus of a given type?

**Definition** devicetree.h:3891

[I2C\_DT\_SPEC\_GET\_ON\_I3C](#ga6479e2c8f807fc8c92646a87d1dcca84)

#define I2C\_DT\_SPEC\_GET\_ON\_I3C(node\_id)

Structure initializer for i2c\_dt\_spec from devicetree (on I3C bus).

**Definition** i2c.h:92

[I2C\_DT\_SPEC\_GET\_ON\_I2C](#gafa81ab3407e8a1da368b729b31471af8)

#define I2C\_DT\_SPEC\_GET\_ON\_I2C(node\_id)

Structure initializer for i2c\_dt\_spec from devicetree (on I2C bus).

**Definition** i2c.h:106

Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree.

This helper macro expands to a static initializer for a struct
[i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") by reading the relevant bus and address data from the devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the I2C device whose struct [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") to create an initializer for |
    | --- | --- |

## [◆ ](#gafa81ab3407e8a1da368b729b31471af8)I2C\_DT\_SPEC\_GET\_ON\_I2C

| #define I2C\_DT\_SPEC\_GET\_ON\_I2C | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.addr = [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id)

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:280

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3861

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2461

Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree (on I2C bus).

This helper macro expands to a static initializer for a struct
[i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") by reading the relevant bus and address data from the devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the I2C device whose struct [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") to create an initializer for |
    | --- | --- |

## [◆ ](#ga6479e2c8f807fc8c92646a87d1dcca84)I2C\_DT\_SPEC\_GET\_ON\_I3C

| #define I2C\_DT\_SPEC\_GET\_ON\_I3C | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.addr = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 0)

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:908

Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree (on I3C bus).

This helper macro expands to a static initializer for a struct
[i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") by reading the relevant bus and address data from the devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the I2C device whose struct [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") to create an initializer for |
    | --- | --- |

## [◆ ](#ga2197cbc5122f0d8b2e0788113bcb5963)I2C\_DT\_SPEC\_INST\_GET

| #define I2C\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

[I2C\_DT\_SPEC\_GET](#gabb3ae5225cea677f3f3b36e4477ed045)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[I2C\_DT\_SPEC\_GET](#gabb3ae5225cea677f3f3b36e4477ed045)

#define I2C\_DT\_SPEC\_GET(node\_id)

Structure initializer for i2c\_dt\_spec from devicetree.

**Definition** i2c.h:120

Structure initializer for [i2c\_dt\_spec](structi2c__dt__spec.md "Complete I2C DT information.") from devicetree instance.

This is equivalent to [I2C\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))](#gabb3ae5225cea677f3f3b36e4477ed045).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#ga451d0877ad5f4c2e9601dc2db8644924)I2C\_IODEV\_DEFINE

| #define I2C\_IODEV\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *\_bus*, |
|  |  |  | *\_addr* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \_i2c\_dt\_spec\_##name = { \

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)(\_bus), \

.addr = \_addr, \

}; \

RTIO\_IODEV\_DEFINE(name, &[i2c\_iodev\_api](#gaea8f7eeb3ed41c260d7a6c3cf078c3ec), (void \*)&\_i2c\_dt\_spec\_##name)

Define an iodev for a given i2c device on a bus.

These do not need to be shared globally but doing so will save a small amount of memory.

Parameters
:   | name | Symbolic name of the iodev to define |
    | --- | --- |
    | \_bus | Node ID for I2C bus |
    | \_addr | I2C target address |

## [◆ ](#ga6b03c8a7668528e2902073ffaa1d3a13)I2C\_MODE\_CONTROLLER

| #define I2C\_MODE\_CONTROLLER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Peripheral to act as Controller.

## [◆ ](#ga5569e8a3e4f6660928dfe443067c472c)I2C\_MSG\_ADDR\_10\_BITS

| #define I2C\_MSG\_ADDR\_10\_BITS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Use 10-bit addressing for this message.

Note
:   Not all SoC I2C implementations support this feature.

## [◆ ](#ga6c3042e882e6a817a6498b7a4e1f0a95)I2C\_MSG\_READ

| #define I2C\_MSG\_READ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Read message from I2C bus.

## [◆ ](#ga8c6cf7be2a04979fdb9d0b7dd9c4f831)I2C\_MSG\_RESTART

| #define I2C\_MSG\_RESTART   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

RESTART I2C transaction for this message.

Note
:   Not all I2C drivers have or require explicit support for this feature. Some drivers require this be present on a read message that follows a write, or vice-versa. Some drivers will merge adjacent fragments into a single transaction using this flag; some will not.

## [◆ ](#gaad55262ad277ee60b786372c71f217aa)I2C\_MSG\_STOP

| #define I2C\_MSG\_STOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Send STOP after this message.

## [◆ ](#gaf622d3c4aa1c832f90fff7200bb33732)I2C\_MSG\_WRITE

| #define I2C\_MSG\_WRITE   (0U << 0U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write message to I2C bus.

## [◆ ](#gad38207f2e64b6ef3c08b17c8ccb3a836)I2C\_SPEED\_DT

| #define I2C\_SPEED\_DT   (0x7U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Device Tree specified speed.

## [◆ ](#gaef9d097ed2b58676498a33f3cf76f38d)I2C\_SPEED\_FAST

| #define I2C\_SPEED\_FAST   (0x2U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

I2C Fast Speed: 400 kHz.

## [◆ ](#ga9c867195c4a99615ed9c0011293a2155)I2C\_SPEED\_FAST\_PLUS

| #define I2C\_SPEED\_FAST\_PLUS   (0x3U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

I2C Fast Plus Speed: 1 MHz.

## [◆ ](#ga0eda328bb70285895d09154f9a828040)I2C\_SPEED\_GET

| #define I2C\_SPEED\_GET | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

(((cfg) & [I2C\_SPEED\_MASK](#gade41614d9cb3efd61b22eda9c1715e4c)) \

>> [I2C\_SPEED\_SHIFT](#ga6d0aaaec30d1e64e1b4ad674423d131f))

[I2C\_SPEED\_SHIFT](#ga6d0aaaec30d1e64e1b4ad674423d131f)

#define I2C\_SPEED\_SHIFT

**Definition** i2c.h:58

[I2C\_SPEED\_MASK](#gade41614d9cb3efd61b22eda9c1715e4c)

#define I2C\_SPEED\_MASK

**Definition** i2c.h:61

## [◆ ](#gac7bce1bbfb422a123d3228e97e2cbb71)I2C\_SPEED\_HIGH

| #define I2C\_SPEED\_HIGH   (0x4U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

I2C High Speed: 3.4 MHz.

## [◆ ](#gade41614d9cb3efd61b22eda9c1715e4c)I2C\_SPEED\_MASK

| #define I2C\_SPEED\_MASK   (0x7U << [I2C\_SPEED\_SHIFT](#ga6d0aaaec30d1e64e1b4ad674423d131f)) /\* 3 bits \*/ |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

## [◆ ](#ga6d64fdac5a2d9008e7856e670b3c4305)I2C\_SPEED\_SET

| #define I2C\_SPEED\_SET | ( |  | *speed* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

**Value:**

(((speed) << [I2C\_SPEED\_SHIFT](#ga6d0aaaec30d1e64e1b4ad674423d131f)) \

& [I2C\_SPEED\_MASK](#gade41614d9cb3efd61b22eda9c1715e4c))

## [◆ ](#ga6d0aaaec30d1e64e1b4ad674423d131f)I2C\_SPEED\_SHIFT

| #define I2C\_SPEED\_SHIFT   (1U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

## [◆ ](#ga5ca8c5fbb2caa99ab0b7007ce2c11633)I2C\_SPEED\_STANDARD

| #define I2C\_SPEED\_STANDARD   (0x1U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

I2C Standard Speed: 100 kHz.

## [◆ ](#ga213468d14d1241632c957873cf2d9628)I2C\_SPEED\_ULTRA

| #define I2C\_SPEED\_ULTRA   (0x5U) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

I2C Ultra Fast Speed: 5 MHz.

## [◆ ](#ga9031b418a053f4fe0ace72fea91dec3d)I2C\_TARGET\_FLAGS\_ADDR\_10\_BITS

| #define I2C\_TARGET\_FLAGS\_ADDR\_10\_BITS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Target device responds to 10-bit addressing.

## Typedef Documentation

## [◆ ](#ga590293ec0d90d3fb0d8cbfee097798fc)i2c\_callback\_t

| typedef void(\* i2c\_callback\_t) (const struct [device](structdevice.md) \*dev, int result, void \*data) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

I2C callback for asynchronous transfer requests.

Parameters
:   | dev | I2C device which is notifying of transfer completion or error |
    | --- | --- |
    | result | Result code of the transfer request. 0 is success, -errno for failure. |
    | data | Transfer requester supplied data which is passed along to the callback. |

## [◆ ](#ga4cb0ae2cf41fc2105d1baa5e496e5dae)i2c\_target\_read\_processed\_cb\_t

| typedef int(\* i2c\_target\_read\_processed\_cb\_t) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Function called when a read from the device is continued.

This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device.

The value returned in `*val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

Parameters
:   | config | the configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |
    | val | pointer to storage for the next byte of data to return for the read request. |

Returns
:   0 if data has been provided, or a negative error code.

## [◆ ](#ga244264ecdbd51210728ee92dcbebbc87)i2c\_target\_read\_requested\_cb\_t

| typedef int(\* i2c\_target\_read\_requested\_cb\_t) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Function called when a read from the device is initiated.

This function is invoked by the controller when the bus completes a start condition for a read operation from the address associated with a particular device.

The value returned in `*val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

Parameters
:   | config | the configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |
    | val | pointer to storage for the first byte of data to return for the read request. |

Returns
:   0 if more data can be requested, or a negative error code.

## [◆ ](#ga3c898d0bef364461a3502037cf3d40b0)i2c\_target\_stop\_cb\_t

| typedef int(\* i2c\_target\_stop\_cb\_t) (struct [i2c\_target\_config](structi2c__target__config.md) \*config) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Function called when a stop condition is observed after a start condition addressed to a particular device.

This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device. After the function returns the controller shall enter a state where it is ready to react to new start conditions.

Parameters
:   | config | the configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |

Returns
:   Ignored.

## [◆ ](#ga619db7eea1c4400adcbea5dddf5cf2c5)i2c\_target\_write\_received\_cb\_t

| typedef int(\* i2c\_target\_write\_received\_cb\_t) (struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Function called when a write to the device is continued.

This function is invoked by the controller when it completes reception of a byte of data in an ongoing write operation to the device.

A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

Parameters
:   | config | the configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |
    | val | the byte received by the controller. |

Returns
:   0 if more data can be accepted, or a negative error code.

## [◆ ](#ga4cd9be521a6c7d088f15b88400624e4e)i2c\_target\_write\_requested\_cb\_t

| typedef int(\* i2c\_target\_write\_requested\_cb\_t) (struct [i2c\_target\_config](structi2c__target__config.md) \*config) |
| --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Function called when a write to the device is initiated.

This function is invoked by the controller when the bus completes a start condition for a write operation to the address associated with a particular device.

A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

Parameters
:   | config | the configuration structure associated with the device to which the operation is addressed. |
    | --- | --- |

Returns
:   0 if the write is accepted, or a negative error code.

## Function Documentation

## [◆ ](#ga4bbb79898f53d0a2fad1bd302369ae9e)i2c\_burst\_read()

| | int i2c\_burst\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dev\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Read multiple bytes from an internal address of an I2C device.

This routine reads multiple bytes from an internal address of an I2C device synchronously.

Instances of this may be replaced by [i2c\_write\_read()](#ga1273a9f8bdb002e0d6ece3a8c893a709).

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | dev\_addr | Address of the I2C device for reading. |
    | start\_addr | Internal address from which the data is being read. |
    | buf | Memory pool that stores the retrieved data. |
    | num\_bytes | Number of bytes being read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga9d2654bbf80f4d253532adaec8566fc3)i2c\_burst\_read\_dt()

| | int i2c\_burst\_read\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Read multiple bytes from an internal address of an I2C device.

This is equivalent to:

```
i2c_burst_read(spec->bus, spec->addr, start_addr, buf, num_bytes);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | start\_addr | Internal address from which the data is being read. |
    | buf | Memory pool that stores the retrieved data. |
    | num\_bytes | Number of bytes to read. |

Returns
:   a value from [i2c\_burst\_read()](#ga4bbb79898f53d0a2fad1bd302369ae9e)

## [◆ ](#gaf995812f31e7bf1ea7f203905db13822)i2c\_burst\_write()

| | int i2c\_burst\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dev\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_addr*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write multiple bytes to an internal address of an I2C device.

This routine writes multiple bytes to an internal address of an I2C device synchronously.

Warning
:   The combined write synthesized by this API may not be supported on all I2C devices. Uses of this API may be made more portable by replacing them with calls to [i2c\_write()](#ga2cc5f49493dce89e128ccbfa9d6149a0) passing a buffer containing the combined address and data.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | dev\_addr | Address of the I2C device for writing. |
    | start\_addr | Internal address to which the data is being written. |
    | buf | Memory pool from which the data is transferred. |
    | num\_bytes | Number of bytes being written. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga0e590c99d3b9c1a7dd8174a318ee5a7d)i2c\_burst\_write\_dt()

| | int i2c\_burst\_write\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_addr*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write multiple bytes to an internal address of an I2C device.

This is equivalent to:

```
i2c_burst_write(spec->bus, spec->addr, start_addr, buf, num_bytes);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | start\_addr | Internal address to which the data is being written. |
    | buf | Memory pool from which the data is transferred. |
    | num\_bytes | Number of bytes being written. |

Returns
:   a value from [i2c\_burst\_write()](#gaf995812f31e7bf1ea7f203905db13822)

## [◆ ](#ga75326a6f38c011d35df9f3e72f2259e9)i2c\_configure()

| int i2c\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_config* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Configure operation of a host controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_config | Bit-packed 32-bit value to the device runtime configuration for the I2C controller. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |

## [◆ ](#gab305de2c97bb9aa3b6a8346a0210e7db)i2c\_dump\_msgs()

| | void i2c\_dump\_msgs | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Dump out an I2C message, before it is executed.

This is equivalent to:

```
i2c_dump_msgs_rw(dev, msgs, num_msgs, addr, false);
```

The read messages' data isn't dumped.

Parameters
:   | dev | Target for the messages being sent. Its name will be printed in the log. |
    | --- | --- |
    | msgs | Array of messages to dump. |
    | num\_msgs | Number of messages to dump. |
    | addr | Address of the I2C target device. |

## [◆ ](#ga2117056d6f6523627dda68f8ba32541e)i2c\_dump\_msgs\_rw()

| void i2c\_dump\_msgs\_rw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *dump\_read* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Dump out an I2C message.

Dumps out a list of I2C messages. For any that are writes (W), the data is displayed in hex. Setting dump\_read will dump the data for read messages too, which only makes sense when called after the messages have been processed.

It looks something like this (with name "testing"):

D: I2C msg: testing, addr=56

D: W len=01: 06

D: W len=0e:

D: contents:

D: 00 01 02 03 04 05 06 07 |........

D: 08 09 0a 0b 0c 0[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) |......

D: W len=01: 0f

D: R len=01: 6c

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

Parameters
:   | dev | Target for the messages being sent. Its name will be printed in the log. |
    | --- | --- |
    | msgs | Array of messages to dump. |
    | num\_msgs | Number of messages to dump. |
    | addr | Address of the I2C target device. |
    | dump\_read | Dump data from I2C reads, otherwise only writes have data dumped. |

## [◆ ](#ga6858e0f1a942b22964105135c334baed)i2c\_get\_config()

| int i2c\_get\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *dev\_config* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Get configuration of a host controller.

This routine provides a way to get current configuration. It is allowed to call the function before i2c\_configure, because some I2C ports can be configured during init process. However, if the I2C port is not configured, i2c\_get\_config returns an error.

i2c\_get\_config can return cached config or probe hardware, but it has to be up to date with current configuration.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_config | Pointer to return bit-packed 32-bit value of the I2C controller configuration. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ERANGE | Configured I2C frequency is invalid. |
    | -ENOSYS | If get config is not implemented |

## [◆ ](#ga1d6d1d28f56a9c7c8fde1e6eb056e128)i2c\_iodev\_submit()

| | void i2c\_iodev\_submit | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Submit request(s) to an I2C device with RTIO.

Parameters
:   | iodev\_sqe | Prepared submissions queue entry connected to an iodev defined by I2C\_DT\_IODEV\_DEFINE. |
    | --- | --- |

## [◆ ](#ga4e01759396817ca46244e6abd5186673)i2c\_iodev\_submit\_fallback()

| void i2c\_iodev\_submit\_fallback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Fallback submit implementation.

This implementation will schedule a blocking I2C transaction on the bus via the RTIO work queue. It is only used if the I2C driver did not implement the iodev\_submit function.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver. |
    | --- | --- |
    | iodev\_sqe | Prepared submissions queue entry connected to an iodev defined by I2C\_DT\_IODEV\_DEFINE. |

## [◆ ](#ga99288e3e995f8cdaebcbd3a38d22b2dc)i2c\_is\_read\_op()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i2c\_is\_read\_op | ( | const struct [i2c\_msg](structi2c__msg.md) \* | *msg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Check if the current message is a read operation.

Parameters
:   | msg | The message to check |
    | --- | --- |

Returns
:   true if the I2C message is a read operation
:   false if the I2C message is a write operation

## [◆ ](#gafc6799ac7a95eaa8e186cbe6981b1548)i2c\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i2c\_is\_ready\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Validate that I2C bus is ready.

Parameters
:   | spec | I2C specification from devicetree |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the I2C bus is ready for use. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the I2C bus is not ready for use. |

## [◆ ](#ga3b43a14edbb1fa3918fb89195f6df91a)i2c\_is\_stop\_op()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i2c\_is\_stop\_op | ( | const struct [i2c\_msg](structi2c__msg.md) \* | *msg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Check if the current message includes a stop.

Parameters
:   | msg | The message to check |
    | --- | --- |

Returns
:   true if the I2C message includes a stop
:   false if the I2C message includes a stop

## [◆ ](#ga935d1fdcbf9a40c9a673aa8977048ee7)i2c\_read()

| | int i2c\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Read a set amount of data from an I2C device.

This routine reads a set amount of data synchronously.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | buf | Memory pool that stores the retrieved data. |
    | num\_bytes | Number of bytes to read. |
    | addr | Address of the I2C device being read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga5cf80d20dca0d5f1d16e16c151f57ef6)i2c\_read\_dt()

| | int i2c\_read\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Read a set amount of data from an I2C device.

This is equivalent to:

```
i2c_read(spec->bus, buf, num_bytes, spec->addr);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | buf | Memory pool that stores the retrieved data. |
    | num\_bytes | Number of bytes to read. |

Returns
:   a value from [i2c\_read()](#ga935d1fdcbf9a40c9a673aa8977048ee7)

## [◆ ](#ga93117c531c39259d89ab69d52bbde85c)i2c\_recover\_bus()

| int i2c\_recover\_bus | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Recover the I2C bus.

Attempt to recover the I2C bus.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EBUSY | If bus is not clear after recovery attempt. |
    | -EIO | General input / output error. |
    | -ENOSYS | If bus recovery is not implemented |

## [◆ ](#gaf8d1722ff4ebe97122293aef6ccf332a)i2c\_reg\_read\_byte()

| | int i2c\_reg\_read\_byte | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dev\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Read internal register of an I2C device.

This routine reads the value of an 8-bit internal register of an I2C device synchronously.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | dev\_addr | Address of the I2C device for reading. |
    | reg\_addr | Address of the internal register being read. |
    | value | Memory pool that stores the retrieved register value. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga6fc14d75c41b8c8d9dd2f77c59533640)i2c\_reg\_read\_byte\_dt()

| | int i2c\_reg\_read\_byte\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Read internal register of an I2C device.

This is equivalent to:

```
i2c_reg_read_byte(spec->bus, spec->addr, reg_addr, value);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | reg\_addr | Address of the internal register being read. |
    | value | Memory pool that stores the retrieved register value. |

Returns
:   a value from [i2c\_reg\_read\_byte()](#gaf8d1722ff4ebe97122293aef6ccf332a)

## [◆ ](#gad07710d37bf6bd4fa6ccfe62be625eb4)i2c\_reg\_update\_byte()

| | int i2c\_reg\_update\_byte | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dev\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Update internal register of an I2C device.

This routine updates the value of a set of bits from an 8-bit internal register of an I2C device synchronously.

Note
:   If the calculated new register value matches the value that was read this function will not generate a write operation.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | dev\_addr | Address of the I2C device for updating. |
    | reg\_addr | Address of the internal register being updated. |
    | mask | Bitmask for updating internal register. |
    | value | Value for updating internal register. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga5000c5e49eabe712b5fd532d3842c3f5)i2c\_reg\_update\_byte\_dt()

| | int i2c\_reg\_update\_byte\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Update internal register of an I2C device.

This is equivalent to:

```
i2c_reg_update_byte(spec->bus, spec->addr, reg_addr, mask, value);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | reg\_addr | Address of the internal register being updated. |
    | mask | Bitmask for updating internal register. |
    | value | Value for updating internal register. |

Returns
:   a value from [i2c\_reg\_update\_byte()](#gad07710d37bf6bd4fa6ccfe62be625eb4)

## [◆ ](#ga687a0da74c22b299b66db8198c6fdcb1)i2c\_reg\_write\_byte()

| | int i2c\_reg\_write\_byte | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dev\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write internal register of an I2C device.

This routine writes a value to an 8-bit internal register of an I2C device synchronously.

Note
:   This function internally combines the register and value into a single bus transaction.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | dev\_addr | Address of the I2C device for writing. |
    | reg\_addr | Address of the internal register being written. |
    | value | Value to be written to internal register. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga664cd76bf4fae0dba848f5c284699a04)i2c\_reg\_write\_byte\_dt()

| | int i2c\_reg\_write\_byte\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write internal register of an I2C device.

This is equivalent to:

```
i2c_reg_write_byte(spec->bus, spec->addr, reg_addr, value);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | reg\_addr | Address of the internal register being written. |
    | value | Value to be written to internal register. |

Returns
:   a value from [i2c\_reg\_write\_byte()](#ga687a0da74c22b299b66db8198c6fdcb1)

## [◆ ](#ga1fc6344eba89f6121c61172698c19093)i2c\_rtio\_copy()

| struct [rtio\_sqe](structrtio__sqe.md) \* i2c\_rtio\_copy | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, |
|  |  | const struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Copy the i2c\_msgs into a set of RTIO requests.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | iodev | RTIO IODev to target for the submissions |
    | msgs | Array of messages |
    | num\_msgs | Number of i2c msgs in array |

Return values
:   | sqe | Last submission in the queue added |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | Not enough memory in the context to copy the requests |

## [◆ ](#ga1ba4520e0c2a3ef19fcc52ba091d97d4)i2c\_target\_driver\_register()

| int i2c\_target\_driver\_register | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Instructs the I2C Target device to register itself to the I2C Controller.

This routine instructs the I2C Target device to register itself to the I2C Controller via its parent controller's [i2c\_target\_register()](#gaa47c3fde397188fa126dcaa4a6e85b47) API.

Parameters
:   | dev | Pointer to the device structure for the I2C target device (not itself an I2C controller). |
    | --- | --- |

Return values
:   | 0 | Is successful |
    | --- | --- |
    | -EINVAL | If parameters are invalid |
    | -EIO | General input / output error. |

## [◆ ](#ga099580e56cfaf800e14f23066db70515)i2c\_target\_driver\_unregister()

| int i2c\_target\_driver\_unregister | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Instructs the I2C Target device to unregister itself from the I2C Controller.

This routine instructs the I2C Target device to unregister itself from the I2C Controller via its parent controller's [i2c\_target\_register()](#gaa47c3fde397188fa126dcaa4a6e85b47) API.

Parameters
:   | dev | Pointer to the device structure for the I2C target device (not itself an I2C controller). |
    | --- | --- |

Return values
:   | 0 | Is successful |
    | --- | --- |
    | -EINVAL | If parameters are invalid |

## [◆ ](#gaa47c3fde397188fa126dcaa4a6e85b47)i2c\_target\_register()

| | int i2c\_target\_register | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i2c\_target\_config](structi2c__target__config.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Registers the provided config as Target device of a controller.

Enable I2C target mode for the 'dev' I2C bus driver using the provided 'config' struct containing the functions and parameters to send bus events. The I2C target will be registered at the address provided as 'address' struct member. Addressing mode - 7 or 10 bit - depends on the 'flags' struct member. Any I2C bus events related to the target mode will be passed onto I2C target device driver via a set of callback functions provided in the 'callbacks' struct member.

Most of the existing hardware allows simultaneous support for controller and target mode. This is however not guaranteed.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in target mode. |
    | --- | --- |
    | cfg | Config struct with functions and parameters used by the I2C driver to send bus events |

Return values
:   | 0 | Is successful |
    | --- | --- |
    | -EINVAL | If parameters are invalid |
    | -EIO | General input / output error. |
    | -ENOSYS | If target mode is not implemented |

## [◆ ](#ga11eada869173f6bd91db39c794dc8979)i2c\_target\_unregister()

| | int i2c\_target\_unregister | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i2c\_target\_config](structi2c__target__config.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Unregisters the provided config as Target device.

This routine disables I2C target mode for the 'dev' I2C bus driver using the provided 'config' struct containing the functions and parameters to send bus events.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in target mode. |
    | --- | --- |
    | cfg | Config struct with functions and parameters used by the I2C driver to send bus events |

Return values
:   | 0 | Is successful |
    | --- | --- |
    | -EINVAL | If parameters are invalid |
    | -ENOSYS | If target mode is not implemented |

## [◆ ](#ga2958e6fe92ffb17851052d5c9a5c058e)i2c\_transfer()

| int i2c\_transfer | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* ) |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Perform data transfer to another I2C device in controller mode.

This routine provides a generic interface to perform data transfer to another I2C device synchronously. Use [i2c\_read()](#ga935d1fdcbf9a40c9a673aa8977048ee7)/i2c\_write() for simple read or write.

The array of message *msgs* must not be NULL. The number of message *num\_msgs* may be zero,in which case no transfer occurs.

Note
:   Not all scatter/gather transactions can be supported by all drivers. As an example, a gather write (multiple consecutive [i2c\_msg](structi2c__msg.md "One I2C Message.") buffers all configured for [I2C\_MSG\_WRITE](#gaf622d3c4aa1c832f90fff7200bb33732)) may be packed into a single transaction by some drivers, but others may emit each fragment as a distinct write transaction, which will not produce the same behavior. See the documentation of struct [i2c\_msg](structi2c__msg.md "One I2C Message.") for limitations on support for multi-message bus transactions.
:   The last message in the scatter/gather transaction implies a STOP whether or not it is explicitly set. This ensures the bus is in a good state for the next transaction which may be from a different call context.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | msgs | Array of messages to transfer. |
    | num\_msgs | Number of messages to transfer. |
    | addr | Address of the I2C target device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#gaab152d5d68b6542019b77b244c239fee)i2c\_transfer\_cb()

| | int i2c\_transfer\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, | |  |  | [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) | *cb*, | |  |  | void \* | *userdata* ) | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Perform data transfer to another I2C device in controller mode.

This routine provides a generic interface to perform data transfer to another I2C device asynchronously with a callback completion.

See also
:   [i2c\_transfer()](#ga2958e6fe92ffb17851052d5c9a5c058e)

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | msgs | Array of messages to transfer, must live until callback completes. |
    | num\_msgs | Number of messages to transfer. |
    | addr | Address of the I2C target device. |
    | cb | Function pointer for completion callback. |
    | userdata | Userdata passed to callback. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If transfer async is not implemented |
    | -EWOULDBLOCK | If the device is temporarily busy doing another transfer |

## [◆ ](#ga08618803640f5520e0e4af4c31b122f5)i2c\_transfer\_cb\_dt()

| | int i2c\_transfer\_cb\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, | |  |  | [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) | *cb*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Perform data transfer to another I2C device in master mode asynchronously.

This is equivalent to:

```
i2c_transfer_cb(spec->bus, msgs, num_msgs, spec->addr, cb, userdata);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | msgs | Array of messages to transfer. |
    | num\_msgs | Number of messages to transfer. |
    | cb | Function pointer for completion callback. |
    | userdata | Userdata passed to callback. |

Returns
:   a value from [i2c\_transfer\_cb()](#gaab152d5d68b6542019b77b244c239fee)

## [◆ ](#ga8dce931e2dd637d811ff651062cec17b)i2c\_transfer\_dt()

| | int i2c\_transfer\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Perform data transfer to another I2C device in controller mode.

This is equivalent to:

```
i2c_transfer(spec->bus, msgs, num_msgs, spec->addr);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | msgs | Array of messages to transfer. |
    | num\_msgs | Number of messages to transfer. |

Returns
:   a value from [i2c\_transfer()](#ga2958e6fe92ffb17851052d5c9a5c058e)

## [◆ ](#gac02fcbebaef5368dbdae21407012e78e)i2c\_transfer\_signal()

| | int i2c\_transfer\_signal | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Perform data transfer to another I2C device in controller mode.

This routine provides a generic interface to perform data transfer to another I2C device asynchronously with a [k\_poll\_signal](structk__poll__signal.md) completion.

See also
:   [i2c\_transfer\_cb()](#gaab152d5d68b6542019b77b244c239fee)

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | msgs | Array of messages to transfer, must live until callback completes. |
    | num\_msgs | Number of messages to transfer. |
    | addr | Address of the I2C target device. |
    | sig | Signal to notify of transfer completion. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If transfer async is not implemented |
    | -EWOULDBLOCK | If the device is temporarily busy doing another transfer |

## [◆ ](#ga2cc5f49493dce89e128ccbfa9d6149a0)i2c\_write()

| | int i2c\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write a set amount of data to an I2C device.

This routine writes a set amount of data synchronously.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | buf | Memory pool from which the data is transferred. |
    | num\_bytes | Number of bytes to write. |
    | addr | Address to the target I2C device for writing. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga2d17b714ba6ebe47d7bdfcb1cf97e44f)i2c\_write\_dt()

| | int i2c\_write\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write a set amount of data to an I2C device.

This is equivalent to:

```
i2c_write(spec->bus, buf, num_bytes, spec->addr);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | buf | Memory pool from which the data is transferred. |
    | num\_bytes | Number of bytes to write. |

Returns
:   a value from [i2c\_write()](#ga2cc5f49493dce89e128ccbfa9d6149a0)

## [◆ ](#ga1273a9f8bdb002e0d6ece3a8c893a709)i2c\_write\_read()

| | int i2c\_write\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, | |  |  | const void \* | *write\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_write*, | |  |  | void \* | *read\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_read* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write then read data from an I2C device.

This supports the common operation "this is what I want", "now give
it to me" transaction pair through a combined write-then-read bus transaction.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | addr | Address of the I2C device |
    | write\_buf | Pointer to the data to be written |
    | num\_write | Number of bytes to write |
    | read\_buf | Pointer to storage for read data |
    | num\_read | Number of bytes to read |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | on error. |

## [◆ ](#ga39d1aa15d2f0fd03fc7e6cbaae26048c)i2c\_write\_read\_cb()

| | int i2c\_write\_read\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, | |  |  | const void \* | *write\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_write*, | |  |  | void \* | *read\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_read*, | |  |  | [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) | *cb*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write then read data from an I2C device asynchronously.

This supports the common operation "this is what I want", "now give
it to me" transaction pair through a combined write-then-read bus transaction but using i2c\_transfer\_cb. This helper function expects caller to pass a message pointer with 2 and only 2 size.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in master mode. |
    | --- | --- |
    | msgs | Array of messages to transfer. |
    | num\_msgs | Number of messages to transfer. |
    | addr | Address of the I2C device |
    | write\_buf | Pointer to the data to be written |
    | num\_write | Number of bytes to write |
    | read\_buf | Pointer to storage for read data |
    | num\_read | Number of bytes to read |
    | cb | Function pointer for completion callback. |
    | userdata | Userdata passed to callback. |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | on error. |

## [◆ ](#ga837a2fd46243940ebd86b08d9d656571)i2c\_write\_read\_cb\_dt()

| | int i2c\_write\_read\_cb\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, | |  |  | const void \* | *write\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_write*, | |  |  | void \* | *read\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_read*, | |  |  | [i2c\_callback\_t](#ga590293ec0d90d3fb0d8cbfee097798fc) | *cb*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write then read data from an I2C device asynchronously.

This is equivalent to:

```
i2c_write_read_cb(spec->bus, msgs, num_msgs,
               spec->addr, write_buf,
               num_write, read_buf, num_read);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | msgs | Array of messages to transfer. |
    | num\_msgs | Number of messages to transfer. |
    | write\_buf | Pointer to the data to be written |
    | num\_write | Number of bytes to write |
    | read\_buf | Pointer to storage for read data |
    | num\_read | Number of bytes to read |
    | cb | Function pointer for completion callback. |
    | userdata | Userdata passed to callback. |

Returns
:   a value from [i2c\_write\_read\_cb()](#ga39d1aa15d2f0fd03fc7e6cbaae26048c)

## [◆ ](#ga301733586dcc2a353bdf149b49df5758)i2c\_write\_read\_dt()

| | int i2c\_write\_read\_dt | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const void \* | *write\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_write*, | |  |  | void \* | *read\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_read* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Write then read data from an I2C device.

This is equivalent to:

```
i2c_write_read(spec->bus, spec->addr,
               write_buf, num_write,
               read_buf, num_read);
```

Parameters
:   | spec | I2C specification from devicetree. |
    | --- | --- |
    | write\_buf | Pointer to the data to be written |
    | num\_write | Number of bytes to write |
    | read\_buf | Pointer to storage for read data |
    | num\_read | Number of bytes to read |

Returns
:   a value from [i2c\_write\_read()](#ga1273a9f8bdb002e0d6ece3a8c893a709)

## [◆ ](#gab2a84398805e2be7662e9ae9cd4f9299)i2c\_xfer\_stats()

| | void i2c\_xfer\_stats | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

Updates the i2c stats for i2c transfers.

Parameters
:   | dev | I2C device to update stats for |
    | --- | --- |
    | msgs | Array of struct [i2c\_msg](structi2c__msg.md "One I2C Message.") |
    | num\_msgs | Number of i2c\_msgs |

## Variable Documentation

## [◆ ](#gaea8f7eeb3ed41c260d7a6c3cf078c3ec)i2c\_iodev\_api

| | const struct [rtio\_iodev\_api](structrtio__iodev__api.md) i2c\_iodev\_api | | --- | | extern |
| --- | --- | --- |

`#include <[i2c.h](drivers_2i2c_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
