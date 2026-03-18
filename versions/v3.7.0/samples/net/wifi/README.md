---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/wifi/README.html
original_path: samples/net/wifi/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Wi-Fi shell

## Overview

This sample allows testing Wi-Fi drivers for various boards by
enabling the Wi-Fi shell module that provides a set of commands:
scan, connect, and disconnect. It also enables the net\_shell module
to verify net\_if settings.

## Building and Running

Verify the board and chip you are targeting provide Wi-Fi support.

For instance you can use TI’s CC3220 by selecting the cc3220sf\_launchxl board.

```shell
west build -b cc3220sf_launchxl samples/net/wifi
```

### Sample console interaction

```shell
shell> wifi scan
Scan requested
shell>
Num  | SSID                             (len) | Chan | RSSI | Sec
1    | kapoueh!                         8     | 1    | -93  | WPA/WPA2
2    | mooooooh                         8     | 6    | -89  | WPA/WPA2
3    | Ap-foo blob..                    13    | 11   | -73  | WPA/WPA2
4    | gksu                             4     | 1    | -26  | WPA/WPA2
----------
Scan request done

shell> wifi connect "gksu" 4 SecretStuff
Connection requested
shell>
Connected
shell>
```
