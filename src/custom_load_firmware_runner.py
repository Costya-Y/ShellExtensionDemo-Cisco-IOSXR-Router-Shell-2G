from cloudshell.networking.cisco.iosxr.flows.cisco_iosxr_load_firmware_flow import CiscoIOSXRLoadFirmwareFlow
from cloudshell.networking.cisco.iosxr.runners.cisco_iosxr_firmware_runner import CiscoIOSXRFirmwareRunner


class CustomCiscoIOSXRLoadFirmwareFlow(CiscoIOSXRLoadFirmwareFlow):
    def __init__(self, cli_handler, logger, packages_to_install, file_system=None):
        # Override init, pass file_system into into the CiscoLoadFirmwareFlow grandparent class"""
        super(CustomCiscoIOSXRLoadFirmwareFlow, self).__init__(cli_handler, logger, packages_to_install)
        self._file_system = file_system

    def execute_flow(self, path, vrf, timeout):
        # Copy and make all required changes from the base class, or call method from parent class:
        # super(CustomCiscoIOSXRLoadFirmwareFlow, self).execute_flow(path, vrf, timeout)
        pass


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
