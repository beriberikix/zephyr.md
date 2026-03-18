---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/west/west-apis.html
original_path: develop/west/west-apis.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# West APIs

This page documents the Python APIs provided by [west](index.md#west), as well as
some additional APIs used by the [west extensions](extensions.md#west-extensions) in
the zephyr repository.

**Contents**:

## [west.commands](#id4)

All built-in and extension commands are implemented as subclasses of the
[`WestCommand`](#west.commands.WestCommand) class defined here. Some exception types are also
provided.

### [WestCommand](#id5)

*class* west.commands.WestCommand(*name: str*, *help: str*, *description: str*, *accepts\_unknown\_args: bool = False*, *requires\_workspace: bool = True*, *verbosity: [Verbosity](#west.commands.Verbosity) = Verbosity.INF*)
:   Abstract superclass for a west command.

    Instance attributes:

    name
    :   As passed to the constructor.

    help
    :   As passed to the constructor.

    description
    :   As passed to the constructor.

    accepts\_unknown\_args
    :   As passed to the constructor.

    requires\_workspace
    :   As passed to the constructor.

    New in version 0.7.0.

    parser
    :   The argument parser created by calling `WestCommand.add_parser()`.

    Instance properties:

    manifest
    :   A property which returns the [`west.manifest.Manifest`](#west.manifest.Manifest)
        instance for the current manifest file or aborts the program if one was
        not provided. This is only safe to use from the `do_run()` method.

    New in version 0.6.1.

    Changed in version 0.7.0: This is now settable.

    has\_manifest
    :   True if reading the manifest property will succeed instead of erroring
        out.

    config
    :   A settable property which returns the
        [`west.configuration.Configuration`](#west.configuration.Configuration) instance or aborts the
        program if one was not provided. This is only safe to use from the
        `do_run()` method.

    New in version 0.13.0.

    has\_config
    :   True if reading the config property will succeed instead of erroring
        out.

    New in version 0.13.0.

    git\_version\_info
    :   A tuple of Git version information.

    New in version 0.11.0.

    color\_ui
    :   True if the west configuration permits colorized output,
        False otherwise.

    New in version 1.0.0.

    Constructor:

    \_\_init\_\_(*name: str*, *help: str*, *description: str*, *accepts\_unknown\_args: bool = False*, *requires\_workspace: bool = True*, *verbosity: [Verbosity](#west.commands.Verbosity) = Verbosity.INF*)
    :   Abstract superclass for a west command.

        Some fields, such as *name*, *help*, and *description*,
        overlap with kwargs that should be passed to the
        `argparse.ArgumentParser` added by WestCommand.add\_parser.
        This wart is by design: `argparse` doesn’t make many API stability
        guarantees, so this information must be duplicated here for
        future-proofing.

        Parameters:
        :   - **name** – the command’s name, as entered by the user
            - **help** – one-line command help text
            - **description** – multi-line command description
            - **accepts\_unknown\_args** – if true, the command can handle
              arbitrary unknown command line arguments in WestCommand.run.
              Otherwise, it’s a fatal to pass unknown arguments.
            - **requires\_workspace** – if true, the command requires a
              west workspace to run, and running it outside of one is
              a fatal error.
            - **verbosity** – command output verbosity level; can be changed later

    New in version 0.6.0: The *requires\_installation* parameter (removed in v0.13.0).

    New in version 0.7.0: The *requires\_workspace* parameter.

    Changed in version 0.8.0: The *topdir* parameter can now be any `os.PathLike`.

    Changed in version 0.13.0: The deprecated *requires\_installation* parameter was removed.

    New in version 1.0.0: The *verbosity* parameter.

    Methods:

    run(*args: Namespace*, *unknown: list[str]*, *topdir: str | PathLike*, *manifest: [Manifest](#west.manifest.Manifest) | None = None*, *config: [Configuration](#west.configuration.Configuration) | None = None*) → None
    :   Run the command.

        This raises west.commands.CommandContextError if the command
        cannot be run due to a context mismatch. Other exceptions may
        be raised as well.

        Parameters:
        :   - **args** – known arguments parsed via WestCommand.add\_parser
            - **unknown** – unknown arguments present on the command line;
              must be empty unless `accepts_unknown_args` is true
            - **topdir** – west workspace topdir, accessible as a str via
              `self.topdir` from WestCommand.do\_run
            - **manifest** – west.manifest.Manifest or `None`,
              accessible as `self.manifest` from WestCommand.do\_run
            - **config** – west.configuration.Configuration or `None`,
              accessible as `self.config` from WestCommand.do\_run

    Changed in version 0.6.0: The *topdir* argument was added.

    add\_parser(*parser\_adder*) → ArgumentParser
    :   Registers a parser for this command, and returns it.

        The parser object is stored in a `parser` attribute.

        Parameters:
        :   **parser\_adder** – The return value of a call to
            `argparse.ArgumentParser.add_subparsers()`

    add\_pre\_run\_hook(*hook: Callable[[[WestCommand](#west.commands.WestCommand)], None]*) → None
    :   Add a hook which will be called right before do\_run().

        This can be useful to defer work that needs a fully set up
        command to work.

        Parameters:
        :   **hook** – hook to add

    New in version 1.0.0.

    check\_call(*args*, *\*\*kwargs*)
    :   Runs `subprocess.check_call(args, **kwargs)` after
        logging the call at Verbosity.DBG\_MORE`` level.

    Changed in version 1.2.0: The *cwd* keyword argument was replaced with a catch-all `**kwargs`.

    Changed in version 0.11.0.

    check\_output(*args*, *\*\*kwargs*)
    :   Runs `subprocess.check_output(args, **kwargs)` after
        logging the call at Verbosity.DBG\_MORE level.

    Changed in version 1.2.0: The *cwd* keyword argument was replaced with a catch-all `**kwargs`.

    Changed in version 0.11.0.

    run\_subprocess(*args*, *\*\*kwargs*)
    :   Runs `subprocess.run(args, **kwargs)` after logging
        the call at Verbosity.DBG\_MORE level.

    New in version 1.2.0.

    All subclasses must provide the following abstract methods, which are used
    to implement the above:

    *abstract* do\_add\_parser(*parser\_adder*) → ArgumentParser
    :   Subclass method for registering command line arguments.

        This is called by WestCommand.add\_parser to register the
        command’s options and arguments.

        Subclasses should `parser_adder.add_parser()` to add an
        `ArgumentParser` for that subcommand, then add any
        arguments. The final parser must be returned.

        Parameters:
        :   **parser\_adder** – The return value of a call to
            `argparse.ArgumentParser.add_subparsers()`

    *abstract* do\_run(*args: Namespace*, *unknown: list[str]*)
    :   Subclasses must implement; called to run the command.

        Parameters:
        :   - **args** – `argparse.Namespace` of parsed arguments
            - **unknown** – If `accepts_unknown_args` is true, a
              sequence of un-parsed argument strings.

    The following methods should be used when the command needs to print output.
    These were introduced to enable a transition from the deprecated
    `west.log` module to a per-command interface that will allow for a global
    “quiet” mode for west commands in a future release:

    dbg(*\*args*, *level: [Verbosity](#west.commands.Verbosity) = Verbosity.DBG*, *end: str = '\n'*)
    :   Print a verbose debug message.

        The message is only printed if *self.verbosity* is at least *level*.

        Parameters:
        :   - **args** – sequence of arguments to print
            - **level** – verbosity level of the message

    Changed in version 1.2.0: The *end* argument.

    New in version 1.0.0.

    inf(*\*args*, *colorize: bool = False*, *end: str = '\n'*)
    :   Print an informational message.

        The message is only printed if *self.verbosity* is at least INF.

        Parameters:
        :   - **args** – sequence of arguments to print.
            - **colorize** – If this is True, the configuration option `color.ui`
              is undefined or true, and stdout is a terminal, then
              the message is printed in green.

    Changed in version 1.2.0: The *end* argument.

    New in version 1.0.0.

    wrn(*\*args*, *end: str = '\n'*)
    :   Print a warning.

        The message is only printed if *self.verbosity* is at least WRN.

        The message is prefixed with the string `"WARNING: "`.

        If the configuration option `color.ui` is undefined or true and
        stdout is a terminal, then the message is printed in yellow.

        Parameters:
        :   **args** – sequence of arguments to print.

    Changed in version 1.2.0: The *end* argument.

    New in version 1.0.0.

    err(*\*args*, *fatal: bool = False*, *end: str = '\n'*)
    :   Print an error.

        The message is only printed if *self.verbosity* is at least ERR.

        This function does not abort the program. For that, use die().

        If the configuration option `color.ui` is undefined or true and
        stdout is a terminal, then the message is printed in red.

        Parameters:
        :   - **args** – sequence of arguments to print.
            - **fatal** – if True, the the message is prefixed with
              “FATAL ERROR: “; otherwise, “ERROR: ” is used.

    Changed in version 1.2.0: The *end* argument.

    New in version 1.0.0.

    die(*\*args*, *exit\_code: int = 1*) → NoReturn
    :   Print a fatal error using err(), and abort the program.

        Parameters:
        :   - **args** – sequence of arguments to print.
            - **exit\_code** – return code the program should use when aborting.

        Equivalent to `die(*args, fatal=True)`, followed by an attempt to
        abort with the given *exit\_code*.

    New in version 1.0.0.

    banner(*\*args*)
    :   Prints args as a “banner” using inf().

        The args are prefixed with ‘=== ‘ and colorized by default.

    New in version 1.0.0.

    small\_banner(*\*args*)
    :   Prints args as a smaller banner(), i.e. prefixed with ‘– ‘ and
        not colorized.

    New in version 1.0.0.

### [Verbosity](#id6)

Since west v1.0, west commands should print output using methods like
west.commands.WestCommand.dbg(), west.commands.WestCommand.inf(), etc. (see
above). This section documents a related enum used to declare verbosity levels.

*class* west.commands.Verbosity(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)
:   Verbosity levels for WestCommand instances.

    QUIET *= 0*
    :   No output is printed when WestCommand.dbg(), .inf(), etc.
        are called.

    ERR *= 1*
    :   Only error messages are printed.

    WRN *= 2*
    :   Only error and warnings are printed.

    INF *= 3*
    :   Errors, warnings, and informational messages are printed.

    DBG *= 4*
    :   Like INFO, but WestCommand.dbg(…, level=Verbosity.DBG) output
        is also printed.

    DBG\_MORE *= 5*
    :   Like DEBUG, but WestCommand.dbg(…, level=Verbosity.DBG\_MORE)
        output is also printed.

    DBG\_EXTREME *= 6*
    :   Like DEBUG\_MORE, but WestCommand.dbg(…, level=Verbosity.DBG\_EXTREME)
        output is also printed.

New in version 1.0.0.

### [Exceptions](#id7)

*class* west.commands.CommandError(*returncode=1*)
:   Bases: `RuntimeError`

    Indicates that a command failed.

    returncode
    :   Recommended program exit code for this error.

*class* west.commands.CommandContextError(*returncode=1*)
:   Bases: [`CommandError`](#west.commands.CommandError)

    Indicates that a context-dependent command could not be run.

## [west.configuration](#id8)

West configuration file handling.

West follows Git-like conventions for configuration file locations.
There are three types of configuration file: system-wide files apply
to all users on the current machine, global files apply to the current
user, and local files apply to the current west workspace.

System files:

- Linux: `/etc/westconfig`
- macOS: `/usr/local/etc/westconfig`
- Windows: `%PROGRAMDATA%\west\config`

Global files:

- Linux: `~/.westconfig` or (if `$XDG_CONFIG_HOME` is set)
  `$XDG_CONFIG_HOME/west/config`
- macOS: `~/.westconfig`
- Windows: `.westconfig` in the user’s home directory, as determined
  by os.path.expanduser.

Local files:

- Linux, macOS, Windows: `<workspace-topdir>/.west/config`

You can override these files’ locations with the `WEST_CONFIG_SYSTEM`,
`WEST_CONFIG_GLOBAL`, and `WEST_CONFIG_LOCAL` environment variables.

Configuration values from later configuration files override configuration
from earlier ones. Local values have highest precedence, and system values
lowest.

Since west v0.13, the recommended class for reading this is
[`west.configuration.Configuration`](#west.configuration.Configuration).

Note that if you are writing a [west extension](extensions.md#west-extensions), you can
access the current `Configuration` object as `self.config`. See
[`west.commands.WestCommand`](#west.commands.WestCommand).

### [Configuration API](#id9)

This is the recommended API to use since west v0.13.

*class* west.configuration.ConfigFile(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)
:   Types of west configuration file.

    Enumeration members:

    - SYSTEM: system level configuration shared by all users
    - GLOBAL: global or user-wide configuration
    - LOCAL: per-workspace configuration
    - ALL: all three of the above, where applicable

*class* west.configuration.Configuration(*topdir: str | PathLike | None = None*)
:   Represents the available configuration options and their values.

    Allows getting, setting, and deleting configuration options
    in the system, global, and local files.

    Setting values affects files immediately and is not protected against
    concurrent reads. The caller is responsible for any necessary
    mutual exclusion.

    WEST\_CONFIG\_\* environment variables take effect when and only when
    a Configuration object is created. This can be used to point
    different objects at different files.

    If no topdir argument is passed to the constructor and WEST\_CONFIG\_LOCAL
    is not defined then the object does not point to any local file.

    New in version 0.13.0.

    delete(*option: str*, *configfile: [ConfigFile](#west.configuration.ConfigFile) | None = None*) → None
    :   Delete an option from the given file or files.

        If *option* is not set in the given *configfile*, KeyError is raised.

        Parameters:
        :   - **option** – option to delete, in ‘foo.bar’ form
            - **configfile** –

              If ConfigFile.ALL, delete *option* in all files
              where it is set.

              If None, delete *option* only in the highest
              precedence file where it is set.

              Otherwise, delete from the given ConfigFile.

    get(*option: str*, *default: str | None = None*, *configfile: [ConfigFile](#west.configuration.ConfigFile) = ConfigFile.ALL*) → str | None
    :   Get a configuration option’s value as a string.

        Parameters:
        :   - **option** – option to get, in ‘foo.bar’ form
            - **default** – default value to return if option is missing
            - **configfile** – type of config file look for the value in

    getboolean(*option: str*, *default: bool = False*, *configfile: [ConfigFile](#west.configuration.ConfigFile) = ConfigFile.ALL*) → bool
    :   Get a configuration option’s value as a bool.

        The configparser module’s conversion to boolean is applied
        to any value discovered. Invalid values raise ValueError.

        Parameters:
        :   - **option** – option to get, in ‘foo.bar’ form
            - **default** – default value to return if option is missing
            - **configfile** – type of config file to look for the value in

    getfloat(*option: str*, *default: float | None = None*, *configfile: [ConfigFile](#west.configuration.ConfigFile) = ConfigFile.ALL*) → float | None
    :   Get a configuration option’s value as a float.

        Parameters:
        :   - **option** – option to get, in ‘foo.bar’ form
            - **default** – default value to return if option is missing
            - **configfile** – type of config file to look for the value in

    getint(*option: str*, *default: int | None = None*, *configfile: [ConfigFile](#west.configuration.ConfigFile) = ConfigFile.ALL*) → int | None
    :   Get a configuration option’s value as an int.

        Parameters:
        :   - **option** – option to get, in ‘foo.bar’ form
            - **default** – default value to return if option is missing
            - **configfile** – type of config file to look for the value in

    items(*configfile: [ConfigFile](#west.configuration.ConfigFile) = ConfigFile.ALL*) → Iterable[tuple[str, Any]]
    :   Iterator of option, value pairs.

    set(*option: str*, *value: Any*, *configfile: [ConfigFile](#west.configuration.ConfigFile) = ConfigFile.LOCAL*) → None
    :   Set a configuration option’s value.

        The write to the configuration file takes effect
        immediately. No concurrency protection is performed against
        concurrent access from the time that this Configuration object
        was created. If the file may have been modified since that
        time, either create a new Configuration object before using
        this method or lose the intervening modifications.

        Parameters:
        :   - **option** – option to set, in ‘foo.bar’ form
            - **value** – value to set option to
            - **configfile** – type of config file to set the value in

### [Deprecated APIs](#id10)

The following APIs also use [`west.configuration.ConfigFile`](#west.configuration.ConfigFile), but they
operate by default on a global object which stores the current workspace
configuration. This has proven to be a bad design decision since west’s APIs
can be used from multiple workspaces. They were deprecated in west v0.13.0.

These APIs are preserved for compatibility with older extensions. They should
not be used in new code when west v0.13.0 or later may be assumed.

west.configuration.read\_config(*configfile: ~west.configuration.ConfigFile | None = None*, *config: ~configparser.ConfigParser = <configparser.ConfigParser object>*, *topdir: str | ~os.PathLike | None = None*) → None
:   Read configuration files into *config*.

    Reads the files given by *configfile*, storing the values into the
    configparser.ConfigParser object *config*. If *config* is not
    given, the global west.configuration.config object is used.

    If *configfile* is given, only the files implied by its value are
    read. If not given, `ConfigFile.ALL` is used.

    If *configfile* requests local configuration options (i.e. if it
    is `ConfigFile.LOCAL` or `ConfigFile.ALL`:

    > - If *topdir* is given, topdir/.west/config is read
    > - Next, if WEST\_CONFIG\_LOCAL is set in the environment, its
    >   contents (a file) are used.
    > - Otherwise, the file system is searched for a local
    >   configuration file, and a failure to find one is ignored.

    Parameters:
    :   - **configfile** – a west.configuration.ConfigFile
        - **config** – configuration object to read into
        - **topdir** – west workspace root to read local options from

Changed in version 0.8.0: The deprecated *read\_config* parameter was removed.

Changed in version 0.6.0: Errors due to an inability to find a local configuration file are ignored.

west.configuration.update\_config(*section: str*, *key: str*, *value: Any*, *configfile: [ConfigFile](#west.configuration.ConfigFile) = ConfigFile.LOCAL*, *topdir: str | PathLike | None = None*) → None
:   Sets `section.key` to *value* in the given configuration file.

    Parameters:
    :   - **section** – config section; will be created if it does not exist
        - **key** – key to set in the given section
        - **value** – value to set the key to
        - **configfile** – west.configuration.ConfigFile, must not be ALL
        - **topdir** – west workspace root to write local config options to

    The destination file to write is given by *configfile*. The
    default value (`ConfigFile.LOCAL`) writes to the local
    configuration file given by:

    - topdir/.west/config, if topdir is given, or
    - the value of ‘WEST\_CONFIG\_LOCAL’ in the environment, if set, or
    - the local configuration file in the west workspace
      found by searching the file system (raising WestNotFound if
      one is not found).

west.configuration.config
:   Module-global ConfigParser instance for the current configuration. This
    should be initialized with [`west.configuration.read_config()`](#west.configuration.read_config) before
    being read.

## [west.log (deprecated)](#id11)

Deprecated due to its use of global state, which makes
west harder to unit test. See:

> [https://github.com/zephyrproject-rtos/west/issues/149](https://github.com/zephyrproject-rtos/west/issues/149)

Removal won’t come until west v2.0.

In the future, commands should use equivalent WestCommand methods
instead. For example, use WestCommand.dbg() instead of west.log.dbg(),
and so forth.

Provides common methods for printing messages to display to the user
which respect the `color.ui` configuration option and verbosity
level. These were formerly encouraged for WestCommand instances.

### [Verbosity control](#id12)

To set the global verbosity level, use `set_verbosity()`.

west.log.set\_verbosity(*value*)
:   Set the logging verbosity level.

    Parameters:
    :   **value** – verbosity level to set, e.g. VERBOSE\_VERY.

These verbosity levels are defined.

west.log.VERBOSE\_NONE *= 0*
:   Default verbosity level, no dbg() messages printed.

west.log.VERBOSE\_NORMAL *= 1*
:   Some verbose messages printed.

west.log.VERBOSE\_VERY *= 2*
:   Very verbose output messages will be printed.

west.log.VERBOSE\_EXTREME *= 3*
:   Extremely verbose output messages will be printed.

### [Output functions](#id13)

The main functions are `dbg()`, `inf()`, `wrn()`, `err()`, and
`die()`. Two special cases of `inf()`, `banner()` and `small_banner()`,
are also available for grouping output into “sections”.

west.log.dbg(*\*args*, *level=1*)
:   Print a verbose debug logging message.

    Parameters:
    :   - **args** – sequence of arguments to print.
        - **level** – verbosity level to set, e.g. VERBOSE\_VERY.

    The message is only printed if the `level` parameter is at most
    the current verbosity level.

west.log.inf(*\*args*, *colorize=False*)
:   Print an informational message.

    Parameters:
    :   - **args** – sequence of arguments to print.
        - **colorize** – If this is True, the configuration option `color.ui`
          is undefined or true, and stdout is a terminal, then
          the message is printed in green.

west.log.wrn(*\*args*)
:   Print a warning.

    Parameters:
    :   **args** – sequence of arguments to print.

    The message is prefixed with the string `"WARNING: "`.

    If the configuration option `color.ui` is undefined or true and
    stdout is a terminal, then the message is printed in yellow.

west.log.err(*\*args*, *fatal=False*)
:   Print an error.

    This function does not abort the program. For that, use die().

    Parameters:
    :   - **args** – sequence of arguments to print.
        - **fatal** – if True, the the message is prefixed with “FATAL ERROR: “;
          otherwise, “ERROR: ” is used.

    If the configuration option `color.ui` is undefined or true and
    stdout is a terminal, then the message is printed in red.

west.log.die(*\*args*, *exit\_code=1*) → NoReturn
:   Print a fatal error, and abort the program.

    Parameters:
    :   - **args** – sequence of arguments to print.
        - **exit\_code** – return code the program should use when aborting.

    Equivalent to `die(*args, fatal=True)`, followed by an attempt to
    abort with the given *exit\_code*.

west.log.banner(*\*args*)
:   Prints args as a “banner” at inf() level.

    The args are prefixed with ‘=== ‘ and colorized by default.

west.log.small\_banner(*\*args*)
:   Prints args as a smaller banner(), i.e. prefixed with ‘– ‘ and
    not colorized.

## [west.manifest](#id14)

Parser and abstract data types for west manifests.

The main classes are [`Manifest`](#west.manifest.Manifest) and [`Project`](#west.manifest.Project). These
represent the contents of a [manifest file](manifest.md#west-manifests). The
recommended method for parsing west manifests is
[`Manifest.from_topdir()`](#west.manifest.Manifest.from_topdir).

### [Constants and functions](#id15)

west.manifest.MANIFEST\_PROJECT\_INDEX *= 0*
:   Index in a Manifest.projects attribute where the ManifestProject
    instance for the workspace is stored.

west.manifest.MANIFEST\_REV\_BRANCH *= 'manifest-rev'*
:   A git revision which points to the most recent Project update.

west.manifest.QUAL\_MANIFEST\_REV\_BRANCH *= 'refs/heads/manifest-rev'*
:   A fully qualified reference to MANIFEST\_REV\_BRANCH.

west.manifest.QUAL\_REFS\_WEST *= 'refs/west/'*
:   Git ref space used by west for internal purposes.

west.manifest.SCHEMA\_VERSION *= '1.2'*
:   The latest manifest schema version supported by this west program.

    This value will change whenever a new version of west includes new
    manifest file features not supported by earlier versions of west.
    (Its value changed to 1.0 following the release of west versions
    v1.0.x, so that users can say “I want schema version 1” instead of
    having to keep using ‘0.13’, which was the previous version this
    changed.)

west.manifest.manifest\_path() → str
:   Absolute path of the manifest file in the current workspace.

    Exceptions raised:

    > - west.util.WestNotFound if called from outside of a west
    >   workspace
    > - MalformedConfig if the configuration file has no
    >   `manifest.path` key
    > - `FileNotFoundError` if no manifest file exists as determined by
    >   `manifest.path` and `manifest.file`

west.manifest.validate(*data: Any*) → dict[str, Any]
:   Validate manifest data

    Raises an exception if the manifest data is not valid for loading
    by this version of west. (Actually attempting to load the data may
    still fail if the it contains imports which cannot be resolved.)

    Returns the validated YAML dictionary, which may be convenient if
    the argument was a str and further loading is required.

    Parameters:
    :   **data** – YAML manifest data as a string or object

Changed in version 0.13.0: This returns the validated dict containing the parsed YAML data.

### [Manifest and sub-objects](#id16)

*class* west.manifest.Manifest(*\**, *source\_data: str | dict | None = None*, *topdir: str | PathLike | None = None*, *config: [Configuration](#west.configuration.Configuration) | None = None*, *importer: Callable[[[Project](#west.manifest.Project), str], str | list[str] | None] | None = None*, *import\_flags: [ImportFlag](#west.manifest.ImportFlag) = ImportFlag.DEFAULT*, *internal\_import\_ctx: \_import\_ctx | None = None*)
:   The parsed contents of a west manifest file.

    \_\_init\_\_(*\**, *source\_data: str | dict | None = None*, *topdir: str | PathLike | None = None*, *config: [Configuration](#west.configuration.Configuration) | None = None*, *importer: Callable[[[Project](#west.manifest.Project), str], str | list[str] | None] | None = None*, *import\_flags: [ImportFlag](#west.manifest.ImportFlag) = ImportFlag.DEFAULT*, *internal\_import\_ctx: \_import\_ctx | None = None*)
    :   Using one of the factory methods may be easier than direct
        instantiation.

        Instance attributes:

        > - `abspath`: absolute path to the manifest file, or None
        > - `posixpath`: like `abspath`, but with slashes (`/`)
        >   as separators
        > - `relative_path`: path to the manifest file relative to
        >   the workspace topdir (i.e. the combined manifest.path
        >   and manifest.file configuration options), or None
        > - `yaml_path`: the value of the “self: path:” field in
        >   the manifest YAML, or None
        > - `repo_path`: relative filesystem path to the manifest
        >   repository from the workspace topdir as a string, or None
        > - `repo_abspath`: the absolute filesystem path to the manifest
        >   repository as a string with symlinks resolved, or None
        > - `repo_posixpath`: like `repo_abspath`, but with slashes
        >   as separators
        > - `topdir`: the workspace top level directory as a string
        >   :   with symlinks resolved, or None
        > - `projects`: sequence of Project instances
        > - `has_imports`: bool, True if the manifest contains
        >   an “import:” attribute in “self:” or “projects:” that were
        >   not ignored due to *import\_flags* or manifest.project-filter;
        >   False otherwise
        > - `group_filter`: a group filter value equivalent to
        >   the resolved manifest’s “group-filter:”, along with any
        >   values from imported manifests. This value may be simpler
        >   than the actual input data.

        You must give exactly one of the *topdir* and *source\_data* kwargs:

        > - Use *topdir* to load a manifest from a workspace
        > - Use *source\_data* to load data without any workspace

        If *topdir* is given:

        > - You may pass *config* if you already have the desired
        >   workspace configuration loaded. This is used to
        >   find the manifest file’s location from the manifest.path
        >   and manifest.file options. It’s your responsibility
        >   to make sure *config* is properly loaded from *topdir*
        >   in this case.
        >
        >   If you don’t pass *config*, the constructor will
        >   instantiate the correct Configuration object itself.
        > - The return value’s absolute paths will be relative to
        >   *topdir*. If *topdir* is not an absolute path, it will be
        >   resolved first (this resolves symlinks too).
        >   If it is absolute, it will not be resolved.

        If *source\_data* is given:

        > - You cannot pass *config*.
        > - Manifest imports will fail unless you pass *importer*
        >   or ignore them with *import\_flags*.
        > - All absolute paths (like `projects[i].abspath`)
        >   in the results will be `None`.

        The *importer* kwarg, if given, is a callable. It is used
        as a callback by the constructor when it must import manifest
        data that aren’t found locally on the file system.

        The *importer* callback will be called as:

        > `importer(project, file)`

        where `project` is a west.manifest.Project and `file`
        is the missing manifest file. The file’s contents at
        refs/heads/manifest-rev should usually be returned by the callback,
        potentially after fetching the project’s revision from its remote URL
        and updating that ref.

        The *importer* callback’s return value should be a string containing
        manifest data, or a list of strings if `file` is a directory
        containing YAML files. A return value of None will cause the import
        to be ignored.

        Exceptions raised:

        > - MalformedManifest: if the manifest data is invalid
        > - ManifestImportFailed: if an import failed
        > - ManifestVersionError: if this version of west is too
        >   old to parse the manifest (based on its schema version)
        > - `OSError`: or subclasses, when files cannot be opened
        > - `ValueError`: for other invalid arguments

        Parameters:
        :   - **source\_data** – parsed YAML data as a Python object, or a
              string containing unparsed YAML data
            - **topdir** – west workspace top level directory
            - **config** – optional pre-loaded configuration from topdir
            - **importer** – provides missing manifest import data
            - **import\_flags** – bit mask, controls import resolution
            - **internal\_import\_ctx** – for internal use only; do not use

    Changed in version 0.7.0: The *importer* and *import\_flags* keyword arguments.

    Changed in version 0.13.0: All arguments were made keyword-only. The *source\_file* argument was
    removed (use *topdir* instead). The function no longer raises
    `WestNotFound`.

    New in version 0.13.0: The *config* argument.

    New in version 0.13.0: The *abspath*, *posixpath*, *relative\_path*, *yaml\_path*, *repo\_path*,
    *repo\_posixpath*, and *userdata* attributes.

    *static* from\_topdir(*topdir: str | PathLike | None = None*, *config: [Configuration](#west.configuration.Configuration) | None = None*, *importer: Callable[[[Project](#west.manifest.Project), str], str | list[str] | None] | None = None*, *import\_flags: [ImportFlag](#west.manifest.ImportFlag) = ImportFlag.DEFAULT*) → [Manifest](#west.manifest.Manifest)
    :   Manifest object factory given a workspace topdir.

        The default behavior if *topdir* is not given is to find the
        current west workspace’s manifest file starting from the
        current working directory.

        Parameters:
        :   - **topdir** – workspace top-level directory
            - **config** – passed to Manifest()
            - **importer** – passed to Manifest()
            - **import\_flags** – passed to Manifest()

    New in version 0.13.0.

    *static* from\_file(*source\_file: str | PathLike | None = None*, *importer: Callable[[[Project](#west.manifest.Project), str], str | list[str] | None] | None = None*, *import\_flags: [ImportFlag](#west.manifest.ImportFlag) = ImportFlag.DEFAULT*) → [Manifest](#west.manifest.Manifest)
    :   Manifest object factory given a source YAML file.

        The default behavior if *source\_file* is not given is to find
        the current west workspace’s manifest file and resolve it
        starting from the current working directory. This matches the
        from\_topdir() behavior.

        With *source\_file*, the *topdir* is found starting there. As a
        special case, this factory allows you to load a Manifest
        from an arbitrary file in an arbitrary git repository in the
        workspace. The `manifest.path` and `manifest.file` configuration
        values do not have to refer to *source\_file* in this case.

        This can be useful to load an alternative manifest file within
        an existing workspace for purposes of comparing two manifests,
        for example.

        Exceptions raised:

        > - west.util.WestNotFound if no *topdir* can be found
        >   starting from *source\_file* or the current working directory
        > - CalledProcessError if the git repository containing
        >   *source\_file* cannot be found
        > - Other exceptions from the Manifest constructor

        Parameters:
        :   - **source\_file** – source file to load
            - **importer** – passed to Manifest()
            - **import\_flags** – passed to Manifest()

    Changed in version 0.7.0: `**kwargs` added.

    Changed in version 0.8.0: The *source\_file*, *manifest\_path*, and *topdir* arguments
    can now be any `os.PathLike`.

    Changed in version 0.13.0: The *manifest\_path* and *topdir* arguments were removed.

    *static* from\_data(*source\_data: str | dict*, *importer: Callable[[[Project](#west.manifest.Project), str], str | list[str] | None] | None = None*, *import\_flags: [ImportFlag](#west.manifest.ImportFlag) = ImportFlag.DEFAULT*) → [Manifest](#west.manifest.Manifest)
    :   Manifest object factory given parsed YAML data.

        This factory does not read any configuration files.

        Let the return value be `m`. Relative project paths in `m`
        (like `m.projects[1].path`) are taken from *source\_data*.
        Absolute project paths are all None.

        May raise the same exceptions as the Manifest constructor.

        Parameters:
        :   - **source\_data** – parsed YAML data as a Python object, or a
              string with unparsed YAML data
            - **importer** – passed to Manifest
            - **import\_flags** – passed to Manifest

    Changed in version 0.7.0: `**kwargs` added, and *source\_data* may be a `str`.

    Changed in version 0.13.0: The *manifest\_path* and *topdir* arguments were removed.

    Conveniences for accessing sub-objects by name or other identifier:

    get\_projects(*project\_ids: Iterable[str | PathLike]*, *allow\_paths: bool = True*, *only\_cloned: bool = False*) → list[[west.manifest.Project](#west.manifest.Project)]
    :   Get a list of Project objects in the manifest from
        *project\_ids*.

        If *project\_ids* is empty, a copy of `self.projects`
        attribute is returned as a list. Otherwise, the returned list
        has projects in the same order as *project\_ids*.

        `ValueError` is raised if:

        > - *project\_ids* contains unknown project IDs
        > - (with *only\_cloned*) an uncloned project was found

        The `ValueError` *args* attribute is a 2-tuple with a list
        of unknown *project\_ids* at index 0, and a list of uncloned
        Project objects at index 1.

        Parameters:
        :   - **project\_ids** – a sequence of projects, identified by name
              or (absolute or relative) path. Names are matched first; path
              checking can be disabled with *allow\_paths*.
            - **allow\_paths** – if false, *project\_ids* is assumed to contain
              names only, not paths
            - **only\_cloned** – raise an exception for uncloned projects

    Changed in version 0.8.0: The *project\_ids* sequence can now contain any `os.PathLike`.

    New in version 0.6.1.

    Additional methods:

    as\_dict(*active\_only: bool = False*) → dict
    :   Returns a dict representing self, fully resolved.

        The value is “resolved” in that the result is as if all
        projects had been defined in a single manifest without any
        import attributes.

        Parameters:
        :   **active\_only** – Do not resolve inactive projects

    New in version 0.7.0.

    as\_frozen\_dict(*active\_only: bool = False*) → dict
    :   Returns a dict representing self, but frozen.

        The value is “frozen” in that all project revisions are the
        full SHAs pointed to by QUAL\_MANIFEST\_REV\_BRANCH references.

        Raises `RuntimeError` if a project SHA can’t be resolved.

        Parameters:
        :   **active\_only** – Do not freeze inactive projects

    as\_yaml(*active\_only: bool = False*, *\*\*kwargs*) → str
    :   Returns a YAML representation for self, fully resolved.

        The value is “resolved” in that the result is as if all
        projects had been defined in a single manifest without any
        import attributes.

        Parameters:
        :   - **active\_only** – Do not resolve inactive projects
            - **kwargs** – passed to yaml.safe\_dump()

    New in version 0.7.0.

    as\_frozen\_yaml(*active\_only: bool = False*, *\*\*kwargs*) → str
    :   Returns a YAML representation for self, but frozen.

        The value is “frozen” in that all project revisions are the
        full SHAs pointed to by QUAL\_MANIFEST\_REV\_BRANCH references.

        Raises `RuntimeError` if a project SHA can’t be resolved.

        Parameters:
        :   - **active\_only** – Do not freeze inactive projects
            - **kwargs** – passed to yaml.safe\_dump()

    New in version 0.7.0.

    is\_active(*project: [Project](#west.manifest.Project)*, *extra\_filter: Iterable[str] | None = None*) → bool
    :   Is a project active?

        If the manifest.project-filter configuration option is set,
        the return value determined by the option’s value:

        - The elements of the manifest.project-filter value are checked
          against the project’s name. If the regular expression in the
          element matches the project’s name, then the project is active
          or inactive depending on if the element begins with + or -
          respectively.
        - If multiple elements have regular expressions matching the
          project’s name, the last element which has a match determines
          the result.
        - This function returns True or False if the project is active or
          inactive according to these rules.

        The manifest.project-filter value that was set at the time
        this Manifest object was constructed is used.

        Otherwise, the return value depends on whether the project has
        any groups, and if so, whether they are enabled:

        - Projects with empty ‘project.groups’ lists are always active,
          and this function returns True for such projects.
        - If ‘project.groups’ is not empty, and any group in it is
          enabled by this manifest’s ‘group-filter:’ list (and the
          ‘manifest.group-filter’ local configuration option, if we
          have a workspace), this returns True.
        - Otherwise, i.e. if all of the project’s groups are disabled,
          this returns False.

        “Inactive” projects should generally be considered absent from
        the workspace for purposes like updating, listing, resolving
        imports, etc.

        Parameters:
        :   - **project** – project to check
            - **extra\_filter** – an optional additional group filter

    New in version 0.9.0.

    Changed in version 1.1.0: This respects the `manifest.project-filter` configuration
    option. See [Built-in Configuration Options](config.md#west-config-index).

*class* west.manifest.ImportFlag(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)
:   Bit flags for handling imports when resolving a manifest.

    Note that any “path-prefix:” values set in an “import:” still take
    effect for the project itself even when IGNORE or IGNORE\_PROJECTS are
    given. For example, in this manifest:

    ```text
    manifest:
      projects:
      - name: foo
        import:
          path-prefix: bar
    ```

    Project ‘foo’ has path ‘bar/foo’ regardless of whether IGNORE or
    IGNORE\_PROJECTS is given. This ensures the Project has the same path
    attribute as it normally would if imported projects weren’t being
    ignored.

    DEFAULT *= 0*
    :   The default value, 0, reads the file system to resolve
        “self: import:”, and runs git to resolve a “projects:” import.

    IGNORE *= 1*
    :   Ignore projects added via “import:” in “self:” and “projects:”

    FORCE\_PROJECTS *= 2*
    :   Always invoke importer callback for “projects:” imports

    IGNORE\_PROJECTS *= 4*
    :   Ignore projects added via “import:” : in “projects:” only;
        including any projects added via “import:” : in “self:”

*class* west.manifest.Project(*name: str*, *url: str*, *description: str | None = None*, *revision: str | None = None*, *path: str | PathLike | None = None*, *submodules: list[[west.manifest.Submodule](#west.manifest.Submodule)] | bool = False*, *clone\_depth: int | None = None*, *west\_commands: str | list[str] | None = None*, *topdir: str | PathLike | None = None*, *remote\_name: str | None = None*, *groups: list[str] | None = None*, *userdata: Any | None = None*)
:   Represents a project defined in a west manifest.

    Attributes:

    - `name`: project’s unique name
    - `description`: project’s description
    - `url`: project fetch URL
    - `revision`: revision to fetch from `url` when the
      project is updated
    - `path`: relative path to the project within the workspace
      (i.e. from `topdir` if that is set)
    - `abspath`: absolute path to the project in the native path name
      format (or `None` if `topdir` is)
    - `posixpath`: like `abspath`, but with slashes (`/`) as
      path separators
    - `clone_depth`: clone depth to fetch when first cloning the
      project, or `None` (the revision should not be a SHA
      if this is used)
    - `west_commands`: list of YAML files where extension commands in
      the project are declared
    - `topdir`: the top level directory of the west workspace
      the project is part of, or `None`
    - `remote_name`: the name of the remote which should be set up
      when the project is being cloned (default: ‘origin’)
    - `groups`: the project’s groups (as a list) as given in the manifest.
      If the manifest data contains no groups for the project, this is
      an empty list.
    - `submodules`: the project’s submodules configuration; either
      a list of Submodule objects, or a boolean.
    - `userdata`: the parsed ‘userdata’ field in the manifest, or None

    Changed in version 0.7.0: The *remote* attribute was removed. Its semantics could no longer
    be preserved when support for manifest `import` keys was added.

    New in version 0.7.0: The *remote\_name* and *name\_and\_path* attributes.

    Changed in version 0.8.0: The *west\_commands* attribute is now always a list. In previous
    releases, it could be a string or `None`.

    New in version 0.9.0: The *group\_filter* and *submodules* attributes.

    New in version 0.12.0: The *userdata* attribute.

    New in version 1.2.0: The *description* attribute.

    Constructor:

    \_\_init\_\_(*name: str*, *url: str*, *description: str | None = None*, *revision: str | None = None*, *path: str | PathLike | None = None*, *submodules: list[[west.manifest.Submodule](#west.manifest.Submodule)] | bool = False*, *clone\_depth: int | None = None*, *west\_commands: str | list[str] | None = None*, *topdir: str | PathLike | None = None*, *remote\_name: str | None = None*, *groups: list[str] | None = None*, *userdata: Any | None = None*)
    :   Project constructor.

        If *topdir* is `None`, then absolute path attributes
        (`abspath` and `posixpath`) will also be `None`.

        Parameters:
        :   - **name** – project’s `name:` attribute in the manifest
            - **description** – project’s description or None
            - **url** – fetch URL
            - **revision** – fetch revision
            - **path** – path (relative to topdir), or None for *name*
            - **submodules** – submodules to pull within the project
            - **clone\_depth** – depth to use for initial clone
            - **west\_commands** – path to a west commands specification YAML
              file in the project, relative to its base directory,
              or list of these
            - **topdir** – the west workspace’s top level directory
            - **remote\_name** – the name of the remote which should be
              set up if the project is being cloned (default: ‘origin’)
            - **groups** – a list of groups found in the manifest data for
              the project, after conversion to str and validation.

    Changed in version 0.8.0: The *path* and *topdir* parameters can now be any `os.PathLike`.

    Changed in version 0.7.0: The parameters were incompatibly changed from previous versions.

    Methods:

    as\_dict() → dict
    :   Return a representation of this object as a dict, as it
        would be parsed from an equivalent YAML manifest.

    New in version 0.7.0.

    git(*cmd: str | list[str]*, *extra\_args: Iterable[str] = ()*, *capture\_stdout: bool = False*, *capture\_stderr: bool = False*, *check: bool = True*, *cwd: str | PathLike | None = None*) → CompletedProcess
    :   Run a git command in the project repository.

        Parameters:
        :   - **cmd** – git command as a string (or list of strings)
            - **extra\_args** – sequence of additional arguments to pass to
              the git command (useful mostly if *cmd* is a string).
            - **capture\_stdout** – if True, git’s standard output is
              captured in the `CompletedProcess` instead of being
              printed.
            - **capture\_stderr** – Like *capture\_stdout*, but for standard
              error. Use with caution: this may prevent error messages
              from being shown to the user.
            - **check** – if given, `subprocess.CalledProcessError` is
              raised if git finishes with a non-zero return code
            - **cwd** – directory to run git in (default: `self.abspath`)

    Changed in version 0.6.1: The *capture\_stderr* kwarg.

    Changed in version 0.7.0: The (now removed) `Project.format` method is no longer called on
    arguments.

    sha(*rev: str*, *cwd: str | PathLike | None = None*) → str
    :   Get the SHA for a project revision.

        Parameters:
        :   - **rev** – git revision (HEAD, v2.0.0, etc.) as a string
            - **cwd** – directory to run command in (default:
              self.abspath)

    Changed in version 0.7.0: Standard error is now captured.

    is\_ancestor\_of(*rev1: str*, *rev2: str*, *cwd: str | PathLike | None = None*) → bool
    :   Check if ‘rev1’ is an ancestor of ‘rev2’ in this project.

        Returns True if rev1 is an ancestor commit of rev2 in the
        given project; rev1 and rev2 can be anything that resolves to
        a commit. (If rev1 and rev2 refer to the same commit, the
        return value is True, i.e. a commit is considered an ancestor
        of itself.) Returns False otherwise.

        Parameters:
        :   - **rev1** – commit that could be the ancestor of *rev2*
            - **rev2** – commit that could be a descendant or *rev1*
            - **cwd** – directory to run command in (default:
              `self.abspath`)

    Changed in version 0.8.0: The *cwd* parameter can now be any `os.PathLike`.

    is\_cloned(*cwd: str | PathLike | None = None*) → bool
    :   Returns `True` if `self.abspath` looks like a git
        repository’s top-level directory, and `False` otherwise.

        Parameters:
        :   **cwd** – directory to run command in (default:
            `self.abspath`)

    Changed in version 0.8.0: The *cwd* parameter can now be any `os.PathLike`.

    New in version 0.6.1.

    is\_up\_to\_date\_with(*rev: str*, *cwd: str | PathLike | None = None*) → bool
    :   Check if the project is up to date with *rev*, returning
        `True` if so.

        This is equivalent to `is_ancestor_of(rev, 'HEAD',
        cwd=cwd)`.

        Parameters:
        :   - **rev** – base revision to check if project is up to date
              with.
            - **cwd** – directory to run command in (default:
              `self.abspath`)

    Changed in version 0.8.0: The *cwd* parameter can now be any `os.PathLike`.

    is\_up\_to\_date(*cwd: str | PathLike | None = None*) → bool
    :   Check if the project HEAD is up to date with the manifest.

        This is equivalent to `is_up_to_date_with(self.revision,
        cwd=cwd)`.

        Parameters:
        :   **cwd** – directory to run command in (default:
            `self.abspath`)

    Changed in version 0.8.0: The *cwd* parameter can now be any `os.PathLike`.

    read\_at(*path: str | PathLike*, *rev: str | None = None*, *cwd: str | PathLike | None = None*) → bytes
    :   Read file contents in the project at a specific revision.

        Parameters:
        :   - **path** – relative path to file in this project
            - **rev** – revision to read *path* from (default: `self.revision`)
            - **cwd** – directory to run command in (default: `self.abspath`)

    Changed in version 0.8.0: The *cwd* parameter can now be any `os.PathLike`.

    New in version 0.7.0.

    listdir\_at(*path: str | PathLike*, *rev: str | None = None*, *cwd: str | PathLike | None = None*, *encoding: str | None = None*) → list[str]
    :   List of directory contents in the project at a specific revision.

        The return value is the directory contents as a list of files and
        subdirectories.

        Parameters:
        :   - **path** – relative path to file in this project
            - **rev** – revision to read *path* from (default: `self.revision`)
            - **cwd** – directory to run command in (default: `self.abspath`)
            - **encoding** – directory contents encoding (default: ‘utf-8’)

    Changed in version 0.8.0: The *cwd* parameter can now be any `os.PathLike`.

    New in version 0.7.0.

*class* west.manifest.ManifestProject(*path: str | PathLike | None = None*, *west\_commands: str | list[str] | None = None*, *topdir: str | PathLike | None = None*, *userdata: Any | None = None*)
:   Represents the manifest repository as a Project.

    Meaningful attributes:

    - `name`: the string `"manifest"`
    - `topdir`: the top level directory of the west workspace
      the manifest project controls, or `None`
    - `path`: relative path to the manifest repository within the
      workspace, or `None` (i.e. from `topdir` if that is set)
    - `abspath`: absolute path to the manifest repository in the
      native path name format (or `None` if `topdir` is)
    - `posixpath`: like `abspath`, but with slashes (`/`) as
      path separators
    - `west_commands`:`west_commands:` key in the manifest’s
      `self:` map. This may be a list of such if the self
      section imports multiple additional files with west commands.
    - `userdata`: the parsed ‘userdata’ field under self in the manifest file

    Other readable attributes included for Project compatibility:

    - `url`: the empty string; the west manifest is not
      version-controlled by west itself, even though ‘west init’
      can fetch a manifest repository from a Git remote
    - `revision`: `"HEAD"`
    - `clone_depth`: `None`, because there’s no URL
    - `groups`: the empty list

    A limited subset of Project methods is supported.
    Results for calling others are not specified.

    Changed in version 0.8.0: The *url* attribute is now the empty string instead of `None`.
    The *abspath* attribute is created using `os.path.abspath()`
    instead of `os.path.realpath()`, improving support for symbolic links.

    as\_dict() → dict
    :   Return a representation of this object as a dict, as it would be
        parsed from an equivalent YAML manifest.

New in version 0.6.0.

*class* west.manifest.Submodule(*path: str*, *name: str | None = None*)
:   Represents a Git submodule within a project.

New in version 0.9.0.

### [Exceptions](#id17)

*class* west.configuration.MalformedConfig
:   Bases: `Exception`

    The west configuration was malformed.

*class* west.manifest.MalformedManifest
:   Bases: `Exception`

    Manifest parsing failed due to invalid data.

*class* west.manifest.ManifestVersionError(*version: str*, *file: str | PathLike | None = None*)
:   Bases: `Exception`

    The manifest required a version of west more recent than the
    current version.

    Changed in version 0.8.0: The *file* argument can now be any `os.PathLike`.

*class* west.manifest.ManifestImportFailed(*project: [Project](#west.manifest.Project) | None*, *imp: Any*)
:   Bases: `Exception`

    An operation required to resolve a manifest failed.

    Attributes:

    - `project`: the Project instance with the missing manifest data;
      None if it’s from the manifest via “manifest: self: import:”
    - `imp`: the parsed YAML data whose import was requested

    Changed in version 0.8.0: The *filename* argument can now be any `os.PathLike`.

    Changed in version 0.13.0: The *filename* argument was renamed *imp*, and can now take any value.

## [west.util](#id18)

Miscellaneous utilities.

### [Functions](#id19)

west.util.west\_dir(*start: str | PathLike | None = None*) → str
:   Returns the absolute path of the workspace’s .west directory.

    Starts the search from the start directory, and goes to its
    parents. If the start directory is not specified, the current
    directory is used.

    Raises WestNotFound if no .west directory is found.

    Changed in version 0.8.0: The *start* parameter can be any `os.PathLike`.

west.util.west\_topdir(*start: str | PathLike | None = None*, *fall\_back: bool = True*) → str
:   Like west\_dir(), but returns the path to the parent directory of the .west/
    directory instead, where project repositories are stored

    Changed in version 0.8.0: The *start* parameter can be any `os.PathLike`.

### [Exceptions](#id20)

*class* west.util.WestNotFound
:   Bases: `RuntimeError`

    Neither the current directory nor any parent has a west workspace.
