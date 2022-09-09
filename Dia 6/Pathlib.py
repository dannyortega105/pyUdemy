from pathlib import Path, PureWindowsPath

carpeta = Path('C:\\Users\\Danny Ortega\\Desktop\\Python\\prueba.txt')

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")