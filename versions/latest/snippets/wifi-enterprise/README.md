---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/snippets/wifi-enterprise/README.html
original_path: snippets/wifi-enterprise/README.html
---

# Wi-Fi Enterprise Snippet (wifi-enterprise)

```shell
west build  -S wifi-enterprise [...]
```

Can also be used along with the [Wi-Fi IPv4 Snippet (wifi-ipv4)](../wifi-ipv4/README.md#snippet-wifi-ipv4) snippet.

```shell
west build  -S "wifi-enterprise,wifi-ipv4" [...]
```

## Overview

This snippet enables enterprise Wi-Fi support in supported networking samples.

See [Wi-Fi Management](../../connectivity/networking/api/wifi.md#wifi-mgmt) for more information on the usage.

## Requirements

Hardware support for:

- [`CONFIG_WIFI`](../../kconfig.md#CONFIG_WIFI "CONFIG_WIFI")
- [`CONFIG_WIFI_USE_NATIVE_NETWORKING`](../../kconfig.md#CONFIG_WIFI_USE_NATIVE_NETWORKING "CONFIG_WIFI_USE_NATIVE_NETWORKING")
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT`](../../kconfig.md#CONFIG_WIFI_NM_WPA_SUPPLICANT "CONFIG_WIFI_NM_WPA_SUPPLICANT")
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](../../kconfig.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE "CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE")
