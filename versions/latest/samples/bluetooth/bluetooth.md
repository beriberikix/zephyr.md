---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/bluetooth.html
original_path: samples/bluetooth/bluetooth.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth samples

To build any of the Bluetooth samples, follow the same steps as building
any other Zephyr application. Refer to [Developing Bluetooth Applications](../../connectivity/bluetooth/bluetooth-dev.md#bluetooth-dev) for more information.

Many Bluetooth samples can be run on QEMU or [native\_sim](../../boards/posix/native_sim/doc/index.md#native-sim) with support for
external Bluetooth Controllers. Refer to the [Hardware setup](../../connectivity/bluetooth/bluetooth-dev.md#bluetooth-hw-setup) section
for further details.

Several of the bluetooth samples will build a Zephyr-based Controller that can
then be used with any external Host (including Zephyr running natively or with
QEMU or `native_sim`), those are named accordingly with an “HCI” prefix in the
documentation and are prefixed with `hci_` in their folder names.

Note

If you want to run any bluetooth sample on the nRF5340 device (build using
`-DBOARD=nrf5340dk_nrf5340_cpuapp` or
`-DBOARD=nrf5340dk_nrf5340_cpuapp_ns`) you must also build
and program the corresponding sample for the nRF5340 network core
[Bluetooth: HCI IPC](hci_ipc/README.md#bluetooth-hci-ipc-sample) which implements the Bluetooth
Low Energy controller.

Note

The mutually-shared encryption key created during host-device paring may get
old after many test iterations. If this happens, subsequent host-device
connections will fail. You can force a re-paring and new key to be created
by removing the device from the associated devices list on the host.
