---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/gap-pics.html
original_path: connectivity/bluetooth/gap-pics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# GAP ICS

PTS version: 8.0.3

M - mandatory

O - optional

## Device Configuration

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_0\_1 | False | BR/EDR (C.1) |
| TSPC\_GAP\_0\_2 | True | LE (C.2) |
| TSPC\_GAP\_0\_3 | False | BR/EDR/LE (C.3) |

## Modes

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_1\_1 | False | Non-discoverable mode (C.1) |
| TSPC\_GAP\_1\_2 | False | Limited-discoverable mode (O) |
| TSPC\_GAP\_1\_3 | False | General-discoverable mode (O) |
| TSPC\_GAP\_1\_4 | False | Non-connectable mode (O) |
| TSPC\_GAP\_1\_5 | False | Connectable mode (M) |
| TSPC\_GAP\_1\_6 | False | Non-bondable mode (O) |
| TSPC\_GAP\_1\_7 | False | Bondable mode (C.2) |
| TSPC\_GAP\_1\_8 | False | Non-Synchronizable Mode (C.3) |
| TSPC\_GAP\_1\_9 | False | Synchronizable Mode (C.4) |

## Security Aspects

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_2\_1 | False | Authentication procedure (C.1) |
| TSPC\_GAP\_2\_2 | False | Support of LMP-Authentication (M) |
| TSPC\_GAP\_2\_3 | False | Initiate LMP-Authentication (C.5) |
| TSPC\_GAP\_2\_4 | False | Security mode 1 (C.2) |
| TSPC\_GAP\_2\_5 | False | Security mode 2 (O) |
| TSPC\_GAP\_2\_6 | False | Security mode 3 (C.7) |
| TSPC\_GAP\_2\_7 | False | Security mode 4 (M) |
| TSPC\_GAP\_2\_7a | False | Security mode 4, level 4 (C.9) |
| TSPC\_GAP\_2\_7b | False | Security mode 4, level 3 (C.9) |
| TSPC\_GAP\_2\_7c | False | Security mode 4, level 2 (C.9) |
| TSPC\_GAP\_2\_7d | False | Security mode 4, level 1 (C.9) |
| TSPC\_GAP\_2\_8 | False | Support of Authenticated link key (C.6) |
| TSPC\_GAP\_2\_9 | False | Support of Unauthenticated link key (C.6) |
| TSPC\_GAP\_2\_10 | False | Security Optional (C.6) |
| TSPC\_GAP\_2\_11 | False | Secure Connections Only Mode (C.8) |
| TSPC\_GAP\_2\_12 | False | 56-bit minimum encryption key size (C.10) |
| TSPC\_GAP\_2\_13 | False | 128-bit encryption key size capable (C.11) |

## Idle Mode Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_3\_1 | False | Initiation of general inquiry (C.1) |
| TSPC\_GAP\_3\_2 | False | Initiation of limited inquiry (C.1) |
| TSPC\_GAP\_3\_3 | False | Initiation of name discovery (O) |
| TSPC\_GAP\_3\_4 | False | Initiation of device discovery (O) |
| TSPC\_GAP\_3\_5 | False | Initiation of general bonding (O) |
| TSPC\_GAP\_3\_6 | False | Initiation of dedicated bonding (O) |

## Establishment Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_4\_1 | False | Support link establishment as initiator (M) |
| TSPC\_GAP\_4\_2 | False | Support link establishment as acceptor (M) |
| TSPC\_GAP\_4\_3 | False | Support channel establishment as initiator (O) |
| TSPC\_GAP\_4\_4 | False | Support channel establishment as acceptor (M) |
| TSPC\_GAP\_4\_5 | False | Support connection establishment as initiator (O) |
| TSPC\_GAP\_4\_6 | False | Support connection establishment as acceptor (O) |
| TSPC\_GAP\_4\_7 | False | Support synchronization establishment as receiver (C.1) |

## LE Roles

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_5\_1 | True | Broadcaster (C.1) |
| TSPC\_GAP\_5\_2 | True | Observer (C.1) |
| TSPC\_GAP\_5\_3 | True | Peripheral (C.1) |
| TSPC\_GAP\_5\_4 | True | Central (C.1) |

## Broadcaster Physical Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_6\_1 | True | Transmitter (M) |
| TSPC\_GAP\_6\_2 | True | Receiver (O) |

## Broadcaster Link Layer States

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_7\_1 | True | Standby (M) |
| TSPC\_GAP\_7\_2 | True | Advertising (M) |
| TSPC\_GAP\_7\_3 | False | Isochronous Broadcasting State (C.1) |

## Broadcaster Link Layer Advertising Event Types

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_8\_1 | True | Non-Connectable Undirected Event (M) |
| TSPC\_GAP\_8\_2 | True | Scannable Undirected Event (O) |
| TSPC\_GAP\_8\_3 | True | Non-Connectable and Non-Scannable Directed Event (C.1) |
| TSPC\_GAP\_8\_4 | True | Scannable Directed Event (C.1) |

## Broadcaster Link Layer Advertising Data Types

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_8a\_1 | True | AD Type – Service UUID (O) |
| TSPC\_GAP\_8a\_2 | True | AD Type – Local Name (O) |
| TSPC\_GAP\_8a\_3 | True | AD Type – Flags (O) |
| TSPC\_GAP\_8a\_4 | True | AD Type – Manufacturer Specific Data (O) |
| TSPC\_GAP\_8a\_5 | True | AD Type – TX Power Level (O) |
| TSPC\_GAP\_8a\_6 | False | AD Type – Security Manager Out of Band (OOB) (C.1) |
| TSPC\_GAP\_8a\_7 | True | AD Type – Security Manager TK Value (O) |
| TSPC\_GAP\_8a\_8 | True | AD Type – Peripheral Connection Interval Range (O) |
| TSPC\_GAP\_8a\_9 | True | AD Type - Service Solicitation (O) |
| TSPC\_GAP\_8a\_10 | True | AD Type – Service Data (O) |
| TSPC\_GAP\_8a\_11 | True | AD Type – Appearance (O) |
| TSPC\_GAP\_8a\_12 | True | AD Type – Public Target Address (O) |
| TSPC\_GAP\_8a\_13 | True | AD Type – Random Target Address (O) |
| TSPC\_GAP\_8a\_14 | True | AD Type – Advertising Interval (O) |
| TSPC\_GAP\_8a\_15 | True | AD Type – LE Bluetooth Device Address (O) |
| TSPC\_GAP\_8a\_16 | True | AD Type – LE Role (O) |
| TSPC\_GAP\_8a\_17 | True | AD Type - URI (O) |

## Broadcaster Connection Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_9\_1 | True | Non-Connectable Mode (M) |

## Broadcaster Broadcasting and Observing Features

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_10\_1 | True | Broadcast Mode (M) |
| TSPC\_GAP\_10\_2 | False | Broadcast Isochronous Synchronizability mode (C.1) |
| TSPC\_GAP\_10\_3 | False | Broadcast Isochronous Broadcasting mode (C.2) |
| TSPC\_GAP\_10\_4 | False | Broadcast Isochronous Terminate procedure (C.1) |
| TSPC\_GAP\_10\_5 | False | Broadcast Isochronous Channel Map Update Procedure (C.1) |

## Broadcaster Privacy Feature

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_11\_1 | True | Privacy Feature (O) |
| TSPC\_GAP\_11\_2 | True | Resolvable Private Address Generation Procedure (C.1) |
| TSPC\_GAP\_11\_3 | True | Non-Resolvable Private Address Generation Procedure (C.2) |

## Periodic Advertising Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_11a\_1 | False | Periodic Advertising Synchronizability mode (C.1) |
| TSPC\_GAP\_11a\_2 | False | Periodic Advertising mode (C.2) |

## Broadcaster Security Aspects Features

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_11b\_1 | False | LE Security Mode 3 (C.1) |
| TSPC\_GAP\_11b\_2 | False | LE Security Mode 3, Level 1 (C.2) |
| TSPC\_GAP\_11b\_3 | False | LE Security Mode 3, Level 2 (C.2) |
| TSPC\_GAP\_11b\_4 | False | LE Security Mode 3, Level 3 (C.2) |

## Observer Physical Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_12\_1 | True | Receiver (M) |
| TSPC\_GAP\_12\_2 | True | Transmitter (O) |

## Observer Link Layer States

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_13\_1 | True | Standby (M) |
| TSPC\_GAP\_13\_2 | True | Scanning (M) |

## Observer Link Layer Scanning Types

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_14\_1 | True | Passive Scanning (M) |
| TSPC\_GAP\_14\_2 | True | Active Scanning (O) |

## Observer Connection Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_15\_1 | True | Non-Connectable Modes (M) |

## Observer Broadcasting and Observing Features

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_16\_1 | True | Observation Procedure (M) |
| TSPC\_GAP\_16\_2 | False | Broadcast Isochronous Synchronization Establishment procedure (C.1) |
| TSPC\_GAP\_16\_3 | False | Broadcast Isochronous Termination procedure (C.2) |
| TSPC\_GAP\_16\_4 | False | Broadcast Isochronous Channel Map Update Procedure (C.2) |

## Observer Privacy Feature

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_17\_1 | True | Privacy Feature (O) |
| TSPC\_GAP\_17\_2 | True | Non-Resolvable Private Address Generation Procedure (C.1) |
| TSPC\_GAP\_17\_3 | True | Resolvable Private Address Resolution Procedure (O) |
| TSPC\_GAP\_17\_4 | True | Resolvable Private Address Generation Procedure (C.2) |

## Periodic Advertising Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_17a\_1 | False | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising (C.1) |
| TSPC\_GAP\_17a\_2 | False | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising (C.1) |

## Observer Security Aspects Features

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_17b\_1 | False | LE Security Mode 3 (C.1) |
| TSPC\_GAP\_17b\_2 | False | LE Security Mode 3, Level 1 (C.2) |
| TSPC\_GAP\_17b\_3 | False | LE Security Mode 3, Level 2 (C.2) |
| TSPC\_GAP\_17b\_4 | False | LE Security Mode 3, Level 3 (C.2) |

## Peripheral Physical Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_18\_1 | True | Transmitter (M) |
| TSPC\_GAP\_18\_2 | True | Receiver (M) |

## Peripheral Link Layer States

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_19\_1 | True | Standby (M) |
| TSPC\_GAP\_19\_2 | True | Advertising (M) |
| TSPC\_GAP\_19\_3 | True | Connection, Peripheral Role (M) |

## Peripheral Link Layer Advertising Event Types

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_20\_1 | True | Connectable and Scannable Undirected Event (M) |
| TSPC\_GAP\_20\_2 | True | Connectable Directed Event (O) |
| TSPC\_GAP\_20\_3 | True | Non-Connectable and Non-Scannable Undirected Event (O) |
| TSPC\_GAP\_20\_4 | True | Scannable Undirected Event (O) |
| TSPC\_GAP\_20\_5 | True | Connectable Undirected Event (C.1) |
| TSPC\_GAP\_20\_6 | True | Non-Connectable and Non-Scannable Directed Event (C.1) |
| TSPC\_GAP\_20\_7 | True | Scannable Directed Event (C.1) |

## Peripheral Link Layer Advertising Data Types

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_20A\_1 | True | AD Type – Service UUID (C.1) |
| TSPC\_GAP\_20A\_2 | True | AD Type – Local Name (C.1) |
| TSPC\_GAP\_20A\_3 | True | AD Type – Flags (C.2) |
| TSPC\_GAP\_20A\_4 | True | AD Type – Manufacturer Specific Data (C.1) |
| TSPC\_GAP\_20A\_5 | True | AD Type – TX Power Level (C.1) |
| TSPC\_GAP\_20A\_6 | False | AD Type – Security Manager Out of Band (OOB) (C.3) |
| TSPC\_GAP\_20A\_7 | True | AD Type – Security Manager TK Value (C.1) |
| TSPC\_GAP\_20A\_8 | True | AD Type – Peripheral Connection Interval Range (C.1) |
| TSPC\_GAP\_20A\_9 | True | AD Type – Service Solicitation (C.1) |
| TSPC\_GAP\_20A\_10 | True | AD Type – Service Data (C.1) |
| TSPC\_GAP\_20A\_11 | True | AD Type – Appearance (C.1) |
| TSPC\_GAP\_20A\_12 | True | AD Type – Public Target Address (C.1) |
| TSPC\_GAP\_20A\_13 | True | AD Type – Random Target Address (C.1) |
| TSPC\_GAP\_20A\_14 | True | AD Type – Advertising Interval (C.1) |
| TSPC\_GAP\_20A\_15 | True | AD Type – LE Bluetooth Device Address (C.1) |
| TSPC\_GAP\_20A\_16 | True | AD Type – LE Role (C.1) |
| TSPC\_GAP\_20A\_17 | True | AD Type – URI (O) |

## Peripheral Link Layer Control Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_21\_1 | True | Connection Update Procedure (M) |
| TSPC\_GAP\_21\_2 | True | Channel Map Update Procedure (M) |
| TSPC\_GAP\_21\_3 | True | Encryption Procedure (O) |
| TSPC\_GAP\_21\_4 | True | Central Initiated Feature Exchange Procedure (M) |
| TSPC\_GAP\_21\_5 | True | Version Exchange Procedure (M) |
| TSPC\_GAP\_21\_6 | True | Termination Procedure (M) |
| TSPC\_GAP\_21\_7 | True | LE Ping Procedure (O) |
| TSPC\_GAP\_21\_8 | True | Peripheral Initiated Feature Exchange Procedure (C.1) |
| TSPC\_GAP\_21\_9 | True | Connection Parameter Request Procedure (O) |
| TSPC\_GAP\_21\_10 | True | Data Length Update Procedure (O) |
| TSPC\_GAP\_21\_11 | True | PHY Update Procedure (C.2) |
| TSPC\_GAP\_21\_12 | False | Minimum Number Of Used Channels Procedure (C.2) |

## Peripheral Discovery Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_22\_1 | True | Non-Discoverable Mode (M) |
| TSPC\_GAP\_22\_2 | True | Limited Discoverable Mode (O) |
| TSPC\_GAP\_22\_3 | True | General Discoverable Mode (C.1) |
| TSPC\_GAP\_22\_4 | True | Name Discovery Procedure (O) |

## Peripheral Connection Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_23\_1 | True | Non-Connectable Mode (M) |
| TSPC\_GAP\_23\_2 | False | Directed Connectable Mode (O) |
| TSPC\_GAP\_23\_3 | True | Undirected Connectable Mode (M) |
| TSPC\_GAP\_23\_4 | True | Connection Parameter Update Procedure (O) |
| TSPC\_GAP\_23\_5 | True | Terminate Connection Procedure (M) |
| TSPC\_GAP\_23\_6 | False | Connected Isochronous Stream Request procedure (C.1) |
| TSPC\_GAP\_23\_7 | False | Connected Isochronous Stream Termination procedure (C.1) |

## Peripheral Bonding Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_24\_1 | True | Non-Bondable Mode (M) |
| TSPC\_GAP\_24\_2 | True | Bondable Mode (O) |
| TSPC\_GAP\_24\_3 | True | Bonding Procedure (O) |
| TSPC\_GAP\_24\_4 | True | Multiple Bonds (C.1) |

## Peripheral Security Aspects Features

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_25\_1 | True | Security Mode 1 (O) |
| TSPC\_GAP\_25\_2 | True | Security Mode 2 (O) |
| TSPC\_GAP\_25\_3 | True | Authentication Procedure (O) |
| TSPC\_GAP\_25\_4 | True | Authorization Procedure (O) |
| TSPC\_GAP\_25\_5 | True | Connection Data Signing Procedure (O) |
| TSPC\_GAP\_25\_6 | True | Authenticate Signed Data Procedure (O) |
| TSPC\_GAP\_25\_7 | True | Authenticated Pairing (LE security mode 1 level 3) (C.1) |
| TSPC\_GAP\_25\_8 | True | Unauthenticated Pairing (LE security mode 1 level 2) (C.1) |
| TSPC\_GAP\_25\_9 | True | LE Security Mode 1 Level 4 (C.3) |
| TSPC\_GAP\_25\_10 | True | Secure Connections Only Mode (C.4) |
| TSPC\_GAP\_25\_11 | False | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only (C.3) |
| TSPC\_GAP\_25\_12 | False | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only (C.3) |
| TSPC\_GAP\_25\_13 | True | Minimum 128 Bit entropy key (C.5) |

## Peripheral Privacy Feature

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_26\_1 | True | Privacy Feature (O) |
| TSPC\_GAP\_26\_2 | True | Non-Resolvable Private Address Generation Procedure (O) |
| TSPC\_GAP\_26\_3 | True | Resolvable Private Address Generation Procedure (C.1) |
| TSPC\_GAP\_26\_4 | True | Resolvable Private Address Resolution Procedure (C.1) |

## Peripheral GAP Characteristics

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_27\_1 | True | Device Name (M) |
| TSPC\_GAP\_27\_2 | True | Appearance (M) |
| TSPC\_GAP\_27\_5 | True | Peripheral Preferred Connection Parameters (O) |
| TSPC\_GAP\_27\_6 | True | Writeable Device Name (O) |
| TSPC\_GAP\_27\_7 | False | Writeable Appearance (O) |
| TSPC\_GAP\_27\_9 | True | Central Address Resolution (C.1) |

## Periodic Advertising Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_27a\_1 | False | Periodic Advertising Synchronization Transfer procedure (C.1) |
| TSPC\_GAP\_27a\_2 | False | Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising (C.2) |
| TSPC\_GAP\_27a\_3 | False | Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising (C.3) |

## Central Physical Layer

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_28\_1 | True | Transmitter (M) |
| TSPC\_GAP\_28\_2 | True | Receiver (M) |

## Central Link Layer States

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_29\_1 | True | Standby (M) |
| TSPC\_GAP\_29\_2 | True | Scanning (M) |
| TSPC\_GAP\_29\_3 | True | Initiating (M) |
| TSPC\_GAP\_29\_4 | True | Connection, Central Role (M) |

## Central Link Layer Scanning Types

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_30\_1 | True | Passive Scanning (O) |
| TSPC\_GAP\_30\_2 | True | Active Scanning (C.1) |

## Central Link Layer Control Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_31\_1 | True | Connection Update Procedure (M) |
| TSPC\_GAP\_31\_2 | True | Channel Map Update Procedure (M) |
| TSPC\_GAP\_31\_3 | True | Encryption Procedure (O) |
| TSPC\_GAP\_31\_4 | True | Central Initiated Feature Exchange Procedure (M) |
| TSPC\_GAP\_31\_5 | True | Version Exchange Procedure (M) |
| TSPC\_GAP\_31\_6 | True | Termination Procedure (M) |
| TSPC\_GAP\_31\_7 | False | LE Ping Procedure (O) |
| TSPC\_GAP\_31\_8 | True | Peripheral Initiated Feature Exchange Procedure (C.1) |
| TSPC\_GAP\_31\_9 | True | Connection Parameter Request Procedure (O) |
| TSPC\_GAP\_31\_10 | True | Data Length Update Procedure (O) |
| TSPC\_GAP\_31\_11 | True | PHY Update Procedure (C.2) |
| TSPC\_GAP\_31\_12 | False | Minimum Number Of Used Channels Procedure (C.2) |

## Central Discovery Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_32\_1 | True | Limited Discovery Procedure (O) |
| TSPC\_GAP\_32\_2 | True | General Discovery Procedure (M) |
| TSPC\_GAP\_32\_3 | True | Name Discovery Procedure (O) |

## Central Connection Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_33\_1 | True | Auto Connection Establishment Procedure (O) |
| TSPC\_GAP\_33\_2 | True | General Connection Establishment Procedure (O) |
| TSPC\_GAP\_33\_3 | False | Selective Connection Establishment Procedure (O) |
| TSPC\_GAP\_33\_4 | True | Selective Connection Establishment Procedure (M) |
| TSPC\_GAP\_33\_5 | True | Connection Parameter Update Procedure (M) |
| TSPC\_GAP\_33\_6 | True | Terminate Connection Procedure (M) |
| TSPC\_GAP\_33\_7 | False | Connected Isochronous Stream Creation procedure (C.1) |
| TSPC\_GAP\_33\_8 | False | Connected Isochronous Stream Termination procedure (C.1) |

## Central Bonding Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_34\_1 | True | Non-Bondable Mode (M) |
| TSPC\_GAP\_34\_2 | True | Bondable Mode (O) |
| TSPC\_GAP\_34\_3 | True | Bonding Procedure (O) |

## Central Security Features

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_35\_1 | True | Security Mode 1 (O) |
| TSPC\_GAP\_35\_2 | True | Security Mode 2 (O) |
| TSPC\_GAP\_35\_3 | True | Authentication Procedure (O) |
| TSPC\_GAP\_35\_4 | False | Authorization Procedure (O) |
| TSPC\_GAP\_35\_5 | True | Connection Data Signing Procedure (O) |
| TSPC\_GAP\_35\_6 | True | Authenticate Signed Data Procedure (O) |
| TSPC\_GAP\_35\_7 | True | Authenticated Pairing (LE security mode 1 level 3) (C.1) |
| TSPC\_GAP\_35\_8 | True | Unauthenticated Pairing (LE security mode1 level 2) (C.1) |
| TSPC\_GAP\_35\_9 | True | LE Security Mode 1 Level 4 (C.2) |
| TSPC\_GAP\_35\_10 | True | Secure Connections Only Mode (C.3) |
| TSPC\_GAP\_35\_11 | False | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only (C.2) |
| TSPC\_GAP\_35\_12 | False | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only (C.2) |
| TSPC\_GAP\_35\_13 | True | Minimum 128 Bit entropy key (C.4) |

## Central Privacy Feature

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_36\_1 | True | Privacy Feature (O) |
| TSPC\_GAP\_36\_2 | True | Non-Resolvable Private Address Generation Procedure (O) |
| TSPC\_GAP\_36\_3 | True | Resolvable Private Address Resolution Procedure (C.1) |
| TSPC\_GAP\_36\_5 | True | Resolvable Private Address Generation Procedure (C.1) |

## Central GAP Characteristics

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_37\_1 | True | Device Name (M) |
| TSPC\_GAP\_37\_2 | True | Appearance (M) |
| TSPC\_GAP\_37\_3 | True | Central Address Resolution (C.1) |

## Periodic Advertising Modes and Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_37a\_1 | False | Periodic Advertising Synchronization Transfer procedure (C.1) |
| TSPC\_GAP\_37a\_2 | False | Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising (C.2) |
| TSPC\_GAP\_37a\_3 | False | Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising (C.3) |

## BR/EDR/LE Roles

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_38\_1 | False | Broadcaster (C.1) |
| TSPC\_GAP\_38\_2 | False | Observer (C.1) |
| TSPC\_GAP\_38\_3 | False | Peripheral (C.1) |
| TSPC\_GAP\_38\_4 | False | Central (C.1) |

## Central BR/EDR/LE Security Aspects

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_41\_1 | False | Security Aspects (M) |
| TSPC\_GAP\_41\_2a | False | Derivation of BR/EDR Link Key from LE LTK (C.1) |
| TSPC\_GAP\_41\_2b | False | Derivation of LE LTK from BR/EDR Link Key (C.2) |

## Peripheral BR/EDR/LE Security Aspects

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_43\_1 | False | Security Aspects (M) |
| TSPC\_GAP\_43\_2a | False | Derivation of BR/EDR Link Key from LE LTK (C.1) |
| TSPC\_GAP\_43\_2b | False | Derivation of LE LTK from BR/EDR Link Key (C.2) |

## Central Simultaneous BR/EDR and LE Transports

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_44\_1 | False | Simultaneous BR/EDR and LE Transports – BR/EDR Peripheral to the same device (O) |
| TSPC\_GAP\_44\_2 | False | Simultaneous BR/EDR and LE Transports – BR/EDR Central to the same device (O) |

## Peripheral Simultaneous BR/EDR and LE Transports

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_GAP\_45\_1 | False | Simultaneous BR/EDR and LE Transports – BR/EDR Peripheral to the same device (O) |
| TSPC\_GAP\_45\_2 | False | Simultaneous BR/EDR and LE Transports – BR/EDR Central to the same device (O) |
