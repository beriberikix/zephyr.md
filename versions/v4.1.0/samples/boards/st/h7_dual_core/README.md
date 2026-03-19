---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/st/h7_dual_core/README.html
original_path: samples/boards/st/h7_dual_core/README.html
---

# Hardware Semaphore (HSEM) Inter-Processor Communication on STM32 H7

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/h7_dual_core/README.rst/..)

## Overview

Blinky led triggered by mailbox new message.

## Building and Running

Build for stm32h747i\_disco/stm32h747xx/m7:

```shell
# From the root of the zephyr repository
west build -b stm32h747i_disco/stm32h747xx/m7 samples/boards/st/h7_dual_core
```

Build for stm32h747i\_disco/stm32h747xx/m4:

```shell
# From the root of the zephyr repository
west build -b stm32h747i_disco/stm32h747xx/m4 samples/boards/st/h7_dual_core
```

### Sample Output

```shell
STM32 h7_dual_core application
```

## See also

[IPM Interface](../../../../doxygen/html/group__ipm__interface.md)
