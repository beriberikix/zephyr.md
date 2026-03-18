---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/fs/fs_sample/README.html
original_path: samples/subsys/fs/fs_sample/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# File system manipulation

## Overview

This sample app demonstrates use of the file system API and uses the FAT or Ext2 file
system driver with SDHC card, SoC flash or external flash chip.

To access device the sample uses [Disk Access](../../../../services/storage/disk/access.md#disk-access-api).

## Requirements for SD card support

This project requires SD card support and microSD card formatted with proper file system
(FAT or Ext2) See the [Disk Access](../../../../services/storage/disk/access.md#disk-access-api) documentation for Zephyr implementation details.
Boards that by default use SD card for storage: `arduino_mkrzero`, `esp_wrover_kit`,
`mimxrt1050_evk`, `nrf52840_blip` and `olimexino_stm32`. The sample should be able
to run with any other board that has “zephyr,sdmmc-disk” DT node enabled.

## Requirements for setting up FAT FS on SoC flash

For the FAT FS to work with internal flash, the device needs to support erase
pages of size <= 4096 bytes and have at least 64kiB of flash available for
FAT FS partition alone.
Currently the following boards are supported:
`nrf52840dk_nrf52840`

## Requirements for setting up FAT FS on external flash

This type of configuration requires external flash device to be available
on DK board. Currently following boards support the configuration:
`nrf52840dk_nrf52840` by `nrf52840dk_nrf52840_qspi` configuration.

## Building and Running FAT samples

Boards with default configurations, for example `arduino_mkrzero` or
`nrf52840dk_nrf52840` using internal flash can be build using command:

```shell
west build -b nrf52840_blip samples/subsys/fs/fs_sample
```

Where used example board `nrf52840_blip` should be replaced with desired board.

In case when some more specific configuration is to be used for a given board,
for example `nrf52840dk_nrf52840` with MX25 device over QSPI, configuration
and DTS overlays need to be also selected. The command would look like this:

```shell
west build -b nrf52840dk_nrf52840 samples/subsys/fs/fs_sample -- -DEXTRA_CONF_FILE=nrf52840dk_nrf52840_qspi.conf -DDTC_OVERLAY_FILE=nrf52840dk_nrf52840_qspi.overlay
```

In case when board with SD card is used FAT microSD card should be present in the
microSD slot. If there are any files or directories present in the card, the
sample lists them out on the debug serial output.

Warning

In case when mount fails the device may get re-formatted to FAT FS.
To disable this behaviour disable [`CONFIG_FS_FATFS_MOUNT_MKFS`](../../../../kconfig.md#CONFIG_FS_FATFS_MOUNT_MKFS "CONFIG_FS_FATFS_MOUNT_MKFS") .

## Building and Running EXT2 samples

Ext2 sample can be build for `hifive_unmatched` or `bl5340_dvk_cpuapp`. Because
FAT is default file system for this sample, additional flags must be passed to build
the sample.

```shell
west build -b hifive_unmatched samples/subsys/fs/fs_sample -- -DCONF_FILE=prj_ext.conf
```

A microSD card must be present in a microSD card slot of the board, for the sample to execute.
After starting the sample a contents of a root directory should be printed on the console.
