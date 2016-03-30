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


class InstanceCredential(base.Resource):
    """It involves the template resource.
    """
    def __repr__(self):
        return "<Instance Credential %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class InstanceCredentialManager(base.Manager):
    """It involves the template manager.
    """
    resource_class = InstanceCredential

    def list(self):
        """It lists the Instance Credentials.
        """
        return self._list('/v1/identity/instancecredential',
                          'instancecredentials')

    def create(self, data):
        """It creates a Instance credential
        :param data: The Instance template information.
        """
        return self._create('/v1/identity/instancecredential', data)

    def update(self, inst_cred_id, name):
        """It updates the Instance credentials name .
        :param id: The Instance credentials id.
        :param name: The name to be updated.
        """
        return self._update('/v1/identity/instancecredential/{id}'
                            .format(id=inst_cred_id),
                            data={'name': name})

    def delete(self, inst_cred_id):
        """It deletes an Instance Credentials name.
        :param inst_cred_id: The instance credentials ID.
        """
        return self._delete('/v1/identity/instancecredential/{id}'
                            .format(id=inst_cred_id))

    def get(self, inst_cred_id):
        """It gets information about an Instance credentials.
        :param inst_cred_id: The Instance credentials ID.
        """
        return self._get("/v1/identity/instancecredential/{id}"
                         .format(id=inst_cred_id))
