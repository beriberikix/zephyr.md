---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/device_mgmt/mcumgr.html
original_path: services/device_mgmt/mcumgr.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MCUmgr

## Overview

The management subsystem allows remote management of Zephyr-enabled devices.
The following management operations are available:

- Image management
- File System management
- OS management
- Settings (config) management
- Shell management
- Statistic management
- Zephyr management

over the following transports:

- BLE (Bluetooth Low Energy)
- Serial (UART)
- UDP over IP

The management subsystem is based on the Simple Management Protocol (SMP)
provided by [MCUmgr](https://github.com/apache/mynewt-mcumgr), an open source project that provides a
management subsystem that is portable across multiple real-time operating
systems.

The management subsystem is located in [subsys/mgmt/](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/) inside of
the Zephyr tree.

Additionally, there is a [sample](../../samples/subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.") sample that provides
management functionality over BLE and serial.

## Tools/libraries

There are various tools and libraries available which enable usage of MCUmgr functionality on a
device which are listed below. Note that these tools are not part of or related to the Zephyr
project.

Tools and Libraries for MCUmgr

| Name | OS support | | | | | Transports | | | Groups | | | | | | | Type | Language | License |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Windows | Linux | mac | Mobile | Embedded | Serial | Bluetooth | UDP | OS | IMG | Stat | Settings | FS | Shell | Zephyr |
| [AuTerm](https://github.com/thedjnK/AuTerm/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Application | C++ (Qt) | GPLv3 |
| [mcumgr-client](https://github.com/vouch-opensource/mcumgr-client/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | Application | Rust | BSD |
| [mcumgr-web](https://github.com/boogie/mcumgr-web/) | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | Web page (chrome only) | Javascript | MIT |
| nRF Connect Device Manager:   [Android](https://github.com/NordicSemiconductor/Android-nRF-Connect-Device-Manager/) and [iOS](https://github.com/NordicSemiconductor/IOS-nRF-Connect-Device-Manager) | ✕ | ✕ | ✕ | ✓ | ✕ | ✕ | ✓ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Library and application | Java, Kotlin, Swift | Apache |
| Zephyr MCUmgr client (in-tree) | ✕ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | Library | C | Apache |

Note that a tick for a particular group indicates basic support for that group in the code, it is
possible that not all commands/features of a group are supported by the implementation.

## Command-line Tool

MCUmgr provides a command-line tool, `mcumgr`, for managing remote devices.
The tool is written in the Go programming language.

Note

This tool is provided for evaluation use only and is not recommended for
use in a production environment. It has known issues and will not respect
the MCUmgr protocol properly e.g. when an error is received, instead of
aborting will, in some circumstances, sit in an endless loop of sending the
same command over and over again. A universal replacement for this tool is
currently in development and once released, support for the go tool will be
dropped entirely. It is recommended that usage of tools listed above in the
[Tools/libraries](#mcumgr-tools-libraries) section are used instead of the go client.

To install the tool:

go version < 1.18go version >= 1.18

```shell
go get github.com/apache/mynewt-mcumgr-cli/mcumgr
```

```shell
go install github.com/apache/mynewt-mcumgr-cli/mcumgr@latest
```

## Configuring the transport

There are two command-line options that are responsible for setting and configuring
the transport layer to use when communicating with managed device:

- `--conntype` is used to choose the transport used, and
- `--connstring` is used to pass a comma separated list of options in the
  `key=value` format, where each valid `key` depends on the particular
  `conntype`.

Valid transports for `--conntype` are `serial`, `ble` and `udp`. Each
transport expects a different set of key/value options:

serialbleudp

`--connstring` accepts the following `key` values:

| `dev` | the device name for the OS `mcumgr` is running on (eg, `/dev/ttyUSB0`, `/dev/tty.usbserial`, `COM1`, etc). |
| --- | --- |
| `baud` | the communication speed; must match the baudrate of the server. |
| `mtu` | aka Maximum Transmission Unit, the maximum protocol packet size. |

`--connstring` accepts the following `key` values:

| `ctlr_name` | an OS specific string for the controller name. |
| --- | --- |
| `own_addr_type` | can be one of `public`, `random`, `rpa_pub`, `rpa_rnd`, where `random` is the default. |
| `peer_name` | the name the peer BLE device advertises, this should match the configuration specified with [`CONFIG_BT_DEVICE_NAME`](../../kconfig.md#CONFIG_BT_DEVICE_NAME "CONFIG_BT_DEVICE_NAME"). |
| `peer_id` | the peer BLE device address or UUID. Only required when `peer_name` was not given. The format depends on the OS where `mcumgr` is run, it is a 6 bytes hexadecimal string separated by colons on Linux, or a 128-bit UUID on macOS. |
| `conn_timeout` | a float number representing the connection timeout in seconds. |

`--connstring` takes the form `[addr]:port` where:

| `addr` | can be a DNS name (if it can be resolved to the device IP), IPv4 addr (app must be built with [`CONFIG_MCUMGR_TRANSPORT_UDP_IPV4`](../../kconfig.md#CONFIG_MCUMGR_TRANSPORT_UDP_IPV4 "CONFIG_MCUMGR_TRANSPORT_UDP_IPV4")), or IPv6 addr (app must be built with [`CONFIG_MCUMGR_TRANSPORT_UDP_IPV6`](../../kconfig.md#CONFIG_MCUMGR_TRANSPORT_UDP_IPV6 "CONFIG_MCUMGR_TRANSPORT_UDP_IPV6")) |
| --- | --- |
| `port` | any valid UDP port. |

## Saving the connection config

The transport configuration can be managed with the `conn` sub-command and
later used with `--conn` (or `-c`) parameter to skip typing both `--conntype`
and `--connstring`. For example a new config for a serial device that would
require typing `mcumgr --conntype serial --connstring dev=/dev/ttyACM0,baud=115200,mtu=512`
can be saved with:

```text
mcumgr conn add acm0 type="serial" connstring="dev=/dev/ttyACM0,baud=115200,mtu=512"
```

Accessing this port can now be done with:

```text
mcumgr -c acm0
```

## General options

Some options work for every `mcumgr` command and might be helpful to debug and fix
issues with the communication, among them the following deserve special mention:

| `-l <log-level>` | Configures the log level, which can be one of `critical`, `error`, `warn`, `info` or `debug`, from less to most verbose. When there are communication issues, `-lDEBUG` might be useful to dump the packets for later inspection. |
| --- | --- |
| `-t <timeout>` | Changes the timeout waiting for a response from the default of 10s to a given value. Some commands might take a long time of processing, eg, the erase before an image upload, and might need incrementing the timeout to a larger value. |
| `-r <tries>` | Changes the number of retries on timeout from the default of 1 to a given value. |

## List of Commands

Not all commands defined by `mcumgr` (and SMP protocol) are currently supported
on Zephyr. The ones that are supported are described in the following table:

Tip

Running `mcumgr` with no parameters, or `-h` will display the list
of commands.

| Command | Description |
| --- | --- |
| `echo` | Send data to a device and display the echoed back data. This command is part of the `OS` group, which must be enabled by setting [`CONFIG_MCUMGR_GRP_OS`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS "CONFIG_MCUMGR_GRP_OS"). The `echo` command itself can be enabled by setting [`CONFIG_MCUMGR_GRP_OS_ECHO`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS_ECHO "CONFIG_MCUMGR_GRP_OS_ECHO"). |
| `fs` | Access files on a device. More info in [Filesystem Management](#fs-mgmt). |
| `image` | Manage images on a device. More info in [Image Management](#image-mgmt). |
| `reset` | Perform a soft reset of a device. This command is part of the `OS` group, which must be enabled by setting [`CONFIG_MCUMGR_GRP_OS`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS "CONFIG_MCUMGR_GRP_OS"). The `reset` command itself is always enabled and the time taken for a reset to happen can be set with [`CONFIG_MCUMGR_GRP_OS_RESET_MS`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS_RESET_MS "CONFIG_MCUMGR_GRP_OS_RESET_MS") (in ms). |
| `shell` | Execute a command in the remote shell. This option is disabled by default and can be enabled with [`CONFIG_MCUMGR_GRP_SHELL`](../../kconfig.md#CONFIG_MCUMGR_GRP_SHELL "CONFIG_MCUMGR_GRP_SHELL") = `y`. To know more about the shell in Zephyr check [Shell](../shell/index.md#shell-api). |
| `stat` | Read statistics from a device. More info in [Statistics Management](#stats-mgmt). |
| `taskstat` | Read task statistics from a device. This command is part of the `OS` group, which must be enabled by setting [`CONFIG_MCUMGR_GRP_OS`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS "CONFIG_MCUMGR_GRP_OS"). The `taskstat` command itself can be enabled by setting [`CONFIG_MCUMGR_GRP_OS_TASKSTAT`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT "CONFIG_MCUMGR_GRP_OS_TASKSTAT"). [`CONFIG_THREAD_MONITOR`](../../kconfig.md#CONFIG_THREAD_MONITOR "CONFIG_THREAD_MONITOR") also needs to be enabled otherwise a `-8` (`MGMT_ERR_ENOTSUP`) will be returned. |

Tip

`taskstat` has a few options that might require tweaking. The
[`CONFIG_THREAD_NAME`](../../kconfig.md#CONFIG_THREAD_NAME "CONFIG_THREAD_NAME") must be set to display the task names, otherwise
the priority is displayed. Since the `taskstat` packets are large, they
might need increasing the [`CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE`](../../kconfig.md#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE "CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE") option.

Warning

To display the correct stack size in the `taskstat` command, the
[`CONFIG_THREAD_STACK_INFO`](../../kconfig.md#CONFIG_THREAD_STACK_INFO "CONFIG_THREAD_STACK_INFO") option must be set.
To display the correct stack usage in the `taskstat` command, both
[`CONFIG_THREAD_STACK_INFO`](../../kconfig.md#CONFIG_THREAD_STACK_INFO "CONFIG_THREAD_STACK_INFO") and [`CONFIG_INIT_STACKS`](../../kconfig.md#CONFIG_INIT_STACKS "CONFIG_INIT_STACKS") options
must be set.

## J-Link Virtual MSD Interaction Note

On boards where a J-Link OB is present which has both CDC and MSC (virtual Mass
Storage Device, also known as drag-and-drop) support, the MSD functionality can
prevent MCUmgr commands over the CDC UART port from working due to how USB
endpoints are configured in the J-Link firmware (for example on the
[Nordic nrf52840dk\_nrf52840 board](../../boards/arm/nrf52840dk_nrf52840/doc/index.md#nrf52840dk-nrf52840)) because of
limiting the maximum packet size (most likely to occur when using image
management commands for updating firmware). This issue can be
resolved by disabling MSD functionality on the J-Link device, follow the
instructions on [Disabling the Mass Storage Device functionality](../../develop/flash_debug/nordic_segger.md#nordic-segger-msd) to disable MSD support.

## Image Management

The image management provided by `mcumgr` is based on the image format defined
by MCUboot. For more details on the internals see [MCUboot design](https://github.com/mcu-tools/mcuboot/blob/main/docs/design.md) and [Signing Binaries](../../develop/west/sign.md#west-sign).

To list available images in a device:

```text
mcumgr <connection-options> image list
```

This should result in an output similar to this:

```text
$ mcumgr -c acm0 image list
Images:
  image=0 slot=0
    version: 1.0.0
    bootable: true
    flags: active confirmed
    hash: 86dca73a3439112b310b5e033d811ec2df728d2264265f2046fced5a9ed00cc7
Split status: N/A (0)
```

Where `image` is the number of the image pair in a multi-image system, and slot
is the number of the slot where the image is stored, `0` for primary and `1` for
secondary. This image being `active` and `confirmed` means it will run again on
next reset. Also relevant is the `hash`, which is used by other commands to
refer to this specific image when performing operations.

An image can be manually erased using:

```text
mcumgr <connection-options> image erase
```

The behavior of `erase` is defined by the server (`MCUmgr` in the device).
The current implementation is limited to erasing the image in the secondary
partition.

To upload a new image:

```text
mcumgr <connection-options> image upload [-n] [-e] [-u] [-w] <signed-bin>
```

- `-n`: This option allows uploading a new image to a specific set of images
  in a multi-image system, and is currently only supported by MCUboot when the
  CONFIG\_MCUBOOT\_SERIAL option is enabled.
- `-e`: This option avoids performing a full erase of the partition before
  starting a new upload.

Tip

The `-e` option should always be passed in because the `upload` command
already checks if an erase is required, respecting the
[`CONFIG_IMG_ERASE_PROGRESSIVELY`](../../kconfig.md#CONFIG_IMG_ERASE_PROGRESSIVELY "CONFIG_IMG_ERASE_PROGRESSIVELY") setting.

Tip

If the `upload` command times out while waiting for a response from the
device, `-t` might be used to increase the wait time to something larger
than the default of 10s. See [general\_options](#general-options).

Warning

`mcumgr` does not understand .hex files, when uploading a new image always
use the .bin file.

- `-u`: This option allows upgrading only to newer image version.
- `-w`: This option allows setting the maximum size for the window of outstanding chunks in transit.
  It is set to 5 by default.

  Tip

  If the option is set to a value lower than the default one, for example `-w 1`, less chunks are transmitted on the window,
  resulting in lower risk of errors. Conversely, setting a value higher than 5 increases risk of errors and may impact performance.

After an image upload is finished, a new `image list` would now have an output
like this:

```text
$ mcumgr -c acm0 image upload -e build/zephyr/zephyr.signed.bin
  35.69 KiB / 92.92 KiB [==========>---------------]  38.41% 2.97 KiB/s 00m19
```

Now listing the images again:

```text
$ mcumgr -c acm0 image list
Images:
 image=0 slot=0
  version: 1.0.0
  bootable: true
  flags: active confirmed
  hash: 86dca73a3439112b310b5e033d811ec2df728d2264265f2046fced5a9ed00cc7
 image=0 slot=1
  version: 1.1.0
  bootable: true
  flags:
  hash: e8cf0dcef3ec8addee07e8c4d5dc89e64ba3fae46a2c5267fc4efbea4ca0e9f4
Split status: N/A (0)
```

To test a new upgrade image the `test` command is used:

```text
mcumgr <connection-options> image test <hash>
```

This command should mark a `test` upgrade, which means that after the next
reboot the bootloader will execute the upgrade and jump into the new image. If no
other image operations are executed on the newly running image, it will `revert`
back to the image that was previously running on the device on the subsequent reset.
When a `test` is requested, `flags` will be updated with `pending` to inform
that a new image will be run after a reset:

```text
$ mcumgr -c acm0 image test e8cf0dcef3ec8addee07e8c4d5dc89e64ba3fae46a2c5267fc4efbea4ca0e9f4
Images:
 image=0 slot=0
  version: 1.0.0
  bootable: true
  flags: active confirmed
  hash: 86dca73a3439112b310b5e033d811ec2df728d2264265f2046fced5a9ed00cc7
 image=0 slot=1
  version: 1.1.0
  bootable: true
  flags: pending
  hash: e8cf0dcef3ec8addee07e8c4d5dc89e64ba3fae46a2c5267fc4efbea4ca0e9f4
Split status: N/A (0)
```

After a reset the output with change to:

```text
$ mcumgr -c acm0 image list
Images:
 image=0 slot=0
  version: 1.1.0
  bootable: true
  flags: active
  hash: e8cf0dcef3ec8addee07e8c4d5dc89e64ba3fae46a2c5267fc4efbea4ca0e9f4
 image=0 slot=1
  version: 1.0.0
  bootable: true
  flags: confirmed
  hash: 86dca73a3439112b310b5e033d811ec2df728d2264265f2046fced5a9ed00cc7
Split status: N/A (0)
```

Tip

It’s important to mention that an upgrade only ever happens if the image is
valid. The first thing MCUboot does when an upgrade is requested is to
validate the image, using the SHA-256 and/or the signature (depending on
the configuration). So before uploading an image, one way to be sure it is
valid is to run `imgtool verify -k <your-signature-key> <your-image>`,
where `-k <your-signature-key` can be skipped if no signature validation
was enabled.

The `confirmed` flag in the secondary slot tells that after the next reset a
revert upgrade will be performed to switch back to the original layout.

The `confirm` command used to confirm that an image is OK and no revert
should happen (empty `hash` required) is:

```text
mcumgr <connection-options> image confirm ""
```

The `confirm` command can also be run passing in a `hash` so that instead of
doing a `test`/`revert` procedure, the image in the secondary partition is
directly upgraded to, eg:

```text
mcumgr <connection-options> image confirm <hash>
```

Tip

The whole `test`/`revert` cycle does not need to be done using only the
`mcumgr` command-line tool. A better alternative is to perform a `test`
and allow the new running image to self-confirm after any checks by calling
[`boot_write_img_confirmed()`](dfu.md#c.boot_write_img_confirmed "boot_write_img_confirmed").

Tip

Building with [`CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR "CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR") enables better error
messages when failures happen (but increases the application size).

## Statistics Management

Statistics are used for troubleshooting, maintenance, and usage monitoring; it
consists basically of user-defined counters which are tightly connected to
`mcumgr` and can be used to track any information for easy retrieval. The
available sub-commands are:

```text
mcumgr <connection-options> stat list
mcumgr <connection-options> stat <section-name>
```

Statistics are organized in sections (also called groups), and each section can
be individually queried. Defining new statistics sections is done by using macros
available under `zephyr/stats/stats.h`. Each section consists of multiple
variables (or counters), all with the same size (16, 32 or 64 bits).

To create a new section `my_stats`:

```text
STATS_SECT_START(my_stats)
  STATS_SECT_ENTRY(my_stat_counter1)
  STATS_SECT_ENTRY(my_stat_counter2)
  STATS_SECT_ENTRY(my_stat_counter3)
STATS_SECT_END;

STATS_SECT_DECL(my_stats) my_stats;
```

Each entry can be declared with `STATS_SECT_ENTRY` (or the equivalent
`STATS_SECT_ENTRY32`), `STATS_SECT_ENTRY16` or
`STATS_SECT_ENTRY64`.
All statistics in a section must be declared with the same size.

The statistics counters can either have names or not, depending on the setting
of the [`CONFIG_STATS_NAMES`](../../kconfig.md#CONFIG_STATS_NAMES "CONFIG_STATS_NAMES") option. Using names requires an extra
declaration step:

```text
STATS_NAME_START(my_stats)
  STATS_NAME(my_stats, my_stat_counter1)
  STATS_NAME(my_stats, my_stat_counter2)
  STATS_NAME(my_stats, my_stat_counter3)
STATS_NAME_END(my_stats);
```

Tip

Disabling [`CONFIG_STATS_NAMES`](../../kconfig.md#CONFIG_STATS_NAMES "CONFIG_STATS_NAMES") will free resources. When this option
is disabled the `STATS_NAME*` macros output nothing, so adding them in the
code does not increase the binary size.

Tip

[`CONFIG_MCUMGR_GRP_STAT_MAX_NAME_LEN`](../../kconfig.md#CONFIG_MCUMGR_GRP_STAT_MAX_NAME_LEN "CONFIG_MCUMGR_GRP_STAT_MAX_NAME_LEN") sets the maximum length of a section
name that can can be accepted as parameter for showing the section data, and
might require tweaking for long section names.

The final steps to use a statistics section is to initialize and register it:

```text
rc = STATS_INIT_AND_REG(my_stats, STATS_SIZE_32, "my_stats");
assert (rc == 0);
```

In the running code a statistics counter can be incremented by 1 using
`STATS_INC`, by N using `STATS_INCN` or reset with
`STATS_CLEAR`.

Let’s suppose we want to increment those counters by `1`, `2` and `3`
every second. To get a list of stats:

```text
$ mcumgr --conn acm0 stat list
stat groups:
  my_stats
```

To get the current value of the counters in `my_stats`:

```text
$ mcumgr --conn acm0 stat my_stats
stat group: my_stats
      13 my_stat_counter1
      26 my_stat_counter2
      39 my_stat_counter3

$ mcumgr --conn acm0 stat my_stats
stat group: my_stats
      16 my_stat_counter1
      32 my_stat_counter2
      48 my_stat_counter3
```

When [`CONFIG_STATS_NAMES`](../../kconfig.md#CONFIG_STATS_NAMES "CONFIG_STATS_NAMES") is disabled the output will look like this:

```text
$ mcumgr --conn acm0 stat my_stats
stat group: my_stats
       8 s0
      16 s1
      24 s2
```

## Filesystem Management

The filesystem module is disabled by default due to security concerns:
because of a lack of access control by default, every file in the FS will be
accessible, including secrets, etc. To enable it
[`CONFIG_MCUMGR_GRP_FS`](../../kconfig.md#CONFIG_MCUMGR_GRP_FS "CONFIG_MCUMGR_GRP_FS") must be set (`y`). Once enabled the
following sub-commands can be used:

```text
mcumgr <connection-options> fs download <remote-file> <local-file>
mcumgr <connection-options> fs upload <local-file> <remote-file>
```

Using the `fs` command, requires [`CONFIG_FILE_SYSTEM`](../../kconfig.md#CONFIG_FILE_SYSTEM "CONFIG_FILE_SYSTEM") to be enabled,
and that some particular filesystem is enabled and properly mounted by the running
application, eg for littlefs this would mean enabling
[`CONFIG_FILE_SYSTEM_LITTLEFS`](../../kconfig.md#CONFIG_FILE_SYSTEM_LITTLEFS "CONFIG_FILE_SYSTEM_LITTLEFS"), defining a storage partition [Flash map](../storage/flash_map/flash_map.md#flash-map-api)
and mounting the filesystem in the startup ([`fs_mount()`](../file_system/index.md#c.fs_mount "fs_mount")).

Uploading a new file to a littlefs storage, mounted under `/lfs`, can be done with:

```text
$ mcumgr -c acm0 fs upload foo.txt /lfs/foo.txt
25
Done
```

Where `25` is the size of the file.

For downloading a file, let’s first use the `fs` command
([`CONFIG_FILE_SYSTEM_SHELL`](../../kconfig.md#CONFIG_FILE_SYSTEM_SHELL "CONFIG_FILE_SYSTEM_SHELL") must be enabled) in a remote shell to create
a new file:

```text
uart:~$ fs write /lfs/bar.txt 41 42 43 44 31 32 33 34 0a
uart:~$ fs read /lfs/bar.txt
File size: 9
00000000  41 42 43 44 31 32 33 34 0A                       ABCD1234.
```

Now it can be downloaded using:

```text
$ mcumgr -c acm0 fs download /lfs/bar.txt bar.txt
0
9
Done
$ cat bar.txt
ABCD1234
```

Where `0` is the return code, and `9` is the size of the file.

Warning

The commands might exhaust the system workqueue, if its size is not large
enough, so increasing [`CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE`](../../kconfig.md#CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE "CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE") might be
required for correct behavior.

The size of the stack allocated buffer used to store the blocks, while transferring
a file can be adjusted with [`CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE`](../../kconfig.md#CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE "CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE"); this allows
saving RAM resources.

Tip

[`CONFIG_MCUMGR_GRP_FS_PATH_LEN`](../../kconfig.md#CONFIG_MCUMGR_GRP_FS_PATH_LEN "CONFIG_MCUMGR_GRP_FS_PATH_LEN") sets the maximum PATH accepted for a file
name. It might require tweaking for longer file names.

Note

To add security to the filesystem management group, callbacks for MCUmgr
hooks can be registered by a user application when the upload/download
functions are ran which allows the application to control if access to a
file is allowed or denied. See the [MCUmgr Callbacks](mcumgr_callbacks.md#mcumgr-callbacks) section for
details.

## Bootloader Integration

The [Device Firmware Upgrade](dfu.md#dfu) subsystem integrates the management subsystem with the
bootloader, providing the ability to send and upgrade a Zephyr image to a
device.

Currently only the MCUboot bootloader is supported. See [MCUboot](dfu.md#mcuboot) for more
information.

## Discord channel

Developers welcome!

- Discord mcumgr channel: [https://discord.com/invite/Ck7jw53nU2](https://discord.com/invite/Ck7jw53nU2)

## API Reference

*group* mcumgr\_mgmt\_api
:   MCUmgr mgmt API.

    Defines

    MGMT\_CTXT\_SET\_RC\_RSN(mc, rsn)

    MGMT\_CTXT\_RC\_RSN(mc)

    MGMT\_RETURN\_CHECK(ok)
    :   Used at end of MCUmgr handlers to return an error if the message size limit was reached, or OK if it was not.

    MGMT\_HDR\_SIZE

    Typedefs

    typedef void \*(\*mgmt\_alloc\_rsp\_fn)(const void \*src\_buf, void \*arg)
    :   Allocates a buffer suitable for holding a response.

        If a source buf is provided, its user data is copied into the new buffer.

        Param src\_buf:
        :   An optional source buffer to copy user data from.

        Param arg:
        :   Optional streamer argument.

        Return:
        :   Newly-allocated buffer on success NULL on failure.

    typedef void (\*mgmt\_reset\_buf\_fn)(void \*buf, void \*arg)
    :   Resets a buffer to a length of 0.

        The buffer’s user data remains, but its payload is cleared.

        Param buf:
        :   The buffer to reset.

        Param arg:
        :   Optional streamer argument.

    typedef int (\*mgmt\_handler\_fn)(struct smp\_streamer \*ctxt)
    :   Processes a request and writes the corresponding response.

        A separate handler is required for each supported op-ID pair.

        Param ctxt:
        :   The mcumgr context to use.

        Return:
        :   0 if a response was successfully encoded, [mcumgr\_err\_t](#group__mcumgr__mgmt__api_1gac5d8757a7ca945c77f405764b85ad5c5) code on failure.

    Enums

    enum mcumgr\_op\_t
    :   Opcodes; encoded in first byte of header.

        *Values:*

        enumerator MGMT\_OP\_READ = 0
        :   Read op-code.

        enumerator MGMT\_OP\_READ\_RSP
        :   Read response op-code.

        enumerator MGMT\_OP\_WRITE
        :   Write op-code.

        enumerator MGMT\_OP\_WRITE\_RSP
        :   Write response op-code.

    enum mcumgr\_group\_t
    :   MCUmgr groups.

        The first 64 groups are reserved for system level mcumgr commands. Per-user commands are then defined after group 64.

        *Values:*

        enumerator MGMT\_GROUP\_ID\_OS = 0
        :   OS (operating system) group.

        enumerator MGMT\_GROUP\_ID\_IMAGE
        :   Image management group, used for uploading firmware images.

        enumerator MGMT\_GROUP\_ID\_STAT
        :   Statistic management group, used for retieving statistics.

        enumerator MGMT\_GROUP\_ID\_SETTINGS
        :   Settings management (config) group, used for reading/writing settings.

        enumerator MGMT\_GROUP\_ID\_LOG
        :   Log management group (unused).

        enumerator MGMT\_GROUP\_ID\_CRASH
        :   Crash group (unused).

        enumerator MGMT\_GROUP\_ID\_SPLIT
        :   Split image management group (unused).

        enumerator MGMT\_GROUP\_ID\_RUN
        :   Run group (unused).

        enumerator MGMT\_GROUP\_ID\_FS
        :   FS (file system) group, used for performing file IO operations.

        enumerator MGMT\_GROUP\_ID\_SHELL
        :   Shell management group, used for executing shell commands.

        enumerator MGMT\_GROUP\_ID\_PERUSER = 64
        :   User groups defined from 64 onwards.

        enumerator ZEPHYR\_MGMT\_GRP\_BASIC = ([MGMT\_GROUP\_ID\_PERUSER](#c.mcumgr_group_t.MGMT_GROUP_ID_PERUSER) - 1)
        :   Zephyr-specific groups decrease from PERUSER to avoid collision with upstream and user-defined groups.

            Zephyr-specific: Basic group

    enum mcumgr\_err\_t
    :   MCUmgr error codes.

        *Values:*

        enumerator MGMT\_ERR\_EOK = 0
        :   No error (success).

        enumerator MGMT\_ERR\_EUNKNOWN
        :   Unknown error.

        enumerator MGMT\_ERR\_ENOMEM
        :   Insufficient memory (likely not enough space for CBOR object).

        enumerator MGMT\_ERR\_EINVAL
        :   Error in input value.

        enumerator MGMT\_ERR\_ETIMEOUT
        :   Operation timed out.

        enumerator MGMT\_ERR\_ENOENT
        :   No such file/entry.

        enumerator MGMT\_ERR\_EBADSTATE
        :   Current state disallows command.

        enumerator MGMT\_ERR\_EMSGSIZE
        :   Response too large.

        enumerator MGMT\_ERR\_ENOTSUP
        :   Command not supported.

        enumerator MGMT\_ERR\_ECORRUPT
        :   Corrupt.

        enumerator MGMT\_ERR\_EBUSY
        :   Command blocked by processing of other command.

        enumerator MGMT\_ERR\_EACCESSDENIED
        :   Access to specific function, command or resource denied.

        enumerator MGMT\_ERR\_UNSUPPORTED\_TOO\_OLD
        :   Requested SMP MCUmgr protocol version is not supported (too old).

        enumerator MGMT\_ERR\_UNSUPPORTED\_TOO\_NEW
        :   Requested SMP MCUmgr protocol version is not supported (too new).

        enumerator MGMT\_ERR\_EPERUSER = 256
        :   User errors defined from 256 onwards.

    Functions

    void mgmt\_register\_group(struct [mgmt\_group](#c.mgmt_group) \*group)
    :   Registers a full command group.

        Parameters:
        :   - **group** – The group to register.

    void mgmt\_unregister\_group(struct [mgmt\_group](#c.mgmt_group) \*group)
    :   Unregisters a full command group.

        Parameters:
        :   - **group** – The group to register.

    const struct [mgmt\_handler](#c.mgmt_handler) \*mgmt\_find\_handler(uint16\_t group\_id, uint16\_t command\_id)
    :   Finds a registered command handler.

        Parameters:
        :   - **group\_id** – The group of the command to find.
            - **command\_id** – The ID of the command to find.

        Returns:
        :   The requested command handler on success; NULL on failure.

    const struct [mgmt\_group](#c.mgmt_group) \*mgmt\_find\_group(uint16\_t group\_id)
    :   Finds a registered command group.

        Parameters:
        :   - **group\_id** – The group id of the command group to find.

        Returns:
        :   The requested group on success; NULL on failure.

    const struct [mgmt\_handler](#c.mgmt_handler) \*mgmt\_get\_handler(const struct [mgmt\_group](#c.mgmt_group) \*group, uint16\_t command\_id)
    :   Finds a registered command handler.

        Parameters:
        :   - **group** – The group of the command to find.
            - **command\_id** – The ID of the command to find.

        Returns:
        :   The requested command handler on success; NULL on failure.

    struct mgmt\_handler
    :   *#include <mgmt.h>*

        Read handler and write handler for a single command ID.

        Set use\_custom\_payload to true when using a user defined payload type

    struct mgmt\_group
    :   *#include <mgmt.h>*

        A collection of handlers for an entire command group.

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Entry list node.

        const struct [mgmt\_handler](#c.mgmt_handler) \*mg\_handlers
        :   Array of handlers; one entry per command ID.

        uint16\_t mg\_group\_id
        :   The numeric ID of this group.
