---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/tracing/README.html
original_path: samples/subsys/tracing/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Tracing

This application can be used to demonstrate the tracing feature. The tracing
formatted packet will be sent to the host with the currently supported tracing
backend under tracing generic infrastructure.

## Requirements

Depends of the boards which you are using, choose one of .conf files for use tracing subsys.

## Usage for UART Tracing Backend

Build a UART-tracing image with:

```shell
west build -b mps2_an521 samples/subsys/tracing -- -DCONF_FILE="prj_uart.conf"
```

or:

```shell
west build -b mps2_an521 samples/subsys/tracing -- -DCONF_FILE="prj_uart_ctf.conf"
```

Note

You may need to set “zephyr,tracing-uart” property under the chosen node in your devicetree. See [boards/mps2\_an521.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/mps2_an521.overlay) for an example.

After the application has run for a while, check the trace output file.

## Usage for USB Tracing Backend

Build a USB-tracing image with:

```shell
west build -b sam_e70_xplained samples/subsys/tracing -- -DCONF_FILE="prj_usb.conf"
```

or:

```shell
west build -b sam_e70_xplained samples/subsys/tracing -- -DCONF_FILE="prj_usb_ctf.conf"
```

After the serial console has stable output like this:

```shell
threadA: Hello World!
threadB: Hello World!
threadA: Hello World!
threadB: Hello World!
```

Connect the board’s USB port to the host device and
run the [scripts/tracing/trace\_capture\_usb.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/tracing/trace_capture_usb.py) script on the host:

```shell
sudo python3 trace_capture_usb.py -v 0x2FE9 -p 0x100 -o channel0_0
```

The VID and PID of USB device can be configured, just adjusting it accordingly.

## Usage for POSIX Tracing Backend

Build a POSIX-tracing image with:

```shell
west build -b native_sim samples/subsys/tracing
```

or:

```shell
west build -b native_sim samples/subsys/tracing -- -DCONF_FILE="prj_native_ctf.conf"
```

After the application has run for a while, check the trace output file.

## Usage for USER Tracing Backend

Build a USER-tracing image with:

```shell
west build -b qemu_x86 samples/subsys/tracing -- -DCONF_FILE="prj_user.conf"
```

After the application has run for a while, check the trace output file.
