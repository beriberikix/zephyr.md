---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/fpga/fpga_controller/README.html
original_path: samples/drivers/fpga/fpga_controller/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# FPGA Controller

## Overview

This module is an FPGA driver that can easily load a bitstream, reset it, check its status, enable or disable the FPGA.
This sample demonstrates how to use the FPGA driver API and the FPGA controller shell subsystem.
Currently the sample works with [Quicklogic Quickfeather board](https://github.com/QuickLogic-Corp/quick-feather-dev-board).

## Requirements

- Zephyr RTOS
  or
- Zephyr RTOS with shell subsystem enabled (for shell application)
- [Quicklogic Quickfeather board](https://github.com/QuickLogic-Corp/quick-feather-dev-board)

## Building

For building on QuickLogic QuickFeather board:

```shell
# From the root of the zephyr repository
west build -b quick_feather samples/drivers/fpga/fpga_controller
```

To build the FPGA Controller shell application, use the supplied
configuration file prj\_shell.conf:

```shell
west build -b quick_feather samples/drivers/fpga/fpga_controller -- -DCONF_FILE=prj_shell.conf
```

## Running

See [QuickFeather](../../../../boards/quicklogic/quick_feather/doc/index.md#quickfeather) on how to load an image to the board.

### Sample output

Once the board is programmed, the LED should alternately flash red and green.

For the FPGA controller shell application, after connecting to the shell console you should see the following output:

```shell
Address of the bitstream (red): 0xADDR
Address of the bitstream (green): 0xADDR
Size of the bitstream (red): 75960
Size of the bitstream (green): 75960

uart:~$
```

This sample is already prepared with bitstreams.
After executing the sample, you can see at what address it is stored and its size in bytes.

The FPGA controller command can now be used (`fpga load <device> <address> <size in bytes>`):

```shell
uart:~$ fpga load FPGA 0x2001a46c 75960
FPGA: loading bitstream
```

The LED should start blinking (color depending on the selected bitstream).
To upload the bitstream again you need to reset the FPGA:

```shell
uart:~$ fpga reset FPGA
FPGA: resetting FPGA
```

You can also use your own bitstream.
To load a bitstream into device memory, use devmem load command.
It is important to use the -e option when sending a bitstream via xxd:

```shell
uart:~$ devmem load -e 0x10000
Loading...
Press ctrl-x + ctrl-q to stop
```

Now, the loader is waiting for data.
You can either type it directly from the console or send it from the host PC (replace ttyX with the appropriate one for your shell console):

```shell
xxd -p data > /dev/ttyX
```

(It is important to use plain-style hex dump)
Once the data is transferred, use ctrl-x + ctrl-q to quit loader.
It will print the sum of the read bytes and return to the shell:

```shell
Number of bytes read: 75960
uart:~$
```

Now the bitstream can be uploaded again.

```shell
uart:~$ fpga load FPGA 0x10000 75960
FPGA: loading bitstream
```

## References
