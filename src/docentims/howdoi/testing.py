# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import docentims.howdoi


class DocentimsHowdoiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=docentims.howdoi)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'docentims.howdoi:default')


DOCENTIMS_HOWDOI_FIXTURE = DocentimsHowdoiLayer()


DOCENTIMS_HOWDOI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DOCENTIMS_HOWDOI_FIXTURE,),
    name='DocentimsHowdoiLayer:IntegrationTesting'
)


DOCENTIMS_HOWDOI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DOCENTIMS_HOWDOI_FIXTURE,),
    name='DocentimsHowdoiLayer:FunctionalTesting'
)


DOCENTIMS_HOWDOI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DOCENTIMS_HOWDOI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DocentimsHowdoiLayer:AcceptanceTesting'
)
