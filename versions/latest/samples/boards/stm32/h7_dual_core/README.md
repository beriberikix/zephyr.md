---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/stm32/h7_dual_core/README.html
original_path: samples/boards/stm32/h7_dual_core/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# STM32 HSEM IPM driver sample

## Overview

Blinky led triggered by mailbox new message.

## Building and Running

Build for stm32h747i\_disco\_m7:

```shell
# From the root of the zephyr repository
west build -b stm32h747i_disco_m7 samples/boards/stm32/h7_dual_core
```

Build for stm32h747i\_disco\_m4:

```shell
# From the root of the zephyr repository
west build -b stm32h747i_disco_m4 samples/boards/stm32/h7_dual_core
```

### Sample Output

```shell
STM32 h7_dual_core application
```
