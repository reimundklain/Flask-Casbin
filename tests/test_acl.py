# -*- coding: utf-8 -*-

__author__ = "Reimund Klain"
__email__ = "reimund.klain@condevtec.de"


def test_acl(acl):
    assert acl.enforce("user:alice", "data:1", "read") is True
    assert acl.enforce("user:alice", "data:1", "write") is False
    assert acl.enforce("user:alice", "data:2", "read") is False
    assert acl.enforce("user:alice", "data:2", "write") is False

    assert acl.enforce("user:bob", "data:1", "read") is False
    assert acl.enforce("user:bob", "data:1", "write") is False
    assert acl.enforce("user:bob", "data:2", "read") is False
    assert acl.enforce("user:bob", "data:2", "write") is True
