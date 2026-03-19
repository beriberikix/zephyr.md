---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/hci_uart_3wire/README.html
original_path: samples/bluetooth/hci_uart_3wire/README.html
---

# HCI 3-wire (H:5)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/hci_uart_3wire/README.rst/..)

## Overview

Expose Bluetooth controller support over UART to another device/CPU
using the H:5 HCI transport protocol.

## Requirements

- A board with Bluetooth LE support

## Default UART settings

By default the controller builds use the following settings:

- Baudrate: 1Mbit/s
- 8 bits, no parity, 1 stop bit
- Hardware Flow Control (RTS/CTS) disabled

## Building and Running

This sample can be found under [samples/bluetooth/hci\_uart\_3wire](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_uart_3wire) in the
Zephyr tree, and it is built as a standard Zephyr application.

## Using the controller with emulators and BlueZ

The instructions below show how to use a Nordic nRF5x device as a Zephyr BLE
controller and expose it to Linux’s BlueZ. This can be very useful for testing
the Zephyr Link Layer with the BlueZ Host. The Zephyr Bluetooth LE controller can also
provide a modern Bluetooth LE 5.0 controller to a Linux-based machine for native
BLE support or QEMU-based development.

First, make sure you have a recent BlueZ version installed by following the
instructions in the [Using BlueZ with Zephyr](../../../connectivity/bluetooth/bluetooth-tools.md#bluetooth-bluez) section.

Now build and flash the sample for the Nordic nRF5x board of your choice.
All of the Nordic Development Kits come with a Segger IC that provides a
debugger interface and a CDC ACM serial port bridge. More information can be
found in [Nordic nRF5x Segger J-Link](../../../develop/flash_debug/nordic_segger.md#nordic-segger).

For example, to build for the nRF52840 Development Kit:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 samples/bluetooth/hci_uart_3wire
west flash
```

### Using the controller with QEMU or native\_sim

In order to use the HCI UART H:5 controller with QEMU or [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) you will
need to attach it to the Linux Host first. To do so simply build the sample and
connect the UART to the Linux machine, and then attach it with this command:

```shell
sudo hciattach -n /dev/ttyACM0 3wire 1000000
```

Note

Depending on the serial port you are using you will need to modify the
`/dev/ttyACM0` string to point to the serial device your controller is
connected to.

Note

If using the BBC micro:bit you will need to modify the baudrate argument
from `1000000` to `115200`.

Note

The `-R` flag passed to `btattach` instructs the kernel to avoid
interacting with the controller and instead just be aware of it in order
to proxy it to QEMU later.

If you are running `btmon` you should see a brief log showing how the
Linux kernel identifies the attached controller.

Once the controller is attached follow the instructions in the
[Running on QEMU or native\_sim](../../../connectivity/bluetooth/bluetooth-tools.md#bluetooth-qemu-native) section to use QEMU with it.

### Using the controller with BlueZ

In order to use the HCI UART H:5 controller with BlueZ you will need to attach it
to the Linux Host first. To do so simply build the sample and connect the
UART to the Linux machine, and then attach it with this command:

```shell
sudo hciattach -n /dev/ttyACM0 3wire 1000000
```

Note

Depending on the serial port you are using you will need to modify the
`/dev/ttyACM0` string to point to the serial device your controller is
connected to.

Note

If using the BBC micro:bit you will need to modify the baudrate argument
from `1000000` to `115200`.

If you are running `btmon` you should see a comprehensive log showing how
BlueZ loads and initializes the attached controller.

Once the controller is attached follow the instructions in the
[Using Zephyr-based Controllers with BlueZ](../../../connectivity/bluetooth/bluetooth-tools.md#bluetooth-ctlr-bluez) section to use BlueZ with it.

### Debugging the controller

The sample can be debugged using RTT since the UART is otherwise used by this
application. To enable debug over RTT the debug configuration file can be used.

```shell
west build samples/bluetooth/hci_uart_3wire -- -DEXTRA_CONF_FILE='debug.conf'
```

Then attach RTT as described here: [Using Segger J-Link](../../../develop/flash_debug/probes.md#using-segger-j-link)

### Support for the Direction Finding

The sample can be built with the support for the Bluetooth LE Direction Finding.
To enable this feature build this sample for specific board variants that provide
required hardware configuration for the Radio.

```shell
west build samples/bluetooth/hci_uart_3wire -b nrf52833dk/nrf52833@df -- -DCONFIG_BT_CTLR_DF=y
```

You can use following targets:

- `nrf5340dk/nrf5340/cpunet@df`
- `nrf52833dk/nrf52833@df`

Check the [Direction Finding Periodic Advertising Locator](../direction_finding_connectionless_rx/README.md#ble_direction_finding_connectionless_rx "Implement Bluetooth LE Direction Finding CTE Locator functionality.") and the
[Direction Finding Periodic Advertising Beacon](../direction_finding_connectionless_tx/README.md#ble_direction_finding_connectionless_tx "Implement Bluetooth LE Direction Finding CTE Broadcaster functionality.") for more details.

### Using a USB CDC ACM UART

The sample can be configured to use a USB UART instead. See [samples/bluetooth/hci\_uart\_3wire/boards/nrf52840dongle\_nrf52840.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_uart_3wire/boards/nrf52840dongle_nrf52840.conf).

### Using the controller with the Zephyr host

This describes how to hook up a board running this sample to a board running
an application that uses the Zephyr host.

On the controller side, the `zephyr,bt-c2h-uart` DTS property (in the `chosen`
block) is used to select which uart device to use. For example if we want to
keep the console logs, we can keep console on uart0 and the HCI on uart1 like
so:

```dts
/ {
   chosen {
      zephyr,console = &uart0;
      zephyr,shell-uart = &uart0;
      zephyr,bt-c2h-uart = &uart1;
   };
};
```

On the host application, some config options need to be used to select the H5
driver instead of the built-in controller:

```cfg
CONFIG_BT_HCI=y
CONFIG_BT_CTLR=n
```

Similarly, the `zephyr,bt-hci` DTS property selects which HCI instance to use.
The UART needs to have as its child node a HCI UART node:

```dts
/ {
   chosen {
      zephyr,console = &uart0;
      zephyr,shell-uart = &uart0;
      zephyr,bt-hci = &bt_hci_uart;
   };
};

&uart1 {
   status = "okay";
   bt_hci_uart: bt_hci_uart {
      compatible = "zephyr,bt-hci-3wire-uart";
      status = "okay";
   };
};
```

## See also

[HCI RAW channel](../../../doxygen/html/group__hci__raw.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

[UART Interface](../../../doxygen/html/group__uart__interface.md)
