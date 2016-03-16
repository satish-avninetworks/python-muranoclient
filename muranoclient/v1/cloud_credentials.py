#    Copyright (c) 2013 Mirantis, Inc.
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

from muranoclient.common import base


class CloudCredential(base.Resource):
    """It involves the template resource.
    """
    def __repr__(self):
        return "<Cloud Credential %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class CloudCredentialManager(base.Manager):
    """It involves the template manager.
    """
    resource_class = CloudCredential

    def list(self):
        """It lists the Cloud Credentials.
        """
        return self._list('/v1/identity/cloudcredential', 'cloudcredential')

    def create(self, data):
        """It creates a environment template
        :param data: The environment template information.
        """
        return self._create('/v1/identity/cloudcredential', data)

    def update(self, id, name):
        """It updates the cloud credentials name .
        :param id: The Cloud credentials id.
        :param name: The name to be updated.
        """
        return self._update('/v1/identity/cloudcredential/{id}'.format(id=id),
                            data={'name': name})

    def delete(self, id):
        """It deletes an environment template name.
        :param env_template_id: The environment template ID.
        """
        return self._delete('/v1/identity/cloudcredential/{id}'.format(id=id))

    def get(self, id):
        """It gets information about an environment template name.
        :param env_template_id: The environment template ID.
        """
        return self._get("/v1/identity/cloudcredential/{id}".format(id=id))
