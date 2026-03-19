---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shell_2shell_8h_source.html
original_path: doxygen/html/shell_2shell_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell.h

[Go to the documentation of this file.](shell_2shell_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_H\_\_

8#define SHELL\_H\_\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/shell/shell\_types.h](shell__types_8h.md)>

12#include <[zephyr/shell/shell\_history.h](shell__history_8h.md)>

13#include <[zephyr/shell/shell\_fprintf.h](shell__fprintf_8h.md)>

14#include <[zephyr/shell/shell\_log\_backend.h](shell__log__backend_8h.md)>

15#include <[zephyr/shell/shell\_string\_conv.h](shell__string__conv_8h.md)>

16#include <[zephyr/logging/log\_instance.h](log__instance_8h.md)>

17#include <[zephyr/logging/log.h](log_8h.md)>

18#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

19#include <[zephyr/sys/util.h](sys_2util_8h.md)>

20

21#if defined CONFIG\_SHELL\_GETOPT

22#include <getopt.h>

23#endif

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29#ifndef CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE

[ 30](shell_2shell_8h.md#a81357b82642c8910ae3fb920cb885370)#define CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE 0

31#endif

32

33#ifndef CONFIG\_SHELL\_CMD\_BUFF\_SIZE

[ 34](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)#define CONFIG\_SHELL\_CMD\_BUFF\_SIZE 0

35#endif

36

37#ifndef CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE

[ 38](shell_2shell_8h.md#af54e892edba822e46ca70cb6eca48146)#define CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE 0

39#endif

40

41#ifndef CONFIG\_SHELL\_HISTORY\_BUFFER

[ 42](shell_2shell_8h.md#ab194ada3483ec28f093fd9521b19265e)#define CONFIG\_SHELL\_HISTORY\_BUFFER 0

43#endif

44

45#define Z\_SHELL\_CMD\_ROOT\_LVL (0u)

46

[ 47](shell_2shell_8h.md#af3a0fbf2152aa4578d29d98000b4d74e)#define SHELL\_HEXDUMP\_BYTES\_IN\_LINE 16

48

[ 60](shell_2shell_8h.md#a2b64d0c6e086ea227e85fe50312896f7)#define SHELL\_OPT\_ARG\_RAW (0xFE)

61

[ 65](shell_2shell_8h.md#a0e2b3ac54184ae15f13e2024df1ac69b)#define SHELL\_OPT\_ARG\_CHECK\_SKIP (0xFF)

66

[ 71](shell_2shell_8h.md#aba166d98da7258a2a50abc94c1b744c8)#define SHELL\_OPT\_ARG\_MAX (0xFD)

72

81

82struct [shell\_static\_entry](structshell__static__entry.md);

83

[ 95](group__shell__api.md#gafc042f32bac2fdd4cbde9f943e29b008)typedef void (\*[shell\_dynamic\_get](group__shell__api.md#gafc042f32bac2fdd4cbde9f943e29b008))(size\_t idx,

96 struct [shell\_static\_entry](structshell__static__entry.md) \*entry);

97

[ 101](unionshell__cmd__entry.md)union [shell\_cmd\_entry](unionshell__cmd__entry.md) {

[ 103](unionshell__cmd__entry.md#aa76e35866f5df37593705fd1b53e15df) [shell\_dynamic\_get](group__shell__api.md#gafc042f32bac2fdd4cbde9f943e29b008) [dynamic\_get](unionshell__cmd__entry.md#aa76e35866f5df37593705fd1b53e15df);

104

[ 106](unionshell__cmd__entry.md#a4abb8327df0e62f63432a05cc885f03d) const struct [shell\_static\_entry](structshell__static__entry.md) \*[entry](unionshell__cmd__entry.md#a4abb8327df0e62f63432a05cc885f03d);

107};

108

109struct [shell](structshell.md);

110

[ 111](structshell__static__args.md)struct [shell\_static\_args](structshell__static__args.md) {

[ 112](structshell__static__args.md#a2c23bfa755d3bb651e299ff461065d98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mandatory](structshell__static__args.md#a2c23bfa755d3bb651e299ff461065d98);

[ 113](structshell__static__args.md#aa3aa836ed537dde38e64d2c677ace5ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [optional](structshell__static__args.md#aa3aa836ed537dde38e64d2c677ace5ae);

114};

115

[ 131](group__shell__api.md#ga571db3aa3e024a09e82b117a74d6f248)const struct [device](structdevice.md) \*[shell\_device\_lookup](group__shell__api.md#ga571db3aa3e024a09e82b117a74d6f248)(size\_t idx,

132 const char \*prefix);

133

[ 144](group__shell__api.md#gaa2b8cf8ac78b8355408ef94958ebdc70)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[shell\_device\_filter\_t](group__shell__api.md#gaa2b8cf8ac78b8355408ef94958ebdc70))(const struct [device](structdevice.md) \*dev);

145

[ 159](group__shell__api.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d)const struct [device](structdevice.md) \*[shell\_device\_filter](group__shell__api.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d)(size\_t idx,

160 [shell\_device\_filter\_t](group__shell__api.md#gaa2b8cf8ac78b8355408ef94958ebdc70) filter);

161

[ 182](group__shell__api.md#ga7fb40045dc0a27c175e37a6c9cd84b53)const struct [device](structdevice.md) \*[shell\_device\_get\_binding](group__shell__api.md#ga7fb40045dc0a27c175e37a6c9cd84b53)(const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d));

183

[ 196](group__shell__api.md#ga331e7d19b9b0755486596f5ffc598338)typedef int (\*[shell\_cmd\_handler](group__shell__api.md#ga331e7d19b9b0755486596f5ffc598338))(const struct [shell](structshell.md) \*sh,

197 size\_t argc, char \*\*argv);

198

[ 212](group__shell__api.md#ga182f247052041f1236d13726589885e2)typedef int (\*[shell\_dict\_cmd\_handler](group__shell__api.md#ga182f247052041f1236d13726589885e2))(const struct [shell](structshell.md) \*sh, size\_t argc,

213 char \*\*argv, void \*data);

214

215/\* When entries are added to the memory section a padding is applied for

216 \* the posix architecture with 64bits builds and x86\_64 targets. Adding padding to allow handle data

217 \* in the memory section as array.

218 \*/

219#if (defined(CONFIG\_ARCH\_POSIX) && defined(CONFIG\_64BIT)) || defined(CONFIG\_X86\_64)

220#define Z\_SHELL\_STATIC\_ENTRY\_PADDING 24

221#else

222#define Z\_SHELL\_STATIC\_ENTRY\_PADDING 0

223#endif

224

225/\*

226 \* @brief Shell static command descriptor.

227 \*/

[ 228](structshell__static__entry.md)struct [shell\_static\_entry](structshell__static__entry.md) {

[ 229](structshell__static__entry.md#ad87defa749ee7481f6d29d8c9084fb91) const char \*[syntax](structshell__static__entry.md#ad87defa749ee7481f6d29d8c9084fb91);

[ 230](structshell__static__entry.md#ac8fb0fc23957a49d9a3664b5baa08704) const char \*[help](structshell__static__entry.md#ac8fb0fc23957a49d9a3664b5baa08704);

[ 231](structshell__static__entry.md#a14534428d81f5ffeb303a5320766cd0a) const union [shell\_cmd\_entry](unionshell__cmd__entry.md) \*[subcmd](structshell__static__entry.md#a14534428d81f5ffeb303a5320766cd0a);

[ 232](structshell__static__entry.md#a3147eb0cc1fea698dd433127acb1f220) [shell\_cmd\_handler](group__shell__api.md#ga331e7d19b9b0755486596f5ffc598338) [handler](structshell__static__entry.md#a3147eb0cc1fea698dd433127acb1f220);

[ 233](structshell__static__entry.md#a73951d31712342c0c0545a142059d367) struct [shell\_static\_args](structshell__static__args.md) [args](structshell__static__entry.md#a73951d31712342c0c0545a142059d367);

[ 234](structshell__static__entry.md#a1ca7de0e195f0f840cd04e4c69b20f80) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [padding](structshell__static__entry.md#a1ca7de0e195f0f840cd04e4c69b20f80)[Z\_SHELL\_STATIC\_ENTRY\_PADDING];

235};

236

[ 252](group__shell__api.md#gae8a8bbcbb842027c02a319b3fb976a3d)#define SHELL\_CMD\_ARG\_REGISTER(syntax, subcmd, help, handler, \

253 mandatory, optional) \

254 static const struct shell\_static\_entry UTIL\_CAT(\_shell\_, syntax) = \

255 SHELL\_CMD\_ARG(syntax, subcmd, help, handler, mandatory, optional); \

256 static const TYPE\_SECTION\_ITERABLE(union shell\_cmd\_entry, \

257 UTIL\_CAT(shell\_cmd\_, syntax), shell\_root\_cmds, \

258 UTIL\_CAT(shell\_cmd\_, syntax) \

259 ) = { \

260 .entry = &UTIL\_CAT(\_shell\_, syntax) \

261 }

262

[ 283](group__shell__api.md#ga6a3ed4ea9051ac138d22cc39134fb2e5)#define SHELL\_COND\_CMD\_ARG\_REGISTER(flag, syntax, subcmd, help, handler, \

284 mandatory, optional) \

285 COND\_CODE\_1(\

286 flag, \

287 (\

288 SHELL\_CMD\_ARG\_REGISTER(syntax, subcmd, help, handler, \

289 mandatory, optional) \

290 ), \

291 (\

292 static shell\_cmd\_handler dummy\_##syntax##\_handler \_\_unused = \

293 handler;\

294 static const union shell\_cmd\_entry \*dummy\_subcmd\_##syntax \

295 \_\_unused = subcmd\

296 ) \

297 )

[ 309](group__shell__api.md#ga06060b98eb505300a3dcc8f922a8e7ab)#define SHELL\_CMD\_REGISTER(syntax, subcmd, help, handler) \

310 SHELL\_CMD\_ARG\_REGISTER(syntax, subcmd, help, handler, 0, 0)

311

[ 325](group__shell__api.md#ga62782121ece6af076407c94935ec94e4)#define SHELL\_COND\_CMD\_REGISTER(flag, syntax, subcmd, help, handler) \

326 SHELL\_COND\_CMD\_ARG\_REGISTER(flag, syntax, subcmd, help, handler, 0, 0)

327

[ 346](group__shell__api.md#gacb2d1a969368efdbeec704ee6e962dee)#define SHELL\_STATIC\_SUBCMD\_SET\_CREATE(name, ...) \

347 static const struct shell\_static\_entry shell\_##name[] = { \

348 \_\_VA\_ARGS\_\_ \

349 }; \

350 static const union shell\_cmd\_entry name = { \

351 .entry = shell\_##name \

352 }

353

354#define Z\_SHELL\_UNDERSCORE(x) \_##x

355#define Z\_SHELL\_SUBCMD\_NAME(...) \

356 UTIL\_CAT(shell\_subcmds, MACRO\_MAP\_CAT(Z\_SHELL\_UNDERSCORE, \_\_VA\_ARGS\_\_))

357#define Z\_SHELL\_SUBCMD\_SECTION\_TAG(...) MACRO\_MAP\_CAT(Z\_SHELL\_UNDERSCORE, \_\_VA\_ARGS\_\_)

358#define Z\_SHELL\_SUBCMD\_SET\_SECTION\_TAG(x) \

359 Z\_SHELL\_SUBCMD\_SECTION\_TAG(NUM\_VA\_ARGS\_LESS\_1 x, \_\_DEBRACKET x)

360#define Z\_SHELL\_SUBCMD\_ADD\_SECTION\_TAG(x, y) \

361 Z\_SHELL\_SUBCMD\_SECTION\_TAG(NUM\_VA\_ARGS\_LESS\_1 x, \_\_DEBRACKET x, y)

362

374

[ 375](group__shell__api.md#ga1e314886b70ee2e7e0763cd945a1a988)#define SHELL\_SUBCMD\_SET\_CREATE(\_name, \_parent) \

376 static const TYPE\_SECTION\_ITERABLE(struct shell\_static\_entry, \_name, shell\_subcmds, \

377 Z\_SHELL\_SUBCMD\_SET\_SECTION\_TAG(\_parent))

378

379

[ 399](group__shell__api.md#gab1b643efbaee748be0256e904642e310)#define SHELL\_SUBCMD\_COND\_ADD(\_flag, \_parent, \_syntax, \_subcmd, \_help, \_handler, \

400 \_mand, \_opt) \

401 COND\_CODE\_1(\_flag, \

402 (static const TYPE\_SECTION\_ITERABLE(struct shell\_static\_entry, \

403 Z\_SHELL\_SUBCMD\_NAME(\_\_DEBRACKET \_parent, \_syntax), \

404 shell\_subcmds, \

405 Z\_SHELL\_SUBCMD\_ADD\_SECTION\_TAG(\_parent, \_syntax)) = \

406 SHELL\_EXPR\_CMD\_ARG(1, \_syntax, \_subcmd, \_help, \

407 \_handler, \_mand, \_opt)\

408 ), \

409 (static shell\_cmd\_handler dummy\_handler\_##\_syntax \_\_unused = \_handler;\

410 static const union shell\_cmd\_entry dummy\_subcmd\_##\_syntax \_\_unused = { \

411 .entry = (const struct shell\_static\_entry \*)\_subcmd\

412 } \

413 ) \

414 )

415

[ 428](group__shell__api.md#ga85b0afcacd3831bf5c724590765e035f)#define SHELL\_SUBCMD\_ADD(\_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt) \

429 SHELL\_SUBCMD\_COND\_ADD(1, \_parent, \_syntax, \_subcmd, \_help, \_handler, \_mand, \_opt)

430

[ 435](group__shell__api.md#ga4f7a3432f76541eb226a426507e10174)#define SHELL\_SUBCMD\_SET\_END {NULL}

436

[ 443](group__shell__api.md#gafa6d91c36c36eb68d3f241ed0c7e7131)#define SHELL\_DYNAMIC\_CMD\_CREATE(name, get) \

444 static const TYPE\_SECTION\_ITERABLE(union shell\_cmd\_entry, name, \

445 shell\_dynamic\_subcmds, name) = \

446 { \

447 .dynamic\_get = get \

448 }

449

[ 463](group__shell__api.md#gad762c496a2ced65069b6d1d02a4d925c)#define SHELL\_CMD\_ARG(syntax, subcmd, help, handler, mand, opt) \

464 SHELL\_EXPR\_CMD\_ARG(1, syntax, subcmd, help, handler, mand, opt)

465

[ 485](group__shell__api.md#ga68229f89484c3459d77cebb450ee1f24)#define SHELL\_COND\_CMD\_ARG(flag, syntax, subcmd, help, handler, mand, opt) \

486 SHELL\_EXPR\_CMD\_ARG(IS\_ENABLED(flag), syntax, subcmd, help, \

487 handler, mand, opt)

488

[ 508](group__shell__api.md#ga6b07c55dd7d42873d604ae299b3cfdf9)#define SHELL\_EXPR\_CMD\_ARG(\_expr, \_syntax, \_subcmd, \_help, \_handler, \

509 \_mand, \_opt) \

510 { \

511 .syntax = (\_expr) ? (const char \*)STRINGIFY(\_syntax) : "", \

512 .help = (\_expr) ? (const char \*)\_help : NULL, \

513 .subcmd = (const union shell\_cmd\_entry \*)((\_expr) ? \

514 \_subcmd : NULL), \

515 .handler = (shell\_cmd\_handler)((\_expr) ? \_handler : NULL), \

516 .args = { .mandatory = \_mand, .optional = \_opt} \

517 }

518

[ 527](group__shell__api.md#ga24ade9db85af9a8776a45ba0084f4cca)#define SHELL\_CMD(\_syntax, \_subcmd, \_help, \_handler) \

528 SHELL\_CMD\_ARG(\_syntax, \_subcmd, \_help, \_handler, 0, 0)

529

[ 542](group__shell__api.md#ga6e27d86443067df4792623f1a04d1ee1)#define SHELL\_COND\_CMD(\_flag, \_syntax, \_subcmd, \_help, \_handler) \

543 SHELL\_COND\_CMD\_ARG(\_flag, \_syntax, \_subcmd, \_help, \_handler, 0, 0)

544

[ 558](group__shell__api.md#ga59a835edbd7db3acdcb204248c0cf5fd)#define SHELL\_EXPR\_CMD(\_expr, \_syntax, \_subcmd, \_help, \_handler) \

559 SHELL\_EXPR\_CMD\_ARG(\_expr, \_syntax, \_subcmd, \_help, \_handler, 0, 0)

560

561/\* Internal macro used for creating handlers for dictionary commands. \*/

562#define Z\_SHELL\_CMD\_DICT\_HANDLER\_CREATE(\_data, \_handler) \

563static int UTIL\_CAT(UTIL\_CAT(cmd\_dict\_, UTIL\_CAT(\_handler, \_)), \

564 GET\_ARG\_N(1, \_\_DEBRACKET \_data))( \

565 const struct shell \*sh, size\_t argc, char \*\*argv) \

566{ \

567 return \_handler(sh, argc, argv, \

568 (void \*)GET\_ARG\_N(2, \_\_DEBRACKET \_data)); \

569}

570

571/\* Internal macro used for creating dictionary commands. \*/

[ 572](group__shell__api.md#gaf33b1b20caccad1effe6733603259a00)#define SHELL\_CMD\_DICT\_CREATE(\_data, \_handler) \

573 SHELL\_CMD\_ARG(GET\_ARG\_N(1, \_\_DEBRACKET \_data), NULL, GET\_ARG\_N(3, \_\_DEBRACKET \_data), \

574 UTIL\_CAT(UTIL\_CAT(cmd\_dict\_, UTIL\_CAT(\_handler, \_)), \

575 GET\_ARG\_N(1, \_\_DEBRACKET \_data)), 1, 0)

576

[ 610](group__shell__api.md#ga401e19cf8ec8601b8a96fe8e95a2b4d2)#define SHELL\_SUBCMD\_DICT\_SET\_CREATE(\_name, \_handler, ...) \

611 FOR\_EACH\_FIXED\_ARG(Z\_SHELL\_CMD\_DICT\_HANDLER\_CREATE, (), \

612 \_handler, \_\_VA\_ARGS\_\_) \

613 SHELL\_STATIC\_SUBCMD\_SET\_CREATE(\_name, \

614 FOR\_EACH\_FIXED\_ARG(SHELL\_CMD\_DICT\_CREATE, (,), \_handler, \_\_VA\_ARGS\_\_), \

615 SHELL\_SUBCMD\_SET\_END \

616 )

617

[ 622](group__shell__api.md#ga8773ed2570714ba4985108b1738d33a0)enum [shell\_receive\_state](group__shell__api.md#ga8773ed2570714ba4985108b1738d33a0) {

[ 623](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a201e367896f86499d317d9ec7b59612a) [SHELL\_RECEIVE\_DEFAULT](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a201e367896f86499d317d9ec7b59612a),

[ 624](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0ab512e3269698524fd025433016b3ad65) [SHELL\_RECEIVE\_ESC](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0ab512e3269698524fd025433016b3ad65),

[ 625](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a7378b6ecb1a51c53577db5a8eeda936a) [SHELL\_RECEIVE\_ESC\_SEQ](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a7378b6ecb1a51c53577db5a8eeda936a),

[ 626](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0afa2dde3374d3971266652cf48a4d13f7) [SHELL\_RECEIVE\_TILDE\_EXP](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0afa2dde3374d3971266652cf48a4d13f7)

627};

628

[ 632](group__shell__api.md#gaf2c6ff9ef31dc06086fd1141763e6266)enum [shell\_state](group__shell__api.md#gaf2c6ff9ef31dc06086fd1141763e6266) {

[ 633](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a0fcbee7b51ec8d90e7d42a1b455360e6) [SHELL\_STATE\_UNINITIALIZED](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a0fcbee7b51ec8d90e7d42a1b455360e6),

[ 634](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266adf8c97c3b6dacfbaf3ace4780cfe3dbd) [SHELL\_STATE\_INITIALIZED](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266adf8c97c3b6dacfbaf3ace4780cfe3dbd),

[ 635](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8a226ad5c1306dd8f491ad321d334b72) [SHELL\_STATE\_ACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8a226ad5c1306dd8f491ad321d334b72),

[ 636](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8d01930f8cbdeddda2bf47d0264c4a8b) [SHELL\_STATE\_PANIC\_MODE\_ACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8d01930f8cbdeddda2bf47d0264c4a8b),

[ 637](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a6423704f7a619e1bfed063cd7455ebfe) [SHELL\_STATE\_PANIC\_MODE\_INACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a6423704f7a619e1bfed063cd7455ebfe)

638};

639

[ 641](group__shell__api.md#gae77673d4c086f2f9312ceb7933745ee1)enum [shell\_transport\_evt](group__shell__api.md#gae77673d4c086f2f9312ceb7933745ee1) {

[ 642](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1aa43ab5965bc3f2c964f206277ab3f1bb) [SHELL\_TRANSPORT\_EVT\_RX\_RDY](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1aa43ab5965bc3f2c964f206277ab3f1bb),

[ 643](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1a6c78a3534128fac6366d9e5dfda81dfb) [SHELL\_TRANSPORT\_EVT\_TX\_RDY](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1a6c78a3534128fac6366d9e5dfda81dfb)

644};

645

[ 646](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)typedef void (\*[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d))(enum [shell\_transport\_evt](group__shell__api.md#gae77673d4c086f2f9312ceb7933745ee1) evt,

647 void \*context);

648

649

[ 650](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25)typedef void (\*[shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25))(const struct [shell](structshell.md) \*sh, int res);

651

[ 658](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d)typedef void (\*[shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d))(const struct [shell](structshell.md) \*sh,

659 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

660 size\_t len);

661

662struct [shell\_transport](structshell__transport.md);

663

[ 668](structshell__transport__api.md)struct [shell\_transport\_api](structshell__transport__api.md) {

[ 680](structshell__transport__api.md#a59afba962312a077343b440448d67135) int (\*[init](structshell__transport__api.md#a59afba962312a077343b440448d67135))(const struct [shell\_transport](structshell__transport.md) \*transport,

681 const void \*config,

682 [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) evt\_handler,

683 void \*context);

684

[ 692](structshell__transport__api.md#a94cc7843174a4aba668389a4b46928d3) int (\*[uninit](structshell__transport__api.md#a94cc7843174a4aba668389a4b46928d3))(const struct [shell\_transport](structshell__transport.md) \*transport);

693

[ 706](structshell__transport__api.md#a95535c7195088e68230ecb306f105713) int (\*[enable](structshell__transport__api.md#a95535c7195088e68230ecb306f105713))(const struct [shell\_transport](structshell__transport.md) \*transport,

707 bool blocking\_tx);

708

[ 719](structshell__transport__api.md#a6bbf2905abcbf6ca564ecf3f07d95712) int (\*[write](structshell__transport__api.md#a6bbf2905abcbf6ca564ecf3f07d95712))(const struct [shell\_transport](structshell__transport.md) \*transport,

720 const void \*data, size\_t length, size\_t \*cnt);

721

[ 732](structshell__transport__api.md#aae0e8ad92065dbff10691c28045d0c8f) int (\*[read](structshell__transport__api.md#aae0e8ad92065dbff10691c28045d0c8f))(const struct [shell\_transport](structshell__transport.md) \*transport,

733 void \*data, size\_t length, size\_t \*cnt);

734

[ 742](structshell__transport__api.md#a3b447d16d7c30f994c582d67bde57ba8) void (\*[update](structshell__transport__api.md#a3b447d16d7c30f994c582d67bde57ba8))(const struct [shell\_transport](structshell__transport.md) \*transport);

743

744};

745

[ 746](structshell__transport.md)struct [shell\_transport](structshell__transport.md) {

[ 747](structshell__transport.md#ab4bee270415b445ded5a8ba6e8cb3a25) const struct [shell\_transport\_api](structshell__transport__api.md) \*[api](structshell__transport.md#ab4bee270415b445ded5a8ba6e8cb3a25);

[ 748](structshell__transport.md#a02f44bb376152452f5b5d20f33ccbdf6) void \*[ctx](structshell__transport.md#a02f44bb376152452f5b5d20f33ccbdf6);

749};

750

[ 754](structshell__stats.md)struct [shell\_stats](structshell__stats.md) {

[ 755](structshell__stats.md#a1ec10ba96a7805f10d1a021ff1dd3bf2) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [log\_lost\_cnt](structshell__stats.md#a1ec10ba96a7805f10d1a021ff1dd3bf2);

756};

757

758#ifdef CONFIG\_SHELL\_STATS

759#define Z\_SHELL\_STATS\_DEFINE(\_name) static struct shell\_stats \_name##\_stats

760#define Z\_SHELL\_STATS\_PTR(\_name) (&(\_name##\_stats))

761#else

762#define Z\_SHELL\_STATS\_DEFINE(\_name)

763#define Z\_SHELL\_STATS\_PTR(\_name) NULL

764#endif /\* CONFIG\_SHELL\_STATS \*/

765

[ 769](structshell__backend__config__flags.md)struct [shell\_backend\_config\_flags](structshell__backend__config__flags.md) {

[ 770](structshell__backend__config__flags.md#ab1df6f41078d4ec2a94f158e62bbfada) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [insert\_mode](structshell__backend__config__flags.md#ab1df6f41078d4ec2a94f158e62bbfada) :1;

[ 771](structshell__backend__config__flags.md#a5745ea5cab202ee446f460b980c5c532) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [echo](structshell__backend__config__flags.md#a5745ea5cab202ee446f460b980c5c532) :1;

[ 772](structshell__backend__config__flags.md#af794ac9c19b948ed733024a2db5b8bbd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [obscure](structshell__backend__config__flags.md#af794ac9c19b948ed733024a2db5b8bbd) :1;

[ 773](structshell__backend__config__flags.md#a231bc4762cac1c07a6f866c5ecf3a024) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mode\_delete](structshell__backend__config__flags.md#a231bc4762cac1c07a6f866c5ecf3a024) :1;

[ 774](structshell__backend__config__flags.md#af810ff3fba00527cb0561a75b70fec09) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [use\_colors](structshell__backend__config__flags.md#af810ff3fba00527cb0561a75b70fec09) :1;

[ 775](structshell__backend__config__flags.md#a0d017df8e9d9609f2830829d8720b9cf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [use\_vt100](structshell__backend__config__flags.md#a0d017df8e9d9609f2830829d8720b9cf) :1;

776};

777

778BUILD\_ASSERT((sizeof(struct [shell\_backend\_config\_flags](structshell__backend__config__flags.md)) == sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))),

779 "Structure must fit in 4 bytes");

780

[ 784](group__shell__api.md#ga7e522b107d4e8b687816a86f14b9a885)#define SHELL\_DEFAULT\_BACKEND\_CONFIG\_FLAGS \

785{ \

786 .insert\_mode = 0, \

787 .echo = 1, \

788 .obscure = IS\_ENABLED(CONFIG\_SHELL\_START\_OBSCURED), \

789 .mode\_delete = 1, \

790 .use\_colors = 1, \

791 .use\_vt100 = 1, \

792};

793

[ 794](structshell__backend__ctx__flags.md)struct [shell\_backend\_ctx\_flags](structshell__backend__ctx__flags.md) {

[ 795](structshell__backend__ctx__flags.md#a7dc2cd17fb1dd9d538dbde3ad7bbe8e9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [processing](structshell__backend__ctx__flags.md#a7dc2cd17fb1dd9d538dbde3ad7bbe8e9) :1;

[ 796](structshell__backend__ctx__flags.md#a662cf22a29856d07ec64b72db004582f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_rdy](structshell__backend__ctx__flags.md#a662cf22a29856d07ec64b72db004582f) :1;

[ 797](structshell__backend__ctx__flags.md#a85b0069c7b0df219cefec0f73cb313d3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [history\_exit](structshell__backend__ctx__flags.md#a85b0069c7b0df219cefec0f73cb313d3) :1;

[ 798](structshell__backend__ctx__flags.md#a7f597db455b0875c9ff11c4ce50cfd92) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [last\_nl](structshell__backend__ctx__flags.md#a7f597db455b0875c9ff11c4ce50cfd92) :8;

[ 799](structshell__backend__ctx__flags.md#adfa22b07dc65e72e24be400d95da11c8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd\_ctx](structshell__backend__ctx__flags.md#adfa22b07dc65e72e24be400d95da11c8) :1;

[ 800](structshell__backend__ctx__flags.md#a18b3c018f2da6a925f50266bda095483) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [print\_noinit](structshell__backend__ctx__flags.md#a18b3c018f2da6a925f50266bda095483) :1;

[ 801](structshell__backend__ctx__flags.md#a2d6c2561aa6ed28a3978e3b70d079008) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sync\_mode](structshell__backend__ctx__flags.md#a2d6c2561aa6ed28a3978e3b70d079008) :1;

[ 802](structshell__backend__ctx__flags.md#a735602bed33c01e8e548200656fd7ff4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [handle\_log](structshell__backend__ctx__flags.md#a735602bed33c01e8e548200656fd7ff4) :1;

803};

804

805BUILD\_ASSERT((sizeof(struct [shell\_backend\_ctx\_flags](structshell__backend__ctx__flags.md)) == sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))),

806 "Structure must fit in 4 bytes");

807

[ 811](unionshell__backend__cfg.md)union [shell\_backend\_cfg](unionshell__backend__cfg.md) {

[ 812](unionshell__backend__cfg.md#a2e2aa4e52af6f6e6a827ea946e6681fc) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [value](unionshell__backend__cfg.md#a2e2aa4e52af6f6e6a827ea946e6681fc);

[ 813](unionshell__backend__cfg.md#a513e4e2c352c62d13ed655049a7ee691) struct [shell\_backend\_config\_flags](structshell__backend__config__flags.md) [flags](unionshell__backend__cfg.md#a513e4e2c352c62d13ed655049a7ee691);

814};

815

[ 819](unionshell__backend__ctx.md)union [shell\_backend\_ctx](unionshell__backend__ctx.md) {

[ 820](unionshell__backend__ctx.md#a8de68016e888b8f9b5371c8a7bed4fcb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [value](unionshell__backend__ctx.md#a8de68016e888b8f9b5371c8a7bed4fcb);

[ 821](unionshell__backend__ctx.md#a12e5e07c77eb1f82bac9db6cd2d31316) struct [shell\_backend\_ctx\_flags](structshell__backend__ctx__flags.md) [flags](unionshell__backend__ctx.md#a12e5e07c77eb1f82bac9db6cd2d31316);

822};

823

[ 824](group__shell__api.md#ga5cd015de5e7295483fa2cff7d54c2d21)enum [shell\_signal](group__shell__api.md#ga5cd015de5e7295483fa2cff7d54c2d21) {

[ 825](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a815c6760bfd5bba8813ea68964bf4713) [SHELL\_SIGNAL\_RXRDY](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a815c6760bfd5bba8813ea68964bf4713),

[ 826](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ab8fe52f7b4f43c98dae5188a1dc8547a) [SHELL\_SIGNAL\_LOG\_MSG](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ab8fe52f7b4f43c98dae5188a1dc8547a),

[ 827](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ad5c07b5872f785b0731c8aaed0f81c3a) [SHELL\_SIGNAL\_KILL](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ad5c07b5872f785b0731c8aaed0f81c3a),

[ 828](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a7962ab077b49c816bb9337a9b1b343ed) [SHELL\_SIGNAL\_TXDONE](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a7962ab077b49c816bb9337a9b1b343ed), /\* TXDONE must be last one before SHELL\_SIGNALS \*/

[ 829](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e) [SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)

830};

831

[ 835](structshell__ctx.md)struct [shell\_ctx](structshell__ctx.md) {

836#if defined(CONFIG\_SHELL\_PROMPT\_CHANGE) && CONFIG\_SHELL\_PROMPT\_CHANGE

837 char [prompt](structshell__ctx.md#a261d4754f4bf3764298e264ed6e87eff)[[CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE](shell_2shell_8h.md#a81357b82642c8910ae3fb920cb885370)];

838#else

[ 839](structshell__ctx.md#a261d4754f4bf3764298e264ed6e87eff) const char \*[prompt](structshell__ctx.md#a261d4754f4bf3764298e264ed6e87eff);

840#endif

841

[ 842](structshell__ctx.md#a7388fd2e850fcf37c4a421cda13661e8) enum [shell\_state](group__shell__api.md#gaf2c6ff9ef31dc06086fd1141763e6266) [state](structshell__ctx.md#a7388fd2e850fcf37c4a421cda13661e8);

[ 843](structshell__ctx.md#abc4135f23c4738fcf6a2c9d8f45d516b) enum [shell\_receive\_state](group__shell__api.md#ga8773ed2570714ba4985108b1738d33a0) [receive\_state](structshell__ctx.md#abc4135f23c4738fcf6a2c9d8f45d516b);

844

[ 846](structshell__ctx.md#a3df8f9a293b4c24d81a80af2d0e0c44e) struct [shell\_static\_entry](structshell__static__entry.md) [active\_cmd](structshell__ctx.md#a3df8f9a293b4c24d81a80af2d0e0c44e);

847

[ 849](structshell__ctx.md#a0e9321e8954a7598cb6521f660480a88) const struct [shell\_static\_entry](structshell__static__entry.md) \*[selected\_cmd](structshell__ctx.md#a0e9321e8954a7598cb6521f660480a88);

850

[ 852](structshell__ctx.md#a25b945fcaba216e039124aacec660600) struct [shell\_vt100\_ctx](structshell__vt100__ctx.md) [vt100\_ctx](structshell__ctx.md#a25b945fcaba216e039124aacec660600);

853

[ 857](structshell__ctx.md#a0ec61f11544cb817bbd46ed4aa332123) [shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25) [uninit\_cb](structshell__ctx.md#a0ec61f11544cb817bbd46ed4aa332123);

858

[ 860](structshell__ctx.md#a8e02d1d9a521379ad4188b4678cc6071) [shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d) [bypass](structshell__ctx.md#a8e02d1d9a521379ad4188b4678cc6071);

861

[ 863](structshell__ctx.md#a3e6374150abdb9cd4875024eb6f7c5ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_level](structshell__ctx.md#a3e6374150abdb9cd4875024eb6f7c5ea);

864

865#if defined CONFIG\_SHELL\_GETOPT

867 struct getopt\_state getopt;

868#endif

869

[ 870](structshell__ctx.md#a948d78719efe7f01b8edf151e1435af6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cmd\_buff\_len](structshell__ctx.md#a948d78719efe7f01b8edf151e1435af6);

[ 871](structshell__ctx.md#a9a8f69e6876e4788ef3961dfb769e53f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cmd\_buff\_pos](structshell__ctx.md#a9a8f69e6876e4788ef3961dfb769e53f);

872

[ 873](structshell__ctx.md#a5dfe5d3b2e27b67a7a78d5c3ad32ff1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cmd\_tmp\_buff\_len](structshell__ctx.md#a5dfe5d3b2e27b67a7a78d5c3ad32ff1d);

874

[ 876](structshell__ctx.md#a385014f2fba5cae182c3520ec934cce6) char [cmd\_buff](structshell__ctx.md#a385014f2fba5cae182c3520ec934cce6)[[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)];

877

[ 879](structshell__ctx.md#a35085b30e92b913b16f02496c5ec6375) char [temp\_buff](structshell__ctx.md#a35085b30e92b913b16f02496c5ec6375)[[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)];

880

[ 882](structshell__ctx.md#aba89a1995fe33838d508810e60c7ea79) char [printf\_buff](structshell__ctx.md#aba89a1995fe33838d508810e60c7ea79)[[CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE](shell_2shell_8h.md#af54e892edba822e46ca70cb6eca48146)];

883

[ 884](structshell__ctx.md#a5437653e57909910df742c80562c1c83) volatile union [shell\_backend\_cfg](unionshell__backend__cfg.md) [cfg](structshell__ctx.md#a5437653e57909910df742c80562c1c83);

[ 885](structshell__ctx.md#ac9bed826ec7421065e6bc6e12ad213ce) volatile union [shell\_backend\_ctx](unionshell__backend__ctx.md) [ctx](structshell__ctx.md#ac9bed826ec7421065e6bc6e12ad213ce);

886

[ 887](structshell__ctx.md#a6d96ff92952aebed16ebf288fe0a96db) struct [k\_poll\_signal](structk__poll__signal.md) [signals](structshell__ctx.md#a6d96ff92952aebed16ebf288fe0a96db)[[SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)];

888

[ 892](structshell__ctx.md#abbbc94a651bfc56d5b0916e1516c3842) struct [k\_poll\_event](structk__poll__event.md) [events](structshell__ctx.md#abbbc94a651bfc56d5b0916e1516c3842)[[SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)];

893

[ 894](structshell__ctx.md#a76cf861f17057cf080c54b67acb1a801) struct [k\_mutex](structk__mutex.md) [wr\_mtx](structshell__ctx.md#a76cf861f17057cf080c54b67acb1a801);

[ 895](structshell__ctx.md#a2cab9b799462a9f6eea898f7076f204f) [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [tid](structshell__ctx.md#a2cab9b799462a9f6eea898f7076f204f);

[ 896](structshell__ctx.md#aab37b8261e69af3dfe3e4ae19de06792) int [ret\_val](structshell__ctx.md#aab37b8261e69af3dfe3e4ae19de06792);

897};

898

899extern const struct [log\_backend\_api](structlog__backend__api.md) [log\_backend\_shell\_api](group__shell__api.md#gaddf27615ed72440ecb63aa1d84962c82);

900

[ 904](group__shell__api.md#ga56bf30741f9ec7a6d94e5c18c2858948)enum [shell\_flag](group__shell__api.md#ga56bf30741f9ec7a6d94e5c18c2858948) {

[ 905](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab) [SHELL\_FLAG\_CRLF\_DEFAULT](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab) = (1<<0),

[ 906](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446) [SHELL\_FLAG\_OLF\_CRLF](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446) = (1<<1)

907};

908

[ 912](structshell.md)struct [shell](structshell.md) {

[ 913](structshell.md#a97c365dfd7202eb091b1ad016014729b) const char \*[default\_prompt](structshell.md#a97c365dfd7202eb091b1ad016014729b);

914

[ 915](structshell.md#ac6033c3c2e44c2c4e29791f1f61c566c) const struct [shell\_transport](structshell__transport.md) \*[iface](structshell.md#ac6033c3c2e44c2c4e29791f1f61c566c);

[ 916](structshell.md#ac14fde7e5f28615b9eec39a2eb8aa8d4) struct [shell\_ctx](structshell__ctx.md) \*[ctx](structshell.md#ac14fde7e5f28615b9eec39a2eb8aa8d4);

917

[ 918](structshell.md#a42d2588d15f601baf3f963684d312c86) struct [shell\_history](structshell__history.md) \*[history](structshell.md#a42d2588d15f601baf3f963684d312c86);

919

[ 920](structshell.md#a3a4f58c6151b3cbd1293d36b92c2f470) const enum [shell\_flag](structshell.md#a3a4f58c6151b3cbd1293d36b92c2f470) [shell\_flag](structshell.md#a3a4f58c6151b3cbd1293d36b92c2f470);

921

[ 922](structshell.md#aba181907e38def0985a4c6ffd459d935) const struct [shell\_fprintf](group__shell__api.md#ga1fd1671311b112f0c87ab2dafd801105) \*[fprintf\_ctx](structshell.md#aba181907e38def0985a4c6ffd459d935);

923

[ 924](structshell.md#a642e7d8fa92464147329247e1325ad2b) struct [shell\_stats](structshell__stats.md) \*[stats](structshell.md#a642e7d8fa92464147329247e1325ad2b);

925

[ 926](structshell.md#a3daffdb9d38ee8132a2644054126680d) const struct [shell\_log\_backend](structshell__log__backend.md) \*[log\_backend](structshell.md#a3daffdb9d38ee8132a2644054126680d);

927

[ 928](structshell.md#a30ad7480b8be019b3b3ed63bf05ad790) [LOG\_INSTANCE\_PTR\_DECLARE](structshell.md#a30ad7480b8be019b3b3ed63bf05ad790)(log);

929

[ 930](structshell.md#a66eb938dae4f2b0fd873980c1efeb00b) const char \*[name](structshell.md#a66eb938dae4f2b0fd873980c1efeb00b);

[ 931](structshell.md#a01b4739356f2428527f322662a3bf0a7) struct [k\_thread](structk__thread.md) \*[thread](structshell.md#a01b4739356f2428527f322662a3bf0a7);

[ 932](structshell.md#ad62262b6b4fa8e56a0e8849f09603b3a) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack](structshell.md#ad62262b6b4fa8e56a0e8849f09603b3a);

933};

934

935extern void z\_shell\_print\_stream(const void \*user\_ctx, const char \*data,

936 size\_t data\_len);

937

950#define Z\_SHELL\_DEFINE(\_name, \_prompt, \_transport\_iface, \_out\_buf, \_log\_backend, \_shell\_flag) \

951 static const struct shell \_name; \

952 static struct shell\_ctx UTIL\_CAT(\_name, \_ctx); \

953 Z\_SHELL\_HISTORY\_DEFINE(\_name##\_history, CONFIG\_SHELL\_HISTORY\_BUFFER); \

954 Z\_SHELL\_FPRINTF\_DEFINE(\_name##\_fprintf, &\_name, \_out\_buf, CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE, \

955 IS\_ENABLED(CONFIG\_SHELL\_PRINTF\_AUTOFLUSH), z\_shell\_print\_stream); \

956 LOG\_INSTANCE\_REGISTER(shell, \_name, CONFIG\_SHELL\_LOG\_LEVEL); \

957 Z\_SHELL\_STATS\_DEFINE(\_name); \

958 static K\_KERNEL\_STACK\_DEFINE(\_name##\_stack, CONFIG\_SHELL\_STACK\_SIZE); \

959 static struct k\_thread \_name##\_thread; \

960 static const STRUCT\_SECTION\_ITERABLE(shell, \_name) = { \

961 .default\_prompt = \_prompt, \

962 .iface = \_transport\_iface, \

963 .ctx = &UTIL\_CAT(\_name, \_ctx), \

964 .history = IS\_ENABLED(CONFIG\_SHELL\_HISTORY) ? &\_name##\_history : NULL, \

965 .shell\_flag = \_shell\_flag, \

966 .fprintf\_ctx = &\_name##\_fprintf, \

967 .stats = Z\_SHELL\_STATS\_PTR(\_name), \

968 .log\_backend = \_log\_backend, \

969 LOG\_INSTANCE\_PTR\_INIT(log, shell, \_name).name = \

970 STRINGIFY(\_name), .thread = &\_name##\_thread, .stack = \_name##\_stack}

971

[ 985](group__shell__api.md#ga158405143b49e4888cb135fec83ad22c)#define SHELL\_DEFINE(\_name, \_prompt, \_transport\_iface, \_log\_queue\_size, \_log\_timeout, \_shell\_flag) \

986 static uint8\_t \_name##\_out\_buffer[CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE]; \

987 Z\_SHELL\_LOG\_BACKEND\_DEFINE(\_name, \_name##\_out\_buffer, CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE, \

988 \_log\_queue\_size, \_log\_timeout); \

989 Z\_SHELL\_DEFINE(\_name, \_prompt, \_transport\_iface, \_name##\_out\_buffer, \

990 Z\_SHELL\_LOG\_BACKEND\_PTR(\_name), \_shell\_flag)

991

[ 1005](group__shell__api.md#ga8764ff11603855a10419c48e46e8221c)int [shell\_init](group__shell__api.md#ga8764ff11603855a10419c48e46e8221c)(const struct [shell](structshell.md) \*sh, const void \*transport\_config,

1006 struct [shell\_backend\_config\_flags](structshell__backend__config__flags.md) cfg\_flags,

1007 bool [log\_backend](structlog__backend.md), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) init\_log\_level);

1008

[ 1015](group__shell__api.md#ga07e76646c5065218464aa8ce78b75af3)void [shell\_uninit](group__shell__api.md#ga07e76646c5065218464aa8ce78b75af3)(const struct [shell](structshell.md) \*sh, [shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25) cb);

1016

[ 1024](group__shell__api.md#gad386d4e8077103e7976f25996fcc3132)int [shell\_start](group__shell__api.md#gad386d4e8077103e7976f25996fcc3132)(const struct [shell](structshell.md) \*sh);

1025

[ 1033](group__shell__api.md#gad27754d0beb31bc501f28f9ef26a362c)int [shell\_stop](group__shell__api.md#gad27754d0beb31bc501f28f9ef26a362c)(const struct [shell](structshell.md) \*sh);

1034

[ 1038](group__shell__api.md#ga4c3a7db0c2bdbf36bbf72302a04bb44d)#define SHELL\_NORMAL SHELL\_VT100\_COLOR\_DEFAULT

1039

[ 1043](group__shell__api.md#gaac0ea96fbb5885432dca93174c9ad4e6)#define SHELL\_INFO SHELL\_VT100\_COLOR\_GREEN

1044

[ 1048](group__shell__api.md#gacc7c6e7b1fc65cc350353cc166da528b)#define SHELL\_OPTION SHELL\_VT100\_COLOR\_CYAN

1049

[ 1053](group__shell__api.md#ga118dd6829e092423a85e2b6de07f8dd3)#define SHELL\_WARNING SHELL\_VT100\_COLOR\_YELLOW

1054

[ 1058](group__shell__api.md#ga7664f5e184e9b41ac92e033f7b8d885d)#define SHELL\_ERROR SHELL\_VT100\_COLOR\_RED

1059

[ 1071](group__shell__api.md#ga863c04af5db00a3804eaff02d401603b)void \_\_printf\_like(3, 4) [shell\_fprintf\_impl](group__shell__api.md#ga863c04af5db00a3804eaff02d401603b)(const struct [shell](structshell.md) \*sh, enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) color,

1072 const char \*fmt, ...);

1073

[ 1074](group__shell__api.md#ga1fd1671311b112f0c87ab2dafd801105)#define shell\_fprintf(sh, color, fmt, ...) shell\_fprintf\_impl(sh, color, fmt, ##\_\_VA\_ARGS\_\_)

1075

[ 1088](group__shell__api.md#ga74a1c4edd803cad14c893fc9816e534f)void [shell\_vfprintf](group__shell__api.md#ga74a1c4edd803cad14c893fc9816e534f)(const struct [shell](structshell.md) \*sh, enum [shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2) color,

1089 const char \*fmt, va\_list args);

1090

[ 1106](group__shell__api.md#ga0b6e69b499c153ae8f7ba256d445f09d)void [shell\_hexdump\_line](group__shell__api.md#ga0b6e69b499c153ae8f7ba256d445f09d)(const struct [shell](structshell.md) \*sh, unsigned int offset,

1107 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

1108

[ 1116](group__shell__api.md#gaeeba0b483974205c54e364d509badd42)void [shell\_hexdump](group__shell__api.md#gaeeba0b483974205c54e364d509badd42)(const struct [shell](structshell.md) \*sh, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

1117

[ 1127](group__shell__api.md#ga9382959c41fe6850c2daa51306b3c5fd)#define shell\_info(\_sh, \_ft, ...) \

1128 shell\_fprintf\_info(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[ 1129](group__shell__api.md#ga30fcc10f13ce8d850f2c1c5de4533a29)void \_\_printf\_like(2, 3) [shell\_fprintf\_info](group__shell__api.md#ga30fcc10f13ce8d850f2c1c5de4533a29)(const struct [shell](structshell.md) \*sh, const char \*fmt, ...);

1130

[ 1140](group__shell__api.md#ga3126019b2100d1ccb2d4dc5efb7d8228)#define shell\_print(\_sh, \_ft, ...) \

1141 shell\_fprintf\_normal(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[ 1142](group__shell__api.md#ga67f638ebc05f8300553e5e6c1771380d)void \_\_printf\_like(2, 3) [shell\_fprintf\_normal](group__shell__api.md#ga67f638ebc05f8300553e5e6c1771380d)(const struct [shell](structshell.md) \*sh, const char \*fmt, ...);

1143

[ 1153](group__shell__api.md#ga3d886cfd7b4340b2e71a92bd7c4534d9)#define shell\_warn(\_sh, \_ft, ...) \

1154 shell\_fprintf\_warn(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[ 1155](group__shell__api.md#ga9c9ced10bf376a5514b8b0bb55e1efcd)void \_\_printf\_like(2, 3) [shell\_fprintf\_warn](group__shell__api.md#ga9c9ced10bf376a5514b8b0bb55e1efcd)(const struct [shell](structshell.md) \*sh, const char \*fmt, ...);

1156

[ 1166](group__shell__api.md#ga408141c02209a9549cb9063f24ef3731)#define shell\_error(\_sh, \_ft, ...) \

1167 shell\_fprintf\_error(\_sh, \_ft "\n", ##\_\_VA\_ARGS\_\_)

[ 1168](group__shell__api.md#ga427d7f51d99aec311348f836d9007df7)void \_\_printf\_like(2, 3) [shell\_fprintf\_error](group__shell__api.md#ga427d7f51d99aec311348f836d9007df7)(const struct [shell](structshell.md) \*sh, const char \*fmt, ...);

1169

[ 1176](group__shell__api.md#ga7e66389d0faf15a2a7c31c68cdd9c36c)void [shell\_process](group__shell__api.md#ga7e66389d0faf15a2a7c31c68cdd9c36c)(const struct [shell](structshell.md) \*sh);

1177

[ 1187](group__shell__api.md#ga2113b7227b155755a7ab8a928f7ae499)int [shell\_prompt\_change](group__shell__api.md#ga2113b7227b155755a7ab8a928f7ae499)(const struct [shell](structshell.md) \*sh, const char \*prompt);

1188

[ 1197](group__shell__api.md#gac3c643a0b332cd2f07fe506337784ac0)void [shell\_help](group__shell__api.md#gac3c643a0b332cd2f07fe506337784ac0)(const struct [shell](structshell.md) \*sh);

1198

[ 1200](group__shell__api.md#ga3be3ecccd6ce1954883c5959c39c7927)#define SHELL\_CMD\_HELP\_PRINTED (1)

1201

[ 1219](group__shell__api.md#gabfb6a1f1f53f90365de349348015311e)int [shell\_execute\_cmd](group__shell__api.md#gabfb6a1f1f53f90365de349348015311e)(const struct [shell](structshell.md) \*sh, const char \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

1220

[ 1232](group__shell__api.md#ga768c606f2d50f24e9b607ba0a341686d)int [shell\_set\_root\_cmd](group__shell__api.md#ga768c606f2d50f24e9b607ba0a341686d)(const char \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

1233

[ 1242](group__shell__api.md#ga7514a072c2819fb93fb9d62542c7cc15)void [shell\_set\_bypass](group__shell__api.md#ga7514a072c2819fb93fb9d62542c7cc15)(const struct [shell](structshell.md) \*sh, [shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d) bypass);

1243

[ 1251](group__shell__api.md#ga79369ddfea2dc2cb5813c5eb5c67634a)bool [shell\_ready](group__shell__api.md#ga79369ddfea2dc2cb5813c5eb5c67634a)(const struct [shell](structshell.md) \*sh);

1252

[ 1263](group__shell__api.md#gaf1f41d8b6cd430357d593ab0fc5adfeb)int [shell\_insert\_mode\_set](group__shell__api.md#gaf1f41d8b6cd430357d593ab0fc5adfeb)(const struct [shell](structshell.md) \*sh, bool val);

1264

[ 1276](group__shell__api.md#ga7d5873456ba43ebd3cc86d25e3f4a72c)int [shell\_use\_colors\_set](group__shell__api.md#ga7d5873456ba43ebd3cc86d25e3f4a72c)(const struct [shell](structshell.md) \*sh, bool val);

1277

[ 1288](group__shell__api.md#ga80ff4b3b4cc62e543fd510c14f55b42a)int [shell\_use\_vt100\_set](group__shell__api.md#ga80ff4b3b4cc62e543fd510c14f55b42a)(const struct [shell](structshell.md) \*sh, bool val);

1289

[ 1300](group__shell__api.md#gad53881371bbaedfd3ef3ecf219706fd1)int [shell\_echo\_set](group__shell__api.md#gad53881371bbaedfd3ef3ecf219706fd1)(const struct [shell](structshell.md) \*sh, bool val);

1301

[ 1313](group__shell__api.md#ga86fade2757d04c9220d5912a4ee540a0)int [shell\_obscure\_set](group__shell__api.md#ga86fade2757d04c9220d5912a4ee540a0)(const struct [shell](structshell.md) \*sh, bool obscure);

1314

[ 1326](group__shell__api.md#ga2df2997c4b04f3246c22f43b274a353b)int [shell\_mode\_delete\_set](group__shell__api.md#ga2df2997c4b04f3246c22f43b274a353b)(const struct [shell](structshell.md) \*sh, bool val);

1327

[ 1335](group__shell__api.md#ga54dc053c92641bc9b9736bc2d61140f7)int [shell\_get\_return\_value](group__shell__api.md#ga54dc053c92641bc9b9736bc2d61140f7)(const struct [shell](structshell.md) \*sh);

1336

1340

1341#ifdef \_\_cplusplus

1342}

1343#endif

1344

1345#ifdef CONFIG\_SHELL\_CUSTOM\_HEADER

1346/\* This include must always be at the end of shell.h \*/

1347#include <zephyr\_custom\_shell.h>

1348#endif

1349

1350#endif /\* SHELL\_H\_\_ \*/

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[shell\_uninit](group__shell__api.md#ga07e76646c5065218464aa8ce78b75af3)

void shell\_uninit(const struct shell \*sh, shell\_uninit\_cb\_t cb)

Uninitializes the transport layer and the internal shell state.

[shell\_uninit\_cb\_t](group__shell__api.md#ga0844a0ce151551d3ccf45d507e5bab25)

void(\* shell\_uninit\_cb\_t)(const struct shell \*sh, int res)

**Definition** shell.h:650

[shell\_hexdump\_line](group__shell__api.md#ga0b6e69b499c153ae8f7ba256d445f09d)

void shell\_hexdump\_line(const struct shell \*sh, unsigned int offset, const uint8\_t \*data, size\_t len)

Print a line of data in hexadecimal format.

[shell\_dict\_cmd\_handler](group__shell__api.md#ga182f247052041f1236d13726589885e2)

int(\* shell\_dict\_cmd\_handler)(const struct shell \*sh, size\_t argc, char \*\*argv, void \*data)

Shell dictionary command handler prototype.

**Definition** shell.h:212

[shell\_fprintf](group__shell__api.md#ga1fd1671311b112f0c87ab2dafd801105)

#define shell\_fprintf(sh, color, fmt,...)

**Definition** shell.h:1074

[shell\_prompt\_change](group__shell__api.md#ga2113b7227b155755a7ab8a928f7ae499)

int shell\_prompt\_change(const struct shell \*sh, const char \*prompt)

Change displayed shell prompt.

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:646

[shell\_mode\_delete\_set](group__shell__api.md#ga2df2997c4b04f3246c22f43b274a353b)

int shell\_mode\_delete\_set(const struct shell \*sh, bool val)

Allow application to control whether the delete key backspaces or deletes.

[shell\_fprintf\_info](group__shell__api.md#ga30fcc10f13ce8d850f2c1c5de4533a29)

void shell\_fprintf\_info(const struct shell \*sh, const char \*fmt,...)

[shell\_cmd\_handler](group__shell__api.md#ga331e7d19b9b0755486596f5ffc598338)

int(\* shell\_cmd\_handler)(const struct shell \*sh, size\_t argc, char \*\*argv)

Shell command handler prototype.

**Definition** shell.h:196

[shell\_fprintf\_error](group__shell__api.md#ga427d7f51d99aec311348f836d9007df7)

void shell\_fprintf\_error(const struct shell \*sh, const char \*fmt,...)

[shell\_get\_return\_value](group__shell__api.md#ga54dc053c92641bc9b9736bc2d61140f7)

int shell\_get\_return\_value(const struct shell \*sh)

Retrieve return value of most recently executed shell command.

[shell\_flag](group__shell__api.md#ga56bf30741f9ec7a6d94e5c18c2858948)

shell\_flag

Flags for setting shell output newline sequence.

**Definition** shell.h:904

[shell\_device\_lookup](group__shell__api.md#ga571db3aa3e024a09e82b117a74d6f248)

const struct device \* shell\_device\_lookup(size\_t idx, const char \*prefix)

Get by index a device that matches .

[shell\_signal](group__shell__api.md#ga5cd015de5e7295483fa2cff7d54c2d21)

shell\_signal

**Definition** shell.h:824

[shell\_fprintf\_normal](group__shell__api.md#ga67f638ebc05f8300553e5e6c1771380d)

void shell\_fprintf\_normal(const struct shell \*sh, const char \*fmt,...)

[shell\_vfprintf](group__shell__api.md#ga74a1c4edd803cad14c893fc9816e534f)

void shell\_vfprintf(const struct shell \*sh, enum shell\_vt100\_color color, const char \*fmt, va\_list args)

vprintf-like function which sends formatted data stream to the shell.

[shell\_set\_bypass](group__shell__api.md#ga7514a072c2819fb93fb9d62542c7cc15)

void shell\_set\_bypass(const struct shell \*sh, shell\_bypass\_cb\_t bypass)

Set bypass callback.

[shell\_set\_root\_cmd](group__shell__api.md#ga768c606f2d50f24e9b607ba0a341686d)

int shell\_set\_root\_cmd(const char \*cmd)

Set root command for all shell instances.

[shell\_ready](group__shell__api.md#ga79369ddfea2dc2cb5813c5eb5c67634a)

bool shell\_ready(const struct shell \*sh)

Get shell readiness to execute commands.

[shell\_use\_colors\_set](group__shell__api.md#ga7d5873456ba43ebd3cc86d25e3f4a72c)

int shell\_use\_colors\_set(const struct shell \*sh, bool val)

Allow application to control whether terminal output uses colored syntax.

[shell\_process](group__shell__api.md#ga7e66389d0faf15a2a7c31c68cdd9c36c)

void shell\_process(const struct shell \*sh)

Process function, which should be executed when data is ready in the transport interface.

[shell\_device\_get\_binding](group__shell__api.md#ga7fb40045dc0a27c175e37a6c9cd84b53)

const struct device \* shell\_device\_get\_binding(const char \*name)

Get a device reference from its device::name field or label.

[shell\_use\_vt100\_set](group__shell__api.md#ga80ff4b3b4cc62e543fd510c14f55b42a)

int shell\_use\_vt100\_set(const struct shell \*sh, bool val)

Allow application to control whether terminal is using vt100 commands.

[shell\_fprintf\_impl](group__shell__api.md#ga863c04af5db00a3804eaff02d401603b)

void shell\_fprintf\_impl(const struct shell \*sh, enum shell\_vt100\_color color, const char \*fmt,...)

printf-like function which sends formatted data stream to the shell.

[shell\_obscure\_set](group__shell__api.md#ga86fade2757d04c9220d5912a4ee540a0)

int shell\_obscure\_set(const struct shell \*sh, bool obscure)

Allow application to control whether user input is obscured with asterisks – useful for implementing ...

[shell\_init](group__shell__api.md#ga8764ff11603855a10419c48e46e8221c)

int shell\_init(const struct shell \*sh, const void \*transport\_config, struct shell\_backend\_config\_flags cfg\_flags, bool log\_backend, uint32\_t init\_log\_level)

Function for initializing a transport layer and internal shell state.

[shell\_receive\_state](group__shell__api.md#ga8773ed2570714ba4985108b1738d33a0)

shell\_receive\_state

**Definition** shell.h:622

[shell\_fprintf\_warn](group__shell__api.md#ga9c9ced10bf376a5514b8b0bb55e1efcd)

void shell\_fprintf\_warn(const struct shell \*sh, const char \*fmt,...)

[shell\_device\_filter\_t](group__shell__api.md#gaa2b8cf8ac78b8355408ef94958ebdc70)

bool(\* shell\_device\_filter\_t)(const struct device \*dev)

Filter callback type, for use with shell\_device\_lookup\_filter.

**Definition** shell.h:144

[shell\_bypass\_cb\_t](group__shell__api.md#gab1dafbf90c42b7d4601122e1b9eabf3d)

void(\* shell\_bypass\_cb\_t)(const struct shell \*sh, uint8\_t \*data, size\_t len)

Bypass callback.

**Definition** shell.h:658

[shell\_execute\_cmd](group__shell__api.md#gabfb6a1f1f53f90365de349348015311e)

int shell\_execute\_cmd(const struct shell \*sh, const char \*cmd)

Execute command.

[shell\_help](group__shell__api.md#gac3c643a0b332cd2f07fe506337784ac0)

void shell\_help(const struct shell \*sh)

Prints the current command help.

[shell\_stop](group__shell__api.md#gad27754d0beb31bc501f28f9ef26a362c)

int shell\_stop(const struct shell \*sh)

Function for stopping shell processing.

[shell\_start](group__shell__api.md#gad386d4e8077103e7976f25996fcc3132)

int shell\_start(const struct shell \*sh)

Function for starting shell processing.

[shell\_echo\_set](group__shell__api.md#gad53881371bbaedfd3ef3ecf219706fd1)

int shell\_echo\_set(const struct shell \*sh, bool val)

Allow application to control whether user input is echoed back.

[log\_backend\_shell\_api](group__shell__api.md#gaddf27615ed72440ecb63aa1d84962c82)

const struct log\_backend\_api log\_backend\_shell\_api

[shell\_device\_filter](group__shell__api.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d)

const struct device \* shell\_device\_filter(size\_t idx, shell\_device\_filter\_t filter)

Get a device by index and filter.

[shell\_transport\_evt](group__shell__api.md#gae77673d4c086f2f9312ceb7933745ee1)

shell\_transport\_evt

Shell transport event.

**Definition** shell.h:641

[shell\_hexdump](group__shell__api.md#gaeeba0b483974205c54e364d509badd42)

void shell\_hexdump(const struct shell \*sh, const uint8\_t \*data, size\_t len)

Print data in hexadecimal format.

[shell\_insert\_mode\_set](group__shell__api.md#gaf1f41d8b6cd430357d593ab0fc5adfeb)

int shell\_insert\_mode\_set(const struct shell \*sh, bool val)

Allow application to control text insert mode.

[shell\_state](group__shell__api.md#gaf2c6ff9ef31dc06086fd1141763e6266)

shell\_state

**Definition** shell.h:632

[shell\_dynamic\_get](group__shell__api.md#gafc042f32bac2fdd4cbde9f943e29b008)

void(\* shell\_dynamic\_get)(size\_t idx, struct shell\_static\_entry \*entry)

Shell dynamic command descriptor.

**Definition** shell.h:95

[SHELL\_FLAG\_CRLF\_DEFAULT](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab)

@ SHELL\_FLAG\_CRLF\_DEFAULT

Do not map CR or LF.

**Definition** shell.h:905

[SHELL\_FLAG\_OLF\_CRLF](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)

@ SHELL\_FLAG\_OLF\_CRLF

Map LF to CRLF on output.

**Definition** shell.h:906

[SHELL\_SIGNALS](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a6dc083b04447ff6ccb4ce4af4c43645e)

@ SHELL\_SIGNALS

**Definition** shell.h:829

[SHELL\_SIGNAL\_TXDONE](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a7962ab077b49c816bb9337a9b1b343ed)

@ SHELL\_SIGNAL\_TXDONE

**Definition** shell.h:828

[SHELL\_SIGNAL\_RXRDY](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21a815c6760bfd5bba8813ea68964bf4713)

@ SHELL\_SIGNAL\_RXRDY

**Definition** shell.h:825

[SHELL\_SIGNAL\_LOG\_MSG](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ab8fe52f7b4f43c98dae5188a1dc8547a)

@ SHELL\_SIGNAL\_LOG\_MSG

**Definition** shell.h:826

[SHELL\_SIGNAL\_KILL](group__shell__api.md#gga5cd015de5e7295483fa2cff7d54c2d21ad5c07b5872f785b0731c8aaed0f81c3a)

@ SHELL\_SIGNAL\_KILL

**Definition** shell.h:827

[SHELL\_RECEIVE\_DEFAULT](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a201e367896f86499d317d9ec7b59612a)

@ SHELL\_RECEIVE\_DEFAULT

**Definition** shell.h:623

[SHELL\_RECEIVE\_ESC\_SEQ](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0a7378b6ecb1a51c53577db5a8eeda936a)

@ SHELL\_RECEIVE\_ESC\_SEQ

**Definition** shell.h:625

[SHELL\_RECEIVE\_ESC](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0ab512e3269698524fd025433016b3ad65)

@ SHELL\_RECEIVE\_ESC

**Definition** shell.h:624

[SHELL\_RECEIVE\_TILDE\_EXP](group__shell__api.md#gga8773ed2570714ba4985108b1738d33a0afa2dde3374d3971266652cf48a4d13f7)

@ SHELL\_RECEIVE\_TILDE\_EXP

**Definition** shell.h:626

[SHELL\_TRANSPORT\_EVT\_TX\_RDY](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1a6c78a3534128fac6366d9e5dfda81dfb)

@ SHELL\_TRANSPORT\_EVT\_TX\_RDY

**Definition** shell.h:643

[SHELL\_TRANSPORT\_EVT\_RX\_RDY](group__shell__api.md#ggae77673d4c086f2f9312ceb7933745ee1aa43ab5965bc3f2c964f206277ab3f1bb)

@ SHELL\_TRANSPORT\_EVT\_RX\_RDY

**Definition** shell.h:642

[SHELL\_STATE\_UNINITIALIZED](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a0fcbee7b51ec8d90e7d42a1b455360e6)

@ SHELL\_STATE\_UNINITIALIZED

**Definition** shell.h:633

[SHELL\_STATE\_PANIC\_MODE\_INACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a6423704f7a619e1bfed063cd7455ebfe)

@ SHELL\_STATE\_PANIC\_MODE\_INACTIVE

Panic requested, not supported.

**Definition** shell.h:637

[SHELL\_STATE\_ACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8a226ad5c1306dd8f491ad321d334b72)

@ SHELL\_STATE\_ACTIVE

**Definition** shell.h:635

[SHELL\_STATE\_PANIC\_MODE\_ACTIVE](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266a8d01930f8cbdeddda2bf47d0264c4a8b)

@ SHELL\_STATE\_PANIC\_MODE\_ACTIVE

Panic activated.

**Definition** shell.h:636

[SHELL\_STATE\_INITIALIZED](group__shell__api.md#ggaf2c6ff9ef31dc06086fd1141763e6266adf8c97c3b6dacfbaf3ace4780cfe3dbd)

@ SHELL\_STATE\_INITIALIZED

**Definition** shell.h:634

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:380

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log.h](log_8h.md)

[log\_instance.h](log__instance_8h.md)

[CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE](shell_2shell_8h.md#a81357b82642c8910ae3fb920cb885370)

#define CONFIG\_SHELL\_PROMPT\_BUFF\_SIZE

**Definition** shell.h:30

[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)

#define CONFIG\_SHELL\_CMD\_BUFF\_SIZE

**Definition** shell.h:34

[CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE](shell_2shell_8h.md#af54e892edba822e46ca70cb6eca48146)

#define CONFIG\_SHELL\_PRINTF\_BUFF\_SIZE

**Definition** shell.h:38

[shell\_fprintf.h](shell__fprintf_8h.md)

[shell\_history.h](shell__history_8h.md)

[shell\_log\_backend.h](shell__log__backend_8h.md)

[shell\_string\_conv.h](shell__string__conv_8h.md)

[shell\_types.h](shell__types_8h.md)

[shell\_vt100\_color](shell__types_8h.md#a6dcf569be711db32286fb1ef2dcf36d2)

shell\_vt100\_color

**Definition** shell\_types.h:14

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)

const char \* name

Name of the device instance.

**Definition** device.h:455

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_poll\_event](structk__poll__event.md)

Poll Event.

**Definition** kernel.h:5988

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5964

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[log\_backend\_api](structlog__backend__api.md)

Logger backend API.

**Definition** log\_backend.h:63

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:95

[shell\_backend\_config\_flags](structshell__backend__config__flags.md)

**Definition** shell.h:769

[shell\_backend\_config\_flags::use\_vt100](structshell__backend__config__flags.md#a0d017df8e9d9609f2830829d8720b9cf)

uint32\_t use\_vt100

Controls VT100 commands usage in shell.

**Definition** shell.h:775

[shell\_backend\_config\_flags::mode\_delete](structshell__backend__config__flags.md#a231bc4762cac1c07a6f866c5ecf3a024)

uint32\_t mode\_delete

Operation mode of backspace key.

**Definition** shell.h:773

[shell\_backend\_config\_flags::echo](structshell__backend__config__flags.md#a5745ea5cab202ee446f460b980c5c532)

uint32\_t echo

Controls shell echo.

**Definition** shell.h:771

[shell\_backend\_config\_flags::insert\_mode](structshell__backend__config__flags.md#ab1df6f41078d4ec2a94f158e62bbfada)

uint32\_t insert\_mode

Controls insert mode for text introduction.

**Definition** shell.h:770

[shell\_backend\_config\_flags::obscure](structshell__backend__config__flags.md#af794ac9c19b948ed733024a2db5b8bbd)

uint32\_t obscure

If echo on, print asterisk instead.

**Definition** shell.h:772

[shell\_backend\_config\_flags::use\_colors](structshell__backend__config__flags.md#af810ff3fba00527cb0561a75b70fec09)

uint32\_t use\_colors

Controls colored syntax.

**Definition** shell.h:774

[shell\_backend\_ctx\_flags](structshell__backend__ctx__flags.md)

**Definition** shell.h:794

[shell\_backend\_ctx\_flags::print\_noinit](structshell__backend__ctx__flags.md#a18b3c018f2da6a925f50266bda095483)

uint32\_t print\_noinit

Print request from not initialized shell.

**Definition** shell.h:800

[shell\_backend\_ctx\_flags::sync\_mode](structshell__backend__ctx__flags.md#a2d6c2561aa6ed28a3978e3b70d079008)

uint32\_t sync\_mode

Shell in synchronous mode.

**Definition** shell.h:801

[shell\_backend\_ctx\_flags::tx\_rdy](structshell__backend__ctx__flags.md#a662cf22a29856d07ec64b72db004582f)

uint32\_t tx\_rdy

**Definition** shell.h:796

[shell\_backend\_ctx\_flags::handle\_log](structshell__backend__ctx__flags.md#a735602bed33c01e8e548200656fd7ff4)

uint32\_t handle\_log

Shell is handling logger backend.

**Definition** shell.h:802

[shell\_backend\_ctx\_flags::processing](structshell__backend__ctx__flags.md#a7dc2cd17fb1dd9d538dbde3ad7bbe8e9)

uint32\_t processing

Shell is executing process function.

**Definition** shell.h:795

[shell\_backend\_ctx\_flags::last\_nl](structshell__backend__ctx__flags.md#a7f597db455b0875c9ff11c4ce50cfd92)

uint32\_t last\_nl

Last received new line character.

**Definition** shell.h:798

[shell\_backend\_ctx\_flags::history\_exit](structshell__backend__ctx__flags.md#a85b0069c7b0df219cefec0f73cb313d3)

uint32\_t history\_exit

Request to exit history mode.

**Definition** shell.h:797

[shell\_backend\_ctx\_flags::cmd\_ctx](structshell__backend__ctx__flags.md#adfa22b07dc65e72e24be400d95da11c8)

uint32\_t cmd\_ctx

Shell is executing command.

**Definition** shell.h:799

[shell\_ctx](structshell__ctx.md)

Shell instance context.

**Definition** shell.h:835

[shell\_ctx::selected\_cmd](structshell__ctx.md#a0e9321e8954a7598cb6521f660480a88)

const struct shell\_static\_entry \* selected\_cmd

New root command.

**Definition** shell.h:849

[shell\_ctx::uninit\_cb](structshell__ctx.md#a0ec61f11544cb817bbd46ed4aa332123)

shell\_uninit\_cb\_t uninit\_cb

Callback called from shell thread context when unitialization is completed just before aborting shell...

**Definition** shell.h:857

[shell\_ctx::vt100\_ctx](structshell__ctx.md#a25b945fcaba216e039124aacec660600)

struct shell\_vt100\_ctx vt100\_ctx

VT100 color and cursor position, terminal width.

**Definition** shell.h:852

[shell\_ctx::prompt](structshell__ctx.md#a261d4754f4bf3764298e264ed6e87eff)

const char \* prompt

**Definition** shell.h:839

[shell\_ctx::tid](structshell__ctx.md#a2cab9b799462a9f6eea898f7076f204f)

k\_tid\_t tid

**Definition** shell.h:895

[shell\_ctx::temp\_buff](structshell__ctx.md#a35085b30e92b913b16f02496c5ec6375)

char temp\_buff[0]

Command temporary buffer.

**Definition** shell.h:879

[shell\_ctx::cmd\_buff](structshell__ctx.md#a385014f2fba5cae182c3520ec934cce6)

char cmd\_buff[0]

Command input buffer.

**Definition** shell.h:876

[shell\_ctx::active\_cmd](structshell__ctx.md#a3df8f9a293b4c24d81a80af2d0e0c44e)

struct shell\_static\_entry active\_cmd

Currently executed command.

**Definition** shell.h:846

[shell\_ctx::log\_level](structshell__ctx.md#a3e6374150abdb9cd4875024eb6f7c5ea)

uint32\_t log\_level

**Definition** shell.h:863

[shell\_ctx::cfg](structshell__ctx.md#a5437653e57909910df742c80562c1c83)

volatile union shell\_backend\_cfg cfg

**Definition** shell.h:884

[shell\_ctx::cmd\_tmp\_buff\_len](structshell__ctx.md#a5dfe5d3b2e27b67a7a78d5c3ad32ff1d)

uint16\_t cmd\_tmp\_buff\_len

Command length in tmp buffer.

**Definition** shell.h:873

[shell\_ctx::signals](structshell__ctx.md#a6d96ff92952aebed16ebf288fe0a96db)

struct k\_poll\_signal signals[SHELL\_SIGNALS]

**Definition** shell.h:887

[shell\_ctx::state](structshell__ctx.md#a7388fd2e850fcf37c4a421cda13661e8)

enum shell\_state state

Internal module state.

**Definition** shell.h:842

[shell\_ctx::wr\_mtx](structshell__ctx.md#a76cf861f17057cf080c54b67acb1a801)

struct k\_mutex wr\_mtx

**Definition** shell.h:894

[shell\_ctx::bypass](structshell__ctx.md#a8e02d1d9a521379ad4188b4678cc6071)

shell\_bypass\_cb\_t bypass

When bypass is set, all incoming data is passed to the callback.

**Definition** shell.h:860

[shell\_ctx::cmd\_buff\_len](structshell__ctx.md#a948d78719efe7f01b8edf151e1435af6)

uint16\_t cmd\_buff\_len

Command length.

**Definition** shell.h:870

[shell\_ctx::cmd\_buff\_pos](structshell__ctx.md#a9a8f69e6876e4788ef3961dfb769e53f)

uint16\_t cmd\_buff\_pos

Command buffer cursor position.

**Definition** shell.h:871

[shell\_ctx::ret\_val](structshell__ctx.md#aab37b8261e69af3dfe3e4ae19de06792)

int ret\_val

**Definition** shell.h:896

[shell\_ctx::printf\_buff](structshell__ctx.md#aba89a1995fe33838d508810e60c7ea79)

char printf\_buff[0]

Printf buffer size.

**Definition** shell.h:882

[shell\_ctx::events](structshell__ctx.md#abbbc94a651bfc56d5b0916e1516c3842)

struct k\_poll\_event events[SHELL\_SIGNALS]

Events that should be used only internally by shell thread.

**Definition** shell.h:892

[shell\_ctx::receive\_state](structshell__ctx.md#abc4135f23c4738fcf6a2c9d8f45d516b)

enum shell\_receive\_state receive\_state

Escape sequence indicator.

**Definition** shell.h:843

[shell\_ctx::ctx](structshell__ctx.md#ac9bed826ec7421065e6bc6e12ad213ce)

volatile union shell\_backend\_ctx ctx

**Definition** shell.h:885

[shell\_history](structshell__history.md)

**Definition** shell\_history.h:21

[shell\_log\_backend](structshell__log__backend.md)

Shell log backend instance structure (RO data).

**Definition** shell\_log\_backend.h:36

[shell\_static\_args](structshell__static__args.md)

**Definition** shell.h:111

[shell\_static\_args::mandatory](structshell__static__args.md#a2c23bfa755d3bb651e299ff461065d98)

uint8\_t mandatory

Number of mandatory arguments.

**Definition** shell.h:112

[shell\_static\_args::optional](structshell__static__args.md#aa3aa836ed537dde38e64d2c677ace5ae)

uint8\_t optional

Number of optional arguments.

**Definition** shell.h:113

[shell\_static\_entry](structshell__static__entry.md)

**Definition** shell.h:228

[shell\_static\_entry::subcmd](structshell__static__entry.md#a14534428d81f5ffeb303a5320766cd0a)

const union shell\_cmd\_entry \* subcmd

Pointer to subcommand.

**Definition** shell.h:231

[shell\_static\_entry::padding](structshell__static__entry.md#a1ca7de0e195f0f840cd04e4c69b20f80)

uint8\_t padding[0]

**Definition** shell.h:234

[shell\_static\_entry::handler](structshell__static__entry.md#a3147eb0cc1fea698dd433127acb1f220)

shell\_cmd\_handler handler

Command handler.

**Definition** shell.h:232

[shell\_static\_entry::args](structshell__static__entry.md#a73951d31712342c0c0545a142059d367)

struct shell\_static\_args args

Command arguments.

**Definition** shell.h:233

[shell\_static\_entry::help](structshell__static__entry.md#ac8fb0fc23957a49d9a3664b5baa08704)

const char \* help

Command help string.

**Definition** shell.h:230

[shell\_static\_entry::syntax](structshell__static__entry.md#ad87defa749ee7481f6d29d8c9084fb91)

const char \* syntax

Command syntax strings.

**Definition** shell.h:229

[shell\_stats](structshell__stats.md)

Shell statistics structure.

**Definition** shell.h:754

[shell\_stats::log\_lost\_cnt](structshell__stats.md#a1ec10ba96a7805f10d1a021ff1dd3bf2)

atomic\_t log\_lost\_cnt

Lost log counter.

**Definition** shell.h:755

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:668

[shell\_transport\_api::update](structshell__transport__api.md#a3b447d16d7c30f994c582d67bde57ba8)

void(\* update)(const struct shell\_transport \*transport)

Function called in shell thread loop.

**Definition** shell.h:742

[shell\_transport\_api::init](structshell__transport__api.md#a59afba962312a077343b440448d67135)

int(\* init)(const struct shell\_transport \*transport, const void \*config, shell\_transport\_handler\_t evt\_handler, void \*context)

Function for initializing the shell transport interface.

**Definition** shell.h:680

[shell\_transport\_api::write](structshell__transport__api.md#a6bbf2905abcbf6ca564ecf3f07d95712)

int(\* write)(const struct shell\_transport \*transport, const void \*data, size\_t length, size\_t \*cnt)

Function for writing data to the transport interface.

**Definition** shell.h:719

[shell\_transport\_api::uninit](structshell__transport__api.md#a94cc7843174a4aba668389a4b46928d3)

int(\* uninit)(const struct shell\_transport \*transport)

Function for uninitializing the shell transport interface.

**Definition** shell.h:692

[shell\_transport\_api::enable](structshell__transport__api.md#a95535c7195088e68230ecb306f105713)

int(\* enable)(const struct shell\_transport \*transport, bool blocking\_tx)

Function for enabling transport in given TX mode.

**Definition** shell.h:706

[shell\_transport\_api::read](structshell__transport__api.md#aae0e8ad92065dbff10691c28045d0c8f)

int(\* read)(const struct shell\_transport \*transport, void \*data, size\_t length, size\_t \*cnt)

Function for reading data from the transport interface.

**Definition** shell.h:732

[shell\_transport](structshell__transport.md)

**Definition** shell.h:746

[shell\_transport::ctx](structshell__transport.md#a02f44bb376152452f5b5d20f33ccbdf6)

void \* ctx

**Definition** shell.h:748

[shell\_transport::api](structshell__transport.md#ab4bee270415b445ded5a8ba6e8cb3a25)

const struct shell\_transport\_api \* api

**Definition** shell.h:747

[shell\_vt100\_ctx](structshell__vt100__ctx.md)

**Definition** shell\_types.h:44

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:912

[shell::thread](structshell.md#a01b4739356f2428527f322662a3bf0a7)

struct k\_thread \* thread

**Definition** shell.h:931

[shell::LOG\_INSTANCE\_PTR\_DECLARE](structshell.md#a30ad7480b8be019b3b3ed63bf05ad790)

LOG\_INSTANCE\_PTR\_DECLARE(log)

[shell::shell\_flag](structshell.md#a3a4f58c6151b3cbd1293d36b92c2f470)

enum shell\_flag shell\_flag

**Definition** shell.h:920

[shell::log\_backend](structshell.md#a3daffdb9d38ee8132a2644054126680d)

const struct shell\_log\_backend \* log\_backend

**Definition** shell.h:926

[shell::history](structshell.md#a42d2588d15f601baf3f963684d312c86)

struct shell\_history \* history

**Definition** shell.h:918

[shell::stats](structshell.md#a642e7d8fa92464147329247e1325ad2b)

struct shell\_stats \* stats

**Definition** shell.h:924

[shell::name](structshell.md#a66eb938dae4f2b0fd873980c1efeb00b)

const char \* name

**Definition** shell.h:930

[shell::default\_prompt](structshell.md#a97c365dfd7202eb091b1ad016014729b)

const char \* default\_prompt

shell default prompt.

**Definition** shell.h:913

[shell::fprintf\_ctx](structshell.md#aba181907e38def0985a4c6ffd459d935)

const struct shell\_fprintf \* fprintf\_ctx

**Definition** shell.h:922

[shell::ctx](structshell.md#ac14fde7e5f28615b9eec39a2eb8aa8d4)

struct shell\_ctx \* ctx

Internal context.

**Definition** shell.h:916

[shell::iface](structshell.md#ac6033c3c2e44c2c4e29791f1f61c566c)

const struct shell\_transport \* iface

Transport interface.

**Definition** shell.h:915

[shell::stack](structshell.md#ad62262b6b4fa8e56a0e8849f09603b3a)

k\_thread\_stack\_t \* stack

**Definition** shell.h:932

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[shell\_backend\_cfg](unionshell__backend__cfg.md)

**Definition** shell.h:811

[shell\_backend\_cfg::value](unionshell__backend__cfg.md#a2e2aa4e52af6f6e6a827ea946e6681fc)

atomic\_t value

**Definition** shell.h:812

[shell\_backend\_cfg::flags](unionshell__backend__cfg.md#a513e4e2c352c62d13ed655049a7ee691)

struct shell\_backend\_config\_flags flags

**Definition** shell.h:813

[shell\_backend\_ctx](unionshell__backend__ctx.md)

**Definition** shell.h:819

[shell\_backend\_ctx::flags](unionshell__backend__ctx.md#a12e5e07c77eb1f82bac9db6cd2d31316)

struct shell\_backend\_ctx\_flags flags

**Definition** shell.h:821

[shell\_backend\_ctx::value](unionshell__backend__ctx.md#a8de68016e888b8f9b5371c8a7bed4fcb)

uint32\_t value

**Definition** shell.h:820

[shell\_cmd\_entry](unionshell__cmd__entry.md)

Shell command descriptor.

**Definition** shell.h:101

[shell\_cmd\_entry::entry](unionshell__cmd__entry.md#a4abb8327df0e62f63432a05cc885f03d)

const struct shell\_static\_entry \* entry

Pointer to array of static commands.

**Definition** shell.h:106

[shell\_cmd\_entry::dynamic\_get](unionshell__cmd__entry.md#aa76e35866f5df37593705fd1b53e15df)

shell\_dynamic\_get dynamic\_get

Pointer to function returning dynamic commands.

**Definition** shell.h:103

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell.h](shell_2shell_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
