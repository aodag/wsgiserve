import pytest


class TestCommand(object):
    @pytest.fixture
    def target(self):
        from wsgiserve import Command
        return Command

    def test_init(self, target):
        config = "test_config.ini"
        reload = False
        command = target(config, reload)
        assert command.config == config
        assert not command.reload


    @pytest.mark.parametrize(
        "config_vars,defaults",
        [
            ([], {}),
            (["var1=x"], {"var1": "x"}),
            (["var1=x", "x"], {"var1": "x"}),
            (["var1=x", "var2=y"], {"var1": "x", "var2": "y"}),
        ]
    )
    def test_get_defaults(self, target, config_vars, defaults):
        config = "test_config.ini"
        reload = False
        command = target(config, reload, config_vars)
        assert command.get_defaults() == defaults
