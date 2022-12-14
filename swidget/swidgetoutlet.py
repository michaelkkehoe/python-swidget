"""Module to represent a Swidget outlet."""
from swidget.swidgetdevice import DeviceType, SwidgetDevice


class SwidgetOutlet(SwidgetDevice):
    """Class to represent a Swidget Outlet/ Plug device."""

    def __init__(self, host, secret_key: str, ssl: bool, use_websockets: bool) -> None:
        super().__init__(
            host=host, secret_key=secret_key, ssl=ssl, use_websockets=use_websockets
        )
        self._device_type = DeviceType.Outlet
