---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell_2shell_8h.html
original_path: doxygen/html/shell_2shell_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/shell/shell_types.h](shell__types_8h_source.md)>`  
`#include <[zephyr/shell/shell_history.h](shell__history_8h_source.md)>`  
`#include <[zephyr/shell/shell_fprintf.h](shell__fprintf_8h_source.md)>`  
`#include <[zephyr/shell/shell_log_backend.h](shell__log__backend_8h_source.md)>`  
`#include <[zephyr/shell/shell_string_conv.h](shell__string__conv_8h_source.md)>`  
`#include <[zephyr/logging/log_instance.h](log__instance_8h_source.md)>`  
`#include <[zephyr/logging/log.h](log_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](shell_2shell_8h_source.md)

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
| #define | [CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE](#a81357b82642c8910ae3fb920cb885370)   0 |
| #define | [CONFIG\_SHELL\_CMD\_BUFF\_SIZE](#abb162a9a784f605dea4b02a0a6cc0c16)   0 |
| #define | [CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE](#af54e892edba822e46ca70cb6eca48146)   0 |
| #define | [CONFIG\_SHELL\_HISTORY\_BUFFER](#ab194ada3483ec28f093fd9521b19265e)   0 |
| #define | [SHELL\_HEXDUMP\_BYTES\_IN\_LINE](#af3a0fbf2152aa4578d29d98000b4d74e)   16 |
| #define | [SHELL\_OPT\_ARG\_RAW](#a2b64d0c6e086ea227e85fe50312896f7)   (0xFE) |
|  | Flag indicates that optional arguments will be treated as one, unformatted argument. |
| #define | [SHELL\_OPT\_ARG\_CHECK\_SKIP](#a0e2b3ac54184ae15f13e2024df1ac69b)   (0xFF) |
|  | Flag indicating that number of optional arguments is not limited. |
| #define | [SHELL\_OPT\_ARG\_MAX](#aba166d98da7258a2a50abc94c1b744c8)   (0xFD) |
|  | Flag indicating maximum number of optional arguments that can be validated. |
| #define | [SHELL\_CMD\_ARG\_REGISTER](group__shell__api.md#gae8a8bbcbb842027c02a319b3fb976a3d)(syntax, subcmd, help, handler, mandatory, optional) |
|  | Macro for defining and adding a root command (level 0) with required number of arguments. |
| #define | [SHELL\_COND\_CMD\_ARG\_REGISTER](group__shell__api.md#ga6a3ed4ea9051ac138d22cc39134fb2e5)(flag, syntax, subcmd, help, handler, mandatory, optional) |
|  | Macro for defining and adding a conditional root command (level 0) with required number of arguments. |
| #define | [SHELL\_CMD\_REGISTER](group__shell__api.md#ga06060b98eb505300a3dcc8f922a8e7ab)(syntax, subcmd, help, handler) |
|  | Macro for defining and adding a root command (level 0) with arguments. |
| #define | [SHELL\_COND\_CMD\_REGISTER](group__shell__api.md#ga62782121ece6af076407c94935ec94e4)(flag, syntax, subcmd, help, handler) |
|  | Macro for defining and adding a conditional root command (level 0) with arguments. |
| #define | [SHELL\_STATIC\_SUBCMD\_SET\_CREATE](group__shell__api.md#gacb2d1a969368efdbeec704ee6e962dee)(name, ...) |
|  | Macro for creating a subcommand set. |
| #define | [SHELL\_SUBCMD\_SET\_CREATE](group__shell__api.md#ga1e314886b70ee2e7e0763cd945a1a988)(\_name, \_parent) |
|  | Create set of subcommands. |
| #define | [SHELL\_SUBCMD\_COND\_ADD](group__shell__api.md#gab1b643efbaee748be0256e904642e310)(\_flag, \_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt) |
|  | Conditionally add command to the set of subcommands. |
| #define | [SHELL\_SUBCMD\_ADD](group__shell__api.md#ga85b0afcacd3831bf5c724590765e035f)(\_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt) |
|  | Add command to the set of subcommands. |
| #define | [SHELL\_SUBCMD\_SET\_END](group__shell__api.md#ga4f7a3432f76541eb226a426507e10174)   {NULL} |
|  | Define ending subcommands set. |
| #define | [SHELL\_DYNAMIC\_CMD\_CREATE](group__shell__api.md#gafa6d91c36c36eb68d3f241ed0c7e7131)(name, get) |
|  | Macro for creating a dynamic entry. |
| #define | [SHELL\_CMD\_ARG](group__shell__api.md#gad762c496a2ced65069b6d1d02a4d925c)(syntax, subcmd, help, handler, mand, opt) |
|  | Initializes a shell command with arguments. |
| #define | [SHELL\_COND\_CMD\_ARG](group__shell__api.md#ga68229f89484c3459d77cebb450ee1f24)(flag, syntax, subcmd, help, handler, mand, opt) |
|  | Initializes a conditional shell command with arguments. |
| #define | [SHELL\_EXPR\_CMD\_ARG](group__shell__api.md#ga6b07c55dd7d42873d604ae299b3cfdf9)(\_expr, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt) |
|  | Initializes a conditional shell command with arguments if expression gives non-zero result at compile time. |
| #define | [SHELL\_CMD](group__shell__api.md#ga24ade9db85af9a8776a45ba0084f4cca)(\_syntax, \_subcmd, \_help, \_handler) |
|  | Initializes a shell command. |
| #define | [SHELL\_COND\_CMD](group__shell__api.md#ga6e27d86443067df4792623f1a04d1ee1)(\_flag, \_syntax, \_subcmd, \_help, \_handler) |
|  | Initializes a conditional shell command. |
| #define | [SHELL\_EXPR\_CMD](group__shell__api.md#ga59a835edbd7db3acdcb204248c0cf5fd)(\_expr, \_syntax, \_subcmd, \_help, \_handler) |
|  | Initializes shell command if expression gives non-zero result at compile time. |
| #define | [SHELL\_CMD\_DICT\_CREATE](group__shell__api.md#gaf33b1b20caccad1effe6733603259a00)(\_data, \_handler) |
| #define | [SHELL\_SUBCMD\_DICT\_SET\_CREATE](group__shell__api.md#ga401e19cf8ec8601b8a96fe8e95a2b4d2)(\_name, \_handler, ...) |
|  | Initializes shell dictionary commands. |
| #define | [SHELL\_DEFAULT\_BACKEND\_CONFIG\_FLAGS](group__shell__api.md#ga7e522b107d4e8b687816a86f14b9a885) |
| #define | [SHELL\_DEFINE](group__shell__api.md#ga158405143b49e4888cb135fec83ad22c)(\_name, \_prompt, \_transport\_iface, \_log\_queue\_size, \_log\_timeout, \_shell\_flag) |
|  | Macro for defining a shell instance. |
| #define | [SHELL\_NORMAL](group__shell__api.md#ga4c3a7db0c2bdbf36bbf72302a04bb44d)   [SHELL\_VT100\_COLOR\_DEFAULT](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a32de6063c44948beeb8501fed9b7d18e) |
|  | Terminal default text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_INFO](group__shell__api.md#gaac0ea96fbb5885432dca93174c9ad4e6)   [SHELL\_VT100\_COLOR\_GREEN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2ac6fce9bc89ceb0043697b26cca380c8a) |
|  | Green text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_OPTION](group__shell__api.md#gacc7c6e7b1fc65cc350353cc166da528b)   [SHELL\_VT100\_COLOR\_CYAN](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a618a6789463b1980f1086ee128c65972) |
|  | Cyan text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_WARNING](group__shell__api.md#ga118dd6829e092423a85e2b6de07f8dd3)   [SHELL\_VT100\_COLOR\_YELLOW](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2adb8fbc39eddceb95f523eed8d5c5bf7d) |
|  | Yellow text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [SHELL\_ERROR](group__shell__api.md#ga7664f5e184e9b41ac92e033f7b8d885d)   [SHELL\_VT100\_COLOR\_RED](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2a6f6be6e431dc8e905c5734b4e9c32af4) |
|  | Red text color for [shell\_fprintf](structshell__fprintf.md "fprintf context") function. |
| #define | [shell\_fprintf](group__shell__api.md#ga1fd1671311b112f0c87ab2dafd801105)(sh, color, fmt, ...) |
| #define | [shell\_info](group__shell__api.md#ga9382959c41fe6850c2daa51306b3c5fd)(\_sh, \_ft, ...) |
|  | Print info message to the shell. |
| #define | [shell\_print](group__shell__api.md#ga3126019b2100d1ccb2d4dc5efb7d8228)(\_sh, \_ft, ...) |
|  | Print normal message to the shell. |
| #define | [shell\_warn](group__shell__api.md#ga3d886cfd7b4340b2e71a92bd7c4534d9)(\_sh, \_ft, ...) |
|  | Print warning message to the shell. |
| #define | [shell\_error](group__shell__api.md#ga408141c02209a9549cb9063f24ef3731)(\_sh, \_ft, ...) |
|  | Print error message to the shell. |
| #define | [SHELL\_CMD\_HELP\_PRINTED](group__shell__api.md#ga3be3ecccd6ce1954883c5959c39c7927)   (1) |
|  | Command's help has been printed. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [shell\_dynamic\_get](group__shell__api.md#gafc042f32bac2fdd4cbde9f943e29b008)) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) idx, struct [shell\_static\_entry](structshell__static__entry.md) \*entry) |
|  | Shell dynamic command descriptor. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [shell\_device\_filter\_t](group__shell__api.md#gaa2b8cf8ac78b8355408ef94958ebdc70)) (const struct [device](structdevice.md) \*dev) |
|  | Filter callback type, for use with shell\_device\_lookup\_filter. |
| typedef int(\* | [shell\_cmd\_handler](group__shell__api.md#ga331e7d19b9b0755486596f5ffc598338)) (const struct [shell](structshell.md) \*sh, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) argc, char \*\*argv) |
|  | Shell command handler prototype. |
| typedef int(\* | [shell\_dict\_cmd\_handler](group__shell__api.md#ga182f247052041f1236d13726589885e2)) (const struct [shell](structshell.md) \*sh, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) argc, char \*\*argv, void \*data) |
|  | Shell dictionary command handler prototype. |
| typedef void(\* | [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)) (enum [shell\_transport\_evt](group__shell__api.md#gae77673d4c086f2f9312ceb7933745ee1) evt, void \*context) |
| typedef void(\* | [shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25)) (const struct [shell](structshell.md) \*sh, int res) |
| typedef void(\* | [shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d)) (const struct [shell](structshell.md) \*sh, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bypass callback. |

| Enumerations | |
| --- | --- |
| enum | [shell\_receive\_state](group__shell__api.md#ga8773ed2570714ba4985108b1738d33a0) { [SHELL\_RECEIVE\_DEFAULT](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a201e367896f86499d317d9ec7b59612a) , [SHELL\_RECEIVE\_ESC](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0ab512e3269698524fd025433016b3ad65) , [SHELL\_RECEIVE\_ESC\_SEQ](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a7378b6ecb1a51c53577db5a8eeda936a) , [SHELL\_RECEIVE\_TILDE\_EXP](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0afa2dde3374d3971266652cf48a4d13f7) } |
| enum | [shell\_state](group__shell__api.md#gaf2c6ff9ef31dc06086fd1141763e6266) {     [SHELL\_STATE\_UNINITIALIZED](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a0fcbee7b51ec8d90e7d42a1b455360e6) , [SHELL\_STATE\_INITIALIZED](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266adf8c97c3b6dacfbaf3ace4780cfe3dbd) , [SHELL\_STATE\_ACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8a226ad5c1306dd8f491ad321d334b72) , [SHELL\_STATE\_PANIC\_MODE\_ACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8d01930f8cbdeddda2bf47d0264c4a8b) ,     [SHELL\_STATE\_PANIC\_MODE\_INACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a6423704f7a619e1bfed063cd7455ebfe)   } |
| enum | [shell\_transport\_evt](group__shell__api.md#gae77673d4c086f2f9312ceb7933745ee1) { [SHELL\_TRANSPORT\_EVT\_RX\_RDY](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1aa43ab5965bc3f2c964f206277ab3f1bb) , [SHELL\_TRANSPORT\_EVT\_TX\_RDY](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1a6c78a3534128fac6366d9e5dfda81dfb) } |
|  | Shell transport event. [More...](group__shell__api.md#gae77673d4c086f2f9312ceb7933745ee1) |
| enum | [shell\_signal](group__shell__api.md#ga5cd015de5e7295483fa2cff7d54c2d21) {     [SHELL\_SIGNAL\_RXRDY](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a815c6760bfd5bba8813ea68964bf4713) , [SHELL\_SIGNAL\_LOG\_MSG](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ab8fe52f7b4f43c98dae5188a1dc8547a) , [SHELL\_SIGNAL\_KILL](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ad5c07b5872f785b0731c8aaed0f81c3a) , [SHELL\_SIGNAL\_TXDONE](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a7962ab077b49c816bb9337a9b1b343ed) ,     [SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)   } |
| enum | [shell\_flag](group__shell__api.md#ga56bf30741f9ec7a6d94e5c18c2858948) { [SHELL\_FLAG\_CRLF\_DEFAULT](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab) = (1<<0) , [SHELL\_FLAG\_OLF\_CRLF](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446) = (1<<1) } |
|  | Flags for setting shell output newline sequence. [More...](group__shell__api.md#ga56bf30741f9ec7a6d94e5c18c2858948) |

| Functions | |
| --- | --- |
| const struct [device](structdevice.md) \* | [shell\_device\_lookup](group__shell__api.md#ga571db3aa3e024a09e82b117a74d6f248) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) idx, const char \*prefix) |
|  | Get by index a device that matches . |
| const struct [device](structdevice.md) \* | [shell\_device\_filter](group__shell__api.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) idx, [shell\_device\_filter\_t](group__shell__api.md#gaa2b8cf8ac78b8355408ef94958ebdc70) filter) |
|  | Get a device by index and filter. |
| int | [shell\_init](group__shell__api.md#ga8764ff11603855a10419c48e46e8221c) (const struct [shell](structshell.md) \*sh, const void \*transport\_config, struct [shell\_backend\_config\_flags](structshell__backend__config__flags.md) cfg\_flags, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [log\_backend](structlog__backend.md), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) init\_log\_level) |
|  | Function for initializing a transport layer and internal shell state. |
| void | [shell\_uninit](group__shell__api.md#ga07e76646c5065218464aa8ce78b75af3) (const struct [shell](structshell.md) \*sh, [shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25) cb) |
|  | Uninitializes the transport layer and the internal shell state. |
| int | [shell\_start](group__shell__api.md#gad386d4e8077103e7976f25996fcc3132) (const struct [shell](structshell.md) \*sh) |
|  | Function for starting shell processing. |
| int | [shell\_stop](group__shell__api.md#gad27754d0beb31bc501f28f9ef26a362c) (const struct [shell](structshell.md) \*sh) |
|  | Function for stopping shell processing. |
| void | [shell\_fprintf\_impl](group__shell__api.md#ga863c04af5db00a3804eaff02d401603b) (const struct [shell](structshell.md) \*sh, enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) color, const char \*fmt,...) |
|  | printf-like function which sends formatted data stream to the shell. |
| void | [shell\_vfprintf](group__shell__api.md#ga74a1c4edd803cad14c893fc9816e534f) (const struct [shell](structshell.md) \*sh, enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) color, const char \*fmt, va\_list args) |
|  | vprintf-like function which sends formatted data stream to the shell. |
| void | [shell\_hexdump\_line](group__shell__api.md#ga0b6e69b499c153ae8f7ba256d445f09d) (const struct [shell](structshell.md) \*sh, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Print a line of data in hexadecimal format. |
| void | [shell\_hexdump](group__shell__api.md#gaeeba0b483974205c54e364d509badd42) (const struct [shell](structshell.md) \*sh, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Print data in hexadecimal format. |
| void | [shell\_process](group__shell__api.md#ga7e66389d0faf15a2a7c31c68cdd9c36c) (const struct [shell](structshell.md) \*sh) |
|  | Process function, which should be executed when data is ready in the transport interface. |
| int | [shell\_prompt\_change](group__shell__api.md#ga2113b7227b155755a7ab8a928f7ae499) (const struct [shell](structshell.md) \*sh, const char \*prompt) |
|  | Change displayed shell prompt. |
| void | [shell\_help](group__shell__api.md#gac3c643a0b332cd2f07fe506337784ac0) (const struct [shell](structshell.md) \*sh) |
|  | Prints the current command help. |
| int | [shell\_execute\_cmd](group__shell__api.md#gabfb6a1f1f53f90365de349348015311e) (const struct [shell](structshell.md) \*sh, const char \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Execute command. |
| int | [shell\_set\_root\_cmd](group__shell__api.md#ga768c606f2d50f24e9b607ba0a341686d) (const char \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Set root command for all shell instances. |
| void | [shell\_set\_bypass](group__shell__api.md#ga7514a072c2819fb93fb9d62542c7cc15) (const struct [shell](structshell.md) \*sh, [shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d) bypass) |
|  | Set bypass callback. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [shell\_ready](group__shell__api.md#ga79369ddfea2dc2cb5813c5eb5c67634a) (const struct [shell](structshell.md) \*sh) |
|  | Get shell readiness to execute commands. |
| int | [shell\_insert\_mode\_set](group__shell__api.md#gaf1f41d8b6cd430357d593ab0fc5adfeb) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control text insert mode. |
| int | [shell\_use\_colors\_set](group__shell__api.md#ga7d5873456ba43ebd3cc86d25e3f4a72c) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether terminal output uses colored syntax. |
| int | [shell\_use\_vt100\_set](group__shell__api.md#ga80ff4b3b4cc62e543fd510c14f55b42a) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether terminal is using vt100 commands. |
| int | [shell\_echo\_set](group__shell__api.md#gad53881371bbaedfd3ef3ecf219706fd1) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether user input is echoed back. |
| int | [shell\_obscure\_set](group__shell__api.md#ga86fade2757d04c9220d5912a4ee540a0) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) obscure) |
|  | Allow application to control whether user input is obscured with asterisks – useful for implementing passwords. |
| int | [shell\_mode\_delete\_set](group__shell__api.md#ga2df2997c4b04f3246c22f43b274a353b) (const struct [shell](structshell.md) \*sh, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) val) |
|  | Allow application to control whether the delete key backspaces or deletes. |
| int | [shell\_get\_return\_value](group__shell__api.md#ga54dc053c92641bc9b9736bc2d61140f7) (const struct [shell](structshell.md) \*sh) |
|  | Retrieve return value of most recently executed shell command. |

| Variables | |
| --- | --- |
| const struct [log\_backend\_api](structlog__backend__api.md) | [log\_backend\_shell\_api](group__shell__api.md#gaddf27615ed72440ecb63aa1d84962c82) |

## Macro Definition Documentation

## [◆ ](#abb162a9a784f605dea4b02a0a6cc0c16)CONFIG\_SHELL\_CMD\_BUFF\_SIZE

| #define CONFIG\_SHELL\_CMD\_BUFF\_SIZE   0 |
| --- |

## [◆ ](#ab194ada3483ec28f093fd9521b19265e)CONFIG\_SHELL\_HISTORY\_BUFFER

| #define CONFIG\_SHELL\_HISTORY\_BUFFER   0 |
| --- |

## [◆ ](#af54e892edba822e46ca70cb6eca48146)CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE

| #define CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE   0 |
| --- |

## [◆ ](#a81357b82642c8910ae3fb920cb885370)CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE

| #define CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE   0 |
| --- |

## [◆ ](#af3a0fbf2152aa4578d29d98000b4d74e)SHELL\_HEXDUMP\_BYTES\_IN\_LINE

| #define SHELL\_HEXDUMP\_BYTES\_IN\_LINE   16 |
| --- |

## [◆ ](#a0e2b3ac54184ae15f13e2024df1ac69b)SHELL\_OPT\_ARG\_CHECK\_SKIP

| #define SHELL\_OPT\_ARG\_CHECK\_SKIP   (0xFF) |
| --- |

Flag indicating that number of optional arguments is not limited.

## [◆ ](#aba166d98da7258a2a50abc94c1b744c8)SHELL\_OPT\_ARG\_MAX

| #define SHELL\_OPT\_ARG\_MAX   (0xFD) |
| --- |

Flag indicating maximum number of optional arguments that can be validated.

## [◆ ](#a2b64d0c6e086ea227e85fe50312896f7)SHELL\_OPT\_ARG\_RAW

| #define SHELL\_OPT\_ARG\_RAW   (0xFE) |
| --- |

Flag indicates that optional arguments will be treated as one, unformatted argument.

By default, shell is parsing all arguments, treats all spaces as argument separators unless they are within quotation marks which are removed in that case. If command rely on unformatted argument then this flag shall be used in place of number of optional arguments in command definition to indicate that only mandatory arguments shall be parsed and remaining command string is passed as a raw string.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell.h](shell_2shell_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
