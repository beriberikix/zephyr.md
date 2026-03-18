---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/simcom-sim7080_8h.html
original_path: doxygen/html/simcom-sim7080_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

simcom-sim7080.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](simcom-sim7080_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sim7080\_gnss\_data](structsim7080__gnss__data.md) |
| struct | [sim7080\_sms](structsim7080__sms.md) |
|  | Buffer structure for sms. [More...](structsim7080__sms.md#details) |
| struct | [sim7080\_sms\_buffer](structsim7080__sms__buffer.md) |
|  | Buffer structure for sms reads. [More...](structsim7080__sms__buffer.md#details) |

| Macros | |
| --- | --- |
| #define | [SIM7080\_GNSS\_DATA\_UTC\_LEN](#ace6ac2be37e58af15aeda674923c8201)   20 |
| #define | [SIM7080\_SMS\_MAX\_LEN](#ab64ab50adf37f68e036db2901dd839a7)   160 |

| Enumerations | |
| --- | --- |
| enum | [sim7080\_sms\_stat](#a04f3c0bce4f7d2b35762dc92f0aa20eb) {     [SIM7080\_SMS\_STAT\_REC\_UNREAD](#a04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86) = 0 , [SIM7080\_SMS\_STAT\_REC\_READ](#a04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165) , [SIM7080\_SMS\_STAT\_STO\_UNSENT](#a04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669) , [SIM7080\_SMS\_STAT\_STO\_SENT](#a04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5) ,     [SIM7080\_SMS\_STAT\_ALL](#a04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35)   } |
|  | Possible sms states in memory. [More...](#a04f3c0bce4f7d2b35762dc92f0aa20eb) |
| enum | [sim7080\_ftp\_rc](#a48afa6e777af6010488fbf726f467e63) { [SIM7080\_FTP\_RC\_OK](#a48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda) = 0 , [SIM7080\_FTP\_RC\_FINISHED](#a48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241) , [SIM7080\_FTP\_RC\_ERROR](#a48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce) } |
|  | Possible ftp return codes. [More...](#a48afa6e777af6010488fbf726f467e63) |

| Functions | |
| --- | --- |
| int | [mdm\_sim7080\_power\_on](#a93395c2713539db360cdcf0170075ea1) (void) |
|  | Power on the Sim7080. |
| int | [mdm\_sim7080\_power\_off](#a35c2b87170079e5700021969d01d7f8b) (void) |
|  | Power off the Sim7080. |
| int | [mdm\_sim7080\_start\_network](#ad857dd548490d40e6b9082c0b72e8d2b) (void) |
|  | Starts the modem in network operation mode. |
| int | [mdm\_sim7080\_start\_gnss](#a6106a7d04282af2130471d26f6080ed4) (void) |
|  | Starts the modem in gnss operation mode. |
| int | [mdm\_sim7080\_query\_gnss](#acce71e254dd7854052678319227c3f5b) (struct [sim7080\_gnss\_data](structsim7080__gnss__data.md) \*data) |
|  | Query gnss position form the modem. |
| const char \* | [mdm\_sim7080\_get\_manufacturer](#a79837aee512ae6f2fed52f3162e39868) (void) |
|  | Get the sim7080 manufacturer. |
| const char \* | [mdm\_sim7080\_get\_model](#a557ec2729649fd92c5588f6dd0a04f15) (void) |
|  | Get the sim7080 model information. |
| const char \* | [mdm\_sim7080\_get\_revision](#a9759bf93bc2e8e15869858853a9499de) (void) |
|  | Get the sim7080 revision. |
| const char \* | [mdm\_sim7080\_get\_imei](#a26d1291993cdcd44982c95bad2dd7b4f) (void) |
|  | Get the sim7080 imei number. |
| int | [mdm\_sim7080\_read\_sms](#aacf368bc85d27d49709bde170a0db2ec) (struct [sim7080\_sms\_buffer](structsim7080__sms__buffer.md) \*buffer) |
|  | Read sms from sim module. |
| int | [mdm\_sim7080\_delete\_sms](#ae7137523b94c96d4816e4c19cb48313c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) index) |
|  | Delete a sms at a given index. |
| int | [mdm\_sim7080\_ftp\_get\_start](#a53a7c0d347cfacf0d7fadaf073fbff6c) (const char \*server, const char \*user, const char \*passwd, const char \*file, const char \*path) |
|  | Start a ftp get session. |
| int | [mdm\_sim7080\_ftp\_get\_read](#a74f00c0b99f71f7340740fb199db58a5) (char \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Read data from a ftp get session. |

## Macro Definition Documentation

## [◆ ](#ace6ac2be37e58af15aeda674923c8201)SIM7080\_GNSS\_DATA\_UTC\_LEN

| #define SIM7080\_GNSS\_DATA\_UTC\_LEN   20 |
| --- |

## [◆ ](#ab64ab50adf37f68e036db2901dd839a7)SIM7080\_SMS\_MAX\_LEN

| #define SIM7080\_SMS\_MAX\_LEN   160 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a48afa6e777af6010488fbf726f467e63)sim7080\_ftp\_rc

| enum [sim7080\_ftp\_rc](#a48afa6e777af6010488fbf726f467e63) |
| --- |

Possible ftp return codes.

| Enumerator | |
| --- | --- |
| SIM7080\_FTP\_RC\_OK |  |
| SIM7080\_FTP\_RC\_FINISHED |  |
| SIM7080\_FTP\_RC\_ERROR |  |

## [◆ ](#a04f3c0bce4f7d2b35762dc92f0aa20eb)sim7080\_sms\_stat

| enum [sim7080\_sms\_stat](#a04f3c0bce4f7d2b35762dc92f0aa20eb) |
| --- |

Possible sms states in memory.

| Enumerator | |
| --- | --- |
| SIM7080\_SMS\_STAT\_REC\_UNREAD |  |
| SIM7080\_SMS\_STAT\_REC\_READ |  |
| SIM7080\_SMS\_STAT\_STO\_UNSENT |  |
| SIM7080\_SMS\_STAT\_STO\_SENT |  |
| SIM7080\_SMS\_STAT\_ALL |  |

## Function Documentation

## [◆ ](#ae7137523b94c96d4816e4c19cb48313c)mdm\_sim7080\_delete\_sms()

| int mdm\_sim7080\_delete\_sms | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

Delete a sms at a given index.

Parameters
:   | index | The index of the sms in memory. |
    | --- | --- |

Returns
:   0 on success. Otherwise -1 is returned.

## [◆ ](#a74f00c0b99f71f7340740fb199db58a5)mdm\_sim7080\_ftp\_get\_read()

| int mdm\_sim7080\_ftp\_get\_read | ( | char \* | *dst*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size* ) |

Read data from a ftp get session.

Parameters
:   | dst | The destination buffer. |
    | --- | --- |
    | size | Initialize to the size of dst. Gets set to the number of bytes actually read. |

Returns
:   According [sim7080\_ftp\_rc](#a48afa6e777af6010488fbf726f467e63).

## [◆ ](#a53a7c0d347cfacf0d7fadaf073fbff6c)mdm\_sim7080\_ftp\_get\_start()

| int mdm\_sim7080\_ftp\_get\_start | ( | const char \* | *server*, |
| --- | --- | --- | --- |
|  |  | const char \* | *user*, |
|  |  | const char \* | *passwd*, |
|  |  | const char \* | *file*, |
|  |  | const char \* | *path* ) |

Start a ftp get session.

Parameters
:   | server | The ftp servers address. |
    | --- | --- |
    | user | User name for the ftp server. |
    | passwd | Password for the ftp user. |
    | file | File to be downloaded. |
    | path | Path to the file on the server. |

Returns
:   0 if the session was started. Otherwise -1 is returned.

## [◆ ](#a26d1291993cdcd44982c95bad2dd7b4f)mdm\_sim7080\_get\_imei()

| const char \* mdm\_sim7080\_get\_imei | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the sim7080 imei number.

## [◆ ](#a79837aee512ae6f2fed52f3162e39868)mdm\_sim7080\_get\_manufacturer()

| const char \* mdm\_sim7080\_get\_manufacturer | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the sim7080 manufacturer.

## [◆ ](#a557ec2729649fd92c5588f6dd0a04f15)mdm\_sim7080\_get\_model()

| const char \* mdm\_sim7080\_get\_model | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the sim7080 model information.

## [◆ ](#a9759bf93bc2e8e15869858853a9499de)mdm\_sim7080\_get\_revision()

| const char \* mdm\_sim7080\_get\_revision | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the sim7080 revision.

## [◆ ](#a35c2b87170079e5700021969d01d7f8b)mdm\_sim7080\_power\_off()

| int mdm\_sim7080\_power\_off | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Power off the Sim7080.

Returns
:   0 on success. Otherwise -1 is returned.

## [◆ ](#a93395c2713539db360cdcf0170075ea1)mdm\_sim7080\_power\_on()

| int mdm\_sim7080\_power\_on | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Power on the Sim7080.

Returns
:   0 on success. Otherwise -1 is returned.

## [◆ ](#acce71e254dd7854052678319227c3f5b)mdm\_sim7080\_query\_gnss()

| int mdm\_sim7080\_query\_gnss | ( | struct [sim7080\_gnss\_data](structsim7080__gnss__data.md) \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

Query gnss position form the modem.

Returns
:   0 on success. If no fix is acquired yet -EAGAIN is returned. Otherwise <0 is returned.

## [◆ ](#aacf368bc85d27d49709bde170a0db2ec)mdm\_sim7080\_read\_sms()

| int mdm\_sim7080\_read\_sms | ( | struct [sim7080\_sms\_buffer](structsim7080__sms__buffer.md) \* | *buffer* | ) |  |
| --- | --- | --- | --- | --- | --- |

Read sms from sim module.

Parameters
:   | buffer | Buffer structure for sms. |
    | --- | --- |

Returns
:   Number of sms read on success. Otherwise -1 is returned.

Note
:   The buffer structure needs to be initialized to the size of the sms buffer. When this function finishes successful, nsms will be set to the number of sms read. If the whole structure is filled a subsequent read may be needed.

## [◆ ](#a6106a7d04282af2130471d26f6080ed4)mdm\_sim7080\_start\_gnss()

| int mdm\_sim7080\_start\_gnss | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Starts the modem in gnss operation mode.

Returns
:   0 on success. Otherwise <0 is returned.

## [◆ ](#ad857dd548490d40e6b9082c0b72e8d2b)mdm\_sim7080\_start\_network()

| int mdm\_sim7080\_start\_network | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Starts the modem in network operation mode.

Returns
:   0 on success. Otherwise <0 is returned.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [modem](dir_921fc901d44f7fec5fdbf8b941e64fce.md)
- [simcom-sim7080.h](simcom-sim7080_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
