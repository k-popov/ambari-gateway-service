"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import os
from resource_management.core import shell
from resource_management.core.resources.system import Execute, Directory, File
from resource_management.core.source import InlineTemplate
from resource_management.libraries.script import Script
from resource_management.core.logger import Logger

class Dms(Script):

    def install(self, env):
        import params
        Logger.info('Install discounts management service node')
        env.set_params(params)
        temp_directory = '/tmp/dms_rpm/'
        rpm_file_name = os.path.basename(params.rpm_gs_location)
        Directory(temp_directory.rstrip(os.path.sep), action='delete')
        Directory(temp_directory.rstrip(os.path.sep), action='create')
        Execute(('gsutil', 'cp', params.rpm_gs_location, temp_directory))
        Execute(('rpm', '-Uvh', os.path.join(temp_directory, rpm_file_name)))
        self.configure(env)


    def configure(self, env, upgrade_type=None, config_dir=None):
        import params
        env.set_params(params)
        Logger.info("Create discounts management service environment file.")
        File('/etc/default/discounts-management-service',
             mode=0644,
             content=InlineTemplate(params.gateway_env_template))

    def stop(self, env, upgrade_type=None):
        import params
        Logger.info('Stop DMS')
        env.set_params(params)
        Execute(('systemctl', 'stop', 'discounts-management-service'))

    def start(self, env, upgrade_type=None):
        import params
        Logger.info('Start DMS')
        env.set_params(params)
        Execute(('systemctl', 'start', 'discounts-management-service'))

    def status(self, env):
        import params
        Logger.info('Status check DMS')
        env.set_params(params)
        Execute(('systemctl', 'status', 'discounts-management-service'))

    def restart(self, env):
        import params
        Logger.info('Restart DMS')
        env.set_params(params)
        Execute(('systemctl', 'restart', 'discounts-management-service'))


if __name__ == "__main__":
    Dms().execute()
