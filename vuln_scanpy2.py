#Author: miguellpz9-ipv8
#https://github.com/miguellpz9-ipv8
import requests
import bs4

def scan():
    site = raw_input("Provide URL: ")
    function_choice = raw_input("Enter the function to run (SQLscn, VERxss, csrf): ")
    if function_choice == "SQLscn":
        SQLscn(site)
    elif function_choice == "VERxss":
        VERxss(site)
    elif function_choice == "csrf":
	csrf(site)
    elif function_choice == "All" or "all":
	SQLscn(site)
	VERxss(site)
	csrf(site)
    else:
        print "Invalid function choice!"
    print "Scanning: {}".format(site)

def enumfiles():
    file_paths = raw_input("Enter file paths (separated by spaces): ").split()
    payloads = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    payloads.append(line.strip())
        except IOError:
            print "File not found: {}".format(file_path)
    return payloads

def SQLscn(site):
    payloads = enumfiles()
    for requested in payloads:
        modified_url = site + requested
        response = requests.get(modified_url)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print "[SQL Injection] Potential vulnerability: {}".format(modified_url)

def VERxss(site):
    payloads = enumfiles()
    for payload in payloads:
        modified_url = site + payload
        response = requests.get(modified_url)
        if payload in response.text:
            print "[XSS] Potential vulnerability: {}".format(modified_url)
def csrf(site):
    response = requests.get(site)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    forms = soup.find_all('form')
    for form in forms:
        if not form.find('input', {'name': 'csrf_token'}):
            return True
    # No CSRF vulnerability found
    return False


scan()

