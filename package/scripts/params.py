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

from resource_management.libraries.script import Script

# server configurations
config = Script.get_config()

rpm_gs_location = config['configurations']['dms-env']['rpm_gs_location']
elastic_url = config['configurations']['dms-env']['elastic_url']
price_url = config['configurations']['dms-env']['price_url']
client_id = config['configurations']['dms-env']['client_id']
application_secret = config['configurations']['dms-env']['application_secret']
gateway_http_port = config['configurations']['dms-env']['gateway_http_port']

catalog_index = config['configurations']['dms-env']['catalog_index']
discounts_index = config['configurations']['dms-env']['discounts_index']
campaigns_index = config['configurations']['dms-env']['campaigns_index']
gateway_env_template = config['configurations']['dms-env']['content']
