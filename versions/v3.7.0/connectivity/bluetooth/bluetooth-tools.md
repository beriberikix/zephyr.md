---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/bluetooth-tools.html
original_path: connectivity/bluetooth/bluetooth-tools.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Tools

This page lists and describes tools that can be used to assist during Bluetooth
stack or application development in order to help, simplify and speed up the
development process.

## [Mobile applications](#id2)

It is often useful to make use of existing mobile applications to interact with
hardware running Zephyr, to test functionality without having to write any
additional code or requiring extra hardware.

The recommended mobile applications for interacting with Zephyr are:

- Android:

  - [nRF Connect for Android](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en)
  - [nRF Mesh for Android](https://play.google.com/store/apps/details?id=no.nordicsemi.android.nrfmeshprovisioner&hl=en)
  - [LightBlue for Android](https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer&hl=en_US)
- iOS:

  - [nRF Connect for iOS](https://itunes.apple.com/us/app/nrf-connect/id1054362403)
  - [nRF Mesh for iOS](https://itunes.apple.com/us/app/nrf-mesh/id1380726771)
  - [LightBlue for iOS](https://itunes.apple.com/us/app/lightblue-explorer/id557428110)

## [Using BlueZ with Zephyr](#id3)

The Linux Bluetooth Protocol Stack, BlueZ, comes with a very useful set of
tools that can be used to debug and interact with Zephyr’s BLE Host and
Controller. In order to benefit from these tools you will need to make sure
that you are running a recent version of the Linux Kernel and BlueZ:

- Linux Kernel 4.10+
- BlueZ 4.45+

Additionally, some of the BlueZ tools might not be bundled by default by your
Linux distribution. If you need to build BlueZ from scratch to update to a
recent version or to obtain all of its tools you can follow the steps below:

```shell
git clone git://git.kernel.org/pub/scm/bluetooth/bluez.git
cd bluez
./bootstrap-configure --disable-android --disable-midi
make
```

You can then find `btattach`, `btmgt` and `btproxy` in the
`tools/` folder and `btmon` in the `monitor/` folder.

You’ll need to enable BlueZ’s experimental features so you can access its
most recent BLE functionality. Do this by editing the file
`/lib/systemd/system/bluetooth.service`
and making sure to include the `-E` option in the daemon’s execution
start line:

```shell
ExecStart=/usr/libexec/bluetooth/bluetoothd -E
```

Finally, reload and restart the daemon:

```shell
sudo systemctl daemon-reload
sudo systemctl restart bluetooth
```

## [Running on QEMU or native\_sim](#id4)

It’s possible to run Bluetooth applications using either the [QEMU
emulator](../../develop/application/index.md#application-run-qemu) or [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim).

In either case, a Bluetooth controller needs to be exported from
the host OS (Linux) to the emulator. For this purpose you will need some tools
described in the [Using BlueZ with Zephyr](#bluetooth-bluez) section.

### [Using the Host System Bluetooth Controller](#id5)

The host OS’s Bluetooth controller is connected in the following manner:

- To the second QEMU serial line using a UNIX socket. This socket gets used
  with the help of the QEMU option `-serial unix:/tmp/bt-server-bredr`.
  This option gets passed to QEMU through **QEMU\_EXTRA\_FLAGS**
  automatically whenever an application has enabled Bluetooth support.
- To [native\_sim’s BT User Channel driver](../../boards/native/native_sim/doc/index.md#nsim-bt-host-cont) through the use of a
  command-line option passed to the native\_sim executable: `--bt-dev=hci0`

On the host side, BlueZ allows you to export its Bluetooth controller
through a so-called user channel for QEMU and [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim) to use.

Note

You only need to run `btproxy` when using QEMU. native\_sim handles
the UNIX socket proxying automatically

If you are using QEMU, in order to make the Controller available you will need
one additional step using `btproxy`:

1. Make sure that the Bluetooth controller is down
2. Use the btproxy tool to open the listening UNIX socket, type:

   ```shell
   sudo tools/btproxy -u -i 0
   Listening on /tmp/bt-server-bredr
   ```

   You might need to replace `-i 0` with the index of the Controller
   you wish to proxy.

   If you see `Received unknown host packet type 0x00` when running QEMU, then
   add `-z` to the `btproxy` command line to ignore any null bytes
   transmitted at startup.

Once the hardware is connected and ready to use, you can then proceed to
building and running a sample:

- Choose one of the Bluetooth sample applications located in
  `samples/bluetooth`.
- To run a Bluetooth application in QEMU, type:

  ```shell
  west build -b qemu_x86 samples/bluetooth/<sample>
  west build -t run
  ```

  Running QEMU now results in a connection with the second serial line to
  the `bt-server-bredr` UNIX socket, letting the application
  access the Bluetooth controller.
- To run a Bluetooth application in [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim), first build it:

  ```shell
  west build -b native_sim samples/bluetooth/<sample>
  ```

  And then run it with:

  ```text
  $ sudo ./build/zephyr/zephyr.exe --bt-dev=hci0
  ```

### [Using a Zephyr-based BLE Controller](#id6)

Depending on which hardware you have available, you can choose between two
transports when building a single-mode, Zephyr-based BLE Controller:

- UART: Use the [hci\_uart](../../samples/bluetooth/hci_uart/README.md#bluetooth-hci-uart-sample) sample and follow
  the instructions in [Using the controller with QEMU or native\_sim](../../samples/bluetooth/hci_uart/README.md#bluetooth-hci-uart-qemu-posix).
- USB: Use the [hci\_usb](../../samples/bluetooth/hci_usb/README.md#bluetooth-hci-usb-sample) sample and then
  treat it as a Host System Bluetooth Controller (see previous section)

### [HCI Tracing](#id7)

When running the Host on a computer connected to an external Controller, it
is very useful to be able to see the full log of exchanges between the two,
in the format of a [Host Controller Interface](bluetooth-arch.md#bluetooth-hci) log.
In order to see those logs, you can use the built-in `btmon` tool from BlueZ:

```shell
$ btmon
```

The output looks like this:

```text
= New Index: 00:00:00:00:00:00 (Primary,Virtual,Control)                     0.274200
= Open Index: 00:00:00:00:00:00                                              0.274500
< HCI Command: Reset (0x03|0x0003) plen 0                                 #1 0.274600
> HCI Event: Command Complete (0x0e) plen 4                               #2 0.274700
      Reset (0x03|0x0003) ncmd 1
      Status: Success (0x00)
< HCI Command: Read Local Supported Features (0x04|0x0003) plen 0         #3 0.274800
> HCI Event: Command Complete (0x0e) plen 12                              #4 0.274900
      Read Local Supported Features (0x04|0x0003) ncmd 1
      Status: Success (0x00)
      Features: 0x00 0x00 0x00 0x00 0x60 0x00 0x00 0x00
         BR/EDR Not Supported
         LE Supported (Controller)
```

#### Embedded HCI tracing

When running both Host and Controller in actual Integrated Circuits, you will
only see normal log messages on the console by default, without any way of
accessing the HCI traffic between the Host and the Controller. However, there
is a special Bluetooth logging mode that converts the console to use a binary
protocol that interleaves both normal log messages as well as the HCI traffic.

Set the following Kconfig options to enable this protocol before building your
application:

```cfg
CONFIG_BT_DEBUG_MONITOR_UART=y
CONFIG_UART_CONSOLE=n
```

- Setting [`CONFIG_BT_DEBUG_MONITOR_UART`](../../kconfig.md#CONFIG_BT_DEBUG_MONITOR_UART "CONFIG_BT_DEBUG_MONITOR_UART") activates the formatting
- Clearing [`CONFIG_UART_CONSOLE`](../../kconfig.md#CONFIG_UART_CONSOLE "CONFIG_UART_CONSOLE") makes the UART unavailable for
  the system console. E.g. for `printk` and the [`boot banner`](../../kconfig.md#CONFIG_BOOT_BANNER "CONFIG_BOOT_BANNER")

To decode the binary protocol that will now be sent to the console UART you need
to use the btmon tool from [BlueZ](#bluetooth-bluez):

```shell
$ btmon --tty <console TTY> --tty-speed 115200
```

If UART is not available (or you still want non-binary logs), you can set
[`CONFIG_BT_DEBUG_MONITOR_RTT`](../../kconfig.md#CONFIG_BT_DEBUG_MONITOR_RTT "CONFIG_BT_DEBUG_MONITOR_RTT") instead, which will use Segger
RTT. For example, if trying to connect to a nRF52840DK with S/N 683578642:

```shell
$ btmon --jlink nRF52840_xxAA,683578642
```

## [Running on a Virtual Controller and native\_sim](#id8)

An alternative to a Bluetooth physical controller is the use of a virtual
controller. This controller can be connected over an HCI TCP server.
This TCP server must support the HCI H4 protocol. In comparison to the physical controller
variant, the virtual controller allows to test a Zephyr application running on the native
boards without a physical Bluetooth controller.

The main use case for a virtual controller is to do Bluetooth connectivity tests without
the need of Bluetooth hardware. This allows to automate Bluetooth integration tests with
external applications such as a Bluetooth gateway or a mobile application.

To demonstrate this functionality an example is given to interact with a virtual controller.
For this purpose, the experimental python module [Bumble](https://github.com/google/bumble) from Google is used as it allows to create
a TCP Bluetooth virtual controller and connect with the Zephyr Bluetooth host. To install
bumble follow the [Bumble Getting Started Guide](https://google.github.io/bumble/getting_started.html).

Note

If your Zephyr application requires the use of the HCI LE Set extended commands, install
the branch `controller-extended-advertising` from Bumble.

### [Android Emulator](#id9)

You can test the virtual controller by connecting a Bluetooth Zephyr application
to the [Android Emulator](https://developer.android.com/studio/run/emulator).

To connect your application to the Android Emulator follow the next steps:

> 1. Build your Zephyr application and disable the HCI ACL flow
>    control (i.e. `CONFIG_BT_HCI_ACL_FLOW_CONTROL=n`) as the
>    virtual controller from android does not support it at the moment.
> 2. Install Android Emulator version >= 33.1.4.0. The easiest way to do this is by installing
>    the latest [Android Studio Preview](https://developer.android.com/studio/preview) version.
> 3. Create a new Android Virtual Device (AVD) with the [Android Device Manager](https://developer.android.com/studio/run/managing-avds). The AVD should use at least SDK API 34.
> 4. Run the Android Emulator via terminal as follows:
>
>    `emulator avd YOUR_AVD -packet-streamer-endpoint default`
> 5. Create a Bluetooth bridge between the Zephyr application and
>    the virtual controller from Android Emulator with the [Bumble](https://github.com/google/bumble) utility `hci-bridge`.
>
>    `bumble-hci-bridge tcp-server:_:1234 android-netsim`
>
>    This command will create a TCP server bridge on the local host IP address `127.0.0.1`
>    and port number `1234`.
> 6. Run the Zephyr application and connect to the TCP server created in the last step.
>
>    `./zephyr.exe --bt-dev=127.0.0.1:1234`

After following these steps the Zephyr application will be available to the Android Emulator
over the virtual Bluetooth controller that was bridged with Bumble. You can verify that the
Zephyr application can communicate over Bluetooth by opening the Bluetooth settings in your
AVD and scanning for your Zephyr application device. To test this you can build the Bluetooth
peripheral samples such as [Peripheral HR](../../samples/bluetooth/peripheral_hr/README.md#peripheral-hr) or [Peripheral DIS](../../samples/bluetooth/peripheral_dis/README.md#peripheral-dis)

## [Using Zephyr-based Controllers with BlueZ](#id10)

If you want to test a Zephyr-powered BLE Controller using BlueZ’s Bluetooth
Host, you will need a few tools described in the [Using BlueZ with Zephyr](#bluetooth-bluez) section.
Once you have installed the tools you can then use them to interact with your
Zephyr-based controller:

> ```shell
> sudo tools/btmgmt --index 0
> [hci0]# auto-power
> [hci0]# find -l
> ```

You might need to replace `--index 0` with the index of the Controller
you wish to manage.
Additional information about `btmgmt` can be found in its manual pages.
