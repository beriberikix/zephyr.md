---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__scan__params.html
original_path: doxygen/html/structwifi__scan__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_scan\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi scan parameters structure.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) | [scan\_type](#a645acc54603cd4692527c1a028933078) |
|  | Scan type, see enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea "Wi-Fi scanning types."). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bands](#a6b571d960ed9d7419e31530e5fb6f97a) |
|  | Bitmap of bands to be scanned. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dwell\_time\_active](#a2453a75c23e04e3572559c0e7199c1b4) |
|  | Active scan dwell time (in ms) on a channel. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dwell\_time\_passive](#a8e7a37ccda8de635e7b7066d7943e814) |
|  | Passive scan dwell time (in ms) on a channel. |
| const char \* | [ssids](#aac11ee8e0ec8a4fa24668f4820bd1a12) [WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX] |
|  | Array of SSID strings to scan. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_bss\_cnt](#a12d5dea7d8fa8ad03ac2366720c46243) |
|  | Specifies the maximum number of scan results to return. |
| struct [wifi\_band\_channel](structwifi__band__channel.md) | [band\_chan](#aa5ddbd6bc97b7598288d4b0d38521681) [WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL] |
|  | Channel information array indexed on Wi-Fi frequency bands and channels within that band. |

## Detailed Description

Wi-Fi scan parameters structure.

Used to specify parameters which can control how the Wi-Fi scan is performed.

## Field Documentation

## [◆ ](#aa5ddbd6bc97b7598288d4b0d38521681)band\_chan

| struct [wifi\_band\_channel](structwifi__band__channel.md) wifi\_scan\_params::band\_chan[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL] |
| --- |

Channel information array indexed on Wi-Fi frequency bands and channels within that band.

E.g. to scan channel 6 and 11 on the 2.4 GHz band, channel 36 on the 5 GHz band:

chan[0] = {[WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11), 6};

chan[1] = {[WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11), 11};

chan[2] = {[WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895), 36};

[WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)

@ WIFI\_FREQ\_BAND\_2\_4\_GHZ

2.4 GHz band.

**Definition** wifi.h:209

[WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)

@ WIFI\_FREQ\_BAND\_5\_GHZ

5 GHz band.

**Definition** wifi.h:211

This list specifies the channels to be **considered for scan**. The underlying Wi-Fi chip can silently omit some channels due to various reasons such as channels not conforming to regulatory restrictions etc. The invoker of the API should ensure that the channels specified follow regulatory rules.

## [◆ ](#a6b571d960ed9d7419e31530e5fb6f97a)bands

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_scan\_params::bands |
| --- |

Bitmap of bands to be scanned.

Refer to [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d "IEEE 802.11 operational frequency bands (not exhaustive).") for bit position of each band.

## [◆ ](#a2453a75c23e04e3572559c0e7199c1b4)dwell\_time\_active

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_scan\_params::dwell\_time\_active |
| --- |

Active scan dwell time (in ms) on a channel.

## [◆ ](#a8e7a37ccda8de635e7b7066d7943e814)dwell\_time\_passive

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_scan\_params::dwell\_time\_passive |
| --- |

Passive scan dwell time (in ms) on a channel.

## [◆ ](#a12d5dea7d8fa8ad03ac2366720c46243)max\_bss\_cnt

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_scan\_params::max\_bss\_cnt |
| --- |

Specifies the maximum number of scan results to return.

These results would be the BSSIDS with the best RSSI values, in all the scanned channels. This should only be used to limit the number of returned scan results, and cannot be counted upon to limit the scan time, since the underlying Wi-Fi chip might have to scan all the channels to find the max\_bss\_cnt number of APs with the best signal strengths. A value of 0 signifies that there is no restriction on the number of scan results to be returned.

## [◆ ](#a645acc54603cd4692527c1a028933078)scan\_type

| enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) wifi\_scan\_params::scan\_type |
| --- |

Scan type, see enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea "Wi-Fi scanning types.").

The scan\_type is only a hint to the underlying Wi-Fi chip for the preferred mode of scan. The actual mode of scan can depend on factors such as the Wi-Fi chip implementation support, regulatory domain restrictions etc.

## [◆ ](#aac11ee8e0ec8a4fa24668f4820bd1a12)ssids

| const char\* wifi\_scan\_params::ssids[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX] |
| --- |

Array of SSID strings to scan.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_scan\_params](structwifi__scan__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
