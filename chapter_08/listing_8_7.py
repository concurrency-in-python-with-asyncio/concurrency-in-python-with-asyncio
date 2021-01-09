import sys
import shutil


def save_cursor_position():
    sys.stdout.write('\0337')


def restore_cursor_position():
    sys.stdout.write('\0338')


def move_to_top_of_screen():
    sys.stdout.write('\033[H')


def delete_line():
    sys.stdout.write('\033[2K')


def clear_line():
    sys.stdout.write('\033[2K\033[0G')


def move_back_one_char():
    sys.stdout.write('\033[1D')


def move_to_bottom_of_screen() -> int:
    _, total_rows = shutil.get_terminal_size()
    print(total_rows)
    input_row = total_rows - 1
    sys.stdout.write(f'\033[{input_row}E')
    return 15
