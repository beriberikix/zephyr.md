---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__semihost.html
original_path: doxygen/html/group__semihost.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Semihosting APIs

[Operating System Services](group__os__services.md)

| Enumerations | |
| --- | --- |
| enum | [semihost\_instr](#gadf61e00be557b7cb4457f7ea6f8da86d) {     [SEMIHOST\_OPEN](#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46) = 0x01 , [SEMIHOST\_ISTTY](#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53) = 0x09 , [SEMIHOST\_WRITE](#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad) = 0x05 , [SEMIHOST\_READ](#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02) = 0x06 ,     [SEMIHOST\_CLOSE](#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac) = 0x02 , [SEMIHOST\_FLEN](#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d) = 0x0C , [SEMIHOST\_SEEK](#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629) = 0x0A , [SEMIHOST\_TMPNAM](#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb) = 0x0D ,     [SEMIHOST\_REMOVE](#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce) = 0x0E , [SEMIHOST\_RENAME](#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627) = 0x0F , [SEMIHOST\_WRITEC](#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7) = 0x03 , [SEMIHOST\_WRITE0](#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff) = 0x04 ,     [SEMIHOST\_READC](#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6) = 0x07 , [SEMIHOST\_CLOCK](#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0) = 0x10 , [SEMIHOST\_ELAPSED](#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367) = 0x30 , [SEMIHOST\_TICKFREQ](#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26) = 0x31 ,     [SEMIHOST\_TIME](#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438) = 0x11 , [SEMIHOST\_ERRNO](#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f) = 0x13 , [SEMIHOST\_GET\_CMDLINE](#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f) = 0x15 , [SEMIHOST\_HEAPINFO](#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f) = 0x16 ,     [SEMIHOST\_ISERROR](#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea) = 0x08 , [SEMIHOST\_SYSTEM](#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a) = 0x12   } |
|  | Semihosting instructions. [More...](#gadf61e00be557b7cb4457f7ea6f8da86d) |
| enum | [semihost\_open\_mode](#ga425c53a045590978b0b3235d545780f7) {     [SEMIHOST\_OPEN\_R](#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b) = 0 , [SEMIHOST\_OPEN\_RB](#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde) = 1 , [SEMIHOST\_OPEN\_R\_PLUS](#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9) = 2 , [SEMIHOST\_OPEN\_RB\_PLUS](#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53) = 3 ,     [SEMIHOST\_OPEN\_W](#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc) = 4 , [SEMIHOST\_OPEN\_WB](#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc) = 5 , [SEMIHOST\_OPEN\_W\_PLUS](#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262) = 6 , [SEMIHOST\_OPEN\_WB\_PLUS](#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244) = 7 ,     [SEMIHOST\_OPEN\_A](#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34) = 8 , [SEMIHOST\_OPEN\_AB](#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708) = 9 , [SEMIHOST\_OPEN\_A\_PLUS](#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f) = 10 , [SEMIHOST\_OPEN\_AB\_PLUS](#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466) = 11   } |
|  | Modes to open a file with. [More...](#ga425c53a045590978b0b3235d545780f7) |

| Functions | |
| --- | --- |
| long | [semihost\_exec](#gab8d683d2011f6683956c47a4b129faf4) (enum [semihost\_instr](#gadf61e00be557b7cb4457f7ea6f8da86d) instr, void \*args) |
|  | Manually execute a semihosting instruction. |
| char | [semihost\_poll\_in](#ga4eb7ceb5ceaaded14c3dc129b7fca07b) (void) |
|  | Read a byte from the console. |
| void | [semihost\_poll\_out](#ga4026806d0ea1f6d754851ef7b9f1c58c) (char c) |
|  | Write a byte to the console. |
| long | [semihost\_open](#ga497b911ba4e6b40e4e5808fa9484f5a4) (const char \*path, long mode) |
|  | Open a file on the host system. |
| long | [semihost\_close](#gad8e5d671a2316901eefaf86cac43ac43) (long fd) |
|  | Close a file. |
| long | [semihost\_flen](#gae7476b25d69979d488e1bbd3521d70e0) (long fd) |
|  | Query the size of a file. |
| long | [semihost\_seek](#ga99f88405f4bdc9f43ab2d59b3526ebbc) (long fd, long offset) |
|  | Seeks to an absolute position in a file. |
| long | [semihost\_read](#gaf0d429779cd2b3a06c29f93f8641e9af) (long fd, void \*buf, long len) |
|  | Read the contents of a file into a buffer. |
| long | [semihost\_write](#ga6c340fadaa86cddee2817e96caa00edf) (long fd, const void \*buf, long len) |
|  | Write the contents of a buffer into a file. |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#gadf61e00be557b7cb4457f7ea6f8da86d)semihost\_instr

| enum [semihost\_instr](#gadf61e00be557b7cb4457f7ea6f8da86d) |
| --- |

`#include <[semihost.h](semihost_8h.md)>`

Semihosting instructions.

| Enumerator | |
| --- | --- |
| SEMIHOST\_OPEN | Open a file or stream on the host system. |
| SEMIHOST\_ISTTY | Check whether a file is associated with a stream/terminal. |
| SEMIHOST\_WRITE | Write to a file or stream. |
| SEMIHOST\_READ | Read from a file at the current cursor position. |
| SEMIHOST\_CLOSE | Closes a file on the host which has been opened by SEMIHOST\_OPEN. |
| SEMIHOST\_FLEN | Get the length of a file. |
| SEMIHOST\_SEEK | Set the file cursor to a given position in a file. |
| SEMIHOST\_TMPNAM | Get a temporary absolute file path to create a temporary file. |
| SEMIHOST\_REMOVE | Remove a file on the host system.  Possibly insecure! |
| SEMIHOST\_RENAME | Rename a file on the host system.  Possibly insecure! |
| SEMIHOST\_WRITEC | Write one character to the debug terminal. |
| SEMIHOST\_WRITE0 | Write a NULL terminated string to the debug terminal. |
| SEMIHOST\_READC | Read one character from the debug terminal. |
| SEMIHOST\_CLOCK |  |
| SEMIHOST\_ELAPSED |  |
| SEMIHOST\_TICKFREQ |  |
| SEMIHOST\_TIME |  |
| SEMIHOST\_ERRNO | Retrieve the errno variable from semihosting operations. |
| SEMIHOST\_GET\_CMDLINE | Get commandline parameters for the application to run with. |
| SEMIHOST\_HEAPINFO |  |
| SEMIHOST\_ISERROR |  |
| SEMIHOST\_SYSTEM |  |

## [◆ ](#ga425c53a045590978b0b3235d545780f7)semihost\_open\_mode

| enum [semihost\_open\_mode](#ga425c53a045590978b0b3235d545780f7) |
| --- |

`#include <[semihost.h](semihost_8h.md)>`

Modes to open a file with.

Behaviour corresponds to equivalent fopen strings. i.e. SEMIHOST\_OPEN\_RB\_PLUS == "rb+"

| Enumerator | |
| --- | --- |
| SEMIHOST\_OPEN\_R |  |
| SEMIHOST\_OPEN\_RB |  |
| SEMIHOST\_OPEN\_R\_PLUS |  |
| SEMIHOST\_OPEN\_RB\_PLUS |  |
| SEMIHOST\_OPEN\_W |  |
| SEMIHOST\_OPEN\_WB |  |
| SEMIHOST\_OPEN\_W\_PLUS |  |
| SEMIHOST\_OPEN\_WB\_PLUS |  |
| SEMIHOST\_OPEN\_A |  |
| SEMIHOST\_OPEN\_AB |  |
| SEMIHOST\_OPEN\_A\_PLUS |  |
| SEMIHOST\_OPEN\_AB\_PLUS |  |

## Function Documentation

## [◆ ](#gad8e5d671a2316901eefaf86cac43ac43)semihost\_close()

| long semihost\_close | ( | long | *fd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[semihost.h](semihost_8h.md)>`

Close a file.

Parameters
:   | fd | handle returned by [semihost\_open](#ga497b911ba4e6b40e4e5808fa9484f5a4). |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -1 | on failure. |

## [◆ ](#gab8d683d2011f6683956c47a4b129faf4)semihost\_exec()

| long semihost\_exec | ( | enum [semihost\_instr](#gadf61e00be557b7cb4457f7ea6f8da86d) | *instr*, |
| --- | --- | --- | --- |
|  |  | void \* | *args* ) |

`#include <[semihost.h](semihost_8h.md)>`

Manually execute a semihosting instruction.

Parameters
:   | instr | instruction code to run |
    | --- | --- |
    | args | instruction specific arguments |

Returns
:   integer return code of instruction

## [◆ ](#gae7476b25d69979d488e1bbd3521d70e0)semihost\_flen()

| long semihost\_flen | ( | long | *fd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[semihost.h](semihost_8h.md)>`

Query the size of a file.

Parameters
:   | fd | handle returned by [semihost\_open](#ga497b911ba4e6b40e4e5808fa9484f5a4). |
    | --- | --- |

Return values
:   | positive | file size on success. |
    | --- | --- |
    | -1 | on failure. |

## [◆ ](#ga497b911ba4e6b40e4e5808fa9484f5a4)semihost\_open()

| long semihost\_open | ( | const char \* | *path*, |
| --- | --- | --- | --- |
|  |  | long | *mode* ) |

`#include <[semihost.h](semihost_8h.md)>`

Open a file on the host system.

Parameters
:   | path | file path to open. Can be absolute or relative to current directory of the running process. |
    | --- | --- |
    | mode | value from [semihost\_open\_mode](#ga425c53a045590978b0b3235d545780f7). |

Return values
:   | handle | positive handle on success. |
    | --- | --- |
    | -1 | on failure. |

## [◆ ](#ga4eb7ceb5ceaaded14c3dc129b7fca07b)semihost\_poll\_in()

| char semihost\_poll\_in | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[semihost.h](semihost_8h.md)>`

Read a byte from the console.

Returns
:   char byte read from the console.

## [◆ ](#ga4026806d0ea1f6d754851ef7b9f1c58c)semihost\_poll\_out()

| void semihost\_poll\_out | ( | char | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[semihost.h](semihost_8h.md)>`

Write a byte to the console.

Parameters
:   | c | byte to write to console |
    | --- | --- |

## [◆ ](#gaf0d429779cd2b3a06c29f93f8641e9af)semihost\_read()

| long semihost\_read | ( | long | *fd*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | long | *len* ) |

`#include <[semihost.h](semihost_8h.md)>`

Read the contents of a file into a buffer.

Parameters
:   | fd | handle returned by [semihost\_open](#ga497b911ba4e6b40e4e5808fa9484f5a4). |
    | --- | --- |
    | buf | buffer to read data into. |
    | len | number of bytes to read. |

Return values
:   | read | number of bytes read on success. |
    | --- | --- |
    | -errno | negative error code on failure. |

## [◆ ](#ga99f88405f4bdc9f43ab2d59b3526ebbc)semihost\_seek()

| long semihost\_seek | ( | long | *fd*, |
| --- | --- | --- | --- |
|  |  | long | *offset* ) |

`#include <[semihost.h](semihost_8h.md)>`

Seeks to an absolute position in a file.

Parameters
:   | fd | handle returned by [semihost\_open](#ga497b911ba4e6b40e4e5808fa9484f5a4). |
    | --- | --- |
    | offset | offset from the start of the file in bytes. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | negative error code on failure. |

## [◆ ](#ga6c340fadaa86cddee2817e96caa00edf)semihost\_write()

| long semihost\_write | ( | long | *fd*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | long | *len* ) |

`#include <[semihost.h](semihost_8h.md)>`

Write the contents of a buffer into a file.

Parameters
:   | fd | handle returned by [semihost\_open](#ga497b911ba4e6b40e4e5808fa9484f5a4). |
    | --- | --- |
    | buf | buffer to write data from. |
    | len | number of bytes to write. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | negative error code on failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
