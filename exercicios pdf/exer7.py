capacete = input("Está utilizando capacete? (s/n): ").strip().lower()
oculos = input("Está utilizando óculos de proteção? (s/n): ").strip().lower()
protetor = input("Está utilizando protetor auricular? (s/n): ").strip().lower()
calcado = input("Está utilizando calçado de segurança? (s/n): ").strip().lower()

if capacete == "s" and oculos == "s" and protetor == "s" and calcado == "s":
    print("\nAcesso liberado para a atividade.")
else:
    print("\nAtenção: verifique os EPIs antes de iniciar a atividade.")

"""
capacete = input("Está utilizando capacete? (s/n): ").strip().lower() // Define o input para não ter espaçamentos e ser minúsculo
oculos = input("Está utilizando óculos de proteção? (s/n)": ).strip().lower() // Define o input para não ter espaçamentos e ser minúsculo
protetor = input("Está utilizando protetor auricular? (s/n): ").strip().lower() // Define o input para não ter espaçamentos e ser minúsculo
calcado = input("Está utilizando calçado de segurança? (s/n): ").strip().lower() // Define o input para não ter espaçamentos e ser minúsculo

if capacete == "s" and oculos == "s" and protetor == "s" and calcado == "s":
    print("\nAcesso lbierado para atividade")
else:
    print("\nAtenção: verifique os EPIs antes de iniciar a atividade!)
"""