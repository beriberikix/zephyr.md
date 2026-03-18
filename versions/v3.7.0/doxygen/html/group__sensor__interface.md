---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__sensor__interface.html
original_path: doxygen/html/group__sensor__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Sensor Interface

[Device Driver APIs](group__io__interfaces.md)

Sensor Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Invensense (TDK) ICM42688 DT Options](group__ICM42688.md) |

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
| #define | [SENSOR\_DECODE\_CONTEXT\_INIT](#gae69ec503df53d2d5ee417e481f9ac9ea)(decoder\_, buffer\_, channel\_type\_, channel\_index\_) |
|  | Initialize a [sensor\_decode\_context](structsensor__decode__context.md "Used for iterating over the data frames via the sensor_decoder_api."). |
| #define | [SENSOR\_STREAM\_TRIGGER\_PREP](#ga9b7b0db322121d220b126d2b5bb7eb73)(\_trigger, \_opt) |
| #define | [SENSOR\_DT\_READ\_IODEV](#ga0cc1ee28114557e9e00257071c7dfa9f)(name, dt\_node, ...) |
|  | Define a reading instance of a sensor. |
| #define | [SENSOR\_DT\_STREAM\_IODEV](#ga35211c4d908a26f98b1f8d925a9b1374)(name, dt\_node, ...) |
|  | Define a stream instance of a sensor. |
| #define | [SENSOR\_CHANNEL\_3\_AXIS](#ga32f679a4004b5707b2de00eb580d0930)(chan) |
|  | checks if a given channel is a 3-axis channel |
| #define | [SENSOR\_G](#ga0066e049c4f084305ca2b978e5c7454d)   9806650LL |
|  | The value of gravitational constant in micro m/s^2. |
| #define | [SENSOR\_PI](#ga6ebdc2f6942334de3cc248a53db7df33)   3141592LL |
|  | The value of constant PI in micros. |
| #define | [SENSOR\_INFO\_DEFINE](#ga7467206da76c3704d2e491d1b1c0973a)(name, ...) |
| #define | [SENSOR\_INFO\_DT\_DEFINE](#ga9e6acbc580e9223bfb86ee8919cdc778)(node\_id) |
| #define | [SENSOR\_DEVICE\_DT\_DEFINE](#gaa67ca630e3931a0c3821ba438c86690c)(node\_id, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with sensor specifics. |
| #define | [SENSOR\_DEVICE\_DT\_INST\_DEFINE](#ga284dc3b9018f14161dc0a2b6bed9a37e)(inst, ...) |
|  | Like [SENSOR\_DEVICE\_DT\_DEFINE()](#gaa67ca630e3931a0c3821ba438c86690c) for an instance of a DT\_DRV\_COMPAT compatible. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sensor\_trigger\_handler\_t](#ga890c1fb6d6974aea22a2d08829a75902)) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trigger) |
|  | Callback API upon firing of a trigger. |
| typedef int(\* | [sensor\_attr\_set\_t](#ga38422ace4194a66a9a912a8ef1e088fb)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) attr, const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Callback API upon setting a sensor's attributes. |
| typedef int(\* | [sensor\_attr\_get\_t](#ga00d05c82b46e56dca5f6e8f7f01c31b8)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) attr, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Callback API upon getting a sensor's attributes. |
| typedef int(\* | [sensor\_trigger\_set\_t](#gad7f7a3d9e714cc16f23656ca06592aa4)) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trig, [sensor\_trigger\_handler\_t](#ga890c1fb6d6974aea22a2d08829a75902) handler) |
|  | Callback API for setting a sensor's trigger and handler. |
| typedef int(\* | [sensor\_sample\_fetch\_t](#gacae110a4edb6f29dfb457cb1ea8d68c1)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan) |
|  | Callback API for fetching data from a sensor. |
| typedef int(\* | [sensor\_channel\_get\_t](#ga5c9b5ed9097464562004b446856043fd)) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Callback API for getting a reading from a sensor. |
| typedef int(\* | [sensor\_get\_decoder\_t](#ga21e407d552d140cfb6bfd0d9513c7d42)) (const struct [device](structdevice.md) \*dev, const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*api) |
|  | Get the decoder associate with the given device. |
| typedef void(\* | [sensor\_submit\_t](#gad77732c8f0ec5520cdd71c2829787981)) (const struct [device](structdevice.md) \*sensor, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*sqe) |
| typedef void(\* | [sensor\_processing\_callback\_t](#gaa8cd6e4fadb5d69e59d101733b4fb462)) (int result, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len, void \*userdata) |
|  | Callback function used with the helper processing function. |

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) {     [SENSOR\_CHAN\_ACCEL\_X](#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c) , [SENSOR\_CHAN\_ACCEL\_Y](#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8) , [SENSOR\_CHAN\_ACCEL\_Z](#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f) , [SENSOR\_CHAN\_ACCEL\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9) ,     [SENSOR\_CHAN\_GYRO\_X](#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015) , [SENSOR\_CHAN\_GYRO\_Y](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847) , [SENSOR\_CHAN\_GYRO\_Z](#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39) , [SENSOR\_CHAN\_GYRO\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e) ,     [SENSOR\_CHAN\_MAGN\_X](#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240) , [SENSOR\_CHAN\_MAGN\_Y](#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942) , [SENSOR\_CHAN\_MAGN\_Z](#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61) , [SENSOR\_CHAN\_MAGN\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32) ,     [SENSOR\_CHAN\_DIE\_TEMP](#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1) , [SENSOR\_CHAN\_AMBIENT\_TEMP](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c) , [SENSOR\_CHAN\_PRESS](#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9) , [SENSOR\_CHAN\_PROX](#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774) ,     [SENSOR\_CHAN\_HUMIDITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042) , [SENSOR\_CHAN\_LIGHT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d) , [SENSOR\_CHAN\_IR](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c) , [SENSOR\_CHAN\_RED](#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa) ,     [SENSOR\_CHAN\_GREEN](#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378) , [SENSOR\_CHAN\_BLUE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5) , [SENSOR\_CHAN\_ALTITUDE](#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512) , [SENSOR\_CHAN\_PM\_1\_0](#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815) ,     [SENSOR\_CHAN\_PM\_2\_5](#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945) , [SENSOR\_CHAN\_PM\_10](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225) , [SENSOR\_CHAN\_DISTANCE](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08) , [SENSOR\_CHAN\_CO2](#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133) ,     [SENSOR\_CHAN\_O2](#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9) , [SENSOR\_CHAN\_VOC](#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e) , [SENSOR\_CHAN\_GAS\_RES](#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01) , [SENSOR\_CHAN\_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d) ,     [SENSOR\_CHAN\_VSHUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9) , [SENSOR\_CHAN\_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950) , [SENSOR\_CHAN\_POWER](#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177) , [SENSOR\_CHAN\_RESISTANCE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b) ,     [SENSOR\_CHAN\_ROTATION](#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf) , [SENSOR\_CHAN\_POS\_DX](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517) , [SENSOR\_CHAN\_POS\_DY](#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76) , [SENSOR\_CHAN\_POS\_DZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9) ,     [SENSOR\_CHAN\_POS\_DXYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740) , [SENSOR\_CHAN\_RPM](#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1) , [SENSOR\_CHAN\_GAUGE\_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d) , [SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8) ,     [SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8) , [SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf) , [SENSOR\_CHAN\_GAUGE\_TEMP](#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214) , [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139) ,     [SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649) , [SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad) , [SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a) , [SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8) ,     [SENSOR\_CHAN\_GAUGE\_AVG\_POWER](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228) , [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6) , [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65) , [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL](#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb) ,     [SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46) , [SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0) , [SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf) , [SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f) ,     [SENSOR\_CHAN\_ALL](#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c) , [SENSOR\_CHAN\_COMMON\_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303) , [SENSOR\_CHAN\_PRIV\_START](#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) = SENSOR\_CHAN\_COMMON\_COUNT , [SENSOR\_CHAN\_MAX](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) = INT16\_MAX   } |
|  | Sensor channels. [More...](#gaaa1b502bc029b10d7b23b0a25ef4e934) |
| enum | [sensor\_trigger\_type](#ga08215279400e8c9eb05ce4e4f0898ffd) {     [SENSOR\_TRIG\_TIMER](#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023) , [SENSOR\_TRIG\_DATA\_READY](#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f) , [SENSOR\_TRIG\_DELTA](#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855) , [SENSOR\_TRIG\_NEAR\_FAR](#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5) ,     [SENSOR\_TRIG\_THRESHOLD](#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606) , [SENSOR\_TRIG\_TAP](#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d) , [SENSOR\_TRIG\_DOUBLE\_TAP](#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef) , [SENSOR\_TRIG\_FREEFALL](#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c) ,     [SENSOR\_TRIG\_MOTION](#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276) , [SENSOR\_TRIG\_STATIONARY](#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d) , [SENSOR\_TRIG\_FIFO\_WATERMARK](#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4) , [SENSOR\_TRIG\_FIFO\_FULL](#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c) ,     [SENSOR\_TRIG\_COMMON\_COUNT](#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5) , [SENSOR\_TRIG\_PRIV\_START](#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) = SENSOR\_TRIG\_COMMON\_COUNT , [SENSOR\_TRIG\_MAX](#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) = INT16\_MAX   } |
|  | Sensor trigger types. [More...](#ga08215279400e8c9eb05ce4e4f0898ffd) |
| enum | [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) {     [SENSOR\_ATTR\_SAMPLING\_FREQUENCY](#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291) , [SENSOR\_ATTR\_LOWER\_THRESH](#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa) , [SENSOR\_ATTR\_UPPER\_THRESH](#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b) , [SENSOR\_ATTR\_SLOPE\_TH](#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302) ,     [SENSOR\_ATTR\_SLOPE\_DUR](#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1) , [SENSOR\_ATTR\_HYSTERESIS](#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94) , [SENSOR\_ATTR\_OVERSAMPLING](#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd) , [SENSOR\_ATTR\_FULL\_SCALE](#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3) ,     [SENSOR\_ATTR\_OFFSET](#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd) , [SENSOR\_ATTR\_CALIB\_TARGET](#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf) , [SENSOR\_ATTR\_CONFIGURATION](#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9) , [SENSOR\_ATTR\_CALIBRATION](#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e) ,     [SENSOR\_ATTR\_FEATURE\_MASK](#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52) , [SENSOR\_ATTR\_ALERT](#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a) , [SENSOR\_ATTR\_FF\_DUR](#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a) , [SENSOR\_ATTR\_BATCH\_DURATION](#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced) ,     [SENSOR\_ATTR\_COMMON\_COUNT](#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8) , [SENSOR\_ATTR\_PRIV\_START](#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) = SENSOR\_ATTR\_COMMON\_COUNT , [SENSOR\_ATTR\_MAX](#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) = INT16\_MAX   } |
|  | Sensor attribute types. [More...](#ga0dcb6842bc969492bd1c9eb49708940b) |
| enum | [sensor\_stream\_data\_opt](#ga8613a20521a37d40fd7371dc63ba2dac) { [SENSOR\_STREAM\_DATA\_INCLUDE](#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) = 0 , [SENSOR\_STREAM\_DATA\_NOP](#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) = 1 , [SENSOR\_STREAM\_DATA\_DROP](#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) = 2 } |
|  | Options for what to do with the associated data when a trigger is consumed. [More...](#ga8613a20521a37d40fd7371dc63ba2dac) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sensor\_chan\_spec\_eq](#gae95715ffea5da18a9593ec2add029824) (struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec0, struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec1) |
|  | Check if channel specs are equivalent. |
| static int | [sensor\_decode](#ga018bca56056ae2558f9e45aeb2fa5f53) (struct [sensor\_decode\_context](structsensor__decode__context.md) \*ctx, void \*out, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count) |
|  | Decode N frames using a [sensor\_decode\_context](structsensor__decode__context.md "Used for iterating over the data frames via the sensor_decoder_api."). |
| int | [sensor\_natively\_supported\_channel\_size\_info](#ga2b045cdbd4d1ca37beed69970093945b) (struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*frame\_size) |
| int | [sensor\_attr\_set](#gafbf65226a227e9f8824908bc38e336f5) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) attr, const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Set an attribute for a sensor. |
| int | [sensor\_attr\_get](#gaedfdfc71dce702dc1fb1c6e60ff0f73a) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) attr, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Get an attribute for a sensor. |
| static int | [sensor\_trigger\_set](#ga7c72aca732e0641612d2f9437c2e41b7) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trig, [sensor\_trigger\_handler\_t](#ga890c1fb6d6974aea22a2d08829a75902) handler) |
|  | Activate a sensor's trigger and set the trigger handler. |
| int | [sensor\_sample\_fetch](#gaa75e25d93ee7cac0bf38399f3c006dff) (const struct [device](structdevice.md) \*dev) |
|  | Fetch a sample from the sensor and store it in an internal driver buffer. |
| int | [sensor\_sample\_fetch\_chan](#gac16192826432438a15274cf28d66e8a6) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) type) |
|  | Fetch a sample from the sensor and store it in an internal driver buffer. |
| int | [sensor\_channel\_get](#ga9e0e6c1408d32c52267984bae7cb268d) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Get a reading from a sensor device. |
| int | [sensor\_get\_decoder](#ga12db6fc43adce48d34c25c16fd2336a3) (const struct [device](structdevice.md) \*dev, const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder) |
|  | Get the sensor's decoder API. |
| int | [sensor\_reconfigure\_read\_iodev](#gab854651e1b6c3206bf2b829ea5a6c420) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [device](structdevice.md) \*sensor, const struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*channels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Reconfigure a reading iodev. |
| static int | [sensor\_stream](#gac77fc83844935f61a2bf9ab2c38987b6) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, void \*userdata, struct [rtio\_sqe](structrtio__sqe.md) \*\*handle) |
| static int | [sensor\_read](#ga1e77abad33cfd4b8330484cdc1354976) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len) |
|  | Blocking one shot read of samples from a sensor into a buffer. |
| static int | [sensor\_read\_async\_mempool](#gab9eee9440b46b545b1faae224ae5949a) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, void \*userdata) |
|  | One shot non-blocking read with pool allocated buffer. |
| void | [sensor\_processing\_with\_callback](#gabb076531445e1b128d515b28c7cc9dc8) (struct [rtio](structrtio.md) \*ctx, [sensor\_processing\_callback\_t](#gaa8cd6e4fadb5d69e59d101733b4fb462) cb) |
|  | Helper function for common processing of sensor data. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_ms2\_to\_g](#gab797f2f578b1c9cc44f54ab5d503bbf8) (const struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from m/s^2 to Gs. |
| static void | [sensor\_g\_to\_ms2](#ga6ab9ce9c6ee2e52d197e5cb4ccd88979) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) g, struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from Gs to m/s^2. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_ms2\_to\_ug](#ga3db980100e634310a0a1623136048742) (const struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from m/s^2 to micro Gs. |
| static void | [sensor\_ug\_to\_ms2](#ga28a1c6cf74a391712a4697792f759d62) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ug, struct [sensor\_value](structsensor__value.md) \*ms2) |
|  | Helper function to convert acceleration from micro Gs to m/s^2. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_rad\_to\_degrees](#ga040a907c8934baab66d27b8dfb1ea220) (const struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting radians to degrees. |
| static void | [sensor\_degrees\_to\_rad](#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting degrees to radians. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sensor\_rad\_to\_10udegrees](#gad80093a6cfe95428dd0ead85547838a6) (const struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting radians to 10 micro degrees. |
| static void | [sensor\_10udegrees\_to\_rad](#gab53418e1eb164364663d3ec3f40399a4) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad) |
|  | Helper function for converting 10 micro degrees to radians. |
| static double | [sensor\_value\_to\_double](#ga29223b754dc436ab1e97ce6209a3ea06) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to double. |
| static float | [sensor\_value\_to\_float](#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to float. |
| static int | [sensor\_value\_from\_double](#gaf01bbb251ad0c7f6c55c5b702e8a4048) (struct [sensor\_value](structsensor__value.md) \*val, double inp) |
|  | Helper function for converting double to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |
| static int | [sensor\_value\_from\_float](#ga64d5a1725eda200c80daf42b1067c46c) (struct [sensor\_value](structsensor__value.md) \*val, float inp) |
|  | Helper function for converting float to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [sensor\_value\_to\_milli](#ga6d69a9644e08a9cd7773645fa11293e3) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to integer milli units. |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [sensor\_value\_to\_micro](#ga9bf7faf60aa54a7540e9b73a61864e25) (const struct [sensor\_value](structsensor__value.md) \*val) |
|  | Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to integer micro units. |
| static int | [sensor\_value\_from\_milli](#ga88b2605526e37420db871f066c5053b3) (struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) milli) |
|  | Helper function for converting integer milli units to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |
| static int | [sensor\_value\_from\_micro](#gabff019c63c89cbc546c0981819040c99) (struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro) |
|  | Helper function for converting integer micro units to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value."). |

## Detailed Description

Sensor Interface.

Since
:   1.2

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga32f679a4004b5707b2de00eb580d0930)SENSOR\_CHANNEL\_3\_AXIS

| #define SENSOR\_CHANNEL\_3\_AXIS | ( |  | *chan* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

**Value:**

((chan) == [SENSOR\_CHAN\_ACCEL\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9) || (chan) == [SENSOR\_CHAN\_GYRO\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e) || \

(chan) == [SENSOR\_CHAN\_MAGN\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32) || (chan) == [SENSOR\_CHAN\_POS\_DXYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740))

[SENSOR\_CHAN\_ACCEL\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)

@ SENSOR\_CHAN\_ACCEL\_XYZ

Acceleration on the X, Y and Z axes.

**Definition** sensor.h:69

[SENSOR\_CHAN\_GYRO\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)

@ SENSOR\_CHAN\_GYRO\_XYZ

Angular velocity around the X, Y and Z axes.

**Definition** sensor.h:77

[SENSOR\_CHAN\_MAGN\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)

@ SENSOR\_CHAN\_MAGN\_XYZ

Magnetic field on the X, Y and Z axes.

**Definition** sensor.h:85

[SENSOR\_CHAN\_POS\_DXYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)

@ SENSOR\_CHAN\_POS\_DXYZ

Position change on the X, Y and Z axis, in points.

**Definition** sensor.h:154

checks if a given channel is a 3-axis channel

Parameters
:   | [in] | chan | The channel to check |
    | --- | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if `chan` is any of [SENSOR\_CHAN\_ACCEL\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9), [SENSOR\_CHAN\_GYRO\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e), or [SENSOR\_CHAN\_MAGN\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32), or [SENSOR\_CHAN\_POS\_DXYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740) |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise |

## [◆ ](#gae69ec503df53d2d5ee417e481f9ac9ea)SENSOR\_DECODE\_CONTEXT\_INIT

| #define SENSOR\_DECODE\_CONTEXT\_INIT | ( |  | *decoder\_*, |
| --- | --- | --- | --- |
|  |  |  | *buffer\_*, |
|  |  |  | *channel\_type\_*, |
|  |  |  | *channel\_index\_* ) |

`#include <[sensor.h](sensor_8h.md)>`

**Value:**

{ \

.decoder = (decoder\_), \

.buffer = (buffer\_), \

.channel = {.chan\_type = (channel\_type\_), .chan\_idx = (channel\_index\_)}, \

.fit = 0, \

}

Initialize a [sensor\_decode\_context](structsensor__decode__context.md "Used for iterating over the data frames via the sensor_decoder_api.").

## [◆ ](#gaa67ca630e3931a0c3821ba438c86690c)SENSOR\_DEVICE\_DT\_DEFINE

| #define SENSOR\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *[pm\_device](structpm__device.md)*, |
|  |  |  | *data\_ptr*, |
|  |  |  | *cfg\_ptr*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api\_ptr*, |
|  |  |  | ... ) |

`#include <[sensor.h](sensor_8h.md)>`

**Value:**

[DEVICE\_DT\_DEFINE](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)(node\_id, init\_fn, [pm\_device](structpm__device.md), \

data\_ptr, cfg\_ptr, level, prio, \

api\_ptr, \_\_VA\_ARGS\_\_); \

\

SENSOR\_INFO\_DT\_DEFINE(node\_id);

[DEVICE\_DT\_DEFINE](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)

#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api,...)

Create a device object from a devicetree node identifier and set it up for boot time initialization.

**Definition** device.h:195

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:163

Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with sensor specifics.

Defines a device which implements the sensor API. May define an element in the sensor info iterable section used to enumerate all sensor devices.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Name of the init function of the driver. |
    | [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") | PM device resources reference (NULL if device does not use PM). |
    | data\_ptr | Pointer to the device's private data. |
    | cfg\_ptr | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api\_ptr | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#ga284dc3b9018f14161dc0a2b6bed9a37e)SENSOR\_DEVICE\_DT\_INST\_DEFINE

| #define SENSOR\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[sensor.h](sensor_8h.md)>`

**Value:**

[SENSOR\_DEVICE\_DT\_DEFINE](#gaa67ca630e3931a0c3821ba438c86690c)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

[SENSOR\_DEVICE\_DT\_DEFINE](#gaa67ca630e3931a0c3821ba438c86690c)

#define SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr,...)

Like DEVICE\_DT\_DEFINE() with sensor specifics.

**Definition** sensor.h:1395

Like [SENSOR\_DEVICE\_DT\_DEFINE()](#gaa67ca630e3931a0c3821ba438c86690c) for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to [SENSOR\_DEVICE\_DT\_DEFINE()](#gaa67ca630e3931a0c3821ba438c86690c). |
    | --- | --- |
    | ... | other parameters as expected by [SENSOR\_DEVICE\_DT\_DEFINE()](#gaa67ca630e3931a0c3821ba438c86690c). |

## [◆ ](#ga0cc1ee28114557e9e00257071c7dfa9f)SENSOR\_DT\_READ\_IODEV

| #define SENSOR\_DT\_READ\_IODEV | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *dt\_node*, |
|  |  |  | ... ) |

`#include <[sensor.h](sensor_8h.md)>`

**Value:**

static struct [sensor\_chan\_spec](structsensor__chan__spec.md) \_CONCAT(\_\_channel\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

static struct [sensor\_read\_config](structsensor__read__config.md) \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

.sensor = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)(dt\_node), \

.is\_streaming = false, \

.channels = \_CONCAT(\_\_channel\_array\_, name), \

.count = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_CONCAT(\_\_channel\_array\_, name)), \

.max = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_CONCAT(\_\_channel\_array\_, name)), \

}; \

RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, \_CONCAT(&\_\_sensor\_read\_config\_, name))

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:246

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:127

[sensor\_chan\_spec](structsensor__chan__spec.md)

Sensor Channel Specification.

**Definition** sensor.h:431

[sensor\_read\_config](structsensor__read__config.md)

**Definition** sensor.h:622

Define a reading instance of a sensor.

Use this macro to generate a [rtio\_iodev](structrtio__iodev.md "rtio_iodev") for reading specific channels. Example:

(.c)

[SENSOR\_DT\_READ\_IODEV](#ga0cc1ee28114557e9e00257071c7dfa9f)(icm42688\_accelgyro, [DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(icm42688),

{ [SENSOR\_CHAN\_ACCEL\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9), 0 },

{ [SENSOR\_CHAN\_GYRO\_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e), 0 });

int main(void) {

[sensor\_read\_async\_mempool](#gab9eee9440b46b545b1faae224ae5949a)(&icm42688\_accelgyro, &[rtio](structrtio.md));

}

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:200

[SENSOR\_DT\_READ\_IODEV](#ga0cc1ee28114557e9e00257071c7dfa9f)

#define SENSOR\_DT\_READ\_IODEV(name, dt\_node,...)

Define a reading instance of a sensor.

**Definition** sensor.h:648

[sensor\_read\_async\_mempool](#gab9eee9440b46b545b1faae224ae5949a)

static int sensor\_read\_async\_mempool(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata)

One shot non-blocking read with pool allocated buffer.

**Definition** sensor.h:1085

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:327

## [◆ ](#ga35211c4d908a26f98b1f8d925a9b1374)SENSOR\_DT\_STREAM\_IODEV

| #define SENSOR\_DT\_STREAM\_IODEV | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *dt\_node*, |
|  |  |  | ... ) |

`#include <[sensor.h](sensor_8h.md)>`

**Value:**

static struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) \_CONCAT(\_\_trigger\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

static struct [sensor\_read\_config](structsensor__read__config.md) \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

.sensor = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)(dt\_node), \

.is\_streaming = true, \

.triggers = \_CONCAT(\_\_trigger\_array\_, name), \

.count = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_CONCAT(\_\_trigger\_array\_, name)), \

.max = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_CONCAT(\_\_trigger\_array\_, name)), \

}; \

RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, &\_CONCAT(\_\_sensor\_read\_config\_, name))

[sensor\_stream\_trigger](structsensor__stream__trigger.md)

**Definition** sensor.h:608

Define a stream instance of a sensor.

Use this macro to generate a [rtio\_iodev](structrtio__iodev.md "rtio_iodev") for starting a stream that's triggered by specific interrupts. Example:

(.c)

[SENSOR\_DT\_STREAM\_IODEV](#ga35211c4d908a26f98b1f8d925a9b1374)(imu\_stream, [DT\_ALIAS](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)(imu),

{[SENSOR\_TRIG\_FIFO\_WATERMARK](#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4), [SENSOR\_STREAM\_DATA\_INCLUDE](#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)},

{[SENSOR\_TRIG\_FIFO\_FULL](#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c), [SENSOR\_STREAM\_DATA\_NOP](#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)});

int main(void) {

struct [rtio\_sqe](structrtio__sqe.md) \*handle;

[sensor\_stream](#gac77fc83844935f61a2bf9ab2c38987b6)(&imu\_stream, &[rtio](structrtio.md), NULL, &handle);

[k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)(1000);

[rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)(handle);

}

[DT\_ALIAS](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)

#define DT\_ALIAS(alias)

Get a node identifier from /aliases.

**Definition** devicetree.h:240

[rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)

int rtio\_sqe\_cancel(struct rtio\_sqe \*sqe)

Attempt to cancel an SQE.

[SENSOR\_DT\_STREAM\_IODEV](#ga35211c4d908a26f98b1f8d925a9b1374)

#define SENSOR\_DT\_STREAM\_IODEV(name, dt\_node,...)

Define a stream instance of a sensor.

**Definition** sensor.h:678

[sensor\_stream](#gac77fc83844935f61a2bf9ab2c38987b6)

static int sensor\_stream(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata, struct rtio\_sqe \*\*handle)

**Definition** sensor.h:1006

[SENSOR\_TRIG\_FIFO\_FULL](#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)

@ SENSOR\_TRIG\_FIFO\_FULL

Trigger fires when the FIFO becomes full.

**Definition** sensor.h:265

[SENSOR\_TRIG\_FIFO\_WATERMARK](#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)

@ SENSOR\_TRIG\_FIFO\_WATERMARK

Trigger fires when the FIFO watermark has been reached.

**Definition** sensor.h:262

[SENSOR\_STREAM\_DATA\_INCLUDE](#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)

@ SENSOR\_STREAM\_DATA\_INCLUDE

Include whatever data is associated with the trigger.

**Definition** sensor.h:601

[SENSOR\_STREAM\_DATA\_NOP](#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)

@ SENSOR\_STREAM\_DATA\_NOP

Do nothing with the associated trigger data, it may be consumed later.

**Definition** sensor.h:603

[k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9)

static int32\_t k\_msleep(int32\_t ms)

Put the current thread to sleep.

**Definition** kernel.h:489

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:232

## [◆ ](#ga0066e049c4f084305ca2b978e5c7454d)SENSOR\_G

| #define SENSOR\_G   9806650LL |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

The value of gravitational constant in micro m/s^2.

## [◆ ](#ga7467206da76c3704d2e491d1b1c0973a)SENSOR\_INFO\_DEFINE

| #define SENSOR\_INFO\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[sensor.h](sensor_8h.md)>`

## [◆ ](#ga9e6acbc580e9223bfb86ee8919cdc778)SENSOR\_INFO\_DT\_DEFINE

| #define SENSOR\_INFO\_DT\_DEFINE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

## [◆ ](#ga6ebdc2f6942334de3cc248a53db7df33)SENSOR\_PI

| #define SENSOR\_PI   3141592LL |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

The value of constant PI in micros.

## [◆ ](#ga9b7b0db322121d220b126d2b5bb7eb73)SENSOR\_STREAM\_TRIGGER\_PREP

| #define SENSOR\_STREAM\_TRIGGER\_PREP | ( |  | *\_trigger*, |
| --- | --- | --- | --- |
|  |  |  | *\_opt* ) |

`#include <[sensor.h](sensor_8h.md)>`

**Value:**

{ \

.trigger = (\_trigger), .opt = (\_opt), \

}

## Typedef Documentation

## [◆ ](#ga00d05c82b46e56dca5f6e8f7f01c31b8)sensor\_attr\_get\_t

| typedef int(\* sensor\_attr\_get\_t) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) attr, struct [sensor\_value](structsensor__value.md) \*val) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Callback API upon getting a sensor's attributes.

See [sensor\_attr\_get()](#gaedfdfc71dce702dc1fb1c6e60ff0f73a) for argument description

## [◆ ](#ga38422ace4194a66a9a912a8ef1e088fb)sensor\_attr\_set\_t

| typedef int(\* sensor\_attr\_set\_t) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) attr, const struct [sensor\_value](structsensor__value.md) \*val) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Callback API upon setting a sensor's attributes.

See [sensor\_attr\_set()](#gafbf65226a227e9f8824908bc38e336f5) for argument description

## [◆ ](#ga5c9b5ed9097464562004b446856043fd)sensor\_channel\_get\_t

| typedef int(\* sensor\_channel\_get\_t) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan, struct [sensor\_value](structsensor__value.md) \*val) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Callback API for getting a reading from a sensor.

See [sensor\_channel\_get()](#ga9e0e6c1408d32c52267984bae7cb268d) for argument description

## [◆ ](#ga21e407d552d140cfb6bfd0d9513c7d42)sensor\_get\_decoder\_t

| typedef int(\* sensor\_get\_decoder\_t) (const struct [device](structdevice.md) \*dev, const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*api) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Get the decoder associate with the given device.

See also
:   [sensor\_get\_decoder](#ga12db6fc43adce48d34c25c16fd2336a3) for more details

## [◆ ](#gaa8cd6e4fadb5d69e59d101733b4fb462)sensor\_processing\_callback\_t

| typedef void(\* sensor\_processing\_callback\_t) (int result, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len, void \*userdata) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Callback function used with the helper processing function.

See also
:   [sensor\_processing\_with\_callback](#gabb076531445e1b128d515b28c7cc9dc8)

Parameters
:   | [in] | result | The result code of the read (0 being success) |
    | --- | --- | --- |
    | [in] | buf | The data buffer holding the sensor data |
    | [in] | buf\_len | The length (in bytes) of the `buf` |
    | [in] | userdata | The optional userdata passed to [sensor\_read\_async\_mempool()](#gab9eee9440b46b545b1faae224ae5949a) |

## [◆ ](#gacae110a4edb6f29dfb457cb1ea8d68c1)sensor\_sample\_fetch\_t

| typedef int(\* sensor\_sample\_fetch\_t) (const struct [device](structdevice.md) \*dev, enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) chan) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Callback API for fetching data from a sensor.

See [sensor\_sample\_fetch()](#gaa75e25d93ee7cac0bf38399f3c006dff) for argument description

## [◆ ](#gad77732c8f0ec5520cdd71c2829787981)sensor\_submit\_t

| typedef void(\* sensor\_submit\_t) (const struct [device](structdevice.md) \*sensor, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*sqe) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

## [◆ ](#ga890c1fb6d6974aea22a2d08829a75902)sensor\_trigger\_handler\_t

| typedef void(\* sensor\_trigger\_handler\_t) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trigger) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Callback API upon firing of a trigger.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |
    | trigger | The trigger |

## [◆ ](#gad7f7a3d9e714cc16f23656ca06592aa4)sensor\_trigger\_set\_t

| typedef int(\* sensor\_trigger\_set\_t) (const struct [device](structdevice.md) \*dev, const struct [sensor\_trigger](structsensor__trigger.md) \*trig, [sensor\_trigger\_handler\_t](#ga890c1fb6d6974aea22a2d08829a75902) handler) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Callback API for setting a sensor's trigger and handler.

See [sensor\_trigger\_set()](#ga7c72aca732e0641612d2f9437c2e41b7) for argument description

## Enumeration Type Documentation

## [◆ ](#ga0dcb6842bc969492bd1c9eb49708940b)sensor\_attribute

| enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Sensor attribute types.

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_SAMPLING\_FREQUENCY | Sensor sampling frequency, i.e.  how many times a second the sensor takes a measurement. |
| SENSOR\_ATTR\_LOWER\_THRESH | Lower threshold for trigger. |
| SENSOR\_ATTR\_UPPER\_THRESH | Upper threshold for trigger. |
| SENSOR\_ATTR\_SLOPE\_TH | Threshold for any-motion (slope) trigger. |
| SENSOR\_ATTR\_SLOPE\_DUR | Duration for which the slope values needs to be outside the threshold for the trigger to fire. |
| SENSOR\_ATTR\_HYSTERESIS |  |
| SENSOR\_ATTR\_OVERSAMPLING | Oversampling factor. |
| SENSOR\_ATTR\_FULL\_SCALE | Sensor range, in SI units. |
| SENSOR\_ATTR\_OFFSET | The sensor value returned will be altered by the amount indicated by offset: final\_value = [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") + offset. |
| SENSOR\_ATTR\_CALIB\_TARGET | Calibration target.  This will be used by the internal chip's algorithms to calibrate itself on a certain axis, or all of them. |
| SENSOR\_ATTR\_CONFIGURATION | Configure the operating modes of a sensor. |
| SENSOR\_ATTR\_CALIBRATION | Set a calibration value needed by a sensor. |
| SENSOR\_ATTR\_FEATURE\_MASK | Enable/disable sensor features. |
| SENSOR\_ATTR\_ALERT | Alert threshold or alert enable/disable. |
| SENSOR\_ATTR\_FF\_DUR | Free-fall duration represented in milliseconds.  If the sampling frequency is changed during runtime, this attribute should be set to adjust freefall duration to the new sampling frequency. |
| SENSOR\_ATTR\_BATCH\_DURATION | Hardware batch duration in ticks. |
| SENSOR\_ATTR\_COMMON\_COUNT | Number of all common sensor attributes. |
| SENSOR\_ATTR\_PRIV\_START | This and higher values are sensor specific.  Refer to the sensor header file. |
| SENSOR\_ATTR\_MAX | Maximum value describing a sensor attribute type. |

## [◆ ](#gaaa1b502bc029b10d7b23b0a25ef4e934)sensor\_channel

| enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Sensor channels.

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_ACCEL\_X | Acceleration on the X axis, in m/s^2. |
| SENSOR\_CHAN\_ACCEL\_Y | Acceleration on the Y axis, in m/s^2. |
| SENSOR\_CHAN\_ACCEL\_Z | Acceleration on the Z axis, in m/s^2. |
| SENSOR\_CHAN\_ACCEL\_XYZ | Acceleration on the X, Y and Z axes. |
| SENSOR\_CHAN\_GYRO\_X | Angular velocity around the X axis, in radians/s. |
| SENSOR\_CHAN\_GYRO\_Y | Angular velocity around the Y axis, in radians/s. |
| SENSOR\_CHAN\_GYRO\_Z | Angular velocity around the Z axis, in radians/s. |
| SENSOR\_CHAN\_GYRO\_XYZ | Angular velocity around the X, Y and Z axes. |
| SENSOR\_CHAN\_MAGN\_X | Magnetic field on the X axis, in Gauss. |
| SENSOR\_CHAN\_MAGN\_Y | Magnetic field on the Y axis, in Gauss. |
| SENSOR\_CHAN\_MAGN\_Z | Magnetic field on the Z axis, in Gauss. |
| SENSOR\_CHAN\_MAGN\_XYZ | Magnetic field on the X, Y and Z axes. |
| SENSOR\_CHAN\_DIE\_TEMP | Device die temperature in degrees Celsius. |
| SENSOR\_CHAN\_AMBIENT\_TEMP | Ambient temperature in degrees Celsius. |
| SENSOR\_CHAN\_PRESS | Pressure in kilopascal. |
| SENSOR\_CHAN\_PROX | Proximity.  Adimensional. A value of 1 indicates that an object is close. |
| SENSOR\_CHAN\_HUMIDITY | Humidity, in percent. |
| SENSOR\_CHAN\_LIGHT | Illuminance in visible spectrum, in lux. |
| SENSOR\_CHAN\_IR | Illuminance in infra-red spectrum, in lux. |
| SENSOR\_CHAN\_RED | Illuminance in red spectrum, in lux. |
| SENSOR\_CHAN\_GREEN | Illuminance in green spectrum, in lux. |
| SENSOR\_CHAN\_BLUE | Illuminance in blue spectrum, in lux. |
| SENSOR\_CHAN\_ALTITUDE | Altitude, in meters. |
| SENSOR\_CHAN\_PM\_1\_0 | 1.0 micro-meters Particulate Matter, in ug/m^3 |
| SENSOR\_CHAN\_PM\_2\_5 | 2.5 micro-meters Particulate Matter, in ug/m^3 |
| SENSOR\_CHAN\_PM\_10 | 10 micro-meters Particulate Matter, in ug/m^3 |
| SENSOR\_CHAN\_DISTANCE | Distance.  From sensor to target, in meters |
| SENSOR\_CHAN\_CO2 | CO2 level, in parts per million (ppm). |
| SENSOR\_CHAN\_O2 | O2 level, in parts per million (ppm). |
| SENSOR\_CHAN\_VOC | VOC level, in parts per billion (ppb). |
| SENSOR\_CHAN\_GAS\_RES | Gas sensor resistance in ohms. |
| SENSOR\_CHAN\_VOLTAGE | Voltage, in volts. |
| SENSOR\_CHAN\_VSHUNT | Current Shunt Voltage in milli-volts. |
| SENSOR\_CHAN\_CURRENT | Current, in amps. |
| SENSOR\_CHAN\_POWER | Power in watts. |
| SENSOR\_CHAN\_RESISTANCE | Resistance , in Ohm. |
| SENSOR\_CHAN\_ROTATION | Angular rotation, in degrees. |
| SENSOR\_CHAN\_POS\_DX | Position change on the X axis, in points. |
| SENSOR\_CHAN\_POS\_DY | Position change on the Y axis, in points. |
| SENSOR\_CHAN\_POS\_DZ | Position change on the Z axis, in points. |
| SENSOR\_CHAN\_POS\_DXYZ | Position change on the X, Y and Z axis, in points. |
| SENSOR\_CHAN\_RPM | Revolutions per minute, in RPM. |
| SENSOR\_CHAN\_GAUGE\_VOLTAGE | Voltage, in volts. |
| SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT | Average current, in amps. |
| SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT | Standby current, in amps. |
| SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT | Max load current, in amps. |
| SENSOR\_CHAN\_GAUGE\_TEMP | Gauge temperature. |
| SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE | State of charge measurement in %. |
| SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY | Full Charge Capacity in mAh. |
| SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY | Remaining Charge Capacity in mAh. |
| SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY | Nominal Available Capacity in mAh. |
| SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY | Full Available Capacity in mAh. |
| SENSOR\_CHAN\_GAUGE\_AVG\_POWER | Average power in mW. |
| SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH | State of health measurement in %. |
| SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY | Time to empty in minutes. |
| SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL | Time to full in minutes. |
| SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT | Cycle count (total number of charge/discharge cycles). |
| SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE | Design voltage of cell in V (max voltage). |
| SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE | Desired voltage of cell in V (nominal voltage). |
| SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT | Desired charging current in mA. |
| SENSOR\_CHAN\_ALL | All channels. |
| SENSOR\_CHAN\_COMMON\_COUNT | Number of all common sensor channels. |
| SENSOR\_CHAN\_PRIV\_START | This and higher values are sensor specific.  Refer to the sensor header file. |
| SENSOR\_CHAN\_MAX | Maximum value describing a sensor channel type. |

## [◆ ](#ga8613a20521a37d40fd7371dc63ba2dac)sensor\_stream\_data\_opt

| enum [sensor\_stream\_data\_opt](#ga8613a20521a37d40fd7371dc63ba2dac) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Options for what to do with the associated data when a trigger is consumed.

| Enumerator | |
| --- | --- |
| SENSOR\_STREAM\_DATA\_INCLUDE | Include whatever data is associated with the trigger. |
| SENSOR\_STREAM\_DATA\_NOP | Do nothing with the associated trigger data, it may be consumed later. |
| SENSOR\_STREAM\_DATA\_DROP | Flush/clear whatever data is associated with the trigger. |

## [◆ ](#ga08215279400e8c9eb05ce4e4f0898ffd)sensor\_trigger\_type

| enum [sensor\_trigger\_type](#ga08215279400e8c9eb05ce4e4f0898ffd) |
| --- |

`#include <[sensor.h](sensor_8h.md)>`

Sensor trigger types.

| Enumerator | |
| --- | --- |
| SENSOR\_TRIG\_TIMER | Timer-based trigger, useful when the sensor does not have an interrupt line. |
| SENSOR\_TRIG\_DATA\_READY | Trigger fires whenever new data is ready. |
| SENSOR\_TRIG\_DELTA | Trigger fires when the selected channel varies significantly.  This includes any-motion detection when the channel is acceleration or gyro. If detection is based on slope between successive channel readings, the slope threshold is configured via the [SENSOR\_ATTR\_SLOPE\_TH](#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302) and [SENSOR\_ATTR\_SLOPE\_DUR](#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1) attributes. |
| SENSOR\_TRIG\_NEAR\_FAR | Trigger fires when a near/far event is detected. |
| SENSOR\_TRIG\_THRESHOLD | Trigger fires when channel reading transitions configured thresholds.  The thresholds are configured via the [SENSOR\_ATTR\_LOWER\_THRESH](#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa), [SENSOR\_ATTR\_UPPER\_THRESH](#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b), and [SENSOR\_ATTR\_HYSTERESIS](#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94) attributes. |
| SENSOR\_TRIG\_TAP | Trigger fires when a single tap is detected. |
| SENSOR\_TRIG\_DOUBLE\_TAP | Trigger fires when a double tap is detected. |
| SENSOR\_TRIG\_FREEFALL | Trigger fires when a free fall is detected. |
| SENSOR\_TRIG\_MOTION | Trigger fires when motion is detected. |
| SENSOR\_TRIG\_STATIONARY | Trigger fires when no motion has been detected for a while. |
| SENSOR\_TRIG\_FIFO\_WATERMARK | Trigger fires when the FIFO watermark has been reached. |
| SENSOR\_TRIG\_FIFO\_FULL | Trigger fires when the FIFO becomes full. |
| SENSOR\_TRIG\_COMMON\_COUNT | Number of all common sensor triggers. |
| SENSOR\_TRIG\_PRIV\_START | This and higher values are sensor specific.  Refer to the sensor header file. |
| SENSOR\_TRIG\_MAX | Maximum value describing a sensor trigger type. |

## Function Documentation

## [◆ ](#gab53418e1eb164364663d3ec3f40399a4)sensor\_10udegrees\_to\_rad()

| | void sensor\_10udegrees\_to\_rad | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *d*, | | --- | --- | --- | --- | |  |  | struct [sensor\_value](structsensor__value.md) \* | *rad* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting 10 micro degrees to radians.

Parameters
:   | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | The value (in 10 micro degrees) to be converted. |
    | --- | --- |
    | rad | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct, where the result is stored. |

## [◆ ](#gaedfdfc71dce702dc1fb1c6e60ff0f73a)sensor\_attr\_get()

| int sensor\_attr\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) | *chan*, |
|  |  | enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) | *attr*, |
|  |  | struct [sensor\_value](structsensor__value.md) \* | *val* ) |

`#include <[sensor.h](sensor_8h.md)>`

Get an attribute for a sensor.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |
    | chan | The channel the attribute belongs to, if any. Some attributes may only be set for all channels of a device, depending on device capabilities. |
    | attr | The attribute to get |
    | val | Pointer to where to store the attribute |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#gafbf65226a227e9f8824908bc38e336f5)sensor\_attr\_set()

| int sensor\_attr\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) | *chan*, |
|  |  | enum [sensor\_attribute](#ga0dcb6842bc969492bd1c9eb49708940b) | *attr*, |
|  |  | const struct [sensor\_value](structsensor__value.md) \* | *val* ) |

`#include <[sensor.h](sensor_8h.md)>`

Set an attribute for a sensor.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |
    | chan | The channel the attribute belongs to, if any. Some attributes may only be set for all channels of a device, depending on device capabilities. |
    | attr | The attribute to set |
    | val | The value to set the attribute to |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#gae95715ffea5da18a9593ec2add029824)sensor\_chan\_spec\_eq()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sensor\_chan\_spec\_eq | ( | struct [sensor\_chan\_spec](structsensor__chan__spec.md) | *chan\_spec0*, | | --- | --- | --- | --- | |  |  | struct [sensor\_chan\_spec](structsensor__chan__spec.md) | *chan\_spec1* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Check if channel specs are equivalent.

Parameters
:   | chan\_spec0 | First chan spec |
    | --- | --- |
    | chan\_spec1 | Second chan spec |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If equivalent |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If not equivalent |

## [◆ ](#ga9e0e6c1408d32c52267984bae7cb268d)sensor\_channel\_get()

| int sensor\_channel\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) | *chan*, |
|  |  | struct [sensor\_value](structsensor__value.md) \* | *val* ) |

`#include <[sensor.h](sensor_8h.md)>`

Get a reading from a sensor device.

Return a useful value for a particular channel, from the driver's internal data. Before calling this function, a sample must be obtained by calling [sensor\_sample\_fetch](#gaa75e25d93ee7cac0bf38399f3c006dff) or [sensor\_sample\_fetch\_chan](#gac16192826432438a15274cf28d66e8a6). It is guaranteed that two subsequent calls of this function for the same channels will yield the same value, if [sensor\_sample\_fetch](#gaa75e25d93ee7cac0bf38399f3c006dff) or [sensor\_sample\_fetch\_chan](#gac16192826432438a15274cf28d66e8a6) has not been called in the meantime.

For vectorial data samples you can request all axes in just one call by passing the specific channel with \_XYZ suffix. The sample will be returned at val[0], val[1] and val[2] (X, Y and Z in that order).

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |
    | chan | The channel to read |
    | val | Where to store the value |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#ga018bca56056ae2558f9e45aeb2fa5f53)sensor\_decode()

| | int sensor\_decode | ( | struct [sensor\_decode\_context](structsensor__decode__context.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | void \* | *out*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *max\_count* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Decode N frames using a [sensor\_decode\_context](structsensor__decode__context.md "Used for iterating over the data frames via the sensor_decoder_api.").

Parameters
:   | [in,out] | ctx | The context to use for decoding |
    | --- | --- | --- |
    | [out] | out | The output buffer |
    | [in] | max\_count | Maximum number of frames to decode |

Returns
:   The decode result from [sensor\_decoder\_api](structsensor__decoder__api.md "Decodes a single raw data buffer.")'s decode function

## [◆ ](#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)sensor\_degrees\_to\_rad()

| | void sensor\_degrees\_to\_rad | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *d*, | | --- | --- | --- | --- | |  |  | struct [sensor\_value](structsensor__value.md) \* | *rad* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting degrees to radians.

Parameters
:   | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | The value (in degrees) to be converted. |
    | --- | --- |
    | rad | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct, where the result is stored. |

## [◆ ](#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)sensor\_g\_to\_ms2()

| | void sensor\_g\_to\_ms2 | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *g*, | | --- | --- | --- | --- | |  |  | struct [sensor\_value](structsensor__value.md) \* | *ms2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function to convert acceleration from Gs to m/s^2.

Parameters
:   | g | The G value to be converted. |
    | --- | --- |
    | ms2 | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct, where the result is stored. |

## [◆ ](#ga12db6fc43adce48d34c25c16fd2336a3)sensor\_get\_decoder()

| int sensor\_get\_decoder | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\* | *decoder* ) |

`#include <[sensor.h](sensor_8h.md)>`

Get the sensor's decoder API.

Parameters
:   | [in] | dev | The sensor device |
    | --- | --- | --- |
    | [in] | decoder | Pointer to the decoder which will be set upon success |

Returns
:   0 on success
:   < 0 on error

## [◆ ](#gab797f2f578b1c9cc44f54ab5d503bbf8)sensor\_ms2\_to\_g()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sensor\_ms2\_to\_g | ( | const struct [sensor\_value](structsensor__value.md) \* | *ms2* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function to convert acceleration from m/s^2 to Gs.

Parameters
:   | ms2 | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct holding the acceleration, in m/s^2. |
    | --- | --- |

Returns
:   The converted value, in Gs.

## [◆ ](#ga3db980100e634310a0a1623136048742)sensor\_ms2\_to\_ug()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sensor\_ms2\_to\_ug | ( | const struct [sensor\_value](structsensor__value.md) \* | *ms2* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function to convert acceleration from m/s^2 to micro Gs.

Parameters
:   | ms2 | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct holding the acceleration, in m/s^2. |
    | --- | --- |

Returns
:   The converted value, in micro Gs.

## [◆ ](#ga2b045cdbd4d1ca37beed69970093945b)sensor\_natively\_supported\_channel\_size\_info()

| int sensor\_natively\_supported\_channel\_size\_info | ( | struct [sensor\_chan\_spec](structsensor__chan__spec.md) | *channel*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *base\_size*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *frame\_size* ) |

`#include <[sensor.h](sensor_8h.md)>`

## [◆ ](#gabb076531445e1b128d515b28c7cc9dc8)sensor\_processing\_with\_callback()

| void sensor\_processing\_with\_callback | ( | struct [rtio](structrtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [sensor\_processing\_callback\_t](#gaa8cd6e4fadb5d69e59d101733b4fb462) | *cb* ) |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for common processing of sensor data.

This function can be called in a blocking manner after [sensor\_read()](#ga1e77abad33cfd4b8330484cdc1354976) or in a standalone thread dedicated to processing. It will wait for a cqe from the RTIO context, once received, it will decode the userdata and call the `cb`. Once the `cb` returns, the buffer will be released back into `ctx's` mempool if available.

Parameters
:   | [in] | ctx | The RTIO context to wait on |
    | --- | --- | --- |
    | [in] | cb | Callback to call when data is ready for processing |

## [◆ ](#gad80093a6cfe95428dd0ead85547838a6)sensor\_rad\_to\_10udegrees()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sensor\_rad\_to\_10udegrees | ( | const struct [sensor\_value](structsensor__value.md) \* | *rad* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting radians to 10 micro degrees.

When the unit is 1 micro degree, the range that the [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) can represent is +/-2147.483 degrees. In order to increase this range, here we use 10 micro degrees as the unit.

Parameters
:   | rad | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct, holding the value in radians. |
    | --- | --- |

Returns
:   The converted value, in 10 micro degrees.

## [◆ ](#ga040a907c8934baab66d27b8dfb1ea220)sensor\_rad\_to\_degrees()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sensor\_rad\_to\_degrees | ( | const struct [sensor\_value](structsensor__value.md) \* | *rad* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting radians to degrees.

Parameters
:   | rad | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct, holding the value in radians. |
    | --- | --- |

Returns
:   The converted value, in degrees.

## [◆ ](#ga1e77abad33cfd4b8330484cdc1354976)sensor\_read()

| | int sensor\_read | ( | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | | --- | --- | --- | --- | |  |  | struct [rtio](structrtio.md) \* | *ctx*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Blocking one shot read of samples from a sensor into a buffer.

Using `cfg`, read data from the device by using the provided RTIO context `ctx`. This call will generate a [rtio\_sqe](structrtio__sqe.md "rtio_sqe") that will be given the provided buffer. The call will wait for the read to complete before returning to the caller.

Parameters
:   | [in] | iodev | The iodev created by [SENSOR\_DT\_READ\_IODEV](#ga0cc1ee28114557e9e00257071c7dfa9f) |
    | --- | --- | --- |
    | [in] | ctx | The RTIO context to service the read |
    | [in] | buf | Pointer to memory to read sample data into |
    | [in] | buf\_len | Size in bytes of the given memory that are valid to read into |

Returns
:   0 on success
:   < 0 on error

## [◆ ](#gab9eee9440b46b545b1faae224ae5949a)sensor\_read\_async\_mempool()

| | int sensor\_read\_async\_mempool | ( | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | | --- | --- | --- | --- | |  |  | struct [rtio](structrtio.md) \* | *ctx*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

One shot non-blocking read with pool allocated buffer.

Using `cfg`, read one snapshot of data from the device by using the provided RTIO context `ctx`. This call will generate a [rtio\_sqe](structrtio__sqe.md "rtio_sqe") that will leverage the RTIO's internal mempool when the time comes to service the read.

Parameters
:   | [in] | iodev | The iodev created by [SENSOR\_DT\_READ\_IODEV](#ga0cc1ee28114557e9e00257071c7dfa9f) |
    | --- | --- | --- |
    | [in] | ctx | The RTIO context to service the read |
    | [in] | userdata | Optional userdata that will be available when the read is complete |

Returns
:   0 on success
:   < 0 on error

## [◆ ](#gab854651e1b6c3206bf2b829ea5a6c420)sensor\_reconfigure\_read\_iodev()

| int sensor\_reconfigure\_read\_iodev | ( | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *sensor*, |
|  |  | const struct [sensor\_chan\_spec](structsensor__chan__spec.md) \* | *channels*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_channels* ) |

`#include <[sensor.h](sensor_8h.md)>`

Reconfigure a reading iodev.

Allows a reconfiguration of the iodev associated with reading a sample from a sensor.

**Important**: If the iodev is currently servicing a read operation, the data will likely be invalid. Please be sure the flush or wait for all pending operations to complete before using the data after a configuration change.

It is also important that the data field of the iodev is a [sensor\_read\_config](structsensor__read__config.md "sensor_read_config").

Parameters
:   | [in] | iodev | The iodev to reconfigure |
    | --- | --- | --- |
    | [in] | sensor | The sensor to read from |
    | [in] | channels | One or more channels to read |
    | [in] | num\_channels | The number of channels in `channels` |

Returns
:   0 on success
:   < 0 on error

## [◆ ](#gaa75e25d93ee7cac0bf38399f3c006dff)sensor\_sample\_fetch()

| int sensor\_sample\_fetch | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Fetch a sample from the sensor and store it in an internal driver buffer.

Read all of a sensor's active channels and, if necessary, perform any additional operations necessary to make the values useful. The user may then get individual channel values by calling [sensor\_channel\_get](#ga9e0e6c1408d32c52267984bae7cb268d).

The function blocks until the fetch operation is complete.

Since the function communicates with the sensor device, it is unsafe to call it in an ISR if the device is connected via I2C or SPI.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#gac16192826432438a15274cf28d66e8a6)sensor\_sample\_fetch\_chan()

| int sensor\_sample\_fetch\_chan | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [sensor\_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934) | *type* ) |

`#include <[sensor.h](sensor_8h.md)>`

Fetch a sample from the sensor and store it in an internal driver buffer.

Read and compute compensation for one type of sensor data (magnetometer, accelerometer, etc). The user may then get individual channel values by calling [sensor\_channel\_get](#ga9e0e6c1408d32c52267984bae7cb268d).

This is mostly implemented by multi function devices enabling reading at different sampling rates.

The function blocks until the fetch operation is complete.

Since the function communicates with the sensor device, it is unsafe to call it in an ISR if the device is connected via I2C or SPI.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |
    | type | The channel that needs updated |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#gac77fc83844935f61a2bf9ab2c38987b6)sensor\_stream()

| | int sensor\_stream | ( | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | | --- | --- | --- | --- | |  |  | struct [rtio](structrtio.md) \* | *ctx*, | |  |  | void \* | *userdata*, | |  |  | struct [rtio\_sqe](structrtio__sqe.md) \*\* | *handle* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

## [◆ ](#ga7c72aca732e0641612d2f9437c2e41b7)sensor\_trigger\_set()

| | int sensor\_trigger\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [sensor\_trigger](structsensor__trigger.md) \* | *trig*, | |  |  | [sensor\_trigger\_handler\_t](#ga890c1fb6d6974aea22a2d08829a75902) | *handler* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Activate a sensor's trigger and set the trigger handler.

The handler will be called from a thread, so I2C or SPI operations are safe. However, the thread's stack is limited and defined by the driver. It is currently up to the caller to ensure that the handler does not overflow the stack.

The user-allocated trigger will be stored by the driver as a pointer, rather than a copy, and passed back to the handler. This enables the handler to use CONTAINER\_OF to retrieve a context pointer when the trigger is embedded in a larger struct and requires that the trigger is not allocated on the stack.

Function properties (list may not be complete)
:   supervisor

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |
    | trig | The trigger to activate |
    | handler | The function that should be called when the trigger fires |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#ga28a1c6cf74a391712a4697792f759d62)sensor\_ug\_to\_ms2()

| | void sensor\_ug\_to\_ms2 | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *ug*, | | --- | --- | --- | --- | |  |  | struct [sensor\_value](structsensor__value.md) \* | *ms2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function to convert acceleration from micro Gs to m/s^2.

Parameters
:   | ug | The micro G value to be converted. |
    | --- | --- |
    | ms2 | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct, where the result is stored. |

## [◆ ](#gaf01bbb251ad0c7f6c55c5b702e8a4048)sensor\_value\_from\_double()

| | int sensor\_value\_from\_double | ( | struct [sensor\_value](structsensor__value.md) \* | *val*, | | --- | --- | --- | --- | |  |  | double | *inp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting double to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.").

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |
    | inp | The converted value. |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#ga64d5a1725eda200c80daf42b1067c46c)sensor\_value\_from\_float()

| | int sensor\_value\_from\_float | ( | struct [sensor\_value](structsensor__value.md) \* | *val*, | | --- | --- | --- | --- | |  |  | float | *inp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting float to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.").

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |
    | inp | The converted value. |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#gabff019c63c89cbc546c0981819040c99)sensor\_value\_from\_micro()

| | int sensor\_value\_from\_micro | ( | struct [sensor\_value](structsensor__value.md) \* | *val*, | | --- | --- | --- | --- | |  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | *micro* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting integer micro units to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.").

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |
    | micro | The converted value. |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#ga88b2605526e37420db871f066c5053b3)sensor\_value\_from\_milli()

| | int sensor\_value\_from\_milli | ( | struct [sensor\_value](structsensor__value.md) \* | *val*, | | --- | --- | --- | --- | |  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | *milli* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting integer milli units to struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.").

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |
    | milli | The converted value. |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#ga29223b754dc436ab1e97ce6209a3ea06)sensor\_value\_to\_double()

| | double sensor\_value\_to\_double | ( | const struct [sensor\_value](structsensor__value.md) \* | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to double.

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |

Returns
:   The converted value.

## [◆ ](#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)sensor\_value\_to\_float()

| | float sensor\_value\_to\_float | ( | const struct [sensor\_value](structsensor__value.md) \* | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to float.

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |

Returns
:   The converted value.

## [◆ ](#ga9bf7faf60aa54a7540e9b73a61864e25)sensor\_value\_to\_micro()

| | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) sensor\_value\_to\_micro | ( | const struct [sensor\_value](structsensor__value.md) \* | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to integer micro units.

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |

Returns
:   The converted value.

## [◆ ](#ga6d69a9644e08a9cd7773645fa11293e3)sensor\_value\_to\_milli()

| | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) sensor\_value\_to\_milli | ( | const struct [sensor\_value](structsensor__value.md) \* | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sensor.h](sensor_8h.md)>`

Helper function for converting struct [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") to integer milli units.

Parameters
:   | val | A pointer to a [sensor\_value](structsensor__value.md "Representation of a sensor readout value.") struct. |
    | --- | --- |

Returns
:   The converted value.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
