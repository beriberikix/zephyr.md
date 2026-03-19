---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/direction_finding_connectionless_tx/README.html
original_path: samples/bluetooth/direction_finding_connectionless_tx/README.html
---

# Direction Finding Periodic Advertising Beacon

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/direction_finding_connectionless_tx/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth LE Direction Finding CTE Broadcaster
functionality by sending Constant Tone Extension with periodic advertising PDUs.

## Requirements

- Nordic nRF SoC based board with Direction Finding support (example boards:
  [nRF52833 DK](../../../boards/nordic/nrf52833dk/doc/index.md#nrf52833dk-nrf52833), [nRF5340 DK](../../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340))
- Antenna matrix for AoD (optional)

Check your SoC’s product specification for Direction Finding support if you are
unsure.

## Building and Running

By default the application supports Angle of Arrival (AoA) and Angle of
Departure (AoD) mode.

To use Angle of Arrival mode only, build this application as follows, changing
`nrf52833dk/nrf52833` as needed for your board:

```shell
west build -b nrf52833dk/nrf52833 samples/bluetooth/direction_finding_connectionless_tx -- -DEXTRA_CONF_FILE=overlay-aoa.conf
west flash
```

To run the application on nRF5340DK, a Bluetooth controller application must
also run on the network core. The [samples/bluetooth/hci\_ipc](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc)
sample application may be used. To build this sample with direction finding
support enabled:

- Copy
  [samples/bluetooth/direction\_finding\_connectionless\_tx/boards/nrf52833dk\_nrf52833.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_connectionless_tx/boards/nrf52833dk_nrf52833.overlay)
  to a new file,
  `samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.overlay`.
- Make sure the same GPIO pins are assigned to Direction Finding Extension in file
  [samples/bluetooth/direction\_finding\_connectionless\_tx/boards/nrf5340dk\_nrf5340\_cpuapp.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_connectionless_tx/boards/nrf5340dk_nrf5340_cpuapp.overlay).
  as those in the created file `samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.overlay`.
- Copy
  [samples/bluetooth/direction\_finding\_connectionless\_tx/boards/nrf52833dk\_nrf52833.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_connectionless_tx/boards/nrf52833dk_nrf52833.conf)
  to a new file,
  `samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.conf`. Add
  the line `CONFIG_BT_EXT_ADV=y` to enable extended size of
  [`CONFIG_BT_BUF_CMD_TX_SIZE`](../../../kconfig.md#CONFIG_BT_BUF_CMD_TX_SIZE "CONFIG_BT_BUF_CMD_TX_SIZE") to support the LE Set Extended
  Advertising Data command.

## Antenna matrix configuration

To use this sample with Angle of Departure enabled on Nordic SoCs, additional
configuration must be provided via [devicetree](../../../build/dts/index.md#dt-guide) to enable
control of the antenna array, as well as via the `ant_patterns` array in the
source code.

An example devicetree overlay is in
[samples/bluetooth/direction\_finding\_connectionless\_tx/boards/nrf52833dk\_nrf52833.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_connectionless_tx/boards/nrf52833dk_nrf52833.overlay).
You can customize this overlay when building for the same board, or create your
own board-specific overlay in the same directory for a different board. See
[`nordic,nrf-radio`](../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) for documentation on the properties used in
this overlay. See [Set devicetree overlays](../../../build/dts/howtos.md#set-devicetree-overlays) for information on setting up
and using overlays.

Note that antenna matrix configuration for the nRF5340 SoC is part of the
network core application. When [HCI IPC](../hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") is used as
network core application, the antenna matrix configuration should be stored in
the file
`samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.overlay`
instead.

In addition to the devicetree configuration, to successfully use the Direction
Finding locator when the AoA mode is enabled, also update the antenna patterns
in the `ant_patterns` array in
[samples/bluetooth/direction\_finding\_connectionless\_tx/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_connectionless_tx/src/main.c).

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
