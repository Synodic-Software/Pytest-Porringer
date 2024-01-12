"""Shared data between the exposed fixtures"""

from abc import ABCMeta
from typing import LiteralString, cast

import pytest
from porringer_core.plugin_schema.environment import Environment, EnvironmentT
from porringer_core.schema import PluginT
from pytest_synodic.plugin import BaseTests as SynodicBaseTests
from pytest_synodic.plugin import IntegrationTests as SynodicBaseIntegrationTests
from pytest_synodic.plugin import UnitTests as SynodicBaseUnitTests

from pytest_porringer.variants import environment_variants


class BaseTests[PluginT](SynodicBaseTests, metaclass=ABCMeta):
    """Shared testing information for all plugin test classes."""

    @pytest.fixture(name="plugin_type", scope="session")
    def fixture_plugin_type(self) -> type[PluginT]:
        """A required testing hook that allows type generation"""

        raise NotImplementedError("Override this fixture")

    @pytest.fixture(name="plugin_group_name", scope="session")
    def fixture_plugin_group_name(self) -> LiteralString:
        """_summary_

        Returns:
            _description_
        """

        return "porringer"


class BaseIntegrationTests[PluginT](SynodicBaseIntegrationTests, metaclass=ABCMeta):
    """Integration testing information for all plugin test classes"""


class BaseUnitTests[PluginT](SynodicBaseUnitTests, metaclass=ABCMeta):
    """Unit testing information for all plugin test classes"""


class PluginTests[PluginT](BaseTests[PluginT], metaclass=ABCMeta):
    """Testing information for basic plugin test classes."""

    @staticmethod
    @pytest.fixture(
        name="plugin",
        scope="session",
    )
    def fixture_plugin(
        plugin_type: type[PluginT],
    ) -> PluginT:
        """Overridden plugin generator for creating a populated data plugin type

        Args:
            plugin_type: Plugin type
        Returns:
            A newly constructed provider
        """

        plugin = plugin_type()

        return plugin


class PluginIntegrationTests[PluginT](BaseIntegrationTests[PluginT], metaclass=ABCMeta):
    """Integration testing information for basic plugin test classes"""


class PluginUnitTests[PluginT](BaseUnitTests[PluginT], metaclass=ABCMeta):
    """Unit testing information for basic plugin test classes"""


class EnvironmentTests[EnvironmentT](PluginTests[EnvironmentT], metaclass=ABCMeta):
    """Shared functionality between the different testing categories"""

    @pytest.fixture(
        name="environment_type",
        scope="session",
        params=environment_variants,
    )
    def fixture_environment_type(self, request: pytest.FixtureRequest) -> type[Environment]:
        """Fixture defining all testable variations mock Environment

        Args:
            request: Parameterization list

        Returns:
            Variation of a Environment
        """
        environment_type = cast(type[Environment], request.param)

        return environment_type
