# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.desktopvirtualization.aio import DesktopVirtualizationMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDesktopVirtualizationMgmtUserSessionsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DesktopVirtualizationMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_host_pool(self, resource_group):
        response = self.client.user_sessions.list_by_host_pool(
            resource_group_name=resource_group.name,
            host_pool_name="str",
            api_version="2024-04-03",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.user_sessions.get(
            resource_group_name=resource_group.name,
            host_pool_name="str",
            session_host_name="str",
            user_session_id="str",
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_delete(self, resource_group):
        response = await self.client.user_sessions.delete(
            resource_group_name=resource_group.name,
            host_pool_name="str",
            session_host_name="str",
            user_session_id="str",
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.user_sessions.list(
            resource_group_name=resource_group.name,
            host_pool_name="str",
            session_host_name="str",
            api_version="2024-04-03",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_disconnect(self, resource_group):
        response = await self.client.user_sessions.disconnect(
            resource_group_name=resource_group.name,
            host_pool_name="str",
            session_host_name="str",
            user_session_id="str",
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_send_message(self, resource_group):
        response = await self.client.user_sessions.send_message(
            resource_group_name=resource_group.name,
            host_pool_name="str",
            session_host_name="str",
            user_session_id="str",
            api_version="2024-04-03",
        )

        # please add some check logic here by yourself
        # ...
