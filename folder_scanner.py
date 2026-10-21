import os
from sys import argv

SAVE_PATH = "data.txt"

def scan(path:str) -> list[str]:
    results : list[str] = []
    stack : list[str] = [path]
    stack_counter : int = 1
    scan_counter : int = 0
    while stack:
        scan_counter += 1
        if(scan_counter % 500 == 0):
            print(
                f"\r\033[KPending: {stack_counter} | Scanned: {scan_counter}",
                end="",
                flush=True
            )
        path = stack.pop()
        stack_counter -= 1
        try:
            dir_list = os.listdir(path)
        except PermissionError:
            continue
        if(len(dir_list) == 0):
            results.append(path)
            continue
        
        folders : list[str] = list(filter(lambda x: os.path.isdir(os.path.join(path, x)),dir_list))
        for folder in folders:
            new_path : str = f"{path}\\{folder}"
            stack.append(new_path)
            stack_counter += 1


    return results

def save_results(re : list[str]) -> None:
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in re)

def Main(argc : int, argv : list[str]) -> None:
    if(argc == 1):
        path = "C:\\"
    else:
        path = argv[1]
    print(f"Scanning path: {path}")
    re = scan(path)
    save_results(re)
    os.startfile(SAVE_PATH)
    


if __name__ == "__main__":
    Main(len(argv), argv)