
# Subdomain Scanner V2

# Importando as bibliotecas
import dns.resolver
import argparse
import logging


# Leitura da wordlist e resolução do DNS
def get_subdomains(domain, wordlist):
    subdomains = set()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']

    with open(wordlist) as f:
        wordlist = f.read().splitlines()

    for word in wordlist:
        subdomain = f"{word}.{domain}"

        try:
            answers = resolver.resolve(subdomain)

            if answers:
                subdomains.add(subdomain)
                logging.info(f"[+] Found subdomain: {subdomain}")

        except dns.resolver.NXDOMAIN:
            logging.debug(f"[-] Subdomain not found: {subdomain}")
        except dns.exception.Timeout:
            logging.error(f"[!] DNS query timed out for: {subdomain}")
        except Exception as e:
            logging.error(f"[!] An error occurred for {subdomain}: {e}")

    return subdomains


# Menu da ferramenta e argumentos
def main():
    parser = argparse.ArgumentParser(description="Scanner de diretórios simples")
    parser.add_argument("-d", "--domain", help="Domínio alvo", required=True)
    parser.add_argument("-w", "--wordlist", help="Wordlist para scan", required=True)
    args = parser.parse_args()

    domain = args.domain
    wordlist = args.wordlist

    logging.basicConfig(level=logging.INFO)

    subdomains = get_subdomains(domain, wordlist)

    if subdomains:
        print(f"[+] Subdomains found: {subdomains}")
    else:
        print("[-] No subdomains found.")


# Retorno da função
if __name__ == "__main__":
    main()
