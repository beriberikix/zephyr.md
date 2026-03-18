---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/sm-pics.html
original_path: connectivity/bluetooth/sm-pics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SM ICS

PTS version: 8.0.3

M - mandatory

O - optional

## Role

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_1\_1 | True | Central Role (Initiator) (C.1) |
| TSPC\_SM\_1\_2 | True | Peripheral Role (Responder) (C.2) |

## Security Properties

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_2\_1 | True | Authenticated MITM protection (O) |
| TSPC\_SM\_2\_2 | True | Unauthenticated no MITM protection (C.1) |
| TSPC\_SM\_2\_3 | True | No security requirements (M) |
| TSPC\_SM\_2\_4 | True | OOB supported (O) |
| TSPC\_SM\_2\_5 | True | LE Secure Connections (O) |

## Encryption Key Size

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_3\_1 | True | Encryption Key Size (M) |

## Pairing Method

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_4\_1 | True | Just Works (O) |
| TSPC\_SM\_4\_2 | True | Passkey Entry (C.1) |
| TSPC\_SM\_4\_3 | True | Out of Band (C.1) |

## Security Initiation

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_5\_1 | True | Encryption Setup using STK (C.3) |
| TSPC\_SM\_5\_2 | True | Encryption Setup using LTK (O) |
| TSPC\_SM\_5\_3 | True | Peripheral Initiated Security (C.1) |
| TSPC\_SM\_5\_4 | True | Peripheral Initiated Security – Central response (C.2) |
| TSPC\_SM\_5\_5 | False | Link Key Conversion Function h7 (C.4) |
| TSPC\_SM\_5\_6 | False | Link Key Conversion Function h6 (C.5) |

## Signing Algorithm

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_6\_1 | True | Signing Algorithm - Generation (O) |
| TSPC\_SM\_6\_2 | True | Signing Algorithm - Resolving (O) |

## Key Distribution

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_7\_1 | True | Encryption Key (C.1) |
| TSPC\_SM\_7\_2 | True | Identity Key (C.2) |
| TSPC\_SM\_7\_3 | True | Signing Key (C.3) |

## Cross-Transport Key Derivation

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_SM\_8\_1 | False | Cross Transport Key Derivation Supported (C.1) |
| TSPC\_SM\_8\_2 | False | Derivation of LE LTK from BR/EDR Link Key (C.2) |
| TSPC\_SM\_8\_3 | False | Derivation of BR/EDR Link Key from LE LTK (C.2) |
