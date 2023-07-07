"""Run an example script to quickly test."""
import asyncio
import logging

from aiohttp import ClientSession
import datetime
import pysnooapi
from pysnooapi.errors import SnooError

_LOGGER = logging.getLogger()

EMAIL = "mzackoff@servicetitan.com"
PASSWORD = "Iloveaz1!"
ISSUE_COMMANDS = False

def print_info(device):
    print(f"      Device: {device.name}")
    print(f"      Device Online: {device.is_online}")
    print(f"      Device On: {device.is_on}")
    print(f"      Device ID: {device.device_id}")
    print(f"      Firmware Version: {device.firmware_version}")
    print(f"      Baby details: {device.baby}")
    print(f"      Session details: {device.session}")
    print(f"      Is on: {device.state != None}")
    print(f"      Current State: {device.state}")
    print("      ---------")

async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.DEBUG)
    async with ClientSession() as websession:
        try:
            # Create an API object:
            print(f"{EMAIL} {PASSWORD}")
            api = await pysnooapi.login(EMAIL, PASSWORD, websession)
            times = await api.get_session_stats_daily_for_account(datetime.date.today() - datetime.timedelta(days=1)
                                                                  , detailedLevels=True
                                                                  , levels=True)
            print(f"Account ID: {api.account.get('userId')}")
            print(f"Account Name: {api.account.get('givenName')}")
            print(f"Devices: {len(api.devices)}")
            if len(api.devices) != 0:
                print("  ---------------")
            for device in api.devices:
                # Get all devices listed with this account
                print_info(device=api.devices[device])
                print("  ------------------------------")

        except SnooError as err:
            _LOGGER.error("There was an error: %s", err)

asyncio.get_event_loop().run_until_complete(main())