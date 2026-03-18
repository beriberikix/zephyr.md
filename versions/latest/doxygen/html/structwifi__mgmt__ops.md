---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structwifi__mgmt__ops.html
original_path: doxygen/html/structwifi__mgmt__ops.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_mgmt\_ops Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi management API.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [scan](#a267030c27da3cdc251badd0ed7f7b1cb) )(const struct [device](structdevice.md) \*dev, struct [wifi\_scan\_params](structwifi__scan__params.md) \*params, [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8) cb) |
|  | Scan for Wi-Fi networks. |
| int(\* | [connect](#ae6255ea77739918797b4f3c7a4634a75) )(const struct [device](structdevice.md) \*dev, struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params) |
|  | Connect to a Wi-Fi network. |
| int(\* | [disconnect](#a5725c6fd93ae189a3019374cd4ad2ff4) )(const struct [device](structdevice.md) \*dev) |
|  | Disconnect from a Wi-Fi network. |
| int(\* | [ap\_enable](#ac2ce3a4a86c43e30d33261f71c44198a) )(const struct [device](structdevice.md) \*dev, struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params) |
|  | Enable AP mode. |
| int(\* | [ap\_disable](#a5aa7a2be82eb1783872abda2b8978235) )(const struct [device](structdevice.md) \*dev) |
|  | Disable AP mode. |
| int(\* | [ap\_sta\_disconnect](#af01aaec29be78c02314acf13b5c1b6f7) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac) |
|  | Disconnect a STA from AP. |
| int(\* | [iface\_status](#adf157476d776bc9c068e99e1a0266fd3) )(const struct [device](structdevice.md) \*dev, struct [wifi\_iface\_status](structwifi__iface__status.md) \*status) |
|  | Get interface status. |
| int(\* | [get\_stats](#a5e6fdf836273fcde54efff4c77bfdf0e) )(const struct [device](structdevice.md) \*dev, struct [net\_stats\_wifi](structnet__stats__wifi.md) \*stats) |
|  | Get Wi-Fi statistics. |
| int(\* | [set\_power\_save](#ac0f3f7fa699b1bc7db2358e77dd44cc4) )(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_params](structwifi__ps__params.md) \*params) |
|  | Set power save status. |
| int(\* | [set\_twt](#ab4500534b6abe0449290c8bd8f729fc4) )(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params) |
|  | Setup or teardown TWT flow. |
| int(\* | [get\_power\_save\_config](#a52690b13f8a1e7b0c2302eaa24ae4c7f) )(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_config](structwifi__ps__config.md) \*config) |
|  | Get power save config. |
| int(\* | [reg\_domain](#a0a287c8acf2d7bf9333b755589294881) )(const struct [device](structdevice.md) \*dev, struct [wifi\_reg\_domain](structwifi__reg__domain.md) \*reg\_domain) |
|  | Set or get regulatory domain. |
| int(\* | [filter](#ad645276745ce8dd9685e0744efdfc733) )(const struct [device](structdevice.md) \*dev, struct [wifi\_filter\_info](structwifi__filter__info.md) \*filter) |
|  | Set or get packet filter settings for monitor and promiscuous modes. |
| int(\* | [mode](#ae2fb1bc35bf9255655a30a2ad8588b7c) )(const struct [device](structdevice.md) \*dev, struct [wifi\_mode\_info](structwifi__mode__info.md) \*mode) |
|  | Set or get mode of operation. |
| int(\* | [channel](#af17ddfea01d0ab478f6fd50b1c9d6015) )(const struct [device](structdevice.md) \*dev, struct [wifi\_channel\_info](structwifi__channel__info.md) \*channel) |
|  | Set or get current channel of operation. |
| int(\* | [get\_version](#aa7e4bc3dbc960091d11ffe5454259885) )(const struct [device](structdevice.md) \*dev, struct [wifi\_version](structwifi__version.md) \*params) |
|  | Get Version of WiFi driver and Firmware. |

## Detailed Description

Wi-Fi management API.

## Field Documentation

## [◆ ](#a5aa7a2be82eb1783872abda2b8978235)ap\_disable

| int(\* wifi\_mgmt\_ops::ap\_disable) (const struct [device](structdevice.md) \*dev) |
| --- |

Disable AP mode.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ac2ce3a4a86c43e30d33261f71c44198a)ap\_enable

| int(\* wifi\_mgmt\_ops::ap\_enable) (const struct [device](structdevice.md) \*dev, struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params) |
| --- |

Enable AP mode.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | params | AP mode parameters |

Returns
:   0 if ok, < 0 if error

## [◆ ](#af01aaec29be78c02314acf13b5c1b6f7)ap\_sta\_disconnect

| int(\* wifi\_mgmt\_ops::ap\_sta\_disconnect) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac) |
| --- |

Disconnect a STA from AP.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mac | MAC address of the STA to disconnect |

Returns
:   0 if ok, < 0 if error

## [◆ ](#af17ddfea01d0ab478f6fd50b1c9d6015)channel

| int(\* wifi\_mgmt\_ops::channel) (const struct [device](structdevice.md) \*dev, struct [wifi\_channel\_info](structwifi__channel__info.md) \*channel) |
| --- |

Set or get current channel of operation.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | [channel](#af17ddfea01d0ab478f6fd50b1c9d6015) | settings |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ae6255ea77739918797b4f3c7a4634a75)connect

| int(\* wifi\_mgmt\_ops::connect) (const struct [device](structdevice.md) \*dev, struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params) |
| --- |

Connect to a Wi-Fi network.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | params | Connect parameters |

Returns
:   0 if ok, < 0 if error

## [◆ ](#a5725c6fd93ae189a3019374cd4ad2ff4)disconnect

| int(\* wifi\_mgmt\_ops::disconnect) (const struct [device](structdevice.md) \*dev) |
| --- |

Disconnect from a Wi-Fi network.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ad645276745ce8dd9685e0744efdfc733)filter

| int(\* wifi\_mgmt\_ops::filter) (const struct [device](structdevice.md) \*dev, struct [wifi\_filter\_info](structwifi__filter__info.md) \*filter) |
| --- |

Set or get packet filter settings for monitor and promiscuous modes.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | packet | filter settings |

Returns
:   0 if ok, < 0 if error

## [◆ ](#a52690b13f8a1e7b0c2302eaa24ae4c7f)get\_power\_save\_config

| int(\* wifi\_mgmt\_ops::get\_power\_save\_config) (const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_config](structwifi__ps__config.md) \*config) |
| --- |

Get power save config.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | config | Power save config |

Returns
:   0 if ok, < 0 if error

## [◆ ](#a5e6fdf836273fcde54efff4c77bfdf0e)get\_stats

| int(\* wifi\_mgmt\_ops::get\_stats) (const struct [device](structdevice.md) \*dev, struct [net\_stats\_wifi](structnet__stats__wifi.md) \*stats) |
| --- |

Get Wi-Fi statistics.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | stats | Wi-Fi statistics |

Returns
:   0 if ok, < 0 if error

## [◆ ](#aa7e4bc3dbc960091d11ffe5454259885)get\_version

| int(\* wifi\_mgmt\_ops::get\_version) (const struct [device](structdevice.md) \*dev, struct [wifi\_version](structwifi__version.md) \*params) |
| --- |

Get Version of WiFi driver and Firmware.

The driver that implements the get\_version function must not use stack to allocate the version information pointers that are returned as params struct members. The version pointer parameters should point to a static memory either in ROM (preferred) or in RAM.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | params | Version parameters |

Returns
:   0 if ok, < 0 if error

## [◆ ](#adf157476d776bc9c068e99e1a0266fd3)iface\_status

| int(\* wifi\_mgmt\_ops::iface\_status) (const struct [device](structdevice.md) \*dev, struct [wifi\_iface\_status](structwifi__iface__status.md) \*status) |
| --- |

Get interface status.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | status | Interface status |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ae2fb1bc35bf9255655a30a2ad8588b7c)mode

| int(\* wifi\_mgmt\_ops::mode) (const struct [device](structdevice.md) \*dev, struct [wifi\_mode\_info](structwifi__mode__info.md) \*mode) |
| --- |

Set or get mode of operation.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | [mode](#ae2fb1bc35bf9255655a30a2ad8588b7c) | settings |

Returns
:   0 if ok, < 0 if error

## [◆ ](#a0a287c8acf2d7bf9333b755589294881)reg\_domain

| int(\* wifi\_mgmt\_ops::reg\_domain) (const struct [device](structdevice.md) \*dev, struct [wifi\_reg\_domain](structwifi__reg__domain.md) \*reg\_domain) |
| --- |

Set or get regulatory domain.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | [reg\_domain](#a0a287c8acf2d7bf9333b755589294881) | Regulatory domain |

Returns
:   0 if ok, < 0 if error

## [◆ ](#a267030c27da3cdc251badd0ed7f7b1cb)scan

| int(\* wifi\_mgmt\_ops::scan) (const struct [device](structdevice.md) \*dev, struct [wifi\_scan\_params](structwifi__scan__params.md) \*params, [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8) cb) |
| --- |

Scan for Wi-Fi networks.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | params | Scan parameters |
    | cb | Callback to be called for each result cb parameter is the cb that should be called for each result by the driver. The wifi mgmt part will take care of raising the necessary event etc. |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ac0f3f7fa699b1bc7db2358e77dd44cc4)set\_power\_save

| int(\* wifi\_mgmt\_ops::set\_power\_save) (const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_params](structwifi__ps__params.md) \*params) |
| --- |

Set power save status.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | params | Power save parameters |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ab4500534b6abe0449290c8bd8f729fc4)set\_twt

| int(\* wifi\_mgmt\_ops::set\_twt) (const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params) |
| --- |

Setup or teardown TWT flow.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | params | TWT parameters |

Returns
:   0 if ok, < 0 if error

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_mgmt\_ops](structwifi__mgmt__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
