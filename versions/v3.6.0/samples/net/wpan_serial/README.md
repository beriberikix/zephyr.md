---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/wpan_serial/README.html
original_path: samples/net/wpan_serial/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# 802.15.4 “serial-radio”

## Overview

The wpan\_serial sample shows how to use hardware with 802.15.4 radio and USB
controller as a “serial-radio” device for Contiki-based border routers.

## Requirements

The sample assumes that 802.15.4 radio and USB controller are supported on
a board. You can pick, for example, a transceiver such as a CC2520 or RF2xx
using overlays, or by using an SoC with a built-in radio, such as a kw41z,
nrf5, or samr21.

## Building and Running

1. Before building and running this sample, be sure your Linux system’s
   ModemManager is disabled, otherwise, it can interfere with serial
   port communication:

   ```shell
   $ sudo systemctl disable ModemManager.service
   ```
2. Build the sample Zephyr application to a board with a 802.15.4 radio
   and USB controller. There are configuration files for various setups
   in the `samples/net/wpan_serial` directory:

   - `prj.conf`
     This is the standard default config. This can be used by itself for
     hardware which has native 802.15.4 support.

   To build the wpan\_serial sample:

   ```shell
   west build -b <board name> samples/net/wpan_serial -- -DCONF_FILE="prj.conf [overlay-<RADIO>.conf]"
   ```

   Here’s how to build and flash the sample for the Atmel SAM R21
   Xplained Pro Development Kit.

   ```shell
   west build -b atsamr21_xpro samples/net/wpan_serial
   west flash
   ```
3. Connect board to Linux PC, /dev/ttyACM[number] should appear.
4. Run Contiki-based native border router (6lbr, native-router, etc)
   Example for Contiki:

   ```shell
   $ cd examples/ipv6/native-border-router
   $ make
   $ sudo ./border-router.native -v5 -s ttyACM0 fd01::1/64
   ```

Now you have a Contiki native board router. You can access its web-based
interface with your browser using the server address printed in the
border-router output.

```shell
...
Server IPv6 addresses:
 0x62c5c0: =>fd01::212:4b00:531f:113a
...
```

Use your browser to access `http://[fd01::212:4b00:531f:113a]/` and you’ll
see available neighbors and routes.
