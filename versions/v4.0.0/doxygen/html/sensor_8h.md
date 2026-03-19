---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sensor_8h.html
original_path: doxygen/html/sensor_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor.h File Reference

Public APIs for the sensor driver.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/sensor_data_types.h](sensor__data__types_8h_source.md)>`  
`#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h_source.md)>`  
`#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <zephyr/syscalls/sensor.h>`

[Go to the source code of this file.](sensor_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sensor\_value](structsensor__value.md) |
|  | Representation of a sensor readout value. [More...](structsensor__value.md#details) |
| struct | [sensor\_trigger](structsensor__trigger.md) |
|  | Sensor trigger spec. [More...](structsensor__trigger.md#details) |
| struct | [sensor\_chan\_spec](structsensor__chan__spec.md) |
|  | Sensor Channel Specification. [More...](structsensor__chan__spec.md#details) |
| struct | [sensor\_decoder\_api](structsensor__decoder__api.md) |
|  | Decodes a single raw data buffer. [More...](structsensor__decoder__api.md#details) |
| struct | [sensor\_decode\_context](structsensor__decode__context.md) |
|  | Used for iterating over the data frames via the [sensor\_decoder\_api](structsensor__decoder__api.md "Decodes a single raw data buffer."). [More...](structsensor__decode__context.md#details) |
| struct | [sensor\_stream\_trigger](structsensor__stream__trigger.md) |
| struct | [sensor\_read\_config](structsensor__read__config.md) |
| struct | [sensor\_driver\_api](structsensor__driver__api.md) |
| struct | [sensor\_data\_generic\_header](structsensor__data__generic__header.md) |

| Macros | |
| --- | --- |
| #define | [SENSOR\_DECODE\_CONTEXT\_INIT](group__sensor__interface.md#gae69ec503df53d2d5ee417e481f9ac9ea)(decoder\_, buffer\_, channel\_type\_, channel\_index\_) |
|  | Initialize a [sensor\_decode\_context](structsensor__decode__context.md "Used for iterating over the data frames via the sensor_decoder_api."). |
| #define | [SENSOR\_STREAM\_TRIGGER\_PREP](group__sensor__interface.md#ga9b7b0db322121d220b126d2b5bb7eb73)(\_trigger, \_opt) |
| #define | [SENSOR\_DT\_READ\_IODEV](group__sensor__interface.md#ga0cc1ee28114557e9e00257071c7dfa9f)(name, dt\_node, ...) |
|  | Define a reading instance of a sensor. |
| #define | [SENSOR\_DT\_STREAM\_IODEV](group__sensor__interface.md#ga35211c4d908a26f98b1f8d925a9b1374)(name, dt\_node, ...) |
|  | Define a stream instance of a sensor. |
| #define | [SENSOR\_CHANNEL\_3\_AXIS](group__sensor__interface.md#ga32f679a4004b5707b2de00eb580d0930)(chan) |
|  | checks if a given channel is a 3-axis channel |
| #define | [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)   9806650LL |
|  | The value of gravitational constant in micro m/s^2. |
| #define | [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33)   3141592LL |
|  | The value of constant PI in micros. |
| #define | [SENSOR\_INFO\_DEFINE](group__sensor__interface.md#ga7467206da76c3704d2e491d1b1c0973a)(name, ...) |
| #define | [SENSOR\_INFO\_DT\_DEFINE](group__sensor__interface.md#ga9e6acbc580e9223bfb86ee8919cdc778)(node\_id) |
| #define | [SENSOR\_DEVICE\_DT\_DEFINE](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c)(node\_id, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with sensor specifics. |
| #define | [SENSOR\_DEVICE\_DT\_INST\_DEFINE](group__sensor__interface.md#ga284dc3b9018f14161dc0a2b6bed9a37e)(inst, ...) |
|  | Like [SENSOR\_DEVICE\_DT\_DEFINE()](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c "Like DEVICE_DT_DEFINE() with sensor specifics.") for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [SENSOR\_DECODER\_NAME](#a8d3434eb5860c2f2e6fe36b4de920c8c)() |
|  | Get the decoder name for the current driver. |
| #define | [SENSOR\_DECODER\_DT\_GET](#a82da2432981c593ed638a21c51fb0873)(node\_id) |
|  | Statically get the decoder for a given node. |
| #define | [SENSOR\_DECODER\_API\_DT\_DEFINE](#a78ad4b76be4a6f5347ba82b7db43b7c2)() |
|  | Define a decoder API. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902)) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trigger) |
|  | Callback API upon firing of a trigger. |
| typedef int(\* | [sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr, const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Callback API upon setting a sensor's attributes. |
| typedef int(\* | [sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Callback API upon getting a sensor's attributes. |
| typedef int(\* | [sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4)) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trig, [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler) |
|  | Callback API for setting a sensor's trigger and handler. |
| typedef int(\* | [sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan) |
|  | Callback API for fetching data from a sensor. |
| typedef int(\* | [sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Callback API for getting a reading from a sensor. |
| typedef int(\* | [sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42)) (const struct [device](structdevice.md) \*dev, const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*api) |
|  | Get the decoder associate with the given device. |
| typedef void(\* | [sensor\_submit\_t](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981)) (const struct [device](structdevice.md) \*sensor, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*sqe) |
| typedef void(\* | [sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462)) (int result, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len, void \*userdata) |
|  | Callback function used with the helper processing function. |

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) {     [SENSOR\_CHAN\_ACCEL\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c) , [SENSOR\_CHAN\_ACCEL\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8) , [SENSOR\_CHAN\_ACCEL\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f) , [SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9) ,     [SENSOR\_CHAN\_GYRO\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015) , [SENSOR\_CHAN\_GYRO\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847) , [SENSOR\_CHAN\_GYRO\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39) , [SENSOR\_CHAN\_GYRO\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e) ,     [SENSOR\_CHAN\_MAGN\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240) , [SENSOR\_CHAN\_MAGN\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942) , [SENSOR\_CHAN\_MAGN\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61) , [SENSOR\_CHAN\_MAGN\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32) ,     [SENSOR\_CHAN\_DIE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1) , [SENSOR\_CHAN\_AMBIENT\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c) , [SENSOR\_CHAN\_PRESS](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9) , [SENSOR\_CHAN\_PROX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774) ,     [SENSOR\_CHAN\_HUMIDITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042) , [SENSOR\_CHAN\_LIGHT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d) , [SENSOR\_CHAN\_IR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c) , [SENSOR\_CHAN\_RED](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa) ,     [SENSOR\_CHAN\_GREEN](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378) , [SENSOR\_CHAN\_BLUE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5) , [SENSOR\_CHAN\_ALTITUDE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512) , [SENSOR\_CHAN\_PM\_1\_0](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815) ,     [SENSOR\_CHAN\_PM\_2\_5](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945) , [SENSOR\_CHAN\_PM\_10](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225) , [SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08) , [SENSOR\_CHAN\_CO2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133) ,     [SENSOR\_CHAN\_O2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9) , [SENSOR\_CHAN\_VOC](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e) , [SENSOR\_CHAN\_GAS\_RES](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01) , [SENSOR\_CHAN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d) ,     [SENSOR\_CHAN\_VSHUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9) , [SENSOR\_CHAN\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950) , [SENSOR\_CHAN\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177) , [SENSOR\_CHAN\_RESISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b) ,     [SENSOR\_CHAN\_ROTATION](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf) , [SENSOR\_CHAN\_POS\_DX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517) , [SENSOR\_CHAN\_POS\_DY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76) , [SENSOR\_CHAN\_POS\_DZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9) ,     [SENSOR\_CHAN\_POS\_DXYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740) , [SENSOR\_CHAN\_RPM](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1) , [SENSOR\_CHAN\_GAUGE\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d) , [SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8) ,     [SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8) , [SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf) , [SENSOR\_CHAN\_GAUGE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214) , [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139) ,     [SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649) , [SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad) , [SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a) , [SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8) ,     [SENSOR\_CHAN\_GAUGE\_AVG\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228) , [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6) , [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65) , [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb) ,     [SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46) , [SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0) , [SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf) , [SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f) ,     [SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c) , [SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303) , [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) = SENSOR\_CHAN\_COMMON\_COUNT , [SENSOR\_CHAN\_MAX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) = INT16\_MAX   } |
|  | Sensor channels. [More...](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) |
| enum | [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) {     [SENSOR\_TRIG\_TIMER](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023) , [SENSOR\_TRIG\_DATA\_READY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f) , [SENSOR\_TRIG\_DELTA](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855) , [SENSOR\_TRIG\_NEAR\_FAR](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5) ,     [SENSOR\_TRIG\_THRESHOLD](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606) , [SENSOR\_TRIG\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d) , [SENSOR\_TRIG\_DOUBLE\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef) , [SENSOR\_TRIG\_FREEFALL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c) ,     [SENSOR\_TRIG\_MOTION](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276) , [SENSOR\_TRIG\_STATIONARY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d) , [SENSOR\_TRIG\_FIFO\_WATERMARK](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4) , [SENSOR\_TRIG\_FIFO\_FULL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c) ,     [SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5) , [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) = SENSOR\_TRIG\_COMMON\_COUNT , [SENSOR\_TRIG\_MAX](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) = INT16\_MAX   } |
|  | Sensor trigger types. [More...](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) |
| enum | [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) {     [SENSOR\_ATTR\_SAMPLING\_FREQUENCY](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291) , [SENSOR\_ATTR\_LOWER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa) , [SENSOR\_ATTR\_UPPER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b) , [SENSOR\_ATTR\_SLOPE\_TH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302) ,     [SENSOR\_ATTR\_SLOPE\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1) , [SENSOR\_ATTR\_HYSTERESIS](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94) , [SENSOR\_ATTR\_OVERSAMPLING](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd) , [SENSOR\_ATTR\_FULL\_SCALE](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3) ,     [SENSOR\_ATTR\_OFFSET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd) , [SENSOR\_ATTR\_CALIB\_TARGET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf) , [SENSOR\_ATTR\_CONFIGURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9) , [SENSOR\_ATTR\_CALIBRATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e) ,     [SENSOR\_ATTR\_FEATURE\_MASK](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52) , [SENSOR\_ATTR\_ALERT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a) , [SENSOR\_ATTR\_FF\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a) , [SENSOR\_ATTR\_BATCH\_DURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced) ,     [SENSOR\_ATTR\_GAIN](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3) , [SENSOR\_ATTR\_RESOLUTION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d) , [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8) , [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) = SENSOR\_ATTR\_COMMON\_COUNT ,     [SENSOR\_ATTR\_MAX](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) = INT16\_MAX   } |
|  | Sensor attribute types. [More...](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) |
| enum | [sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) { [SENSOR\_STREAM\_DATA\_INCLUDE](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) = 0 , [SENSOR\_STREAM\_DATA\_NOP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) = 1 , [SENSOR\_STREAM\_DATA\_DROP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) = 2 } |
|  | Options for what to do with the associated data when a trigger is consumed. [More...](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sensor\_chan\_spec\_eq](group__sensor__interface.md#gae95715ffea5da18a9593ec2add029824) (struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec0, struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec1) |
|  | Check if channel specs are equivalent. |
| static int | [sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53) (struct [sensor\_decode\_context](structsensor__decode__context.md) \*ctx, void \*out, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count) |
|  | Decode N frames using a [sensor\_decode\_context](structsensor__decode__context.md "Used for iterating over the data frames via the sensor_decoder_api."). |
| int | [sensor\_natively\_supported\_channel\_size\_info](group__sensor__interface.md#ga2b045cdbd4d1ca37beed69970093945b) (struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*frame\_size) |
| int | [sensor\_attr\_set](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr, const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Set an attribute for a sensor. |
| int | [sensor\_attr\_get](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Get an attribute for a sensor. |
| static int | [sensor\_trigger\_set](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trig, [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler) |
|  | Activate a sensor's trigger and set the trigger handler. |
| int | [sensor\_sample\_fetch](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff) (const struct [device](structdevice.md) \*dev) |
|  | Fetch a sample from the sensor and store it in an internal driver buffer. |
| int | [sensor\_sample\_fetch\_chan](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) type) |
|  | Fetch a sample from the sensor and store it in an internal driver buffer. |
| int | [sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Get a reading from a sensor device. |
| int | [sensor\_get\_decoder](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3) (const struct [device](structdevice.md) \*dev, const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder) |
|  | Get the sensor's decoder API. |
| int | [sensor\_reconfigure\_read\_iodev](group__sensor__interface.md#gab854651e1b6c3206bf2b829ea5a6c420) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [device](structdevice.md) \*sensor, const struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*channels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Reconfigure a reading iodev. |
| static int | [sensor\_stream](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, void \*userdata, struct [rtio\_sqe](structrtio__sqe.md) \*\*handle) |
| static int | [sensor\_read](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len) |
|  | Blocking one shot read of samples from a sensor into a buffer. |
| static int | [sensor\_read\_async\_mempool](group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, void \*userdata) |
|  | One shot non-blocking read with pool allocated buffer. |
| void | [sensor\_processing\_with\_callback](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8) (struct [rtio](structrtio.md) \*ctx, [sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462) cb) |
|  | Helper function for common processing of sensor data. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_ms2\_to\_g](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8) (const struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from m/s^2 to Gs. |
| static void | [sensor\_g\_to\_ms2](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) g, struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from Gs to m/s^2. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_ms2\_to\_ug](group__sensor__interface.md#ga3db980100e634310a0a1623136048742) (const struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from m/s^2 to micro Gs. |
| static void | [sensor\_ug\_to\_ms2](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ug, struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from micro Gs to m/s^2. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_rad\_to\_degrees](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220) (const struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting radians to degrees. |
| static void | [sensor\_degrees\_to\_rad](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting degrees to radians. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_rad\_to\_10udegrees](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6) (const struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting radians to 10 micro degrees. |
| static void | [sensor\_10udegrees\_to\_rad](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting 10 micro degrees to radians. |
| static double | [sensor\_value\_to\_double](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to double. |
| static float | [sensor\_value\_to\_float](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to float. |
| static int | [sensor\_value\_from\_double](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048) (struct [sensor\_value](structsensor__value.md) \*val, double inp) |
|  | Helper function for converting double to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |
| static int | [sensor\_value\_from\_float](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c) (struct [sensor\_value](structsensor__value.md) \*val, float inp) |
|  | Helper function for converting float to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [sensor\_value\_to\_milli](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to integer milli units. |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [sensor\_value\_to\_micro](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to integer micro units. |
| static int | [sensor\_value\_from\_milli](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3) (struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) milli) |
|  | Helper function for converting integer milli units to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |
| static int | [sensor\_value\_from\_micro](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99) (struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro) |
|  | Helper function for converting integer micro units to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |

## Detailed Description

Public APIs for the sensor driver.

## Macro Definition Documentation

## [◆ ](#a78ad4b76be4a6f5347ba82b7db43b7c2)SENSOR\_DECODER\_API\_DT\_DEFINE

| #define SENSOR\_DECODER\_API\_DT\_DEFINE | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(DT\_DRV\_COMPAT), (), (static)) \

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([sensor\_decoder\_api](structsensor__decoder__api.md), [SENSOR\_DECODER\_NAME](#a8d3434eb5860c2f2e6fe36b4de920c8c)())

[DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)

#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)

Does the devicetree have a status okay node with a compatible?

**Definition** devicetree.h:3604

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

[SENSOR\_DECODER\_NAME](#a8d3434eb5860c2f2e6fe36b4de920c8c)

#define SENSOR\_DECODER\_NAME()

Get the decoder name for the current driver.

**Definition** sensor.h:1490

[sensor\_decoder\_api](structsensor__decoder__api.md)

Decodes a single raw data buffer.

**Definition** sensor.h:466

Define a decoder API.

This macro should be created once per compatible string of a sensor and will create a statically referenceable decoder API.

[SENSOR\_DECODER\_API\_DT\_DEFINE](#a78ad4b76be4a6f5347ba82b7db43b7c2)() = {

.get\_frame\_count = my\_driver\_get\_frame\_count,

.get\_timestamp = my\_driver\_get\_timestamp,

.get\_shift = my\_driver\_get\_shift,

.decode = my\_driver\_decode,

};

[SENSOR\_DECODER\_API\_DT\_DEFINE](#a78ad4b76be4a6f5347ba82b7db43b7c2)

#define SENSOR\_DECODER\_API\_DT\_DEFINE()

Define a decoder API.

**Definition** sensor.h:1517

## [◆ ](#a82da2432981c593ed638a21c51fb0873)SENSOR\_DECODER\_DT\_GET

| #define SENSOR\_DECODER\_DT\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

&[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)([DT\_STRING\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)(node\_id, compatible, 0), \_\_decoder\_api)

[DT\_STRING\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)

#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx)

Get an element out of a string-array property as a token.

**Definition** devicetree.h:1294

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Statically get the decoder for a given node.

static const [sensor\_decoder\_api](structsensor__decoder__api.md) \*decoder = [SENSOR\_DECODER\_DT\_GET](#a82da2432981c593ed638a21c51fb0873)([DT\_ALIAS](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)(accel));

[DT\_ALIAS](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)

#define DT\_ALIAS(alias)

Get a node identifier from /aliases.

**Definition** devicetree.h:236

[SENSOR\_DECODER\_DT\_GET](#a82da2432981c593ed638a21c51fb0873)

#define SENSOR\_DECODER\_DT\_GET(node\_id)

Statically get the decoder for a given node.

**Definition** sensor.h:1499

## [◆ ](#a8d3434eb5860c2f2e6fe36b4de920c8c)SENSOR\_DECODER\_NAME

| #define SENSOR\_DECODER\_NAME | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(DT\_DRV\_COMPAT, \_\_decoder\_api)

Get the decoder name for the current driver.

This function depends on DT\_DRV\_COMPAT being defined.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor.h](sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
