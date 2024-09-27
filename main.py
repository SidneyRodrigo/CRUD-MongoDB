from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sidneyrsilvestre:silvestre321@faculdade.v9mt9uz.mongodb.net/?retryWrites=true&w=majority&appName=Faculdade"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['agenda']
contatos = db['contatos']

def menu():
    print("\n=== Menu de Contatos ===")
    print("1. Inserir novo contato")
    print("2. Exibir todos os contatos")
    print("3. Atualizar um contato")
    print("4. Deletar um contato")
    print("5. Sair")
    return input("\nEscolha uma opção: ")

def inserir_contato():
    print("\n=== Inserir Contatos ===")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    contato = {"nome": nome, "telefone": telefone}
    contatos.insert_one(contato)
    print("Contato inserido com sucesso!")

def listar_contatos():
    print("\n=== Lista de Contatos ===")
    for contato in contatos.find():
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def atualizar_contato():
    print("\n=== Atualizar Contatos ===")
    nome = input("Nome do contato a ser atualizado: ")
    novo_telefone = input("Novo telefone: ")
    contatos.update_one({"nome": nome}, {"$set": {"telefone": novo_telefone}})
    print("Contato atualizado com sucesso!")

def deletar_contato():
    print("\n=== Deletar Contatos ===")
    nome = input("Nome do contato a ser deletado: ")
    contatos.delete_one({"nome": nome})
    print("Contato deletado com sucesso!")

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == '1':
            inserir_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            atualizar_contato()
        elif opcao == '4':
            deletar_contato()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")