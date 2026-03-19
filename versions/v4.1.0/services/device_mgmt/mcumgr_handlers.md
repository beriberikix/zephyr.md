---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/device_mgmt/mcumgr_handlers.html
original_path: services/device_mgmt/mcumgr_handlers.html
---

# MCUmgr handlers

## Overview

MCUmgr functions by having group handlers which identify a group of functions relating to a
specific management area, which is addressed with a 16-bit identification value,
[`mcumgr_group_t`](../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) contains the management groups available in Zephyr with their
corresponding group ID values. The group ID is included in SMP headers to identify which
group a command belongs to, there is also an 8-bit command ID which identifies the function of
that group to execute - see [SMP Protocol Specification](smp_protocol.md#mcumgr-smp-protocol-specification) for details on the SMP
protocol and header. There can only be one registered group per unique ID.

## Implementation

MCUmgr handlers can be added externally by application code or by module code, they do not have
to reside in the upstream Zephyr tree to be usable. The first step to creating a handler is to
create the folder structure for it, the typical Zephyr MCUmgr group layout is as follows:

```text
<dir>/grp/<grp_name>_mgmt/
├── CMakeLists.txt
├── Kconfig
├── include
├──── <grp_name>_mgmt.h
├──── <grp_name>_mgmt_callbacks.h
├── src
└──── <grp_name>_mgmt.c
```

Note that the header files in upstream Zephyr MCUmgr handlers reside in the
`zephyr/include/zephyr/mgmt/mcumgr/grp/<grp_name>_mgmt` directory to allow the files to be
globally included by applications.

### Initial header <grp\_name>\_mgmt.h

The purpose of the header file is to provide defines which can be used by the MCUmgr handler
itself and application code, e.g. to reference the command IDs for executing functions. An example
file would look similar to:

```c
 1/*
 2 * Copyright (c) 2023 Nordic Semiconductor ASA
 3 *
 4 * SPDX-License-Identifier: Apache-2.0
 5 */
 6#ifndef H_EXAMPLE_MGMT_
 7#define H_EXAMPLE_MGMT_
 8
 9#ifdef __cplusplus
10extern "C" {
11#endif
12
13/**
14 * Group ID for example management group.
15 */
16#define MGMT_GROUP_ID_EXAMPLE  MGMT_GROUP_ID_PERUSER
17
18/**
19 * Command IDs for example management group.
20 */
21#define EXAMPLE_MGMT_ID_TEST   0
22#define EXAMPLE_MGMT_ID_OTHER  1
23
24/**
25 * Command result codes for example management group.
26 */
27enum example_mgmt_err_code_t {
28	/** No error, this is implied if there is no ret value in the response */
29	EXAMPLE_MGMT_ERR_OK = 0,
30
31	/** Unknown error occurred. */
32	EXAMPLE_MGMT_ERR_UNKNOWN,
33
34	/** The provided value is not wanted at this time. */
35	EXAMPLE_MGMT_ERR_NOT_WANTED,
36
37	/** The provided value was rejected by a hook. */
38	EXAMPLE_MGMT_ERR_REJECTED_BY_HOOK,
39};
40
41#ifdef __cplusplus
42}
43#endif
44
45#endif
```

This provides the defines for 2 command `test` and `other` and sets up the SMP version 2 error
responses (which have unique error codes per group as opposed to the legacy SMP version 1 error
responses that return a [`mcumgr_err_t`](../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) - there should always be an OK error code with the
value 0 and an unknown error code with the value 1. The above example then adds an error code of
`not wanted` with value 2. In addition, the group ID is set to be
[`MGMT_GROUP_ID_PERUSER`](../../doxygen/html/group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726), which is the start group ID for user-defined groups, note
that group IDs need to be unique so other custom groups should use different values, a central index
header file (as upstream Zephyr has) can be used to distribute group IDs more easily.

### Initial header <grp\_name>\_mgmt\_callbacks.h

The purpose of the header file is to provide defines which can be used by the MCUmgr handler
itself and application code, e.g. to reference the command IDs for executing functions. An example
file would look similar to:

```c
 1/*
 2 * Copyright (c) 2023 Nordic Semiconductor ASA
 3 *
 4 * SPDX-License-Identifier: Apache-2.0
 5 */
 6#ifndef H_MCUMGR_EXAMPLE_MGMT_CALLBACKS_
 7#define H_MCUMGR_EXAMPLE_MGMT_CALLBACKS_
 8#include <stdint.h>
 9#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
10
11#ifdef __cplusplus
12extern "C" {
13#endif
14
15/* This is the event ID for the example group */
16#define MGMT_EVT_GRP_EXAMPLE MGMT_EVT_GRP_USER_CUSTOM_START
17
18/* MGMT event opcodes for example management group */
19enum example_mgmt_group_events {
20	/* Callback when the other command is received, data is example_mgmt_other_data */
21	MGMT_EVT_OP_EXAMPLE_OTHER = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_EXAMPLE, 0),
22
23	/* Used to enable all smp_group events */
24	MGMT_EVT_OP_EXAMPLE_MGMT_ALL  = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_EXAMPLE),
25};
26
27/* Structure provided in the #MGMT_EVT_OP_EXAMPLE_OTHER notification callback */
28struct example_mgmt_other_data {
29	/* Contains the user supplied value */
30	uint32_t user_value;
31};
32
33#ifdef __cplusplus
34}
35#endif
36
37#endif
```

This sets up a single event which application (or module) code can register for to receive a
callback when the function handler is executed, which allows the flow of the handler to be
changed (i.e. to return an error instead of continuing). The event group ID is set to
[`MGMT_EVT_GRP_USER_CUSTOM_START`](../../doxygen/html/group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d), which is the start event ID for user-defined groups,
note that event IDs need to be unique so other custom groups should use different values, a
central index header file (as upstream Zephyr has) can be used to distribute event IDs more
easily.

### Initial source <grp\_name>\_mgmt.c

The purpose of this source file is to handle the incoming MCUmgr commands, provide responses, and
register the transport with MCUmgr so that commands will be sent to it. An example file would
look similar to:

```c
  1/*
  2 * Copyright (c) 2023 Nordic Semiconductor ASA
  3 *
  4 * SPDX-License-Identifier: Apache-2.0
  5 */
  6#include <zephyr/kernel.h>
  7#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
  8#include <zephyr/mgmt/mcumgr/smp/smp.h>
  9#include <zephyr/mgmt/mcumgr/mgmt/handlers.h>
 10/* The below should be updated with the real name of the file */
 11#include <example_mgmt.h>
 12#include <zephyr/logging/log.h>
 13#include <assert.h>
 14#include <limits.h>
 15#include <string.h>
 16#include <stdio.h>
 17#include <zcbor_common.h>
 18#include <zcbor_decode.h>
 19#include <zcbor_encode.h>
 20#include <mgmt/mcumgr/util/zcbor_bulk.h>
 21
 22#if defined(CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)
 23#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
 24#if defined(CONFIG_MCUMGR_GRP_EXAMPLE_OTHER_HOOK)
 25/* The below should be updated with the real name of the file */
 26#include <example_mgmt_callbacks.h>
 27#endif
 28#endif
 29
 30LOG_MODULE_REGISTER(mcumgr_example_grp, CONFIG_MCUMGR_GRP_EXAMPLE_LOG_LEVEL);
 31/* Example function with "read" command support, requires both parameters are supplied */
 32static int example_mgmt_test(struct smp_streamer *ctxt)
 33{
 34	uint32_t uint_value = 0;
 35	zcbor_state_t *zse = ctxt->writer->zs;
 36	zcbor_state_t *zsd = ctxt->reader->zs;
 37	bool ok;
 38	struct zcbor_string string_value = { 0 };
 39	size_t decoded;
 40	struct zcbor_map_decode_key_val example_test_decode[] = {
 41		ZCBOR_MAP_DECODE_KEY_DECODER("uint_key", zcbor_uint32_decode, &uint_value),
 42		ZCBOR_MAP_DECODE_KEY_DECODER("string_key", zcbor_tstr_decode, &string_value),
 43	};
 44
 45	LOG_DBG("Example test function called");
 46
 47	ok = zcbor_map_decode_bulk(zsd, example_test_decode, ARRAY_SIZE(example_test_decode),
 48				   &decoded) == 0;
 49	/* Check that both parameters were supplied and that the value of "string_key" is not
 50	 * empty
 51	 */
 52	if (!ok || string_value.len == 0 || !zcbor_map_decode_bulk_key_found(
 53			   example_test_decode, ARRAY_SIZE(example_test_decode), "uint_key")) {
 54		return MGMT_ERR_EINVAL;
 55	}
 56
 57	/* If the value of "uint_key" is over 50, return an error of "not wanted" */
 58	if (uint_value > 50) {
 59		ok = smp_add_cmd_err(zse, MGMT_GROUP_ID_EXAMPLE, EXAMPLE_MGMT_ERR_NOT_WANTED);
 60		goto end;
 61	}
 62
 63	/* Otherwise, return an integer value of 4691 */
 64	ok = zcbor_tstr_put_lit(zse, "return_int") &&
 65	     zcbor_int32_put(zse, 4691);
 66
 67end:
 68	/* If "ok" is false, then there was an error processing the output cbor message, which
 69	 * likely indicates a lack of available memory
 70	 */
 71	return (ok ? MGMT_ERR_EOK : MGMT_ERR_EMSGSIZE);
 72}
 73
 74/* Example function with "write" command support */
 75static int example_mgmt_other(struct smp_streamer *ctxt)
 76{
 77	uint32_t user_value = 0;
 78	zcbor_state_t *zse = ctxt->writer->zs;
 79	zcbor_state_t *zsd = ctxt->reader->zs;
 80	bool ok;
 81	size_t decoded;
 82	struct zcbor_map_decode_key_val example_other_decode[] = {
 83		ZCBOR_MAP_DECODE_KEY_DECODER("user_value", zcbor_uint32_decode, &user_value),
 84	};
 85
 86#if defined(CONFIG_MCUMGR_GRP_EXAMPLE_OTHER_HOOK)
 87	struct example_mgmt_other_data other_data;
 88	enum mgmt_cb_return status;
 89	int32_t err_rc;
 90	uint16_t err_group;
 91#endif
 92
 93	LOG_DBG("Example other function called");
 94
 95	ok = zcbor_map_decode_bulk(zsd, example_other_decode, ARRAY_SIZE(example_other_decode),
 96				   &decoded) == 0;
 97
 98	/* The supplied value is optional, therefore do not return an error if it was not
 99	 * provided
100	 */
101	if (!ok) {
102		return MGMT_ERR_EINVAL;
103	}
104
105#if defined(CONFIG_MCUMGR_GRP_EXAMPLE_OTHER_HOOK)
106	/* Send request to application to check what to do */
107	other_data.user_value = user_value;
108	status = mgmt_callback_notify(MGMT_EVT_OP_EXAMPLE_OTHER, &other_data, sizeof(other_data),
109				      &err_rc, &err_group);
110	if (status != MGMT_CB_OK) {
111		/* If a callback returned an RC error, exit out, if it returned a group error
112		 * code, add the error code to the response and return to the calling function to
113		 * have it sent back to the client
114		 */
115		if (status == MGMT_CB_ERROR_RC) {
116			return err_rc;
117		}
118
119		ok = smp_add_cmd_err(zse, err_group, (uint16_t)err_rc);
120		goto end;
121	}
122#endif
123	/* Return some dummy data to the client */
124	ok = zcbor_tstr_put_lit(zse, "return_string") &&
125	     zcbor_tstr_put_lit(zse, "some dummy data!");
126
127#if defined(CONFIG_MCUMGR_GRP_EXAMPLE_OTHER_HOOK)
128end:
129#endif
130	/* If "ok" is false, then there was an error processing the output cbor message, which
131	 * likely indicates a lack of available memory
132	 */
133	return (ok ? MGMT_ERR_EOK : MGMT_ERR_EMSGSIZE);
134}
135
136#ifdef CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL
137/* This is a lookup function that converts from SMP version 2 group error codes to legacy
138 * MCUmgr error codes, it is only included if support for the original protocol is enabled.
139 * Note that in SMP version 2, MCUmgr error codes can still be returned, but are to be used
140 * only for general SMP/MCUmgr errors. The success/OK error code is not used in translation
141 * functions as it is automatically handled by the base SMP code.
142 */
143static int example_mgmt_translate_error_code(uint16_t err)
144{
145	int rc;
146
147	switch (err) {
148	case EXAMPLE_MGMT_ERR_NOT_WANTED:
149		rc = MGMT_ERR_ENOENT;
150		break;
151
152	case EXAMPLE_MGMT_ERR_REJECTED_BY_HOOK:
153		rc = MGMT_ERR_EBADSTATE;
154		break;
155
156	case EXAMPLE_MGMT_ERR_UNKNOWN:
157	default:
158		rc = MGMT_ERR_EUNKNOWN;
159	}
160
161	return rc;
162}
163#endif
164
165static const struct mgmt_handler example_mgmt_handlers[] = {
166	[EXAMPLE_MGMT_ID_TEST] = {
167		.mh_read = example_mgmt_test,
168		.mh_write = NULL,
169	},
170	[EXAMPLE_MGMT_ID_OTHER] = {
171		.mh_read = NULL,
172		.mh_write = example_mgmt_other,
173	},
174};
175
176static struct mgmt_group example_mgmt_group = {
177	.mg_handlers = example_mgmt_handlers,
178	.mg_handlers_count = ARRAY_SIZE(example_mgmt_handlers),
179	.mg_group_id = MGMT_GROUP_ID_EXAMPLE,
180#ifdef CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL
181	.mg_translate_error = example_mgmt_translate_error_code,
182#endif
183};
184
185static void example_mgmt_register_group(void)
186{
187	/* This function is called during system init before main() is invoked, if the
188	 * handler needs to set anything up before it can be used, it should do it here.
189	 * This register the group so that clients can call the function handlers.
190	 */
191	mgmt_register_group(&example_mgmt_group);
192}
193
194MCUMGR_HANDLER_DEFINE(example_mgmt, example_mgmt_register_group);
```

The above code creates 2 function handlers, `test` which supports read requests and takes 2
required parameters, and `other` which supports write requests and takes 1 optional parameter,
this function handler has an optional notification callback feature that allows other parts of
the code to listen for the event and take any required actions that are necessary or prevent
further execution of the function by returning an error, further details on MCUmgr callback
functionality can be found on [MCUmgr Callbacks](mcumgr_callbacks.md#mcumgr-callbacks).

Note that other code referencing callbacks for custom MCUmgr handlers needs to include both the
base Zephyr callback include file and the custom handler callback file, only in-tree Zephyr
handler headers are included when including the upstream Zephyr callback header file.

### Initial Kconfig

The purpose of the Kconfig file is to provide options which users can enable or change relating
to the functionality of the handler being implemented. An example file would look similar to:

```kconfig
# Copyright Nordic Semiconductor ASA 2023. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# The Kconfig file is dedicated to example management group of
# of MCUmgr subsystem and provides Kconfig options to configure
# group commands behaviour and other aspects.
#
# Options defined in this file should be prefixed:
#  MCUMGR_GRP_EXAMPLE_ -- general group options;
#
# When adding Kconfig options, that control the same feature,
# try to group them together by the same stem after prefix.
if MCUMGR

menuconfig MCUMGR_GRP_EXAMPLE_APP
	bool "MCUmgr handlers for example management (app)"
	select MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
	default y
	help
	  Enables MCUmgr handlers for example management. This demonstrates the
	  file at application-level.

if MCUMGR_GRP_EXAMPLE_APP
config MCUMGR_GRP_EXAMPLE_OTHER_HOOK
	bool "Other hook"
	depends on MCUMGR_MGMT_NOTIFICATION_HOOKS
	help
	  Allows applications to receive callback when the "other" example
	  management function is called

module = MCUMGR_GRP_EXAMPLE
module-str = mcumgr_grp_example
source "subsys/logging/Kconfig.template.log_config"

endif

endif

source "Kconfig.zephyr"
```

### Initial CMakeLists.txt

The CMakeLists.txt file is used by the build system to setup files to compile, include
directories to add and specify options that can be changed. A basic file only need to include the
source files if the Kconfig options are enabled. An example file would look similar to:

Zephyr moduleApplication

```cmake
# Copyright (c) 2023 Nordic Semiconductor ASA
# SPDX-License-Identifier: Apache-2.0

if(CONFIG_MCUMGR_GRP_EXAMPLE_MODULE)
  zephyr_library(mgmt_mcumgr_grp_example)
  # The below should be updated with the real name of the file
  zephyr_library_sources(src/example_mgmt.c)
  zephyr_include_directories(include)
endif()
```

```cmake
if(CONFIG_MCUMGR_GRP_EXAMPLE_APP)
  target_sources(app PRIVATE example_as_module/src/example_mgmt.c)
  zephyr_include_directories(example_as_module/include)
endif()
```

## Including from application

Application-specific MCUmgr handlers can be added by creating/editing application build files.
Example modifications are shown below.

### Example CMakeLists.txt

The application `CMakeLists.txt` file can load the CMake file for the example MCUmgr handler by
adding the following:

```cmake
add_subdirectory(mcumgr/grp/<grp_name>)
```

### Example Kconfig

The application Kconfig file can include the Kconfig file for the example MCUmgr handler by adding
the following to the `Kconfig` file in the application directory (or creating it if it does not
exist):

```kconfig
rsource "mcumgr/grp/<grp_name>/Kconfig"

# Include Zephyr's Kconfig
source "Kconfig.zephyr"
```

## Including from Zephyr Module

Zephyr [Modules (External projects)](../../develop/modules.md#modules) can be used to add custom MCUmgr handlers to multiple different applications
without needing to duplicate the code in each application’s source tree, see [Module yaml file description](../../develop/modules.md#module-yml) for
details on how to set up the module files. Example files are shown below.

### Example zephyr/module.yml

This is an example file which can be used to load the Kconfig and CMake files from the root of the
module directory, and would be placed at `zephyr/module.yml`:

```yaml
build:
  kconfig: Kconfig
  cmake: .
```

### Example CMakeLists.txt

This is an example CMakeLists.txt file which loads the CMake file for the example MCUmgr handler,
and would be placed at `CMakeLists.txt`:

```cmake
add_subdirectory(mcumgr/grp/<grp_name>)
```

### Example Kconfig

This is an example Kconfig file which loads the Kconfig file for the example MCUmgr handler, and
would be placed at `Kconfig`:

```kconfig
rsource "mcumgr/grp/<grp_name>/Kconfig"
```

## Demonstration handler

There is a demonstration project which includes configuration for both application and zephyr
module-MCUmgr handlers which can be used as a basis for created your own in
[tests/subsys/mgmt/mcumgr/handler\_demo/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/mgmt/mcumgr/handler_demo/).
