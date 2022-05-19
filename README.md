# Spack for Singular/GPI-Space

This is a repo containing spack scripts for installing various projects in the
Singular/GPI-Space framework

To install packages described here, the user must first install Spack itself,
which entails cloning the Spack repo and running a bootstrapping script

## Installing Spack
Assume you want to clone spack and these scripts to some directory
`software-root`:

```bash
export software_ROOT=<software-root>
```

Spack may now be cloned there, by running:

```bash
git clone https://github.com/spack/spack.git $software_ROOT/spack
```

For the most predictable experience, check out verison v0.17 of spack:
```bash
cd $software_ROOT/spack
git checkout v0.17
cd -
```

Run the setup script in the spack repo:

```bash
. $software_ROOT/spack/share/spack/setup-env.sh
```
Note, this setup needs to be run for every new session in which the user wishes
to use spack.

When cloning spack initially, Spack still needs to boostrap clingo. This can be
done by concretizing any spec, for example
```
spack spec zlib
```
This may take some time.

## Adding this repo to Spack

Clone this repo

```bash
git clone                                                         \
    --depth 1                                                     \
    https://github.com/singular-gpispace/spack.git                \
    $software_ROOT/spack_packages
```

Add this repo to spack
```bash
spack repo add $software_ROOT/spack/spack_packages
```

## Installing packages
The user may no install any of the packages described in this repo, for instance

```bash
spack install pfd
```
Once the installation is done (which may take some time), the user needs to load
the installed package

```bash
spack load pfd
```

Please refer to the repos of the various projects on how to run them.