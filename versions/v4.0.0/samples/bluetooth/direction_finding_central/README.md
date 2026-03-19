---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/direction_finding_central/README.html
original_path: samples/bluetooth/direction_finding_central/README.html
---

# Direction Finding Central

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/direction_finding_central/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth LE Direction Finding CTE reception in
connected mode by requesting transmission of a packet containing Constant
Tone Extension by connected peer device.

## Requirements

- Nordic nRF SoC based board with Direction Finding support (example boards:
  [nRF52833 DK](../../../boards/nordic/nrf52833dk/doc/index.md#nrf52833dk-nrf52833), [nRF52820 emulation on nRF52833 DK](../../../boards/nordic/nrf52833dk/doc/index.md#nrf52833dk-nrf52820), [nRF5340 DK](../../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340))
- Antenna matrix for AoA (optional)

Check your SoC’s product specification for Direction Finding support if you are
unsure.

## Building and Running

By default the application supports Angle of Arrival and Angle of Departure mode.

To use Angle of Departure mode only, build this application as follows,
changing `nrf52833dk/nrf52833` as needed for your board:

```shell
west build -b nrf52833dk/nrf52833 samples/bluetooth/direction_finding_central -- -DEXTRA_CONF_FILE=overlay-aod.conf
west flash
```

To run the application on nRF5340DK, a Bluetooth controller application must
also run on the network core. The [HCI IPC](../hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") sample
application may be used. To build this sample with direction finding support
enabled:

- Copy
  [samples/bluetooth/direction\_finding\_central/boards/nrf52833dk\_nrf52833.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_central/boards/nrf52833dk_nrf52833.overlay)
  to a new file,
  `samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.overlay`.
- Make sure the same GPIO pins are assigned to Direction Finding Extension in file
  [samples/bluetooth/direction\_finding\_central/boards/nrf5340dk\_nrf5340\_cpuapp.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_central/boards/nrf5340dk_nrf5340_cpuapp.overlay).
  as those in the created file `samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.overlay`.
- Copy
  [samples/bluetooth/direction\_finding\_central/boards/nrf52833dk\_nrf52833.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_central/boards/nrf52833dk_nrf52833.conf)
  to a new file,
  `samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.conf`.

## Antenna matrix configuration

To use this sample with Angle of Arrival enabled on Nordic SoCs, additional
configuration must be provided via [devicetree](../../../build/dts/index.md#dt-guide) to enable
control of the antenna array.

An example devicetree overlay is in
[samples/bluetooth/direction\_finding\_central/boards/nrf52833dk\_nrf52833.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direction_finding_central/boards/nrf52833dk_nrf52833.overlay).
You can customize this overlay when building for the same board, or create your
own board-specific overlay in the same directory for a different board. See
[`nordic,nrf-radio`](../../../build/dts/api/bindings/net/wireless/nordic%2Cnrf-radio.md#std-dtcompatible-nordic-nrf-radio) for documentation on the properties used in
this overlay. See [Set devicetree overlays](../../../build/dts/howtos.md#set-devicetree-overlays) for information on setting up
and using overlays.

Note that antenna matrix configuration for the nRF5340 SoC is part of the
network core application. When [HCI IPC](../hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") is used as the
network core application, the antenna matrix configuration should be stored in
the file
`samples/bluetooth/hci_ipc/boards/nrf5340dk_nrf5340_cpunet.overlay`
instead.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
