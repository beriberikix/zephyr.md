---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbc__ppc_8h.html
original_path: doxygen/html/usbc__ppc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_ppc.h File Reference

USB Type-C Power Path Controller device API.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`

[Go to the source code of this file.](usbc__ppc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usbc\_ppc\_drv](structusbc__ppc__drv.md) |
|  | Structure with pointers to the functions implemented by driver. [More...](structusbc__ppc__drv.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usbc\_ppc\_event\_cb\_t](#a8195a7a51eb5bd3cbcec985b97b84e73)) (const struct [device](structdevice.md) \*dev, void \*data, enum [usbc\_ppc\_event](#a3dbbb1a6701a3a79c9a1d148b239fcf9) ev) |

| Enumerations | |
| --- | --- |
| enum | [usbc\_ppc\_event](#a3dbbb1a6701a3a79c9a1d148b239fcf9) {     [USBC\_PPC\_EVENT\_DEAD\_BATTERY\_ERROR](#a3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e) = 0 , [USBC\_PPC\_EVENT\_SRC\_OVERVOLTAGE](#a3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109) , [USBC\_PPC\_EVENT\_SRC\_REVERSE\_CURRENT](#a3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6) , [USBC\_PPC\_EVENT\_SRC\_OVERCURRENT](#a3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238) ,     [USBC\_PPC\_EVENT\_SRC\_SHORT](#a3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4) , [USBC\_PPC\_EVENT\_OVER\_TEMPERATURE](#a3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c) , [USBC\_PPC\_EVENT\_BOTH\_SNKSRC\_ENABLED](#a3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94) , [USBC\_PPC\_EVENT\_SNK\_REVERSE\_CURRENT](#a3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759) ,     [USBC\_PPC\_EVENT\_SNK\_SHORT](#a3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d) , [USBC\_PPC\_EVENT\_SNK\_OVERVOLTAGE](#a3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e)   } |
|  | Type of event being notified by Power Path Controller. [More...](#a3dbbb1a6701a3a79c9a1d148b239fcf9) |

| Functions | |
| --- | --- |
| static int | [ppc\_is\_dead\_battery\_mode](#a5f70af9a0d0336c208ff4f7a90c4b665) (const struct [device](structdevice.md) \*dev) |
|  | Check if PPC is in the dead battery mode. |
| static int | [ppc\_exit\_dead\_battery\_mode](#abcbebdf47ca1c8a9b7c2e803bb833f5a) (const struct [device](structdevice.md) \*dev) |
|  | Request the PPC to exit from the dead battery mode Return from this call doesn't mean that the PPC is not in the dead battery anymore. |
| static int | [ppc\_is\_vbus\_source](#aab85fda6d4030c83052deb1965d814f3) (const struct [device](structdevice.md) \*dev) |
|  | Check if the PPC is sourcing the VBUS. |
| static int | [ppc\_is\_vbus\_sink](#af5e3999f3a016e33adf4797b62009d6d) (const struct [device](structdevice.md) \*dev) |
|  | Check if the PPC is sinking the VBUS. |
| static int | [ppc\_set\_snk\_ctrl](#ae157ab53326686361309f20dfe5c4e64) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set the state of VBUS sinking. |
| static int | [ppc\_set\_src\_ctrl](#ad38e1b5b5598c23ded44b343af58b791) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set the state of VBUS sourcing. |
| static int | [ppc\_set\_vbus\_discharge](#ae66cb0377ffefabf85bc002a2fd04a47) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set the state of VBUS discharging. |
| static int | [ppc\_is\_vbus\_present](#acd1ac1ac4ea60f16c58f57c9df11d536) (const struct [device](structdevice.md) \*dev) |
|  | Check if VBUS is present. |
| static int | [ppc\_set\_event\_handler](#a1d59cc94e8d303f0125fc88e5b447a69) (const struct [device](structdevice.md) \*dev, [usbc\_ppc\_event\_cb\_t](#a8195a7a51eb5bd3cbcec985b97b84e73) handler, void \*data) |
|  | Set the callback used to notify about PPC events. |
| static int | [ppc\_dump\_regs](#aeee650c29ce524b1e4d8ef66f295c1d7) (const struct [device](structdevice.md) \*dev) |
|  | Print the values or PPC registers. |

## Detailed Description

USB Type-C Power Path Controller device API.

## Typedef Documentation

## [◆ ](#a8195a7a51eb5bd3cbcec985b97b84e73)usbc\_ppc\_event\_cb\_t

| typedef void(\* usbc\_ppc\_event\_cb\_t) (const struct [device](structdevice.md) \*dev, void \*data, enum [usbc\_ppc\_event](#a3dbbb1a6701a3a79c9a1d148b239fcf9) ev) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a3dbbb1a6701a3a79c9a1d148b239fcf9)usbc\_ppc\_event

| enum [usbc\_ppc\_event](#a3dbbb1a6701a3a79c9a1d148b239fcf9) |
| --- |

Type of event being notified by Power Path Controller.

| Enumerator | |
| --- | --- |
| USBC\_PPC\_EVENT\_DEAD\_BATTERY\_ERROR | Exit from dead-battery mode failed. |
| USBC\_PPC\_EVENT\_SRC\_OVERVOLTAGE | Overvoltage detected while being in a source role. |
| USBC\_PPC\_EVENT\_SRC\_REVERSE\_CURRENT | Reverse current detected while being in a source role. |
| USBC\_PPC\_EVENT\_SRC\_OVERCURRENT | Overcurrent detected while being in a source role. |
| USBC\_PPC\_EVENT\_SRC\_SHORT | VBUS short detected while being in a source role. |
| USBC\_PPC\_EVENT\_OVER\_TEMPERATURE | Chip over temperature detected. |
| USBC\_PPC\_EVENT\_BOTH\_SNKSRC\_ENABLED | Sink and source paths enabled simultaneously. |
| USBC\_PPC\_EVENT\_SNK\_REVERSE\_CURRENT | Reverse current detected while being in a sink role. |
| USBC\_PPC\_EVENT\_SNK\_SHORT | VBUS short detected while being in a sink role. |
| USBC\_PPC\_EVENT\_SNK\_OVERVOLTAGE | Overvoltage detected while being in a sink role. |

## Function Documentation

## [◆ ](#aeee650c29ce524b1e4d8ef66f295c1d7)ppc\_dump\_regs()

| | int ppc\_dump\_regs | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Print the values or PPC registers.

Parameters
:   | dev | PPC device structure |
    | --- | --- |

Return values
:   | 0 | if success |
    | --- | --- |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#abcbebdf47ca1c8a9b7c2e803bb833f5a)ppc\_exit\_dead\_battery\_mode()

| | int ppc\_exit\_dead\_battery\_mode | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Request the PPC to exit from the dead battery mode Return from this call doesn't mean that the PPC is not in the dead battery anymore.

In the case of error, the driver should execute the callback with USBC\_PPC\_EVENT\_DEAD\_BATTERY\_ERROR enum. To check if the PPC disabled the dead battery mode, the call to ppc\_is\_dead\_battery\_mode should be done.

Parameters
:   | dev | PPC device structure |
    | --- | --- |

Return values
:   | 0 | if request was successfully sent |
    | --- | --- |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#a5f70af9a0d0336c208ff4f7a90c4b665)ppc\_is\_dead\_battery\_mode()

| | int ppc\_is\_dead\_battery\_mode | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Check if PPC is in the dead battery mode.

Parameters
:   | dev | PPC device structure |
    | --- | --- |

Return values
:   | 1 | if PPC is in the dead battery mode |
    | --- | --- |
    | 0 | if PPC is not in the dead battery mode |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#acd1ac1ac4ea60f16c58f57c9df11d536)ppc\_is\_vbus\_present()

| | int ppc\_is\_vbus\_present | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Check if VBUS is present.

Parameters
:   | dev | PPC device structure |
    | --- | --- |

Return values
:   | 1 | if VBUS voltage is present |
    | --- | --- |
    | 0 | if no VBUS voltage is detected |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#af5e3999f3a016e33adf4797b62009d6d)ppc\_is\_vbus\_sink()

| | int ppc\_is\_vbus\_sink | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Check if the PPC is sinking the VBUS.

Parameters
:   | dev | PPC device structure |
    | --- | --- |

Return values
:   | 1 | if the PPC is sinking the VBUS |
    | --- | --- |
    | 0 | if the PPC is not sinking the VBUS |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#aab85fda6d4030c83052deb1965d814f3)ppc\_is\_vbus\_source()

| | int ppc\_is\_vbus\_source | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Check if the PPC is sourcing the VBUS.

Parameters
:   | dev | PPC device structure |
    | --- | --- |

Return values
:   | 1 | if the PPC is sourcing the VBUS |
    | --- | --- |
    | 0 | if the PPC is not sourcing the VBUS |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#a1d59cc94e8d303f0125fc88e5b447a69)ppc\_set\_event\_handler()

| | int ppc\_set\_event\_handler | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [usbc\_ppc\_event\_cb\_t](#a8195a7a51eb5bd3cbcec985b97b84e73) | *handler*, | |  |  | void \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set the callback used to notify about PPC events.

Parameters
:   | dev | PPC device structure |
    | --- | --- |
    | handler | Handler that will be called with events notifications |
    | data | Pointer used as an argument to the callback |

Return values
:   | 0 | if success |
    | --- | --- |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#ae157ab53326686361309f20dfe5c4e64)ppc\_set\_snk\_ctrl()

| | int ppc\_set\_snk\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set the state of VBUS sinking.

Parameters
:   | dev | PPC device structure |
    | --- | --- |
    | enable | True if sinking VBUS should be enabled, false if should be disabled |

Return values
:   | 0 | if success |
    | --- | --- |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#ad38e1b5b5598c23ded44b343af58b791)ppc\_set\_src\_ctrl()

| | int ppc\_set\_src\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set the state of VBUS sourcing.

Parameters
:   | dev | PPC device structure |
    | --- | --- |
    | enable | True if sourcing VBUS should be enabled, false if should be disabled |

Return values
:   | 0 | if success |
    | --- | --- |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

## [◆ ](#ae66cb0377ffefabf85bc002a2fd04a47)ppc\_set\_vbus\_discharge()

| | int ppc\_set\_vbus\_discharge | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set the state of VBUS discharging.

Parameters
:   | dev | PPC device structure |
    | --- | --- |
    | enable | True if VBUS discharging should be enabled, false if should be disabled |

Return values
:   | 0 | if success |
    | --- | --- |
    | -EIO | if I2C communication failed |
    | -ENOSYS | if this function is not supported by the driver |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_ppc.h](usbc__ppc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
