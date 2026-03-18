---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nxp__mpu_8h.html
original_path: doxygen/html/nxp__mpu_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_mpu.h File Reference

[Go to the source code of this file.](nxp__mpu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [nxp\_mpu\_region\_attr](structnxp__mpu__region__attr.md) |
| struct | [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) |
| struct | [nxp\_mpu\_region](structnxp__mpu__region.md) |
| struct | [nxp\_mpu\_config](structnxp__mpu__config.md) |

| Macros | |
| --- | --- |
| #define | [NXP\_MPU\_REGION\_NUMBER](#a21a1ac0d36f7afb791f73b4266c29f70)   12 |
| #define | [UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9)   4 |
| #define | [UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd)   2 |
| #define | [UM\_EXEC](#ab5140794b05a3c2331d97ba4a3c4ed26)   1 |
| #define | [BM0\_UM\_SHIFT](#a827ffa4bfa173421765be3af7d732b7d)   0 |
| #define | [BM1\_UM\_SHIFT](#ab241d9fcbae38cab7dae9f38c5ec69f6)   6 |
| #define | [BM2\_UM\_SHIFT](#a43b74013e6cc3fd0263efd3dfb2083fc)   12 |
| #define | [BM3\_UM\_SHIFT](#a398f479f1d9a9085d75b1b5cdf62968b)   18 |
| #define | [SM\_RWX\_ALLOW](#aeec3e5dfce7d167654f6073a0dac731e)   0 |
| #define | [SM\_RX\_ALLOW](#a15ac6f38d430aa401c2df437a095e8af)   1 |
| #define | [SM\_RW\_ALLOW](#ac834b1a3618a4a361a766de8d8d9b729)   2 |
| #define | [SM\_SAME\_AS\_UM](#a9c450188b4f476319609a5eff9981013)   3 |
| #define | [BM0\_SM\_SHIFT](#a9a682bd5d2dfd42b17a251e7d75df108)   3 |
| #define | [BM1\_SM\_SHIFT](#ab37c2c0b12942cb036dab45b213446fd)   9 |
| #define | [BM2\_SM\_SHIFT](#a1a07f20ecd6d1b553477a4d1b689e215)   15 |
| #define | [BM3\_SM\_SHIFT](#ac4701e5b2dabd074952b8a146f2752bb)   21 |
| #define | [BM4\_WE\_SHIFT](#a1bf58e90c0e0c756d46a312e49d257ac)   24 |
| #define | [BM4\_RE\_SHIFT](#a1eb38fe0712d071cb776310123402946)   25 |
| #define | [BM4\_PERMISSIONS](#a5714f056c45e223a683a59a7fc6997a7)   0 |
| #define | [MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) |
| #define | [MPU\_REGION\_WRITE](#a0c9f505077068c3466e0c5a147a77874) |
| #define | [MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52) |
| #define | [MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019) |
| #define | [MPU\_REGION\_SU\_RX](#a95d67eb3ec1451fdb29f8d813719a349) |
| #define | [MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810) |
| #define | [MPU\_REGION\_SU\_RWX](#ab385c5e2584e7397e1664233d0e1a88b) |
| #define | [ENDADDR\_ROUND](#a754d89dc3b794e45d432b48a6f65919e)(x) |
| #define | [REGION\_USER\_MODE\_ATTR](#a83037f3495bf5755e88d39bbf4a259aa) |
| #define | [REGION\_RAM\_ATTR](#a859d811feecb32c788b16a413e1b4781) |
| #define | [REGION\_FLASH\_ATTR](#aef333777108782979d84344af4bc51d6) |
| #define | [REGION\_IO\_ATTR](#a4ce0d123898b8cb22cb161c8d69c411f) |
| #define | [REGION\_RO\_ATTR](#af0fd70c24b3a61a7587a486c8035f305)   {([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))} |
| #define | [REGION\_USER\_RO\_ATTR](#aa0fe2dcd3799fe21fa51d87f7ce0e28f) |
| #define | [REGION\_DEBUGGER\_AND\_DEVICE\_ATTR](#adf8f684a3f851ee1915f7d11cb44fc77) |
| #define | [REGION\_DEBUG\_ATTR](#a92c302d8df1ca631080e48e30e5ce14d)   {[MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019)} |
| #define | [REGION\_BACKGROUND\_ATTR](#a96b453ef40506d7d33e28cd48bcc6de3)   {[MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810)} |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA](#a73bc6803ccf24aad395089a4395bd22f) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#a9b7cc3c51f518517031d76807470aa10) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RO](#a6636a59c913e035646a1a9e5ed61559d) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#a3c52d13e42a66beb72d088ac56388951) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#a708338371e91b5a3f2d44f9ae48849db) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#a706eaa9c515f1cc859d97ef8455b2f2f) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RWX](#a29db5fb48087c0cae596ff212989ed24) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RX](#a81878d7a3177ef4c37ea3046da004c9a) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#a78f9b21aa8b5c894db28328f5a1e2641) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](#a7879968909ce2f0e33763ae1e2fc9d84)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](#ab6fb9b9c6c1c968a11ae80bfd70fec26)(attr) |
| #define | [MPU\_REGION\_ENTRY](#aa8d5b264821eea9086eadc256c1af90f)(\_name, \_base, \_end, \_attr) |

| Typedefs | |
| --- | --- |
| typedef struct [nxp\_mpu\_region\_attr](structnxp__mpu__region__attr.md) | [nxp\_mpu\_region\_attr\_t](#ab9cc02d4320ccbc4385061ce7b92ced0) |

| Variables | |
| --- | --- |
| const struct [nxp\_mpu\_config](structnxp__mpu__config.md) | [mpu\_config](#a07ea21656f7fd3c46d30eab43d5b2721) |

## Macro Definition Documentation

## [◆ ](#a9a682bd5d2dfd42b17a251e7d75df108)BM0\_SM\_SHIFT

| #define BM0\_SM\_SHIFT   3 |
| --- |

## [◆ ](#a827ffa4bfa173421765be3af7d732b7d)BM0\_UM\_SHIFT

| #define BM0\_UM\_SHIFT   0 |
| --- |

## [◆ ](#ab37c2c0b12942cb036dab45b213446fd)BM1\_SM\_SHIFT

| #define BM1\_SM\_SHIFT   9 |
| --- |

## [◆ ](#ab241d9fcbae38cab7dae9f38c5ec69f6)BM1\_UM\_SHIFT

| #define BM1\_UM\_SHIFT   6 |
| --- |

## [◆ ](#a1a07f20ecd6d1b553477a4d1b689e215)BM2\_SM\_SHIFT

| #define BM2\_SM\_SHIFT   15 |
| --- |

## [◆ ](#a43b74013e6cc3fd0263efd3dfb2083fc)BM2\_UM\_SHIFT

| #define BM2\_UM\_SHIFT   12 |
| --- |

## [◆ ](#ac4701e5b2dabd074952b8a146f2752bb)BM3\_SM\_SHIFT

| #define BM3\_SM\_SHIFT   21 |
| --- |

## [◆ ](#a398f479f1d9a9085d75b1b5cdf62968b)BM3\_UM\_SHIFT

| #define BM3\_UM\_SHIFT   18 |
| --- |

## [◆ ](#a5714f056c45e223a683a59a7fc6997a7)BM4\_PERMISSIONS

| #define BM4\_PERMISSIONS   0 |
| --- |

## [◆ ](#a1eb38fe0712d071cb776310123402946)BM4\_RE\_SHIFT

| #define BM4\_RE\_SHIFT   25 |
| --- |

## [◆ ](#a1bf58e90c0e0c756d46a312e49d257ac)BM4\_WE\_SHIFT

| #define BM4\_WE\_SHIFT   24 |
| --- |

## [◆ ](#a754d89dc3b794e45d432b48a6f65919e)ENDADDR\_ROUND

| #define ENDADDR\_ROUND | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(x - 0x1F)

## [◆ ](#ab6fb9b9c6c1c968a11ae80bfd70fec26)K\_MEM\_PARTITION\_IS\_EXECUTABLE

| #define K\_MEM\_PARTITION\_IS\_EXECUTABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

int \_\_is\_executable\_\_; \

switch (attr.ap\_attr) { \

case [MPU\_REGION\_SU\_RX](#a95d67eb3ec1451fdb29f8d813719a349): \

case [MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52): \

\_\_is\_executable\_\_ = 1; \

break; \

default: \

\_\_is\_executable\_\_ = 0; \

} \

\_\_is\_executable\_\_; \

})

[MPU\_REGION\_SU\_RX](#a95d67eb3ec1451fdb29f8d813719a349)

#define MPU\_REGION\_SU\_RX

**Definition** nxp\_mpu.h:67

[MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52)

#define MPU\_REGION\_EXEC

**Definition** nxp\_mpu.h:56

## [◆ ](#a7879968909ce2f0e33763ae1e2fc9d84)K\_MEM\_PARTITION\_IS\_WRITABLE

| #define K\_MEM\_PARTITION\_IS\_WRITABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

int \_\_is\_writable\_\_; \

switch (attr.ap\_attr) { \

case [MPU\_REGION\_WRITE](#a0c9f505077068c3466e0c5a147a77874): \

case [MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810): \

\_\_is\_writable\_\_ = 1; \

break; \

default: \

\_\_is\_writable\_\_ = 0; \

} \

\_\_is\_writable\_\_; \

})

[MPU\_REGION\_WRITE](#a0c9f505077068c3466e0c5a147a77874)

#define MPU\_REGION\_WRITE

**Definition** nxp\_mpu.h:50

[MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810)

#define MPU\_REGION\_SU\_RW

**Definition** nxp\_mpu.h:72

## [◆ ](#a73bc6803ccf24aad395089a4395bd22f)K\_MEM\_PARTITION\_P\_NA\_U\_NA

| #define K\_MEM\_PARTITION\_P\_NA\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))})

[MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019)

#define MPU\_REGION\_SU

**Definition** nxp\_mpu.h:62

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

## [◆ ](#a706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_SU\_RX](#a95d67eb3ec1451fdb29f8d813719a349))})

## [◆ ](#a708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))})

[MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e)

#define MPU\_REGION\_READ

**Definition** nxp\_mpu.h:44

## [◆ ](#a3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810))})

## [◆ ](#a6636a59c913e035646a1a9e5ed61559d)K\_MEM\_PARTITION\_P\_RW\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810))})

## [◆ ](#a9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_WRITE](#a0c9f505077068c3466e0c5a147a77874) | [MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))})

## [◆ ](#a29db5fb48087c0cae596ff212989ed24)K\_MEM\_PARTITION\_P\_RWX\_U\_RWX

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_WRITE](#a0c9f505077068c3466e0c5a147a77874) | \

[MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52) | [MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))})

## [◆ ](#a81878d7a3177ef4c37ea3046da004c9a)K\_MEM\_PARTITION\_P\_RWX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52) | [MPU\_REGION\_SU\_RWX](#ab385c5e2584e7397e1664233d0e1a88b))})

[MPU\_REGION\_SU\_RWX](#ab385c5e2584e7397e1664233d0e1a88b)

#define MPU\_REGION\_SU\_RWX

**Definition** nxp\_mpu.h:77

## [◆ ](#a78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52) | [MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))})

## [◆ ](#aa8d5b264821eea9086eadc256c1af90f)MPU\_REGION\_ENTRY

| #define MPU\_REGION\_ENTRY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_base*, |
|  |  |  | *\_end*, |
|  |  |  | *\_attr* ) |

**Value:**

{\

.name = \_name, \

.base = \_base, \

.end = \_end, \

.attr = \_attr, \

}

## [◆ ](#aecde7abc56ba1104be002a478cb68c52)MPU\_REGION\_EXEC

| #define MPU\_REGION\_EXEC |
| --- |

**Value:**

(([UM\_EXEC](#ab5140794b05a3c2331d97ba4a3c4ed26) << [BM0\_UM\_SHIFT](#a827ffa4bfa173421765be3af7d732b7d)) | \

([UM\_EXEC](#ab5140794b05a3c2331d97ba4a3c4ed26) << [BM1\_UM\_SHIFT](#ab241d9fcbae38cab7dae9f38c5ec69f6)) | \

([UM\_EXEC](#ab5140794b05a3c2331d97ba4a3c4ed26) << [BM2\_UM\_SHIFT](#a43b74013e6cc3fd0263efd3dfb2083fc)) | \

([UM\_EXEC](#ab5140794b05a3c2331d97ba4a3c4ed26) << [BM3\_UM\_SHIFT](#a398f479f1d9a9085d75b1b5cdf62968b)))

[BM3\_UM\_SHIFT](#a398f479f1d9a9085d75b1b5cdf62968b)

#define BM3\_UM\_SHIFT

**Definition** nxp\_mpu.h:21

[BM2\_UM\_SHIFT](#a43b74013e6cc3fd0263efd3dfb2083fc)

#define BM2\_UM\_SHIFT

**Definition** nxp\_mpu.h:20

[BM0\_UM\_SHIFT](#a827ffa4bfa173421765be3af7d732b7d)

#define BM0\_UM\_SHIFT

**Definition** nxp\_mpu.h:18

[BM1\_UM\_SHIFT](#ab241d9fcbae38cab7dae9f38c5ec69f6)

#define BM1\_UM\_SHIFT

**Definition** nxp\_mpu.h:19

[UM\_EXEC](#ab5140794b05a3c2331d97ba4a3c4ed26)

#define UM\_EXEC

**Definition** nxp\_mpu.h:16

## [◆ ](#aaf9c10295c149cc7f843d52a9993bc6e)MPU\_REGION\_READ

| #define MPU\_REGION\_READ |
| --- |

**Value:**

(([UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9) << [BM0\_UM\_SHIFT](#a827ffa4bfa173421765be3af7d732b7d)) | \

([UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9) << [BM1\_UM\_SHIFT](#ab241d9fcbae38cab7dae9f38c5ec69f6)) | \

([UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9) << [BM2\_UM\_SHIFT](#a43b74013e6cc3fd0263efd3dfb2083fc)) | \

([UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9) << [BM3\_UM\_SHIFT](#a398f479f1d9a9085d75b1b5cdf62968b)))

[UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9)

#define UM\_READ

**Definition** nxp\_mpu.h:14

## [◆ ](#a9efc4e45f22f3dab38d72bd45ff98019)MPU\_REGION\_SU

| #define MPU\_REGION\_SU |
| --- |

**Value:**

(([SM\_SAME\_AS\_UM](#a9c450188b4f476319609a5eff9981013) << [BM0\_SM\_SHIFT](#a9a682bd5d2dfd42b17a251e7d75df108)) | \

([SM\_SAME\_AS\_UM](#a9c450188b4f476319609a5eff9981013) << [BM1\_SM\_SHIFT](#ab37c2c0b12942cb036dab45b213446fd)) | \

([SM\_SAME\_AS\_UM](#a9c450188b4f476319609a5eff9981013) << [BM2\_SM\_SHIFT](#a1a07f20ecd6d1b553477a4d1b689e215)) | \

([SM\_SAME\_AS\_UM](#a9c450188b4f476319609a5eff9981013) << [BM3\_SM\_SHIFT](#ac4701e5b2dabd074952b8a146f2752bb)))

[BM2\_SM\_SHIFT](#a1a07f20ecd6d1b553477a4d1b689e215)

#define BM2\_SM\_SHIFT

**Definition** nxp\_mpu.h:31

[BM0\_SM\_SHIFT](#a9a682bd5d2dfd42b17a251e7d75df108)

#define BM0\_SM\_SHIFT

**Definition** nxp\_mpu.h:29

[SM\_SAME\_AS\_UM](#a9c450188b4f476319609a5eff9981013)

#define SM\_SAME\_AS\_UM

**Definition** nxp\_mpu.h:27

[BM1\_SM\_SHIFT](#ab37c2c0b12942cb036dab45b213446fd)

#define BM1\_SM\_SHIFT

**Definition** nxp\_mpu.h:30

[BM3\_SM\_SHIFT](#ac4701e5b2dabd074952b8a146f2752bb)

#define BM3\_SM\_SHIFT

**Definition** nxp\_mpu.h:32

## [◆ ](#afe53263c929f7b16590ce575b813a810)MPU\_REGION\_SU\_RW

| #define MPU\_REGION\_SU\_RW |
| --- |

**Value:**

(([SM\_RW\_ALLOW](#ac834b1a3618a4a361a766de8d8d9b729) << [BM0\_SM\_SHIFT](#a9a682bd5d2dfd42b17a251e7d75df108)) | \

([SM\_RW\_ALLOW](#ac834b1a3618a4a361a766de8d8d9b729) << [BM1\_SM\_SHIFT](#ab37c2c0b12942cb036dab45b213446fd)) | \

([SM\_RW\_ALLOW](#ac834b1a3618a4a361a766de8d8d9b729) << [BM2\_SM\_SHIFT](#a1a07f20ecd6d1b553477a4d1b689e215)) | \

([SM\_RW\_ALLOW](#ac834b1a3618a4a361a766de8d8d9b729) << [BM3\_SM\_SHIFT](#ac4701e5b2dabd074952b8a146f2752bb)))

[SM\_RW\_ALLOW](#ac834b1a3618a4a361a766de8d8d9b729)

#define SM\_RW\_ALLOW

**Definition** nxp\_mpu.h:26

## [◆ ](#ab385c5e2584e7397e1664233d0e1a88b)MPU\_REGION\_SU\_RWX

| #define MPU\_REGION\_SU\_RWX |
| --- |

**Value:**

(([SM\_RWX\_ALLOW](#aeec3e5dfce7d167654f6073a0dac731e) << [BM0\_SM\_SHIFT](#a9a682bd5d2dfd42b17a251e7d75df108)) | \

([SM\_RWX\_ALLOW](#aeec3e5dfce7d167654f6073a0dac731e) << [BM1\_SM\_SHIFT](#ab37c2c0b12942cb036dab45b213446fd)) | \

([SM\_RWX\_ALLOW](#aeec3e5dfce7d167654f6073a0dac731e) << [BM2\_SM\_SHIFT](#a1a07f20ecd6d1b553477a4d1b689e215)) | \

([SM\_RWX\_ALLOW](#aeec3e5dfce7d167654f6073a0dac731e) << [BM3\_SM\_SHIFT](#ac4701e5b2dabd074952b8a146f2752bb)))

[SM\_RWX\_ALLOW](#aeec3e5dfce7d167654f6073a0dac731e)

#define SM\_RWX\_ALLOW

**Definition** nxp\_mpu.h:24

## [◆ ](#a95d67eb3ec1451fdb29f8d813719a349)MPU\_REGION\_SU\_RX

| #define MPU\_REGION\_SU\_RX |
| --- |

**Value:**

(([SM\_RX\_ALLOW](#a15ac6f38d430aa401c2df437a095e8af) << [BM0\_SM\_SHIFT](#a9a682bd5d2dfd42b17a251e7d75df108)) | \

([SM\_RX\_ALLOW](#a15ac6f38d430aa401c2df437a095e8af) << [BM1\_SM\_SHIFT](#ab37c2c0b12942cb036dab45b213446fd)) | \

([SM\_RX\_ALLOW](#a15ac6f38d430aa401c2df437a095e8af) << [BM2\_SM\_SHIFT](#a1a07f20ecd6d1b553477a4d1b689e215)) | \

([SM\_RX\_ALLOW](#a15ac6f38d430aa401c2df437a095e8af) << [BM3\_SM\_SHIFT](#ac4701e5b2dabd074952b8a146f2752bb)))

[SM\_RX\_ALLOW](#a15ac6f38d430aa401c2df437a095e8af)

#define SM\_RX\_ALLOW

**Definition** nxp\_mpu.h:25

## [◆ ](#a0c9f505077068c3466e0c5a147a77874)MPU\_REGION\_WRITE

| #define MPU\_REGION\_WRITE |
| --- |

**Value:**

(([UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd) << [BM0\_UM\_SHIFT](#a827ffa4bfa173421765be3af7d732b7d)) | \

([UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd) << [BM1\_UM\_SHIFT](#ab241d9fcbae38cab7dae9f38c5ec69f6)) | \

([UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd) << [BM2\_UM\_SHIFT](#a43b74013e6cc3fd0263efd3dfb2083fc)) | \

([UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd) << [BM3\_UM\_SHIFT](#a398f479f1d9a9085d75b1b5cdf62968b)))

[UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd)

#define UM\_WRITE

**Definition** nxp\_mpu.h:15

## [◆ ](#a21a1ac0d36f7afb791f73b4266c29f70)NXP\_MPU\_REGION\_NUMBER

| #define NXP\_MPU\_REGION\_NUMBER   12 |
| --- |

## [◆ ](#a96b453ef40506d7d33e28cd48bcc6de3)REGION\_BACKGROUND\_ATTR

| #define REGION\_BACKGROUND\_ATTR   {[MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810)} |
| --- |

## [◆ ](#a92c302d8df1ca631080e48e30e5ce14d)REGION\_DEBUG\_ATTR

| #define REGION\_DEBUG\_ATTR   {[MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019)} |
| --- |

## [◆ ](#adf8f684a3f851ee1915f7d11cb44fc77)REGION\_DEBUGGER\_AND\_DEVICE\_ATTR

| #define REGION\_DEBUGGER\_AND\_DEVICE\_ATTR |
| --- |

**Value:**

{(([MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019)) | \

(([UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9) | [UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd)) << [BM3\_UM\_SHIFT](#a398f479f1d9a9085d75b1b5cdf62968b)) | \

([BM4\_PERMISSIONS](#a5714f056c45e223a683a59a7fc6997a7)))}

[BM4\_PERMISSIONS](#a5714f056c45e223a683a59a7fc6997a7)

#define BM4\_PERMISSIONS

**Definition** nxp\_mpu.h:40

## [◆ ](#aef333777108782979d84344af4bc51d6)REGION\_FLASH\_ATTR

| #define REGION\_FLASH\_ATTR |
| --- |

**Value:**

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | \

[MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52) | \

[MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))}

## [◆ ](#a4ce0d123898b8cb22cb161c8d69c411f)REGION\_IO\_ATTR

| #define REGION\_IO\_ATTR |
| --- |

**Value:**

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | \

[MPU\_REGION\_WRITE](#a0c9f505077068c3466e0c5a147a77874) | \

[MPU\_REGION\_EXEC](#aecde7abc56ba1104be002a478cb68c52) | \

[MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))}

## [◆ ](#a859d811feecb32c788b16a413e1b4781)REGION\_RAM\_ATTR

| #define REGION\_RAM\_ATTR |
| --- |

**Value:**

{(([MPU\_REGION\_SU\_RW](#afe53263c929f7b16590ce575b813a810)) | \

(([UM\_READ](#a7b4052cfa2a098b33448fd381ce154a9) | [UM\_WRITE](#aef84434979e31bb7c9b90ddaa17b4ffd)) << [BM3\_UM\_SHIFT](#a398f479f1d9a9085d75b1b5cdf62968b)) | \

([BM4\_PERMISSIONS](#a5714f056c45e223a683a59a7fc6997a7)))}

## [◆ ](#af0fd70c24b3a61a7587a486c8035f305)REGION\_RO\_ATTR

| #define REGION\_RO\_ATTR   {([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | [MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))} |
| --- |

## [◆ ](#a83037f3495bf5755e88d39bbf4a259aa)REGION\_USER\_MODE\_ATTR

| #define REGION\_USER\_MODE\_ATTR |
| --- |

**Value:**

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | \

[MPU\_REGION\_WRITE](#a0c9f505077068c3466e0c5a147a77874) | \

[MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))}

## [◆ ](#aa0fe2dcd3799fe21fa51d87f7ce0e28f)REGION\_USER\_RO\_ATTR

| #define REGION\_USER\_RO\_ATTR |
| --- |

**Value:**

{([MPU\_REGION\_READ](#aaf9c10295c149cc7f843d52a9993bc6e) | \

[MPU\_REGION\_SU](#a9efc4e45f22f3dab38d72bd45ff98019))}

## [◆ ](#ac834b1a3618a4a361a766de8d8d9b729)SM\_RW\_ALLOW

| #define SM\_RW\_ALLOW   2 |
| --- |

## [◆ ](#aeec3e5dfce7d167654f6073a0dac731e)SM\_RWX\_ALLOW

| #define SM\_RWX\_ALLOW   0 |
| --- |

## [◆ ](#a15ac6f38d430aa401c2df437a095e8af)SM\_RX\_ALLOW

| #define SM\_RX\_ALLOW   1 |
| --- |

## [◆ ](#a9c450188b4f476319609a5eff9981013)SM\_SAME\_AS\_UM

| #define SM\_SAME\_AS\_UM   3 |
| --- |

## [◆ ](#ab5140794b05a3c2331d97ba4a3c4ed26)UM\_EXEC

| #define UM\_EXEC   1 |
| --- |

## [◆ ](#a7b4052cfa2a098b33448fd381ce154a9)UM\_READ

| #define UM\_READ   4 |
| --- |

## [◆ ](#aef84434979e31bb7c9b90ddaa17b4ffd)UM\_WRITE

| #define UM\_WRITE   2 |
| --- |

## Typedef Documentation

## [◆ ](#ab9cc02d4320ccbc4385061ce7b92ced0)nxp\_mpu\_region\_attr\_t

| typedef struct [nxp\_mpu\_region\_attr](structnxp__mpu__region__attr.md) [nxp\_mpu\_region\_attr\_t](#ab9cc02d4320ccbc4385061ce7b92ced0) |
| --- |

## Variable Documentation

## [◆ ](#a07ea21656f7fd3c46d30eab43d5b2721)mpu\_config

| | const struct [nxp\_mpu\_config](structnxp__mpu__config.md) mpu\_config | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [nxp\_mpu.h](nxp__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
