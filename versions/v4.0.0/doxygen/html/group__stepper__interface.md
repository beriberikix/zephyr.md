---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__stepper__interface.html
original_path: doxygen/html/group__stepper__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Stepper Controller Interface

[Device Driver APIs](group__io__interfaces.md)

Stepper Controller Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Trinamic Stepper Controller Interface](group__trinamic__stepper__interface.md) |
|  | Trinamic Stepper Controller Interface. |

| Macros | |
| --- | --- |
| #define | [MICRO\_STEP\_RES\_INDEX](#ga49df951f1b18bd399a609842514bdbc1)(res) |

| Enumerations | |
| --- | --- |
| enum | [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) {     [STEPPER\_MICRO\_STEP\_1](#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) = 1 , [STEPPER\_MICRO\_STEP\_2](#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) = 2 , [STEPPER\_MICRO\_STEP\_4](#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) = 4 , [STEPPER\_MICRO\_STEP\_8](#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) = 8 ,     [STEPPER\_MICRO\_STEP\_16](#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) = 16 , [STEPPER\_MICRO\_STEP\_32](#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) = 32 , [STEPPER\_MICRO\_STEP\_64](#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) = 64 , [STEPPER\_MICRO\_STEP\_128](#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) = 128 ,     [STEPPER\_MICRO\_STEP\_256](#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) = 256   } |
|  | Stepper Motor micro step resolution options. [More...](#gad8d053f92eb3a194652b4600af531e30) |
| enum | [stepper\_direction](#ga04be36af941edfd3a52fda2fb0ee2a01) { [STEPPER\_DIRECTION\_NEGATIVE](#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) = 0 , [STEPPER\_DIRECTION\_POSITIVE](#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) = 1 } |
|  | Stepper Motor direction options. [More...](#ga04be36af941edfd3a52fda2fb0ee2a01) |
| enum | [stepper\_run\_mode](#ga5f9c911155e7c19afa4dc6827313c239) { [STEPPER\_RUN\_MODE\_HOLD](#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) = 0 , [STEPPER\_RUN\_MODE\_POSITION](#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) = 1 , [STEPPER\_RUN\_MODE\_VELOCITY](#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) = 2 } |
|  | Stepper Motor run mode options. [More...](#ga5f9c911155e7c19afa4dc6827313c239) |
| enum | [stepper\_event](#gab1534238fbf8d2270ea4f69d3a558b5f) { [STEPPER\_EVENT\_STEPS\_COMPLETED](#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) = 0 , [STEPPER\_EVENT\_STALL\_DETECTED](#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) = 1 , [STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) = 2 , [STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) = 3 } |
|  | Stepper Events. [More...](#gab1534238fbf8d2270ea4f69d3a558b5f) |

| Functions | |
| --- | --- |
| int | [stepper\_enable](#ga3fbda29131df4618204f7df86b82f450) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or Disable Motor Controller. |
| int | [stepper\_move](#ga7622a8e1e95b2bbb2dc1273bd84e88a5) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps) |
|  | Set the micro\_steps to be moved from the current position i.e. |
| int | [stepper\_set\_max\_velocity](#gabbb691c2f1beb2bdc7e856a7f77b4de4) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) micro\_steps\_per\_second) |
|  | Set the target velocity to be reached by the motor. |
| int | [stepper\_set\_micro\_step\_res](#gac3f2e315551e11500513dac837567625) (const struct [device](structdevice.md) \*dev, enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) resolution) |
|  | Set the microstep resolution in stepper motor controller. |
| int | [stepper\_get\_micro\_step\_res](#ga72c54073cd703fd747533c01a447113e) (const struct [device](structdevice.md) \*dev, enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) \*resolution) |
|  | Get the microstep resolution in stepper motor controller. |
| int | [stepper\_set\_actual\_position](#gaf312a93167aabb39d814c6548991d6c6) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set the actual a.k.a reference position of the stepper. |
| int | [stepper\_get\_actual\_position](#ga6880673dcb5648c3da139a980d319157) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Get the actual a.k.a reference position of the stepper. |
| int | [stepper\_set\_target\_position](#ga2417b3ca2f77553bcd6a8b909e5f4d27) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set the absolute target position of the stepper. |
| int | [stepper\_is\_moving](#gaaba23377932454df4eb5a43437beb18c) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*is\_moving) |
|  | Check if the stepper motor is currently moving. |
| int | [stepper\_enable\_constant\_velocity\_mode](#ga430250f6e3544e5bba49d5b6ceba1bf9) (const struct [device](structdevice.md) \*dev, enum [stepper\_direction](#ga04be36af941edfd3a52fda2fb0ee2a01) direction, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Enable constant velocity mode for the stepper with a given velocity. |
| int | [stepper\_set\_callback](#gaeaaab5037a4c0f4e5aa9ebc12340517c) (const struct [device](structdevice.md) \*dev, stepper\_event\_callback\_t callback, void \*user\_data) |
|  | Set the callback function to be called when a stepper event occurs. |

## Detailed Description

Stepper Controller Interface.

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

**Definition** util.h:702

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
| STEPPER\_EVENT\_STEPS\_COMPLETED | Steps set using move or set\_target\_position have been executed. |
| STEPPER\_EVENT\_STALL\_DETECTED | Stall detected. |
| STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED | Left end switch status changes to pressed. |
| STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED | Right end switch status changes to pressed. |

## [◆ ](#gad8d053f92eb3a194652b4600af531e30)stepper\_micro\_step\_resolution

| enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) |
| --- |

`#include <[stepper.h](stepper_8h.md)>`

Stepper Motor micro step resolution options.

| Enumerator | |
| --- | --- |
| STEPPER\_MICRO\_STEP\_1 | Full step resolution. |
| STEPPER\_MICRO\_STEP\_2 | 2 micro steps per full step |
| STEPPER\_MICRO\_STEP\_4 | 4 micro steps per full step |
| STEPPER\_MICRO\_STEP\_8 | 8 micro steps per full step |
| STEPPER\_MICRO\_STEP\_16 | 16 micro steps per full step |
| STEPPER\_MICRO\_STEP\_32 | 32 micro steps per full step |
| STEPPER\_MICRO\_STEP\_64 | 64 micro steps per full step |
| STEPPER\_MICRO\_STEP\_128 | 128 micro steps per full step |
| STEPPER\_MICRO\_STEP\_256 | 256 micro steps per full step |

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

Enable or Disable Motor Controller.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | enable | Input enable or disable motor controller |

Return values
:   | -EIO | Error during Enabling |
    | --- | --- |
    | 0 | Success |

## [◆ ](#ga430250f6e3544e5bba49d5b6ceba1bf9)stepper\_enable\_constant\_velocity\_mode()

| int stepper\_enable\_constant\_velocity\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [stepper\_direction](#ga04be36af941edfd3a52fda2fb0ee2a01) | *direction*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value* ) |

`#include <[stepper.h](stepper_8h.md)>`

Enable constant velocity mode for the stepper with a given velocity.

activate constant velocity mode with the given velocity in micro\_steps\_per\_second. If velocity > 0, motor shall be set into motion and run incessantly until and unless stalled or stopped using some other command, for instance, motor\_enable(false).

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | direction | The direction to set |
    | value | The velocity to set in steps per second where one step is dependent on the current microstepping resolution: 0: Enable constant velocity mode with the given velocity in a given direction 0: Disable constant velocity mode |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#ga6880673dcb5648c3da139a980d319157)stepper\_get\_actual\_position()

| int stepper\_get\_actual\_position | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *value* ) |

`#include <[stepper.h](stepper_8h.md)>`

Get the actual a.k.a reference position of the stepper.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | value | The actual position to get in micro\_steps |

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

Get the microstep resolution in stepper motor controller.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | resolution | microstep resolution |

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

Check if the stepper motor is currently moving.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | is\_moving | Pointer to a boolean to store the moving status of the stepper motor |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#ga7622a8e1e95b2bbb2dc1273bd84e88a5)stepper\_move()

| int stepper\_move | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *micro\_steps* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the micro\_steps to be moved from the current position i.e.

relative movement

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | micro\_steps | target micro\_steps to be moved from the current position |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | 0 | Success |

## [◆ ](#gaf312a93167aabb39d814c6548991d6c6)stepper\_set\_actual\_position()

| int stepper\_set\_actual\_position | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *value* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the actual a.k.a reference position of the stepper.

Parameters
:   | dev | Pointer to the stepper motor controller instance. |
    | --- | --- |
    | value | The reference position to set in micro-steps. |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

## [◆ ](#gaeaaab5037a4c0f4e5aa9ebc12340517c)stepper\_set\_callback()

| int stepper\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | stepper\_event\_callback\_t | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the callback function to be called when a stepper event occurs.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | callback | Callback function to be called when a stepper event occurs passing NULL will disable the callback |
    | user\_data | User data to be passed to the callback function |

Return values
:   | -ENOSYS | If not implemented by device driver |
    | --- | --- |
    | 0 | Success |

## [◆ ](#gabbb691c2f1beb2bdc7e856a7f77b4de4)stepper\_set\_max\_velocity()

| int stepper\_set\_max\_velocity | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *micro\_steps\_per\_second* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the target velocity to be reached by the motor.

For controllers such as DRV8825 where you toggle the STEP Pin, the pulse\_length would have to be calculated based on this parameter in the driver. For controllers where velocity can be set, this parameter corresponds to max\_velocity

Note
:   Setting max velocity does not set the motor into motion, a combination of set\_max\_velocity and move is required to set the motor into motion.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | micro\_steps\_per\_second | speed in micro\_steps per second |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -EINVAL | If the requested velocity is not supported |
    | 0 | Success |

## [◆ ](#gac3f2e315551e11500513dac837567625)stepper\_set\_micro\_step\_res()

| int stepper\_set\_micro\_step\_res | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [stepper\_micro\_step\_resolution](#gad8d053f92eb3a194652b4600af531e30) | *resolution* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the microstep resolution in stepper motor controller.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | resolution | microstep resolution |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | -ENOTSUP | If the requested resolution is not supported |
    | 0 | Success |

## [◆ ](#ga2417b3ca2f77553bcd6a8b909e5f4d27)stepper\_set\_target\_position()

| int stepper\_set\_target\_position | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *value* ) |

`#include <[stepper.h](stepper_8h.md)>`

Set the absolute target position of the stepper.

Parameters
:   | dev | pointer to the stepper motor controller instance |
    | --- | --- |
    | value | target position to set in micro\_steps |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
