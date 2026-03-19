---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/wifi/shell/README.html
original_path: samples/net/wifi/shell/README.html
---

# Wi-Fi shell

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/wifi/shell/README.rst/..)

## Overview

This sample allows testing Wi-Fi drivers for various boards by
enabling the Wi-Fi shell module that provides a set of commands:
scan, connect, and disconnect. It also enables the net\_shell module
to verify net\_if settings.

## Building and Running

Verify the board and chip you are targeting provide Wi-Fi support.

For instance you can use Nordic’s nrf7002dk by selecting the nrf7002dk/nrf5340/cpuapp board.

```shell
west build -b nrf7002dk/nrf5340/cpuapp samples/net/wifi/shell
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

## See also

[Network Statistics Library](../../../../doxygen/html/group__net__stats.md)
