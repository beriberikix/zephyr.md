---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/west/basics.html
original_path: develop/west/basics.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Basics

This page introduces west’s basic concepts and provides references to further
reading.

West’s built-in commands allow you to work with *projects* (Git
repositories) under a common *workspace* directory.

## Example workspace

If you’ve followed the upstream Zephyr getting started guide, your
workspace looks like this:

```text
zephyrproject/                 # west topdir
├── .west/                     # marks the location of the topdir
│   └── config                 # per-workspace local configuration file
│
│   # The manifest repository, never modified by west after creation:
├── zephyr/                    # .git/ repo
│   ├── west.yml               # manifest file
│   └── [... other files ...]
│
│   # Projects managed by west:
├── modules/
│   └── lib/
│       └── zcbor/             # .git/ project
├── net-tools/                 # .git/ project
└── [ ... other projects ...]
```

## Workspace concepts

Here are the basic concepts you should understand about this structure.
Additional details are in [Workspaces](workspaces.md#west-workspaces).

topdir
:   Above, `zephyrproject` is the name of the workspace’s top level
    directory, or *topdir*. (The name `zephyrproject` is just an example
    – it could be anything, like `z`, `my-zephyr-workspace`, etc.)

    You’ll typically create the topdir and a few other files and directories
    using [west init](#west-init-basics).

.west directory
:   The topdir contains the `.west` directory. When west needs to find
    the topdir, it searches for `.west`, and uses its parent directory.
    The search starts from the current working directory (and starts again from
    the location in the [`ZEPHYR_BASE`](../env_vars.md#envvar-ZEPHYR_BASE) environment variable as a
    fallback if that fails).

configuration file
:   The file `.west/config` is the workspace’s [local configuration
    file](config.md#west-config).

manifest repository
:   Every west workspace contains exactly one *manifest repository*, which is a
    Git repository containing a *manifest file*. The location of the manifest
    repository is given by the [manifest.path configuration option](config.md#west-config-index) in the local configuration file.

    For upstream Zephyr, `zephyr` is the manifest repository, but you can
    configure west to use any Git repository in the workspace as the manifest
    repository. The only requirement is that it contains a valid manifest file.
    See [Topologies supported](workspaces.md#west-topologies) for information on other options, and
    [West Manifests](manifest.md#west-manifests) for details on the manifest file format.

manifest file
:   The manifest file is a YAML file that defines *projects*, which are the
    additional Git repositories in the workspace managed by west. The manifest
    file is named `west.yml` by default; this can be overridden using the
    `manifest.file` local configuration option.

    You use the [west update](#west-update-basics) command to update the
    workspace’s projects based on the contents of the manifest file.

projects
:   Projects are Git repositories managed by west. Projects are defined in the
    manifest file and can be located anywhere inside the workspace. In the above
    example workspace, `zcbor` and `net-tools` are projects.

    By default, the Zephyr [build system](../../build/index.md#build-overview) uses west to get
    the locations of all the projects in the workspace, so any code they contain
    can be used as [Modules (External projects)](../modules.md#modules). Note however that modules and projects
    [are conceptually different](../modules.md#modules-vs-projects).

extensions
:   Any repository known to west (either the manifest repository or any project
    repository) can define [Extensions](extensions.md#west-extensions). Extensions are extra west
    commands you can run when using that workspace.

    The zephyr repository uses this feature to provide Zephyr-specific commands
    like [west build](build-flash-debug.md#west-building). Defining these as extensions keeps
    west’s core agnostic to the specifics of any workspace’s Zephyr version,
    etc.

ignored files
:   A workspace can contain additional Git repositories or other files and
    directories not managed by west. West basically ignores anything in the
    workspace except `.west`, the manifest repository, and the projects
    specified in the manifest file.

## west init and west update

The two most important workspace-related commands are `west init` and `west
update`.

### `west init` basics

This command creates a west workspace.

Important

West doesn’t change your manifest repository contents after `west init` is
run. Use ordinary Git commands to pull new versions, etc.

You will typically run it once, like this:

```shell
west init -m https://github.com/zephyrproject-rtos/zephyr --mr v2.5.0 zephyrproject
```

This will:

1. Create the topdir, `zephyrproject`, along with
   `.west` and `.west/config` inside it
2. Clone the manifest repository from
   [https://github.com/zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr), placing it into
   `zephyrproject/zephyr`
3. Check out the `v2.5.0` git tag in your local zephyr clone
4. Set `manifest.path` to `zephyr` in `.west/config`
5. Set `manifest.file` to `west.yml`

Your workspace is now almost ready to use; you just need to run `west update`
to clone the rest of the projects into the workspace to finish.

For more details, see [west init](built-in.md#west-init).

### `west update` basics

This command makes sure your workspace contains Git repositories matching the
projects in the manifest file.

Important

Whenever you check out a different revision in your manifest repository, you
should run `west update` to make sure your workspace contains the
project repositories the new revision expects.

The `west update` command reads the manifest file’s contents by:

1. Finding the topdir. In the `west init` example above, that
   means finding `zephyrproject`.
2. Loading `.west/config` in the topdir to read the `manifest.path`
   (e.g. `zephyr`) and `manifest.file` (e.g. `west.yml`) options.
3. Loading the manifest file given by these options (e.g.
   `zephyrproject/zephyr/west.yml`).

It then uses the manifest file to decide where missing projects should be
placed within the workspace, what URLs to clone them from, and what Git
revisions should be checked out locally. Project repositories which already
exist are updated in place by fetching and checking out their respective Git
revisions in the manifest file.

For more details, see [west update](built-in.md#west-update).

## Other built-in commands

See [Built-in commands](built-in.md#west-built-in-cmds).

## Zephyr Extensions

See the following pages for information on Zephyr’s extension commands:

- [Building, Flashing and Debugging](build-flash-debug.md#west-build-flash-debug)
- [Signing Binaries](sign.md#west-sign)
- [Additional Zephyr extension commands](zephyr-cmds.md#west-zephyr-ext-cmds)
- [Enabling shell completion](install.md#west-shell-completion)

## Troubleshooting

See [Troubleshooting West](troubleshooting.md#west-troubleshooting).
