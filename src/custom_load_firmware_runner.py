from cloudshell.networking.cisco.iosxr.flows.cisco_iosxr_load_firmware_flow import CiscoIOSXRLoadFirmwareFlow
from cloudshell.networking.cisco.iosxr.runners.cisco_iosxr_firmware_runner import CiscoIOSXRFirmwareRunner


class CustomCiscoIOSXRLoadFirmwareFlow(CiscoIOSXRLoadFirmwareFlow):
    def __init__(self, cli_handler, logger, packages_to_install, file_system=None):
        # Override init, pass file_system into into the CiscoLoadFirmwareFlow grandparent class"""
        super(CiscoIOSXRLoadFirmwareFlow, self).__init__(cli_handler, logger, file_system)

        # Rest of Init is same as original CiscoIOSXRLoadFirmwareFlow Parent Class
        self._packages_to_add = []
        self._result_dict = {}
        self._sync = None
        self._is_old_iosxr = False
        self._cmd_admin_prefix = None
        if not packages_to_install or packages_to_install == "*" or packages_to_install.lower() == "all":
            self._packages_to_add = []
        else:
            self._packages_to_add = packages_to_install.lower().split(" ")


class CustomFirmwareRunner(CiscoIOSXRFirmwareRunner):
    def __init__(self, logger, cli_handler, features_to_install, file_system=None):
        super(CustomFirmwareRunner, self).__init__(logger, cli_handler, features_to_install)
        self.file_system = file_system

    @property
    def load_firmware_flow(self):
        return CustomCiscoIOSXRLoadFirmwareFlow(self.cli_handler,
                                                self._logger,
                                                self._features_to_install,
                                                self.file_system)
