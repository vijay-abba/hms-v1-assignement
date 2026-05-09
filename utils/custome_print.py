from rich.console import Console

console = Console()


class ColPt:

    @staticmethod
    def red(msg):
        console.print(msg, style="bold red")

    @staticmethod
    def blue(msg):
        console.print(msg, style="bold blue")

    @staticmethod
    def green(msg):
        console.print(msg, style="bold bright_green")

    @staticmethod
    def yellow(msg):
        console.print(msg, style="bold bright_yellow")
    @staticmethod

    def orange(msg):
        console.print(msg, style="bold orange1")

    @staticmethod
    def cyan(msg):
        console.print(msg, style="bold bright_cyan")

    @staticmethod
    def magenta(msg):
        console.print(msg, style="bold bright_magenta")


    @staticmethod
    def input_yellow(msg):
        return console.input(f"[bold yellow] {msg}")


