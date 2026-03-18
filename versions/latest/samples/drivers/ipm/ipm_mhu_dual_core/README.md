---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/ipm/ipm_mhu_dual_core/README.html
original_path: samples/drivers/ipm/ipm_mhu_dual_core/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# IPM with ARM MHU

## Overview

An MHU (Message Handling Unit) enables software to raise interrupts to
the processor cores. This sample is a simple dual-core example for a
Musca A1 board that has two MHU units. This sample only test MHU0, the
steps are:

1. CPU 0 will wake up CPU 1 after initialization
2. CPU 1 will send to CPU 0 an interrupt over MHU0
3. CPU 0 return the same to CPU 1 when received MHU0 interrupt
4. Test done when CPU 1 received MHU0 interrupt

## Building and Running

### On Musca B1

This project outputs ‘IPM MHU sample on musca\_b1’ to the console.
It can be built and executed on Musca B1 CPU 0 as follows:

```shell
west build -b v2m_musca_b1 samples/drivers/ipm/ipm_mhu_dual_core
west build -t run
```

This project outputs ‘IPM MHU sample on v2m\_musca\_b1\_ns’ to the console.
It can be built and executed on Musca B1 CPU 1 as follows:

```shell
west build -b v2m_musca_b1_ns samples/drivers/ipm/ipm_mhu_dual_core
west build -t run
```

#### Combine images for Musca

A third-party tool (srecord) is used to generate the Intel formatted hex image.
For more information refer to the [Srecord Manual](https://srecord.sourceforge.net/man/man1/srec_cat.1.html).

```shell
srec_cat zephyr.bin -Binary -offset $IMAGE_OFFSET zephyr_nonsecure.bin -Binary -offset $IMAGE_NS_OFFSET -o dual_core_zephyr.hex -Intel

# This command is an example for Musca B1
srec_cat zephyr.bin -Binary -offset 0xA000000 zephyr_nonsecure.bin -Binary -offset 0xA060400 -o dual_core_zephyr.hex -Intel
```

Open a serial terminal (minicom, putty, etc.) and connect the board with the
following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and the following message will appear on the corresponding
serial port.

#### Sample Output

```shell
***** Booting Zephyr OS zephyr-v1.13.0-3378-g3625524 *****
IPM MHU sample on musca_a
CPU 0, get MHU0 success!
***** Booting Zephyr OS zephyr-v1.13.0-3378-g3625524 *****
IPM MHU sample on musca_a_nonsecure
CPU 1, get MHU0 success!
MHU ISR on CPU 0
MHU ISR on CPU 1
MHU Test Done.
```
