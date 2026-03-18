---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__input__events.html
original_path: doxygen/html/group__input__events.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Input Event Definitions

[Device Driver APIs](group__io__interfaces.md) » [Input Interface](group__input__interface.md)

| Input event types. | |
| --- | --- |
|  | |
| #define | [INPUT\_EV\_KEY](#ga4a517c31bdbdd1bd82ba456d256ef1f1)   0x01 |
|  | Key event. |
| #define | [INPUT\_EV\_REL](#ga02de6c85efab3d21eb81e88e54d58e03)   0x02 |
|  | Relative coordinate event. |
| #define | [INPUT\_EV\_ABS](#gaa6bcd6755fbdb3eb103f03a72759ce4f)   0x03 |
|  | Absolute coordinate event. |
| #define | [INPUT\_EV\_MSC](#ga40ab1faa2e28e32c30016ad854afa6cf)   0x04 |
|  | Miscellaneous event. |
| #define | [INPUT\_EV\_VENDOR\_START](#ga7037a9ea2e0a63c40a5d206e507e5f42)   0xf0 |
|  | Vendor specific event start. |
| #define | [INPUT\_EV\_VENDOR\_STOP](#gaa19a341e18ff5c43e1b8ddf58c7b9676)   0xff |
|  | Vendor specific event stop. |

| Input event KEY codes. | |
| --- | --- |
|  | |
| #define | [INPUT\_KEY\_RESERVED](#ga94e5a0d74dad76e57679b97af90ecb65)   0 |
|  | Reserved, do not use. |
| #define | [INPUT\_KEY\_0](#gab41cb2f1768b0a0667ab6509b6d3af21)   11 |
|  | 0 Key |
| #define | [INPUT\_KEY\_1](#gad62520853a15b74d68c1bab5a3119eaa)   2 |
|  | 1 Key |
| #define | [INPUT\_KEY\_2](#gadb02e289d07d4d4457c88b1ada7e2534)   3 |
|  | 2 Key |
| #define | [INPUT\_KEY\_3](#ga95a246cefcaafd26d15c1c124bdf2ca4)   4 |
|  | 3 Key |
| #define | [INPUT\_KEY\_4](#ga0c16c2e62a65eab0fe8952a4cf60254d)   5 |
|  | 4 Key |
| #define | [INPUT\_KEY\_5](#ga386e2c69d5e5a9549668b1a2a2d297e1)   6 |
|  | 5 Key |
| #define | [INPUT\_KEY\_6](#ga87e0cea90040710253718ce29c407f3e)   7 |
|  | 6 Key |
| #define | [INPUT\_KEY\_7](#ga090686eaaacddb8c2f58b31b4b9801b8)   8 |
|  | 7 Key |
| #define | [INPUT\_KEY\_8](#ga6f2b66c0eea17b044778a326ffcd3f57)   9 |
|  | 8 Key |
| #define | [INPUT\_KEY\_9](#ga91473de481c47f3f9e40caf42e49250f)   10 |
|  | 9 Key |
| #define | [INPUT\_KEY\_A](#ga553b457efaafb3cdc41e7b1e953cd6fe)   30 |
|  | A Key. |
| #define | [INPUT\_KEY\_APOSTROPHE](#gaa528a10eb85fa9dc46198e08962fab3a)   40 |
|  | Apostrophe Key. |
| #define | [INPUT\_KEY\_B](#gaaae2c60e8907c14c094e5c1c4e3dae3b)   48 |
|  | B Key. |
| #define | [INPUT\_KEY\_BACK](#gab5ad87c6e97f6b09f9dc1a1570a9c299)   158 |
|  | Back Key. |
| #define | [INPUT\_KEY\_BACKSLASH](#ga180fcae595fbc580bfe1a94414a4b02b)   43 |
|  | Backslash Key. |
| #define | [INPUT\_KEY\_BACKSPACE](#ga654ffbdc8f2fef696ee0237704cebc34)   14 |
|  | Backspace Key. |
| #define | [INPUT\_KEY\_BLUETOOTH](#ga26f6330d7631bdae0f2bb34f623a85ae)   237 |
|  | Bluetooth Key. |
| #define | [INPUT\_KEY\_BRIGHTNESSDOWN](#gac4afc3e97b18a1f22e3d59730177e27f)   224 |
|  | Brightness Up Key. |
| #define | [INPUT\_KEY\_BRIGHTNESSUP](#gaff59e776a3e3a0fe4d32caeb41a32c53)   225 |
|  | Brightneess Down Key. |
| #define | [INPUT\_KEY\_C](#ga1b88afc2eacfbbd778785398baebd287)   46 |
|  | C Key. |
| #define | [INPUT\_KEY\_CAPSLOCK](#ga8dfa14142766962272afc77538f8a909)   58 |
|  | Caps Lock Key. |
| #define | [INPUT\_KEY\_COFFEE](#ga345dc788101108c27f488cfa0fc885c8)   152 |
|  | Screen Saver Key. |
| #define | [INPUT\_KEY\_COMMA](#ga1220a9e90676992fcd3c308a7f1038f7)   51 |
|  | Comma Key. |
| #define | [INPUT\_KEY\_COMPOSE](#ga52882fff91dc0c288cf0b60baa60be65)   127 |
|  | Compose Key. |
| #define | [INPUT\_KEY\_CONNECT](#gaedf1f55d35163e56ca03f4409ea6b7d0)   218 |
|  | Connect Key. |
| #define | [INPUT\_KEY\_D](#ga206eda236c1ce08e3ad6eef192ac303e)   32 |
|  | D Key. |
| #define | [INPUT\_KEY\_DELETE](#ga2abef21124d504927c675959331a4c3b)   111 |
|  | Delete Key. |
| #define | [INPUT\_KEY\_DOT](#gacbd30145c479c472d105a0c5251c0e4d)   52 |
|  | Dot Key. |
| #define | [INPUT\_KEY\_DOWN](#gad80b82e35e50f775a091b8f5031d2c9b)   108 |
|  | Down Key. |
| #define | [INPUT\_KEY\_E](#ga4c1a1f169d8159ed36b194ae3d0aa0e7)   18 |
|  | E Key. |
| #define | [INPUT\_KEY\_END](#gaff91435e45612b50955523d029dfd1e4)   107 |
|  | End Key. |
| #define | [INPUT\_KEY\_ENTER](#ga8e4e6c4072fd5595a80a4e4ff1ae1c32)   28 |
|  | Enter Key. |
| #define | [INPUT\_KEY\_EQUAL](#ga0775ec23155f396f368425fb4dc35e54)   13 |
|  | Equal Key. |
| #define | [INPUT\_KEY\_ESC](#ga2026ab8608c7013781cdcf1e546e4d93)   1 |
|  | Escape Key. |
| #define | [INPUT\_KEY\_F](#gaed15f4e46a5e80bd9d8508f2f0317386)   33 |
|  | F Key. |
| #define | [INPUT\_KEY\_F1](#ga06374b0c4c42d708874d799afac87f54)   59 |
|  | F1 Key. |
| #define | [INPUT\_KEY\_F10](#ga925bd568cbef2c8241a8bc38cd1fc0ee)   68 |
|  | F10 Key. |
| #define | [INPUT\_KEY\_F11](#gaf8db5439ca4244843ddea6c78e235227)   87 |
|  | F11 Key. |
| #define | [INPUT\_KEY\_F12](#gac206e26c278998da99fc7907f2d68d90)   88 |
|  | F12 Key. |
| #define | [INPUT\_KEY\_F13](#gafe37c9d54407b3401974a400831d9200)   183 |
|  | F13 Key. |
| #define | [INPUT\_KEY\_F14](#ga57112c273fb46a4f748047953355e430)   184 |
|  | F14 Key. |
| #define | [INPUT\_KEY\_F15](#ga379756870b1a1d808f97f60cf2d3ecc5)   185 |
|  | F15 Key. |
| #define | [INPUT\_KEY\_F16](#ga0336cf1cdcaa5ee62c1a4a7d7b5f94b0)   186 |
|  | F16 Key. |
| #define | [INPUT\_KEY\_F17](#ga15ae8eaffd7978c3d91fe05bfedaec0d)   187 |
|  | F17 Key. |
| #define | [INPUT\_KEY\_F18](#gaf58e8117aadc979c00e99e5d2944e572)   188 |
|  | F18 Key. |
| #define | [INPUT\_KEY\_F19](#ga45127f8182970453761bea5703e164ca)   189 |
|  | F19 Key. |
| #define | [INPUT\_KEY\_F2](#gae7ea4afc3ee03cba0820e1230a1bc844)   60 |
|  | F2 Key. |
| #define | [INPUT\_KEY\_F20](#gaa0d8d5c8f17f26a6571bd50acd7e7c56)   190 |
|  | F20 Key. |
| #define | [INPUT\_KEY\_F21](#ga958fc836aa61bd04731563b97b3f2c3b)   191 |
|  | F21 Key. |
| #define | [INPUT\_KEY\_F22](#ga9f865f6f67f7ad3e747450cbe7bd001b)   192 |
|  | F22 Key. |
| #define | [INPUT\_KEY\_F23](#ga201402a9046f510fcc818fc281acdd74)   193 |
|  | F23 Key. |
| #define | [INPUT\_KEY\_F24](#gade48ffdee4f9fc816467f61444e388d4)   194 |
|  | F24 Key. |
| #define | [INPUT\_KEY\_F3](#gaa186203f9efabb0868348938e5eabcfd)   61 |
|  | F3 Key. |
| #define | [INPUT\_KEY\_F4](#gace5db941d06022b3b33dd9e72a799b68)   62 |
|  | F4 Key. |
| #define | [INPUT\_KEY\_F5](#ga5ab64f326303e6b097eac8f9a1827feb)   63 |
|  | F5 Key. |
| #define | [INPUT\_KEY\_F6](#ga3f8d3788cd179ffb9d68de85e23ee1b0)   64 |
|  | F6 Key. |
| #define | [INPUT\_KEY\_F7](#ga647c9e3d15d4866c3ae486b09f6182fa)   65 |
|  | F7 Key. |
| #define | [INPUT\_KEY\_F8](#ga6a1be4c1720c9bbd18950ba7d9b91042)   66 |
|  | F8 Key. |
| #define | [INPUT\_KEY\_F9](#ga16baac9275d3b860e117705aba632681)   67 |
|  | F9 Key. |
| #define | [INPUT\_KEY\_FASTFORWARD](#ga6c9a01c0a070b213af72cb8088e75876)   208 |
|  | Fast Forward Key. |
| #define | [INPUT\_KEY\_FORWARD](#gad64d70c2ccc65f5189666efa0847ca7a)   159 |
|  | Forward Key. |
| #define | [INPUT\_KEY\_G](#ga5480ba49acaa553a194984a98b92f552)   34 |
|  | G Key. |
| #define | [INPUT\_KEY\_GRAVE](#ga1aaa62276091bde62d4e5aa872902559)   41 |
|  | Grave (backtick) Key. |
| #define | [INPUT\_KEY\_H](#ga3014cf5abad3b71a0ae45b5b7c713f38)   35 |
|  | H Key. |
| #define | [INPUT\_KEY\_HOME](#gaa8314d1e4f4ca225922f039791b36d42)   102 |
|  | Home Key. |
| #define | [INPUT\_KEY\_I](#ga6c987aa5736663b7f309f2b2fb9423c5)   23 |
|  | I Key. |
| #define | [INPUT\_KEY\_INSERT](#gabfa379fe24dd23461e435de41c23864d)   110 |
|  | Insert Key. |
| #define | [INPUT\_KEY\_J](#ga7d5c3e334909eb4b2c76217b69a61260)   36 |
|  | J Key. |
| #define | [INPUT\_KEY\_K](#ga8cb73e35923639e77e861631565134df)   37 |
|  | K Key. |
| #define | [INPUT\_KEY\_KP0](#ga8e5438fce6c7a717da4322de2982a2ed)   82 |
|  | Keypad 0 Key. |
| #define | [INPUT\_KEY\_KP1](#gaa5b65c8ff4b94208ff434f3ed8c9f1f1)   79 |
|  | Keypad 1 Key. |
| #define | [INPUT\_KEY\_KP2](#gad50d9044613b97c6d6292afe15cceb06)   80 |
|  | Keypad 2 Key. |
| #define | [INPUT\_KEY\_KP3](#ga8a084e91c2906b1f8dd43939293d4812)   81 |
|  | Keypad 3 Key. |
| #define | [INPUT\_KEY\_KP4](#ga1a9ca528816497bf32bee4e524d2977c)   75 |
|  | Keypad 4 Key. |
| #define | [INPUT\_KEY\_KP5](#ga83e04456cf68db301973d09af1a19641)   76 |
|  | Keypad 5 Key. |
| #define | [INPUT\_KEY\_KP6](#gabd7a6dc0d9440de1ffef2a3643583966)   77 |
|  | Keypad 6 Key. |
| #define | [INPUT\_KEY\_KP7](#ga58709627a1190549d0e0004e4b5bcd74)   71 |
|  | Keypad 7 Key. |
| #define | [INPUT\_KEY\_KP8](#ga94e64bbd09dda7434d8a9f086daca1a7)   72 |
|  | Keypad 8 Key. |
| #define | [INPUT\_KEY\_KP9](#ga7dda283e4603e0ce4d14a9a87ea74c4f)   73 |
|  | Keypad 9 Key. |
| #define | [INPUT\_KEY\_KPASTERISK](#gaa0c33b6ba975617f93230aa75a49fef5)   55 |
|  | Keypad Asterisk Key. |
| #define | [INPUT\_KEY\_KPCOMMA](#gabb3767d06adbe20b3fb580e8816f916f)   121 |
|  | Keypad Comma Key. |
| #define | [INPUT\_KEY\_KPDOT](#gac6c07467b6202089166c56c498fd4b27)   83 |
|  | Keypad Dot Key. |
| #define | [INPUT\_KEY\_KPENTER](#gae8fd841f81d29788d5d0b602538bbd0e)   96 |
|  | Keypad Enter Key. |
| #define | [INPUT\_KEY\_KPEQUAL](#gaefdae376c1daf752b698efaf89a07b18)   117 |
|  | Keypad Equal Key. |
| #define | [INPUT\_KEY\_KPMINUS](#gad4f23f54ec4f2252864c507e09ad9cea)   74 |
|  | Keypad Minus Key. |
| #define | [INPUT\_KEY\_KPPLUS](#ga3d6307d0237d8f34a3d448dc9e40528f)   78 |
|  | Keypad Plus Key. |
| #define | [INPUT\_KEY\_KPPLUSMINUS](#ga21a77384e45feb96ecc322032dc7231e)   118 |
|  | Keypad Plus Key. |
| #define | [INPUT\_KEY\_KPSLASH](#gab3f0ce8548cef85df2672d09d021fe39)   98 |
|  | Keypad Slash Key. |
| #define | [INPUT\_KEY\_L](#gad79329b4b6c3eaad43aabac8c3538622)   38 |
|  | L Key. |
| #define | [INPUT\_KEY\_LEFT](#gae8c0a4811cd2056d0b6885239d635492)   105 |
|  | Left Key. |
| #define | [INPUT\_KEY\_LEFTALT](#ga8d384257be19e2eb0d807d35f2656f16)   56 |
|  | Left Alt Key. |
| #define | [INPUT\_KEY\_LEFTBRACE](#gaecdffb7aff0fee1e078319a23a97e10e)   26 |
|  | Left Brace Key. |
| #define | [INPUT\_KEY\_LEFTCTRL](#ga1bc52bc876c50da66cc292f250603db7)   29 |
|  | Left Ctrl Key. |
| #define | [INPUT\_KEY\_LEFTMETA](#gad18b505a7f718887f932a5b7fedfecd3)   125 |
|  | Left Meta Key. |
| #define | [INPUT\_KEY\_LEFTSHIFT](#gacaf73383130558303396a7add94bdafd)   42 |
|  | Left Shift Key. |
| #define | [INPUT\_KEY\_M](#ga7c8f628eb719d1d4b428805914c376a7)   50 |
|  | M Key. |
| #define | [INPUT\_KEY\_MENU](#gab159cae18818e930e4d928ebcc206651)   139 |
|  | Menu Key. |
| #define | [INPUT\_KEY\_MINUS](#gae9779c5f21b9e14e5cbe1db8c5073819)   12 |
|  | Minus Key. |
| #define | [INPUT\_KEY\_MUTE](#ga8554adab31fc9c20c9de01bcb2aff839)   113 |
|  | Mute Key. |
| #define | [INPUT\_KEY\_N](#ga09c0c860ee76803bb317dbac1072cd1d)   49 |
|  | N Key. |
| #define | [INPUT\_KEY\_NUMLOCK](#ga93e220e43b3d33ffa985445f6dbf9c3c)   69 |
|  | Num Lock Key. |
| #define | [INPUT\_KEY\_O](#gae964cb377e0bcd958dad6da9626d298c)   24 |
|  | O Key. |
| #define | [INPUT\_KEY\_P](#ga396def37642dee65c74c48ff72aaa53d)   25 |
|  | P Key. |
| #define | [INPUT\_KEY\_PAGEDOWN](#gaf6bc999ac2a136235fe95803c6df73c1)   109 |
|  | Page Down Key. |
| #define | [INPUT\_KEY\_PAGEUP](#gaebb169acd4c3ce873353fd595364b374)   104 |
|  | Page UpKey. |
| #define | [INPUT\_KEY\_PAUSE](#ga08319efd258cd774ff8bc964c5a402dd)   119 |
|  | Pause Key. |
| #define | [INPUT\_KEY\_PLAY](#ga1a377fdb1967aeff84e96d47c71bcf41)   207 |
|  | Play Key. |
| #define | [INPUT\_KEY\_POWER](#ga2b05b5429ef1b0dc37698b82201d257d)   116 |
|  | Power Key. |
| #define | [INPUT\_KEY\_PRINT](#ga4927612cf9f69324b15d8d9e46ab3326)   210 |
|  | Print Key. |
| #define | [INPUT\_KEY\_Q](#ga9ee8d6012d74e489ee8072f71497a36e)   16 |
|  | Q Key. |
| #define | [INPUT\_KEY\_R](#ga421f14c501d86ed907ed4249f93a9e7e)   19 |
|  | R Key. |
| #define | [INPUT\_KEY\_RIGHT](#ga1bf6f292c1ab3ca25001b4ef4ca2626b)   106 |
|  | Right Key. |
| #define | [INPUT\_KEY\_RIGHTALT](#gac02b6a2133d5ddf8847e1ce94250536f)   100 |
|  | Right Alt Key. |
| #define | [INPUT\_KEY\_RIGHTBRACE](#gaa0802d3471f6c774d37a8827e632d7fb)   27 |
|  | Right Brace Key. |
| #define | [INPUT\_KEY\_RIGHTCTRL](#gabb2e15ee9c30a649c92e82c42f513a35)   97 |
|  | Right Ctrl Key. |
| #define | [INPUT\_KEY\_RIGHTMETA](#ga23ebc28da84872b585c9dcfeb057bfc9)   126 |
|  | Right Meta Key. |
| #define | [INPUT\_KEY\_RIGHTSHIFT](#ga4fce26a4ffc693507043c1cfe95d279d)   54 |
|  | Right Shift Key. |
| #define | [INPUT\_KEY\_S](#gadefb5566a41148a0df4dd95cb2c5e2d2)   31 |
|  | S Key. |
| #define | [INPUT\_KEY\_SCALE](#ga32491acdefb2e9f0eab5e7fc5755d2bc)   120 |
|  | Scale Key. |
| #define | [INPUT\_KEY\_SCROLLLOCK](#ga1d0958d93ddb7f3ff662e84a06c95a7c)   70 |
|  | Scroll Lock Key. |
| #define | [INPUT\_KEY\_SEMICOLON](#ga7d45c7e2399dc6b20b6e470cb35d1dd6)   39 |
|  | Semicolon Key. |
| #define | [INPUT\_KEY\_SLASH](#gab17a459ab34d1353809c1a7360db3818)   53 |
|  | Slash Key. |
| #define | [INPUT\_KEY\_SLEEP](#gaf826720ad8af092655351c0527b849df)   142 |
|  | System Sleep Key. |
| #define | [INPUT\_KEY\_SPACE](#ga4d6d5af48ea84fbea0df2fcb38ac7812)   57 |
|  | Space Key. |
| #define | [INPUT\_KEY\_SYSRQ](#ga41b7f92a09624c06eee3a3650ac36139)   99 |
|  | SysReq Key. |
| #define | [INPUT\_KEY\_T](#gadc43d9d7846b0e87dc217dcab831e4fe)   20 |
|  | T Key. |
| #define | [INPUT\_KEY\_TAB](#gac38db99311ad987f019f16e601a6911d)   15 |
|  | Tab Key. |
| #define | [INPUT\_KEY\_U](#gab6403be2f0b9b60f626a57e5c9ed2666)   22 |
|  | U Key. |
| #define | [INPUT\_KEY\_UP](#ga01e7f6a6aee5972612536c70a84db848)   103 |
|  | Up Key. |
| #define | [INPUT\_KEY\_UWB](#ga74c693d33698eac543ee6ad4943c2d81)   239 |
|  | Ultra-Wideband Key. |
| #define | [INPUT\_KEY\_V](#ga9f37deb8d631a8705cc0506d9b46b42c)   47 |
|  | V Key. |
| #define | [INPUT\_KEY\_VOLUMEDOWN](#ga36b4c1340f9d7c5374e4fbe82244d492)   114 |
|  | Volume Down Key. |
| #define | [INPUT\_KEY\_VOLUMEUP](#gaa876076df525fa996dbced370c1be2e3)   115 |
|  | Volume Up Key. |
| #define | [INPUT\_KEY\_W](#gaafc7f5b6c9d8f7ef13527ce60c08d36d)   17 |
|  | W Key. |
| #define | [INPUT\_KEY\_WAKEUP](#gaeba4b122e3850b8c96e803353ac7bd35)   143 |
|  | System Wake Up Key. |
| #define | [INPUT\_KEY\_WLAN](#gae008f06aa7ca74912fe8ebbcd3dda45f)   238 |
|  | Wireless LAN Key. |
| #define | [INPUT\_KEY\_X](#ga8665fe56c47f02bd98793674dbc145b9)   45 |
|  | X Key. |
| #define | [INPUT\_KEY\_Y](#gae86058bcd4e4a5393b35253176dc498f)   21 |
|  | Y Key. |
| #define | [INPUT\_KEY\_Z](#ga32a1603a3c0127e6ebe059af32314273)   44 |
|  | Z Key. |

| Input event BTN codes. | |
| --- | --- |
|  | |
| #define | [INPUT\_BTN\_0](#ga30976f1bb4418fccbae30a56f714bea1)   0x100 |
|  | 0 button |
| #define | [INPUT\_BTN\_1](#ga1f76026fc79560722aaf95aee0985705)   0x101 |
|  | 1 button |
| #define | [INPUT\_BTN\_2](#ga73129f8a7a6216f629f3d3b3433c4430)   0x102 |
|  | 2 button |
| #define | [INPUT\_BTN\_3](#gae8651f9708cb6def0e64094542018b6e)   0x103 |
|  | 3 button |
| #define | [INPUT\_BTN\_4](#ga11b176175bd1ff1d062d2dfc111c80f3)   0x104 |
|  | 4 button |
| #define | [INPUT\_BTN\_5](#ga9ea411071196ca3e90df6bbfbb48cf57)   0x105 |
|  | 5 button |
| #define | [INPUT\_BTN\_6](#ga66d852c7078d65fcb2e34cee8a5fcd61)   0x106 |
|  | 6 button |
| #define | [INPUT\_BTN\_7](#ga55330f8419dacc72404607f4abd2ac3e)   0x107 |
|  | 7 button |
| #define | [INPUT\_BTN\_8](#gab92962cc2fd0784c1afbf0ed036a92a4)   0x108 |
|  | 8 button |
| #define | [INPUT\_BTN\_9](#ga790321e6da41ee0dfe7550b03166f514)   0x109 |
|  | 9 button |
| #define | [INPUT\_BTN\_A](#ga1e7a8c57c7a0a33cd3311ee141a0836c)   BTN\_SOUTH |
|  | A button. |
| #define | [INPUT\_BTN\_B](#gae4355ae2a831823486b28388a78dd964)   BTN\_EAST |
|  | B button. |
| #define | [INPUT\_BTN\_C](#ga0e20c12420205d110a4e20c3a798cd8f)   0x132 |
|  | C button. |
| #define | [INPUT\_BTN\_DPAD\_DOWN](#ga912a826581f671fbc3f04b9bb2582432)   0x221 |
|  | Directional pad Down. |
| #define | [INPUT\_BTN\_DPAD\_LEFT](#ga7360624be8436db1e33ecc62e4e74b14)   0x222 |
|  | Directional pad Left. |
| #define | [INPUT\_BTN\_DPAD\_RIGHT](#gabcf0e865e8c374ec77ef8bd3abf23117)   0x223 |
|  | Directional pad Right. |
| #define | [INPUT\_BTN\_DPAD\_UP](#ga3b2879d72a2e4a4292442cee04f6a5c6)   0x220 |
|  | Directional pad Up. |
| #define | [INPUT\_BTN\_EAST](#gae57dc96a45c1a29169a6df702bb70cb7)   0x131 |
|  | East button. |
| #define | [INPUT\_BTN\_GEAR\_DOWN](#gac1810029daec295ab8df9c2463c3b12d)   0x150 |
|  | Gear Up button. |
| #define | [INPUT\_BTN\_GEAR\_UP](#ga5f84880e2febbd344348a235cba670d1)   0x151 |
|  | Gear Down button. |
| #define | [INPUT\_BTN\_LEFT](#ga391066a02e4297af7c214031037aeb3e)   0x110 |
|  | Left button. |
| #define | [INPUT\_BTN\_MIDDLE](#ga86b7c6fbd3e37e21bd6b0fb379c89b44)   0x112 |
|  | Middle button. |
| #define | [INPUT\_BTN\_MODE](#ga0b1db382e01c7d8f88dd531625f4b759)   0x13c |
|  | Mode button. |
| #define | [INPUT\_BTN\_NORTH](#gab1378ad64c11487f0f607d039db61d82)   0x133 |
|  | North button. |
| #define | [INPUT\_BTN\_RIGHT](#ga300d9d3924d22f27180272908f6ad8db)   0x111 |
|  | Right button. |
| #define | [INPUT\_BTN\_SELECT](#gaad0c944797cd368eca5f6753326fe28a)   0x13a |
|  | Select button. |
| #define | [INPUT\_BTN\_SOUTH](#ga5bbd97c212dbd08288cbdf1dc1a64cb5)   0x130 |
|  | South button. |
| #define | [INPUT\_BTN\_START](#ga874350c63269e66869d3424d108bf891)   0x13b |
|  | Start button. |
| #define | [INPUT\_BTN\_THUMBL](#ga5809e3b7e5f922904b5177f551880ceb)   0x13d |
|  | Left thumbstick button. |
| #define | [INPUT\_BTN\_THUMBR](#ga83061a701ecd88a543a1ff9850cfd070)   0x13e |
|  | Right thumbstick button. |
| #define | [INPUT\_BTN\_TL](#ga3c5f6d03b079c2771d5b5a0dbed75cad)   0x136 |
|  | Left trigger (L1). |
| #define | [INPUT\_BTN\_TL2](#ga59b1954abc7d0f4d05e025a570439155)   0x138 |
|  | Left trigger 2 (L2). |
| #define | [INPUT\_BTN\_TOUCH](#ga80661f579f180f02e05fa3c1175728c4)   0x14a |
|  | Touchscreen touch. |
| #define | [INPUT\_BTN\_TR](#gacc3e39f0e70af828684efe126931b5ff)   0x137 |
|  | Right trigger (R1). |
| #define | [INPUT\_BTN\_TR2](#ga7401c1c0ec2b6d20ab4ca0bfa87b06bd)   0x139 |
|  | Right trigger 2 (R2). |
| #define | [INPUT\_BTN\_WEST](#ga0913edaa3f7176c942c6708090719d48)   0x134 |
|  | West button. |
| #define | [INPUT\_BTN\_X](#gad205e660b5cc9e148db7b0acd22c4560)   BTN\_NORTH |
|  | X button. |
| #define | [INPUT\_BTN\_Y](#ga4a11b785ae5dab8922f481217e01fd08)   BTN\_WEST |
|  | Y button. |
| #define | [INPUT\_BTN\_Z](#ga09f473104f9c92f40e2f481b1e02a28f)   0x135 |
|  | Z button. |

| Input event ABS codes. | |
| --- | --- |
|  | |
| #define | [INPUT\_ABS\_BRAKE](#ga79930c9f3260ca7ae2026e85280b9808)   0x0a |
|  | Absolute brake position. |
| #define | [INPUT\_ABS\_GAS](#ga77831126c364a12132db3e51af8002e3)   0x09 |
|  | Absolute gas position. |
| #define | [INPUT\_ABS\_RUDDER](#ga5c9daa51741ad28757bfb4e7538bf2c7)   0x07 |
|  | Absolute rudder position. |
| #define | [INPUT\_ABS\_RX](#ga2564b261dc72e0d48776bfd80282baf4)   0x03 |
|  | Absolute rotation around X axis. |
| #define | [INPUT\_ABS\_RY](#ga69109075f91f270b43de41f7e558f894)   0x04 |
|  | Absolute rotation around Y axis. |
| #define | [INPUT\_ABS\_RZ](#gad4f9589ef67776adc52a2cee72bb1634)   0x05 |
|  | Absolute rotation around Z axis. |
| #define | [INPUT\_ABS\_THROTTLE](#ga44d3e48d42006c73e011d9ee8d5656c3)   0x06 |
|  | Absolute throttle position. |
| #define | [INPUT\_ABS\_WHEEL](#ga5fde78f9e113ac35ebb4f1735a08d3e3)   0x08 |
|  | Absolute wheel position. |
| #define | [INPUT\_ABS\_X](#ga6bb2cf3decdbbeac354f66db7239f8c1)   0x00 |
|  | Absolute X coordinate. |
| #define | [INPUT\_ABS\_Y](#gad2f731397644733e4b3d9f8f96d4f87a)   0x01 |
|  | Absolute Y coordinate. |
| #define | [INPUT\_ABS\_Z](#gae007afd99bf586fdc4c6b1a5ae1a3859)   0x02 |
|  | Absolute Z coordinate. |

| Input event REL codes. | |
| --- | --- |
|  | |
| #define | [INPUT\_REL\_DIAL](#gab8aeb81a612ec63d687cbe1d9becb823)   0x07 |
|  | Relative dial coordinate. |
| #define | [INPUT\_REL\_HWHEEL](#ga5b9989321b8e8f883bd338c1a37d50c2)   0x06 |
|  | Relative horizontal wheel coordinate. |
| #define | [INPUT\_REL\_MISC](#gaf2a08d3d5a0aa60b8f56ff7e2110a54e)   0x09 |
|  | Relative misc coordinate. |
| #define | [INPUT\_REL\_RX](#ga5727f75f795b31982dc8681a0eed3378)   0x03 |
|  | Relative rotation around X axis. |
| #define | [INPUT\_REL\_RY](#ga85cde1de349dffef0c7dd5757e94cb4a)   0x04 |
|  | Relative rotation around Y axis. |
| #define | [INPUT\_REL\_RZ](#ga1f1ed1ce01e943906e5cecf071c0bf96)   0x05 |
|  | Relative rotation around Z axis. |
| #define | [INPUT\_REL\_WHEEL](#ga3884c7bbfb3b23e9cbc054f327b4344c)   0x08 |
|  | Relative wheel coordinate. |
| #define | [INPUT\_REL\_X](#ga6afab29530dfffbb81b191b90548ffd2)   0x00 |
|  | Relative X coordinate. |
| #define | [INPUT\_REL\_Y](#ga5fbdf5c33ac1e5330c3f30b37ee8f51d)   0x01 |
|  | Relative Y coordinate. |
| #define | [INPUT\_REL\_Z](#gae5626b188d77b39a79df4bb7790cd316)   0x02 |
|  | Relative Z coordinate. |

| Input event MSC codes. | |
| --- | --- |
|  | |
| #define | [INPUT\_MSC\_SCAN](#ga62a5a51f0beb512236dfa276211e1f43)   0x04 |
|  | Scan code. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga79930c9f3260ca7ae2026e85280b9808)INPUT\_ABS\_BRAKE

| #define INPUT\_ABS\_BRAKE   0x0a |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute brake position.

## [◆ ](#ga77831126c364a12132db3e51af8002e3)INPUT\_ABS\_GAS

| #define INPUT\_ABS\_GAS   0x09 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute gas position.

## [◆ ](#ga5c9daa51741ad28757bfb4e7538bf2c7)INPUT\_ABS\_RUDDER

| #define INPUT\_ABS\_RUDDER   0x07 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute rudder position.

## [◆ ](#ga2564b261dc72e0d48776bfd80282baf4)INPUT\_ABS\_RX

| #define INPUT\_ABS\_RX   0x03 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute rotation around X axis.

## [◆ ](#ga69109075f91f270b43de41f7e558f894)INPUT\_ABS\_RY

| #define INPUT\_ABS\_RY   0x04 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute rotation around Y axis.

## [◆ ](#gad4f9589ef67776adc52a2cee72bb1634)INPUT\_ABS\_RZ

| #define INPUT\_ABS\_RZ   0x05 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute rotation around Z axis.

## [◆ ](#ga44d3e48d42006c73e011d9ee8d5656c3)INPUT\_ABS\_THROTTLE

| #define INPUT\_ABS\_THROTTLE   0x06 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute throttle position.

## [◆ ](#ga5fde78f9e113ac35ebb4f1735a08d3e3)INPUT\_ABS\_WHEEL

| #define INPUT\_ABS\_WHEEL   0x08 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute wheel position.

## [◆ ](#ga6bb2cf3decdbbeac354f66db7239f8c1)INPUT\_ABS\_X

| #define INPUT\_ABS\_X   0x00 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute X coordinate.

## [◆ ](#gad2f731397644733e4b3d9f8f96d4f87a)INPUT\_ABS\_Y

| #define INPUT\_ABS\_Y   0x01 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute Y coordinate.

## [◆ ](#gae007afd99bf586fdc4c6b1a5ae1a3859)INPUT\_ABS\_Z

| #define INPUT\_ABS\_Z   0x02 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute Z coordinate.

## [◆ ](#ga30976f1bb4418fccbae30a56f714bea1)INPUT\_BTN\_0

| #define INPUT\_BTN\_0   0x100 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

0 button

## [◆ ](#ga1f76026fc79560722aaf95aee0985705)INPUT\_BTN\_1

| #define INPUT\_BTN\_1   0x101 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

1 button

## [◆ ](#ga73129f8a7a6216f629f3d3b3433c4430)INPUT\_BTN\_2

| #define INPUT\_BTN\_2   0x102 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

2 button

## [◆ ](#gae8651f9708cb6def0e64094542018b6e)INPUT\_BTN\_3

| #define INPUT\_BTN\_3   0x103 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

3 button

## [◆ ](#ga11b176175bd1ff1d062d2dfc111c80f3)INPUT\_BTN\_4

| #define INPUT\_BTN\_4   0x104 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

4 button

## [◆ ](#ga9ea411071196ca3e90df6bbfbb48cf57)INPUT\_BTN\_5

| #define INPUT\_BTN\_5   0x105 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

5 button

## [◆ ](#ga66d852c7078d65fcb2e34cee8a5fcd61)INPUT\_BTN\_6

| #define INPUT\_BTN\_6   0x106 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

6 button

## [◆ ](#ga55330f8419dacc72404607f4abd2ac3e)INPUT\_BTN\_7

| #define INPUT\_BTN\_7   0x107 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

7 button

## [◆ ](#gab92962cc2fd0784c1afbf0ed036a92a4)INPUT\_BTN\_8

| #define INPUT\_BTN\_8   0x108 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

8 button

## [◆ ](#ga790321e6da41ee0dfe7550b03166f514)INPUT\_BTN\_9

| #define INPUT\_BTN\_9   0x109 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

9 button

## [◆ ](#ga1e7a8c57c7a0a33cd3311ee141a0836c)INPUT\_BTN\_A

| #define INPUT\_BTN\_A   BTN\_SOUTH |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

A button.

## [◆ ](#gae4355ae2a831823486b28388a78dd964)INPUT\_BTN\_B

| #define INPUT\_BTN\_B   BTN\_EAST |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

B button.

## [◆ ](#ga0e20c12420205d110a4e20c3a798cd8f)INPUT\_BTN\_C

| #define INPUT\_BTN\_C   0x132 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

C button.

## [◆ ](#ga912a826581f671fbc3f04b9bb2582432)INPUT\_BTN\_DPAD\_DOWN

| #define INPUT\_BTN\_DPAD\_DOWN   0x221 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Directional pad Down.

## [◆ ](#ga7360624be8436db1e33ecc62e4e74b14)INPUT\_BTN\_DPAD\_LEFT

| #define INPUT\_BTN\_DPAD\_LEFT   0x222 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Directional pad Left.

## [◆ ](#gabcf0e865e8c374ec77ef8bd3abf23117)INPUT\_BTN\_DPAD\_RIGHT

| #define INPUT\_BTN\_DPAD\_RIGHT   0x223 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Directional pad Right.

## [◆ ](#ga3b2879d72a2e4a4292442cee04f6a5c6)INPUT\_BTN\_DPAD\_UP

| #define INPUT\_BTN\_DPAD\_UP   0x220 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Directional pad Up.

## [◆ ](#gae57dc96a45c1a29169a6df702bb70cb7)INPUT\_BTN\_EAST

| #define INPUT\_BTN\_EAST   0x131 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

East button.

## [◆ ](#gac1810029daec295ab8df9c2463c3b12d)INPUT\_BTN\_GEAR\_DOWN

| #define INPUT\_BTN\_GEAR\_DOWN   0x150 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Gear Up button.

## [◆ ](#ga5f84880e2febbd344348a235cba670d1)INPUT\_BTN\_GEAR\_UP

| #define INPUT\_BTN\_GEAR\_UP   0x151 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Gear Down button.

## [◆ ](#ga391066a02e4297af7c214031037aeb3e)INPUT\_BTN\_LEFT

| #define INPUT\_BTN\_LEFT   0x110 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left button.

## [◆ ](#ga86b7c6fbd3e37e21bd6b0fb379c89b44)INPUT\_BTN\_MIDDLE

| #define INPUT\_BTN\_MIDDLE   0x112 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Middle button.

## [◆ ](#ga0b1db382e01c7d8f88dd531625f4b759)INPUT\_BTN\_MODE

| #define INPUT\_BTN\_MODE   0x13c |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Mode button.

## [◆ ](#gab1378ad64c11487f0f607d039db61d82)INPUT\_BTN\_NORTH

| #define INPUT\_BTN\_NORTH   0x133 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

North button.

## [◆ ](#ga300d9d3924d22f27180272908f6ad8db)INPUT\_BTN\_RIGHT

| #define INPUT\_BTN\_RIGHT   0x111 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right button.

## [◆ ](#gaad0c944797cd368eca5f6753326fe28a)INPUT\_BTN\_SELECT

| #define INPUT\_BTN\_SELECT   0x13a |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Select button.

## [◆ ](#ga5bbd97c212dbd08288cbdf1dc1a64cb5)INPUT\_BTN\_SOUTH

| #define INPUT\_BTN\_SOUTH   0x130 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

South button.

## [◆ ](#ga874350c63269e66869d3424d108bf891)INPUT\_BTN\_START

| #define INPUT\_BTN\_START   0x13b |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Start button.

## [◆ ](#ga5809e3b7e5f922904b5177f551880ceb)INPUT\_BTN\_THUMBL

| #define INPUT\_BTN\_THUMBL   0x13d |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left thumbstick button.

## [◆ ](#ga83061a701ecd88a543a1ff9850cfd070)INPUT\_BTN\_THUMBR

| #define INPUT\_BTN\_THUMBR   0x13e |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right thumbstick button.

## [◆ ](#ga3c5f6d03b079c2771d5b5a0dbed75cad)INPUT\_BTN\_TL

| #define INPUT\_BTN\_TL   0x136 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left trigger (L1).

## [◆ ](#ga59b1954abc7d0f4d05e025a570439155)INPUT\_BTN\_TL2

| #define INPUT\_BTN\_TL2   0x138 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left trigger 2 (L2).

## [◆ ](#ga80661f579f180f02e05fa3c1175728c4)INPUT\_BTN\_TOUCH

| #define INPUT\_BTN\_TOUCH   0x14a |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Touchscreen touch.

## [◆ ](#gacc3e39f0e70af828684efe126931b5ff)INPUT\_BTN\_TR

| #define INPUT\_BTN\_TR   0x137 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right trigger (R1).

## [◆ ](#ga7401c1c0ec2b6d20ab4ca0bfa87b06bd)INPUT\_BTN\_TR2

| #define INPUT\_BTN\_TR2   0x139 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right trigger 2 (R2).

## [◆ ](#ga0913edaa3f7176c942c6708090719d48)INPUT\_BTN\_WEST

| #define INPUT\_BTN\_WEST   0x134 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

West button.

## [◆ ](#gad205e660b5cc9e148db7b0acd22c4560)INPUT\_BTN\_X

| #define INPUT\_BTN\_X   BTN\_NORTH |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

X button.

## [◆ ](#ga4a11b785ae5dab8922f481217e01fd08)INPUT\_BTN\_Y

| #define INPUT\_BTN\_Y   BTN\_WEST |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Y button.

## [◆ ](#ga09f473104f9c92f40e2f481b1e02a28f)INPUT\_BTN\_Z

| #define INPUT\_BTN\_Z   0x135 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Z button.

## [◆ ](#gaa6bcd6755fbdb3eb103f03a72759ce4f)INPUT\_EV\_ABS

| #define INPUT\_EV\_ABS   0x03 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Absolute coordinate event.

## [◆ ](#ga4a517c31bdbdd1bd82ba456d256ef1f1)INPUT\_EV\_KEY

| #define INPUT\_EV\_KEY   0x01 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Key event.

## [◆ ](#ga40ab1faa2e28e32c30016ad854afa6cf)INPUT\_EV\_MSC

| #define INPUT\_EV\_MSC   0x04 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Miscellaneous event.

## [◆ ](#ga02de6c85efab3d21eb81e88e54d58e03)INPUT\_EV\_REL

| #define INPUT\_EV\_REL   0x02 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative coordinate event.

## [◆ ](#ga7037a9ea2e0a63c40a5d206e507e5f42)INPUT\_EV\_VENDOR\_START

| #define INPUT\_EV\_VENDOR\_START   0xf0 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Vendor specific event start.

## [◆ ](#gaa19a341e18ff5c43e1b8ddf58c7b9676)INPUT\_EV\_VENDOR\_STOP

| #define INPUT\_EV\_VENDOR\_STOP   0xff |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Vendor specific event stop.

## [◆ ](#gab41cb2f1768b0a0667ab6509b6d3af21)INPUT\_KEY\_0

| #define INPUT\_KEY\_0   11 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

0 Key

## [◆ ](#gad62520853a15b74d68c1bab5a3119eaa)INPUT\_KEY\_1

| #define INPUT\_KEY\_1   2 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

1 Key

## [◆ ](#gadb02e289d07d4d4457c88b1ada7e2534)INPUT\_KEY\_2

| #define INPUT\_KEY\_2   3 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

2 Key

## [◆ ](#ga95a246cefcaafd26d15c1c124bdf2ca4)INPUT\_KEY\_3

| #define INPUT\_KEY\_3   4 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

3 Key

## [◆ ](#ga0c16c2e62a65eab0fe8952a4cf60254d)INPUT\_KEY\_4

| #define INPUT\_KEY\_4   5 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

4 Key

## [◆ ](#ga386e2c69d5e5a9549668b1a2a2d297e1)INPUT\_KEY\_5

| #define INPUT\_KEY\_5   6 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

5 Key

## [◆ ](#ga87e0cea90040710253718ce29c407f3e)INPUT\_KEY\_6

| #define INPUT\_KEY\_6   7 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

6 Key

## [◆ ](#ga090686eaaacddb8c2f58b31b4b9801b8)INPUT\_KEY\_7

| #define INPUT\_KEY\_7   8 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

7 Key

## [◆ ](#ga6f2b66c0eea17b044778a326ffcd3f57)INPUT\_KEY\_8

| #define INPUT\_KEY\_8   9 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

8 Key

## [◆ ](#ga91473de481c47f3f9e40caf42e49250f)INPUT\_KEY\_9

| #define INPUT\_KEY\_9   10 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

9 Key

## [◆ ](#ga553b457efaafb3cdc41e7b1e953cd6fe)INPUT\_KEY\_A

| #define INPUT\_KEY\_A   30 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

A Key.

## [◆ ](#gaa528a10eb85fa9dc46198e08962fab3a)INPUT\_KEY\_APOSTROPHE

| #define INPUT\_KEY\_APOSTROPHE   40 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Apostrophe Key.

## [◆ ](#gaaae2c60e8907c14c094e5c1c4e3dae3b)INPUT\_KEY\_B

| #define INPUT\_KEY\_B   48 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

B Key.

## [◆ ](#gab5ad87c6e97f6b09f9dc1a1570a9c299)INPUT\_KEY\_BACK

| #define INPUT\_KEY\_BACK   158 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Back Key.

## [◆ ](#ga180fcae595fbc580bfe1a94414a4b02b)INPUT\_KEY\_BACKSLASH

| #define INPUT\_KEY\_BACKSLASH   43 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Backslash Key.

## [◆ ](#ga654ffbdc8f2fef696ee0237704cebc34)INPUT\_KEY\_BACKSPACE

| #define INPUT\_KEY\_BACKSPACE   14 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Backspace Key.

## [◆ ](#ga26f6330d7631bdae0f2bb34f623a85ae)INPUT\_KEY\_BLUETOOTH

| #define INPUT\_KEY\_BLUETOOTH   237 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Bluetooth Key.

## [◆ ](#gac4afc3e97b18a1f22e3d59730177e27f)INPUT\_KEY\_BRIGHTNESSDOWN

| #define INPUT\_KEY\_BRIGHTNESSDOWN   224 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Brightness Up Key.

## [◆ ](#gaff59e776a3e3a0fe4d32caeb41a32c53)INPUT\_KEY\_BRIGHTNESSUP

| #define INPUT\_KEY\_BRIGHTNESSUP   225 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Brightneess Down Key.

## [◆ ](#ga1b88afc2eacfbbd778785398baebd287)INPUT\_KEY\_C

| #define INPUT\_KEY\_C   46 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

C Key.

## [◆ ](#ga8dfa14142766962272afc77538f8a909)INPUT\_KEY\_CAPSLOCK

| #define INPUT\_KEY\_CAPSLOCK   58 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Caps Lock Key.

## [◆ ](#ga345dc788101108c27f488cfa0fc885c8)INPUT\_KEY\_COFFEE

| #define INPUT\_KEY\_COFFEE   152 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Screen Saver Key.

## [◆ ](#ga1220a9e90676992fcd3c308a7f1038f7)INPUT\_KEY\_COMMA

| #define INPUT\_KEY\_COMMA   51 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Comma Key.

## [◆ ](#ga52882fff91dc0c288cf0b60baa60be65)INPUT\_KEY\_COMPOSE

| #define INPUT\_KEY\_COMPOSE   127 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Compose Key.

## [◆ ](#gaedf1f55d35163e56ca03f4409ea6b7d0)INPUT\_KEY\_CONNECT

| #define INPUT\_KEY\_CONNECT   218 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Connect Key.

## [◆ ](#ga206eda236c1ce08e3ad6eef192ac303e)INPUT\_KEY\_D

| #define INPUT\_KEY\_D   32 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

D Key.

## [◆ ](#ga2abef21124d504927c675959331a4c3b)INPUT\_KEY\_DELETE

| #define INPUT\_KEY\_DELETE   111 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Delete Key.

## [◆ ](#gacbd30145c479c472d105a0c5251c0e4d)INPUT\_KEY\_DOT

| #define INPUT\_KEY\_DOT   52 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Dot Key.

## [◆ ](#gad80b82e35e50f775a091b8f5031d2c9b)INPUT\_KEY\_DOWN

| #define INPUT\_KEY\_DOWN   108 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Down Key.

## [◆ ](#ga4c1a1f169d8159ed36b194ae3d0aa0e7)INPUT\_KEY\_E

| #define INPUT\_KEY\_E   18 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

E Key.

## [◆ ](#gaff91435e45612b50955523d029dfd1e4)INPUT\_KEY\_END

| #define INPUT\_KEY\_END   107 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

End Key.

## [◆ ](#ga8e4e6c4072fd5595a80a4e4ff1ae1c32)INPUT\_KEY\_ENTER

| #define INPUT\_KEY\_ENTER   28 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Enter Key.

## [◆ ](#ga0775ec23155f396f368425fb4dc35e54)INPUT\_KEY\_EQUAL

| #define INPUT\_KEY\_EQUAL   13 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Equal Key.

## [◆ ](#ga2026ab8608c7013781cdcf1e546e4d93)INPUT\_KEY\_ESC

| #define INPUT\_KEY\_ESC   1 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Escape Key.

## [◆ ](#gaed15f4e46a5e80bd9d8508f2f0317386)INPUT\_KEY\_F

| #define INPUT\_KEY\_F   33 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F Key.

## [◆ ](#ga06374b0c4c42d708874d799afac87f54)INPUT\_KEY\_F1

| #define INPUT\_KEY\_F1   59 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F1 Key.

## [◆ ](#ga925bd568cbef2c8241a8bc38cd1fc0ee)INPUT\_KEY\_F10

| #define INPUT\_KEY\_F10   68 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F10 Key.

## [◆ ](#gaf8db5439ca4244843ddea6c78e235227)INPUT\_KEY\_F11

| #define INPUT\_KEY\_F11   87 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F11 Key.

## [◆ ](#gac206e26c278998da99fc7907f2d68d90)INPUT\_KEY\_F12

| #define INPUT\_KEY\_F12   88 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F12 Key.

## [◆ ](#gafe37c9d54407b3401974a400831d9200)INPUT\_KEY\_F13

| #define INPUT\_KEY\_F13   183 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F13 Key.

## [◆ ](#ga57112c273fb46a4f748047953355e430)INPUT\_KEY\_F14

| #define INPUT\_KEY\_F14   184 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F14 Key.

## [◆ ](#ga379756870b1a1d808f97f60cf2d3ecc5)INPUT\_KEY\_F15

| #define INPUT\_KEY\_F15   185 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F15 Key.

## [◆ ](#ga0336cf1cdcaa5ee62c1a4a7d7b5f94b0)INPUT\_KEY\_F16

| #define INPUT\_KEY\_F16   186 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F16 Key.

## [◆ ](#ga15ae8eaffd7978c3d91fe05bfedaec0d)INPUT\_KEY\_F17

| #define INPUT\_KEY\_F17   187 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F17 Key.

## [◆ ](#gaf58e8117aadc979c00e99e5d2944e572)INPUT\_KEY\_F18

| #define INPUT\_KEY\_F18   188 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F18 Key.

## [◆ ](#ga45127f8182970453761bea5703e164ca)INPUT\_KEY\_F19

| #define INPUT\_KEY\_F19   189 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F19 Key.

## [◆ ](#gae7ea4afc3ee03cba0820e1230a1bc844)INPUT\_KEY\_F2

| #define INPUT\_KEY\_F2   60 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F2 Key.

## [◆ ](#gaa0d8d5c8f17f26a6571bd50acd7e7c56)INPUT\_KEY\_F20

| #define INPUT\_KEY\_F20   190 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F20 Key.

## [◆ ](#ga958fc836aa61bd04731563b97b3f2c3b)INPUT\_KEY\_F21

| #define INPUT\_KEY\_F21   191 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F21 Key.

## [◆ ](#ga9f865f6f67f7ad3e747450cbe7bd001b)INPUT\_KEY\_F22

| #define INPUT\_KEY\_F22   192 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F22 Key.

## [◆ ](#ga201402a9046f510fcc818fc281acdd74)INPUT\_KEY\_F23

| #define INPUT\_KEY\_F23   193 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F23 Key.

## [◆ ](#gade48ffdee4f9fc816467f61444e388d4)INPUT\_KEY\_F24

| #define INPUT\_KEY\_F24   194 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F24 Key.

## [◆ ](#gaa186203f9efabb0868348938e5eabcfd)INPUT\_KEY\_F3

| #define INPUT\_KEY\_F3   61 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F3 Key.

## [◆ ](#gace5db941d06022b3b33dd9e72a799b68)INPUT\_KEY\_F4

| #define INPUT\_KEY\_F4   62 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F4 Key.

## [◆ ](#ga5ab64f326303e6b097eac8f9a1827feb)INPUT\_KEY\_F5

| #define INPUT\_KEY\_F5   63 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F5 Key.

## [◆ ](#ga3f8d3788cd179ffb9d68de85e23ee1b0)INPUT\_KEY\_F6

| #define INPUT\_KEY\_F6   64 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F6 Key.

## [◆ ](#ga647c9e3d15d4866c3ae486b09f6182fa)INPUT\_KEY\_F7

| #define INPUT\_KEY\_F7   65 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F7 Key.

## [◆ ](#ga6a1be4c1720c9bbd18950ba7d9b91042)INPUT\_KEY\_F8

| #define INPUT\_KEY\_F8   66 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F8 Key.

## [◆ ](#ga16baac9275d3b860e117705aba632681)INPUT\_KEY\_F9

| #define INPUT\_KEY\_F9   67 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

F9 Key.

## [◆ ](#ga6c9a01c0a070b213af72cb8088e75876)INPUT\_KEY\_FASTFORWARD

| #define INPUT\_KEY\_FASTFORWARD   208 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Fast Forward Key.

## [◆ ](#gad64d70c2ccc65f5189666efa0847ca7a)INPUT\_KEY\_FORWARD

| #define INPUT\_KEY\_FORWARD   159 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Forward Key.

## [◆ ](#ga5480ba49acaa553a194984a98b92f552)INPUT\_KEY\_G

| #define INPUT\_KEY\_G   34 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

G Key.

## [◆ ](#ga1aaa62276091bde62d4e5aa872902559)INPUT\_KEY\_GRAVE

| #define INPUT\_KEY\_GRAVE   41 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Grave (backtick) Key.

## [◆ ](#ga3014cf5abad3b71a0ae45b5b7c713f38)INPUT\_KEY\_H

| #define INPUT\_KEY\_H   35 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

H Key.

## [◆ ](#gaa8314d1e4f4ca225922f039791b36d42)INPUT\_KEY\_HOME

| #define INPUT\_KEY\_HOME   102 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Home Key.

## [◆ ](#ga6c987aa5736663b7f309f2b2fb9423c5)INPUT\_KEY\_I

| #define INPUT\_KEY\_I   23 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

I Key.

## [◆ ](#gabfa379fe24dd23461e435de41c23864d)INPUT\_KEY\_INSERT

| #define INPUT\_KEY\_INSERT   110 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Insert Key.

## [◆ ](#ga7d5c3e334909eb4b2c76217b69a61260)INPUT\_KEY\_J

| #define INPUT\_KEY\_J   36 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

J Key.

## [◆ ](#ga8cb73e35923639e77e861631565134df)INPUT\_KEY\_K

| #define INPUT\_KEY\_K   37 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

K Key.

## [◆ ](#ga8e5438fce6c7a717da4322de2982a2ed)INPUT\_KEY\_KP0

| #define INPUT\_KEY\_KP0   82 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 0 Key.

## [◆ ](#gaa5b65c8ff4b94208ff434f3ed8c9f1f1)INPUT\_KEY\_KP1

| #define INPUT\_KEY\_KP1   79 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 1 Key.

## [◆ ](#gad50d9044613b97c6d6292afe15cceb06)INPUT\_KEY\_KP2

| #define INPUT\_KEY\_KP2   80 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 2 Key.

## [◆ ](#ga8a084e91c2906b1f8dd43939293d4812)INPUT\_KEY\_KP3

| #define INPUT\_KEY\_KP3   81 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 3 Key.

## [◆ ](#ga1a9ca528816497bf32bee4e524d2977c)INPUT\_KEY\_KP4

| #define INPUT\_KEY\_KP4   75 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 4 Key.

## [◆ ](#ga83e04456cf68db301973d09af1a19641)INPUT\_KEY\_KP5

| #define INPUT\_KEY\_KP5   76 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 5 Key.

## [◆ ](#gabd7a6dc0d9440de1ffef2a3643583966)INPUT\_KEY\_KP6

| #define INPUT\_KEY\_KP6   77 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 6 Key.

## [◆ ](#ga58709627a1190549d0e0004e4b5bcd74)INPUT\_KEY\_KP7

| #define INPUT\_KEY\_KP7   71 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 7 Key.

## [◆ ](#ga94e64bbd09dda7434d8a9f086daca1a7)INPUT\_KEY\_KP8

| #define INPUT\_KEY\_KP8   72 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 8 Key.

## [◆ ](#ga7dda283e4603e0ce4d14a9a87ea74c4f)INPUT\_KEY\_KP9

| #define INPUT\_KEY\_KP9   73 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad 9 Key.

## [◆ ](#gaa0c33b6ba975617f93230aa75a49fef5)INPUT\_KEY\_KPASTERISK

| #define INPUT\_KEY\_KPASTERISK   55 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Asterisk Key.

## [◆ ](#gabb3767d06adbe20b3fb580e8816f916f)INPUT\_KEY\_KPCOMMA

| #define INPUT\_KEY\_KPCOMMA   121 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Comma Key.

## [◆ ](#gac6c07467b6202089166c56c498fd4b27)INPUT\_KEY\_KPDOT

| #define INPUT\_KEY\_KPDOT   83 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Dot Key.

## [◆ ](#gae8fd841f81d29788d5d0b602538bbd0e)INPUT\_KEY\_KPENTER

| #define INPUT\_KEY\_KPENTER   96 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Enter Key.

## [◆ ](#gaefdae376c1daf752b698efaf89a07b18)INPUT\_KEY\_KPEQUAL

| #define INPUT\_KEY\_KPEQUAL   117 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Equal Key.

## [◆ ](#gad4f23f54ec4f2252864c507e09ad9cea)INPUT\_KEY\_KPMINUS

| #define INPUT\_KEY\_KPMINUS   74 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Minus Key.

## [◆ ](#ga3d6307d0237d8f34a3d448dc9e40528f)INPUT\_KEY\_KPPLUS

| #define INPUT\_KEY\_KPPLUS   78 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Plus Key.

## [◆ ](#ga21a77384e45feb96ecc322032dc7231e)INPUT\_KEY\_KPPLUSMINUS

| #define INPUT\_KEY\_KPPLUSMINUS   118 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Plus Key.

## [◆ ](#gab3f0ce8548cef85df2672d09d021fe39)INPUT\_KEY\_KPSLASH

| #define INPUT\_KEY\_KPSLASH   98 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Keypad Slash Key.

## [◆ ](#gad79329b4b6c3eaad43aabac8c3538622)INPUT\_KEY\_L

| #define INPUT\_KEY\_L   38 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

L Key.

## [◆ ](#gae8c0a4811cd2056d0b6885239d635492)INPUT\_KEY\_LEFT

| #define INPUT\_KEY\_LEFT   105 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left Key.

## [◆ ](#ga8d384257be19e2eb0d807d35f2656f16)INPUT\_KEY\_LEFTALT

| #define INPUT\_KEY\_LEFTALT   56 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left Alt Key.

## [◆ ](#gaecdffb7aff0fee1e078319a23a97e10e)INPUT\_KEY\_LEFTBRACE

| #define INPUT\_KEY\_LEFTBRACE   26 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left Brace Key.

## [◆ ](#ga1bc52bc876c50da66cc292f250603db7)INPUT\_KEY\_LEFTCTRL

| #define INPUT\_KEY\_LEFTCTRL   29 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left Ctrl Key.

## [◆ ](#gad18b505a7f718887f932a5b7fedfecd3)INPUT\_KEY\_LEFTMETA

| #define INPUT\_KEY\_LEFTMETA   125 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left Meta Key.

## [◆ ](#gacaf73383130558303396a7add94bdafd)INPUT\_KEY\_LEFTSHIFT

| #define INPUT\_KEY\_LEFTSHIFT   42 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Left Shift Key.

## [◆ ](#ga7c8f628eb719d1d4b428805914c376a7)INPUT\_KEY\_M

| #define INPUT\_KEY\_M   50 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

M Key.

## [◆ ](#gab159cae18818e930e4d928ebcc206651)INPUT\_KEY\_MENU

| #define INPUT\_KEY\_MENU   139 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Menu Key.

## [◆ ](#gae9779c5f21b9e14e5cbe1db8c5073819)INPUT\_KEY\_MINUS

| #define INPUT\_KEY\_MINUS   12 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Minus Key.

## [◆ ](#ga8554adab31fc9c20c9de01bcb2aff839)INPUT\_KEY\_MUTE

| #define INPUT\_KEY\_MUTE   113 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Mute Key.

## [◆ ](#ga09c0c860ee76803bb317dbac1072cd1d)INPUT\_KEY\_N

| #define INPUT\_KEY\_N   49 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

N Key.

## [◆ ](#ga93e220e43b3d33ffa985445f6dbf9c3c)INPUT\_KEY\_NUMLOCK

| #define INPUT\_KEY\_NUMLOCK   69 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Num Lock Key.

## [◆ ](#gae964cb377e0bcd958dad6da9626d298c)INPUT\_KEY\_O

| #define INPUT\_KEY\_O   24 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

O Key.

## [◆ ](#ga396def37642dee65c74c48ff72aaa53d)INPUT\_KEY\_P

| #define INPUT\_KEY\_P   25 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

P Key.

## [◆ ](#gaf6bc999ac2a136235fe95803c6df73c1)INPUT\_KEY\_PAGEDOWN

| #define INPUT\_KEY\_PAGEDOWN   109 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Page Down Key.

## [◆ ](#gaebb169acd4c3ce873353fd595364b374)INPUT\_KEY\_PAGEUP

| #define INPUT\_KEY\_PAGEUP   104 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Page UpKey.

## [◆ ](#ga08319efd258cd774ff8bc964c5a402dd)INPUT\_KEY\_PAUSE

| #define INPUT\_KEY\_PAUSE   119 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Pause Key.

## [◆ ](#ga1a377fdb1967aeff84e96d47c71bcf41)INPUT\_KEY\_PLAY

| #define INPUT\_KEY\_PLAY   207 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Play Key.

## [◆ ](#ga2b05b5429ef1b0dc37698b82201d257d)INPUT\_KEY\_POWER

| #define INPUT\_KEY\_POWER   116 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Power Key.

## [◆ ](#ga4927612cf9f69324b15d8d9e46ab3326)INPUT\_KEY\_PRINT

| #define INPUT\_KEY\_PRINT   210 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Print Key.

## [◆ ](#ga9ee8d6012d74e489ee8072f71497a36e)INPUT\_KEY\_Q

| #define INPUT\_KEY\_Q   16 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Q Key.

## [◆ ](#ga421f14c501d86ed907ed4249f93a9e7e)INPUT\_KEY\_R

| #define INPUT\_KEY\_R   19 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

R Key.

## [◆ ](#ga94e5a0d74dad76e57679b97af90ecb65)INPUT\_KEY\_RESERVED

| #define INPUT\_KEY\_RESERVED   0 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Reserved, do not use.

## [◆ ](#ga1bf6f292c1ab3ca25001b4ef4ca2626b)INPUT\_KEY\_RIGHT

| #define INPUT\_KEY\_RIGHT   106 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right Key.

## [◆ ](#gac02b6a2133d5ddf8847e1ce94250536f)INPUT\_KEY\_RIGHTALT

| #define INPUT\_KEY\_RIGHTALT   100 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right Alt Key.

## [◆ ](#gaa0802d3471f6c774d37a8827e632d7fb)INPUT\_KEY\_RIGHTBRACE

| #define INPUT\_KEY\_RIGHTBRACE   27 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right Brace Key.

## [◆ ](#gabb2e15ee9c30a649c92e82c42f513a35)INPUT\_KEY\_RIGHTCTRL

| #define INPUT\_KEY\_RIGHTCTRL   97 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right Ctrl Key.

## [◆ ](#ga23ebc28da84872b585c9dcfeb057bfc9)INPUT\_KEY\_RIGHTMETA

| #define INPUT\_KEY\_RIGHTMETA   126 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right Meta Key.

## [◆ ](#ga4fce26a4ffc693507043c1cfe95d279d)INPUT\_KEY\_RIGHTSHIFT

| #define INPUT\_KEY\_RIGHTSHIFT   54 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Right Shift Key.

## [◆ ](#gadefb5566a41148a0df4dd95cb2c5e2d2)INPUT\_KEY\_S

| #define INPUT\_KEY\_S   31 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

S Key.

## [◆ ](#ga32491acdefb2e9f0eab5e7fc5755d2bc)INPUT\_KEY\_SCALE

| #define INPUT\_KEY\_SCALE   120 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Scale Key.

## [◆ ](#ga1d0958d93ddb7f3ff662e84a06c95a7c)INPUT\_KEY\_SCROLLLOCK

| #define INPUT\_KEY\_SCROLLLOCK   70 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Scroll Lock Key.

## [◆ ](#ga7d45c7e2399dc6b20b6e470cb35d1dd6)INPUT\_KEY\_SEMICOLON

| #define INPUT\_KEY\_SEMICOLON   39 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Semicolon Key.

## [◆ ](#gab17a459ab34d1353809c1a7360db3818)INPUT\_KEY\_SLASH

| #define INPUT\_KEY\_SLASH   53 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Slash Key.

## [◆ ](#gaf826720ad8af092655351c0527b849df)INPUT\_KEY\_SLEEP

| #define INPUT\_KEY\_SLEEP   142 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

System Sleep Key.

## [◆ ](#ga4d6d5af48ea84fbea0df2fcb38ac7812)INPUT\_KEY\_SPACE

| #define INPUT\_KEY\_SPACE   57 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Space Key.

## [◆ ](#ga41b7f92a09624c06eee3a3650ac36139)INPUT\_KEY\_SYSRQ

| #define INPUT\_KEY\_SYSRQ   99 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

SysReq Key.

## [◆ ](#gadc43d9d7846b0e87dc217dcab831e4fe)INPUT\_KEY\_T

| #define INPUT\_KEY\_T   20 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

T Key.

## [◆ ](#gac38db99311ad987f019f16e601a6911d)INPUT\_KEY\_TAB

| #define INPUT\_KEY\_TAB   15 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Tab Key.

## [◆ ](#gab6403be2f0b9b60f626a57e5c9ed2666)INPUT\_KEY\_U

| #define INPUT\_KEY\_U   22 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

U Key.

## [◆ ](#ga01e7f6a6aee5972612536c70a84db848)INPUT\_KEY\_UP

| #define INPUT\_KEY\_UP   103 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Up Key.

## [◆ ](#ga74c693d33698eac543ee6ad4943c2d81)INPUT\_KEY\_UWB

| #define INPUT\_KEY\_UWB   239 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Ultra-Wideband Key.

## [◆ ](#ga9f37deb8d631a8705cc0506d9b46b42c)INPUT\_KEY\_V

| #define INPUT\_KEY\_V   47 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

V Key.

## [◆ ](#ga36b4c1340f9d7c5374e4fbe82244d492)INPUT\_KEY\_VOLUMEDOWN

| #define INPUT\_KEY\_VOLUMEDOWN   114 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Volume Down Key.

## [◆ ](#gaa876076df525fa996dbced370c1be2e3)INPUT\_KEY\_VOLUMEUP

| #define INPUT\_KEY\_VOLUMEUP   115 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Volume Up Key.

## [◆ ](#gaafc7f5b6c9d8f7ef13527ce60c08d36d)INPUT\_KEY\_W

| #define INPUT\_KEY\_W   17 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

W Key.

## [◆ ](#gaeba4b122e3850b8c96e803353ac7bd35)INPUT\_KEY\_WAKEUP

| #define INPUT\_KEY\_WAKEUP   143 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

System Wake Up Key.

## [◆ ](#gae008f06aa7ca74912fe8ebbcd3dda45f)INPUT\_KEY\_WLAN

| #define INPUT\_KEY\_WLAN   238 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Wireless LAN Key.

## [◆ ](#ga8665fe56c47f02bd98793674dbc145b9)INPUT\_KEY\_X

| #define INPUT\_KEY\_X   45 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

X Key.

## [◆ ](#gae86058bcd4e4a5393b35253176dc498f)INPUT\_KEY\_Y

| #define INPUT\_KEY\_Y   21 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Y Key.

## [◆ ](#ga32a1603a3c0127e6ebe059af32314273)INPUT\_KEY\_Z

| #define INPUT\_KEY\_Z   44 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Z Key.

## [◆ ](#ga62a5a51f0beb512236dfa276211e1f43)INPUT\_MSC\_SCAN

| #define INPUT\_MSC\_SCAN   0x04 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Scan code.

## [◆ ](#gab8aeb81a612ec63d687cbe1d9becb823)INPUT\_REL\_DIAL

| #define INPUT\_REL\_DIAL   0x07 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative dial coordinate.

## [◆ ](#ga5b9989321b8e8f883bd338c1a37d50c2)INPUT\_REL\_HWHEEL

| #define INPUT\_REL\_HWHEEL   0x06 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative horizontal wheel coordinate.

## [◆ ](#gaf2a08d3d5a0aa60b8f56ff7e2110a54e)INPUT\_REL\_MISC

| #define INPUT\_REL\_MISC   0x09 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative misc coordinate.

## [◆ ](#ga5727f75f795b31982dc8681a0eed3378)INPUT\_REL\_RX

| #define INPUT\_REL\_RX   0x03 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative rotation around X axis.

## [◆ ](#ga85cde1de349dffef0c7dd5757e94cb4a)INPUT\_REL\_RY

| #define INPUT\_REL\_RY   0x04 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative rotation around Y axis.

## [◆ ](#ga1f1ed1ce01e943906e5cecf071c0bf96)INPUT\_REL\_RZ

| #define INPUT\_REL\_RZ   0x05 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative rotation around Z axis.

## [◆ ](#ga3884c7bbfb3b23e9cbc054f327b4344c)INPUT\_REL\_WHEEL

| #define INPUT\_REL\_WHEEL   0x08 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative wheel coordinate.

## [◆ ](#ga6afab29530dfffbb81b191b90548ffd2)INPUT\_REL\_X

| #define INPUT\_REL\_X   0x00 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative X coordinate.

## [◆ ](#ga5fbdf5c33ac1e5330c3f30b37ee8f51d)INPUT\_REL\_Y

| #define INPUT\_REL\_Y   0x01 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative Y coordinate.

## [◆ ](#gae5626b188d77b39a79df4bb7790cd316)INPUT\_REL\_Z

| #define INPUT\_REL\_Z   0x02 |
| --- |

`#include <[input-event-codes.h](input-event-codes_8h.md)>`

Relative Z coordinate.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
