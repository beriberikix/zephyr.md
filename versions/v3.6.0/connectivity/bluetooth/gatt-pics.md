---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/gatt-pics.html
original_path: connectivity/bluetooth/gatt-pics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# GATT ICS

PTS version: 8.0.3

M - mandatory

O - optional

## Generic Attribute Profile Support

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_1\_1 | True | Generic Attribute Profile (GATT) Client (C.1) |
| TSPC\_GATT\_1\_2 | True | Generic Attribute Profile (GATT) Server (C.2) |

## GATT role configuration

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_1a\_1 | True | GATT Client over LE (C.1) |
| TSPC\_GATT\_1a\_2 | False | GATT Client over BR/EDR (C.2) |
| TSPC\_GATT\_1a\_3 | True | GATT Server over LE (C.3) |
| TSPC\_GATT\_1a\_4 | False | GATT Server over BR/EDR (C.4) |

## Attribute Protocol Transport

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_2\_1 | False | Attribute Protocol Supported over BR/EDR (L2CAP fixed channel support) (C.1) |
| TSPC\_GATT\_2\_2 | True | Attribute Protocol Supported over LE (C.2) |
| TSPC\_GATT\_2\_3 | True | Enhanced ATT bearer Attribute Protocol Supported (L2CAP fixed EATT PSM supported) (C.3) |
| TSPC\_GATT\_2\_3a | True | Enhanced ATT bearer supported over LE (C.4) |
| TSPC\_GATT\_2\_3b | False | Enhanced ATT bearer supported over BR/EDR (C.5) |

## Generic Attribute Profile Feature Support, by Client

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_3\_1 | True | Exchange MTU (C.11) |
| TSPC\_GATT\_3\_2 | True | Discover All Primary Services (O) |
| TSPC\_GATT\_3\_3 | True | Discover Primary Services by Service UUID (O) |
| TSPC\_GATT\_3\_4 | True | Find Included Services (O) |
| TSPC\_GATT\_3\_5 | True | Discover All characteristics of a Service (O) |
| TSPC\_GATT\_3\_6 | True | Discover Characteristics by UUID (O) |
| TSPC\_GATT\_3\_7 | True | Discover All Characteristic Descriptors (O) |
| TSPC\_GATT\_3\_8 | True | Read Characteristic Value (O) |
| TSPC\_GATT\_3\_9 | True | Read Using Characteristic UUID (O) |
| TSPC\_GATT\_3\_10 | True | Read Long Characteristic Values (O) |
| TSPC\_GATT\_3\_11 | True | Read Multiple Characteristic Values (O) |
| TSPC\_GATT\_3\_12 | True | Write without Response (O) |
| TSPC\_GATT\_3\_13 | True | Signed Write Without Response (C.11) |
| TSPC\_GATT\_3\_14 | True | Write Characteristic Value (O) |
| TSPC\_GATT\_3\_15 | True | Write Long Characteristic Values (O) |
| TSPC\_GATT\_3\_16 | True | Characteristic Value Reliable Writes (O) |
| TSPC\_GATT\_3\_17 | True | Notifications (C.7) |
| TSPC\_GATT\_3\_18 | True | Indications (M) |
| TSPC\_GATT\_3\_19 | True | Read Characteristic Descriptors (O) |
| TSPC\_GATT\_3\_20 | True | Read Long Characteristic Descriptors (O) |
| TSPC\_GATT\_3\_21 | True | Write Characteristic Descriptors (O) |
| TSPC\_GATT\_3\_22 | True | Write Long Characteristic Descriptors (O) |
| TSPC\_GATT\_3\_23 | True | Service Changed Characteristic (M) |
| TSPC\_GATT\_3\_24 | False | Configured Broadcast (C.2) |
| TSPC\_GATT\_3\_25 | True | Client Supported Features Characteristic (C.4) |
| TSPC\_GATT\_3\_26 | True | Database Hash Characteristic (C.4) |
| TSPC\_GATT\_3\_27 | False | Read and Interpret Characteristic Presentation Format (O) |
| TSPC\_GATT\_3\_28 | False | Read and Interpret Characteristic Aggregate Format (C.6) |
| TSPC\_GATT\_3\_29 | False | Read Multiple Variable Length Characteristic Values (C.9) |
| TSPC\_GATT\_3\_30 | False | Multiple Variable Length Notifications (C.10) |

## Generic Attribute Profile Feature Support, by Server

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_4\_1 | True | Exchange MTU (C.6) |
| TSPC\_GATT\_4\_2 | True | Discover All Primary Services (M) |
| TSPC\_GATT\_4\_3 | True | Discover Primary Services by Service UUID (M) |
| TSPC\_GATT\_4\_4 | True | Find Included Services (M) |
| TSPC\_GATT\_4\_5 | True | Discover All characteristics of a Service (M) |
| TSPC\_GATT\_4\_6 | True | Discover Characteristics by UUID (M) |
| TSPC\_GATT\_4\_7 | True | Discover All Characteristic Descriptors (M) |
| TSPC\_GATT\_4\_8 | True | Read Characteristic Value (M) |
| TSPC\_GATT\_4\_9 | True | Read Using Characteristic UUID (M) |
| TSPC\_GATT\_4\_10 | True | Read Long Characteristic Values (C.12) |
| TSPC\_GATT\_4\_11 | True | Read Multiple Characteristic Values (O) |
| TSPC\_GATT\_4\_12 | True | Write without Response (C.2) |
| TSPC\_GATT\_4\_13 | True | Signed Write Without Response (C.6) |
| TSPC\_GATT\_4\_14 | True | Write Characteristic Value (C.3) |
| TSPC\_GATT\_4\_15 | True | Write Long Characteristic Values (C.12) |
| TSPC\_GATT\_4\_16 | True | Characteristic Value ReliableWrites (O) |
| TSPC\_GATT\_4\_17 | True | Notifications (O) |
| TSPC\_GATT\_4\_18 | True | Indications (C.1) |
| TSPC\_GATT\_4\_19 | True | Read Characteristic Descriptors (C.12) |
| TSPC\_GATT\_4\_20 | True | Read Long Characteristic Descriptors (C.12) |
| TSPC\_GATT\_4\_21 | True | Write Characteristic Descriptors (C.12) |
| TSPC\_GATT\_4\_22 | True | Write Long Characteristic Descriptors (O) |
| TSPC\_GATT\_4\_23 | True | Service Changed Characteristic (C.1) |
| TSPC\_GATT\_4\_24 | False | Configured Broadcast (C.5) |
| TSPC\_GATT\_4\_25 | False | Execute Write Request with empty queue (C.7) |
| TSPC\_GATT\_4\_26 | True | Client Supported Features Characteristic (C.9) |
| TSPC\_GATT\_4\_27 | True | Database Hash Characteristic (C.8) |
| TSPC\_GATT\_4\_28 | False | Report Characteristic Value: Characteristic Presentation Format (O) |
| TSPC\_GATT\_4\_29 | False | Report aggregate Characteristic Value: Characteristic Aggregate Format (C.10) |
| TSPC\_GATT\_4\_30 | False | Read Multiple Variable Length Characteristic Values (C.13) |
| TSPC\_GATT\_4\_31 | False | Multiple Variable Length Notifications (C.13) |

## SDP Interoperability

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_6\_2 | False | Discover GATT Services using Service Discovery Profile (C.1) |
| TSPC\_GATT\_6\_3 | False | Publish SDP record for GATT services support via BR/EDR (C.2) |

## Attribute Protocol Transport Security

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_7\_1 | False | Security Mode 4 (C.1) |
| TSPC\_GATT\_7\_2 | True | LE Security Mode 1 (C.5) |
| TSPC\_GATT\_7\_3 | True | LE Security Mode 2 (C.6) |
| TSPC\_GATT\_7\_4 | True | LE Authentication Procedure (C.4) |
| TSPC\_GATT\_7\_5 | True | LE connection data signing procedure (C.2) |
| TSPC\_GATT\_7\_6 | True | LE Authenticate signed data procedure (C.2) |
| TSPC\_GATT\_7\_7 | True | LE Authorization Procedure (C.3) |

## Multiple Simultaneous ATT Bearers

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GATT\_8\_1 | False | Support for multiple simultaneous active ATT bearers from same device – ATT over LE and ATT over BR/EDR (C.1) |
| TSPC\_GATT\_8\_2 | True | Support for multiple simultaneous active ATT bearers from same device – ATT over LE and EATT over LE (C.2) |
| TSPC\_GATT\_8\_3 | False | Support for multiple simultaneous active ATT bearers from same device – ATT over BR/EDR and EATT over BR/EDR (C.3) |
| TSPC\_GATT\_8\_4 | False | Support for multiple simultaneous active ATT bearers from same device – ATT over LE and EATT over BR/EDR (C.4) |
| TSPC\_GATT\_8\_5 | False | Support for multiple simultaneous active ATT bearers from same device – ATT over BR/EDR and EATT over LE (C.5) |
| TSPC\_GATT\_8\_6 | False | Support for multiple simultaneous active EATT bearers from same device – EATT over BR/EDR and EATT over LE (C.6) |
| TSPC\_GATT\_8\_7 | False | Support for multiple simultaneous active EATT bearers from same device – EATT over BR/EDR (C.7) |
| TSPC\_GATT\_8\_8 | True | Support for multiple simultaneous active EATT bearers from same device – EATT over LE (C.7) |
