import socket
import argparse

def domain_to_ip(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return None

def convert_domains(input_file, output_file=None, single_domain=None):
    ip_addresses = []

    if input_file:
        with open(input_file, 'r') as file:
            domains = file.readlines()

        for domain in domains:
            domain = domain.strip()
            ip_address = domain_to_ip(domain)
            if ip_address:
                ip_addresses.append(ip_address)

    if single_domain:
        ip_address = domain_to_ip(single_domain)
        if ip_address:
            ip_addresses.append(ip_address)

    if output_file:
        with open(output_file, 'w') as file:
            for ip_address in ip_addresses:
                file.write(ip_address + '\n')

    for ip_address in ip_addresses:
        print(ip_address)

def print_banner():
    banner = """
   ___             _    
  / _ \\___  __ _  (_)__ 
 / // / _ \\/  ' \\/ / _ \\
/____/\\___/_/_/_/_/ .__/
                 /_/    v1
        github.com/X-Projetion        
"""
    print(banner)

def main():
    parser = argparse.ArgumentParser(description='Convert domain names to IP addresses.')
    parser.add_argument('-l', '--list-file', help='Input file containing list of domains')
    parser.add_argument('-u', '--single-domain', help='Single domain name to convert')
    parser.add_argument('-o', '--output-file', help='Output file to save the IP addresses')
    args = parser.parse_args()

    if not args.list_file and not args.single_domain:
        parser.error('At least one of -l or -u is required.')

    convert_domains(args.list_file, args.output_file, args.single_domain)

if __name__ == "__main__":
    print_banner()
    main()
