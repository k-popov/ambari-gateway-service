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
from resource_management.core.resources.system import Execute, ExecuteScript, Directory
from resource_management.libraries.script import Script
from resource_management.core.logger import Logger

class Gateway(Script):

    def install(self, env):
        import params
#        env.set_params(params)
        Logger.info('Install gateway service node')
        temp_directory = '/tmp/gateway_rpm/'
        rpm_file_name = os.path.basename(params.rpm_gs_location)
        Directory(temp_directory, action='delete')
        Directory(temp_directory, action='create')
        Execute(command=('gsutil', 'cp', params.rpm_gs_location, temp_directory))
        Execute(command=('rpm', '-ivh', os.path.join(temp_directory, rpm_file_name)))

    def configure(self, env, upgrade_type=None, config_dir=None):
        import params
        env.set_params(params)
        Logger.info('Configure gateway node')

    def stop(self, env, upgrade_type=None):
        import params
        env.set_params(params)
        Logger.info('Stop gateway node')

    def start(self, env, upgrade_type=None):
        import params
        env.set_params(params)
        Logger.info('Start gateway node')
        self.configure(env)

    def status(self, env):
        import params
        env.set_params(params)
        Logger.info('Status check gateway node')

    def restart(self, env):
        import params
        env.set_params(params)
        Logger.info('Restart gateway node')
        self.configure(env)


if __name__ == "__main__":
    Gateway().execute()
