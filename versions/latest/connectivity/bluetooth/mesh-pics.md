---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/mesh-pics.html
original_path: connectivity/bluetooth/mesh-pics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MESH ICS

PTS version: 8.0.3

M - mandatory

O - optional

## Major Profile Version (X.Y)

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_0\_1 | True | Mesh v1.0 (M) |

## Minor Profile Version (X.Y.Z)

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_0a\_1 | True | Erratum 10395 (C.1) |
| TSPC\_MESH\_0a\_2 | True | Mesh v1.0.1 (C.2) |
| TSPC\_MESH\_0a\_3 | True | Erratum 16350 (C.1) |

## Roles

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_2\_1 | True | Node (C.1) |
| TSPC\_MESH\_2\_2 | False | Provisioner (C.1) |

## Node Capabilities - Bearers

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_3\_1 | True | Advertising Bearer (C.1) |
| TSPC\_MESH\_3\_2 | True | GATT Bearer (C.1) |

## Node Capabilities - Provisioning

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_4\_1 | True | PB-ADV (C.1) |
| TSPC\_MESH\_4\_2 | True | PB-GATT (C.2) |
| TSPC\_MESH\_4\_3 | True | Device UUID (C.3) |
| TSPC\_MESH\_4\_4 | True | Sending Unprovisioned Device Beacon (C.4) |
| TSPC\_MESH\_4\_5 | True | Generic Provisioning Layer (C.3) |
| TSPC\_MESH\_4\_6 | True | Provisioning Protocol (Provisioning Server) (C.3) |
| TSPC\_MESH\_4\_7 | False | Provisioning: Public Key OOB (C.5) |
| TSPC\_MESH\_4\_8 | True | Provisioning: Public Key No OOB (C.5) |
| TSPC\_MESH\_4\_9 | True | Provisioning: Authentication Output OOB (C.6) |
| TSPC\_MESH\_4\_10 | False | Provisioning: Authentication Input OOB (C.6) |
| TSPC\_MESH\_4\_11 | False | Provisioning: Authentication Static OOB (C.6) |
| TSPC\_MESH\_4\_12 | True | Provisioning: Authentication No OOB (C.3) |

## Node Capabilities – Network Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_5\_1 | True | Transmitting and Receiving Secured Network Layer Messages (M) |
| TSPC\_MESH\_5\_2 | True | Relay Feature (C.1) |
| TSPC\_MESH\_5\_3 | True | Network Message Cache (C.2) |
| TSPC\_MESH\_5\_4 | False | Multiple Subnet Support (O) |

## Node Capabilities – Lower Transport Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_6\_1 | True | Transmitting and Receiving a Lower Transport PDU (M) |
| TSPC\_MESH\_6\_2 | True | Segmentation and Reassembly Behavior (M) |
| TSPC\_MESH\_6\_3 | True | Friend Cache (C.1) |

## Node Capabilities – Upper Transport Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_7\_1 | True | Transmitting a Secured Access Payload (M) |
| TSPC\_MESH\_7\_2 | True | Receiving a Secured Upper Transport PDU (M) |
| TSPC\_MESH\_7\_3 | True | Friend Feature (C.1) |
| TSPC\_MESH\_7\_4 | True | Low Power Feature (C.1) |
| TSPC\_MESH\_7\_5 | True | Heartbeat (M) |

## Node Capabilities – Access Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_8\_1 | True | Transmitting and Receiving an Access Layer Message (M) |

## Node Capabilities – Security

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_9\_1 | True | Message Replay Protection (M) |

## Node Capabilities – Mesh Management

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_10\_1 | True | Secure Network Beacon (M) |
| TSPC\_MESH\_10\_2 | True | Key Refresh Procedure (M) |
| TSPC\_MESH\_10\_3 | True | IV Update Procedure (M) |
| TSPC\_MESH\_10\_4 | True | IV Index Recovery Procedure (M) |

## Node Capabilities – Foundation Mesh Models

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_11\_1 | True | Configuration Server Model (M) |
| TSPC\_MESH\_11\_2 | True | Health Server Model (M) |
| TSPC\_MESH\_11\_3 | False | Configuration Client Model (O) |
| TSPC\_MESH\_11\_4 | False | Health Client Model (O) |

## Node Capabilities – Proxy

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_12\_1 | True | Proxy Server (C.1) |
| TSPC\_MESH\_12\_2 | True | GATT Server (C.2) |
| TSPC\_MESH\_12\_3 | True | Advertising with Network ID (C.2) |
| TSPC\_MESH\_12\_4 | True | Advertising with Node Identity (C.2) |
| TSPC\_MESH\_12\_5 | False | Proxy Client (C.3) |
| TSPC\_MESH\_12\_6 | False | GATT Client (C.4) |

## Mesh GATT Services

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_13\_1 | True | Mesh Provisioning Service (C.1) |
| TSPC\_MESH\_13\_2 | True | Mesh Proxy Service (C.2) |

## GATT Server Requirements

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_14\_1 | True | Discover All Primary Services (M) |
| TSPC\_MESH\_14\_2 | True | Discover Primary Services by Service UUID (M) |
| TSPC\_MESH\_14\_3 | True | Write without Response (M) |
| TSPC\_MESH\_14\_4 | True | Notifications (M) |
| TSPC\_MESH\_14\_5 | True | Write Characteristic Descriptors (M) |

## GATT Client Requirements

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_15\_1 | False | Discover All Primary Services (C.1) |
| TSPC\_MESH\_15\_2 | False | Discover Primary Services by Service UUID (C.1) |
| TSPC\_MESH\_15\_3 | False | Write without Response (M) |
| TSPC\_MESH\_15\_4 | False | Notifications (M) |
| TSPC\_MESH\_15\_5 | False | Write Characteristic Descriptors (M) |

## GAP Requirements

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_16\_1 | True | Broadcaster (C.1) |
| TSPC\_MESH\_16\_2 | True | Observer (C.1) |
| TSPC\_MESH\_16\_3 | True | Peripheral (C.2) |
| TSPC\_MESH\_16\_4 | True | Peripheral – Security Mode 1 (C.2) |
| TSPC\_MESH\_16\_5 | False | Central (C.3) |
| TSPC\_MESH\_16\_6 | False | Central – Security Mode 1 (C.3) |

## Provisioner – Bearers

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_17\_1 | False | Advertising Bearer (C.1) |
| TSPC\_MESH\_17\_2 | False | GATT Bearer (C.1) |

## Provisioner – Provisioning

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_18\_1 | False | Receiving Unprovisioned Device Beacon (C.1) |
| TSPC\_MESH\_18\_2 | False | PB-ADV (C.1) |
| TSPC\_MESH\_18\_3 | False | Generic Provisioning Layer (M) |
| TSPC\_MESH\_18\_4 | False | Provisioning Protocol (Provisioning Client) (M) |
| TSPC\_MESH\_18\_5 | False | PB-GATT (C.2) |
| TSPC\_MESH\_18\_6 | False | GATT Client (C.2) |
| TSPC\_MESH\_18\_7 | False | Provisioning: Public Key OOB (M) |
| TSPC\_MESH\_18\_8 | False | Provisioning: Public Key No OOB (M) |
| TSPC\_MESH\_18\_9 | False | Provisioning: Authentication Output OOB (M) |
| TSPC\_MESH\_18\_10 | False | Provisioning: Authentication Input OOB (M) |
| TSPC\_MESH\_18\_11 | False | Provisioning: Authentication Static or No OOB (M) |

## Provisioner – Mesh Management

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_19\_1 | False | Receiving Secure Network Beacon (M) |

## GATT Client Requirements

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_20\_1 | False | Discover All Primary Services (C.1) |
| TSPC\_MESH\_20\_2 | False | Discover Primary Services by Service UUID (C.1) |
| TSPC\_MESH\_20\_3 | False | Write without Response (M) |
| TSPC\_MESH\_20\_4 | False | Notifications (M) |
| TSPC\_MESH\_20\_5 | False | Write Characteristic Descriptors (M) |

## GAP Requirements

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_MESH\_21\_1 | False | Broadcaster (C.1) |
| TSPC\_MESH\_21\_2 | False | Observer (C.1) |
| TSPC\_MESH\_21\_3 | False | Central (C.2) |
| TSPC\_MESH\_21\_4 | False | Central - Security Mode 1 (C.2) |
