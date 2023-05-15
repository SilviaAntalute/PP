import subprocess
command = input("Introduceți comanda: ")

commands = command.split("|")

input_data = None

for cmd in commands:
    # Eliminarea spațiilor albe de la început și sfârșit
    cmd = cmd.strip()

    process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    output, _ = process.communicate(input_data)

    input_data = output

    print(output.decode())