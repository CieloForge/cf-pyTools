import click
import math
import re

@click.group()
def cli():
    """Profit Estimator CLI Tool - Compound Growth Calculator"""
    pass

# Period definitions with their corresponding number of occurrences per year
PERIOD_DEFINITIONS = {
    'yearly': 1,
    'year': 1,
    'annually': 1,
    'monthly': 12,
    'month': 12,
    'weekly': 52,
    'week': 52,
    'daily': 365,
    'day': 365,
    'hourly': 8760,
    'hour': 8760
}

# Textual number mappings (for patterns like "twice a day", "three times a week")
TEXTUAL_NUMBERS = {
    'once': 1,
    'one': 1,
    'twice': 2,
    'two': 2,
    'three': 3,
    'thrice': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12
}

def parse_period(period_str):
    """Parse period string and return (frequency, base_period, periods_per_year)"""
    # Remove extra whitespace and convert to lowercase
    period_str = period_str.strip().lower()
    
    # Match patterns like "twice a day", "three times a week", "daily", "monthly"
    
    # First, handle patterns with textual numbers
    for text_num, num in TEXTUAL_NUMBERS.items():
        # Look for patterns like "twice a day" or "twice per day" or "twice daily"
        patterns = [
            rf'{text_num}\s*a\s*(\w+)',
            rf'{text_num}\s*per\s*(\w+)', 
            rf'{text_num}\s*times?\s*a\s*(\w+)',
            rf'{text_num}\s*times?\s*per\s*(\w+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, period_str)
            if match:
                base_period = match.group(1)
                if base_period in PERIOD_DEFINITIONS:
                    base_periods_per_year = PERIOD_DEFINITIONS[base_period]
                    periods_per_year = num * base_periods_per_year
                    return num, base_period, periods_per_year
                # Also check if base period is in plural form
                if base_period + 'ly' in PERIOD_DEFINITIONS:
                    base_period = base_period + 'ly'
                    base_periods_per_year = PERIOD_DEFINITIONS[base_period]
                    periods_per_year = num * base_periods_per_year
                    return num, base_period, periods_per_year
    
    # Then, handle numeric frequency patterns
    numeric_patterns = [
        r'(\d+)\s*a\s*(\w+)',
        r'(\d+)\s*per\s*(\w+)',
        r'(\d+)\s*times?\s*a\s*(\w+)',
        r'(\d+)\s*times?\s*per\s*(\w+)'
    ]
    
    for pattern in numeric_patterns:
        match = re.search(pattern, period_str)
        if match:
            frequency = int(match.group(1))
            base_period = match.group(2)
            
            if base_period in PERIOD_DEFINITIONS:
                base_periods_per_year = PERIOD_DEFINITIONS[base_period]
                periods_per_year = frequency * base_periods_per_year
                return frequency, base_period, periods_per_year
                
            if base_period + 'ly' in PERIOD_DEFINITIONS:
                base_period = base_period + 'ly'
                base_periods_per_year = PERIOD_DEFINITIONS[base_period]
                periods_per_year = frequency * base_periods_per_year
                return frequency, base_period, periods_per_year
    
    # Handle simple period types (daily, monthly, etc.)
    if period_str in PERIOD_DEFINITIONS:
        return 1, period_str, PERIOD_DEFINITIONS[period_str]
    
    raise ValueError(f"Unknown period: {period_str}")

@cli.command()
@click.option('--initial', type=float, required=True, help='Initial investment amount (e.g., 1000.0)')
@click.option('--gain', type=float, required=True, help='Estimated % gain per period (e.g., 5 for 5%)')
@click.option('--period', type=str, required=True, help='Name of the period (e.g., "monthly", "yearly", "weekly", "twice a day", "three times a week")')
@click.option('--increments', type=int, required=True, help='Number of periods (e.g., 12, 60)')
def estimate(initial, gain, period, increments):
    """Calculate compound growth and show detailed breakdown."""
    # ── Input validation ───────────────────────────────────────────────
    errors = []

    if initial <= 0:
        errors.append("Initial amount must be positive.")
    if increments < 0:
        errors.append("Number of increments cannot be negative.")
    if increments == 0:
        click.echo("0 increments → no growth. Final = initial.")
        click.echo(f"Final amount: ${initial:,.2f}")
        click.echo("Profit: $0.00")
        return
    if gain == 0:
        click.echo("0% gain per period → no growth.")
        click.echo(f"Final amount: ${initial:,.2f}")
        click.echo("Profit: $0.00")
        return

    # Parse period string
    try:
        frequency, base_period, periods_per_year = parse_period(period)
    except ValueError as e:
        errors.append(str(e))

    if errors:
        click.echo("Error(s) in input:")
        for err in errors:
            click.echo(f"  • {err}")
        click.echo("\nPlease correct and try again.")
        return

    # ── Calculation ────────────────────────────────────────────────────
    rate = gain / 100.0
    multiplier = (1 + rate) ** increments
    final_amount = initial * multiplier
    profit = final_amount - initial
    profit_pct = (profit / initial) * 100 if initial != 0 else 0

    # Effective annual rate calculation (works for all period types)
    effective_annual_rate = ((1 + rate) ** periods_per_year - 1) * 100

    # ── Output ─────────────────────────────────────────────────────────
    click.secho("\n┌──────────────────────────────────────────────┐", fg="bright_blue")
    click.secho("          Compound Growth Estimate             ", bold=True, fg="bright_blue")
    click.secho("└──────────────────────────────────────────────┘", fg="bright_blue")

    # Format period string for display
    if frequency == 1:
        display_period = period
    else:
        display_period = period
    
    click.echo(f"  Initial amount       :  ${initial:,.2f}")
    click.echo(f"  Gain per {display_period}  :  {gain:+.2f}%")
    click.echo(f"  Number of periods     :  {increments:,}")
    click.echo(f"  Growth multiplier     :  ×{multiplier:,.3f}")
    click.echo("")

    if increments <= 20:
        click.echo("Progression (first few and last periods):")
        current = initial
        for i in range(1, min(increments + 1, 21)):
            current *= (1 + rate)
            if i <= 5 or i == increments:
                click.echo(f"  After {i:2d} {display_period:<8} → ${current:,.2f}")
        if increments > 10:
            click.echo("  ...")
    else:
        click.echo(f"(Detailed period-by-period breakdown skipped — {increments} periods is large)")

    click.secho(f"\n  Final amount          :  ${final_amount:,.2f}", bold=True, fg="green")
    click.secho(f"  Total profit          :  ${profit:,.2f}", bold=True, fg="green")
    click.secho(f"  Total return          :  {profit_pct:+.2f}%", bold=True, fg="green")

    click.echo(f"  ≈ Effective annual rate : {effective_annual_rate:.2f}%")

    click.echo("")


if __name__ == '__main__':
    cli()