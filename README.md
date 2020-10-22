# nephelaiio.cassandra

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-cassandra.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-cassandra)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.cassandra-blue.svg)](https://galaxy.ansible.com/nephelaiio/cassandra/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/cassandra) to install and configure cassandra

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Dependencies

By default this role does not depend on any external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

## Example Playbook

```
- hosts: servers
  roles:
     - role: nephelaiio.cassandra
       cassandra_package_state: latest
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):
  * CentOS 7

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
