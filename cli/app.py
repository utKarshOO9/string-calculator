import click


@click.command("string_calculator")
@click.option("--numbers", required=True, help="strings of number with delimited values")
def main(numbers: str):
    click.echo(
        "\n".join(
            ["Output:", "==================", f"Input: {numbers}", "Addition of numbers: 0", "=================="]
        )
    )


if __name__ == "__main__":
    main()
