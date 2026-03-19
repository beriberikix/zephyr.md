---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__stepper__interface.html
original_path: doxygen/html/group__stepper__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Stepper Driver Interface

[Device Driver APIs](group__io__interfaces.md)

Stepper Driver Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Trinamic Stepper Controller Interface](group__trinamic__stepper__interface.md) |
|  | Trinamic Stepper Controller Interface. |

| Macros | |
| --- | --- |
| #define | [MICRO\_STEP\_RES\_INDEX](#ga49df951f1b18bd399a609842514bdbc1)(res) |
|  | Macro to calculate the index of the microstep resolution. |

| Enumerations | |
| --- | --- |
| enum | [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) {     [STEPPER\_MICRO\_STEP\_1](#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) = 1 , [STEPPER\_MICRO\_STEP\_2](#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) = 2 , [STEPPER\_MICRO\_STEP\_4](#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) = 4 , [STEPPER\_MICRO\_STEP\_8](#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) = 8 ,     [STEPPER\_MICRO\_STEP\_16](#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) = 16 , [STEPPER\_MICRO\_STEP\_32](#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) = 32 , [STEPPER\_MICRO\_STEP\_64](#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) = 64 , [STEPPER\_MICRO\_STEP\_128](#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) = 128 ,     [STEPPER\_MICRO\_STEP\_256](#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) = 256   } |
|  | Stepper Motor micro-step resolution options. [More...](#gad8d053f92eb3a194652b4600af531e30) |
| enum | [stepper\_direction](#ga04be36af941edfd3a52fda2fb0ee2a01) { [STEPPER\_DIRECTION\_NEGATIVE](#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) = 0 , [STEPPER\_DIRECTION\_POSITIVE](#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) = 1 } |
|  | Stepper Motor direction options. [More...](#ga04be36af941edfd3a52fda2fb0ee2a01) |
| enum | [stepper\_run\_mode](#ga5f9c911155e7c19afa4dc6827313c239) { [STEPPER\_RUN\_MODE\_HOLD](#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) = 0 , [STEPPER\_RUN\_MODE\_POSITION](#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) = 1 , [STEPPER\_RUN\_MODE\_VELOCITY](#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) = 2 } |
|  | Stepper Motor run mode options. [More...](#ga5f9c911155e7c19afa4dc6827313c239) |
| enum | [stepper\_event](#gab1534238fbf8d2270ea4f69d3a558b5f) { [STEPPER\_EVENT\_STEPS\_COMPLETED](#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) = 0 , [STEPPER\_EVENT\_STALL\_DETECTED](#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) = 1 , [STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) = 2 , [STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) = 3 } |
|  | Stepper Events. [More...](#gab1534238fbf8d2270ea4f69d3a558b5f) |

| Functions | |
| --- | --- |
| int | [stepper\_enable](#ga3fbda29131df4618204f7df86b82f450) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or disable stepper driver. |
| int | [stepper\_set\_micro\_step\_res](#gac3f2e315551e11500513dac837567625) (const struct [device](structdevice.md) \*dev, enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) resolution) |
|  | Set the micro-step resolution in stepper driver. |
| int | [stepper\_get\_micro\_step\_res](#ga72c54073cd703fd747533c01a447113e) (const struct [device](structdevice.md) \*dev, enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) \*resolution) |
|  | Get the micro-step resolution in stepper driver. |
| int | [stepper\_set\_reference\_position](#ga472ba1e64876fcaf79ba95edd8261a36) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set the reference position of the stepper. |
| int | [stepper\_get\_actual\_position](#ga6880673dcb5648c3da139a980d319157) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Get the actual a.k.a reference position of the stepper. |
| int | [stepper\_set\_event\_callback](#gad44cc67d4667114c933d82f527ad2b77) (const struct [device](structdevice.md) \*dev, stepper\_event\_callback\_t callback, void \*user\_data) |
|  | Set the callback function to be called when a stepper event occurs. |
| int | [stepper\_set\_microstep\_interval](#ga5faf922c228ace81cc0341fc0931d7f7) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) microstep\_interval\_ns) |
|  | Set the time interval between steps in nanoseconds. |
| int | [stepper\_move\_by](#ga851c6b8f0cfe485095f345f33186535a) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps) |
|  | Set the micro-steps to be moved from the current position i.e. |
| int | [stepper\_move\_to](#ga7d12d3ff146698662090d8b761a57615) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps) |
|  | Set the absolute target position of the stepper. |
| int | [stepper\_run](#ga911eda0a495ab7b9c34b05c09b06ac87) (const struct [device](structdevice.md) \*dev, enum [stepper\_direction](#ga04be36af941edfd3a52fda2fb0ee2a01) direction) |
|  | Run the stepper with a given step interval in a given direction. |
| int | [stepper\_is\_moving](#gaaba23377932454df4eb5a43437beb18c) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*is\_moving) |
|  | Check if the stepper is currently moving. |

## Detailed Description

Stepper Driver Interface.

Since
:   4.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga49df951f1b18bd399a609842514bdbc1)MICRO\_STEP\_RES\_INDEX

| #define MICRO\_STEP\_RES\_INDEX | ( |  | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[stepper.h](stepper_8h.md)>`

**Value:**

[LOG2](group__sys-util.md#ga40805b5dd56ee36df59a7bbe403ddf33)(res)

[LOG2](group__sys-util.md#ga40805b5dd56ee36df59a7bbe403ddf33)

#define LOG2(x)

Compute log2(x).

**Definition** util.h:703

Macro to calculate the index of the microstep resolution.

Parameters
:   | res | Microstep resolution |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga04be36af941edfd3a52fda2fb0ee2a01)stepper\_direction

| enum [stepper\_direction](#ga04be36af941edfd3a52fda2fb0ee2a01) |
| --- |

`#include <[stepper.h](stepper_8h.md)>`

Stepper Motor direction options.

| Enumerator | |
| --- | --- |
| STEPPER\_DIRECTION\_NEGATIVE | Negative direction. |
| STEPPER\_DIRECTION\_POSITIVE | Positive direction. |

## [◆ ](#gab1534238fbf8d2270ea4f69d3a558b5f)stepper\_event

| enum [stepper\_event](#gab1534238fbf8d2270ea4f69d3a558b5f) |
| --- |

`#include <[stepper.h](stepper_8h.md)>`

Stepper Events.

| Enumerator | |
| --- | --- |
| STEPPER\_EVENT\_STEPS\_COMPLETED | Steps set using move\_by or move\_to have been executed. |
| STEPPER\_EVENT\_STALL\_DETECTED | Stall detected. |
| STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED | Left end switch status changes to pressed. |
| STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED | Right end switch status changes to pressed. |

## [◆ ](#gad8d053f92eb3a194652b4600af531e30)stepper\_micro\_step\_resolution

| enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) |
| --- |

`#include <[stepper.h](stepper_8h.md)>`

Stepper Motor micro-step resolution options.

| Enumerator | |
| --- | --- |
| STEPPER\_MICRO\_STEP\_1 | Full step resolution. |
| STEPPER\_MICRO\_STEP\_2 | 2 micro-steps per full step |
| STEPPER\_MICRO\_STEP\_4 | 4 micro-steps per full step |
| STEPPER\_MICRO\_STEP\_8 | 8 micro-steps per full step |
| STEPPER\_MICRO\_STEP\_16 | 16 micro-steps per full step |
| STEPPER\_MICRO\_STEP\_32 | 32 micro-steps per full step |
| STEPPER\_MICRO\_STEP\_64 | 64 micro-steps per full step |
| STEPPER\_MICRO\_STEP\_128 | 128 micro-steps per full step |
| STEPPER\_MICRO\_STEP\_256 | 256 micro-steps per full step |

## [◆ ](#ga5f9c911155e7c19afa4dc6827313c239)stepper\_run\_mode

| enum [stepper\_run\_mode](#ga5f9c911155e7c19afa4dc6827313c239) |
| --- |

`#include <[stepper.h](stepper_8h.md)>`

Stepper Motor run mode options.

| Enumerator | |
| --- | --- |
| STEPPER\_RUN\_MODE\_HOLD | Hold Mode. |
| STEPPER\_RUN\_MODE\_POSITION | Position Mode. |
| STEPPER\_RUN\_MODE\_VELOCITY | Velocity Mode. |

## Function Documentation

## [◆ ](#ga3fbda29131df4618204f7df86b82f450)stepper\_enable()

| int stepper\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[stepper.h](stepper_8h.md)>`

Enable or disable stepper driver.

Enabling the driver will energize the coils, however not set the stepper in motion. Disabling the driver will de-energize the coils.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | enable | Input enable or disable stepper driver |

Return values
:   | -EIO | Error during Enabling |
    | --- | --- |
    | 0 | Success |

## [◆ ](#ga6880673dcb5648c3da139a980d319157)stepper\_get\_actual\_position()

| int stepper\_get\_actual\_position | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *value* ) |

`#include <[stepper.h](stepper_8h.md)>`

Get the actual a.k.a reference position of the stepper.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | value | The actual position to get in micro-steps |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#ga72c54073cd703fd747533c01a447113e)stepper\_get\_micro\_step\_res()

| int stepper\_get\_micro\_step\_res | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) \* | *resolution* ) |

`#include <[stepper.h](stepper_8h.md)>`

Get the micro-step resolution in stepper driver.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | resolution | micro-step resolution |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#gaaba23377932454df4eb5a43437beb18c)stepper\_is\_moving()

| int stepper\_is\_moving | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *is\_moving* ) |

`#include <[stepper.h](stepper_8h.md)>`

Check if the stepper is currently moving.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | is\_moving | Pointer to a boolean to store the moving status of the stepper |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#ga851c6b8f0cfe485095f345f33186535a)stepper\_move\_by()

| int stepper\_move\_by | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *micro\_steps* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the micro-steps to be moved from the current position i.e.

relative movement

The stepper will move by the given number of micro-steps from the current position. This function is non-blocking.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | micro\_steps | target micro-steps to be moved from the current position |

Return values
:   | -ECANCELED | If the stepper is disabled |
    | --- | --- |
    | -EIO | General input / output error |
    | 0 | Success |

## [◆ ](#ga7d12d3ff146698662090d8b761a57615)stepper\_move\_to()

| int stepper\_move\_to | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *micro\_steps* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the absolute target position of the stepper.

The stepper will move to the given micro-steps position from the reference position. This function is non-blocking.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | micro\_steps | target position to set in micro-steps |

Return values
:   | -ECANCELED | If the stepper is disabled |
    | --- | --- |
    | -EIO | General input / output error |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#ga911eda0a495ab7b9c34b05c09b06ac87)stepper\_run()

| int stepper\_run | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [stepper\_direction](#ga04be36af941edfd3a52fda2fb0ee2a01) | *direction* ) |

`#include <[stepper.h](stepper_8h.md)>`

Run the stepper with a given step interval in a given direction.

The stepper shall be set into motion and run continuously until stalled or stopped using some other command, for instance, stepper\_enable(false). This function is non-blocking.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | direction | The direction to set |

Return values
:   | -ECANCELED | If the stepper is disabled |
    | --- | --- |
    | -EIO | General input / output error |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#gad44cc67d4667114c933d82f527ad2b77)stepper\_set\_event\_callback()

| int stepper\_set\_event\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | stepper\_event\_callback\_t | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the callback function to be called when a stepper event occurs.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | callback | Callback function to be called when a stepper event occurs passing NULL will disable the callback |
    | user\_data | User data to be passed to the callback function |

Return values
:   | -ENOSYS | If not implemented by device driver |
    | --- | --- |
    | 0 | Success |

## [◆ ](#gac3f2e315551e11500513dac837567625)stepper\_set\_micro\_step\_res()

| int stepper\_set\_micro\_step\_res | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) | *resolution* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the micro-step resolution in stepper driver.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | resolution | micro-step resolution |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | -ENOTSUP | If the requested resolution is not supported |
    | 0 | Success |

## [◆ ](#ga5faf922c228ace81cc0341fc0931d7f7)stepper\_set\_microstep\_interval()

| int stepper\_set\_microstep\_interval | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *microstep\_interval\_ns* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the time interval between steps in nanoseconds.

Note
:   Setting step interval does not set the stepper into motion, a combination of set\_microstep\_interval and move is required to set the stepper into motion.

Parameters
:   | dev | pointer to the stepper driver instance |
    | --- | --- |
    | microstep\_interval\_ns | time interval between steps in nanoseconds |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -EINVAL | If the requested step interval is not supported |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#ga472ba1e64876fcaf79ba95edd8261a36)stepper\_set\_reference\_position()

| int stepper\_set\_reference\_position | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *value* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the reference position of the stepper.

Parameters
:   | dev | Pointer to the stepper driver instance. |
    | --- | --- |
    | value | The reference position to set in micro-steps. |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
