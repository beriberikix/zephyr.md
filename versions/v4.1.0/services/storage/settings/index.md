---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/storage/settings/index.html
original_path: services/storage/settings/index.html
---

# Settings

The settings subsystem gives modules a way to store persistent per-device
configuration and runtime state. A variety of storage implementations are
provided behind a common API using FCB, NVS, ZMS or a file system. These
different implementations give the application developer flexibility to select
an appropriate storage medium, and even change it later as needs change. This
subsystem is used by various Zephyr components and can be used simultaneously by
user applications.

Settings items are stored as key-value pair strings. By convention,
the keys can be organized by the package and subtree defining the key,
for example the key `id/serial` would define the `serial` configuration
element for the package `id`.

Convenience routines are provided for converting a key value to
and from a string type.

For an example of the settings subsystem refer to [Settings API](../../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.") sample.

Note

As of Zephyr release 4.1 the recommended backends for non-filesystem
storage are [NVS](../nvs/nvs.md#nvs-api) and [ZMS](../zms/zms.md#zms-api).

## Handlers

Settings handlers for subtree implement a set of handler functions.
These are registered using a call to [`settings_register()`](../../../doxygen/html/group__settings.md#gab2043a6d799202e177cc3dfa0cbfa531) for
dynamic handlers or defined using a call to [`SETTINGS_STATIC_HANDLER_DEFINE()`](../../../doxygen/html/group__settings.md#ga2098bcfc32c6daa13292d937712e476e)
for static handlers.

**h\_get**
:   This gets called when asking for a settings element value by its name using
    [`settings_runtime_get()`](../../../doxygen/html/group__settings__rt.md#ga99a4714ba8c184afc659c43ec2020844) from the runtime backend.

**h\_set**
:   This gets called when the value is loaded from persistent storage with
    [`settings_load()`](../../../doxygen/html/group__settings.md#ga89c6d618df81f197cc5c1a2018b00648), or when using [`settings_runtime_set()`](../../../doxygen/html/group__settings__rt.md#gae1b95c47c49774d53b4745af810e881e) from the
    runtime backend.

**h\_commit**
:   This gets called after the settings have been loaded in full.
    Sometimes you don’t want an individual setting value to take
    effect right away, for example if there are multiple settings
    which are interdependent.

**h\_export**
:   This gets called to write all current settings. This happens
    when [`settings_save()`](../../../doxygen/html/group__settings.md#ga789410aa059398d6c8a7851ea6945b55) tries to save the settings or transfer to any
    user-implemented back-end.

Settings handlers also have a commit priority `cprio` that allows to prioritize
the `h_commit` calls. This can be advantageous when e.g. a subsystem initializes
a service that other `h_commit` calls depend on.

Settings handlers `h_commit` routines are by default initialized with `cprio = 0`,
initializing a settings handler with a different priority is done using a call to
[`settings_register_with_cprio()`](../../../doxygen/html/group__settings.md#gadf612631e30119ff688f83f16ad5aa89) for dynamic handlers or using a call to
[`SETTINGS_STATIC_HANDLER_DEFINE_WITH_CPRIO()`](../../../doxygen/html/group__settings.md#ga2ab4b85d30c5f6c19e505fdd8cc8f437) for static handlers. The
specified `cprio` value is an integer where lower values mean higher priority.

## Backends

Backends are meant to load and save data to/from setting handlers, and
implement a set of handler functions. These are registered using a call to
[`settings_src_register()`](../../../doxygen/html/group__settings__backend.md#gad16bb70588cf69873f8872d7bf90e1c6) for backends that can load data, and/or
[`settings_dst_register()`](../../../doxygen/html/group__settings__backend.md#ga37bcada0be44b023cd3759e519e69d01) for backends that can save data. The current
implementation allows for multiple source backends but only a single destination
backend.

**csi\_load**
:   This gets called when loading values from persistent storage using
    [`settings_load()`](../../../doxygen/html/group__settings.md#ga89c6d618df81f197cc5c1a2018b00648).

**csi\_save**
:   This gets called when saving a single setting to persistent storage using
    [`settings_save_one()`](../../../doxygen/html/group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30).

**csi\_save\_start**
:   This gets called when starting a save of all current settings using
    [`settings_save()`](../../../doxygen/html/group__settings.md#ga789410aa059398d6c8a7851ea6945b55) or [`settings_save_subtree()`](../../../doxygen/html/group__settings.md#ga988b9cb22e256c87ac99d8007ff54a13).

**csi\_save\_end**
:   This gets called after having saved of all current settings using
    [`settings_save()`](../../../doxygen/html/group__settings.md#ga789410aa059398d6c8a7851ea6945b55) or [`settings_save_subtree()`](../../../doxygen/html/group__settings.md#ga988b9cb22e256c87ac99d8007ff54a13).

## Zephyr Storage Backends

Zephyr offers the following storage backends:

- Flash Circular Buffer ([`CONFIG_SETTINGS_FCB`](../../../kconfig.md#CONFIG_SETTINGS_FCB "CONFIG_SETTINGS_FCB")).
- A file in the filesystem ([`CONFIG_SETTINGS_FILE`](../../../kconfig.md#CONFIG_SETTINGS_FILE "CONFIG_SETTINGS_FILE")).
- Non-Volatile Storage ([`CONFIG_SETTINGS_NVS`](../../../kconfig.md#CONFIG_SETTINGS_NVS "CONFIG_SETTINGS_NVS")).
- Zephyr Memory Storage ([`CONFIG_SETTINGS_ZMS`](../../../kconfig.md#CONFIG_SETTINGS_ZMS "CONFIG_SETTINGS_ZMS")).

You can declare multiple sources for settings; settings from
all of these are restored when [`settings_load()`](../../../doxygen/html/group__settings.md#ga89c6d618df81f197cc5c1a2018b00648) is called.

There can be only one target for writing settings; this is where
data is stored when you call [`settings_save()`](../../../doxygen/html/group__settings.md#ga789410aa059398d6c8a7851ea6945b55), or [`settings_save_one()`](../../../doxygen/html/group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30).

FCB read target is registered using `settings_fcb_src()`, and write target
using `settings_fcb_dst()`. As a side-effect, `settings_fcb_src()`
initializes the FCB area, so it must be called before calling
`settings_fcb_dst()`. File read target is registered using
`settings_file_src()`, and write target by using `settings_file_dst()`.

Non-volatile storage read target is registered using
`settings_nvs_src()`, and write target by using
`settings_nvs_dst()`.

Zephyr Memory Storage (ZMS) read target is registered using `settings_zms_src()`,
and write target is registered using `settings_zms_dst()`.

ZMS backend has the particularity of using hash functions to hash the settings
key before storing it to the persistent storage. This implementation implies
that some collisions between key’s hashes could occur if a big number of
different keys are stored. This number depends on the selected hash function.

ZMS backend can handle \(2^n\) maximum collisions where n is defined by
(`SETTINGS_ZMS_MAX_COLLISIONS_BITS`).

## Storage Location

The FCB, non-volatile storage (NVS) and ZMS backends look for a fixed
partition with label “storage” by default. A different partition can be
selected by setting the `zephyr,settings-partition` property of the
chosen node in the devicetree.

The file path used by the file backend to store settings is selected via the
option [`CONFIG_SETTINGS_FILE_PATH`](../../../kconfig.md#CONFIG_SETTINGS_FILE_PATH "CONFIG_SETTINGS_FILE_PATH").

## Loading data from persistent storage

A call to [`settings_load()`](../../../doxygen/html/group__settings.md#ga89c6d618df81f197cc5c1a2018b00648) uses an `h_set` implementation
to load settings data from storage to volatile memory.
After all data is loaded, the `h_commit` handler is issued,
signalling the application that the settings were successfully
retrieved.

Technically FCB and file backends may store some history of the entities.
This means that the newest data entity is stored after any
older existing data entities.
Starting with Zephyr 2.1, the back-end must filter out all old entities and
call the callback with only the newest entity.

## Storing data to persistent storage

A call to [`settings_save_one()`](../../../doxygen/html/group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30) uses a backend implementation to store
settings data to the storage medium. A call to [`settings_save()`](../../../doxygen/html/group__settings.md#ga789410aa059398d6c8a7851ea6945b55) uses an
`h_export` implementation to store different data in one operation using
[`settings_save_one()`](../../../doxygen/html/group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30).
A key needs to be covered by a `h_export` only if it is supposed to be stored
by [`settings_save()`](../../../doxygen/html/group__settings.md#ga789410aa059398d6c8a7851ea6945b55) call.

For both FCB and file back-end only storage requests with data which
changes most actual key’s value are stored, therefore there is no need to check
whether a value changed by the application. Such a storage mechanism implies
that storage can contain multiple value assignments for a key , while only the
last is the current value for the key.

### Garbage collection

When storage becomes full (FCB) or consumes too much space (file),
the backend removes non-recent key-value pairs records and unnecessary
key-delete records.

## Secure domain settings

Currently settings doesn’t provide scheme of being secure, and non-secure
configuration storage simultaneously for the same instance.
It is recommended that secure domain uses its own settings instance and it might
provide data for non-secure domain using dedicated interface if needed
(case dependent).

## Example: Device Configuration

This is a simple example, where the settings handler only implements `h_set`
and `h_export`. `h_set` is called when the value is restored from storage
(or when set initially), and `h_export` is used to write the value to
storage thanks to `storage_func()`. The user can also implement some other
export functionality, for example, writing to the shell console).

```c
#define DEFAULT_FOO_VAL_VALUE 1

static int8 foo_val = DEFAULT_FOO_VAL_VALUE;

static int foo_settings_set(const char *name, size_t len,
                            settings_read_cb read_cb, void *cb_arg)
{
    const char *next;
    int rc;

    if (settings_name_steq(name, "bar", &next) && !next) {
        if (len != sizeof(foo_val)) {
            return -EINVAL;
        }

        rc = read_cb(cb_arg, &foo_val, sizeof(foo_val));
        if (rc >= 0) {
            /* key-value pair was properly read.
             * rc contains value length.
             */
            return 0;
        }
        /* read-out error */
        return rc;
    }

    return -ENOENT;
}

static int foo_settings_export(int (*storage_func)(const char *name,
                                                   const void *value,
                                                   size_t val_len))
{
    return storage_func("foo/bar", &foo_val, sizeof(foo_val));
}

struct settings_handler my_conf = {
    .name = "foo",
    .h_set = foo_settings_set,
    .h_export = foo_settings_export
};
```

## Example: Persist Runtime State

This is a simple example showing how to persist runtime state. In this example,
only `h_set` is defined, which is used when restoring value from
persistent storage.

In this example, the `main` function increments `foo_val`, and then
persists the latest number. When the system restarts, the application calls
[`settings_load()`](../../../doxygen/html/group__settings.md#ga89c6d618df81f197cc5c1a2018b00648) while initializing, and `foo_val` will continue counting
up from where it was before restart.

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/reboot.h>
#include <zephyr/settings/settings.h>
#include <zephyr/sys/printk.h>
#include <inttypes.h>

#define DEFAULT_FOO_VAL_VALUE 0

static uint8_t foo_val = DEFAULT_FOO_VAL_VALUE;

static int foo_settings_set(const char *name, size_t len,
                            settings_read_cb read_cb, void *cb_arg)
{
    const char *next;
    int rc;

    if (settings_name_steq(name, "bar", &next) && !next) {
        if (len != sizeof(foo_val)) {
            return -EINVAL;
        }

        rc = read_cb(cb_arg, &foo_val, sizeof(foo_val));
        if (rc >= 0) {
            return 0;
        }

        return rc;
    }

    return -ENOENT;
}

struct settings_handler my_conf = {
    .name = "foo",
    .h_set = foo_settings_set
};

int main(void)
{
    settings_subsys_init();
    settings_register(&my_conf);
    settings_load();

    foo_val++;
    settings_save_one("foo/bar", &foo_val, sizeof(foo_val));

    printk("foo: %d\n", foo_val);

    k_msleep(1000);
    sys_reboot(SYS_REBOOT_COLD);
}
```

## Example: Custom Backend Implementation

This is a simple example showing how to register a simple custom backend
handler ([`CONFIG_SETTINGS_CUSTOM`](../../../kconfig.md#CONFIG_SETTINGS_CUSTOM "CONFIG_SETTINGS_CUSTOM")).

```c
static int settings_custom_load(struct settings_store *cs,
                                const struct settings_load_arg *arg)
{
    //...
}

static int settings_custom_save(struct settings_store *cs, const char *name,
                                const char *value, size_t val_len)
{
    //...
}

/* custom backend interface */
static struct settings_store_itf settings_custom_itf = {
    .csi_load = settings_custom_load,
    .csi_save = settings_custom_save,
};

/* custom backend node */
static struct settings_store settings_custom_store = {
    .cs_itf = &settings_custom_itf
};

int settings_backend_init(void)
{
    /* register custom backend */
    settings_dst_register(&settings_custom_store);
    settings_src_register(&settings_custom_store);
    return 0;
}
```

## API Reference

The Settings subsystem APIs are provided by [include/zephyr/settings/settings.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/settings/settings.h).

### API for general settings usage

[Settings](../../../doxygen/html/group__settings.md)

Related code samples

- [Settings API](../../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.")Load and save configuration values using the settings API.

### API for key-name processing

[Settings name processing](../../../doxygen/html/group__settings__name__proc.md)

Related code samples

- [Settings API](../../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.")Load and save configuration values using the settings API.

### API for runtime settings manipulation

[Settings subsystem runtime](../../../doxygen/html/group__settings__rt.md)

Related code samples

- [Settings API](../../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.")Load and save configuration values using the settings API.

### API of backend interface

[Settings backend interface](../../../doxygen/html/group__settings__backend.md)
