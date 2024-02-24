"""
Програма «Рекурсивне копіювання файлів»

Рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії
та сортує в піддиректорії, назви яких базуються на розширенні файлів."""

# import os
import shutil
from pathlib import Path
import argparse


# def copy_files(source_dir, destination_dir):
#     for root, dirs, files in os.walk(source_dir):
#         for file in files:
#             extension = os.path.splitext(file)[1]
#             if not os.path.exists(os.path.join(destination_dir, extension)):
#                 os.makedirs(os.path.join(destination_dir, extension))
#             shutil.copy(
#                 os.path.join(root, file), os.path.join(destination_dir, extension)
#             )


def parse_argv():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        # prog="Рекурсивне копіювання файлів",
        description="Рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.",
    )
    parser.add_argument(
        "-s",
        "--source",
        dest="source",
        metavar="",
        type=Path,
        required=True,
        help="шлях до вихідної директорії",
    )
    parser.add_argument(
        "-d",
        "--destination",
        dest="destination",
        metavar="",
        type=Path,
        required=False,
        default="dist",
        help="шлях до нової директорії",
    )
    return parser.parse_args()


def recursive_copy(src: Path, dst: Path):
    if not src.exists():
        print(f"Шлях {src} не існує")
        return
    for item in src.iterdir():
        if item.is_dir():
            recursive_copy(item, dst)
        else:
            try:
                folder = dst / item.suffix[1:] if item.suffix else dst
                folder.mkdir(exist_ok=True, parents=True)
                new_path = shutil.copy2(item, folder)
                # print(f"Скопійовано {new_path}")
            except shutil.Error as e:
                print(f"Помилка копіювання {item} - {e}")
    return


if __name__ == "__main__":
    args = parse_argv()
    args_str = "\n".join(f"{k} = {v}" for k, v in vars(args).items())
    print(f"Задані аргументи: \n{args_str}")
    recursive_copy(args.source, args.destination)
