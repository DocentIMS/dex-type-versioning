# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from docentims.howdoi.testing import DOCENTIMS_HOWDOI_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that docentims.howdoi is properly installed."""

    layer = DOCENTIMS_HOWDOI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if docentims.howdoi is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'docentims.howdoi'))

    def test_browserlayer(self):
        """Test that IDocentimsHowdoiLayer is registered."""
        from docentims.howdoi.interfaces import (
            IDocentimsHowdoiLayer)
        from plone.browserlayer import utils
        self.assertIn(IDocentimsHowdoiLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DOCENTIMS_HOWDOI_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['docentims.howdoi'])

    def test_product_uninstalled(self):
        """Test if docentims.howdoi is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'docentims.howdoi'))

    def test_browserlayer_removed(self):
        """Test that IDocentimsHowdoiLayer is removed."""
        from docentims.howdoi.interfaces import IDocentimsHowdoiLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDocentimsHowdoiLayer, utils.registered_layers())
