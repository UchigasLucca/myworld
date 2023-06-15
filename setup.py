from cx_Freeze import setup, Executable

# Configuração do executável
executables = [Executable("apicossumm.py")]

# Configuração do setup
setup(
    name="Pokeinfo",
    version="1.1",
    description="Programa designado aos estudos do Lucca. Valeu",
    executables=executables
)

