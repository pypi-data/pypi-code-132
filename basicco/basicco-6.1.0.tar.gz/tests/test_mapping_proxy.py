from __future__ import absolute_import, division, print_function

import pytest  # noqa

from basicco.mapping_proxy import MappingProxyType


def test_wrap_dict():
    internal_dict = {"foo": "bar"}
    proxy_dict = MappingProxyType(internal_dict)
    assert proxy_dict["foo"] == "bar"

    with pytest.raises(TypeError):
        proxy_dict["foo"] = "foo"

    with pytest.raises(TypeError):
        del proxy_dict["foo"]

    internal_dict["foo"] = "foo"
    assert proxy_dict["foo"] == "foo"

    del internal_dict["foo"]
    assert "foo" not in proxy_dict


if __name__ == "__main__":
    pytest.main()
