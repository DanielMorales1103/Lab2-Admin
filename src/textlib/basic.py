from __future__ import annotations

import unicodedata
from typing import Iterable

def _ensure_str(value: str, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{name} debe ser str; se recibió {type(value).__name__}")

def _strip_accents(text: str) -> str:
    # Normaliza a NFD y elimina marcas diacríticas (acentos)
    nfd = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in nfd if unicodedata.category(ch) != "Mn")

def reverse(s: str) -> str:
    """
    Retorna la cadena en orden inverso.
    """
    _ensure_str(s, "s")
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Retorna el total de vocales en la cadena.
    Soporta español (cuenta vocales con y sin acento: a, e, i, o, u; á, é, í, ó, ú; ü).
    """
    _ensure_str(s, "s")
    # Quitamos acentos para simplificar el conteo e incluimos 'ü'
    base = _strip_accents(s).lower().replace("ü", "u")
    vowels = set("aeiou")
    return sum(1 for ch in base if ch in vowels)

def is_palindrome(s: str) -> bool:
    """
    Retorna True si s es palíndromo, ignorando:
      - mayúsculas/minúsculas,
      - espacios y signos de puntuación,
    Considera únicamente caracteres alfanuméricos.
    """
    _ensure_str(s, "s")
    normalized = _strip_accents(s)
    filtered = [ch.lower() for ch in normalized if ch.isalnum()]
    return filtered == filtered[::-1]

def to_upper(s: str) -> str:
    """
    Retorna la cadena en MAYÚSCULAS (respeta Unicode).
    """
    _ensure_str(s, "s")
    return s.upper()

def concat(a: str, b: str) -> str:
    """
    Retorna la concatenación de a y b.
    """
    _ensure_str(a, "a")
    _ensure_str(b, "b")
    return a + b
