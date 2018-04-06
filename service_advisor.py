#!/usr/bin/env python

import os
import imp
import traceback

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STACKS_DIR = os.path.join(SCRIPT_DIR, '../../../../')
PARENT_FILE = os.path.join(STACKS_DIR, 'service_advisor.py')

try:
    with open(PARENT_FILE, 'rb') as fp:
        service_advisor = imp.load_module('service_advisor', fp, PARENT_FILE, ('.py', 'rb', imp.PY_SOURCE))
except Exception as e:
    traceback.print_exc()
    print 'Failed to load parent'

class GATEWAYServiceAdvisor(service_advisor.ServiceAdvisor):
    def getServiceConfigurationRecommendations(self, configurations, clusterSummary, services, hosts):
        DEFAULT_PROPERTIES = {
            'rpm_gs_location': 'gs://mlsandbox-gs-bucket/repository/gateway/discounts-management-service-1.0-1522737814674.noarch.rpm',
            'gateway_http_port': '9090'
        }
        if 'gateway-env' in services['configurations']:
            putGatewayEnvProperty = self.putProperty(configurations, 'gateway-env', services)
            for prop, def_value in DEFAULT_PROPERTIES.iteritems():
                if prop not in services['configurations']['gateway-env']['properties']:
                    putGatewayEnvProperty(prop, def_value)
