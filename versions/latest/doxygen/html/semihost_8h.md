---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/semihost_8h.html
original_path: doxygen/html/semihost_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

semihost.h File Reference

public Semihosting APIs based on ARM definitions.
[More...](#details)

[Go to the source code of this file.](semihost_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [semihost\_instr](group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d) {     [SEMIHOST\_OPEN](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46) = 0x01 , [SEMIHOST\_ISTTY](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53) = 0x09 , [SEMIHOST\_WRITE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad) = 0x05 , [SEMIHOST\_READ](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02) = 0x06 ,     [SEMIHOST\_CLOSE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac) = 0x02 , [SEMIHOST\_FLEN](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d) = 0x0C , [SEMIHOST\_SEEK](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629) = 0x0A , [SEMIHOST\_TMPNAM](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb) = 0x0D ,     [SEMIHOST\_REMOVE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce) = 0x0E , [SEMIHOST\_RENAME](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627) = 0x0F , [SEMIHOST\_WRITEC](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7) = 0x03 , [SEMIHOST\_WRITE0](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff) = 0x04 ,     [SEMIHOST\_READC](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6) = 0x07 , [SEMIHOST\_CLOCK](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0) = 0x10 , [SEMIHOST\_ELAPSED](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367) = 0x30 , [SEMIHOST\_TICKFREQ](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26) = 0x31 ,     [SEMIHOST\_TIME](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438) = 0x11 , [SEMIHOST\_ERRNO](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f) = 0x13 , [SEMIHOST\_GET\_CMDLINE](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f) = 0x15 , [SEMIHOST\_HEAPINFO](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f) = 0x16 ,     [SEMIHOST\_ISERROR](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea) = 0x08 , [SEMIHOST\_SYSTEM](group__semihost.md#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a) = 0x12   } |
|  | Semihosting instructions. [More...](group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d) |
| enum | [semihost\_open\_mode](group__semihost.md#ga425c53a045590978b0b3235d545780f7) {     [SEMIHOST\_OPEN\_R](group__semihost.md#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b) = 0 , [SEMIHOST\_OPEN\_RB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde) = 1 , [SEMIHOST\_OPEN\_R\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9) = 2 , [SEMIHOST\_OPEN\_RB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53) = 3 ,     [SEMIHOST\_OPEN\_W](group__semihost.md#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc) = 4 , [SEMIHOST\_OPEN\_WB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc) = 5 , [SEMIHOST\_OPEN\_W\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262) = 6 , [SEMIHOST\_OPEN\_WB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244) = 7 ,     [SEMIHOST\_OPEN\_A](group__semihost.md#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34) = 8 , [SEMIHOST\_OPEN\_AB](group__semihost.md#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708) = 9 , [SEMIHOST\_OPEN\_A\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f) = 10 , [SEMIHOST\_OPEN\_AB\_PLUS](group__semihost.md#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466) = 11   } |
|  | Modes to open a file with. [More...](group__semihost.md#ga425c53a045590978b0b3235d545780f7) |

| Functions | |
| --- | --- |
| long | [semihost\_exec](group__semihost.md#gab8d683d2011f6683956c47a4b129faf4) (enum [semihost\_instr](group__semihost.md#gadf61e00be557b7cb4457f7ea6f8da86d) instr, void \*args) |
|  | Manually execute a semihosting instruction. |
| char | [semihost\_poll\_in](group__semihost.md#ga4eb7ceb5ceaaded14c3dc129b7fca07b) (void) |
|  | Read a byte from the console. |
| void | [semihost\_poll\_out](group__semihost.md#ga4026806d0ea1f6d754851ef7b9f1c58c) (char c) |
|  | Write a byte to the console. |
| long | [semihost\_open](group__semihost.md#ga497b911ba4e6b40e4e5808fa9484f5a4) (const char \*path, long mode) |
|  | Open a file on the host system. |
| long | [semihost\_close](group__semihost.md#gad8e5d671a2316901eefaf86cac43ac43) (long fd) |
|  | Close a file. |
| long | [semihost\_flen](group__semihost.md#gae7476b25d69979d488e1bbd3521d70e0) (long fd) |
|  | Query the size of a file. |
| long | [semihost\_seek](group__semihost.md#ga99f88405f4bdc9f43ab2d59b3526ebbc) (long fd, long offset) |
|  | Seeks to an absolute position in a file. |
| long | [semihost\_read](group__semihost.md#gaf0d429779cd2b3a06c29f93f8641e9af) (long fd, void \*buf, long len) |
|  | Read the contents of a file into a buffer. |
| long | [semihost\_write](group__semihost.md#ga6c340fadaa86cddee2817e96caa00edf) (long fd, const void \*buf, long len) |
|  | Write the contents of a buffer into a file. |

## Detailed Description

public Semihosting APIs based on ARM definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [semihost.h](semihost_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
