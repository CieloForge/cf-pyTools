# src/currency/__main__.py
from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Optional

import click
import requests
from rich.console import Console
from rich.table import Table

console = Console()


@dataclass
class RateInfo:
    from_curr: str
    to_curr: str
    rate: float
    updated: str


def fetch_rate(from_curr: str, to_curr: str) -> Optional[RateInfo]:
    from_curr = from_curr.upper()
    to_curr = to_curr.upper()

    url = f"https://open.er-api.com/v6/latest/{from_curr}"

    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        data = resp.json()

        if data.get("result") != "success":
            console.print(f"[red]API error: {data.get('error-type', 'unknown')}[/red]")
            return None

        rate = data["rates"].get(to_curr)
        if rate is None:
            console.print(f"[red]Currency '{to_curr}' not supported[/red]")
            return None

        return RateInfo(
            from_curr=from_curr,
            to_curr=to_curr,
            rate=rate,
            updated=data.get("time_last_update_utc", "unknown time"),
        )

    except requests.RequestException as e:
        console.print(f"[red]Request failed: {e}[/red]")
        return None


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--list", "list_currencies", is_flag=True, help="Just list available currencies and exit"
)
@click.option(
    "--precise", is_flag=True, default=False, help="Show more decimal places in rate"
)
@click.argument("amount", type=float, required=False)
@click.argument("from_currency", type=str, required=False)
@click.argument("to_currency", type=str, required=False)
def convert(
    list_currencies: bool,
    precise: bool,
    amount: float,
    from_currency: str,
    to_currency: str,
):
    """Convert AMOUNT from FROM_CURRENCY to TO_CURRENCY.

    Example:
        currency 500 PHP USD
        currency 1200 USD JPY --precise
    """
    if list_currencies:
        console.print("[yellow]Supported currencies (partial list):[/yellow]")
        console.print("USD, EUR, GBP, JPY, PHP, KRW, CAD, AUD, INR, CNY, ...")
        console.print("[dim](fetches live from open.er-api.com — 170+ currencies)[/dim]")
        sys.exit(0)
    
    # Validate required arguments if not listing currencies
    if amount is None or from_currency is None or to_currency is None:
        console.print("[red]Error: Missing required arguments[/red]")
        console.print("Usage: currency AMOUNT FROM_CURRENCY TO_CURRENCY")
        console.print("Try 'currency --help' for more information.")
        sys.exit(1)

    rate_info = fetch_rate(from_currency, to_currency)

    if not rate_info:
        sys.exit(1)

    result = amount * rate_info.rate

    decimals = 6 if precise else 4

    from rich.box import MINIMAL
    table = Table(show_header=True, header_style="bold cyan", box=MINIMAL)
    table.add_column("From", justify="right")
    table.add_column("To", justify="right")
    table.add_column("Rate", justify="right")
    table.add_column("Result", justify="right", style="bold green")

    table.add_row(
        f"{amount:,.2f} {rate_info.from_curr}",
        rate_info.to_curr,
        f"1 {rate_info.from_curr} = {rate_info.rate:,.{decimals}f} {rate_info.to_curr}",
        f"{result:,.2f} {rate_info.to_curr}",
    )

    console.print(f"\n[grey50]Updated:[/] {rate_info.updated}")
    console.print(table)


if __name__ == "__main__":
    convert()