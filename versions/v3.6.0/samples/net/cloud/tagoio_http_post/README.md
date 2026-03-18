---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/cloud/tagoio_http_post/README.html
original_path: samples/net/cloud/tagoio_http_post/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# TagoIO HTTP Post

## Overview

This sample application implements an HTTP client that will do an HTTP post
request to [TagoIO](https://tago.io/) [[1]](#id1) IoT Service Platform. The sample sends random temperature
values to simulate a real device. This can be used to speed-up development
and shows how to send simple JSON data to [TagoIO](https://tago.io/) [[1]](#id1) servers.

The source code for this sample application can be found at:
[samples/net/cloud/tagoio\_http\_post](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/tagoio_http_post).

## Requirements

- A free [TagoIO](https://tago.io/) [[1]](#id1) account
- A board with internet connectivity, see [Networking](../../../../connectivity/networking/index.md#networking)
- The example provides three ways to get internet:

  - Ethernet: Using default configuration
  - WiFi: Using default configuration plus wifi overlay
  - Modem: Using default configuration plus modem overlay

## TagoIO Device Configuration

If you don’t have a [TagoIO](https://tago.io/) [[1]](#id1) account, simple create a free account at
[TagoIO](https://tago.io/) [[1]](#id1). After that, add a device selecting Custom HTTP(S) protocol. That
is it! Now reveal your device token. The token will be used to identify your
device when sending data. You need fill `CONFIG_TAGOIO_DEVICE_TOKEN` at
[samples/net/cloud/tagoio\_http\_post/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/tagoio_http_post/prj.conf) file with that
information.

## Building and Running

### Ethernet

You can use this application on a supported board with ethernet port. There
are many like [SAM4E Xplained Pro](../../../../boards/arm/sam4e_xpro/doc/index.md#sam4e-xpro), [SAM V71(B) Xplained Ultra](../../../../boards/arm/sam_v71_xult/doc/index.md#sam-v71-xplained-ultra),
[NXP FRDM-K64F](../../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f), [ST Nucleo F767ZI](../../../../boards/arm/nucleo_f767zi/doc/index.md#nucleo-f767zi-board) etc. Pick one and just build
tagoio-http-client sample application with minimal configuration:

```shell
west build -b [sam4e_xpro | sam_v71_xult | frdm_k64f | nucleo_f767zi] samples/net/cloud/tagoio_http_post
west flash
```

### WIFI

To enable WIFI support, you need a board with an embedded WIFI support like
[ST Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/arm/disco_l475_iot1/doc/index.md#disco-l475-iot1-board) or you can add a shield like
[ESP-8266 Modules](../../../../boards/shields/esp_8266/doc/index.md#module-esp-8266) or [Inventek es-WIFI Shield](../../../../boards/shields/inventek_eswifi/doc/index.md#inventek-eswifi-shield). Additionally you
need fill `CONFIG_TAGOIO_HTTP_WIFI_SSID` with your wifi network SSID and
`CONFIG_TAGOIO_HTTP_WIFI_PSK` with the correspondent password at
[samples/net/cloud/tagoio\_http\_post/overlay-wifi.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/tagoio_http_post/overlay-wifi.conf) file.

```shell
west build -b disco_l475_iot1 samples/net/cloud/tagoio_http_post -- -DEXTRA_CONF_FILE=overlay-wifi.conf
west flash
```

```shell
west build -b [sam_v71_xult | frdm_k64f | nucleo_f767zi] samples/net/cloud/tagoio_http_post -- -DSHIELD=[esp_8266_arduino | inventek_eswifi_arduino_uart] -DEXTRA_CONF_FILE=overlay-wifi.conf
west flash
```

### Modem

The Modem support is quite similar to WIFI, you need a board with an embedded
Modem support or you can add a shield. Currently, the overlay was created to
allow modems with PPP support. This was tested using `SIMcom SIM808 EVB`.
Additionally you need fill `CONFIG_MODEM_GSM_APN` with the correspondent Access
Point Name (APN) at
[samples/net/cloud/tagoio\_http\_post/overlay-modem.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/tagoio_http_post/overlay-modem.conf) file. A
DTC overlay file should be used to configure the glue between the modem and the
uart port. It can reside at boards directory, with the board name, or it can be
a special designator like defined at `arduino.overlay`.

```shell
west build -b sam4e_xpro samples/net/cloud/tagoio_http_post -- -DEXTRA_CONF_FILE=overlay-modem.conf
west flash
```

```shell
west build -b frdm_k64f samples/net/cloud/tagoio_http_post -- -DEXTRA_CONF_FILE=overlay-modem.conf -DDTC_OVERLAY_FILE=arduino.overlay
west flash
```

In a terminal window you can check if communication is happen:

```shell
$ minicom -D /dev/ttyACM0

*** Booting Zephyr OS build zephyr-v2.4.0-1135-g137732e23c1e  ***

[00:00:02.172,000] <inf> modem_gsm: Manufacturer: SIMCOM_Lt
[00:00:02.227,000] <inf> modem_gsm: Model: SIMCOM_SIM808
[00:00:02.283,000] <inf> modem_gsm: Revision: 1418B04SIM808M32
[00:00:02.338,000] <inf> modem_gsm: IMSI: XXXXXX
[00:00:02.393,000] <inf> modem_gsm: ICCID: XXXXXX
[00:00:02.453,000] <inf> modem_gsm: IMEI: XXXXXX
[00:00:02.574,000] <inf> modem_gsm: Attached to packet service!
[00:00:02.575,000] <inf> net_ppp: Initializing PPP to use UART_3
[00:00:13.370,000] <inf> tagoio: TagoIO IoT - HTTP Client - Temperature demo
[00:00:13.370,000] <inf> tagoio: Temp: 20
[00:00:25.237,000] <inf> tagoio: Temp: 76
[00:00:37.581,000] <inf> tagoio: Temp: 36
[00:00:50.437,000] <inf> tagoio: Temp: 98
```

## Visualizing TagoIO dashboard

After you got some logs on console it is time to create a dashboard on the
TagoIO to visualize the data.

- Go to the TagoIO web console
- Create a dashboard as Normal, give it a denomination and move next
- Add a line plot graph. You will see your device, temperature variable will
  be automatically selected for you.
- Just Save and enjoy!

[![TagoIO web dashboard](../../../../_images/TagoIO-pc.jpeg)](../../../../_images/TagoIO-pc.jpeg)

You can experiment the TagoIO mobile application on your cellphone or tablet.
Simple go to your app store and search by TagoIO, install, sign in, enjoy!

[![TagoIO mobile dashboard](../../../../_images/TagoIO-mobile.jpeg)](../../../../_images/TagoIO-mobile.jpeg)

More information at [TagoIO](https://tago.io/) [[1]](#id1) and [TagoIO Documentation](https://docs.tago.io) [[2]](#id8).

## References

[1]
([1](#id2),[2](#id3),[3](#id4),[4](#id5),[5](#id6),[6](#id7))

[https://tago.io/](https://tago.io/)

[[2](#id9)]

[https://docs.tago.io](https://docs.tago.io)
