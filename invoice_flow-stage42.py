# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: InvoiceFlow
ANSI_RED = '\033[31m'
ANSI_GREEN = '\033[32m'
ANSI_YELLOW = '\033[33m'
ANSI_BLUE = '\033[34m'
ANSI_CYAN = '\033[36m'
ANSI_WHITE = '\033[37m'
ANSI_RESET = '\033[0m'
ANSI_BOLD = '\033[1m'

def colorize(text, color):
    if os.environ.get('NO_COLOR'):
        return text
    return f'{color}{text}{ANSI_RESET}'

def green(text):
    return colorize(text, ANSI_GREEN)

def red(text):
    return colorize(text, ANSI_RED)

def yellow(text):
    return colorize(text, ANSI_YELLOW)

def blue(text):
    return colorize(text, ANSI_BLUE)

def cyan(text):
    return colorize(text, ANSI_CYAN)

def bold(text):
    return colorize(text, ANSI_BOLD)

if __name__ == '__main__':
    print(f'{bold("InvoiceFlow v42")} - ANSI Color Support')
    print(f'{green("✓")} Status colors enabled')
    print(f'{red("✗")} Failed invoice')
    print(f'{yellow("⚠")} Warning')
    print(f'{cyan("ℹ")} Info')
    print(f'{blue("→")} Processing...')
