---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/bluetooth-shell.html
original_path: connectivity/bluetooth/bluetooth-shell.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth Shell

The Bluetooth Shell is an application based on the [Shell](../../services/shell/index.md#shell-api) module. It offer a collection of
commands made to easily interact with the Bluetooth stack.

## Bluetooth Shell Setup and Usage

First you need to build and flash your board with the Bluetooth shell. For how to do that, see the
[Getting Started Guide](../../develop/getting_started/index.md#getting-started). The Bluetooth shell itself is located in
[tests/bluetooth/shell/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/bluetooth/shell/).

When it’s done, connect to the CLI using your favorite serial terminal application. You should see
the following prompt:

```shell
uart:~$
```

For more details on general usage of the shell, see [Shell](../../services/shell/index.md#shell-api).

The first step is enabling Bluetooth. To do so, use the `bt init` command. The following
message is printed to confirm Bluetooth has been initialized.

```shell
uart:~$ bt init
Bluetooth initialized
Settings Loaded
[00:02:26.771,148] <inf> fs_nvs: nvs_mount: 8 Sectors of 4096 bytes
[00:02:26.771,148] <inf> fs_nvs: nvs_mount: alloc wra: 0, fe8
[00:02:26.771,179] <inf> fs_nvs: nvs_mount: data wra: 0, 0
[00:02:26.777,984] <inf> bt_hci_core: hci_vs_init: HW Platform: Nordic Semiconductor (0x0002)
[00:02:26.778,015] <inf> bt_hci_core: hci_vs_init: HW Variant: nRF52x (0x0002)
[00:02:26.778,045] <inf> bt_hci_core: hci_vs_init: Firmware: Standard Bluetooth controller (0x00) Version 3.2 Build 99
[00:02:26.778,656] <inf> bt_hci_core: bt_init: No ID address. App must call settings_load()
[00:02:26.794,738] <inf> bt_hci_core: bt_dev_show_info: Identity: EB:BF:36:26:42:09 (random)
[00:02:26.794,769] <inf> bt_hci_core: bt_dev_show_info: HCI: version 5.3 (0x0c) revision 0x0000, manufacturer 0x05f1
[00:02:26.794,799] <inf> bt_hci_core: bt_dev_show_info: LMP: version 5.3 (0x0c) subver 0xffff
```

## Identities

Identities are a Zephyr host concept, allowing a single physical device to behave like multiple
logical Bluetooth devices.

The shell allows the creation of multiple identities, to a maximum that is set by the Kconfig symbol
[`CONFIG_BT_ID_MAX`](../../kconfig.md#CONFIG_BT_ID_MAX "CONFIG_BT_ID_MAX"). To create a new identity, use `bt id-create` command. You
can then use it by selecting it with its ID `bt id-select <id>`. Finally, you can list all the
available identities with `id-show`.

## Scan for devices

Start scanning by using the `bt scan on` command. Depending on the environment you’re in, you
may see a lot of lines printed on the shell. To stop the scan, run `bt scan off`, the
scrolling should stop.

Here is an example of what you can expect:

```shell
uart:~$ bt scan on
Bluetooth active scan enabled
[DEVICE]: CB:01:1A:2D:6E:AE (random), AD evt type 0, RSSI -78  C:1 S:1 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: 20:C2:EE:59:85:5B (random), AD evt type 3, RSSI -62  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: E3:72:76:87:2F:E8 (random), AD evt type 3, RSSI -74  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: 1E:19:25:8A:CB:84 (random), AD evt type 3, RSSI -67  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: 26:42:F3:D5:A0:86 (random), AD evt type 3, RSSI -73  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: 0C:61:D1:B9:5D:9E (random), AD evt type 3, RSSI -87  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: 20:C2:EE:59:85:5B (random), AD evt type 3, RSSI -66  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: 25:3F:7A:EE:0F:55 (random), AD evt type 3, RSSI -83  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
uart:~$ bt scan off
Scan successfully stopped
```

As you can see, this can lead to a high number of results. To reduce that number and easily find a
specific device, you can enable scan filters. There are four types of filters: by name, by RSSI, by
address and by periodic advertising interval. To apply a filter, use the `bt scan-set-filter`
command followed by the type of filters. You can add multiple filters by using the commands again.

For example, if you want to look only for devices with the name *test shell*:

```shell
uart:~$ bt scan-filter-set name "test shell"
```

Or if you want to look for devices at a very close range:

```shell
uart:~$ bt scan-filter-set rssi -40
RSSI cutoff set at -40 dB
```

Finally, if you want to remove all filters:

```shell
uart:~$ bt scan-filter-clear all
```

You can use the command `bt scan on` to create an *active* scanner, meaning that the scanner
will ask the advertisers for more information by sending a *scan request* packet. Alternatively, you
can create a *passive scanner* by using the `bt scan passive` command, so the scanner will not
ask the advertiser for more information.

## Connecting to a device

To connect to a device, you need to know its address and type of address and use the
`bt connect` command with the address and the type as arguments.

Here is an example:

```shell
uart:~$ bt connect 52:84:F6:BD:CE:48 random
Connection pending
Connected: 52:84:F6:BD:CE:48 (random)
Remote LMP version 5.3 (0x0c) subversion 0xffff manufacturer 0x05f1
LE Features: 0x000000000001412f
LE PHY updated: TX PHY LE 2M, RX PHY LE 2M
LE conn  param req: int (0x0018, 0x0028) lat 0 to 42
LE conn param updated: int 0x0028 lat 0 to 42
```

You can list the active connections of the shell using the `bt connections` command. The shell
maximum number of connections is defined by [`CONFIG_BT_MAX_CONN`](../../kconfig.md#CONFIG_BT_MAX_CONN "CONFIG_BT_MAX_CONN"). You can disconnect
from a connection with the
`bt disconnect <address: XX:XX:XX:XX:XX:XX> <type: (public|random)>` command.

Note

If you were scanning just before, you can connect to the last scanned device by
simply running the `bt connect` command.

Alternatively, you can use the `bt connect-name <name>` command to automatically
enable scanning with a name filter and connect to the first match.

## Advertising

Begin advertising by using the `bt advertise on` command. This will use the default parameters
and advertise a resolvable private address with the name of the device. You can choose to use the
identity address instead by running the `bt advertise on identity` command. To stop
advertising use the `bt advertise off` command.

To enable more advanced features of advertising, you should create an advertiser using the
`bt adv-create` command. Parameters for the advertiser can be passed either at the creation of
it or by using the `bt adv-param` command. To begin advertising with this newly created
advertiser, use the `bt adv-start` command, and then the `bt adv-stop` command to stop
advertising.

When using the custom advertisers, you can choose if it will be connectable or scannable. This leads
to four options: `conn-scan`, `conn-nscan`, `nconn-scan` and `nconn-nscan`.
Those parameters are mandatory when creating an advertiser or updating its parameters.

For example, if you want to create a connectable and scannable advertiser and start it:

```shell
uart:~$ bt adv-create conn-scan
Created adv id: 0, adv: 0x200022f0
uart:~$ bt adv-start
Advertiser[0] 0x200022f0 set started
```

You may notice that with this, the custom advertiser does not advertise the device name; you need to
enable it. Continuing from the previous example:

```shell
uart:~$ bt adv-stop
Advertiser set stopped
uart:~$ bt adv-param conn-scan name
uart:~$ bt adv-start
Advertiser[0] 0x200022f0 set started
```

You should now see the name of the device in the advertising data. You can also set the advertising
data manually by using the `bt adv-data` command. The following example shows how to set the
advertiser name with it:

```shell
uart:~$ bt adv-create conn-scan
Created adv id: 0, adv: 0x20002348
uart:~$ bt adv-data 1009426C7565746F6F74682D5368656C6C
uart:~$ bt adv-start
Advertiser[0] 0x20002348 set started
```

The data must be formatted according to the Bluetooth Core Specification (see version 5.3, vol. 3,
part C, 11). In this example, the first octet is the size of the data (the data and one octet for
the data type), the second one is the type of data, `0x09` is the Complete Local Name and the
remaining data are the name in ASCII. So, on the other device you should see the name
*Bluetooth-Shell*.

When advertising, if others devices use an *active* scanner, you may receive *scan request* packets.
To visualize those packets, you can add `scan-reports` to the parameters of your advertiser.

### Directed Advertising

It is possible to use directed advertising on the shell if you want to reconnect to a device. The
following example demonstrates how to create a directed advertiser with the address specified right
after the parameter `directed`. The `low` parameter indicates that we want to use the
low duty cycle mode, and the `dir-rpa` parameter is required if the remote device is
privacy-enabled and supports address resolution of the target address in directed advertisement.

```shell
uart:~$ bt adv-create conn-scan directed D7:54:03:CE:F3:B4 random low dir-rpa
Created adv id: 0, adv: 0x20002348
```

After that, you can start the advertiser and then the target device will be able to reconnect.

### Extended Advertising

Let’s now have a look at some extended advertising features. To enable extended advertising, use the
ext-adv parameter.

```shell
uart:~$ bt adv-create conn-nscan ext-adv name-ad
Created adv id: 0, adv: 0x200022f0
uart:~$ bt adv-start
Advertiser[0] 0x200022f0 set started
```

This will create an extended advertiser, that is connectable and non-scannable.

## Filter Accept List

It’s possible to create a list of allowed addresses that can be used to
connect to those addresses automatically. Here is how to do it:

```shell
uart:~$ bt fal-add 47:38:76:EA:29:36 random
uart:~$ bt fal-add 66:C8:80:2A:05:73 random
uart:~$ bt fal-connect on
```

The shell will then connect to the first available device. In the example, if both devices are
advertising at the same time, we will connect to the first address added to the list.

The Filter Accept List can also be used for scanning or advertising by using the option `fal`.
For example, if we want to scan for a bunch of selected addresses, we can set up a Filter Accept
List:

```shell
uart:~$ bt fal-add 65:4B:9E:83:AF:73 random
uart:~$ bt fal-add 73:72:82:B4:8F:B9 random
uart:~$ bt fal-add 5D:85:50:1C:72:64 random
uart:~$ bt scan on fal
```

You should see only those three addresses reported by the scanner.

## Enabling security

When connected to a device, you can enable multiple levels of security, here is the list for
Bluetooth LE:

- **1** No encryption and no authentication;
- **2** Encryption and no authentication;
- **3** Encryption and authentication;
- **4** Bluetooth LE Secure Connection.

To enable security, use the `bt security <level>` command. For levels requiring authentication
(level 3 and above), you must first set the authentication method. To do it, you can use the
`bt auth all` command. After that, when you will set the security level, you will be asked to
confirm the passkey on both devices. On the shell side, do it with the command
`bt auth-passkey-confirm`.

### Pairing

Enabling authentication requires the devices to be bondable. By default the shell is bondable. You
can make the shell not bondable using `bt bondable off`. You can list all the devices you are
paired with using the command `bt bonds`.

The maximum number of paired devices is set using [`CONFIG_BT_MAX_PAIRED`](../../kconfig.md#CONFIG_BT_MAX_PAIRED "CONFIG_BT_MAX_PAIRED"). You can
remove a paired device using `bt clear <address: XX:XX:XX:XX:XX:XX> <type: (public|random)>`
or remove all paired devices with the command `bt clear all`.

## GATT

The following examples assume that you have two devices already connected.

To perform service discovery on the client side, use the `gatt discover` command. This should
print all the services that are available on the GATT server.

On the server side, you can register pre-defined test services using the `gatt register`
command. When done, you should see the newly added services on the client side when running the
discovery command.

You can now subscribe to those new services on the client side. Here is an example on how to
subscribe to the test service:

```shell
uart:~$ gatt subscribe 26 25
Subscribed
```

The server can now notify the client with the command `gatt notify`.

Another option available through the GATT command is initiating the MTU exchange. To do it, use the
`gatt exchange-mtu` command. To update the shell maximum MTU, you need to update Kconfig
symbols in the configuration file of the shell. For more details, see
[Bluetooth: MTU Update](../../samples/bluetooth/mtu_update/README.md#bluetooth-mtu-update-sample).

## L2CAP

The `l2cap` command exposes parts of the L2CAP API. The following example shows how to
register a LE PSM, connect to it from another device and send 3 packets of 14 octets each.

The example assumes that the two devices are already connected.

On device A, register the LE PSM:

```shell
uart:~$ l2cap register 29
L2CAP psm 41 sec_level 1 registered
```

On device B, connect to the registered LE PSM and send data:

```shell
uart:~$ l2cap connect 29
Chan sec: 1
L2CAP connection pending
Channel 0x20000210 connected
Channel 0x20000210 status 1
uart:~$ l2cap send 3 14
Rem 2
Rem 1
Rem 0
Outgoing data channel 0x20000210 transmitted
Outgoing data channel 0x20000210 transmitted
Outgoing data channel 0x20000210 transmitted
```

On device A, you should have received the data:

```shell
Incoming conn 0x20002398
Channel 0x20000210 status 1
Channel 0x20000210 connected
Channel 0x20000210 requires buffer
Incoming data channel 0x20000210 len 14
00000000: ff ff ff ff ff ff ff ff  ff ff ff ff ff ff       |........ ......  |
Channel 0x20000210 requires buffer
Incoming data channel 0x20000210 len 14
00000000: ff ff ff ff ff ff ff ff  ff ff ff ff ff ff       |........ ......  |
Channel 0x20000210 requires buffer
Incoming data channel 0x20000210 len 14
00000000: ff ff ff ff ff ff ff ff  ff ff ff ff ff ff       |........ ......  |
```

## Logging

You can configure the logging level per module at runtime. This depends on the maximum logging level
that is compiled in. To configure, use the `log` command. Here are some examples:

- List the available modules and their current logging level

```shell
uart:~$ log status
```

- Disable logging for *bt\_hci\_core*

```shell
uart:~$ log disable bt_hci_core
```

- Enable error logs for *bt\_att* and *bt\_smp*

```shell
uart:~$ log enable err bt_att bt_smp
```

- Disable logging for all modules

```shell
uart:~$ log disable
```

- Enable warning logs for all modules

```shell
uart:~$ log enable wrn
```
