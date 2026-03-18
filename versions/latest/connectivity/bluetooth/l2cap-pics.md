---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/l2cap-pics.html
original_path: connectivity/bluetooth/l2cap-pics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# L2CAP ICS

PTS version: 8.0.3

M - mandatory

O - optional

## L2CAP Transport Configuration

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_L2CAP\_0\_1 | False | BR/EDR (includes possible support of GAP LE Broadcaster or LE Observer roles) (C.1) |
| TSPC\_L2CAP\_0\_2 | True | LE (C.2) |
| TSPC\_L2CAP\_0\_3 | False | BR/EDR/LE (C.3) |

## Roles

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_L2CAP\_1\_1 | False | Data Channel Initiator (C.3) |
| TSPC\_L2CAP\_1\_2 | False | Data Channel Acceptor (C.1) |
| TSPC\_L2CAP\_1\_3 | True | LE Master (C.2) |
| TSPC\_L2CAP\_1\_4 | True | LE Slave (C.2) |
| TSPC\_L2CAP\_1\_5 | True | LE Data Channel Initiator (C.4) |
| TSPC\_L2CAP\_1\_6 | True | LE Data Channel Acceptor (C.5) |

## General Operation

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_L2CAP\_2\_1 | False | Support of L2CAP signalling channel (C.16) |
| TSPC\_L2CAP\_2\_2 | False | Support of configuration process (C.16) |
| TSPC\_L2CAP\_2\_3 | False | Support of connection oriented data channel (C.16) |
| TSPC\_L2CAP\_2\_4 | False | Support of command echo request (C.17) |
| TSPC\_L2CAP\_2\_5 | False | Support of command echo response (C.16) |
| TSPC\_L2CAP\_2\_6 | False | Support of command information request (C.17) |
| TSPC\_L2CAP\_2\_7 | False | Support of command information response (C.16) |
| TSPC\_L2CAP\_2\_8 | False | Support of a channel group (C.17) |
| TSPC\_L2CAP\_2\_9 | False | Support of packet for connectionless channel (C.17) |
| TSPC\_L2CAP\_2\_10 | False | Support retransmission mode (C.17) |
| TSPC\_L2CAP\_2\_11 | False | Support flow control mode (C.17) |
| TSPC\_L2CAP\_2\_12 | False | Enhanced Retransmission Mode (C.11) |
| TSPC\_L2CAP\_2\_13 | False | Streaming Mode (O) |
| TSPC\_L2CAP\_2\_14 | False | FCS Option (C.1) |
| TSPC\_L2CAP\_2\_15 | False | Generate Local Busy Condition (C.2) |
| TSPC\_L2CAP\_2\_16 | False | Send Reject (C.2) |
| TSPC\_L2CAP\_2\_17 | False | Send Selective Reject (C.2) |
| TSPC\_L2CAP\_2\_18 | False | Mandatory use of ERTM (C.3) |
| TSPC\_L2CAP\_2\_19 | False | Mandatory use of Streaming Mode (C.4) |
| TSPC\_L2CAP\_2\_20 | False | Optional use of ERTM (C.3) |
| TSPC\_L2CAP\_2\_21 | False | Optional use of Streaming Mode (C.4) |
| TSPC\_L2CAP\_2\_22 | False | Send data using SAR in ERTM (C.5) |
| TSPC\_L2CAP\_2\_23 | False | Send data using SAR in Streaming Mode (C.6) |
| TSPC\_L2CAP\_2\_24 | False | Actively request Basic Mode for a PSM that supports the use of ERTM or Streaming Mode (C.7) |
| TSPC\_L2CAP\_2\_25 | False | Supports performing L2CAP channel mode configuration fallback from SM to ERTM (C.8) |
| TSPC\_L2CAP\_2\_26 | False | Supports sending more than one unacknowledged I-Frame when operating in ERTM (C.9) |
| TSPC\_L2CAP\_2\_27 | False | Supports sending more than three unacknowledged I-Frame when operating in ERTM (C.9) |
| TSPC\_L2CAP\_2\_28 | False | Supports configuring the peer TxWindow greater than 1. (C.10) |
| TSPC\_L2CAP\_2\_29 | False | AMP Support (C.11) |
| TSPC\_L2CAP\_2\_30 | False | Fixed Channel Support (C.11) |
| TSPC\_L2CAP\_2\_31 | False | AMP Manager Support (C.11) |
| TSPC\_L2CAP\_2\_32 | False | ERTM over AMP (C.11) |
| TSPC\_L2CAP\_2\_33 | False | Streaming Mode Source over AMP Support (C.12) |
| TSPC\_L2CAP\_2\_34 | False | Streaming Mode Sink over AMP Support (C.12) |
| TSPC\_L2CAP\_2\_35 | False | Unicast Connectionless Data, Reception (O) |
| TSPC\_L2CAP\_2\_36 | False | Ability to transmit an unencrypted packet over a unicast connectionless L2CAP channel (O) |
| TSPC\_L2CAP\_2\_37 | False | Ability to transmit an encrypted packet over a unicast connectionless L2CAP channel. (O) |
| TSPC\_L2CAP\_2\_38 | False | Extended Flow Specification for BR/EDR (C.7) |
| TSPC\_L2CAP\_2\_39 | False | Extended Window Size (C.7) |
| TSPC\_L2CAP\_2\_40 | True | Support of Low Energy signaling channel (C.13) |
| TSPC\_L2CAP\_2\_41 | True | Support of command reject (C.13) |
| TSPC\_L2CAP\_2\_42 | True | Send Connection Parameter Update Request (C.14) |
| TSPC\_L2CAP\_2\_43 | True | Send Connection Parameter Update Response (C.15) |
| TSPC\_L2CAP\_2\_44 | False | Extended Flow Specification for AMP (C.18) |
| TSPC\_L2CAP\_2\_45 | False | Send Disconnect Request Command (C.21) |
| TSPC\_L2CAP\_2\_45a | True | Send Disconnect Request Command – LE (C.22) |
| TSPC\_L2CAP\_2\_46 | True | Support LE Credit Based Flow Control Mode (C.19) |
| TSPC\_L2CAP\_2\_47 | True | Support for LE Data Channel (C.20) |
| TSPC\_L2CAP\_2\_48 | True | Support Enhanced Credit Based Flow Control Mode (C.23) |

## Configurable Parameters

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_L2CAP\_3\_1 | True | Support of RTX timer (M) |
| TSPC\_L2CAP\_3\_2 | False | Support of ERTX timer (C.4) |
| TSPC\_L2CAP\_3\_3 | False | Support minimum MTU size 48 octets (C.4) |
| TSPC\_L2CAP\_3\_4 | False | Support MTU size larger than 48 octets (C.5) |
| TSPC\_L2CAP\_3\_5 | False | Support of flush timeout value for reliable channel (C.4) |
| TSPC\_L2CAP\_3\_6 | False | Support of flush timeout value for unreliable channel (C.5) |
| TSPC\_L2CAP\_3\_7 | False | Support of bi-directional quality of service (QoS) option field (C.1) |
| TSPC\_L2CAP\_3\_8 | False | Negotiate QoS service type (C.5) |
| TSPC\_L2CAP\_3\_9 | False | Negotiate and support service type ‘No Traffic’ (C.2) |
| TSPC\_L2CAP\_3\_10 | False | Negotiate and support service type ‘Best effort’ (C.3) |
| TSPC\_L2CAP\_3\_11 | False | Negotiate and support service type ‘Guaranteed’ (C.2) |
| TSPC\_L2CAP\_3\_12 | True | Support minimum MTU size 23 octets (C.6) |
| TSPC\_L2CAP\_3\_13 | False | Negotiate and support service type ‘No traffic’ for Extended Flow Specification (C.7) |
| TSPC\_L2CAP\_3\_14 | False | Negotiate and support service type ‘Best Effort’ for Extended Flow Specification (C.8) |
| TSPC\_L2CAP\_3\_15 | False | Negotiate and support service type ‘Guaranteed’ for Extended Flow Specification. (C.9) |
| TSPC\_L2CAP\_3\_16 | True | Support Multiple Simultaneous LE Data Channels (C.10) |
