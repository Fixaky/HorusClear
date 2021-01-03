import requests,json,os,time,sys,re
from colorama import Fore, init, Style
init(convert = True)
os.system("title Horus Clear")
bottle1 = f"""





{Fore.GREEN}
[+] Carregando...                 

                              
"""
logo = """

██╗░░██╗░█████╗░██████╗░██╗░░░██╗░██████╗
██║░░██║██╔══██╗██╔══██╗██║░░░██║██╔════╝
███████║██║░░██║██████╔╝██║░░░██║╚█████╗░
██╔══██║██║░░██║██╔══██╗██║░░░██║░╚═══██╗
██║░░██║╚█████╔╝██║░░██║╚██████╔╝██████╔╝
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═════╝░
                            
                   By Noxty and Fixaky  
"""







print(bottle1)
time.sleep(0.1)
os.system("cls")


print(Fore.CYAN)
print(logo)
token = input("[!] Token da conta:")
token = token.replace('',"")
print(f"{Fore.CYAN}[+] Validando token...")
time.sleep(0.1)
validate = requests.get("https://canary.discordapp.com/api/v6/users/@me", headers={'authorization': token}).status_code


if validate == 200:
    print(f"{Fore.GREEN}[+] Token valido.")
    time.sleep(1.5)
else:
    print(f"{Fore.RED}[-] Token invalido.")
    input("[-] Aperta qualquer tecla para fechar!")
    sys.exit(0)













def convoclean():
    headers = {'Authorization': token}
    resp = requests.get("https://discord.com/api/v8/users/@me/channels",headers=headers)
    data = json.loads(resp.text)
    deleted = int(0)

    for i in range(len(data)):
        convodeletion = requests.delete(f"https://discord.com/api/v8/channels/{data[i]['id']}",headers=headers).status_code
        if convodeletion == 200:
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Deletando conversas privadas!")
            deleted += 1
            os.system(f"title Deletando {deleted} conversas!")
        else:
            print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Ocorreu um erro ao deletar as conversas!")
        time.sleep(1)
    print(f"[+] Conversas deletadas! Foram {deleted} conversas deletadas!")
       
    

def serverclean():
    headers = {'Authorization': token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds",headers=headers)
    data = json.loads(resp.text)
    deleted = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{data[i]['id']}",headers=headers).status_code

        if serverleaving == 204:
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Saindo dos servidores!")
            deleted += 1
            os.system(f"title Saiu de {deleted} servidores!")
        else:
            print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Erro ao sair do servidor!")
        time.sleep(1)
    print(f"[+] Servidores limpados! Foram {deleted} servidores!")


def allfriendremove():
        ids = []
        success = 0
        headers = {
            'authorization': token,
        }

        friends = requests.get('https://discordapp.com/api/v6/users/@me/relationships', headers=headers)
        if '401: Unauthorized' not in friends.text:
            types = re.findall(r'"id": "\w{18}", "type": \w{1}', friends.text)
        else:
            pass

        for type_ in types:
            if ': 1' in type_:
                ids.append(type_)

        if len(ids) != 0:
            for id_ in ids:
                id_raw = id_.split('"id": "')[1].split('", "')[0]
                decline = requests.delete('https://discord.com/api/v6/users/@me/relationships/%s' % (id_raw), headers=headers)
                if decline.status_code == 204:
                    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Amizade removida!")
                    success = success + 1
                else:
                    print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Erro ao remover amizade!")
    
            if success != 1:
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Amigos {sucess} removidos!")
            else:
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Um amigo foi removido!")
        else:
            print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE}Não foi encontrado nenhum amigo para remover!')

os.system("cls")
menu = f"""
{Fore.CYAN}[{Fore.WHITE}1{Fore.CYAN}]{Fore.WHITE} = Limpar todas as conversas e sair de todos os servidores.
{Fore.CYAN}[{Fore.WHITE}2{Fore.CYAN}]{Fore.WHITE} = Sair de todos os servidores.
{Fore.CYAN}[{Fore.WHITE}3{Fore.CYAN}]{Fore.WHITE} = Remover todas as amizades.
{Fore.CYAN}[{Fore.WHITE}4{Fore.CYAN}]{Fore.WHITE} = Ultimate
"""   

print(menu)
choice = input("[>] = ")
if choice == "1":
    convoclean()
elif choice == "2":
    serverclean()
elif choice == "3":
    allfriendremove()
elif choice == "4" or choice.lower() == "all":
    convoclean()
    serverclean()
    allfriendremove()




