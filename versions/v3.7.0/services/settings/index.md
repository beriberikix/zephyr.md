---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/settings/index.html
original_path: services/settings/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Settings

The settings subsystem gives modules a way to store persistent per-device
configuration and runtime state. A variety of storage implementations are
provided behind a common API using FCB, NVS, or a file system. These different
implementations give the application developer flexibility to select an
appropriate storage medium, and even change it later as needs change. This
subsystem is used by various Zephyr components and can be used simultaneously by
user applications.

Settings items are stored as key-value pair strings. By convention,
the keys can be organized by the package and subtree defining the key,
for example the key `id/serial` would define the `serial` configuration
element for the package `id`.

Convenience routines are provided for converting a key value to
and from a string type.

For an example of the settings subsystem refer to [Settings API](../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.") sample.

Note

As of Zephyr release 2.1 the recommended backend for non-filesystem
storage is [NVS](../storage/nvs/nvs.md#nvs-api).

## Handlers

Settings handlers for subtree implement a set of handler functions.
These are registered using a call to `settings_register()`.

**h\_get**
:   This gets called when asking for a settings element value by its name using
    `settings_runtime_get()` from the runtime backend.

**h\_set**
:   This gets called when the value is loaded from persisted storage with
    `settings_load()`, or when using `settings_runtime_set()` from the
    runtime backend.

**h\_commit**
:   This gets called after the settings have been loaded in full.
    Sometimes you don’t want an individual setting value to take
    effect right away, for example if there are multiple settings
    which are interdependent.

**h\_export**
:   This gets called to write all current settings. This happens
    when `settings_save()` tries to save the settings or transfer to any
    user-implemented back-end.

## Backends

Backends are meant to load and save data to/from setting handlers, and
implement a set of handler functions. These are registered using a call to
`settings_src_register()` for backends that can load data, and/or
`settings_dst_register()` for backends that can save data. The current
implementation allows for multiple source backends but only a single destination
backend.

**csi\_load**
:   This gets called when loading values from persistent storage using
    `settings_load()`.

**csi\_save**
:   This gets called when saving a single setting to persistent storage using
    `settings_save_one()`.

**csi\_save\_start**
:   This gets called when starting a save of all current settings using
    `settings_save()`.

**csi\_save\_end**
:   This gets called after having saved of all current settings using
    `settings_save()`.

## Zephyr Storage Backends

Zephyr has three storage backends: a Flash Circular Buffer
([`CONFIG_SETTINGS_FCB`](../../kconfig.md#CONFIG_SETTINGS_FCB "CONFIG_SETTINGS_FCB")), a file in the filesystem
([`CONFIG_SETTINGS_FILE`](../../kconfig.md#CONFIG_SETTINGS_FILE "CONFIG_SETTINGS_FILE")), or non-volatile storage
([`CONFIG_SETTINGS_NVS`](../../kconfig.md#CONFIG_SETTINGS_NVS "CONFIG_SETTINGS_NVS")).

You can declare multiple sources for settings; settings from
all of these are restored when `settings_load()` is called.

There can be only one target for writing settings; this is where
data is stored when you call `settings_save()`, or `settings_save_one()`.

FCB read target is registered using `settings_fcb_src()`, and write target
using `settings_fcb_dst()`. As a side-effect, `settings_fcb_src()`
initializes the FCB area, so it must be called before calling
`settings_fcb_dst()`. File read target is registered using
`settings_file_src()`, and write target by using `settings_file_dst()`.
Non-volatile storage read target is registered using
`settings_nvs_src()`, and write target by using
`settings_nvs_dst()`.

## Storage Location

The FCB and non-volatile storage (NVS) backends both look for a fixed
partition with label “storage” by default. A different partition can be
selected by setting the `zephyr,settings-partition` property of the
chosen node in the devicetree.

The file path used by the file backend to store settings is selected via the
option `CONFIG_SETTINGS_FILE_PATH`.

## Loading data from persisted storage

A call to `settings_load()` uses an `h_set` implementation
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

A call to `settings_save_one()` uses a backend implementation to store
settings data to the storage medium. A call to `settings_save()` uses an
`h_export` implementation to store different data in one operation using
`settings_save_one()`.
A key need to be covered by a `h_export` only if it is supposed to be stored
by `settings_save()` call.

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
persisted storage.

In this example, the `main` function increments `foo_val`, and then
persists the latest number. When the system restarts, the application calls
`settings_load()` while initializing, and `foo_val` will continue counting
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
handler ([`CONFIG_SETTINGS_CUSTOM`](../../kconfig.md#CONFIG_SETTINGS_CUSTOM "CONFIG_SETTINGS_CUSTOM")).

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

The Settings subsystem APIs are provided by `settings.h`:

### API for general settings usage

Related code samples

[Settings API](../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.")
:   Load and save configuration values using the settings API.

*group* Settings
:   **Since**
    :   1.12

    **Version**
    :   1.0.0

    Defines

    SETTINGS\_MAX\_DIR\_DEPTH

    SETTINGS\_MAX\_NAME\_LEN

    SETTINGS\_MAX\_VAL\_LEN

    SETTINGS\_NAME\_SEPARATOR

    SETTINGS\_NAME\_END

    SETTINGS\_EXTRA\_LEN

    SETTINGS\_STATIC\_HANDLER\_DEFINE(\_hname, \_tree, \_get, \_set, \_commit, \_export)
    :   Define a static handler for settings items.

        This creates a variable *hname prepended by [settings\_handler](#structsettings__handler)*.

        Parameters:
        :   - **\_hname** – handler name
            - **\_tree** – subtree name
            - **\_get** – get routine (can be NULL)
            - **\_set** – set routine (can be NULL)
            - **\_commit** – commit routine (can be NULL)
            - **\_export** – export routine (can be NULL)

    Typedefs

    typedef ssize\_t (\*settings\_read\_cb)(void \*cb\_arg, void \*data, size\_t len)
    :   Function used to read the data from the settings storage in h\_set handler implementations.

        Param cb\_arg:
        :   **[in]** arguments for the read function. Appropriate cb\_arg is transferred to h\_set handler implementation by the backend.

        Param data:
        :   **[out]** the destination buffer

        Param len:
        :   **[in]** length of read

        Return:
        :   positive: Number of bytes read, 0: key-value pair is deleted. On error returns -ERRNO code.

    typedef int (\*settings\_load\_direct\_cb)(const char \*key, size\_t len, [settings\_read\_cb](#c.settings_read_cb) read\_cb, void \*cb\_arg, void \*param)
    :   Callback function used for direct loading.

        Used by [settings\_load\_subtree\_direct](#group__settings_1ga1dfe42f40a7d63bbdb81aed864d0ff12) function.

        Param key:
        :   **[in]** the name with skipped part that was used as name in handler registration

        Param len:
        :   **[in]** the size of the data found in the backend.

        Param read\_cb:
        :   **[in]** function provided to read the data from the backend.

        Param cb\_arg:
        :   **[inout]** arguments for the read function provided by the backend.

        Param param:
        :   **[inout]** parameter given to the [settings\_load\_subtree\_direct](#group__settings_1ga1dfe42f40a7d63bbdb81aed864d0ff12) function.

        Return:
        :   When nonzero value is returned, further subtree searching is stopped.

    Functions

    int settings\_subsys\_init(void)
    :   Initialization of settings and backend.

        Can be called at application startup. In case the backend is a FS Remember to call it after the FS was mounted. For FCB backend it can be called without such a restriction.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_register(struct [settings\_handler](#c.settings_handler) \*cf)
    :   Register a handler for settings items stored in RAM.

        Parameters:
        :   - **cf** – Structure containing registration info.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_load(void)
    :   Load serialized items from registered persistence sources.

        Handlers for serialized item subtrees registered earlier will be called for encountered values.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_load\_subtree(const char \*subtree)
    :   Load limited set of serialized items from registered persistence sources.

        Handlers for serialized item subtrees registered earlier will be called for encountered values that belong to the subtree.

        Parameters:
        :   - **subtree** – **[in]** name of the subtree to be loaded.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_load\_subtree\_direct(const char \*subtree, [settings\_load\_direct\_cb](#c.settings_load_direct_cb) cb, void \*param)
    :   Load limited set of serialized items using given callback.

        This function bypasses the normal data workflow in settings module. All the settings values that are found are passed to the given callback.

        Note

        This function does not call commit function. It works as a blocking function, so it is up to the user to call any kind of commit function when this operation ends.

        Parameters:
        :   - **subtree** – **[in]** subtree name of the subtree to be loaded.
            - **cb** – **[in]** pointer to the callback function.
            - **param** – **[inout]** parameter to be passed when callback function is called.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_save(void)
    :   Save currently running serialized items.

        All serialized items which are different from currently persisted values will be saved.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_save\_subtree(const char \*subtree)
    :   Save limited set of currently running serialized items.

        All serialized items that belong to subtree and which are different from currently persisted values will be saved.

        Parameters:
        :   - **subtree** – **[in]** name of the subtree to be loaded.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_save\_one(const char \*name, const void \*value, size\_t val\_len)
    :   Write a single serialized value to persisted storage (if it has changed value).

        Parameters:
        :   - **name** – Name/key of the settings item.
            - **value** – Pointer to the value of the settings item. This value will be transferred to the [settings\_handler::h\_export](#structsettings__handler_1a30207125407f57a0f117ecaee5a2054a) handler implementation.
            - **val\_len** – Length of the value.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_delete(const char \*name)
    :   Delete a single serialized in persisted storage.

        Deleting an existing key-value pair in the settings mean to set its value to NULL.

        Parameters:
        :   - **name** – Name/key of the settings item.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_commit(void)
    :   Call commit for all settings handler.

        This should apply all settings which has been set, but not applied yet.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_commit\_subtree(const char \*subtree)
    :   Call commit for settings handler that belong to subtree.

        This should apply all settings which has been set, but not applied yet.

        Parameters:
        :   - **subtree** – **[in]** name of the subtree to be committed.

        Returns:
        :   0 on success, non-zero on failure.

    struct settings\_handler
    :   *#include <settings.h>*

        Config handlers for subtree implement a set of handler functions.

        These are registered using a call to [settings\_register](#group__settings_1gab2043a6d799202e177cc3dfa0cbfa531).

        Public Members

        const char \*name
        :   Name of subtree.

        int (\*h\_get)(const char \*key, char \*val, int val\_len\_max)
        :   Get values handler of settings items identified by keyword names.

            Parameters:

            - key[in] the name with skipped part that was used as name in handler registration
            - val[out] buffer to receive value.
            - val\_len\_max[in] size of that buffer.

            Return: length of data read on success, negative on failure.

        int (\*h\_set)(const char \*key, size\_t len, [settings\_read\_cb](#c.settings_read_cb) read\_cb, void \*cb\_arg)
        :   Set value handler of settings items identified by keyword names.

            Parameters:

            - key[in] the name with skipped part that was used as name in handler registration
            - len[in] the size of the data found in the backend.
            - read\_cb[in] function provided to read the data from the backend.
            - cb\_arg[in] arguments for the read function provided by the backend.

            Return: 0 on success, non-zero on failure.

        int (\*h\_commit)(void)
        :   This handler gets called after settings has been loaded in full.

            User might use it to apply setting to the application.

            Return: 0 on success, non-zero on failure.

        int (\*h\_export)(int (\*export\_func)(const char \*name, const void \*val, size\_t val\_len))
        :   This gets called to dump all current settings items.

            This happens when [settings\_save](#group__settings_1ga789410aa059398d6c8a7851ea6945b55) tries to save the settings. Parameters:

            - export\_func: the pointer to the internal function which appends a single key-value pair to persisted settings. Don’t store duplicated value. The name is subtree/key string, val is the string with value.

            Return: 0 on success, non-zero on failure.

            Remark

            The User might limit a implementations of handler to serving only one keyword at one call - what will impose limit to get/set values using full subtree/key name.

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Linked list node info for module internal usage.

    struct settings\_handler\_static
    :   *#include <settings.h>*

        Config handlers without the node element, used for static handlers.

        These are registered using a call to [SETTINGS\_STATIC\_HANDLER\_DEFINE()](#group__settings_1ga2098bcfc32c6daa13292d937712e476e).

        Public Members

        const char \*name
        :   Name of subtree.

        int (\*h\_get)(const char \*key, char \*val, int val\_len\_max)
        :   Get values handler of settings items identified by keyword names.

            Parameters:

            - key[in] the name with skipped part that was used as name in handler registration
            - val[out] buffer to receive value.
            - val\_len\_max[in] size of that buffer.

            Return: length of data read on success, negative on failure.

        int (\*h\_set)(const char \*key, size\_t len, [settings\_read\_cb](#c.settings_read_cb) read\_cb, void \*cb\_arg)
        :   Set value handler of settings items identified by keyword names.

            Parameters:

            - key[in] the name with skipped part that was used as name in handler registration
            - len[in] the size of the data found in the backend.
            - read\_cb[in] function provided to read the data from the backend.
            - cb\_arg[in] arguments for the read function provided by the backend.

            Return: 0 on success, non-zero on failure.

        int (\*h\_commit)(void)
        :   This handler gets called after settings has been loaded in full.

            User might use it to apply setting to the application.

        int (\*h\_export)(int (\*export\_func)(const char \*name, const void \*val, size\_t val\_len))
        :   This gets called to dump all current settings items.

            This happens when [settings\_save](#group__settings_1ga789410aa059398d6c8a7851ea6945b55) tries to save the settings. Parameters:

            - export\_func: the pointer to the internal function which appends a single key-value pair to persisted settings. Don’t store duplicated value. The name is subtree/key string, val is the string with value.

            Return: 0 on success, non-zero on failure.

            Remark

            The User might limit a implementations of handler to serving only one keyword at one call - what will impose limit to get/set values using full subtree/key name.

### API for key-name processing

Related code samples

[Settings API](../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.")
:   Load and save configuration values using the settings API.

*group* Settings name processing
:   API for const name processing.

    Functions

    int settings\_name\_steq(const char \*name, const char \*key, const char \*\*next)
    :   Compares the start of name with a key.

        Some examples: settings\_name\_steq(“bt/btmesh/iv”, “b”, &next) returns 1, next=”t/btmesh/iv” settings\_name\_steq(“bt/btmesh/iv”, “bt”, &next) returns 1, next=”btmesh/iv” settings\_name\_steq(“bt/btmesh/iv”, “bt/”, &next) returns 0, next=NULL settings\_name\_steq(“bt/btmesh/iv”, “bta”, &next) returns 0, next=NULL

        REMARK: This routine could be simplified if the [settings\_handler](#structsettings__handler) names would include a separator at the end.

        Parameters:
        :   - **name** – **[in]** in string format
            - **key** – **[in]** comparison string
            - **next** – **[out]** pointer to remaining of name, when the remaining part starts with a separator the separator is removed from next

        Returns:
        :   0: no match 1: match, next can be used to check if match is full

    int settings\_name\_next(const char \*name, const char \*\*next)
    :   determine the number of characters before the first separator

        Parameters:
        :   - **name** – **[in]** in string format
            - **next** – **[out]** pointer to remaining of name (excluding separator)

        Returns:
        :   index of the first separator, in case no separator was found this is the size of name

### API for runtime settings manipulation

Related code samples

[Settings API](../../samples/subsys/settings/README.md#settings "Load and save configuration values using the settings API.")
:   Load and save configuration values using the settings API.

*group* Settings subsystem runtime
:   API for runtime settings.

    Functions

    int settings\_runtime\_set(const char \*name, const void \*data, size\_t len)
    :   Set a value with a specific key to a module handler.

        Parameters:
        :   - **name** – Key in string format.
            - **data** – Binary value.
            - **len** – Value length in bytes.

        Returns:
        :   0 on success, non-zero on failure.

    int settings\_runtime\_get(const char \*name, void \*data, size\_t len)
    :   Get a value corresponding to a key from a module handler.

        Parameters:
        :   - **name** – Key in string format.
            - **data** – Returned binary value.
            - **len** – requested value length in bytes.

        Returns:
        :   length of data read on success, negative on failure.

    int settings\_runtime\_commit(const char \*name)
    :   Apply settings in a module handler.

        Parameters:
        :   - **name** – Key in string format.

        Returns:
        :   0 on success, non-zero on failure.

### API of backend interface

*group* Settings backend interface
:   settings

    Functions

    void settings\_src\_register(struct [settings\_store](#c.settings_store) \*cs)
    :   Register a backend handler acting as source.

        Parameters:
        :   - **cs** – Backend handler node containing handler information.

    void settings\_dst\_register(struct [settings\_store](#c.settings_store) \*cs)
    :   Register a backend handler acting as destination.

        Parameters:
        :   - **cs** – Backend handler node containing handler information.

    struct settings\_handler\_ \*settings\_parse\_and\_lookup(const char \*name, const char \*\*next)
    :   Parses a key to an array of elements and locate corresponding module handler.

        Parameters:
        :   - **name** – **[in]** in string format
            - **next** – **[out]** remaining of name after matched handler

        Returns:
        :   [settings\_handler\_static](#structsettings__handler__static) on success, NULL on failure.

    int settings\_call\_set\_handler(const char \*name, size\_t len, [settings\_read\_cb](#c.settings_read_cb) read\_cb, void \*read\_cb\_arg, const struct [settings\_load\_arg](#c.settings_load_arg) \*load\_arg)
    :   Calls settings handler.

        Parameters:
        :   - **name** – **[in]** The name of the data found in the backend.
            - **len** – **[in]** The size of the data found in the backend.
            - **read\_cb** – **[in]** Function provided to read the data from the backend.
            - **read\_cb\_arg** – **[inout]** Arguments for the read function provided by the backend.
            - **load\_arg** – **[inout]** Arguments for data loading.

        Returns:
        :   0 or negative error code

    struct settings\_store
    :   *#include <settings.h>*

        Backend handler node for storage handling.

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") cs\_next
        :   Linked list node info for internal usage.

        const struct [settings\_store\_itf](#c.settings_store_itf) \*cs\_itf
        :   Backend handler structure.

    struct settings\_load\_arg
    :   *#include <settings.h>*

        Arguments for data loading.

        Holds all parameters that changes the way data should be loaded from backend.

        Public Members

        const char \*subtree
        :   Name of the subtree to be loaded.

            If NULL, all values would be loaded.

        [settings\_load\_direct\_cb](#c.settings_load_direct_cb) cb
        :   Pointer to the callback function.

            If NULL then matching registered function would be used.

        void \*param
        :   Parameter for callback function.

            Parameter to be passed to the callback function.

    struct settings\_store\_itf
    :   *#include <settings.h>*

        Backend handler functions.

        Sources are registered using a call to [settings\_src\_register](#group__settings__backend_1gad16bb70588cf69873f8872d7bf90e1c6). Destinations are registered using a call to [settings\_dst\_register](#group__settings__backend_1ga37bcada0be44b023cd3759e519e69d01).

        Public Members

        int (\*csi\_load)(struct [settings\_store](#c.settings_store) \*cs, const struct [settings\_load\_arg](#c.settings_load_arg) \*arg)
        :   Loads values from storage limited to subtree defined by subtree.

            Parameters:

            - cs - Corresponding backend handler node,
            - arg - Structure that holds additional data for data loading.

            Note

            Backend is expected not to provide duplicates of the entities. It means that if the backend does not contain any functionality to really delete old keys, it has to filter out old entities and call load callback only on the final entity.

        int (\*csi\_save\_start)(struct [settings\_store](#c.settings_store) \*cs)
        :   Handler called before an export operation.

            Parameters:

            - cs - Corresponding backend handler node

        int (\*csi\_save)(struct [settings\_store](#c.settings_store) \*cs, const char \*name, const char \*value, size\_t val\_len)
        :   Save a single key-value pair to storage.

            Parameters:

            - cs - Corresponding backend handler node
            - name - Key in string format
            - value - Binary value
            - val\_len - Length of value in bytes.

        int (\*csi\_save\_end)(struct [settings\_store](#c.settings_store) \*cs)
        :   Handler called after an export operation.

            Parameters:

            - cs - Corresponding backend handler node Get pointer to the storage instance used by the backend.

            Parameters:

            - cs - Corresponding backend handler node
