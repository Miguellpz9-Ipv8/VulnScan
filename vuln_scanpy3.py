import requests

def scan():
    site = input("Provide URL: ")
    function_choice = input("Enter the function to run (SQLscn or VERxss): ")
    if function_choice == "SQLscn" or "SQL" or "sqlscan":
        SQLscn(site)
    elif function_choice == "VERxss" or "XSS" or "xssscan":
        VERxss(site)
    elif function_choice == "SQLscn" & "VERxss":
        SQLscn(site)
        VERxss(site)
    else:
        print("Invalid function choice!")
    print("Scanning: {site}")

def enumfiles():
    file_paths = input("Enter file paths (separated by spaces): ").split()
    payloads = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    payloads.append(line.strip())
        except FileNotFoundError:
            print("File not found: {file_path}")
    return payloads

def SQLscn(site):
    payloads = enumfiles()
    for requested in payloads:
        modified_url = site + requested
        response = requests.get(modified_url)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print("[SQL Injection] Potential vulnerability: '{modified_url}'")

def VERxss(site):
    payloads = enumfiles()
    for payload in payloads:
        modified_url = site + payload
        response = requests.get(modified_url)
        if payload in response.text:
            print("[XSS] Potential vulnerability: '{modified_url}'")

scan()

