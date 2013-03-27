# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls.defaults import patterns, url

from .views import IndexView, WinServices, CreateWinDCView, DetailServiceView
from .views import Wizard
from .forms import WizardFormServiceType, WizardFormConfiguration

VIEW_MOD = 'openstack_dashboard.dashboards.project.windc.views'

urlpatterns = patterns(VIEW_MOD,
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^create$',
        Wizard.as_view([WizardFormServiceType, WizardFormConfiguration]),
        name='create'),
    url(r'^create_dc$', CreateWinDCView.as_view(), name='create_dc'),
    url(r'^(?P<data_center_id>[^/]+)/$', WinServices.as_view(),
        name='services'),
    url(r'^(?P<service_id>[^/]+)/$', DetailServiceView.as_view(),
        name='service_details')
)
