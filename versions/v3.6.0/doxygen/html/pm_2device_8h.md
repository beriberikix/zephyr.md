---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pm_2device_8h.html
original_path: doxygen/html/pm_2device_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](pm_2device_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pm\_device\_base](structpm__device__base.md) |
|  | Device PM info. [More...](structpm__device__base.md#details) |
| struct | [pm\_device](structpm__device.md) |
|  | Runtime PM info for device with generic PM. [More...](structpm__device.md#details) |
| struct | [pm\_device\_isr](structpm__device__isr.md) |
|  | Runtime PM info for device with synchronous PM. [More...](structpm__device__isr.md#details) |

| Macros | |
| --- | --- |
| #define | [PM\_DEVICE\_ISR\_SAFE](group__subsys__pm__device.md#ga18bb96fc4d5003516ab2eaf73cb35912)   1 |
|  | Flag indicating that runtime PM API for the device can be called from any context. |
| #define | [PM\_DEVICE\_DEFINE](group__subsys__pm__device.md#gae85fb5a7c31863a3663cef8dd7229c6c)(dev\_id, pm\_action\_cb, ...) |
|  | Define device PM resources for the given device name. |
| #define | [PM\_DEVICE\_DT\_DEFINE](group__subsys__pm__device.md#gaa2bd2c490fee99a6fc2b23605e799ef0)(node\_id, pm\_action\_cb, ...) |
|  | Define device PM resources for the given node identifier. |
| #define | [PM\_DEVICE\_DT\_INST\_DEFINE](group__subsys__pm__device.md#ga5b201836d9c19a1c87cdde93631a4b0c)(idx, pm\_action\_cb, ...) |
|  | Define device PM resources for the given instance. |
| #define | [PM\_DEVICE\_GET](group__subsys__pm__device.md#gaa94d19d0590659b7aba83566de9bd0c5)(dev\_id) |
|  | Obtain a reference to the device PM resources for the given device. |
| #define | [PM\_DEVICE\_DT\_GET](group__subsys__pm__device.md#gad244d742bc6b9874bfb90a2c3c87c4e8)(node\_id) |
|  | Obtain a reference to the device PM resources for the given node. |
| #define | [PM\_DEVICE\_DT\_INST\_GET](group__subsys__pm__device.md#ga52892f2c34f6ccc9598002625baf12ce)(idx) |
|  | Obtain a reference to the device PM resources for the given instance. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179)) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) action) |
|  | Device PM action callback. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pm\_device\_action\_failed\_cb\_t](group__subsys__pm__device.md#ga9cfb6437873089714635d2b26aafefac)) (const struct [device](structdevice.md) \*dev, int err) |
|  | Device PM action failed callback. |

| Enumerations | |
| --- | --- |
| enum | [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) { [PM\_DEVICE\_STATE\_ACTIVE](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7) , [PM\_DEVICE\_STATE\_SUSPENDED](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5) , [PM\_DEVICE\_STATE\_SUSPENDING](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a51a5904aff980deff73d29568b6f7deb) , [PM\_DEVICE\_STATE\_OFF](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2) } |
|  | Device power states. [More...](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) |
| enum | [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) { [PM\_DEVICE\_ACTION\_SUSPEND](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca5b7ae11deaee85eb0b8452bc89383790) , [PM\_DEVICE\_ACTION\_RESUME](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564) , [PM\_DEVICE\_ACTION\_TURN\_OFF](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca2bcd7dee3a85b27157bbc465bacf521e) , [PM\_DEVICE\_ACTION\_TURN\_ON](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544) } |
|  | Device PM actions. [More...](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) |

| Functions | |
| --- | --- |
| const char \* | [pm\_device\_state\_str](group__subsys__pm__device.md#gad109511e4314fa6145ee97dd655ec7bb) (enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get name of device PM state. |
| int | [pm\_device\_action\_run](group__subsys__pm__device.md#ga3840d6e7832a00b93763247a5951bfde) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) action) |
|  | Run a pm action on a device. |
| void | [pm\_device\_children\_action\_run](group__subsys__pm__device.md#ga765a5412f66070ccefd8e80ed9f62b1b) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) action, [pm\_device\_action\_failed\_cb\_t](group__subsys__pm__device.md#ga9cfb6437873089714635d2b26aafefac) failure\_cb) |
|  | Run a pm action on all children of a device. |
| int | [pm\_device\_state\_get](group__subsys__pm__device.md#gaffcf0aea5df10657235d4ed1f8c74d5a) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Obtain the power state of a device. |
| static void | [pm\_device\_init\_suspended](group__subsys__pm__device.md#ga4c366f49e326a8b8e01d90cb2ee424ba) (const struct [device](structdevice.md) \*dev) |
|  | Initialize a device state to [PM\_DEVICE\_STATE\_SUSPENDED](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5 "Device is suspended."). |
| static void | [pm\_device\_init\_off](group__subsys__pm__device.md#gafb12ecf4679dd449e2faad0ede2c75fd) (const struct [device](structdevice.md) \*dev) |
|  | Initialize a device state to [PM\_DEVICE\_STATE\_OFF](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2 "Device is turned off (power removed)."). |
| void | [pm\_device\_busy\_set](group__subsys__pm__device.md#ga7ea002352f3d1c90aecff1d54c255a06) (const struct [device](structdevice.md) \*dev) |
|  | Mark a device as busy. |
| void | [pm\_device\_busy\_clear](group__subsys__pm__device.md#ga8b527314f0c61b85602876b4f5a52275) (const struct [device](structdevice.md) \*dev) |
|  | Clear a device busy status. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_is\_any\_busy](group__subsys__pm__device.md#gae59a1fbcd2399717076fbfcee1e5e411) (void) |
|  | Check if any device is busy. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_is\_busy](group__subsys__pm__device.md#ga8ff7c3197d5ded860878302d00ac709c) (const struct [device](structdevice.md) \*dev) |
|  | Check if a device is busy. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_wakeup\_enable](group__subsys__pm__device.md#ga74fde62f71393fb9863916b3a2e5c460) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or disable a device as a wake up source. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_wakeup\_is\_enabled](group__subsys__pm__device.md#ga0716c6158804ac48022280d8d237f8c1) (const struct [device](structdevice.md) \*dev) |
|  | Check if a device is enabled as a wake up source. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_wakeup\_is\_capable](group__subsys__pm__device.md#gac818aafb748b57d70909808b45d89379) (const struct [device](structdevice.md) \*dev) |
|  | Check if a device is wake up capable. |
| void | [pm\_device\_state\_lock](group__subsys__pm__device.md#gaab27e932950e1063b2f1f4c4e19dbf01) (const struct [device](structdevice.md) \*dev) |
|  | Lock current device state. |
| void | [pm\_device\_state\_unlock](group__subsys__pm__device.md#gaa5d2387a01a4ca4d765b1ea2361155bb) (const struct [device](structdevice.md) \*dev) |
|  | Unlock the current device state. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_state\_is\_locked](group__subsys__pm__device.md#gaf577cada579b6f871bc55e4a282ef8a6) (const struct [device](structdevice.md) \*dev) |
|  | Check if the device pm is locked. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_on\_power\_domain](group__subsys__pm__device.md#ga32eb5e210d2f0ba533b0185a94c8744e) (const struct [device](structdevice.md) \*dev) |
|  | Check if the device is on a switchable power domain. |
| int | [pm\_device\_power\_domain\_add](group__subsys__pm__device.md#gaa10a3f1ce71409cb591db416a1611377) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*domain) |
|  | Add a device to a power domain. |
| int | [pm\_device\_power\_domain\_remove](group__subsys__pm__device.md#ga1d7ab9b0b497e016b9b22d2506cd23f9) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*domain) |
|  | Remove a device from a power domain. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_is\_powered](group__subsys__pm__device.md#ga9e926dffd7eafc567499ce1ea537486b) (const struct [device](structdevice.md) \*dev) |
|  | Check if the device is currently powered. |
| int | [pm\_device\_driver\_init](group__subsys__pm__device.md#gad563094c2d4ad066bc4ce30586e13fb3) (const struct [device](structdevice.md) \*dev, [pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179) action\_cb) |
|  | Setup a device driver into the lowest valid power mode. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [device.h](pm_2device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
