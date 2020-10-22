import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def cqlsh(u, p, c):
    return f"cqlsh -u {u} -p {p} -e '{c}'"


def hostname(host):
    return host.ansible.get_variables()['inventory_hostname']


def test_status(host):
    assert host.command('nodetool status').rc == 0


def test_roles(host):
    assert host.command(cqlsh('cassandra', 'cassandra', 'quit;')).rc == 0
    assert host.command(cqlsh('topsecret', 'topsecret', 'quit;')).rc == 0
    assert host.command(cqlsh('nosecret', 'nosecret', 'quit;')).rc == 0
