"""This script generates devinfo files for the test suite.

If you have new, yet unsupported device or a device with no devinfo file under swidget/tests/fixtures,
feel free to run this script and create a PR to add the file to the repository.

Executing this script will several modules and methods one by one,
and finally execute a query to query all of them at once.
"""

import json
import logging

import asyncclick as click
from aiohttp import ClientSession, TCPConnector


@click.command()
@click.argument("host")
@click.option("-p", "--password", is_flag=False)
@click.option("-d", "--debug", is_flag=True)
async def cli(host, password, debug):
    """Generate devinfo file for given device."""
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    headers = {"x-secret-key": password}
    connector = TCPConnector(force_close=True)
    _session = ClientSession(headers=headers, connector=connector)
    async with _session.get(
        url=f"https://{host}/api/v1/summary",
        ssl=False,
    ) as response:
        summary = await response.json()

    click.echo(click.style("== Summary info ==", bold=True))
    click.echo(json.dumps(summary, sort_keys=True, indent=2))
    click.echo()
    async with _session.get(url=f"https://{host}/api/v1/state", ssl=False) as response:
        state = await response.json()

    click.echo(click.style("== State info ==", bold=True))
    click.echo(json.dumps(state, sort_keys=True, indent=2))

    final = {"state": state, "summary": summary}
    save_to = f"{summary['model']}_{summary['version']}.json"
    save = click.prompt(f"Do you want to save the above content to {save_to} (y/n)")
    if save == "y":
        click.echo(f"Saving info to {save_to}")

        with open(save_to, "w") as f:
            json.dump(final, f, sort_keys=True, indent=2)
            f.write("\n")
    else:
        click.echo("Not saving.")


if __name__ == "__main__":
    cli()
