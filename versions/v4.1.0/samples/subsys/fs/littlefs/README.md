---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/fs/littlefs/README.html
original_path: samples/subsys/fs/littlefs/README.html
---

# LittleFS filesystem

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/fs/littlefs/README.rst/..)

## Overview

This sample app demonstrates use of Zephyr’s [file system API](../../../../services/file_system/index.md#file-system-api) over [littlefs](https://github.com/ARMmbed/littlefs), using file system with files that:
\* count the number of times the system has booted
\* holds binary pattern with properly incremented values in it

Other information about the file system is also displayed.

## Requirements

### Flash memory device

The partition labeled “storage” will be used for the file system; see
[Flash map](../../../../services/storage/flash_map/flash_map.md#flash-map-api). If that area does not already have a
compatible littlefs file system its contents will be replaced by an
empty file system. You will see diagnostics like this:

```text
[00:00:00.010,192] <inf> littlefs: LittleFS version 2.0, disk version 2.0
[00:00:00.010,559] <err> littlefs: Corrupted dir pair at 0 1
[00:00:00.010,559] <wrn> littlefs: can't mount (LFS -84); formatting
```

The error and warning are normal for a new file system.

After the file system is mounted you’ll also see:

```text
[00:00:00.182,434] <inf> littlefs: filesystem mounted!
[00:00:00.867,034] <err> fs: failed get file or dir stat (-2)
```

This error is also normal for Zephyr not finding a file (the boot count,
in this case).

### Block device (e.g. SD card)

One needs to prepare the SD/MMC card with littlefs file system on
the host machine with the [lfs](https://www.thevtool.com/mounting-littlefs-on-linux-machine/) program.

```shell
sudo chmod a+rw /dev/sda
lfs -d -s -f --read_size=512 --prog_size=512 --block_size=512 --cache_size=512 --lookahead_size=8192 --format /dev/sda
lfs -d -s -f --read_size=512 --prog_size=512 --block_size=512 --cache_size=512 --lookahead_size=8192 /dev/sda ./mnt_littlefs
cd ./mnt_littlefs
echo -en '\x01' > foo.txt
cd -
fusermount -u ./mnt_littlefs
```

## Building and Running

### Flash memory device

This example should work on any board that provides a “storage”
partition. Two tested board targets are described below.

You can set `CONFIG_APP_WIPE_STORAGE` to force the file system to be
recreated.

### Block device (e.g. SD card)

This example has been devised and initially tested on [Nucleo H743ZI](../../../../boards/st/nucleo_h743zi/doc/index.md#nucleo_h743zi)
board. It can be also run on any other board with SD/MMC card connected to it.

To build the test:

```shell
west build -b nucleo_h743zi samples/subsys/fs/littlefs -- -DCONF_FILE=prj_blk.conf
west flash
```

At the moment, only two types of block devices are acceptable in this sample: SDMMC and MMC.

It is possible that both the `zephyr,sdmmc-disk` and `zephyr,mmc-disk` block devices will be
present and enabled in the final board dts and configuration files simultaneously, the mount
point name for the `littlefs` file system block device will be determined based on the
following logic:

- if the [`CONFIG_DISK_DRIVER_SDMMC`](../../../../kconfig.md#CONFIG_DISK_DRIVER_SDMMC "CONFIG_DISK_DRIVER_SDMMC") configuration is defined, `"SD"`
  will be used as the mount point name;
- if the [`CONFIG_DISK_DRIVER_SDMMC`](../../../../kconfig.md#CONFIG_DISK_DRIVER_SDMMC "CONFIG_DISK_DRIVER_SDMMC") configuration is not defined, but the
  [`CONFIG_DISK_DRIVER_MMC`](../../../../kconfig.md#CONFIG_DISK_DRIVER_MMC "CONFIG_DISK_DRIVER_MMC") configuration is defined, `"SD2"` will
  be used as the mount point name;
- if neither [`CONFIG_DISK_DRIVER_SDMMC`](../../../../kconfig.md#CONFIG_DISK_DRIVER_SDMMC "CONFIG_DISK_DRIVER_SDMMC") nor [`CONFIG_DISK_DRIVER_MMC`](../../../../kconfig.md#CONFIG_DISK_DRIVER_MMC "CONFIG_DISK_DRIVER_MMC")
  configurations are defined, the mount point name will not be determined, and an appropriate error
  will appear during the sample build.

#### NRF52840 Development Kit

On this device the file system will be placed in the SOC flash.

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/fs/littlefs
```

#### Particle Xenon

On this device the file system will be placed on the external SPI NOR
flash memory.

```shell
west build -b particle_xenon samples/subsys/fs/littlefs
```

## See also

[File System APIs](../../../../doxygen/html/group__file__system__api.md)

[flash area Interface](../../../../doxygen/html/group__flash__area__api.md)
