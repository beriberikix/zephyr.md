---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/rfcomm-pics.html
original_path: connectivity/bluetooth/rfcomm-pics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# RFCOMM PICS

PTS version: 6.4

- - different than PTS defaults

## Protocol Version

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_RFCOMM\_0\_1 | False | RFCOMM 1.1 with TS 07.10 |
| TSPC\_RFCOMM\_0\_2 | True (\*) | RFCOMM 1.2 with TS 07.10 |

## Supported Procedures

| Parameter Name | Selected | Description |
| --- | --- | --- |
| TSPC\_RFCOMM\_1\_1 | True (\*) | Initialize RFCOMM Session |
| TSPC\_RFCOMM\_1\_2 | True (\*) | Respond to Initialization of an RFCOMM Session |
| TSPC\_RFCOMM\_1\_3 | True | Shutdown RFCOMM Session |
| TSPC\_RFCOMM\_1\_4 | True | Respond to a Shutdown of an RFCOMM Session |
| TSPC\_RFCOMM\_1\_5 | True (\*) | Establish DLC |
| TSPC\_RFCOMM\_1\_6 | True (\*) | Respond to Establishment of a DLC |
| TSPC\_RFCOMM\_1\_7 | True | Disconnect DLC |
| TSPC\_RFCOMM\_1\_8 | True | Respond to Disconnection of a DLC |
| TSPC\_RFCOMM\_1\_9 | True | Respond to and send MSC Command |
| TSPC\_RFCOMM\_1\_10 | True | Initiate Transfer Information |
| TSPC\_RFCOMM\_1\_11 | True | Respond to Test Command |
| TSPC\_RFCOMM\_1\_12 | False | Send Test Command |
| TSPC\_RFCOMM\_1\_13 | True | React to Aggregate Flow Control |
| TSPC\_RFCOMM\_1\_14 | True | Respond to RLS Command |
| TSPC\_RFCOMM\_1\_15 | False | Send RLS Command |
| TSPC\_RFCOMM\_1\_16 | True | Respond to PN Command |
| TSPC\_RFCOMM\_1\_17 | True (\*) | Send PN Command |
| TSPC\_RFCOMM\_1\_18 | True (\*) | Send Non-Supported Command (NSC) response |
| TSPC\_RFCOMM\_1\_19 | True | Respond to RPN Command |
| TSPC\_RFCOMM\_1\_20 | False | Send RPN Command |
| TSPC\_RFCOMM\_1\_21 | True (\*) | Closing Multiplexer by First Sending a DISC Command |
| TSPC\_RFCOMM\_1\_22 | True | Support of Credit Based Flow Control |
