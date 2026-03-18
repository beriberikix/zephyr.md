---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/intel/ish/doc/index.html
original_path: boards/intel/ish/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Intel Integrated Sensor Hub (ISH)

## Overview

Intel Integrated Sensor Hub (ISH) is a lower-power/always-on co-processor
inside many Intel Processors. It helps offload sensor processing tasks from
the core processor for better power saving.

## Hardware

- LMT MinuteIA Core:

  - 16KB instruction cache and 16KB data cache.
  - 640KB SRAM space for code and data - implemented as L2 SRAM.
  - 8KB AON RF space for code resident during deep D0i2/3 PG states.
- Interface-to-Sensor peripherals (I2C, SPI, UART, I3C, GPIO, DMA).
- Inter Process Communications (IPC) to core processor and other IP processors.

### Supported Features

In addition to the standard architecture devices (HPET, local and I/O APICs,
etc.), Zephyr supports the following ISH-specific SoC devices:

- HSUART

## Programming and Debugging

Use the following procedures for booting an ISH image on a ADL RVP board
for Chrome.

### [Build Zephyr application](#contents)

1. Build a Zephyr application; for instance, to build the `hello_world`
   application for ISH 5.4.1 on Intel ADL Processor:

   ```shell
   # From the root of the zephyr repository
   west build -b intel_ish_5_4_1 samples/hello_world
   ```

   Note

   A Zephyr image file named `ish_fw.bin` is automatically
   created in the build directory after the application is built.

### [Run ish\_fw.bin on ADL RVP board for Chrome](#contents)

- Power on the ADL RVP board.
- Log in Chrome OS. (Note: the user must have root access right, see [Developer Mode](https://chromium.googlesource.com/chromiumos/docs/+/HEAD/developer_mode.md))
- Re-mount the root filesystem as read-write:

```shell
$ mount -o remount,rw /
```

- If re-mount fails, execute below commands to Remove rootfs verification:

```shell
$ /usr/share/vboot/bin/make_dev_ssd.sh --remove_rootfs_verification --partitions
$ reboot
```

- Go to the ISH firmware direcoty:

```shell
$ cd /lib/firmware/intel
```

- Relace the file adlrvp\_ish.bin with zephyr image built out, ish\_fw.bin.
- Reboot, then observe Zephyr log output via ISH UART0.
