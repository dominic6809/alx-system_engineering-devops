# 0x0A. Configuration management

# Puppet Project

## Overview

This project contains Puppet manifests for various tasks including creating files, installing packages, and managing processes. 

## Manifests

### school.pp

This manifest ensures that a file named `/tmp/school` exists with specific content, permissions, ownership, and group.

## Usage

### Ensure puppet and puppet-lint are installed on your system.
### Clone this repository or download the manifest files.
### Apply each manifest as needed using the following command

:sudo puppet apply <manifest_file>
For example, to apply the school.pp manifest:

sudo puppet apply school.pp

## Requirements
Ubuntu 20.04 LTS
Puppet
puppet-lint version 2.1.1
