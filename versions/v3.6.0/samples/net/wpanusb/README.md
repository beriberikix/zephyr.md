---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/wpanusb/README.html
original_path: samples/net/wpanusb/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# 802.15.4 USB

## Overview

This application exports ieee802154 radio over USB to be used in
other OSes such as Linux. For Linux, the ieee802154 stack would be
implemented using the Linux SoftMAC driver.
This sample can be found under [samples/net/wpanusb](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wpanusb) in the
Zephyr project tree.

## Requirements

- a Zephyr board with supported 802.15.4 radio and supported USB driver
  (such as the [nRF52840 DK](../../../boards/arm/nrf52840dk_nrf52840/doc/index.md#nrf52840dk-nrf52840) or [SAM R21 Xplained Pro Evaluation Kit](../../../boards/arm/atsamr21_xpro/doc/index.md#atsamr21-xpro))
  connected via USB to a Linux host
- wpanusb Linux kernel driver (in the process of being open sourced)
- wpan-tools (available for all Linux distributions)

## Building and Running

There are configuration files for various setups in the
`samples/net/wpanusb` directory:

- `prj.conf`
  :   This is the standard default config. This can be used by itself for
      hardware which has native 802.15.4 support.
- `overlay-cc2520.conf`
  :   This overlay config enables support for CC2520

Build the wpanusb sample for a board:

```shell
west build -b <board to use> samples/net/wpanusb -- -DEXTRA_CONF_FILE=<overlay file to use>
```

Example building for the Nordic nRF52840 Development Kit:

```shell
west build -b nrf52840dk_nrf52840 samples/net/wpanusb
```

When connected to Linux with wpanusb kernel driver, it is recognized as:

```shell
...
T:  Bus=01 Lev=02 Prnt=02 Port=00 Cnt=01 Dev#=  3 Spd=12  MxCh= 0
D:  Ver= 1.10 Cls=ff(vend.) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=2fe3 ProdID=000d Rev=01.00
C:  #Ifs= 1 Cfg#= 1 Atr=c0 MxPwr=100mA
I:  If#= 0 Alt= 0 #EPs= 1 Cls=ff(vend.) Sub=00 Prot=00 Driver=wpanusb
...
```

The following script enables the network interface in Linux
(uses iwpan tool from above):

```shell
#!/bin/sh
PHY=`iwpan phy | grep wpan_phy | cut -d' ' -f2`
echo 'Using phy' $PHY
iwpan dev wpan0 set pan_id 0xabcd
iwpan dev wpan0 set short_addr 0xbeef
iwpan phy $PHY set channel 0 26
ip link add link wpan0 name lowpan0 type lowpan
ip link set wpan0 up
ip link set lowpan0 up
```
