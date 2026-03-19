---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/snippets/wifi-ipv4/README.html
original_path: snippets/wifi-ipv4/README.html
---

# Wi-Fi IPv4 Snippet (wifi-ipv4)

```shell
west build -S wifi-ipv4 [...]
```

## Overview

This snippet enables IPv4 Wi-Fi support in supported networking samples.
The sample execution is postponed until Wi-Fi connectivity is established.

Use Wi-Fi shell to connect to the Wi-Fi network:

```shell
wifi connect -s <SSID> -k <key_management> -p <passphrase>
```

## Requirements

Hardware support for:

- [`CONFIG_WIFI`](../../kconfig.md#CONFIG_WIFI "CONFIG_WIFI")
- [`CONFIG_WIFI_USE_NATIVE_NETWORKING`](../../kconfig.md#CONFIG_WIFI_USE_NATIVE_NETWORKING "CONFIG_WIFI_USE_NATIVE_NETWORKING")
