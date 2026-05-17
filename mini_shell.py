#!/usr/bin/env python3

import os
import subprocess
import shutil

# ==============================
# Mini Linux Shell in Python
# ==============================

def show_commands():
    print("""
================ Available Commands ================

Basic Navigation:
    pwd                 -> Show current directory
    ls                  -> List files and folders
    cd <directory>      -> Change directory
    clear               -> Clear terminal

File & Directory Operations:
    mkdir <name>        -> Create directory
    touch <file>        -> Create empty file
    cat <file>          -> Display file content
    rm <file>           -> Remove file
    cp <src> <dest>     -> Copy file
    mv <src> <dest>     -> Move/Rename file

User & System:
    whoami              -> Show current user
    history             -> Show command history
    date                -> Show current date and time

Process & System Info:
    ps                  -> Show running processes
    top                 -> Show system monitor
    ifconfig            -> Show network interfaces
    ip route            -> Show routing table

Networking:
    ping <host>         -> Ping a host

Text Utilities:
    echo <text>         -> Print text
    grep <word> <file>  -> Search text in file
    wc <file>           -> Count lines/words/chars

Extra:
    Commands            -> Show this command list
    exit                -> Exit the shell

====================================================
""")


def execute_command(command):
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error: {e}")


def mini_shell():
    history = []

    print("===================================")
    print("   Welcome to Python Mini Shell")
    print("   Type 'Commands' to see commands")
    print("   Type 'exit' to quit")
    print("===================================")

    while True:
        try:
            current_dir = os.getcwd()
            user_input = input(f"{current_dir} $ ")

            if not user_input.strip():
                continue

            history.append(user_input)

            parts = user_input.split()

            command = parts[0]

            # Exit shell
            if command == "exit":
                print("Exiting Mini Shell...")
                break

            # Show available commands
            elif command == "Commands":
                show_commands()

            # pwd
            elif command == "pwd":
                print(os.getcwd())

            # ls
            elif command == "ls":
                execute_command("ls")

            # cd
            elif command == "cd":
                if len(parts) > 1:
                    try:
                        os.chdir(parts[1])
                    except FileNotFoundError:
                        print("Directory not found.")
                else:
                    print("Usage: cd <directory>")

            # clear
            elif command == "clear":
                os.system("clear")

            # mkdir
            elif command == "mkdir":
                if len(parts) > 1:
                    os.mkdir(parts[1])
                else:
                    print("Usage: mkdir <directory_name>")

            # touch
            elif command == "touch":
                if len(parts) > 1:
                    open(parts[1], 'a').close()
                else:
                    print("Usage: touch <filename>")

            # cat
            elif command == "cat":
                if len(parts) > 1:
                    try:
                        with open(parts[1], 'r') as file:
                            print(file.read())
                    except FileNotFoundError:
                        print("File not found.")
                else:
                    print("Usage: cat <filename>")

            # rm
            elif command == "rm":
                if len(parts) > 1:
                    try:
                        os.remove(parts[1])
                    except FileNotFoundError:
                        print("File not found.")
                else:
                    print("Usage: rm <filename>")

            # cp
            elif command == "cp":
                if len(parts) > 2:
                    try:
                        shutil.copy(parts[1], parts[2])
                    except FileNotFoundError:
                        print("File not found.")
                else:
                    print("Usage: cp <source> <destination>")

            # mv
            elif command == "mv":
                if len(parts) > 2:
                    try:
                        shutil.move(parts[1], parts[2])
                    except FileNotFoundError:
                        print("File not found.")
                else:
                    print("Usage: mv <source> <destination>")

            # whoami
            elif command == "whoami":
                execute_command("whoami")

            # history
            elif command == "history":
                for index, cmd in enumerate(history, start=1):
                    print(f"{index}: {cmd}")

            # date
            elif command == "date":
                execute_command("date")

            # ps
            elif command == "ps":
                execute_command("ps")

            # top
            elif command == "top":
                execute_command("top")

            # ifconfig
            elif command == "ifconfig":
                execute_command("ifconfig")

            # ip route
            elif command == "ip":
                execute_command(user_input)

            # ping
            elif command == "ping":
                execute_command(user_input)

            # echo
            elif command == "echo":
                print(" ".join(parts[1:]))

            # grep
            elif command == "grep":
                execute_command(user_input)

            # wc
            elif command == "wc":
                execute_command(user_input)

            # Unknown command
            else:
                print(f"Command not found: {command}")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")

        except Exception as e:
            print(f"Unexpected Error: {e}")


# Run the shell
if __name__ == "__main__":
    mini_shell()
