from dataclasses import dataclass
from typing import Dict, List, Tuple
import json
import random
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "cards.json"

@dataclass
class Card:
    nome: str
    atributos: Dict[str, float]

def carregar_baralho(caminho: Path = DATA_FILE) -> List[Card]:
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    baralho: List[Card] = []
    for item in dados:
        nome = item.get("nome", "Sem nome")
        atributos = {k: v for k, v in item.items() if k != "nome"}
        baralho.append(Card(nome=nome, atributos=atributos))
    return baralho

def sortear_duas_cartas(baralho: List[Card]) -> Tuple[Card, Card]:
    cartas = random.sample(baralho, 2)
    return cartas[0], cartas[1]

def comparar(carta1: Card, carta2: Card, atributo: str) -> int:
    """
    Retorna:
      1 se carta1 vence,
      -1 se carta2 vence,
      0 se empata.
    Regra: valor MAIOR vence.
    """
    v1 = float(carta1.atributos.get(atributo, float("-inf")))
    v2 = float(carta2.atributos.get(atributo, float("-inf")))
    if v1 > v2:
        return 1
    if v2 > v1:
        return -1
    return 0

def atributos_disponiveis(baralho: List[Card]) -> List[str]:
    # Assume que todas têm os mesmos atributos que a primeira
    if not baralho:
        return []
    return list(baralho[0].atributos.keys())
