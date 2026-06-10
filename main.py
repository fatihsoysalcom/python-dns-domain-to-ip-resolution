import socket
import sys

def resolve_domain_to_ip(domain_name):
    """
    Simulates the DNS lookup process to get the IP address for a given domain name.
    This is the core DNS resolution step mentioned in the article.
    """
    try:
        # socket.gethostbyname performs the DNS lookup.
        # It takes a domain name (e.g., www.example.com)
        # and returns its corresponding IPv4 address (e.g., 93.184.216.34).
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        return f"Error resolving domain '{domain_name}': {e}"

if __name__ == "__main__":
    print("--- Domain Name System (DNS) Resolution Example ---")
    print("This script demonstrates how a domain name is translated into an IP address,")
    print("a fundamental step when you click a link, as explained in the article.")
    print("Before your browser can request content, it must find the server's IP address.")
    print("-" * 60)

    # Example domains to resolve
    domains_to_test = ["www.google.com", "www.dev.to", "example.com", "nonexistent-domain-12345.com"]

    # If an argument is provided, use it as the domain
    if len(sys.argv) > 1:
        domains_to_test = [sys.argv[1]]

    for domain in domains_to_test:
        print(f"\nAttempting to resolve: {domain}")
        resolved_ip = resolve_domain_to_ip(domain)
        # The article explains that DNS translates domain names to IP addresses.
        # This output shows that translation in action.
        print(f"Resolved IP Address: {resolved_ip}")

    print("\n-- End of Example --")
    print("This simple lookup is what happens before your browser can even try to connect to the server.")
