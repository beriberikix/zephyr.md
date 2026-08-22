---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/connectivity/networking/api/wifi_credentials.html
original_path: connectivity/networking/api/wifi_credentials.html
---

# Wi-Fi credentials Library

The Wi-Fi credentials library provides means to load and store Wi-Fi® network credentials.

## [Overview](#id2)

This library uses either Zephyr’s settings subsystem or Platform Security Architecture (PSA) Internal Trusted Storage (ITS) to store credentials.
It also holds a list of SSIDs in RAM to provide dictionary-like access using SSIDs as keys.

## [Configuration](#id3)

To use the Wi-Fi credentials library, enable the [`CONFIG_WIFI_CREDENTIALS`](../../../kconfig.md#CONFIG_WIFI_CREDENTIALS "CONFIG_WIFI_CREDENTIALS") Kconfig option.

You can pick the backend using the following options:

- [`CONFIG_WIFI_CREDENTIALS_BACKEND_PSA`](../../../kconfig.md#CONFIG_WIFI_CREDENTIALS_BACKEND_PSA "CONFIG_WIFI_CREDENTIALS_BACKEND_PSA") - Default option for non-secure targets, which includes a TF-M partition (non-minimal TF-M profile type).
- [`CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS`](../../../kconfig.md#CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS "CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS") - Default option for secure targets.

To configure the maximum number of networks, use the [`CONFIG_WIFI_CREDENTIALS_MAX_ENTRIES`](../../../kconfig.md#CONFIG_WIFI_CREDENTIALS_MAX_ENTRIES "CONFIG_WIFI_CREDENTIALS_MAX_ENTRIES") Kconfig option.

The IEEE 802.11 standard does not specify the maximum length of SAE passwords.
To change the default, use the [`CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH`](../../../kconfig.md#CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH "CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH") Kconfig option.

## [Adding credentials](#id4)

You can add credentials using the [`wifi_credentials_set_personal()`](../../../doxygen/html/group__wifi__credentials.md#ga28b13d11cca692921252e98788552957) and [`wifi_credentials_set_personal_struct()`](../../../doxygen/html/group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055) functions.
The former will build the internally used struct from given fields, while the latter takes the struct directly.
If you add credentials with the same SSID twice, the older entry will be overwritten.

## [Querying credentials](#id5)

With an SSID, you can query credentials using the [`wifi_credentials_get_by_ssid_personal()`](../../../doxygen/html/group__wifi__credentials.md#ga548522fbc6b5fdcff4585c34f3565c82) and [`wifi_credentials_get_by_ssid_personal_struct()`](../../../doxygen/html/group__wifi__credentials.md#ga3d83001e713206ec07f94996137537d5) functions.

You can iterate over all stored credentials with the [`wifi_credentials_for_each_ssid()`](../../../doxygen/html/group__wifi__credentials.md#ga3a5b20d07afc52cc452a9c55998ebcf7) function.
Deleting or overwriting credentials while iterating is allowed, since these operations do not change internal indices.

## [Removing credentials](#id6)

You can remove credentials using the [`wifi_credentials_delete_by_ssid()`](../../../doxygen/html/group__wifi__credentials.md#ga644d29db8091512a977f8e27b245975e) function.

## [Shell commands](#id7)

`wifi cred` is an extension to the Wi-Fi command line.
It adds the following subcommands to interact with the Wi-Fi credentials library:

Wi-Fi credentials shell subcommands

| Subcommands | Description |
| --- | --- |
| add | Add a network to the credentials storage with following parameters:  <-s –ssid "<SSID>">: SSID.  [-c –channel]: Channel that needs to be scanned for connection. 0:any channel  [-b, –band] 0: any band (2:2.4GHz, 5:5GHz, 6:6GHz)  [-p, –passphrase]: Passphrase (valid only for secure SSIDs)  [-k, –key-mgmt]: Key management type.  0:None, 1:WPA2-PSK, 2:WPA2-PSK-256, 3:SAE-HNP, 4:SAE-H2E, 5:SAE-AUTO, 6:WAPI,”  “ 7:EAP-TLS, 8:WEP, 9: WPA-PSK, 10: WPA-Auto-Personal, 11: DPP  [-w, –ieee-80211w]: MFP (optional: needs security type to be specified)  : 0:Disable, 1:Optional, 2:Required.  [-m, –bssid]: MAC address of the AP (BSSID).  [-t, –timeout]: Duration after which connection attempt needs to fail.  [-a, –identity]: Identity for enterprise mode.  [-K, –key-passwd]: Private key passwd for enterprise mode.  [-h, –help]: Print out the help for the connect command. |
| delete <SSID> | Removes network from credentials storage. |
| list | Lists networks in credential storage. |
| auto\_connect | Automatically connects to any stored network. |

## [Limitations](#id8)

The library has the following limitations:

- Although permitted by the IEEE 802.11 standard, this library does not support zero-length SSIDs.
- Wi-Fi Protected Access (WPA) Enterprise credentials are only partially supported.
- The number of networks stored is fixed compile time.

## [API documentation](#id9)

The following section provides an overview and reference for the Wi-Fi credentials API available in Zephyr:

[Wi-Fi credentials library](../../../doxygen/html/group__wifi__credentials.md)
