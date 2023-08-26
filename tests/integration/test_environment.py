"""Tests the integration test plugin
"""
import pytest

from pytest_porringer.mock.environment import MockEnvironment
from pytest_porringer.tests import EnvironmentIntegrationTests


class TestCPPythonEnvironment(EnvironmentIntegrationTests[MockEnvironment]):
    """The tests for the Mock environment"""

    @pytest.fixture(name="plugin_type", scope="session")
    def fixture_plugin_type(self) -> type[MockEnvironment]:
        """A required testing hook that allows type generation

        Returns:
            An overridden environment type
        """
        return MockEnvironment
