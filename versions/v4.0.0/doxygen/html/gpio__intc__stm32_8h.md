---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gpio__intc__stm32_8h.html
original_path: doxygen/html/gpio__intc__stm32_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_intc\_stm32.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](gpio__intc__stm32_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) |
|  | GPIO interrupt controller API for STM32 MCUs. |
| typedef void(\* | [stm32\_gpio\_irq\_cb\_t](#a69ad9c575223c813f484423e56200560)) ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pin, void \*user) |
|  | GPIO interrupt callback function signature. |

| Enumerations | |
| --- | --- |
| enum | [stm32\_gpio\_irq\_trigger](#a8f9c3db22937ebe4382215227c410b61) {     [STM32\_GPIO\_IRQ\_TRIG\_NONE](#a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2) = 0x0 , [STM32\_GPIO\_IRQ\_TRIG\_RISING](#a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae) = 0x1 , [STM32\_GPIO\_IRQ\_TRIG\_FALLING](#a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9) = 0x2 , [STM32\_GPIO\_IRQ\_TRIG\_BOTH](#a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301) = 0x3 ,     [STM32\_GPIO\_IRQ\_TRIG\_HIGH\_LEVEL](#a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048) = 0x4 , [STM32\_GPIO\_IRQ\_TRIG\_LOW\_LEVEL](#a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c) = 0x5   } |
|  | GPIO interrupt trigger flags. [More...](#a8f9c3db22937ebe4382215227c410b61) |

| Functions | |
| --- | --- |
| [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) | [stm32\_gpio\_intc\_get\_pin\_irq\_line](#a03badd2828ca67e3f8adadc75fec2bd2) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Get the GPIO interrupt line value corresponding to specified `pin` of GPIO port `port`. |
| void | [stm32\_gpio\_intc\_enable\_line](#ad1c9359de9847ebd2670987302c48f8d) ([stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) line) |
|  | Enable GPIO interrupts for specified line. |
| void | [stm32\_gpio\_intc\_disable\_line](#a0bb3bd355218c41e9173f061f46ec997) ([stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) line) |
|  | Disable GPIO interrupts for specified line. |
| void | [stm32\_gpio\_intc\_select\_line\_trigger](#a23b9ea466101b4367232237ab5a9a42f) ([stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) line, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trg) |
|  | Select trigger for interrupt on specified GPIO line. |
| int | [stm32\_gpio\_intc\_set\_irq\_callback](#a4a750e87f445487c517f24a0266f6a4b) ([stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) line, [stm32\_gpio\_irq\_cb\_t](#a69ad9c575223c813f484423e56200560) cb, void \*user) |
|  | Set callback invoked when an interrupt occurs on specified GPIO line. |
| void | [stm32\_gpio\_intc\_remove\_irq\_callback](#a21b0c2213fbcdf179c8b4bdb29561863) ([stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) line) |
|  | Removes the interrupt callback of specified EXTI line. |

## Typedef Documentation

## [◆ ](#a69ad9c575223c813f484423e56200560)stm32\_gpio\_irq\_cb\_t

| typedef void(\* stm32\_gpio\_irq\_cb\_t) ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pin, void \*user) |
| --- |

GPIO interrupt callback function signature.

Parameters
:   | pin | GPIO pin on which interrupt occurred |
    | --- | --- |
    | user | `data` provided to [stm32\_gpio\_intc\_set\_irq\_callback](#a4a750e87f445487c517f24a0266f6a4b) |

Note
:   This callback is invoked in ISR context.

## [◆ ](#a52c69f3ce04242217e00981c1315a374)stm32\_gpio\_irq\_line\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) |
| --- |

GPIO interrupt controller API for STM32 MCUs.

This API is used to interact with the GPIO interrupt controller of STM32 microcontrollers.

Opaque type representing a GPIO interrupt line

## Enumeration Type Documentation

## [◆ ](#a8f9c3db22937ebe4382215227c410b61)stm32\_gpio\_irq\_trigger

| enum [stm32\_gpio\_irq\_trigger](#a8f9c3db22937ebe4382215227c410b61) |
| --- |

GPIO interrupt trigger flags.

| Enumerator | |
| --- | --- |
| STM32\_GPIO\_IRQ\_TRIG\_NONE |  |
| STM32\_GPIO\_IRQ\_TRIG\_RISING |  |
| STM32\_GPIO\_IRQ\_TRIG\_FALLING |  |
| STM32\_GPIO\_IRQ\_TRIG\_BOTH |  |
| STM32\_GPIO\_IRQ\_TRIG\_HIGH\_LEVEL |  |
| STM32\_GPIO\_IRQ\_TRIG\_LOW\_LEVEL |  |

## Function Documentation

## [◆ ](#a0bb3bd355218c41e9173f061f46ec997)stm32\_gpio\_intc\_disable\_line()

| void stm32\_gpio\_intc\_disable\_line | ( | [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable GPIO interrupts for specified line.

Parameters
:   | line | GPIO interrupt line |
    | --- | --- |

## [◆ ](#ad1c9359de9847ebd2670987302c48f8d)stm32\_gpio\_intc\_enable\_line()

| void stm32\_gpio\_intc\_enable\_line | ( | [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable GPIO interrupts for specified line.

Parameters
:   | line | GPIO interrupt line |
    | --- | --- |

## [◆ ](#a03badd2828ca67e3f8adadc75fec2bd2)stm32\_gpio\_intc\_get\_pin\_irq\_line()

| [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) stm32\_gpio\_intc\_get\_pin\_irq\_line | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) |

Get the GPIO interrupt line value corresponding to specified `pin` of GPIO port `port`.

## [◆ ](#a21b0c2213fbcdf179c8b4bdb29561863)stm32\_gpio\_intc\_remove\_irq\_callback()

| void stm32\_gpio\_intc\_remove\_irq\_callback | ( | [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

Removes the interrupt callback of specified EXTI line.

Parameters
:   | line | EXTI interrupt line |
    | --- | --- |

## [◆ ](#a23b9ea466101b4367232237ab5a9a42f)stm32\_gpio\_intc\_select\_line\_trigger()

| void stm32\_gpio\_intc\_select\_line\_trigger | ( | [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) | *line*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *trg* ) |

Select trigger for interrupt on specified GPIO line.

Parameters
:   | line | GPIO interrupt line |
    | --- | --- |
    | trg | Interrupt trigger (see [stm32\_gpio\_irq\_trigger](#a8f9c3db22937ebe4382215227c410b61)) |

## [◆ ](#a4a750e87f445487c517f24a0266f6a4b)stm32\_gpio\_intc\_set\_irq\_callback()

| int stm32\_gpio\_intc\_set\_irq\_callback | ( | [stm32\_gpio\_irq\_line\_t](#a52c69f3ce04242217e00981c1315a374) | *line*, |
| --- | --- | --- | --- |
|  |  | [stm32\_gpio\_irq\_cb\_t](#a69ad9c575223c813f484423e56200560) | *cb*, |
|  |  | void \* | *user* ) |

Set callback invoked when an interrupt occurs on specified GPIO line.

Parameters
:   | line | GPIO interrupt line |
    | --- | --- |
    | cb | Interrupt callback function |
    | user | Custom user data for usage by the callback |

Returns
:   0 on success, -EBUSY if a callback is already set for `line`

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gpio\_intc\_stm32.h](gpio__intc__stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
