---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/dis-pics.html
original_path: connectivity/bluetooth/dis-pics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DIS ICS

PTS version: 8.0.3

M - mandatory

O - optional

## Service Version

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_DIS\_0\_1 | True | Device Information Service v1.1 (M) |

## Transport Requirements

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_DIS\_1\_1 | False | Service supported over BR/EDR (C.1) |
| TSPC\_DIS\_1\_2 | True | Service supported over LE (C.1) |
| TSPC\_DIS\_1\_3 | False | Service supported over HS (C.1) |

## Service Requirements

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_DIS\_2\_1 | True | Device Information Service (M) |
| TSPC\_DIS\_2\_2 | True | Manufacturer Name String Characteristic (O) |
| TSPC\_DIS\_2\_3 | True | Model Number String Characteristic (O) |
| TSPC\_DIS\_2\_4 | True | Serial Number String Characteristic (O) |
| TSPC\_DIS\_2\_5 | True | Hardware Revision String Characteristic (O) |
| TSPC\_DIS\_2\_6 | True | Firmware Revision String Characteristic (O) |
| TSPC\_DIS\_2\_7 | True | Software Revision String Characteristic (O) |
| TSPC\_DIS\_2\_8 | False | System ID Characteristic (O) |
| TSPC\_DIS\_2\_9 | False | IEEE 11073-20601 Regulatory Certification Data List Characteristic (O) |
| TSPC\_DIS\_2\_10 | False | SDP Interoperability (C.1) |
| TSPC\_DIS\_2\_11 | True | PnP ID (O) |
