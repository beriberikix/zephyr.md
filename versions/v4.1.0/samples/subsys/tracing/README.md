---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/tracing/README.html
original_path: samples/subsys/tracing/README.html
---

# Tracing

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/tracing/README.rst/..)

This application can be used to demonstrate the tracing feature. The tracing
formatted packet will be sent to the host with the currently supported tracing
backend under tracing generic infrastructure.

## Requirements

Depends of the boards which you are using, choose one of .conf files for use tracing subsys.

## Usage for UART Tracing Backend

Build a UART-tracing image with:

```shell
west build -b mps2/an521 samples/subsys/tracing -- -DCONF_FILE="prj_uart.conf"
```

or:

```shell
west build -b mps2/an521 samples/subsys/tracing -- -DCONF_FILE="prj_uart_ctf.conf"
```

Note

You may need to set “zephyr,tracing-uart” property under the chosen node in your devicetree.
See [samples/subsys/tracing/boards/mps2\_an521\_cpu0.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/tracing/boards/mps2_an521_cpu0.overlay) for an example.

After the application has run for a while, check the trace output file.

## Usage for USB Tracing Backend

Build a USB-tracing image with:

```shell
west build -b sam_e70_xplained/same70q21 samples/subsys/tracing -- -DCONF_FILE="prj_usb.conf"
```

or:

```shell
west build -b sam_e70_xplained/same70q21 samples/subsys/tracing -- -DCONF_FILE="prj_usb_ctf.conf"
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

## Usage for SEGGER SystemView RTT

Build a SystemView-tracing image with the [SystemView RTT Tracing Snippet (rtt-tracing)](../../../snippets/rtt-tracing/README.md#snippet-rtt-tracing):

```shell
west build -b frdm_k64f -S rtt-tracing samples/subsys/tracing
```

After the application has run for a while, check the trace output file.

## Usage for GPIO Tracing Backend

Build a GPIO-tracing image with:

```shell
west build -b native_sim samples/subsys/tracing -- -DCONF_FILE="prj_gpio.conf"
```

After the application has run for a while, check the trace output file.
