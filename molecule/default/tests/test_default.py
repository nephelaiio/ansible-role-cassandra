import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def hostname(host):
    return host.ansible.get_variables()['inventory_hostname']


def test_status(host):
    assert host.command('nodetool status').rc == 0
