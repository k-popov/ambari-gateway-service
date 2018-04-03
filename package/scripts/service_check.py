#!/usr/bin/env python
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
from __future__ import print_function

import time

from resource_management.core.resources.system import Execute
from resource_management.core.exceptions import ExecutionFailed
from resource_management.libraries.script import Script
from resource_management.core.logger import Logger

class ServiceCheck(Script):

    def service_check(self, env):
        import params
        check_url = 'http://localhost:{0}/'.format(params.gateway_http_port)
        max_checks = 18
        checks_done = 0
        env.set_params(params)
        Logger.info("Running gateway service check")
        while True:
            try:
                Execute(('curl', '--fail', '--silent', check_url))
                break
            except ExecutionFailed as ex:
                Logger.info('Service check failed: {0}'.format(ex.exception_message))
                if checks_done < max_checks:
                    checks_done += 1
                    time.sleep(10)
                else:
                    raise ex
            except:
                raise
        Logger.info("Gateway service check successful")
        exit(0)

if __name__ == "__main__":
    ServiceCheck().execute()
