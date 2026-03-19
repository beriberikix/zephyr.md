---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/input-event-codes_8h.html
original_path: doxygen/html/input-event-codes_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input-event-codes.h File Reference

[Go to the source code of this file.](input-event-codes_8h_source.md)

| Macros | |
| --- | --- |
| Input event types. | |
|  | |
| #define | [INPUT\_EV\_KEY](group__input__events.md#ga4a517c31bdbdd1bd82ba456d256ef1f1)   0x01 |
|  | Key event. |
| #define | [INPUT\_EV\_REL](group__input__events.md#ga02de6c85efab3d21eb81e88e54d58e03)   0x02 |
|  | Relative coordinate event. |
| #define | [INPUT\_EV\_ABS](group__input__events.md#gaa6bcd6755fbdb3eb103f03a72759ce4f)   0x03 |
|  | Absolute coordinate event. |
| #define | [INPUT\_EV\_MSC](group__input__events.md#ga40ab1faa2e28e32c30016ad854afa6cf)   0x04 |
|  | Miscellaneous event. |
| #define | [INPUT\_EV\_DEVICE](group__input__events.md#ga3ebe8a83ea38c4c87cda6bc9e18f2e61)   0xef |
|  | Device specific input event. |
| #define | [INPUT\_EV\_VENDOR\_START](group__input__events.md#ga7037a9ea2e0a63c40a5d206e507e5f42)   0xf0 |
|  | Vendor specific event start. |
| #define | [INPUT\_EV\_VENDOR\_STOP](group__input__events.md#gaa19a341e18ff5c43e1b8ddf58c7b9676)   0xff |
|  | Vendor specific event stop. |
| Input event KEY codes. | |
|  | |
| #define | [INPUT\_KEY\_RESERVED](group__input__events.md#ga94e5a0d74dad76e57679b97af90ecb65)   0 |
|  | Reserved, do not use. |
| #define | [INPUT\_KEY\_0](group__input__events.md#gab41cb2f1768b0a0667ab6509b6d3af21)   11 |
|  | 0 Key |
| #define | [INPUT\_KEY\_1](group__input__events.md#gad62520853a15b74d68c1bab5a3119eaa)   2 |
|  | 1 Key |
| #define | [INPUT\_KEY\_2](group__input__events.md#gadb02e289d07d4d4457c88b1ada7e2534)   3 |
|  | 2 Key |
| #define | [INPUT\_KEY\_3](group__input__events.md#ga95a246cefcaafd26d15c1c124bdf2ca4)   4 |
|  | 3 Key |
| #define | [INPUT\_KEY\_4](group__input__events.md#ga0c16c2e62a65eab0fe8952a4cf60254d)   5 |
|  | 4 Key |
| #define | [INPUT\_KEY\_5](group__input__events.md#ga386e2c69d5e5a9549668b1a2a2d297e1)   6 |
|  | 5 Key |
| #define | [INPUT\_KEY\_6](group__input__events.md#ga87e0cea90040710253718ce29c407f3e)   7 |
|  | 6 Key |
| #define | [INPUT\_KEY\_7](group__input__events.md#ga090686eaaacddb8c2f58b31b4b9801b8)   8 |
|  | 7 Key |
| #define | [INPUT\_KEY\_8](group__input__events.md#ga6f2b66c0eea17b044778a326ffcd3f57)   9 |
|  | 8 Key |
| #define | [INPUT\_KEY\_9](group__input__events.md#ga91473de481c47f3f9e40caf42e49250f)   10 |
|  | 9 Key |
| #define | [INPUT\_KEY\_A](group__input__events.md#ga553b457efaafb3cdc41e7b1e953cd6fe)   30 |
|  | A Key. |
| #define | [INPUT\_KEY\_APOSTROPHE](group__input__events.md#gaa528a10eb85fa9dc46198e08962fab3a)   40 |
|  | Apostrophe Key. |
| #define | [INPUT\_KEY\_B](group__input__events.md#gaaae2c60e8907c14c094e5c1c4e3dae3b)   48 |
|  | B Key. |
| #define | [INPUT\_KEY\_BACK](group__input__events.md#gab5ad87c6e97f6b09f9dc1a1570a9c299)   158 |
|  | Back Key. |
| #define | [INPUT\_KEY\_BACKSLASH](group__input__events.md#ga180fcae595fbc580bfe1a94414a4b02b)   43 |
|  | Backslash Key. |
| #define | [INPUT\_KEY\_BACKSPACE](group__input__events.md#ga654ffbdc8f2fef696ee0237704cebc34)   14 |
|  | Backspace Key. |
| #define | [INPUT\_KEY\_BLUETOOTH](group__input__events.md#ga26f6330d7631bdae0f2bb34f623a85ae)   237 |
|  | Bluetooth Key. |
| #define | [INPUT\_KEY\_BRIGHTNESSDOWN](group__input__events.md#gac4afc3e97b18a1f22e3d59730177e27f)   224 |
|  | Brightness Up Key. |
| #define | [INPUT\_KEY\_BRIGHTNESSUP](group__input__events.md#gaff59e776a3e3a0fe4d32caeb41a32c53)   225 |
|  | Brightneess Down Key. |
| #define | [INPUT\_KEY\_C](group__input__events.md#ga1b88afc2eacfbbd778785398baebd287)   46 |
|  | C Key. |
| #define | [INPUT\_KEY\_CAPSLOCK](group__input__events.md#ga8dfa14142766962272afc77538f8a909)   58 |
|  | Caps Lock Key. |
| #define | [INPUT\_KEY\_COFFEE](group__input__events.md#ga345dc788101108c27f488cfa0fc885c8)   152 |
|  | Screen Saver Key. |
| #define | [INPUT\_KEY\_COMMA](group__input__events.md#ga1220a9e90676992fcd3c308a7f1038f7)   51 |
|  | Comma Key. |
| #define | [INPUT\_KEY\_COMPOSE](group__input__events.md#ga52882fff91dc0c288cf0b60baa60be65)   127 |
|  | Compose Key. |
| #define | [INPUT\_KEY\_CONNECT](group__input__events.md#gaedf1f55d35163e56ca03f4409ea6b7d0)   218 |
|  | Connect Key. |
| #define | [INPUT\_KEY\_D](group__input__events.md#ga206eda236c1ce08e3ad6eef192ac303e)   32 |
|  | D Key. |
| #define | [INPUT\_KEY\_DELETE](group__input__events.md#ga2abef21124d504927c675959331a4c3b)   111 |
|  | Delete Key. |
| #define | [INPUT\_KEY\_DOT](group__input__events.md#gacbd30145c479c472d105a0c5251c0e4d)   52 |
|  | Dot Key. |
| #define | [INPUT\_KEY\_DOWN](group__input__events.md#gad80b82e35e50f775a091b8f5031d2c9b)   108 |
|  | Down Key. |
| #define | [INPUT\_KEY\_E](group__input__events.md#ga4c1a1f169d8159ed36b194ae3d0aa0e7)   18 |
|  | E Key. |
| #define | [INPUT\_KEY\_END](group__input__events.md#gaff91435e45612b50955523d029dfd1e4)   107 |
|  | End Key. |
| #define | [INPUT\_KEY\_ENTER](group__input__events.md#ga8e4e6c4072fd5595a80a4e4ff1ae1c32)   28 |
|  | Enter Key. |
| #define | [INPUT\_KEY\_EQUAL](group__input__events.md#ga0775ec23155f396f368425fb4dc35e54)   13 |
|  | Equal Key. |
| #define | [INPUT\_KEY\_ESC](group__input__events.md#ga2026ab8608c7013781cdcf1e546e4d93)   1 |
|  | Escape Key. |
| #define | [INPUT\_KEY\_F](group__input__events.md#gaed15f4e46a5e80bd9d8508f2f0317386)   33 |
|  | F Key. |
| #define | [INPUT\_KEY\_F1](group__input__events.md#ga06374b0c4c42d708874d799afac87f54)   59 |
|  | F1 Key. |
| #define | [INPUT\_KEY\_F10](group__input__events.md#ga925bd568cbef2c8241a8bc38cd1fc0ee)   68 |
|  | F10 Key. |
| #define | [INPUT\_KEY\_F11](group__input__events.md#gaf8db5439ca4244843ddea6c78e235227)   87 |
|  | F11 Key. |
| #define | [INPUT\_KEY\_F12](group__input__events.md#gac206e26c278998da99fc7907f2d68d90)   88 |
|  | F12 Key. |
| #define | [INPUT\_KEY\_F13](group__input__events.md#gafe37c9d54407b3401974a400831d9200)   183 |
|  | F13 Key. |
| #define | [INPUT\_KEY\_F14](group__input__events.md#ga57112c273fb46a4f748047953355e430)   184 |
|  | F14 Key. |
| #define | [INPUT\_KEY\_F15](group__input__events.md#ga379756870b1a1d808f97f60cf2d3ecc5)   185 |
|  | F15 Key. |
| #define | [INPUT\_KEY\_F16](group__input__events.md#ga0336cf1cdcaa5ee62c1a4a7d7b5f94b0)   186 |
|  | F16 Key. |
| #define | [INPUT\_KEY\_F17](group__input__events.md#ga15ae8eaffd7978c3d91fe05bfedaec0d)   187 |
|  | F17 Key. |
| #define | [INPUT\_KEY\_F18](group__input__events.md#gaf58e8117aadc979c00e99e5d2944e572)   188 |
|  | F18 Key. |
| #define | [INPUT\_KEY\_F19](group__input__events.md#ga45127f8182970453761bea5703e164ca)   189 |
|  | F19 Key. |
| #define | [INPUT\_KEY\_F2](group__input__events.md#gae7ea4afc3ee03cba0820e1230a1bc844)   60 |
|  | F2 Key. |
| #define | [INPUT\_KEY\_F20](group__input__events.md#gaa0d8d5c8f17f26a6571bd50acd7e7c56)   190 |
|  | F20 Key. |
| #define | [INPUT\_KEY\_F21](group__input__events.md#ga958fc836aa61bd04731563b97b3f2c3b)   191 |
|  | F21 Key. |
| #define | [INPUT\_KEY\_F22](group__input__events.md#ga9f865f6f67f7ad3e747450cbe7bd001b)   192 |
|  | F22 Key. |
| #define | [INPUT\_KEY\_F23](group__input__events.md#ga201402a9046f510fcc818fc281acdd74)   193 |
|  | F23 Key. |
| #define | [INPUT\_KEY\_F24](group__input__events.md#gade48ffdee4f9fc816467f61444e388d4)   194 |
|  | F24 Key. |
| #define | [INPUT\_KEY\_F3](group__input__events.md#gaa186203f9efabb0868348938e5eabcfd)   61 |
|  | F3 Key. |
| #define | [INPUT\_KEY\_F4](group__input__events.md#gace5db941d06022b3b33dd9e72a799b68)   62 |
|  | F4 Key. |
| #define | [INPUT\_KEY\_F5](group__input__events.md#ga5ab64f326303e6b097eac8f9a1827feb)   63 |
|  | F5 Key. |
| #define | [INPUT\_KEY\_F6](group__input__events.md#ga3f8d3788cd179ffb9d68de85e23ee1b0)   64 |
|  | F6 Key. |
| #define | [INPUT\_KEY\_F7](group__input__events.md#ga647c9e3d15d4866c3ae486b09f6182fa)   65 |
|  | F7 Key. |
| #define | [INPUT\_KEY\_F8](group__input__events.md#ga6a1be4c1720c9bbd18950ba7d9b91042)   66 |
|  | F8 Key. |
| #define | [INPUT\_KEY\_F9](group__input__events.md#ga16baac9275d3b860e117705aba632681)   67 |
|  | F9 Key. |
| #define | [INPUT\_KEY\_FASTFORWARD](group__input__events.md#ga6c9a01c0a070b213af72cb8088e75876)   208 |
|  | Fast Forward Key. |
| #define | [INPUT\_KEY\_FORWARD](group__input__events.md#gad64d70c2ccc65f5189666efa0847ca7a)   159 |
|  | Forward Key. |
| #define | [INPUT\_KEY\_G](group__input__events.md#ga5480ba49acaa553a194984a98b92f552)   34 |
|  | G Key. |
| #define | [INPUT\_KEY\_GRAVE](group__input__events.md#ga1aaa62276091bde62d4e5aa872902559)   41 |
|  | Grave (backtick) Key. |
| #define | [INPUT\_KEY\_H](group__input__events.md#ga3014cf5abad3b71a0ae45b5b7c713f38)   35 |
|  | H Key. |
| #define | [INPUT\_KEY\_HOME](group__input__events.md#gaa8314d1e4f4ca225922f039791b36d42)   102 |
|  | Home Key. |
| #define | [INPUT\_KEY\_I](group__input__events.md#ga6c987aa5736663b7f309f2b2fb9423c5)   23 |
|  | I Key. |
| #define | [INPUT\_KEY\_INSERT](group__input__events.md#gabfa379fe24dd23461e435de41c23864d)   110 |
|  | Insert Key. |
| #define | [INPUT\_KEY\_J](group__input__events.md#ga7d5c3e334909eb4b2c76217b69a61260)   36 |
|  | J Key. |
| #define | [INPUT\_KEY\_K](group__input__events.md#ga8cb73e35923639e77e861631565134df)   37 |
|  | K Key. |
| #define | [INPUT\_KEY\_KP0](group__input__events.md#ga8e5438fce6c7a717da4322de2982a2ed)   82 |
|  | Keypad 0 Key. |
| #define | [INPUT\_KEY\_KP1](group__input__events.md#gaa5b65c8ff4b94208ff434f3ed8c9f1f1)   79 |
|  | Keypad 1 Key. |
| #define | [INPUT\_KEY\_KP2](group__input__events.md#gad50d9044613b97c6d6292afe15cceb06)   80 |
|  | Keypad 2 Key. |
| #define | [INPUT\_KEY\_KP3](group__input__events.md#ga8a084e91c2906b1f8dd43939293d4812)   81 |
|  | Keypad 3 Key. |
| #define | [INPUT\_KEY\_KP4](group__input__events.md#ga1a9ca528816497bf32bee4e524d2977c)   75 |
|  | Keypad 4 Key. |
| #define | [INPUT\_KEY\_KP5](group__input__events.md#ga83e04456cf68db301973d09af1a19641)   76 |
|  | Keypad 5 Key. |
| #define | [INPUT\_KEY\_KP6](group__input__events.md#gabd7a6dc0d9440de1ffef2a3643583966)   77 |
|  | Keypad 6 Key. |
| #define | [INPUT\_KEY\_KP7](group__input__events.md#ga58709627a1190549d0e0004e4b5bcd74)   71 |
|  | Keypad 7 Key. |
| #define | [INPUT\_KEY\_KP8](group__input__events.md#ga94e64bbd09dda7434d8a9f086daca1a7)   72 |
|  | Keypad 8 Key. |
| #define | [INPUT\_KEY\_KP9](group__input__events.md#ga7dda283e4603e0ce4d14a9a87ea74c4f)   73 |
|  | Keypad 9 Key. |
| #define | [INPUT\_KEY\_KPASTERISK](group__input__events.md#gaa0c33b6ba975617f93230aa75a49fef5)   55 |
|  | Keypad Asterisk Key. |
| #define | [INPUT\_KEY\_KPCOMMA](group__input__events.md#gabb3767d06adbe20b3fb580e8816f916f)   121 |
|  | Keypad Comma Key. |
| #define | [INPUT\_KEY\_KPDOT](group__input__events.md#gac6c07467b6202089166c56c498fd4b27)   83 |
|  | Keypad Dot Key. |
| #define | [INPUT\_KEY\_KPENTER](group__input__events.md#gae8fd841f81d29788d5d0b602538bbd0e)   96 |
|  | Keypad Enter Key. |
| #define | [INPUT\_KEY\_KPEQUAL](group__input__events.md#gaefdae376c1daf752b698efaf89a07b18)   117 |
|  | Keypad Equal Key. |
| #define | [INPUT\_KEY\_KPMINUS](group__input__events.md#gad4f23f54ec4f2252864c507e09ad9cea)   74 |
|  | Keypad Minus Key. |
| #define | [INPUT\_KEY\_KPPLUS](group__input__events.md#ga3d6307d0237d8f34a3d448dc9e40528f)   78 |
|  | Keypad Plus Key. |
| #define | [INPUT\_KEY\_KPPLUSMINUS](group__input__events.md#ga21a77384e45feb96ecc322032dc7231e)   118 |
|  | Keypad Plus Key. |
| #define | [INPUT\_KEY\_KPSLASH](group__input__events.md#gab3f0ce8548cef85df2672d09d021fe39)   98 |
|  | Keypad Slash Key. |
| #define | [INPUT\_KEY\_L](group__input__events.md#gad79329b4b6c3eaad43aabac8c3538622)   38 |
|  | L Key. |
| #define | [INPUT\_KEY\_LEFT](group__input__events.md#gae8c0a4811cd2056d0b6885239d635492)   105 |
|  | Left Key. |
| #define | [INPUT\_KEY\_LEFTALT](group__input__events.md#ga8d384257be19e2eb0d807d35f2656f16)   56 |
|  | Left Alt Key. |
| #define | [INPUT\_KEY\_LEFTBRACE](group__input__events.md#gaecdffb7aff0fee1e078319a23a97e10e)   26 |
|  | Left Brace Key. |
| #define | [INPUT\_KEY\_LEFTCTRL](group__input__events.md#ga1bc52bc876c50da66cc292f250603db7)   29 |
|  | Left Ctrl Key. |
| #define | [INPUT\_KEY\_LEFTMETA](group__input__events.md#gad18b505a7f718887f932a5b7fedfecd3)   125 |
|  | Left Meta Key. |
| #define | [INPUT\_KEY\_LEFTSHIFT](group__input__events.md#gacaf73383130558303396a7add94bdafd)   42 |
|  | Left Shift Key. |
| #define | [INPUT\_KEY\_M](group__input__events.md#ga7c8f628eb719d1d4b428805914c376a7)   50 |
|  | M Key. |
| #define | [INPUT\_KEY\_MENU](group__input__events.md#gab159cae18818e930e4d928ebcc206651)   139 |
|  | Menu Key. |
| #define | [INPUT\_KEY\_MINUS](group__input__events.md#gae9779c5f21b9e14e5cbe1db8c5073819)   12 |
|  | Minus Key. |
| #define | [INPUT\_KEY\_MUTE](group__input__events.md#ga8554adab31fc9c20c9de01bcb2aff839)   113 |
|  | Mute Key. |
| #define | [INPUT\_KEY\_N](group__input__events.md#ga09c0c860ee76803bb317dbac1072cd1d)   49 |
|  | N Key. |
| #define | [INPUT\_KEY\_NUMLOCK](group__input__events.md#ga93e220e43b3d33ffa985445f6dbf9c3c)   69 |
|  | Num Lock Key. |
| #define | [INPUT\_KEY\_O](group__input__events.md#gae964cb377e0bcd958dad6da9626d298c)   24 |
|  | O Key. |
| #define | [INPUT\_KEY\_P](group__input__events.md#ga396def37642dee65c74c48ff72aaa53d)   25 |
|  | P Key. |
| #define | [INPUT\_KEY\_PAGEDOWN](group__input__events.md#gaf6bc999ac2a136235fe95803c6df73c1)   109 |
|  | Page Down Key. |
| #define | [INPUT\_KEY\_PAGEUP](group__input__events.md#gaebb169acd4c3ce873353fd595364b374)   104 |
|  | Page UpKey. |
| #define | [INPUT\_KEY\_PAUSE](group__input__events.md#ga08319efd258cd774ff8bc964c5a402dd)   119 |
|  | Pause Key. |
| #define | [INPUT\_KEY\_PLAY](group__input__events.md#ga1a377fdb1967aeff84e96d47c71bcf41)   207 |
|  | Play Key. |
| #define | [INPUT\_KEY\_POWER](group__input__events.md#ga2b05b5429ef1b0dc37698b82201d257d)   116 |
|  | Power Key. |
| #define | [INPUT\_KEY\_PRINT](group__input__events.md#ga4927612cf9f69324b15d8d9e46ab3326)   210 |
|  | Print Key. |
| #define | [INPUT\_KEY\_Q](group__input__events.md#ga9ee8d6012d74e489ee8072f71497a36e)   16 |
|  | Q Key. |
| #define | [INPUT\_KEY\_R](group__input__events.md#ga421f14c501d86ed907ed4249f93a9e7e)   19 |
|  | R Key. |
| #define | [INPUT\_KEY\_RIGHT](group__input__events.md#ga1bf6f292c1ab3ca25001b4ef4ca2626b)   106 |
|  | Right Key. |
| #define | [INPUT\_KEY\_RIGHTALT](group__input__events.md#gac02b6a2133d5ddf8847e1ce94250536f)   100 |
|  | Right Alt Key. |
| #define | [INPUT\_KEY\_RIGHTBRACE](group__input__events.md#gaa0802d3471f6c774d37a8827e632d7fb)   27 |
|  | Right Brace Key. |
| #define | [INPUT\_KEY\_RIGHTCTRL](group__input__events.md#gabb2e15ee9c30a649c92e82c42f513a35)   97 |
|  | Right Ctrl Key. |
| #define | [INPUT\_KEY\_RIGHTMETA](group__input__events.md#ga23ebc28da84872b585c9dcfeb057bfc9)   126 |
|  | Right Meta Key. |
| #define | [INPUT\_KEY\_RIGHTSHIFT](group__input__events.md#ga4fce26a4ffc693507043c1cfe95d279d)   54 |
|  | Right Shift Key. |
| #define | [INPUT\_KEY\_S](group__input__events.md#gadefb5566a41148a0df4dd95cb2c5e2d2)   31 |
|  | S Key. |
| #define | [INPUT\_KEY\_SCALE](group__input__events.md#ga32491acdefb2e9f0eab5e7fc5755d2bc)   120 |
|  | Scale Key. |
| #define | [INPUT\_KEY\_SCROLLLOCK](group__input__events.md#ga1d0958d93ddb7f3ff662e84a06c95a7c)   70 |
|  | Scroll Lock Key. |
| #define | [INPUT\_KEY\_SEMICOLON](group__input__events.md#ga7d45c7e2399dc6b20b6e470cb35d1dd6)   39 |
|  | Semicolon Key. |
| #define | [INPUT\_KEY\_SLASH](group__input__events.md#gab17a459ab34d1353809c1a7360db3818)   53 |
|  | Slash Key. |
| #define | [INPUT\_KEY\_SLEEP](group__input__events.md#gaf826720ad8af092655351c0527b849df)   142 |
|  | System Sleep Key. |
| #define | [INPUT\_KEY\_SPACE](group__input__events.md#ga4d6d5af48ea84fbea0df2fcb38ac7812)   57 |
|  | Space Key. |
| #define | [INPUT\_KEY\_SYSRQ](group__input__events.md#ga41b7f92a09624c06eee3a3650ac36139)   99 |
|  | SysReq Key. |
| #define | [INPUT\_KEY\_T](group__input__events.md#gadc43d9d7846b0e87dc217dcab831e4fe)   20 |
|  | T Key. |
| #define | [INPUT\_KEY\_TAB](group__input__events.md#gac38db99311ad987f019f16e601a6911d)   15 |
|  | Tab Key. |
| #define | [INPUT\_KEY\_U](group__input__events.md#gab6403be2f0b9b60f626a57e5c9ed2666)   22 |
|  | U Key. |
| #define | [INPUT\_KEY\_UP](group__input__events.md#ga01e7f6a6aee5972612536c70a84db848)   103 |
|  | Up Key. |
| #define | [INPUT\_KEY\_UWB](group__input__events.md#ga74c693d33698eac543ee6ad4943c2d81)   239 |
|  | Ultra-Wideband Key. |
| #define | [INPUT\_KEY\_V](group__input__events.md#ga9f37deb8d631a8705cc0506d9b46b42c)   47 |
|  | V Key. |
| #define | [INPUT\_KEY\_VOLUMEDOWN](group__input__events.md#ga36b4c1340f9d7c5374e4fbe82244d492)   114 |
|  | Volume Down Key. |
| #define | [INPUT\_KEY\_VOLUMEUP](group__input__events.md#gaa876076df525fa996dbced370c1be2e3)   115 |
|  | Volume Up Key. |
| #define | [INPUT\_KEY\_W](group__input__events.md#gaafc7f5b6c9d8f7ef13527ce60c08d36d)   17 |
|  | W Key. |
| #define | [INPUT\_KEY\_WAKEUP](group__input__events.md#gaeba4b122e3850b8c96e803353ac7bd35)   143 |
|  | System Wake Up Key. |
| #define | [INPUT\_KEY\_WLAN](group__input__events.md#gae008f06aa7ca74912fe8ebbcd3dda45f)   238 |
|  | Wireless LAN Key. |
| #define | [INPUT\_KEY\_X](group__input__events.md#ga8665fe56c47f02bd98793674dbc145b9)   45 |
|  | X Key. |
| #define | [INPUT\_KEY\_Y](group__input__events.md#gae86058bcd4e4a5393b35253176dc498f)   21 |
|  | Y Key. |
| #define | [INPUT\_KEY\_Z](group__input__events.md#ga32a1603a3c0127e6ebe059af32314273)   44 |
|  | Z Key. |
| Input event BTN codes. | |
|  | |
| #define | [INPUT\_BTN\_0](group__input__events.md#ga30976f1bb4418fccbae30a56f714bea1)   0x100 |
|  | 0 button |
| #define | [INPUT\_BTN\_1](group__input__events.md#ga1f76026fc79560722aaf95aee0985705)   0x101 |
|  | 1 button |
| #define | [INPUT\_BTN\_2](group__input__events.md#ga73129f8a7a6216f629f3d3b3433c4430)   0x102 |
|  | 2 button |
| #define | [INPUT\_BTN\_3](group__input__events.md#gae8651f9708cb6def0e64094542018b6e)   0x103 |
|  | 3 button |
| #define | [INPUT\_BTN\_4](group__input__events.md#ga11b176175bd1ff1d062d2dfc111c80f3)   0x104 |
|  | 4 button |
| #define | [INPUT\_BTN\_5](group__input__events.md#ga9ea411071196ca3e90df6bbfbb48cf57)   0x105 |
|  | 5 button |
| #define | [INPUT\_BTN\_6](group__input__events.md#ga66d852c7078d65fcb2e34cee8a5fcd61)   0x106 |
|  | 6 button |
| #define | [INPUT\_BTN\_7](group__input__events.md#ga55330f8419dacc72404607f4abd2ac3e)   0x107 |
|  | 7 button |
| #define | [INPUT\_BTN\_8](group__input__events.md#gab92962cc2fd0784c1afbf0ed036a92a4)   0x108 |
|  | 8 button |
| #define | [INPUT\_BTN\_9](group__input__events.md#ga790321e6da41ee0dfe7550b03166f514)   0x109 |
|  | 9 button |
| #define | [INPUT\_BTN\_A](group__input__events.md#ga1e7a8c57c7a0a33cd3311ee141a0836c)   [INPUT\_BTN\_SOUTH](group__input__events.md#ga5bbd97c212dbd08288cbdf1dc1a64cb5) |
|  | A button. |
| #define | [INPUT\_BTN\_B](group__input__events.md#gae4355ae2a831823486b28388a78dd964)   [INPUT\_BTN\_EAST](group__input__events.md#gae57dc96a45c1a29169a6df702bb70cb7) |
|  | B button. |
| #define | [INPUT\_BTN\_BACK](group__input__events.md#ga1aae01791507acfc119387d7600e8e6a)   0x116 |
|  | Back button. |
| #define | [INPUT\_BTN\_C](group__input__events.md#ga0e20c12420205d110a4e20c3a798cd8f)   0x132 |
|  | C button. |
| #define | [INPUT\_BTN\_DPAD\_DOWN](group__input__events.md#ga912a826581f671fbc3f04b9bb2582432)   0x221 |
|  | Directional pad Down. |
| #define | [INPUT\_BTN\_DPAD\_LEFT](group__input__events.md#ga7360624be8436db1e33ecc62e4e74b14)   0x222 |
|  | Directional pad Left. |
| #define | [INPUT\_BTN\_DPAD\_RIGHT](group__input__events.md#gabcf0e865e8c374ec77ef8bd3abf23117)   0x223 |
|  | Directional pad Right. |
| #define | [INPUT\_BTN\_DPAD\_UP](group__input__events.md#ga3b2879d72a2e4a4292442cee04f6a5c6)   0x220 |
|  | Directional pad Up. |
| #define | [INPUT\_BTN\_EAST](group__input__events.md#gae57dc96a45c1a29169a6df702bb70cb7)   0x131 |
|  | East button. |
| #define | [INPUT\_BTN\_EXTRA](group__input__events.md#ga296364e72a76c9d03729b35ff64a3ea3)   0x114 |
|  | Extra button. |
| #define | [INPUT\_BTN\_FORWARD](group__input__events.md#ga1483e1ef939172b42b98be83961d3668)   0x115 |
|  | Forward button. |
| #define | [INPUT\_BTN\_GEAR\_DOWN](group__input__events.md#gac1810029daec295ab8df9c2463c3b12d)   0x150 |
|  | Gear Up button. |
| #define | [INPUT\_BTN\_GEAR\_UP](group__input__events.md#ga5f84880e2febbd344348a235cba670d1)   0x151 |
|  | Gear Down button. |
| #define | [INPUT\_BTN\_LEFT](group__input__events.md#ga391066a02e4297af7c214031037aeb3e)   0x110 |
|  | Left button. |
| #define | [INPUT\_BTN\_MIDDLE](group__input__events.md#ga86b7c6fbd3e37e21bd6b0fb379c89b44)   0x112 |
|  | Middle button. |
| #define | [INPUT\_BTN\_MODE](group__input__events.md#ga0b1db382e01c7d8f88dd531625f4b759)   0x13c |
|  | Mode button. |
| #define | [INPUT\_BTN\_NORTH](group__input__events.md#gab1378ad64c11487f0f607d039db61d82)   0x133 |
|  | North button. |
| #define | [INPUT\_BTN\_RIGHT](group__input__events.md#ga300d9d3924d22f27180272908f6ad8db)   0x111 |
|  | Right button. |
| #define | [INPUT\_BTN\_SELECT](group__input__events.md#gaad0c944797cd368eca5f6753326fe28a)   0x13a |
|  | Select button. |
| #define | [INPUT\_BTN\_SIDE](group__input__events.md#gaf34f37dd3c5ef85af7805c1a307bdcc4)   0x113 |
|  | Side button. |
| #define | [INPUT\_BTN\_SOUTH](group__input__events.md#ga5bbd97c212dbd08288cbdf1dc1a64cb5)   0x130 |
|  | South button. |
| #define | [INPUT\_BTN\_START](group__input__events.md#ga874350c63269e66869d3424d108bf891)   0x13b |
|  | Start button. |
| #define | [INPUT\_BTN\_TASK](group__input__events.md#ga14273a631fbaec99bf96c7929034cb2d)   0x117 |
|  | Task button. |
| #define | [INPUT\_BTN\_THUMBL](group__input__events.md#ga5809e3b7e5f922904b5177f551880ceb)   0x13d |
|  | Left thumbstick button. |
| #define | [INPUT\_BTN\_THUMBR](group__input__events.md#ga83061a701ecd88a543a1ff9850cfd070)   0x13e |
|  | Right thumbstick button. |
| #define | [INPUT\_BTN\_TL](group__input__events.md#ga3c5f6d03b079c2771d5b5a0dbed75cad)   0x136 |
|  | Left trigger (L1). |
| #define | [INPUT\_BTN\_TL2](group__input__events.md#ga59b1954abc7d0f4d05e025a570439155)   0x138 |
|  | Left trigger 2 (L2). |
| #define | [INPUT\_BTN\_TOUCH](group__input__events.md#ga80661f579f180f02e05fa3c1175728c4)   0x14a |
|  | Touchscreen touch. |
| #define | [INPUT\_BTN\_TR](group__input__events.md#gacc3e39f0e70af828684efe126931b5ff)   0x137 |
|  | Right trigger (R1). |
| #define | [INPUT\_BTN\_TR2](group__input__events.md#ga7401c1c0ec2b6d20ab4ca0bfa87b06bd)   0x139 |
|  | Right trigger 2 (R2). |
| #define | [INPUT\_BTN\_WEST](group__input__events.md#ga0913edaa3f7176c942c6708090719d48)   0x134 |
|  | West button. |
| #define | [INPUT\_BTN\_X](group__input__events.md#gad205e660b5cc9e148db7b0acd22c4560)   [INPUT\_BTN\_NORTH](group__input__events.md#gab1378ad64c11487f0f607d039db61d82) |
|  | X button. |
| #define | [INPUT\_BTN\_Y](group__input__events.md#ga4a11b785ae5dab8922f481217e01fd08)   [INPUT\_BTN\_WEST](group__input__events.md#ga0913edaa3f7176c942c6708090719d48) |
|  | Y button. |
| #define | [INPUT\_BTN\_Z](group__input__events.md#ga09f473104f9c92f40e2f481b1e02a28f)   0x135 |
|  | Z button. |
| Input event ABS codes. | |
|  | |
| #define | [INPUT\_ABS\_BRAKE](group__input__events.md#ga79930c9f3260ca7ae2026e85280b9808)   0x0a |
|  | Absolute brake position. |
| #define | [INPUT\_ABS\_GAS](group__input__events.md#ga77831126c364a12132db3e51af8002e3)   0x09 |
|  | Absolute gas position. |
| #define | [INPUT\_ABS\_MT\_SLOT](group__input__events.md#ga7dbd7e0140f5d13c7b92243568dba95b)   0x2f |
|  | Absolute multitouch slot identifier. |
| #define | [INPUT\_ABS\_RUDDER](group__input__events.md#ga5c9daa51741ad28757bfb4e7538bf2c7)   0x07 |
|  | Absolute rudder position. |
| #define | [INPUT\_ABS\_RX](group__input__events.md#ga2564b261dc72e0d48776bfd80282baf4)   0x03 |
|  | Absolute rotation around X axis. |
| #define | [INPUT\_ABS\_RY](group__input__events.md#ga69109075f91f270b43de41f7e558f894)   0x04 |
|  | Absolute rotation around Y axis. |
| #define | [INPUT\_ABS\_RZ](group__input__events.md#gad4f9589ef67776adc52a2cee72bb1634)   0x05 |
|  | Absolute rotation around Z axis. |
| #define | [INPUT\_ABS\_THROTTLE](group__input__events.md#ga44d3e48d42006c73e011d9ee8d5656c3)   0x06 |
|  | Absolute throttle position. |
| #define | [INPUT\_ABS\_WHEEL](group__input__events.md#ga5fde78f9e113ac35ebb4f1735a08d3e3)   0x08 |
|  | Absolute wheel position. |
| #define | [INPUT\_ABS\_X](group__input__events.md#ga6bb2cf3decdbbeac354f66db7239f8c1)   0x00 |
|  | Absolute X coordinate. |
| #define | [INPUT\_ABS\_Y](group__input__events.md#gad2f731397644733e4b3d9f8f96d4f87a)   0x01 |
|  | Absolute Y coordinate. |
| #define | [INPUT\_ABS\_Z](group__input__events.md#gae007afd99bf586fdc4c6b1a5ae1a3859)   0x02 |
|  | Absolute Z coordinate. |
| Input event REL codes. | |
|  | |
| #define | [INPUT\_REL\_DIAL](group__input__events.md#gab8aeb81a612ec63d687cbe1d9becb823)   0x07 |
|  | Relative dial coordinate. |
| #define | [INPUT\_REL\_HWHEEL](group__input__events.md#ga5b9989321b8e8f883bd338c1a37d50c2)   0x06 |
|  | Relative horizontal wheel coordinate. |
| #define | [INPUT\_REL\_MISC](group__input__events.md#gaf2a08d3d5a0aa60b8f56ff7e2110a54e)   0x09 |
|  | Relative misc coordinate. |
| #define | [INPUT\_REL\_RX](group__input__events.md#ga5727f75f795b31982dc8681a0eed3378)   0x03 |
|  | Relative rotation around X axis. |
| #define | [INPUT\_REL\_RY](group__input__events.md#ga85cde1de349dffef0c7dd5757e94cb4a)   0x04 |
|  | Relative rotation around Y axis. |
| #define | [INPUT\_REL\_RZ](group__input__events.md#ga1f1ed1ce01e943906e5cecf071c0bf96)   0x05 |
|  | Relative rotation around Z axis. |
| #define | [INPUT\_REL\_WHEEL](group__input__events.md#ga3884c7bbfb3b23e9cbc054f327b4344c)   0x08 |
|  | Relative wheel coordinate. |
| #define | [INPUT\_REL\_X](group__input__events.md#ga6afab29530dfffbb81b191b90548ffd2)   0x00 |
|  | Relative X coordinate. |
| #define | [INPUT\_REL\_Y](group__input__events.md#ga5fbdf5c33ac1e5330c3f30b37ee8f51d)   0x01 |
|  | Relative Y coordinate. |
| #define | [INPUT\_REL\_Z](group__input__events.md#gae5626b188d77b39a79df4bb7790cd316)   0x02 |
|  | Relative Z coordinate. |
| Input event MSC codes. | |
|  | |
| #define | [INPUT\_MSC\_SCAN](group__input__events.md#ga62a5a51f0beb512236dfa276211e1f43)   0x04 |
|  | Scan code. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [input](dir_ab844d62c7a22d129cc80e6c359d2c21.md)
- [input-event-codes.h](input-event-codes_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
