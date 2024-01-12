
# Subdomain Scanner V1

# Importando as bibliotecas
import dns.resolver
import argparse

# Menu da ferramenta e argumentos
parser = argparse.ArgumentParser(description="Scanner de diretórios simples")
parser.add_argument("-d", "--domain", help="Domínio alvo", required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist para scan", required=True)
args = parser.parse_args()

# Definindo as variáveis
domain = args.domain
wordlist = args.wordlist


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

        except:
            pass
    return subdomains


# Retorno da função
subdomains = get_subdomains(domain, wordlist)
print(f"[+] ON: {subdomains}")
