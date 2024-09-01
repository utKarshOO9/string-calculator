import click
from string_calculator import calculator


@click.command("string_calculator")
@click.option("--numbers", required=True, help="strings of number with delimited values")
def main(numbers: str):
    result = calculator.add(numbers)
    click.echo(
        "\n".join(
            [
                "Output:",
                "==================",
                f"Input: {numbers}",
                f"Addition of numbers: {result}",
                "==================",
            ]
        )
    )


if __name__ == "__main__":
    main()
