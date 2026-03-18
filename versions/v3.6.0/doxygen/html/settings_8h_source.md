---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/settings_8h_source.html
original_path: doxygen/html/settings_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings.h

[Go to the documentation of this file.](settings_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \* Copyright (c) 2015 Runtime Inc

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_SETTINGS\_SETTINGS\_H\_

9#define ZEPHYR\_INCLUDE\_SETTINGS\_SETTINGS\_H\_

10

11#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

12#include <[zephyr/sys/util.h](util_8h.md)>

13#include <[zephyr/sys/slist.h](slist_8h.md)>

14#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

15#include <[stdint.h](stdint_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21

28

34

[ 35](group__settings.md#ga2afa32b032e88a188c5263156d9e73e1)#define SETTINGS\_MAX\_DIR\_DEPTH 8 /\* max depth of settings tree \*/

[ 36](group__settings.md#gad96357290d7289dd1d7917abd575c4f7)#define SETTINGS\_MAX\_NAME\_LEN (8 \* SETTINGS\_MAX\_DIR\_DEPTH)

[ 37](group__settings.md#gaa9705c71c2d7cfdf3beab49d6b510769)#define SETTINGS\_MAX\_VAL\_LEN 256

[ 38](group__settings.md#gab66e3bb2f0f5f5e3a20c6702df6a0694)#define SETTINGS\_NAME\_SEPARATOR '/'

[ 39](group__settings.md#ga41fb7b74ecb502093d4aa5cd6adb4093)#define SETTINGS\_NAME\_END '='

40

41/\* place for settings additions:

42 \* up to 7 separators, '=', '\0'

43 \*/

[ 44](group__settings.md#ga9f10069ed74c368aef366d659d3a917d)#define SETTINGS\_EXTRA\_LEN ((SETTINGS\_MAX\_DIR\_DEPTH - 1) + 2)

45

[ 59](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04)typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04))(void \*cb\_arg, void \*data, size\_t len);

60

[ 66](structsettings__handler.md)struct [settings\_handler](structsettings__handler.md) {

67

[ 68](structsettings__handler.md#ab8eee945dc866ec90b272fb526abc646) const char \*[name](structsettings__handler.md#ab8eee945dc866ec90b272fb526abc646);

70

[ 71](structsettings__handler.md#a8d4036babe22872777610e54c4dadf21) int (\*[h\_get](structsettings__handler.md#a8d4036babe22872777610e54c4dadf21))(const char \*key, char \*val, int val\_len\_max);

82

[ 83](structsettings__handler.md#a70aa25bf3b53898ab22906e9949963a4) int (\*[h\_set](structsettings__handler.md#a70aa25bf3b53898ab22906e9949963a4))(const char \*key, size\_t len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb,

84 void \*cb\_arg);

97

[ 98](structsettings__handler.md#ad5e23a2acf29bbb2a5a4f249b5f80e0a) int (\*[h\_commit](structsettings__handler.md#ad5e23a2acf29bbb2a5a4f249b5f80e0a))(void);

104

[ 105](structsettings__handler.md#a30207125407f57a0f117ecaee5a2054a) int (\*[h\_export](structsettings__handler.md#a30207125407f57a0f117ecaee5a2054a))(int (\*export\_func)(const char \*[name](structsettings__handler.md#ab8eee945dc866ec90b272fb526abc646), const void \*val,

106 size\_t val\_len));

122

[ 123](structsettings__handler.md#a6aa2cc76c84341c3d29b679d2cc9c6ab) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structsettings__handler.md#a6aa2cc76c84341c3d29b679d2cc9c6ab);

125};

126

[ 132](structsettings__handler__static.md)struct [settings\_handler\_static](structsettings__handler__static.md) {

133

[ 134](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b) const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b);

136

[ 137](structsettings__handler__static.md#acc65e884503cf7db1276e7777f57fb12) int (\*[h\_get](structsettings__handler__static.md#acc65e884503cf7db1276e7777f57fb12))(const char \*key, char \*val, int val\_len\_max);

148

[ 149](structsettings__handler__static.md#a2cf94a6dad3ec35ca58b5ef869c7edae) int (\*[h\_set](structsettings__handler__static.md#a2cf94a6dad3ec35ca58b5ef869c7edae))(const char \*key, size\_t len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb,

150 void \*cb\_arg);

163

[ 164](structsettings__handler__static.md#a093ab8346aedd0a9cb06dfaa4387f393) int (\*[h\_commit](structsettings__handler__static.md#a093ab8346aedd0a9cb06dfaa4387f393))(void);

168

[ 169](structsettings__handler__static.md#abb1df3f0f05fb2a57cd08e380bfffa09) int (\*[h\_export](structsettings__handler__static.md#abb1df3f0f05fb2a57cd08e380bfffa09))(int (\*export\_func)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b), const void \*val,

170 size\_t val\_len));

186};

187

201

[ 202](group__settings.md#ga2098bcfc32c6daa13292d937712e476e)#define SETTINGS\_STATIC\_HANDLER\_DEFINE(\_hname, \_tree, \_get, \_set, \_commit, \

203 \_export) \

204 const STRUCT\_SECTION\_ITERABLE(settings\_handler\_static, \

205 settings\_handler\_ ## \_hname) = { \

206 .name = \_tree, \

207 .h\_get = \_get, \

208 .h\_set = \_set, \

209 .h\_commit = \_commit, \

210 .h\_export = \_export, \

211 }

212

[ 222](group__settings.md#gaf81fad8575840f73a739d16d79613f8e)int [settings\_subsys\_init](group__settings.md#gaf81fad8575840f73a739d16d79613f8e)(void);

223

[ 231](group__settings.md#gab2043a6d799202e177cc3dfa0cbfa531)int [settings\_register](group__settings.md#gab2043a6d799202e177cc3dfa0cbfa531)(struct [settings\_handler](structsettings__handler.md) \*cf);

232

[ 240](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648)int [settings\_load](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648)(void);

241

[ 250](group__settings.md#gab80e8a21c80243359b652386f7ce2424)int [settings\_load\_subtree](group__settings.md#gab80e8a21c80243359b652386f7ce2424)(const char \*subtree);

251

[ 267](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535)typedef int (\*[settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535))(

268 const char \*key,

269 size\_t len,

270 [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb,

271 void \*cb\_arg,

272 void \*param);

273

[ 291](group__settings.md#ga1dfe42f40a7d63bbdb81aed864d0ff12)int [settings\_load\_subtree\_direct](group__settings.md#ga1dfe42f40a7d63bbdb81aed864d0ff12)(

292 const char \*subtree,

293 [settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535) cb,

294 void \*param);

295

[ 302](group__settings.md#ga789410aa059398d6c8a7851ea6945b55)int [settings\_save](group__settings.md#ga789410aa059398d6c8a7851ea6945b55)(void);

303

[ 315](group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30)int [settings\_save\_one](group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30)(const char \*name, const void \*value, size\_t val\_len);

316

[ 327](group__settings.md#ga070b6ad31bca0bee71ec1f1a4d67618d)int [settings\_delete](group__settings.md#ga070b6ad31bca0bee71ec1f1a4d67618d)(const char \*name);

328

[ 335](group__settings.md#ga623c60b89dda3145f9334343748d5954)int [settings\_commit](group__settings.md#ga623c60b89dda3145f9334343748d5954)(void);

336

[ 345](group__settings.md#ga11523bc43121d78e0ac8ee1443559e42)int [settings\_commit\_subtree](group__settings.md#ga11523bc43121d78e0ac8ee1443559e42)(const char \*subtree);

346

350

351

357

358/\*

359 \* API for config storage

360 \*/

361

362struct [settings\_store\_itf](structsettings__store__itf.md);

363

[ 367](structsettings__store.md)struct [settings\_store](structsettings__store.md) {

[ 368](structsettings__store.md#a9f382f4e61737585228a6a3b86e9a38c) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [cs\_next](structsettings__store.md#a9f382f4e61737585228a6a3b86e9a38c);

370

[ 371](structsettings__store.md#aaa0f629059f0c49b0f92f278791ce19c) const struct [settings\_store\_itf](structsettings__store__itf.md) \*[cs\_itf](structsettings__store.md#aaa0f629059f0c49b0f92f278791ce19c);

373};

374

[ 379](structsettings__load__arg.md)struct [settings\_load\_arg](structsettings__load__arg.md) {

[ 385](structsettings__load__arg.md#a0764239993147761b12e8999f860d267) const char \*[subtree](structsettings__load__arg.md#a0764239993147761b12e8999f860d267);

[ 391](structsettings__load__arg.md#aec32e51b4a6b61aff2ea415aa80a9987) [settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535) [cb](structsettings__load__arg.md#aec32e51b4a6b61aff2ea415aa80a9987);

[ 397](structsettings__load__arg.md#a7cbe713a1e0d2885528644b5a54f27d3) void \*[param](structsettings__load__arg.md#a7cbe713a1e0d2885528644b5a54f27d3);

398};

399

[ 405](structsettings__store__itf.md)struct [settings\_store\_itf](structsettings__store__itf.md) {

[ 406](structsettings__store__itf.md#a8c08da2cd010f5d73689e84d02d12734) int (\*[csi\_load](structsettings__store__itf.md#a8c08da2cd010f5d73689e84d02d12734))(struct [settings\_store](structsettings__store.md) \*cs,

407 const struct [settings\_load\_arg](structsettings__load__arg.md) \*arg);

420

[ 421](structsettings__store__itf.md#af6aae0b06cdc935975f19eb4c56eb991) int (\*[csi\_save\_start](structsettings__store__itf.md#af6aae0b06cdc935975f19eb4c56eb991))(struct [settings\_store](structsettings__store.md) \*cs);

427

[ 428](structsettings__store__itf.md#af97b8a3e2bdac663dd3872117251f0d2) int (\*[csi\_save](structsettings__store__itf.md#af97b8a3e2bdac663dd3872117251f0d2))(struct [settings\_store](structsettings__store.md) \*cs, const char \*name,

429 const char \*value, size\_t val\_len);

438

[ 439](structsettings__store__itf.md#a90c2506cb06e5d80dffc6c08c6007bce) int (\*[csi\_save\_end](structsettings__store__itf.md#a90c2506cb06e5d80dffc6c08c6007bce))(struct [settings\_store](structsettings__store.md) \*cs);

445

[ 451](structsettings__store__itf.md#a01440145124432463ada9a7e1badf727) void \*(\*csi\_storage\_get)(struct [settings\_store](structsettings__store.md) \*cs);

452};

453

[ 460](group__settings__backend.md#gad16bb70588cf69873f8872d7bf90e1c6)void [settings\_src\_register](group__settings__backend.md#gad16bb70588cf69873f8872d7bf90e1c6)(struct [settings\_store](structsettings__store.md) \*cs);

461

[ 468](group__settings__backend.md#ga37bcada0be44b023cd3759e519e69d01)void [settings\_dst\_register](group__settings__backend.md#ga37bcada0be44b023cd3759e519e69d01)(struct [settings\_store](structsettings__store.md) \*cs);

469

470

471/\*

472 \* API for handler lookup

473 \*/

474

[ 483](group__settings__backend.md#gab03a10ed0b65809369b4b6f220aa3df6)struct [settings\_handler\_static](structsettings__handler__static.md) \*[settings\_parse\_and\_lookup](group__settings__backend.md#gab03a10ed0b65809369b4b6f220aa3df6)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b),

484 const char \*\*next);

485

[ 499](group__settings__backend.md#gaf94e311eba2b109cdbddd2767e502e77)int [settings\_call\_set\_handler](group__settings__backend.md#gaf94e311eba2b109cdbddd2767e502e77)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b),

500 size\_t len,

501 [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb,

502 void \*read\_cb\_arg,

503 const struct [settings\_load\_arg](structsettings__load__arg.md) \*load\_arg);

507

514

[ 535](group__settings__name__proc.md#ga6d9d36d54a1bfd59bf7729621653edd9)int [settings\_name\_steq](group__settings__name__proc.md#ga6d9d36d54a1bfd59bf7729621653edd9)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b), const char \*key, const char \*\*next);

536

[ 547](group__settings__name__proc.md#gacf259320845ae83c46df634f93c6d3e5)int [settings\_name\_next](group__settings__name__proc.md#gacf259320845ae83c46df634f93c6d3e5)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b), const char \*\*next);

551

552#ifdef CONFIG\_SETTINGS\_RUNTIME

553

560

[ 570](group__settings__rt.md#gae1b95c47c49774d53b4745af810e881e)int [settings\_runtime\_set](group__settings__rt.md#gae1b95c47c49774d53b4745af810e881e)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b), const void \*data, size\_t len);

571

[ 581](group__settings__rt.md#ga99a4714ba8c184afc659c43ec2020844)int [settings\_runtime\_get](group__settings__rt.md#ga99a4714ba8c184afc659c43ec2020844)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b), void \*data, size\_t len);

582

[ 590](group__settings__rt.md#gafa96974170dced7a131bfd5f022483f8)int [settings\_runtime\_commit](group__settings__rt.md#gafa96974170dced7a131bfd5f022483f8)(const char \*[name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b));

594

595#endif /\* CONFIG\_SETTINGS\_RUNTIME \*/

596

[ 608](settings_8h.md#a282c5c2c25ae5a375c51150a87869f14)int [settings\_storage\_get](settings_8h.md#a282c5c2c25ae5a375c51150a87869f14)(void \*\*storage);

609

610#ifdef \_\_cplusplus

611}

612#endif

613

614#endif /\* ZEPHYR\_INCLUDE\_SETTINGS\_SETTINGS\_H\_ \*/

[settings\_dst\_register](group__settings__backend.md#ga37bcada0be44b023cd3759e519e69d01)

void settings\_dst\_register(struct settings\_store \*cs)

Register a backend handler acting as destination.

[settings\_parse\_and\_lookup](group__settings__backend.md#gab03a10ed0b65809369b4b6f220aa3df6)

struct settings\_handler\_static \* settings\_parse\_and\_lookup(const char \*name, const char \*\*next)

Parses a key to an array of elements and locate corresponding module handler.

[settings\_src\_register](group__settings__backend.md#gad16bb70588cf69873f8872d7bf90e1c6)

void settings\_src\_register(struct settings\_store \*cs)

Register a backend handler acting as source.

[settings\_call\_set\_handler](group__settings__backend.md#gaf94e311eba2b109cdbddd2767e502e77)

int settings\_call\_set\_handler(const char \*name, size\_t len, settings\_read\_cb read\_cb, void \*read\_cb\_arg, const struct settings\_load\_arg \*load\_arg)

Calls settings handler.

[settings\_name\_steq](group__settings__name__proc.md#ga6d9d36d54a1bfd59bf7729621653edd9)

int settings\_name\_steq(const char \*name, const char \*key, const char \*\*next)

Compares the start of name with a key.

[settings\_name\_next](group__settings__name__proc.md#gacf259320845ae83c46df634f93c6d3e5)

int settings\_name\_next(const char \*name, const char \*\*next)

determine the number of characters before the first separator

[settings\_runtime\_get](group__settings__rt.md#ga99a4714ba8c184afc659c43ec2020844)

int settings\_runtime\_get(const char \*name, void \*data, size\_t len)

Get a value corresponding to a key from a module handler.

[settings\_runtime\_set](group__settings__rt.md#gae1b95c47c49774d53b4745af810e881e)

int settings\_runtime\_set(const char \*name, const void \*data, size\_t len)

Set a value with a specific key to a module handler.

[settings\_runtime\_commit](group__settings__rt.md#gafa96974170dced7a131bfd5f022483f8)

int settings\_runtime\_commit(const char \*name)

Apply settings in a module handler.

[settings\_delete](group__settings.md#ga070b6ad31bca0bee71ec1f1a4d67618d)

int settings\_delete(const char \*name)

Delete a single serialized in persisted storage.

[settings\_commit\_subtree](group__settings.md#ga11523bc43121d78e0ac8ee1443559e42)

int settings\_commit\_subtree(const char \*subtree)

Call commit for settings handler that belong to subtree.

[settings\_load\_subtree\_direct](group__settings.md#ga1dfe42f40a7d63bbdb81aed864d0ff12)

int settings\_load\_subtree\_direct(const char \*subtree, settings\_load\_direct\_cb cb, void \*param)

Load limited set of serialized items using given callback.

[settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04)

ssize\_t(\* settings\_read\_cb)(void \*cb\_arg, void \*data, size\_t len)

Function used to read the data from the settings storage in h\_set handler implementations.

**Definition** settings.h:59

[settings\_commit](group__settings.md#ga623c60b89dda3145f9334343748d5954)

int settings\_commit(void)

Call commit for all settings handler.

[settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535)

int(\* settings\_load\_direct\_cb)(const char \*key, size\_t len, settings\_read\_cb read\_cb, void \*cb\_arg, void \*param)

Callback function used for direct loading.

**Definition** settings.h:267

[settings\_save](group__settings.md#ga789410aa059398d6c8a7851ea6945b55)

int settings\_save(void)

Save currently running serialized items.

[settings\_load](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648)

int settings\_load(void)

Load serialized items from registered persistence sources.

[settings\_register](group__settings.md#gab2043a6d799202e177cc3dfa0cbfa531)

int settings\_register(struct settings\_handler \*cf)

Register a handler for settings items stored in RAM.

[settings\_load\_subtree](group__settings.md#gab80e8a21c80243359b652386f7ce2424)

int settings\_load\_subtree(const char \*subtree)

Load limited set of serialized items from registered persistence sources.

[settings\_save\_one](group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30)

int settings\_save\_one(const char \*name, const void \*value, size\_t val\_len)

Write a single serialized value to persisted storage (if it has changed value).

[settings\_subsys\_init](group__settings.md#gaf81fad8575840f73a739d16d79613f8e)

int settings\_subsys\_init(void)

Initialization of settings and backend.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[settings\_storage\_get](settings_8h.md#a282c5c2c25ae5a375c51150a87869f14)

int settings\_storage\_get(void \*\*storage)

Get the storage instance used by zephyr.

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[settings\_handler\_static](structsettings__handler__static.md)

Config handlers without the node element, used for static handlers.

**Definition** settings.h:132

[settings\_handler\_static::h\_commit](structsettings__handler__static.md#a093ab8346aedd0a9cb06dfaa4387f393)

int(\* h\_commit)(void)

This handler gets called after settings has been loaded in full.

**Definition** settings.h:164

[settings\_handler\_static::h\_set](structsettings__handler__static.md#a2cf94a6dad3ec35ca58b5ef869c7edae)

int(\* h\_set)(const char \*key, size\_t len, settings\_read\_cb read\_cb, void \*cb\_arg)

Set value handler of settings items identified by keyword names.

**Definition** settings.h:149

[settings\_handler\_static::name](structsettings__handler__static.md#aa8e57471bd89f4792cfb0689462b6f9b)

const char \* name

Name of subtree.

**Definition** settings.h:134

[settings\_handler\_static::h\_export](structsettings__handler__static.md#abb1df3f0f05fb2a57cd08e380bfffa09)

int(\* h\_export)(int(\*export\_func)(const char \*name, const void \*val, size\_t val\_len))

This gets called to dump all current settings items.

**Definition** settings.h:169

[settings\_handler\_static::h\_get](structsettings__handler__static.md#acc65e884503cf7db1276e7777f57fb12)

int(\* h\_get)(const char \*key, char \*val, int val\_len\_max)

Get values handler of settings items identified by keyword names.

**Definition** settings.h:137

[settings\_handler](structsettings__handler.md)

Config handlers for subtree implement a set of handler functions.

**Definition** settings.h:66

[settings\_handler::h\_export](structsettings__handler.md#a30207125407f57a0f117ecaee5a2054a)

int(\* h\_export)(int(\*export\_func)(const char \*name, const void \*val, size\_t val\_len))

This gets called to dump all current settings items.

**Definition** settings.h:105

[settings\_handler::node](structsettings__handler.md#a6aa2cc76c84341c3d29b679d2cc9c6ab)

sys\_snode\_t node

Linked list node info for module internal usage.

**Definition** settings.h:123

[settings\_handler::h\_set](structsettings__handler.md#a70aa25bf3b53898ab22906e9949963a4)

int(\* h\_set)(const char \*key, size\_t len, settings\_read\_cb read\_cb, void \*cb\_arg)

Set value handler of settings items identified by keyword names.

**Definition** settings.h:83

[settings\_handler::h\_get](structsettings__handler.md#a8d4036babe22872777610e54c4dadf21)

int(\* h\_get)(const char \*key, char \*val, int val\_len\_max)

Get values handler of settings items identified by keyword names.

**Definition** settings.h:71

[settings\_handler::name](structsettings__handler.md#ab8eee945dc866ec90b272fb526abc646)

const char \* name

Name of subtree.

**Definition** settings.h:68

[settings\_handler::h\_commit](structsettings__handler.md#ad5e23a2acf29bbb2a5a4f249b5f80e0a)

int(\* h\_commit)(void)

This handler gets called after settings has been loaded in full.

**Definition** settings.h:98

[settings\_load\_arg](structsettings__load__arg.md)

Arguments for data loading.

**Definition** settings.h:379

[settings\_load\_arg::subtree](structsettings__load__arg.md#a0764239993147761b12e8999f860d267)

const char \* subtree

Name of the subtree to be loaded.

**Definition** settings.h:385

[settings\_load\_arg::param](structsettings__load__arg.md#a7cbe713a1e0d2885528644b5a54f27d3)

void \* param

Parameter for callback function.

**Definition** settings.h:397

[settings\_load\_arg::cb](structsettings__load__arg.md#aec32e51b4a6b61aff2ea415aa80a9987)

settings\_load\_direct\_cb cb

Pointer to the callback function.

**Definition** settings.h:391

[settings\_store\_itf](structsettings__store__itf.md)

Backend handler functions.

**Definition** settings.h:405

[settings\_store\_itf::csi\_load](structsettings__store__itf.md#a8c08da2cd010f5d73689e84d02d12734)

int(\* csi\_load)(struct settings\_store \*cs, const struct settings\_load\_arg \*arg)

Loads values from storage limited to subtree defined by subtree.

**Definition** settings.h:406

[settings\_store\_itf::csi\_save\_end](structsettings__store__itf.md#a90c2506cb06e5d80dffc6c08c6007bce)

int(\* csi\_save\_end)(struct settings\_store \*cs)

Handler called after an export operation.

**Definition** settings.h:439

[settings\_store\_itf::csi\_save\_start](structsettings__store__itf.md#af6aae0b06cdc935975f19eb4c56eb991)

int(\* csi\_save\_start)(struct settings\_store \*cs)

Handler called before an export operation.

**Definition** settings.h:421

[settings\_store\_itf::csi\_save](structsettings__store__itf.md#af97b8a3e2bdac663dd3872117251f0d2)

int(\* csi\_save)(struct settings\_store \*cs, const char \*name, const char \*value, size\_t val\_len)

Save a single key-value pair to storage.

**Definition** settings.h:428

[settings\_store](structsettings__store.md)

Backend handler node for storage handling.

**Definition** settings.h:367

[settings\_store::cs\_next](structsettings__store.md#a9f382f4e61737585228a6a3b86e9a38c)

sys\_snode\_t cs\_next

Linked list node info for internal usage.

**Definition** settings.h:368

[settings\_store::cs\_itf](structsettings__store.md#aaa0f629059f0c49b0f92f278791ce19c)

const struct settings\_store\_itf \* cs\_itf

Backend handler structure.

**Definition** settings.h:371

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [settings](dir_d86a196c339fcb483c3ba090e397efd2.md)
- [settings.h](settings_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
