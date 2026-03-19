---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__shell__api.html
original_path: doxygen/html/group__shell__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Shell API

[Operating System Services](group__os__services.md)

Shell API.
[More...](#details)

| Data Structures | |
| --- | --- |
| union | [shell\_cmd\_entry](unionshell__cmd__entry.md) |
|  | Shell command descriptor. [More...](unionshell__cmd__entry.md#details) |
| struct | [shell\_static\_args](structshell__static__args.md) |
| struct | [shell\_static\_entry](structshell__static__entry.md) |
| struct | [shell\_transport\_api](structshell__transport__api.md) |
|  | Unified shell transport interface. [More...](structshell__transport__api.md#details) |
| struct | [shell\_transport](structshell__transport.md) |
| struct | [shell\_stats](structshell__stats.md) |
|  | Shell statistics structure. [More...](structshell__stats.md#details) |
| struct | [shell\_backend\_config\_flags](structshell__backend__config__flags.md) |
| struct | [shell\_backend\_ctx\_flags](structshell__backend__ctx__flags.md) |
| union | [shell\_backend\_cfg](unionshell__backend__cfg.md) |
| union | [shell\_backend\_ctx](unionshell__backend__ctx.md) |
| struct | [shell\_ctx](structshell__ctx.md) |
|  | Shell instance context. [More...](structshell__ctx.md#details) |
| struct | [shell](structshell.md) |
|  | Shell instance internals. [More...](structshell.md#details) |

| Macros | |
| --- | --- |
| #define | [SHELL\_CMD\_ARG\_REGISTER](#gae8a8bbcbb842027c02a319b3fb976a3d)(syntax, subcmd, help, handler, mandatory, optional) |
|  | Macro for defining and adding a root command (level 0) with required number of arguments. |
| #define | [SHELL\_COND\_CMD\_ARG\_REGISTER](#ga6a3ed4ea9051ac138d22cc39134fb2e5)(flag, syntax, subcmd, help, handler, mandatory, optional) |
|  | Macro for defining and adding a conditional root command (level 0) with required number of arguments. |
| #define | [SHELL\_CMD\_REGISTER](#ga06060b98eb505300a3dcc8f922a8e7ab)(syntax, subcmd, help, handler) |
|  | Macro for defining and adding a root command (level 0) with arguments. |
| #define | [SHELL\_COND\_CMD\_REGISTER](#ga62782121ece6af076407c94935ec94e4)(flag, syntax, subcmd, help, handler) |
|  | Macro for defining and adding a conditional root command (level 0) with arguments. |
| #define | [SHELL\_STATIC\_SUBCMD\_SET\_CREATE](#gacb2d1a969368efdbeec704ee6e962dee)(name, ...) |
|  | Macro for creating a subcommand set. |
| #define | [SHELL\_SUBCMD\_SET\_CREATE](#ga1e314886b70ee2e7e0763cd945a1a988)(\_name, \_parent) |
|  | Create set of subcommands. |
| #define | [SHELL\_SUBCMD\_COND\_ADD](#gab1b643efbaee748be0256e904642e310)(\_flag, \_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt) |
|  | Conditionally add command to the set of subcommands. |
| #define | [SHELL\_SUBCMD\_ADD](#ga85b0afcacd3831bf5c724590765e035f)(\_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt) |
|  | Add command to the set of subcommands. |
| #define | [SHELL\_SUBCMD\_SET\_END](#ga4f7a3432f76541eb226a426507e10174)   {NULL} |
|  | Define ending subcommands set. |
| #define | [SHELL\_DYNAMIC\_CMD\_CREATE](#gafa6d91c36c36eb68d3f241ed0c7e7131)(name, get) |
|  | Macro for creating a dynamic entry. |
| #define | [SHELL\_CMD\_ARG](#gad762c496a2ced65069b6d1d02a4d925c)(syntax, subcmd, help, handler, mand, opt) |
|  | Initializes a shell command with arguments. |
| #define | [SHELL\_COND\_CMD\_ARG](#ga68229f89484c3459d77cebb450ee1f24)(flag, syntax, subcmd, help, handler, mand, opt) |
|  | Initializes a conditional shell command with arguments. |
| #define | [SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9)(\_expr, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt) |
|  | Initializes a conditional shell command with arguments if expression gives non-zero result at compile time. |
| #define | [SHELL\_CMD](#ga24ade9db85af9a8776a45ba0084f4cca)(\_syntax, \_subcmd, \_help, \_handler) |
|  | Initializes a shell command. |
| #define | [SHELL\_COND\_CMD](#ga6e27d86443067df4792623f1a04d1ee1)(\_flag, \_syntax, \_subcmd, \_help, \_handler) |
|  | Initializes a conditional shell command. |
| #define | [SHELL\_EXPR\_CMD](#ga59a835edbd7db3acdcb204248c0cf5fd)(\_expr, \_syntax, \_subcmd, \_help, \_handler) |
|  | Initializes shell command if expression gives non-zero result at compile time. |
| #define | [SHELL\_CMD\_DICT\_CREATE](#gaf33b1b20caccad1effe6733603259a00)(\_data, \_handler) |
| #define | [SHELL\_SUBCMD\_DICT\_SET\_CREATE](#ga401e19cf8ec8601b8a96fe8e95a2b4d2)(\_name, \_handler, ...) |
|  | Initializes shell dictionary commands. |
| #define | [SHELL\_DEFAULT\_BACKEND\_CONFIG\_FLAGS](#ga7e522b107d4e8b687816a86f14b9a885) |
| #define | [SHELL\_DEFINE](#ga158405143b49e4888cb135fec83ad22c)(\_name, \_prompt, \_transport\_iface, \_log\_queue\_size, \_log\_timeout, \_shell\_flag) |
|  | Macro for defining a shell instance. |
| #define | [SHELL\_NORMAL](#ga4c3a7db0c2bdbf36bbf72302a04bb44d)   [SHELL\_VT100\_COLOR\_DEFAULT](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e) |
|  | Terminal default text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_INFO](#gaac0ea96fbb5885432dca93174c9ad4e6)   [SHELL\_VT100\_COLOR\_GREEN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a) |
|  | Green text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_OPTION](#gacc7c6e7b1fc65cc350353cc166da528b)   [SHELL\_VT100\_COLOR\_CYAN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972) |
|  | Cyan text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_WARNING](#ga118dd6829e092423a85e2b6de07f8dd3)   [SHELL\_VT100\_COLOR\_YELLOW](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d) |
|  | Yellow text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_ERROR](#ga7664f5e184e9b41ac92e033f7b8d885d)   [SHELL\_VT100\_COLOR\_RED](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4) |
|  | Red text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [shell\_fprintf](#ga1fd1671311b112f0c87ab2dafd801105)(sh, color, fmt, ...) |
| #define | [shell\_info](#ga9382959c41fe6850c2daa51306b3c5fd)(\_sh, \_ft, ...) |
|  | Print info message to the shell. |
| #define | [shell\_print](#ga3126019b2100d1ccb2d4dc5efb7d8228)(\_sh, \_ft, ...) |
|  | Print normal message to the shell. |
| #define | [shell\_warn](#ga3d886cfd7b4340b2e71a92bd7c4534d9)(\_sh, \_ft, ...) |
|  | Print warning message to the shell. |
| #define | [shell\_error](#ga408141c02209a9549cb9063f24ef3731)(\_sh, \_ft, ...) |
|  | Print error message to the shell. |
| #define | [SHELL\_CMD\_HELP\_PRINTED](#ga3be3ecccd6ce1954883c5959c39c7927)   (1) |
|  | Command's help has been printed. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [shell\_dynamic\_get](#gafc042f32bac2fdd4cbde9f943e29b008)) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) idx, struct [shell\_static\_entry](structshell__static__entry.md) \*entry) |
|  | Shell dynamic command descriptor. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [shell\_device\_filter\_t](#gaa2b8cf8ac78b8355408ef94958ebdc70)) (const struct [device](structdevice.md) \*dev) |
|  | Filter callback type, for use with shell\_device\_lookup\_filter. |
| typedef int(\* | [shell\_cmd\_handler](#ga331e7d19b9b0755486596f5ffc598338)) (const struct [shell](structshell.md) \*sh, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) argc, char \*\*argv) |
|  | Shell command handler prototype. |
| typedef int(\* | [shell\_dict\_cmd\_handler](#ga182f247052041f1236d13726589885e2)) (const struct [shell](structshell.md) \*sh, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) argc, char \*\*argv, void \*data) |
|  | Shell dictionary command handler prototype. |
| typedef void(\* | [shell\_transport\_handler\_t](#ga265807c2d8eba7b9ea633968627e085d)) (enum [shell\_transport\_evt](#gae77673d4c086f2f9312ceb7933745ee1) evt, void \*context) |
| typedef void(\* | [shell\_uninit\_cb\_t](#ga0844a0ce151551d3ccf45d507e5bab25)) (const struct [shell](structshell.md) \*sh, int res) |
| typedef void(\* | [shell\_bypass\_cb\_t](#gab1dafbf90c42b7d4601122e1b9eabf3d)) (const struct [shell](structshell.md) \*sh, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bypass callback. |

| Enumerations | |
| --- | --- |
| enum | [shell\_receive\_state](#ga8773ed2570714ba4985108b1738d33a0) { [SHELL\_RECEIVE\_DEFAULT](#gga8773ed2570714ba4985108b1738d33a0a201e367896f86499d317d9ec7b59612a) , [SHELL\_RECEIVE\_ESC](#gga8773ed2570714ba4985108b1738d33a0ab512e3269698524fd025433016b3ad65) , [SHELL\_RECEIVE\_ESC\_SEQ](#gga8773ed2570714ba4985108b1738d33a0a7378b6ecb1a51c53577db5a8eeda936a) , [SHELL\_RECEIVE\_TILDE\_EXP](#gga8773ed2570714ba4985108b1738d33a0afa2dde3374d3971266652cf48a4d13f7) } |
| enum | [shell\_state](#gaf2c6ff9ef31dc06086fd1141763e6266) {     [SHELL\_STATE\_UNINITIALIZED](#ggaf2c6ff9ef31dc06086fd1141763e6266a0fcbee7b51ec8d90e7d42a1b455360e6) , [SHELL\_STATE\_INITIALIZED](#ggaf2c6ff9ef31dc06086fd1141763e6266adf8c97c3b6dacfbaf3ace4780cfe3dbd) , [SHELL\_STATE\_ACTIVE](#ggaf2c6ff9ef31dc06086fd1141763e6266a8a226ad5c1306dd8f491ad321d334b72) , [SHELL\_STATE\_PANIC\_MODE\_ACTIVE](#ggaf2c6ff9ef31dc06086fd1141763e6266a8d01930f8cbdeddda2bf47d0264c4a8b) ,     [SHELL\_STATE\_PANIC\_MODE\_INACTIVE](#ggaf2c6ff9ef31dc06086fd1141763e6266a6423704f7a619e1bfed063cd7455ebfe)   } |
| enum | [shell\_transport\_evt](#gae77673d4c086f2f9312ceb7933745ee1) { [SHELL\_TRANSPORT\_EVT\_RX\_RDY](#ggae77673d4c086f2f9312ceb7933745ee1aa43ab5965bc3f2c964f206277ab3f1bb) , [SHELL\_TRANSPORT\_EVT\_TX\_RDY](#ggae77673d4c086f2f9312ceb7933745ee1a6c78a3534128fac6366d9e5dfda81dfb) } |
|  | Shell transport event. [More...](#gae77673d4c086f2f9312ceb7933745ee1) |
| enum | [shell\_signal](#ga5cd015de5e7295483fa2cff7d54c2d21) {     [SHELL\_SIGNAL\_RXRDY](#gga5cd015de5e7295483fa2cff7d54c2d21a815c6760bfd5bba8813ea68964bf4713) , [SHELL\_SIGNAL\_LOG\_MSG](#gga5cd015de5e7295483fa2cff7d54c2d21ab8fe52f7b4f43c98dae5188a1dc8547a) , [SHELL\_SIGNAL\_KILL](#gga5cd015de5e7295483fa2cff7d54c2d21ad5c07b5872f785b0731c8aaed0f81c3a) , [SHELL\_SIGNAL\_TXDONE](#gga5cd015de5e7295483fa2cff7d54c2d21a7962ab077b49c816bb9337a9b1b343ed) ,     [SHELL\_SIGNALS](#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)   } |
| enum | [shell\_flag](#ga56bf30741f9ec7a6d94e5c18c2858948) { [SHELL\_FLAG\_CRLF\_DEFAULT](#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab) = (1<<0) , [SHELL\_FLAG\_OLF\_CRLF](#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446) = (1<<1) } |
|  | Flags for setting shell output newline sequence. [More...](#ga56bf30741f9ec7a6d94e5c18c2858948) |

| Functions | |
| --- | --- |
| const struct [device](structdevice.md) \* | [shell\_device\_lookup](#ga571db3aa3e024a09e82b117a74d6f248) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) idx, const char \*prefix) |
|  | Get by index a device that matches . |
| const struct [device](structdevice.md) \* | [shell\_device\_filter](#gae2a8e3d44a9bf5eb55be80833ac6eb5d) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) idx, [shell\_device\_filter\_t](#gaa2b8cf8ac78b8355408ef94958ebdc70) filter) |
|  | Get a device by index and filter. |
| int | [shell\_init](#ga8764ff11603855a10419c48e46e8221c) (const struct [shell](structshell.md) \*sh, const void \*transport\_config, struct [shell\_backend\_config\_flags](structshell__backend__config__flags.md) cfg\_flags, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [log\_backend](structlog__backend.md), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) init\_log\_level) |
|  | Function for initializing a transport layer and internal shell state. |
| void | [shell\_uninit](#ga07e76646c5065218464aa8ce78b75af3) (const struct [shell](structshell.md) \*sh, [shell\_uninit\_cb\_t](#ga0844a0ce151551d3ccf45d507e5bab25) cb) |
|  | Uninitializes the transport layer and the internal shell state. |
| int | [shell\_start](#gad386d4e8077103e7976f25996fcc3132) (const struct [shell](structshell.md) \*sh) |
|  | Function for starting shell processing. |
| int | [shell\_stop](#gad27754d0beb31bc501f28f9ef26a362c) (const struct [shell](structshell.md) \*sh) |
|  | Function for stopping shell processing. |
| void | [shell\_fprintf\_impl](#ga863c04af5db00a3804eaff02d401603b) (const struct [shell](structshell.md) \*sh, enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) color, const char \*fmt,...) |
|  | printf-like function which sends formatted data stream to the shell. |
| void | [shell\_vfprintf](#ga74a1c4edd803cad14c893fc9816e534f) (const struct [shell](structshell.md) \*sh, enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) color, const char \*fmt, va\_list args) |
|  | vprintf-like function which sends formatted data stream to the shell. |
| void | [shell\_hexdump\_line](#ga0b6e69b499c153ae8f7ba256d445f09d) (const struct [shell](structshell.md) \*sh, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Print a line of data in hexadecimal format. |
| void | [shell\_hexdump](#gaeeba0b483974205c54e364d509badd42) (const struct [shell](structshell.md) \*sh, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Print data in hexadecimal format. |
| void | [shell\_fprintf\_info](#ga30fcc10f13ce8d850f2c1c5de4533a29) (const struct [shell](structshell.md) \*sh, const char \*fmt,...) |
| void | [shell\_fprintf\_normal](#ga67f638ebc05f8300553e5e6c1771380d) (const struct [shell](structshell.md) \*sh, const char \*fmt,...) |
| void | [shell\_fprintf\_warn](#ga9c9ced10bf376a5514b8b0bb55e1efcd) (const struct [shell](structshell.md) \*sh, const char \*fmt,...) |
| void | [shell\_fprintf\_error](#ga427d7f51d99aec311348f836d9007df7) (const struct [shell](structshell.md) \*sh, const char \*fmt,...) |
| void | [shell\_process](#ga7e66389d0faf15a2a7c31c68cdd9c36c) (const struct [shell](structshell.md) \*sh) |
|  | Process function, which should be executed when data is ready in the transport interface. |
| int | [shell\_prompt\_change](#ga2113b7227b155755a7ab8a928f7ae499) (const struct [shell](structshell.md) \*sh, const char \*prompt) |
|  | Change displayed shell prompt. |
| void | [shell\_help](#gac3c643a0b332cd2f07fe506337784ac0) (const struct [shell](structshell.md) \*sh) |
|  | Prints the current command help. |
| int | [shell\_execute\_cmd](#gabfb6a1f1f53f90365de349348015311e) (const struct [shell](structshell.md) \*sh, const char \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Execute command. |
| int | [shell\_set\_root\_cmd](#ga768c606f2d50f24e9b607ba0a341686d) (const char \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Set root command for all shell instances. |
| void | [shell\_set\_bypass](#ga7514a072c2819fb93fb9d62542c7cc15) (const struct [shell](structshell.md) \*sh, [shell\_bypass\_cb\_t](#gab1dafbf90c42b7d4601122e1b9eabf3d) bypass) |
|  | Set bypass callback. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [shell\_ready](#ga79369ddfea2dc2cb5813c5eb5c67634a) (const struct [shell](structshell.md) \*sh) |
|  | Get shell readiness to execute commands. |
| int | [shell\_insert\_mode\_set](#gaf1f41d8b6cd430357d593ab0fc5adfeb) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control text insert mode. |
| int | [shell\_use\_colors\_set](#ga7d5873456ba43ebd3cc86d25e3f4a72c) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether terminal output uses colored syntax. |
| int | [shell\_use\_vt100\_set](#ga80ff4b3b4cc62e543fd510c14f55b42a) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether terminal is using vt100 commands. |
| int | [shell\_echo\_set](#gad53881371bbaedfd3ef3ecf219706fd1) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether user input is echoed back. |
| int | [shell\_obscure\_set](#ga86fade2757d04c9220d5912a4ee540a0) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) obscure) |
|  | Allow application to control whether user input is obscured with asterisks – useful for implementing passwords. |
| int | [shell\_mode\_delete\_set](#ga2df2997c4b04f3246c22f43b274a353b) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether the delete key backspaces or deletes. |
| int | [shell\_get\_return\_value](#ga54dc053c92641bc9b9736bc2d61140f7) (const struct [shell](structshell.md) \*sh) |
|  | Retrieve return value of most recently executed shell command. |

| Variables | |
| --- | --- |
| const struct [log\_backend\_api](structlog__backend__api.md) | [log\_backend\_shell\_api](#gaddf27615ed72440ecb63aa1d84962c82) |

## Detailed Description

Shell API.

Since
:   1.14

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga24ade9db85af9a8776a45ba0084f4cca)SHELL\_CMD

| #define SHELL\_CMD | ( |  | *\_syntax*, |
| --- | --- | --- | --- |
|  |  |  | *\_subcmd*, |
|  |  |  | *\_help*, |
|  |  |  | *\_handler* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_CMD\_ARG](#gad762c496a2ced65069b6d1d02a4d925c)(\_syntax, \_subcmd, \_help, \_handler, 0, 0)

[SHELL\_CMD\_ARG](#gad762c496a2ced65069b6d1d02a4d925c)

#define SHELL\_CMD\_ARG(syntax, subcmd, help, handler, mand, opt)

Initializes a shell command with arguments.

**Definition** shell.h:441

Initializes a shell command.

Parameters
:   | [in] | \_syntax | Command syntax (for example: history). |
    | --- | --- | --- |
    | [in] | \_subcmd | Pointer to a subcommands array. |
    | [in] | \_help | Pointer to a command help string. |
    | [in] | \_handler | Pointer to a function handler. |

## [◆ ](#gad762c496a2ced65069b6d1d02a4d925c)SHELL\_CMD\_ARG

| #define SHELL\_CMD\_ARG | ( |  | *syntax*, |
| --- | --- | --- | --- |
|  |  |  | *subcmd*, |
|  |  |  | *help*, |
|  |  |  | *handler*, |
|  |  |  | *mand*, |
|  |  |  | *opt* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9)(1, syntax, subcmd, help, handler, mand, opt)

[SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9)

#define SHELL\_EXPR\_CMD\_ARG(\_expr, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt)

Initializes a conditional shell command with arguments if expression gives non-zero result at compile...

**Definition** shell.h:486

Initializes a shell command with arguments.

Note
:   If a command will be called with wrong number of arguments shell will print an error message and command handler will not be called.

Parameters
:   | [in] | syntax | Command syntax (for example: history). |
    | --- | --- | --- |
    | [in] | subcmd | Pointer to a subcommands array. |
    | [in] | help | Pointer to a command help string. |
    | [in] | handler | Pointer to a function handler. |
    | [in] | mand | Number of mandatory arguments including command name. |
    | [in] | opt | Number of optional arguments. |

## [◆ ](#gae8a8bbcbb842027c02a319b3fb976a3d)SHELL\_CMD\_ARG\_REGISTER

| #define SHELL\_CMD\_ARG\_REGISTER | ( |  | *syntax*, |
| --- | --- | --- | --- |
|  |  |  | *subcmd*, |
|  |  |  | *help*, |
|  |  |  | *handler*, |
|  |  |  | *mandatory*, |
|  |  |  | *optional* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

static const struct [shell\_static\_entry](structshell__static__entry.md) [UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(\_shell\_, syntax) = \

SHELL\_CMD\_ARG(syntax, subcmd, help, handler, mandatory, optional); \

static const [TYPE\_SECTION\_ITERABLE](group__iterable__section__apis.md#gac5177fefd615bdd3025fac742d414808)(union [shell\_cmd\_entry](unionshell__cmd__entry.md), \

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(shell\_cmd\_, syntax), shell\_root\_cmds, \

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(shell\_cmd\_, syntax) \

) = { \

.entry = &[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(\_shell\_, syntax) \

}

[TYPE\_SECTION\_ITERABLE](group__iterable__section__apis.md#gac5177fefd615bdd3025fac742d414808)

#define TYPE\_SECTION\_ITERABLE(type, varname, secname, section\_postfix)

Defines a new element for an iterable section for a generic type.

**Definition** iterable\_sections.h:42

[shell\_static\_entry](structshell__static__entry.md)

**Definition** shell.h:206

[shell\_cmd\_entry](unionshell__cmd__entry.md)

Shell command descriptor.

**Definition** shell.h:101

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Macro for defining and adding a root command (level 0) with required number of arguments.

Note
:   Each root command shall have unique syntax. If a command will be called with wrong number of arguments shell will print an error message and command handler will not be called.

Parameters
:   | [in] | syntax | Command syntax (for example: history). |
    | --- | --- | --- |
    | [in] | subcmd | Pointer to a subcommands array. |
    | [in] | help | Pointer to a command help string. |
    | [in] | handler | Pointer to a function handler. |
    | [in] | mandatory | Number of mandatory arguments including command name. |
    | [in] | optional | Number of optional arguments. |

## [◆ ](#gaf33b1b20caccad1effe6733603259a00)SHELL\_CMD\_DICT\_CREATE

| #define SHELL\_CMD\_DICT\_CREATE | ( |  | *\_data*, |
| --- | --- | --- | --- |
|  |  |  | *\_handler* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_CMD\_ARG](#gad762c496a2ced65069b6d1d02a4d925c)([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_DEBRACKET \_data), NULL, [GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(3, \_\_DEBRACKET \_data), \

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(cmd\_dict\_, [UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(\_handler, \_)), \

[GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_DEBRACKET \_data)), 1, 0)

[GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)

#define GET\_ARG\_N(N,...)

Get nth argument from argument list.

**Definition** util\_macro.h:371

## [◆ ](#ga3be3ecccd6ce1954883c5959c39c7927)SHELL\_CMD\_HELP\_PRINTED

| #define SHELL\_CMD\_HELP\_PRINTED   (1) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Command's help has been printed.

## [◆ ](#ga06060b98eb505300a3dcc8f922a8e7ab)SHELL\_CMD\_REGISTER

| #define SHELL\_CMD\_REGISTER | ( |  | *syntax*, |
| --- | --- | --- | --- |
|  |  |  | *subcmd*, |
|  |  |  | *help*, |
|  |  |  | *handler* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_CMD\_ARG\_REGISTER](#gae8a8bbcbb842027c02a319b3fb976a3d)(syntax, subcmd, help, handler, 0, 0)

[SHELL\_CMD\_ARG\_REGISTER](#gae8a8bbcbb842027c02a319b3fb976a3d)

#define SHELL\_CMD\_ARG\_REGISTER(syntax, subcmd, help, handler, mandatory, optional)

Macro for defining and adding a root command (level 0) with required number of arguments.

**Definition** shell.h:230

Macro for defining and adding a root command (level 0) with arguments.

Note
:   All root commands must have different name.

Parameters
:   | [in] | syntax | Command syntax (for example: history). |
    | --- | --- | --- |
    | [in] | subcmd | Pointer to a subcommands array. |
    | [in] | help | Pointer to a command help string. |
    | [in] | handler | Pointer to a function handler. |

## [◆ ](#ga6e27d86443067df4792623f1a04d1ee1)SHELL\_COND\_CMD

| #define SHELL\_COND\_CMD | ( |  | *\_flag*, |
| --- | --- | --- | --- |
|  |  |  | *\_syntax*, |
|  |  |  | *\_subcmd*, |
|  |  |  | *\_help*, |
|  |  |  | *\_handler* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_COND\_CMD\_ARG](#ga68229f89484c3459d77cebb450ee1f24)(\_flag, \_syntax, \_subcmd, \_help, \_handler, 0, 0)

[SHELL\_COND\_CMD\_ARG](#ga68229f89484c3459d77cebb450ee1f24)

#define SHELL\_COND\_CMD\_ARG(flag, syntax, subcmd, help, handler, mand, opt)

Initializes a conditional shell command with arguments.

**Definition** shell.h:463

Initializes a conditional shell command.

See also
:   [SHELL\_COND\_CMD\_ARG](#ga68229f89484c3459d77cebb450ee1f24).

Parameters
:   | [in] | \_flag | Compile time flag. Command is present only if flag exists and equals 1. |
    | --- | --- | --- |
    | [in] | \_syntax | Command syntax (for example: history). |
    | [in] | \_subcmd | Pointer to a subcommands array. |
    | [in] | \_help | Pointer to a command help string. |
    | [in] | \_handler | Pointer to a function handler. |

## [◆ ](#ga68229f89484c3459d77cebb450ee1f24)SHELL\_COND\_CMD\_ARG

| #define SHELL\_COND\_CMD\_ARG | ( |  | *flag*, |
| --- | --- | --- | --- |
|  |  |  | *syntax*, |
|  |  |  | *subcmd*, |
|  |  |  | *help*, |
|  |  |  | *handler*, |
|  |  |  | *mand*, |
|  |  |  | *opt* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9)([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(flag), syntax, subcmd, help, \

handler, mand, opt)

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

Initializes a conditional shell command with arguments.

See also
:   [SHELL\_CMD\_ARG](#gad762c496a2ced65069b6d1d02a4d925c). Based on the flag, creates a valid entry or an empty command which is ignored by the [shell](structshell.md "Shell instance internals."). It is an alternative to #ifdefs around command registration and command handler. However, empty structure is present in the flash even if command is disabled (subcommands and handler are removed). Macro internally handles case if flag is not defined so flag must be provided without any wrapper, e.g.: [SHELL\_COND\_CMD\_ARG(CONFIG\_FOO, ...)](#ga68229f89484c3459d77cebb450ee1f24)

Parameters
:   | [in] | flag | Compile time flag. Command is present only if flag exists and equals 1. |
    | --- | --- | --- |
    | [in] | syntax | Command syntax (for example: history). |
    | [in] | subcmd | Pointer to a subcommands array. |
    | [in] | help | Pointer to a command help string. |
    | [in] | handler | Pointer to a function handler. |
    | [in] | mand | Number of mandatory arguments including command name. |
    | [in] | opt | Number of optional arguments. |

## [◆ ](#ga6a3ed4ea9051ac138d22cc39134fb2e5)SHELL\_COND\_CMD\_ARG\_REGISTER

| #define SHELL\_COND\_CMD\_ARG\_REGISTER | ( |  | *flag*, |
| --- | --- | --- | --- |
|  |  |  | *syntax*, |
|  |  |  | *subcmd*, |
|  |  |  | *help*, |
|  |  |  | *handler*, |
|  |  |  | *mandatory*, |
|  |  |  | *optional* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(\

flag, \

(\

[SHELL\_CMD\_ARG\_REGISTER](#gae8a8bbcbb842027c02a319b3fb976a3d)(syntax, subcmd, help, handler, \

mandatory, optional) \

), \

(\

static [shell\_cmd\_handler](#ga331e7d19b9b0755486596f5ffc598338) dummy\_##syntax##\_handler \_\_unused = \

handler;\

static const union [shell\_cmd\_entry](unionshell__cmd__entry.md) \*dummy\_subcmd\_##syntax \

\_\_unused = subcmd\

) \

)

[shell\_cmd\_handler](#ga331e7d19b9b0755486596f5ffc598338)

int(\* shell\_cmd\_handler)(const struct shell \*sh, size\_t argc, char \*\*argv)

Shell command handler prototype.

**Definition** shell.h:174

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

Macro for defining and adding a conditional root command (level 0) with required number of arguments.

See also
:   [SHELL\_CMD\_ARG\_REGISTER](#gae8a8bbcbb842027c02a319b3fb976a3d) for details.

Macro can be used to create a command which can be conditionally present. It is and alternative to #ifdefs around command registration and command handler. If command is disabled handler and subcommands are removed from the application.

Parameters
:   | [in] | flag | Compile time flag. Command is present only if flag exists and equals 1. |
    | --- | --- | --- |
    | [in] | syntax | Command syntax (for example: history). |
    | [in] | subcmd | Pointer to a subcommands array. |
    | [in] | help | Pointer to a command help string. |
    | [in] | handler | Pointer to a function handler. |
    | [in] | mandatory | Number of mandatory arguments including command name. |
    | [in] | optional | Number of optional arguments. |

## [◆ ](#ga62782121ece6af076407c94935ec94e4)SHELL\_COND\_CMD\_REGISTER

| #define SHELL\_COND\_CMD\_REGISTER | ( |  | *flag*, |
| --- | --- | --- | --- |
|  |  |  | *syntax*, |
|  |  |  | *subcmd*, |
|  |  |  | *help*, |
|  |  |  | *handler* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_COND\_CMD\_ARG\_REGISTER](#ga6a3ed4ea9051ac138d22cc39134fb2e5)(flag, syntax, subcmd, help, handler, 0, 0)

[SHELL\_COND\_CMD\_ARG\_REGISTER](#ga6a3ed4ea9051ac138d22cc39134fb2e5)

#define SHELL\_COND\_CMD\_ARG\_REGISTER(flag, syntax, subcmd, help, handler, mandatory, optional)

Macro for defining and adding a conditional root command (level 0) with required number of arguments.

**Definition** shell.h:261

Macro for defining and adding a conditional root command (level 0) with arguments.

See also
:   [SHELL\_COND\_CMD\_ARG\_REGISTER](#ga6a3ed4ea9051ac138d22cc39134fb2e5).

Parameters
:   | [in] | flag | Compile time flag. Command is present only if flag exists and equals 1. |
    | --- | --- | --- |
    | [in] | syntax | Command syntax (for example: history). |
    | [in] | subcmd | Pointer to a subcommands array. |
    | [in] | help | Pointer to a command help string. |
    | [in] | handler | Pointer to a function handler. |

## [◆ ](#ga7e522b107d4e8b687816a86f14b9a885)SHELL\_DEFAULT\_BACKEND\_CONFIG\_FLAGS

| #define SHELL\_DEFAULT\_BACKEND\_CONFIG\_FLAGS |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

{ \

.insert\_mode = 0, \

.echo = 1, \

.obscure = [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_SHELL\_START\_OBSCURED), \

.mode\_delete = 1, \

.use\_colors = 1, \

.use\_vt100 = 1, \

};

## [◆ ](#ga158405143b49e4888cb135fec83ad22c)SHELL\_DEFINE

| #define SHELL\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_prompt*, |
|  |  |  | *\_transport\_iface*, |
|  |  |  | *\_log\_queue\_size*, |
|  |  |  | *\_log\_timeout*, |
|  |  |  | *\_shell\_flag* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_name##\_out\_buffer[[CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE](shell_2shell_8h.md#af54e892edba822e46ca70cb6eca48146)]; \

Z\_SHELL\_LOG\_BACKEND\_DEFINE(\_name, \_name##\_out\_buffer, [CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE](shell_2shell_8h.md#af54e892edba822e46ca70cb6eca48146), \

\_log\_queue\_size, \_log\_timeout); \

Z\_SHELL\_DEFINE(\_name, \_prompt, \_transport\_iface, \_name##\_out\_buffer, \

Z\_SHELL\_LOG\_BACKEND\_PTR(\_name), \_shell\_flag)

[CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE](shell_2shell_8h.md#af54e892edba822e46ca70cb6eca48146)

#define CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE

**Definition** shell.h:38

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Macro for defining a shell instance.

Parameters
:   | [in] | \_name | Instance name. |
    | --- | --- | --- |
    | [in] | \_prompt | Shell default prompt string. |
    | [in] | \_transport\_iface | Pointer to the transport interface. |
    | [in] | \_log\_queue\_size | Logger processing queue size. |
    | [in] | \_log\_timeout | Logger thread timeout in milliseconds on full log queue. If queue is full logger thread is blocked for given amount of time before log message is dropped. |
    | [in] | \_shell\_flag | Shell output newline sequence. |

## [◆ ](#gafa6d91c36c36eb68d3f241ed0c7e7131)SHELL\_DYNAMIC\_CMD\_CREATE

| #define SHELL\_DYNAMIC\_CMD\_CREATE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *get* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

static const [TYPE\_SECTION\_ITERABLE](group__iterable__section__apis.md#gac5177fefd615bdd3025fac742d414808)(union [shell\_cmd\_entry](unionshell__cmd__entry.md), name, \

shell\_dynamic\_subcmds, name) = \

{ \

.dynamic\_get = get \

}

Macro for creating a dynamic entry.

Parameters
:   | [in] | name | Name of the dynamic entry. |
    | --- | --- | --- |
    | [in] | get | Pointer to the function returning dynamic commands array |

## [◆ ](#ga7664f5e184e9b41ac92e033f7b8d885d)SHELL\_ERROR

| #define SHELL\_ERROR   [SHELL\_VT100\_COLOR\_RED](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Red text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function.

## [◆ ](#ga408141c02209a9549cb9063f24ef3731)shell\_error

| #define shell\_error | ( |  | *\_sh*, |
| --- | --- | --- | --- |
|  |  |  | *\_ft*, |
|  |  |  | ... ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[shell\_fprintf\_error](#ga427d7f51d99aec311348f836d9007df7)(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[shell\_fprintf\_error](#ga427d7f51d99aec311348f836d9007df7)

void shell\_fprintf\_error(const struct shell \*sh, const char \*fmt,...)

Print error message to the shell.

See [shell\_fprintf](structshell__fprintf.md "shell_fprintf").

Parameters
:   | [in] | \_sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | \_ft | Format string. |
    | [in] | ... | List of parameters to print. |

## [◆ ](#ga59a835edbd7db3acdcb204248c0cf5fd)SHELL\_EXPR\_CMD

| #define SHELL\_EXPR\_CMD | ( |  | *\_expr*, |
| --- | --- | --- | --- |
|  |  |  | *\_syntax*, |
|  |  |  | *\_subcmd*, |
|  |  |  | *\_help*, |
|  |  |  | *\_handler* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9)(\_expr, \_syntax, \_subcmd, \_help, \_handler, 0, 0)

Initializes shell command if expression gives non-zero result at compile time.

See also
:   [SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9).

Parameters
:   | [in] | \_expr | Compile time expression. Command is present only if expression is non-zero. |
    | --- | --- | --- |
    | [in] | \_syntax | Command syntax (for example: history). |
    | [in] | \_subcmd | Pointer to a subcommands array. |
    | [in] | \_help | Pointer to a command help string. |
    | [in] | \_handler | Pointer to a function handler. |

## [◆ ](#ga6b07c55dd7d42873d604ae299b3cfdf9)SHELL\_EXPR\_CMD\_ARG

| #define SHELL\_EXPR\_CMD\_ARG | ( |  | *\_expr*, |
| --- | --- | --- | --- |
|  |  |  | *\_syntax*, |
|  |  |  | *\_subcmd*, |
|  |  |  | *\_help*, |
|  |  |  | *\_handler*, |
|  |  |  | *\_mand*, |
|  |  |  | *\_opt* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

{ \

.syntax = (\_expr) ? (const char \*)[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_syntax) : "", \

.help = (\_expr) ? (const char \*)\_help : NULL, \

.subcmd = (const union [shell\_cmd\_entry](unionshell__cmd__entry.md) \*)((\_expr) ? \

\_subcmd : NULL), \

.handler = ([shell\_cmd\_handler](#ga331e7d19b9b0755486596f5ffc598338))((\_expr) ? \_handler : NULL), \

.args = { .mandatory = \_mand, .optional = \_opt} \

}

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

Initializes a conditional shell command with arguments if expression gives non-zero result at compile time.

See also
:   [SHELL\_CMD\_ARG](#gad762c496a2ced65069b6d1d02a4d925c). Based on the expression, creates a valid entry or an empty command which is ignored by the [shell](structshell.md "Shell instance internals."). It should be used instead of [SHELL\_COND\_CMD\_ARG](#ga68229f89484c3459d77cebb450ee1f24) if condition is not a single configuration flag, e.g.: [SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9)([IS\_ENABLED(CONFIG\_FOO)](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a "Check for macro definition in compiler-visible expressions.") && [IS\_ENABLED(CONFIG\_FOO\_SETTING\_1)](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a "Check for macro definition in compiler-visible expressions."), ...)

Parameters
:   | [in] | \_expr | Expression. |
    | --- | --- | --- |
    | [in] | \_syntax | Command syntax (for example: history). |
    | [in] | \_subcmd | Pointer to a subcommands array. |
    | [in] | \_help | Pointer to a command help string. |
    | [in] | \_handler | Pointer to a function handler. |
    | [in] | \_mand | Number of mandatory arguments including command name. |
    | [in] | \_opt | Number of optional arguments. |

## [◆ ](#ga1fd1671311b112f0c87ab2dafd801105)shell\_fprintf

| #define shell\_fprintf | ( |  | *sh*, |
| --- | --- | --- | --- |
|  |  |  | *color*, |
|  |  |  | *fmt*, |
|  |  |  | ... ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[shell\_fprintf\_impl](#ga863c04af5db00a3804eaff02d401603b)(sh, color, fmt, ##\_\_VA\_ARGS\_\_)

[shell\_fprintf\_impl](#ga863c04af5db00a3804eaff02d401603b)

void shell\_fprintf\_impl(const struct shell \*sh, enum shell\_vt100\_color color, const char \*fmt,...)

printf-like function which sends formatted data stream to the shell.

## [◆ ](#gaac0ea96fbb5885432dca93174c9ad4e6)SHELL\_INFO

| #define SHELL\_INFO   [SHELL\_VT100\_COLOR\_GREEN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Green text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function.

## [◆ ](#ga9382959c41fe6850c2daa51306b3c5fd)shell\_info

| #define shell\_info | ( |  | *\_sh*, |
| --- | --- | --- | --- |
|  |  |  | *\_ft*, |
|  |  |  | ... ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[shell\_fprintf\_info](#ga30fcc10f13ce8d850f2c1c5de4533a29)(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[shell\_fprintf\_info](#ga30fcc10f13ce8d850f2c1c5de4533a29)

void shell\_fprintf\_info(const struct shell \*sh, const char \*fmt,...)

Print info message to the shell.

See [shell\_fprintf](structshell__fprintf.md "shell_fprintf").

Parameters
:   | [in] | \_sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | \_ft | Format string. |
    | [in] | ... | List of parameters to print. |

## [◆ ](#ga4c3a7db0c2bdbf36bbf72302a04bb44d)SHELL\_NORMAL

| #define SHELL\_NORMAL   [SHELL\_VT100\_COLOR\_DEFAULT](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Terminal default text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function.

## [◆ ](#gacc7c6e7b1fc65cc350353cc166da528b)SHELL\_OPTION

| #define SHELL\_OPTION   [SHELL\_VT100\_COLOR\_CYAN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Cyan text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function.

## [◆ ](#ga3126019b2100d1ccb2d4dc5efb7d8228)shell\_print

| #define shell\_print | ( |  | *\_sh*, |
| --- | --- | --- | --- |
|  |  |  | *\_ft*, |
|  |  |  | ... ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[shell\_fprintf\_normal](#ga67f638ebc05f8300553e5e6c1771380d)(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[shell\_fprintf\_normal](#ga67f638ebc05f8300553e5e6c1771380d)

void shell\_fprintf\_normal(const struct shell \*sh, const char \*fmt,...)

Print normal message to the shell.

See [shell\_fprintf](structshell__fprintf.md "shell_fprintf").

Parameters
:   | [in] | \_sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | \_ft | Format string. |
    | [in] | ... | List of parameters to print. |

## [◆ ](#gacb2d1a969368efdbeec704ee6e962dee)SHELL\_STATIC\_SUBCMD\_SET\_CREATE

| #define SHELL\_STATIC\_SUBCMD\_SET\_CREATE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

static const struct [shell\_static\_entry](structshell__static__entry.md) shell\_##name[] = { \

\_\_VA\_ARGS\_\_ \

}; \

static const union [shell\_cmd\_entry](unionshell__cmd__entry.md) name = { \

.entry = shell\_##name \

}

Macro for creating a subcommand set.

It must be used outside of any function body.

Example usage:

[SHELL\_STATIC\_SUBCMD\_SET\_CREATE](#gacb2d1a969368efdbeec704ee6e962dee)(

foo,

[SHELL\_CMD](#ga24ade9db85af9a8776a45ba0084f4cca)(abc, ...),

[SHELL\_CMD](#ga24ade9db85af9a8776a45ba0084f4cca)(def, ...),

[SHELL\_SUBCMD\_SET\_END](#ga4f7a3432f76541eb226a426507e10174)

)

[SHELL\_CMD](#ga24ade9db85af9a8776a45ba0084f4cca)

#define SHELL\_CMD(\_syntax, \_subcmd, \_help, \_handler)

Initializes a shell command.

**Definition** shell.h:505

[SHELL\_SUBCMD\_SET\_END](#ga4f7a3432f76541eb226a426507e10174)

#define SHELL\_SUBCMD\_SET\_END

Define ending subcommands set.

**Definition** shell.h:413

[SHELL\_STATIC\_SUBCMD\_SET\_CREATE](#gacb2d1a969368efdbeec704ee6e962dee)

#define SHELL\_STATIC\_SUBCMD\_SET\_CREATE(name,...)

Macro for creating a subcommand set.

**Definition** shell.h:324

Parameters
:   | [in] | name | Name of the subcommand set. |
    | --- | --- | --- |
    | [in] | ... | List of commands created with [SHELL\_CMD\_ARG](#gad762c496a2ced65069b6d1d02a4d925c) or or [SHELL\_CMD](#ga24ade9db85af9a8776a45ba0084f4cca) |

## [◆ ](#ga85b0afcacd3831bf5c724590765e035f)SHELL\_SUBCMD\_ADD

| #define SHELL\_SUBCMD\_ADD | ( |  | *\_parent*, |
| --- | --- | --- | --- |
|  |  |  | *\_syntax*, |
|  |  |  | *\_subcmd*, |
|  |  |  | *\_help*, |
|  |  |  | *\_handler*, |
|  |  |  | *\_mand*, |
|  |  |  | *\_opt* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[SHELL\_SUBCMD\_COND\_ADD](#gab1b643efbaee748be0256e904642e310)(1, \_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt)

[SHELL\_SUBCMD\_COND\_ADD](#gab1b643efbaee748be0256e904642e310)

#define SHELL\_SUBCMD\_COND\_ADD(\_flag, \_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt)

Conditionally add command to the set of subcommands.

**Definition** shell.h:377

Add command to the set of subcommands.

Add command to the set created with [SHELL\_SUBCMD\_SET\_CREATE](#ga1e314886b70ee2e7e0763cd945a1a988).

Parameters
:   | [in] | \_parent | Parent command sequence. Comma separated in parenthesis. |
    | --- | --- | --- |
    | [in] | \_syntax | Command syntax (for example: history). |
    | [in] | \_subcmd | Pointer to a subcommands array. |
    | [in] | \_help | Pointer to a command help string. |
    | [in] | \_handler | Pointer to a function handler. |
    | [in] | \_mand | Number of mandatory arguments including command name. |
    | [in] | \_opt | Number of optional arguments. |

## [◆ ](#gab1b643efbaee748be0256e904642e310)SHELL\_SUBCMD\_COND\_ADD

| #define SHELL\_SUBCMD\_COND\_ADD | ( |  | *\_flag*, |
| --- | --- | --- | --- |
|  |  |  | *\_parent*, |
|  |  |  | *\_syntax*, |
|  |  |  | *\_subcmd*, |
|  |  |  | *\_help*, |
|  |  |  | *\_handler*, |
|  |  |  | *\_mand*, |
|  |  |  | *\_opt* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(\_flag, \

(static const [TYPE\_SECTION\_ITERABLE](group__iterable__section__apis.md#gac5177fefd615bdd3025fac742d414808)(struct [shell\_static\_entry](structshell__static__entry.md), \

Z\_SHELL\_SUBCMD\_NAME(\_\_DEBRACKET \_parent, \_syntax), \

shell\_subcmds, \

Z\_SHELL\_SUBCMD\_ADD\_SECTION\_TAG(\_parent, \_syntax)) = \

[SHELL\_EXPR\_CMD\_ARG](#ga6b07c55dd7d42873d604ae299b3cfdf9)(1, \_syntax, \_subcmd, \_help, \

\_handler, \_mand, \_opt)\

), \

(static [shell\_cmd\_handler](#ga331e7d19b9b0755486596f5ffc598338) dummy\_handler\_##\_syntax \_\_unused = \_handler;\

static const union [shell\_cmd\_entry](unionshell__cmd__entry.md) dummy\_subcmd\_##\_syntax \_\_unused = { \

.entry = (const struct [shell\_static\_entry](structshell__static__entry.md) \*)\_subcmd\

} \

) \

)

Conditionally add command to the set of subcommands.

Add command to the set created with [SHELL\_SUBCMD\_SET\_CREATE](#ga1e314886b70ee2e7e0763cd945a1a988).

Note
:   The name of the section is formed as concatenation of number of parent commands, names of all parent commands and own syntax. Number of parent commands is added to ensure that section prefix is unique. Without it subcommands of (foo) and (foo, cmd1) would mix.

Parameters
:   | [in] | \_flag | Compile time flag. Command is present only if flag exists and equals 1. |
    | --- | --- | --- |
    | [in] | \_parent | Parent command sequence. Comma separated in parenthesis. |
    | [in] | \_syntax | Command syntax (for example: history). |
    | [in] | \_subcmd | Pointer to a subcommands array. |
    | [in] | \_help | Pointer to a command help string. |
    | [in] | \_handler | Pointer to a function handler. |
    | [in] | \_mand | Number of mandatory arguments including command name. |
    | [in] | \_opt | Number of optional arguments. |

## [◆ ](#ga401e19cf8ec8601b8a96fe8e95a2b4d2)SHELL\_SUBCMD\_DICT\_SET\_CREATE

| #define SHELL\_SUBCMD\_DICT\_SET\_CREATE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_handler*, |
|  |  |  | ... ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)(Z\_SHELL\_CMD\_DICT\_HANDLER\_CREATE, (), \

\_handler, \_\_VA\_ARGS\_\_) \

SHELL\_STATIC\_SUBCMD\_SET\_CREATE(\_name, \

[FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)([SHELL\_CMD\_DICT\_CREATE](#gaf33b1b20caccad1effe6733603259a00), (,), \_handler, \_\_VA\_ARGS\_\_), \

[SHELL\_SUBCMD\_SET\_END](#ga4f7a3432f76541eb226a426507e10174) \

)

[SHELL\_CMD\_DICT\_CREATE](#gaf33b1b20caccad1effe6733603259a00)

#define SHELL\_CMD\_DICT\_CREATE(\_data, \_handler)

**Definition** shell.h:550

[FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)

#define FOR\_EACH\_FIXED\_ARG(F, sep, fixed\_arg,...)

Call macro F on each provided argument, with an additional fixed argument as a parameter.

**Definition** util\_macro.h:601

Initializes shell dictionary commands.

This is a special kind of static commands. Dictionary commands can be used every time you want to use a pair: (string <-> corresponding data) in a command handler. The string is usually a verbal description of a given data. The idea is to use the string as a command syntax that can be prompted by the shell and corresponding data can be used to process the command.

Parameters
:   | [in] | \_name | Name of the dictionary subcommand set |
    | --- | --- | --- |
    | [in] | \_handler | Command handler common for all dictionary commands. |

See also
:   [shell\_dict\_cmd\_handler](#ga182f247052041f1236d13726589885e2)

Parameters
:   | [in] | ... | Dictionary triplets: (command\_syntax, value, helper). Value will be passed to the \_handler as user data. |
    | --- | --- | --- |

Example usage:

static int my\_handler(const struct [shell](structshell.md) \*sh,

size\_t argc, char \*\*argv, void \*data)

{

int val = (int)data;

[shell\_print](#ga3126019b2100d1ccb2d4dc5efb7d8228)(sh, "(syntax, value) : (%s, %d)", argv[0], val);

return 0;

}

[SHELL\_SUBCMD\_DICT\_SET\_CREATE](#ga401e19cf8ec8601b8a96fe8e95a2b4d2)(sub\_dict\_cmds, my\_handler,

(value\_0, 0, "value 0"), (value\_1, 1, "value 1"),

(value\_2, 2, "value 2"), (value\_3, 3, "value 3")

);

[SHELL\_CMD\_REGISTER](#ga06060b98eb505300a3dcc8f922a8e7ab)(dictionary, &sub\_dict\_cmds, NULL, NULL);

[SHELL\_CMD\_REGISTER](#ga06060b98eb505300a3dcc8f922a8e7ab)

#define SHELL\_CMD\_REGISTER(syntax, subcmd, help, handler)

Macro for defining and adding a root command (level 0) with arguments.

**Definition** shell.h:287

[shell\_print](#ga3126019b2100d1ccb2d4dc5efb7d8228)

#define shell\_print(\_sh, \_ft,...)

Print normal message to the shell.

**Definition** shell.h:1118

[SHELL\_SUBCMD\_DICT\_SET\_CREATE](#ga401e19cf8ec8601b8a96fe8e95a2b4d2)

#define SHELL\_SUBCMD\_DICT\_SET\_CREATE(\_name, \_handler,...)

Initializes shell dictionary commands.

**Definition** shell.h:588

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:890

## [◆ ](#ga1e314886b70ee2e7e0763cd945a1a988)SHELL\_SUBCMD\_SET\_CREATE

| #define SHELL\_SUBCMD\_SET\_CREATE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_parent* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

static const [TYPE\_SECTION\_ITERABLE](group__iterable__section__apis.md#gac5177fefd615bdd3025fac742d414808)(struct [shell\_static\_entry](structshell__static__entry.md), \_name, shell\_subcmds, \

Z\_SHELL\_SUBCMD\_SET\_SECTION\_TAG(\_parent))

Create set of subcommands.

Commands to this set are added using [SHELL\_SUBCMD\_ADD](#ga85b0afcacd3831bf5c724590765e035f) and [SHELL\_SUBCMD\_COND\_ADD](#gab1b643efbaee748be0256e904642e310). Commands can be added from multiple files.

Parameters
:   | [in] | \_name | Name of the set. `_name` is used to refer the set in the parent command. |
    | --- | --- | --- |
    | [in] | \_parent | Set of comma separated parent commands in parenthesis, e.g. (foo\_cmd) if subcommands are for the root command "foo\_cmd". |

## [◆ ](#ga4f7a3432f76541eb226a426507e10174)SHELL\_SUBCMD\_SET\_END

| #define SHELL\_SUBCMD\_SET\_END   {NULL} |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Define ending subcommands set.

## [◆ ](#ga3d886cfd7b4340b2e71a92bd7c4534d9)shell\_warn

| #define shell\_warn | ( |  | *\_sh*, |
| --- | --- | --- | --- |
|  |  |  | *\_ft*, |
|  |  |  | ... ) |

`#include <[shell.h](shell_2shell_8h.md)>`

**Value:**

[shell\_fprintf\_warn](#ga9c9ced10bf376a5514b8b0bb55e1efcd)(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[shell\_fprintf\_warn](#ga9c9ced10bf376a5514b8b0bb55e1efcd)

void shell\_fprintf\_warn(const struct shell \*sh, const char \*fmt,...)

Print warning message to the shell.

See [shell\_fprintf](structshell__fprintf.md "shell_fprintf").

Parameters
:   | [in] | \_sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | \_ft | Format string. |
    | [in] | ... | List of parameters to print. |

## [◆ ](#ga118dd6829e092423a85e2b6de07f8dd3)SHELL\_WARNING

| #define SHELL\_WARNING   [SHELL\_VT100\_COLOR\_YELLOW](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Yellow text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function.

## Typedef Documentation

## [◆ ](#gab1dafbf90c42b7d4601122e1b9eabf3d)shell\_bypass\_cb\_t

| typedef void(\* shell\_bypass\_cb\_t) (const struct [shell](structshell.md) \*sh, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Bypass callback.

Parameters
:   | sh | Shell instance. |
    | --- | --- |
    | data | Raw data from transport. |
    | len | Data length. |

## [◆ ](#ga331e7d19b9b0755486596f5ffc598338)shell\_cmd\_handler

| typedef int(\* shell\_cmd\_handler) (const struct [shell](structshell.md) \*sh, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) argc, char \*\*argv) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Shell command handler prototype.

Parameters
:   | sh | Shell instance. |
    | --- | --- |
    | argc | Arguments count. |
    | argv | Arguments. |

Return values
:   | 0 | Successful command execution. |
    | --- | --- |
    | 1 | Help printed and command not executed. |
    | -EINVAL | Argument validation failed. |
    | -ENOEXEC | Command not executed. |

## [◆ ](#gaa2b8cf8ac78b8355408ef94958ebdc70)shell\_device\_filter\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* shell\_device\_filter\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Filter callback type, for use with shell\_device\_lookup\_filter.

This is used as an argument of shell\_device\_lookup\_filter to only return devices that match a specific condition, implemented by the filter.

Parameters
:   | dev | pointer to a struct device. |
    | --- | --- |

Returns
:   bool, true if the filter matches the device type.

## [◆ ](#ga182f247052041f1236d13726589885e2)shell\_dict\_cmd\_handler

| typedef int(\* shell\_dict\_cmd\_handler) (const struct [shell](structshell.md) \*sh, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) argc, char \*\*argv, void \*data) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Shell dictionary command handler prototype.

Parameters
:   | sh | Shell instance. |
    | --- | --- |
    | argc | Arguments count. |
    | argv | Arguments. |
    | data | Pointer to the user data. |

Return values
:   | 0 | Successful command execution. |
    | --- | --- |
    | 1 | Help printed and command not executed. |
    | -EINVAL | Argument validation failed. |
    | -ENOEXEC | Command not executed. |

## [◆ ](#gafc042f32bac2fdd4cbde9f943e29b008)shell\_dynamic\_get

| typedef void(\* shell\_dynamic\_get) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) idx, struct [shell\_static\_entry](structshell__static__entry.md) \*entry) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Shell dynamic command descriptor.

Function shall fill the received [shell\_static\_entry](structshell__static__entry.md) structure with requested (idx) dynamic subcommand data. If there is more than one dynamic subcommand available, the function shall ensure that the returned commands: entry->syntax are sorted in alphabetical order. If idx exceeds the available dynamic subcommands, the function must write to entry->syntax NULL value. This will indicate to the shell module that there are no more dynamic commands to read.

## [◆ ](#ga265807c2d8eba7b9ea633968627e085d)shell\_transport\_handler\_t

| typedef void(\* shell\_transport\_handler\_t) (enum [shell\_transport\_evt](#gae77673d4c086f2f9312ceb7933745ee1) evt, void \*context) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

## [◆ ](#ga0844a0ce151551d3ccf45d507e5bab25)shell\_uninit\_cb\_t

| typedef void(\* shell\_uninit\_cb\_t) (const struct [shell](structshell.md) \*sh, int res) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga56bf30741f9ec7a6d94e5c18c2858948)shell\_flag

| enum [shell\_flag](#ga56bf30741f9ec7a6d94e5c18c2858948) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Flags for setting shell output newline sequence.

| Enumerator | |
| --- | --- |
| SHELL\_FLAG\_CRLF\_DEFAULT | Do not map CR or LF. |
| SHELL\_FLAG\_OLF\_CRLF | Map LF to CRLF on output. |

## [◆ ](#ga8773ed2570714ba4985108b1738d33a0)shell\_receive\_state

| enum [shell\_receive\_state](#ga8773ed2570714ba4985108b1738d33a0) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

| Enumerator | |
| --- | --- |
| SHELL\_RECEIVE\_DEFAULT |  |
| SHELL\_RECEIVE\_ESC |  |
| SHELL\_RECEIVE\_ESC\_SEQ |  |
| SHELL\_RECEIVE\_TILDE\_EXP |  |

## [◆ ](#ga5cd015de5e7295483fa2cff7d54c2d21)shell\_signal

| enum [shell\_signal](#ga5cd015de5e7295483fa2cff7d54c2d21) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

| Enumerator | |
| --- | --- |
| SHELL\_SIGNAL\_RXRDY |  |
| SHELL\_SIGNAL\_LOG\_MSG |  |
| SHELL\_SIGNAL\_KILL |  |
| SHELL\_SIGNAL\_TXDONE |  |
| SHELL\_SIGNALS |  |

## [◆ ](#gaf2c6ff9ef31dc06086fd1141763e6266)shell\_state

| enum [shell\_state](#gaf2c6ff9ef31dc06086fd1141763e6266) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

| Enumerator | |
| --- | --- |
| SHELL\_STATE\_UNINITIALIZED |  |
| SHELL\_STATE\_INITIALIZED |  |
| SHELL\_STATE\_ACTIVE |  |
| SHELL\_STATE\_PANIC\_MODE\_ACTIVE | Panic activated. |
| SHELL\_STATE\_PANIC\_MODE\_INACTIVE | Panic requested, not supported. |

## [◆ ](#gae77673d4c086f2f9312ceb7933745ee1)shell\_transport\_evt

| enum [shell\_transport\_evt](#gae77673d4c086f2f9312ceb7933745ee1) |
| --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Shell transport event.

| Enumerator | |
| --- | --- |
| SHELL\_TRANSPORT\_EVT\_RX\_RDY |  |
| SHELL\_TRANSPORT\_EVT\_TX\_RDY |  |

## Function Documentation

## [◆ ](#gae2a8e3d44a9bf5eb55be80833ac6eb5d)shell\_device\_filter()

| const struct [device](structdevice.md) \* shell\_device\_filter | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *idx*, |
| --- | --- | --- | --- |
|  |  | [shell\_device\_filter\_t](#gaa2b8cf8ac78b8355408ef94958ebdc70) | *filter* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Get a device by index and filter.

This can be used to return devices matching a specific type.

Devices that the filter returns false for, failed to initialize or do not have a non-empty name are excluded from the candidates for a match.

Parameters
:   | idx | the device number starting from zero. |
    | --- | --- |
    | filter | a pointer to a [shell\_device\_filter\_t](#gaa2b8cf8ac78b8355408ef94958ebdc70) function that returns true if the device matches the filter. |

## [◆ ](#ga571db3aa3e024a09e82b117a74d6f248)shell\_device\_lookup()

| const struct [device](structdevice.md) \* shell\_device\_lookup | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *idx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *prefix* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Get by index a device that matches .

This can be used, for example, to identify I2C\_1 as the second I2C device.

Devices that failed to initialize or do not have a non-empty name are excluded from the candidates for a match.

Parameters
:   | idx | the device number starting from zero. |
    | --- | --- |
    | prefix | optional name prefix used to restrict candidate devices. Indexing is done relative to devices with names that start with this text. Pass null if no prefix match is required. |

## [◆ ](#gad53881371bbaedfd3ef3ecf219706fd1)shell\_echo\_set()

| int shell\_echo\_set | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *val* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Allow application to control whether user input is echoed back.

Value is modified atomically and the previous value is returned.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | val | Echo mode. |

Return values
:   | 0 | or 1: previous value |
    | --- | --- |
    | -EINVAL | if shell is NULL. |

## [◆ ](#gabfb6a1f1f53f90365de349348015311e)shell\_execute\_cmd()

| int shell\_execute\_cmd | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const char \* | *cmd* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Execute command.

Pass command line to shell to execute.

Note: This by no means makes any of the commands a stable interface, so this function should only be used for debugging/diagnostic.

This function must not be called from shell command context!

Parameters
:   | [in] | sh | Pointer to the shell instance. It can be NULL when the  ``` CONFIG_SHELL_BACKEND_DUMMY ```  option is enabled. |
    | --- | --- | --- |
    | [in] | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command to be executed. |

Returns
:   Result of the execution

## [◆ ](#ga427d7f51d99aec311348f836d9007df7)shell\_fprintf\_error()

| void shell\_fprintf\_error | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const char \* | *fmt*, |
|  |  |  | *...* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

## [◆ ](#ga863c04af5db00a3804eaff02d401603b)shell\_fprintf\_impl()

| void shell\_fprintf\_impl | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) | *color*, |
|  |  | const char \* | *fmt*, |
|  |  |  | *...* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

printf-like function which sends formatted data stream to the shell.

This function can be used from the command handler or from threads, but not from an interrupt context.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | color | Printed text color. |
    | [in] | fmt | Format string. |
    | [in] | ... | List of parameters to print. |

## [◆ ](#ga30fcc10f13ce8d850f2c1c5de4533a29)shell\_fprintf\_info()

| void shell\_fprintf\_info | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const char \* | *fmt*, |
|  |  |  | *...* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

## [◆ ](#ga67f638ebc05f8300553e5e6c1771380d)shell\_fprintf\_normal()

| void shell\_fprintf\_normal | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const char \* | *fmt*, |
|  |  |  | *...* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

## [◆ ](#ga9c9ced10bf376a5514b8b0bb55e1efcd)shell\_fprintf\_warn()

| void shell\_fprintf\_warn | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const char \* | *fmt*, |
|  |  |  | *...* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

## [◆ ](#ga54dc053c92641bc9b9736bc2d61140f7)shell\_get\_return\_value()

| int shell\_get\_return\_value | ( | const struct [shell](structshell.md) \* | *sh* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Retrieve return value of most recently executed shell command.

Parameters
:   | [in] | sh | Pointer to the shell instance |
    | --- | --- | --- |

Return values
:   | return | value of previous command |
    | --- | --- |

## [◆ ](#gac3c643a0b332cd2f07fe506337784ac0)shell\_help()

| void shell\_help | ( | const struct [shell](structshell.md) \* | *sh* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Prints the current command help.

Function will print a help string with: the currently entered command and subcommands (if they exist).

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |

## [◆ ](#gaeeba0b483974205c54e364d509badd42)shell\_hexdump()

| void shell\_hexdump | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Print data in hexadecimal format.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | data | Pointer to data. |
    | [in] | len | Length of data. |

## [◆ ](#ga0b6e69b499c153ae8f7ba256d445f09d)shell\_hexdump\_line()

| void shell\_hexdump\_line | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *offset*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Print a line of data in hexadecimal format.

Each line shows the offset, bytes and then ASCII representation.

For example:

00008010: 20 25 00 20 2f 48 00 08 80 05 00 20 af 46 00 | %. /H.. ... .F. |

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | offset | Offset to show for this line. |
    | [in] | data | Pointer to data. |
    | [in] | len | Length of data. |

## [◆ ](#ga8764ff11603855a10419c48e46e8221c)shell\_init()

| int shell\_init | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const void \* | *transport\_config*, |
|  |  | struct [shell\_backend\_config\_flags](structshell__backend__config__flags.md) | *cfg\_flags*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *log\_backend*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *init\_log\_level* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Function for initializing a transport layer and internal shell state.

Parameters
:   | [in] | sh | Pointer to shell instance. |
    | --- | --- | --- |
    | [in] | transport\_config | Transport configuration during initialization. |
    | [in] | cfg\_flags | Initial backend configuration flags. Shell will copy this data. |
    | [in] | [log\_backend](structlog__backend.md "Logger backend structure.") | If true, the console will be used as logger backend. |
    | [in] | init\_log\_level | Default severity level for the logger. |

Returns
:   Standard error code.

## [◆ ](#gaf1f41d8b6cd430357d593ab0fc5adfeb)shell\_insert\_mode\_set()

| int shell\_insert\_mode\_set | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *val* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Allow application to control text insert mode.

Value is modified atomically and the previous value is returned.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | val | Insert mode. |

Return values
:   | 0 | or 1: previous value |
    | --- | --- |
    | -EINVAL | if shell is NULL. |

## [◆ ](#ga2df2997c4b04f3246c22f43b274a353b)shell\_mode\_delete\_set()

| int shell\_mode\_delete\_set | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *val* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Allow application to control whether the delete key backspaces or deletes.

Value is modified atomically and the previous value is returned.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | val | Delete mode. |

Return values
:   | 0 | or 1: previous value |
    | --- | --- |
    | -EINVAL | if shell is NULL. |

## [◆ ](#ga86fade2757d04c9220d5912a4ee540a0)shell\_obscure\_set()

| int shell\_obscure\_set | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *obscure* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Allow application to control whether user input is obscured with asterisks – useful for implementing passwords.

Value is modified atomically and the previous value is returned.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | obscure | Obscure mode. |

Return values
:   | 0 | or 1: previous value. |
    | --- | --- |
    | -EINVAL | if shell is NULL. |

## [◆ ](#ga7e66389d0faf15a2a7c31c68cdd9c36c)shell\_process()

| void shell\_process | ( | const struct [shell](structshell.md) \* | *sh* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Process function, which should be executed when data is ready in the transport interface.

To be used if shell thread is disabled.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |

## [◆ ](#ga2113b7227b155755a7ab8a928f7ae499)shell\_prompt\_change()

| int shell\_prompt\_change | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | const char \* | *prompt* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Change displayed shell prompt.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | prompt | New shell prompt. |

Returns
:   0 Success.
:   -EINVAL Pointer to new prompt is not correct.

## [◆ ](#ga79369ddfea2dc2cb5813c5eb5c67634a)shell\_ready()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_ready | ( | const struct [shell](structshell.md) \* | *sh* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Get shell readiness to execute commands.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Shell backend is ready to execute commands. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Shell backend is not initialized or not started. |

## [◆ ](#ga7514a072c2819fb93fb9d62542c7cc15)shell\_set\_bypass()

| void shell\_set\_bypass | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [shell\_bypass\_cb\_t](#gab1dafbf90c42b7d4601122e1b9eabf3d) | *bypass* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Set bypass callback.

Bypass callback is called whenever data is received. Shell is bypassed and data is passed directly to the callback. Use null to disable bypass functionality.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | bypass | Bypass callback or null to disable. |

## [◆ ](#ga768c606f2d50f24e9b607ba0a341686d)shell\_set\_root\_cmd()

| int shell\_set\_root\_cmd | ( | const char \* | *cmd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Set root command for all shell instances.

It allows setting from the code the root command. It is an equivalent of calling select command with one of the root commands as the argument (e.g "select log") except it sets command for all shell instances.

Parameters
:   | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | String with one of the root commands or null pointer to reset. |
    | --- | --- |

Return values
:   | 0 | if root command is set. |
    | --- | --- |
    | -EINVAL | if invalid root command is provided. |

## [◆ ](#gad386d4e8077103e7976f25996fcc3132)shell\_start()

| int shell\_start | ( | const struct [shell](structshell.md) \* | *sh* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Function for starting shell processing.

Parameters
:   | sh | Pointer to the shell instance. |
    | --- | --- |

Returns
:   Standard error code.

## [◆ ](#gad27754d0beb31bc501f28f9ef26a362c)shell\_stop()

| int shell\_stop | ( | const struct [shell](structshell.md) \* | *sh* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

Function for stopping shell processing.

Parameters
:   | sh | Pointer to shell instance. |
    | --- | --- |

Returns
:   Standard error code.

## [◆ ](#ga07e76646c5065218464aa8ce78b75af3)shell\_uninit()

| void shell\_uninit | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [shell\_uninit\_cb\_t](#ga0844a0ce151551d3ccf45d507e5bab25) | *cb* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Uninitializes the transport layer and the internal shell state.

Parameters
:   | sh | Pointer to shell instance. |
    | --- | --- |
    | cb | Callback called when uninitialization is completed. |

## [◆ ](#ga7d5873456ba43ebd3cc86d25e3f4a72c)shell\_use\_colors\_set()

| int shell\_use\_colors\_set | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *val* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Allow application to control whether terminal output uses colored syntax.

Value is modified atomically and the previous value is returned.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | val | Color mode. |

Return values
:   | 0 | or 1: previous value |
    | --- | --- |
    | -EINVAL | if shell is NULL. |

## [◆ ](#ga80ff4b3b4cc62e543fd510c14f55b42a)shell\_use\_vt100\_set()

| int shell\_use\_vt100\_set | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *val* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

Allow application to control whether terminal is using vt100 commands.

Value is modified atomically and the previous value is returned.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | val | vt100 mode. |

Return values
:   | 0 | or 1: previous value |
    | --- | --- |
    | -EINVAL | if shell is NULL. |

## [◆ ](#ga74a1c4edd803cad14c893fc9816e534f)shell\_vfprintf()

| void shell\_vfprintf | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) | *color*, |
|  |  | const char \* | *fmt*, |
|  |  | va\_list | *args* ) |

`#include <[shell.h](shell_2shell_8h.md)>`

vprintf-like function which sends formatted data stream to the shell.

This function can be used from the command handler or from threads, but not from an interrupt context. It is similar to [shell\_fprintf()](#ga1fd1671311b112f0c87ab2dafd801105) but takes a va\_list instead of variable arguments.

Parameters
:   | [in] | sh | Pointer to the shell instance. |
    | --- | --- | --- |
    | [in] | color | Printed text color. |
    | [in] | fmt | Format string. |
    | [in] | args | List of parameters to print. |

## Variable Documentation

## [◆ ](#gaddf27615ed72440ecb63aa1d84962c82)log\_backend\_shell\_api

| | const struct [log\_backend\_api](structlog__backend__api.md) log\_backend\_shell\_api | | --- | | extern |
| --- | --- | --- |

`#include <[shell.h](shell_2shell_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
