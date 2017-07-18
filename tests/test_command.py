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
