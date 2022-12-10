"""A module to provision the Swidget device to be managable locally."""
import time

import requests


def provision_wifi(ssid, network_password, secret_key):
    """Provision WiFi credentials to the Swidget host. Verify the changes were made."""
    payload = {"ssid": ssid, "password": network_password, "secretKey": secret_key}
    headers = {"x-secret-key": secret_key}
    url = "https://10.123.45.1/network"
    initial_provision = requests.post(url, data=payload, verify=False).json()
    print(f"Response from setting {initial_provision}")

    time.sleep(5)
    url = "https://10.123.45.1/network"
    verify_connection = requests.get(url, headers=headers, verify=False).json()
    print(f"Verification request data: {verify_connection}")
