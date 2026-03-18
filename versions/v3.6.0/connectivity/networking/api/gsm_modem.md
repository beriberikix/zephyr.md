---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/gsm_modem.html
original_path: connectivity/networking/api/gsm_modem.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Generic GSM Modem

## Overview

The generic GSM modem driver allows the user to connect Zephyr to a GSM modem
which provides a data connection to cellular operator’s network.
The Zephyr uses [PPP (Point-to-Point Protocol)](ppp.md#ppp) to connect
to the GSM modem using UART. Note that some cellular modems have proprietary
offloading support using AT commands, but usually those modems also support
3GPP standards and provide PPP connection to them.
See [GSM modem sample application](../../../samples/net/gsm_modem/README.md#gsm-modem "Use a GSM modem to connect to a GPRS network.") how to setup Zephyr
to use the GSM modem.

The GSM muxing, that is defined in
[GSM 07.10](https://www.etsi.org/deliver/etsi_ts/127000_127099/127010/15.00.00_60/ts_127010v150000p.pdf),
and which allows mixing of AT commands and PPP traffic, is also supported in
this version of Zephyr. One needs to enable [`CONFIG_GSM_MUX`](../../../kconfig.md#CONFIG_GSM_MUX "CONFIG_GSM_MUX") and
[`CONFIG_UART_MUX`](../../../kconfig.md#CONFIG_UART_MUX "CONFIG_UART_MUX") configuration options to enable muxing.
