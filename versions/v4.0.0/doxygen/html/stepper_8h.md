---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stepper_8h.html
original_path: doxygen/html/stepper_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper.h File Reference

Public API for Stepper Driver.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <zephyr/syscalls/stepper.h>`

[Go to the source code of this file.](stepper_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MICRO\_STEP\_RES\_INDEX](group__stepper__interface.md#ga49df951f1b18bd399a609842514bdbc1)(res) |

| Enumerations | |
| --- | --- |
| enum | [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) {     [STEPPER\_MICRO\_STEP\_1](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) = 1 , [STEPPER\_MICRO\_STEP\_2](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) = 2 , [STEPPER\_MICRO\_STEP\_4](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) = 4 , [STEPPER\_MICRO\_STEP\_8](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) = 8 ,     [STEPPER\_MICRO\_STEP\_16](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) = 16 , [STEPPER\_MICRO\_STEP\_32](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) = 32 , [STEPPER\_MICRO\_STEP\_64](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) = 64 , [STEPPER\_MICRO\_STEP\_128](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) = 128 ,     [STEPPER\_MICRO\_STEP\_256](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) = 256   } |
|  | Stepper Motor micro step resolution options. [More...](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) |
| enum | [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) { [STEPPER\_DIRECTION\_NEGATIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) = 0 , [STEPPER\_DIRECTION\_POSITIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) = 1 } |
|  | Stepper Motor direction options. [More...](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) |
| enum | [stepper\_run\_mode](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239) { [STEPPER\_RUN\_MODE\_HOLD](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) = 0 , [STEPPER\_RUN\_MODE\_POSITION](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) = 1 , [STEPPER\_RUN\_MODE\_VELOCITY](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) = 2 } |
|  | Stepper Motor run mode options. [More...](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239) |
| enum | [stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) { [STEPPER\_EVENT\_STEPS\_COMPLETED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) = 0 , [STEPPER\_EVENT\_STALL\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) = 1 , [STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) = 2 , [STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) = 3 } |
|  | Stepper Events. [More...](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) |

| Functions | |
| --- | --- |
| int | [stepper\_enable](group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or Disable Motor Controller. |
| int | [stepper\_move](group__stepper__interface.md#ga7622a8e1e95b2bbb2dc1273bd84e88a5) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps) |
|  | Set the micro\_steps to be moved from the current position i.e. |
| int | [stepper\_set\_max\_velocity](group__stepper__interface.md#gabbb691c2f1beb2bdc7e856a7f77b4de4) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) micro\_steps\_per\_second) |
|  | Set the target velocity to be reached by the motor. |
| int | [stepper\_set\_micro\_step\_res](group__stepper__interface.md#gac3f2e315551e11500513dac837567625) (const struct [device](structdevice.md) \*dev, enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution) |
|  | Set the microstep resolution in stepper motor controller. |
| int | [stepper\_get\_micro\_step\_res](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e) (const struct [device](structdevice.md) \*dev, enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution) |
|  | Get the microstep resolution in stepper motor controller. |
| int | [stepper\_set\_actual\_position](group__stepper__interface.md#gaf312a93167aabb39d814c6548991d6c6) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set the actual a.k.a reference position of the stepper. |
| int | [stepper\_get\_actual\_position](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Get the actual a.k.a reference position of the stepper. |
| int | [stepper\_set\_target\_position](group__stepper__interface.md#ga2417b3ca2f77553bcd6a8b909e5f4d27) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set the absolute target position of the stepper. |
| int | [stepper\_is\_moving](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*is\_moving) |
|  | Check if the stepper motor is currently moving. |
| int | [stepper\_enable\_constant\_velocity\_mode](group__stepper__interface.md#ga430250f6e3544e5bba49d5b6ceba1bf9) (const struct [device](structdevice.md) \*dev, enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Enable constant velocity mode for the stepper with a given velocity. |
| int | [stepper\_set\_callback](group__stepper__interface.md#gaeaaab5037a4c0f4e5aa9ebc12340517c) (const struct [device](structdevice.md) \*dev, stepper\_event\_callback\_t callback, void \*user\_data) |
|  | Set the callback function to be called when a stepper event occurs. |

## Detailed Description

Public API for Stepper Driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper.h](stepper_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
