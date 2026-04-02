def todas_tabuadas_cem():
    input("Pressione Enter para ver todas as tabuadas de 1 a 100...") 
    for i in range(1, 101):
        print(f"--- Tabuada do {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
todas_tabuadas_cem()