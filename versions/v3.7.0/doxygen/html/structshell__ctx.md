---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell__ctx.html
original_path: doxygen/html/structshell__ctx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_ctx Struct Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

Shell instance context.
[More...](#details)

`#include <[shell.h](shell_2shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [prompt](#a261d4754f4bf3764298e264ed6e87eff) |
| enum [shell\_state](group__shell__api.md#gaf2c6ff9ef31dc06086fd1141763e6266) | [state](#a7388fd2e850fcf37c4a421cda13661e8) |
|  | Internal module state. |
| enum [shell\_receive\_state](group__shell__api.md#ga8773ed2570714ba4985108b1738d33a0) | [receive\_state](#abc4135f23c4738fcf6a2c9d8f45d516b) |
|  | Escape sequence indicator. |
| struct [shell\_static\_entry](structshell__static__entry.md) | [active\_cmd](#a3df8f9a293b4c24d81a80af2d0e0c44e) |
|  | Currently executed command. |
| const struct [shell\_static\_entry](structshell__static__entry.md) \* | [selected\_cmd](#a0e9321e8954a7598cb6521f660480a88) |
|  | New root command. |
| struct [shell\_vt100\_ctx](structshell__vt100__ctx.md) | [vt100\_ctx](#a25b945fcaba216e039124aacec660600) |
|  | VT100 color and cursor position, terminal width. |
| [shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25) | [uninit\_cb](#a0ec61f11544cb817bbd46ed4aa332123) |
|  | Callback called from shell thread context when unitialization is completed just before aborting shell thread. |
| [shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d) | [bypass](#a8e02d1d9a521379ad4188b4678cc6071) |
|  | When bypass is set, all incoming data is passed to the callback. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_level](#a3e6374150abdb9cd4875024eb6f7c5ea) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cmd\_buff\_len](#a948d78719efe7f01b8edf151e1435af6) |
|  | Command length. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cmd\_buff\_pos](#a9a8f69e6876e4788ef3961dfb769e53f) |
|  | Command buffer cursor position. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cmd\_tmp\_buff\_len](#a5dfe5d3b2e27b67a7a78d5c3ad32ff1d) |
|  | Command length in tmp buffer. |
| char | [cmd\_buff](#a385014f2fba5cae182c3520ec934cce6) [0] |
|  | Command input buffer. |
| char | [temp\_buff](#a35085b30e92b913b16f02496c5ec6375) [0] |
|  | Command temporary buffer. |
| char | [printf\_buff](#aba89a1995fe33838d508810e60c7ea79) [0] |
|  | Printf buffer size. |
| volatile union [shell\_backend\_cfg](unionshell__backend__cfg.md) | [cfg](#a5437653e57909910df742c80562c1c83) |
| volatile union [shell\_backend\_ctx](unionshell__backend__ctx.md) | [ctx](#ac9bed826ec7421065e6bc6e12ad213ce) |
| struct [k\_poll\_signal](structk__poll__signal.md) | [signals](#a6d96ff92952aebed16ebf288fe0a96db) [[SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)] |
| struct [k\_poll\_event](structk__poll__event.md) | [events](#abbbc94a651bfc56d5b0916e1516c3842) [[SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)] |
|  | Events that should be used only internally by shell thread. |
| struct [k\_mutex](structk__mutex.md) | [wr\_mtx](#a76cf861f17057cf080c54b67acb1a801) |
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [tid](#a2cab9b799462a9f6eea898f7076f204f) |
| int | [ret\_val](#aab37b8261e69af3dfe3e4ae19de06792) |

## Detailed Description

Shell instance context.

## Field Documentation

## [◆ ](#a3df8f9a293b4c24d81a80af2d0e0c44e)active\_cmd

| struct [shell\_static\_entry](structshell__static__entry.md) shell\_ctx::active\_cmd |
| --- |

Currently executed command.

## [◆ ](#a8e02d1d9a521379ad4188b4678cc6071)bypass

| [shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d) shell\_ctx::bypass |
| --- |

When bypass is set, all incoming data is passed to the callback.

Logging level for a backend.

## [◆ ](#a5437653e57909910df742c80562c1c83)cfg

| volatile union [shell\_backend\_cfg](unionshell__backend__cfg.md) shell\_ctx::cfg |
| --- |

## [◆ ](#a385014f2fba5cae182c3520ec934cce6)cmd\_buff

| char shell\_ctx::cmd\_buff[0] |
| --- |

Command input buffer.

## [◆ ](#a948d78719efe7f01b8edf151e1435af6)cmd\_buff\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_ctx::cmd\_buff\_len |
| --- |

Command length.

## [◆ ](#a9a8f69e6876e4788ef3961dfb769e53f)cmd\_buff\_pos

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_ctx::cmd\_buff\_pos |
| --- |

Command buffer cursor position.

## [◆ ](#a5dfe5d3b2e27b67a7a78d5c3ad32ff1d)cmd\_tmp\_buff\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_ctx::cmd\_tmp\_buff\_len |
| --- |

Command length in tmp buffer.

## [◆ ](#ac9bed826ec7421065e6bc6e12ad213ce)ctx

| volatile union [shell\_backend\_ctx](unionshell__backend__ctx.md) shell\_ctx::ctx |
| --- |

## [◆ ](#abbbc94a651bfc56d5b0916e1516c3842)events

| struct [k\_poll\_event](structk__poll__event.md) shell\_ctx::events[[SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)] |
| --- |

Events that should be used only internally by shell thread.

Event for SHELL\_SIGNAL\_TXDONE is initialized but unused.

## [◆ ](#a3e6374150abdb9cd4875024eb6f7c5ea)log\_level

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_ctx::log\_level |
| --- |

## [◆ ](#aba89a1995fe33838d508810e60c7ea79)printf\_buff

| char shell\_ctx::printf\_buff[0] |
| --- |

Printf buffer size.

## [◆ ](#a261d4754f4bf3764298e264ed6e87eff)prompt

| const char\* shell\_ctx::prompt |
| --- |

## [◆ ](#abc4135f23c4738fcf6a2c9d8f45d516b)receive\_state

| enum [shell\_receive\_state](group__shell__api.md#ga8773ed2570714ba4985108b1738d33a0) shell\_ctx::receive\_state |
| --- |

Escape sequence indicator.

## [◆ ](#aab37b8261e69af3dfe3e4ae19de06792)ret\_val

| int shell\_ctx::ret\_val |
| --- |

## [◆ ](#a0e9321e8954a7598cb6521f660480a88)selected\_cmd

| const struct [shell\_static\_entry](structshell__static__entry.md)\* shell\_ctx::selected\_cmd |
| --- |

New root command.

If NULL shell uses default root commands.

## [◆ ](#a6d96ff92952aebed16ebf288fe0a96db)signals

| struct [k\_poll\_signal](structk__poll__signal.md) shell\_ctx::signals[[SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)] |
| --- |

## [◆ ](#a7388fd2e850fcf37c4a421cda13661e8)state

| enum [shell\_state](group__shell__api.md#gaf2c6ff9ef31dc06086fd1141763e6266) shell\_ctx::state |
| --- |

Internal module state.

## [◆ ](#a35085b30e92b913b16f02496c5ec6375)temp\_buff

| char shell\_ctx::temp\_buff[0] |
| --- |

Command temporary buffer.

## [◆ ](#a2cab9b799462a9f6eea898f7076f204f)tid

| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) shell\_ctx::tid |
| --- |

## [◆ ](#a0ec61f11544cb817bbd46ed4aa332123)uninit\_cb

| [shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25) shell\_ctx::uninit\_cb |
| --- |

Callback called from shell thread context when unitialization is completed just before aborting shell thread.

## [◆ ](#a25b945fcaba216e039124aacec660600)vt100\_ctx

| struct [shell\_vt100\_ctx](structshell__vt100__ctx.md) shell\_ctx::vt100\_ctx |
| --- |

VT100 color and cursor position, terminal width.

## [◆ ](#a76cf861f17057cf080c54b67acb1a801)wr\_mtx

| struct [k\_mutex](structk__mutex.md) shell\_ctx::wr\_mtx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell\_ctx](structshell__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
