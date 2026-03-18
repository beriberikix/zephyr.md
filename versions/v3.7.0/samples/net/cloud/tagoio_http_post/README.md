---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/cloud/tagoio_http_post/README.html
original_path: samples/net/cloud/tagoio_http_post/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
are many like [SAM4E Xplained Pro](../../../../boards/atmel/sam/sam4e_xpro/doc/index.md#sam4e-xpro), [SAM V71(B) Xplained Ultra](../../../../boards/atmel/sam/sam_v71_xult/doc/index.md#sam-v71-xplained-ultra),
[NXP FRDM-K64F](../../../../boards/nxp/frdm_k64f/doc/index.md#frdm-k64f), [ST Nucleo F767ZI](../../../../boards/st/nucleo_f767zi/doc/index.md#nucleo-f767zi-board) etc. Pick one and just build
tagoio-http-client sample application with minimal configuration:

```shell
west build -b [sam4e_xpro | sam_v71_xult/samv71q21 | frdm_k64f | nucleo_f767zi] samples/net/cloud/tagoio_http_post
west flash
```

### WIFI

To enable WIFI support, you need a board with an embedded WIFI support like
[ST Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/st/disco_l475_iot1/doc/index.md#disco-l475-iot1-board) or you can add a shield like
[ESP-8266 Modules](../../../../boards/shields/esp_8266/doc/index.md#module-esp-8266) or [Inventek es-WIFI Shield](../../../../boards/shields/inventek_eswifi/doc/index.md#inventek-eswifi-shield). Additionally you
need fill `CONFIG_TAGOIO_HTTP_WIFI_SSID` with your wifi network SSID and
`CONFIG_TAGOIO_HTTP_WIFI_PSK` with the correspondent password at
[samples/net/cloud/tagoio\_http\_post/overlay-wifi.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/cloud/tagoio_http_post/overlay-wifi.conf) file.

```shell
west build -b disco_l475_iot1 samples/net/cloud/tagoio_http_post -- -DEXTRA_CONF_FILE=overlay-wifi.conf
west flash
```

```shell
west build -b [sam_v71_xult/samv71q21 | frdm_k64f | nucleo_f767zi] --shield [esp_8266_arduino | inventek_eswifi_arduino_uart] samples/net/cloud/tagoio_http_post -- -DEXTRA_CONF_FILE=overlay-wifi.conf
west flash
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
