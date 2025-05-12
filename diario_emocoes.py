from datetime import datetime 
def registrar_emocao():
    emocao=input("Como você está se sentindo hoje?")
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
    with open("diario.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_formatada}] {emocao}\n")
    print("Sua emoção foi registrada com sucesso!")
if _name_ == "_main_":
    print("=== Diário de Emoções ===")
    registrar_emocao()
