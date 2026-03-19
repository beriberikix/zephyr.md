---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/semihost_8h_source.html
original_path: doxygen/html/semihost_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

semihost.h

[Go to the documentation of this file.](semihost_8h.md)

1/\*

2 \* Copyright (c) 2022, Commonwealth Scientific and Industrial Research

3 \* Organisation (CSIRO) ABN 41 687 119 230.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*

7 \* Based on the ARM semihosting API from:

8 \* https://github.com/ARM-software/abi-aa/blob/main/semihosting/semihosting.rst

9 \*

10 \* RISC-V semihosting also follows these conventions:

11 \* https://github.com/riscv/riscv-semihosting-spec/blob/main/riscv-semihosting-spec.adoc

12 \*/

13

22

23#ifndef ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SEMIHOST\_H\_

24#define ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SEMIHOST\_H\_

25

[ 27](group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d)enum [semihost\_instr](group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d) {

28 /\*

29 \* File I/O operations

30 \*/

31

[ 33](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46) [SEMIHOST\_OPEN](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46) = 0x01,

[ 35](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53) [SEMIHOST\_ISTTY](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53) = 0x09,

[ 37](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad) [SEMIHOST\_WRITE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad) = 0x05,

[ 39](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02) [SEMIHOST\_READ](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02) = 0x06,

[ 41](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac) [SEMIHOST\_CLOSE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac) = 0x02,

[ 43](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d) [SEMIHOST\_FLEN](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d) = 0x0C,

[ 45](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629) [SEMIHOST\_SEEK](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629) = 0x0A,

[ 47](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb) [SEMIHOST\_TMPNAM](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb) = 0x0D,

[ 49](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce) [SEMIHOST\_REMOVE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce) = 0x0E,

[ 51](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627) [SEMIHOST\_RENAME](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627) = 0x0F,

52

53 /\*

54 \* Terminal I/O operations

55 \*/

56

[ 58](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7) [SEMIHOST\_WRITEC](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7) = 0x03,

[ 60](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff) [SEMIHOST\_WRITE0](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff) = 0x04,

[ 62](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6) [SEMIHOST\_READC](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6) = 0x07,

63

64 /\*

65 \* Time operations

66 \*/

[ 67](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0) [SEMIHOST\_CLOCK](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0) = 0x10,

[ 68](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367) [SEMIHOST\_ELAPSED](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367) = 0x30,

[ 69](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26) [SEMIHOST\_TICKFREQ](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26) = 0x31,

[ 70](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438) [SEMIHOST\_TIME](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438) = 0x11,

71

72 /\*

73 \* System/Misc. operations

74 \*/

75

[ 77](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f) [SEMIHOST\_ERRNO](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f) = 0x13,

[ 79](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f) [SEMIHOST\_GET\_CMDLINE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f) = 0x15,

[ 80](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f) [SEMIHOST\_HEAPINFO](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f) = 0x16,

[ 81](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea) [SEMIHOST\_ISERROR](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea) = 0x08,

[ 82](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a) [SEMIHOST\_SYSTEM](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a) = 0x12

83};

84

[ 91](group__semihost.md#ga425c53a045590978b0b3235d545780f7)enum [semihost\_open\_mode](group__semihost.md#ga425c53a045590978b0b3235d545780f7) {

[ 92](group__semihost.md#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b) [SEMIHOST\_OPEN\_R](group__semihost.md#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b) = 0,

[ 93](group__semihost.md#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde) [SEMIHOST\_OPEN\_RB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde) = 1,

[ 94](group__semihost.md#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9) [SEMIHOST\_OPEN\_R\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9) = 2,

[ 95](group__semihost.md#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53) [SEMIHOST\_OPEN\_RB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53) = 3,

[ 96](group__semihost.md#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc) [SEMIHOST\_OPEN\_W](group__semihost.md#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc) = 4,

[ 97](group__semihost.md#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc) [SEMIHOST\_OPEN\_WB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc) = 5,

[ 98](group__semihost.md#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262) [SEMIHOST\_OPEN\_W\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262) = 6,

[ 99](group__semihost.md#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244) [SEMIHOST\_OPEN\_WB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244) = 7,

[ 100](group__semihost.md#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34) [SEMIHOST\_OPEN\_A](group__semihost.md#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34) = 8,

[ 101](group__semihost.md#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708) [SEMIHOST\_OPEN\_AB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708) = 9,

[ 102](group__semihost.md#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f) [SEMIHOST\_OPEN\_A\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f) = 10,

[ 103](group__semihost.md#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466) [SEMIHOST\_OPEN\_AB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466) = 11,

104};

105

[ 114](group__semihost.md#gab8d683d2011f6683956c47a4b129faf4)long [semihost\_exec](group__semihost.md#gab8d683d2011f6683956c47a4b129faf4)(enum [semihost\_instr](group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d) instr, void \*args);

115

[ 121](group__semihost.md#ga4eb7ceb5ceaaded14c3dc129b7fca07b)char [semihost\_poll\_in](group__semihost.md#ga4eb7ceb5ceaaded14c3dc129b7fca07b)(void);

122

[ 128](group__semihost.md#ga4026806d0ea1f6d754851ef7b9f1c58c)void [semihost\_poll\_out](group__semihost.md#ga4026806d0ea1f6d754851ef7b9f1c58c)(char c);

129

[ 140](group__semihost.md#ga497b911ba4e6b40e4e5808fa9484f5a4)long [semihost\_open](group__semihost.md#ga497b911ba4e6b40e4e5808fa9484f5a4)(const char \*path, long mode);

141

[ 150](group__semihost.md#gad8e5d671a2316901eefaf86cac43ac43)long [semihost\_close](group__semihost.md#gad8e5d671a2316901eefaf86cac43ac43)(long fd);

151

[ 160](group__semihost.md#gae7476b25d69979d488e1bbd3521d70e0)long [semihost\_flen](group__semihost.md#gae7476b25d69979d488e1bbd3521d70e0)(long fd);

161

[ 171](group__semihost.md#ga99f88405f4bdc9f43ab2d59b3526ebbc)long [semihost\_seek](group__semihost.md#ga99f88405f4bdc9f43ab2d59b3526ebbc)(long fd, long offset);

172

[ 183](group__semihost.md#gaf0d429779cd2b3a06c29f93f8641e9af)long [semihost\_read](group__semihost.md#gaf0d429779cd2b3a06c29f93f8641e9af)(long fd, void \*buf, long len);

184

[ 195](group__semihost.md#ga6c340fadaa86cddee2817e96caa00edf)long [semihost\_write](group__semihost.md#ga6c340fadaa86cddee2817e96caa00edf)(long fd, const void \*buf, long len);

196

200

201#endif /\* ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SEMIHOST\_H\_ \*/

[semihost\_poll\_out](group__semihost.md#ga4026806d0ea1f6d754851ef7b9f1c58c)

void semihost\_poll\_out(char c)

Write a byte to the console.

[semihost\_open\_mode](group__semihost.md#ga425c53a045590978b0b3235d545780f7)

semihost\_open\_mode

Modes to open a file with.

**Definition** semihost.h:91

[semihost\_open](group__semihost.md#ga497b911ba4e6b40e4e5808fa9484f5a4)

long semihost\_open(const char \*path, long mode)

Open a file on the host system.

[semihost\_poll\_in](group__semihost.md#ga4eb7ceb5ceaaded14c3dc129b7fca07b)

char semihost\_poll\_in(void)

Read a byte from the console.

[semihost\_write](group__semihost.md#ga6c340fadaa86cddee2817e96caa00edf)

long semihost\_write(long fd, const void \*buf, long len)

Write the contents of a buffer into a file.

[semihost\_seek](group__semihost.md#ga99f88405f4bdc9f43ab2d59b3526ebbc)

long semihost\_seek(long fd, long offset)

Seeks to an absolute position in a file.

[semihost\_exec](group__semihost.md#gab8d683d2011f6683956c47a4b129faf4)

long semihost\_exec(enum semihost\_instr instr, void \*args)

Manually execute a semihosting instruction.

[semihost\_close](group__semihost.md#gad8e5d671a2316901eefaf86cac43ac43)

long semihost\_close(long fd)

Close a file.

[semihost\_instr](group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d)

semihost\_instr

Semihosting instructions.

**Definition** semihost.h:27

[semihost\_flen](group__semihost.md#gae7476b25d69979d488e1bbd3521d70e0)

long semihost\_flen(long fd)

Query the size of a file.

[semihost\_read](group__semihost.md#gaf0d429779cd2b3a06c29f93f8641e9af)

long semihost\_read(long fd, void \*buf, long len)

Read the contents of a file into a buffer.

[SEMIHOST\_OPEN\_R\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9)

@ SEMIHOST\_OPEN\_R\_PLUS

**Definition** semihost.h:94

[SEMIHOST\_OPEN\_AB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708)

@ SEMIHOST\_OPEN\_AB

**Definition** semihost.h:101

[SEMIHOST\_OPEN\_W](group__semihost.md#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc)

@ SEMIHOST\_OPEN\_W

**Definition** semihost.h:96

[SEMIHOST\_OPEN\_A](group__semihost.md#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34)

@ SEMIHOST\_OPEN\_A

**Definition** semihost.h:100

[SEMIHOST\_OPEN\_WB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244)

@ SEMIHOST\_OPEN\_WB\_PLUS

**Definition** semihost.h:99

[SEMIHOST\_OPEN\_RB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde)

@ SEMIHOST\_OPEN\_RB

**Definition** semihost.h:93

[SEMIHOST\_OPEN\_A\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f)

@ SEMIHOST\_OPEN\_A\_PLUS

**Definition** semihost.h:102

[SEMIHOST\_OPEN\_WB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc)

@ SEMIHOST\_OPEN\_WB

**Definition** semihost.h:97

[SEMIHOST\_OPEN\_AB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466)

@ SEMIHOST\_OPEN\_AB\_PLUS

**Definition** semihost.h:103

[SEMIHOST\_OPEN\_RB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53)

@ SEMIHOST\_OPEN\_RB\_PLUS

**Definition** semihost.h:95

[SEMIHOST\_OPEN\_R](group__semihost.md#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b)

@ SEMIHOST\_OPEN\_R

**Definition** semihost.h:92

[SEMIHOST\_OPEN\_W\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262)

@ SEMIHOST\_OPEN\_W\_PLUS

**Definition** semihost.h:98

[SEMIHOST\_READ](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02)

@ SEMIHOST\_READ

Read from a file at the current cursor position.

**Definition** semihost.h:39

[SEMIHOST\_OPEN](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46)

@ SEMIHOST\_OPEN

Open a file or stream on the host system.

**Definition** semihost.h:33

[SEMIHOST\_ELAPSED](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367)

@ SEMIHOST\_ELAPSED

**Definition** semihost.h:68

[SEMIHOST\_RENAME](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627)

@ SEMIHOST\_RENAME

Rename a file on the host system.

**Definition** semihost.h:51

[SEMIHOST\_TICKFREQ](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26)

@ SEMIHOST\_TICKFREQ

**Definition** semihost.h:69

[SEMIHOST\_WRITE0](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff)

@ SEMIHOST\_WRITE0

Write a NULL terminated string to the debug terminal.

**Definition** semihost.h:60

[SEMIHOST\_WRITEC](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7)

@ SEMIHOST\_WRITEC

Write one character to the debug terminal.

**Definition** semihost.h:58

[SEMIHOST\_SYSTEM](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a)

@ SEMIHOST\_SYSTEM

**Definition** semihost.h:82

[SEMIHOST\_ISERROR](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea)

@ SEMIHOST\_ISERROR

**Definition** semihost.h:81

[SEMIHOST\_REMOVE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce)

@ SEMIHOST\_REMOVE

Remove a file on the host system.

**Definition** semihost.h:49

[SEMIHOST\_HEAPINFO](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f)

@ SEMIHOST\_HEAPINFO

**Definition** semihost.h:80

[SEMIHOST\_CLOSE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac)

@ SEMIHOST\_CLOSE

Closes a file on the host which has been opened by SEMIHOST\_OPEN.

**Definition** semihost.h:41

[SEMIHOST\_GET\_CMDLINE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f)

@ SEMIHOST\_GET\_CMDLINE

Get commandline parameters for the application to run with.

**Definition** semihost.h:79

[SEMIHOST\_CLOCK](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0)

@ SEMIHOST\_CLOCK

**Definition** semihost.h:67

[SEMIHOST\_WRITE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad)

@ SEMIHOST\_WRITE

Write to a file or stream.

**Definition** semihost.h:37

[SEMIHOST\_SEEK](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629)

@ SEMIHOST\_SEEK

Set the file cursor to a given position in a file.

**Definition** semihost.h:45

[SEMIHOST\_TMPNAM](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb)

@ SEMIHOST\_TMPNAM

Get a temporary absolute file path to create a temporary file.

**Definition** semihost.h:47

[SEMIHOST\_ERRNO](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f)

@ SEMIHOST\_ERRNO

Retrieve the errno variable from semihosting operations.

**Definition** semihost.h:77

[SEMIHOST\_ISTTY](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53)

@ SEMIHOST\_ISTTY

Check whether a file is associated with a stream/terminal.

**Definition** semihost.h:35

[SEMIHOST\_READC](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6)

@ SEMIHOST\_READC

Read one character from the debug terminal.

**Definition** semihost.h:62

[SEMIHOST\_FLEN](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d)

@ SEMIHOST\_FLEN

Get the length of a file.

**Definition** semihost.h:43

[SEMIHOST\_TIME](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438)

@ SEMIHOST\_TIME

**Definition** semihost.h:70

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [semihost.h](semihost_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
