import argparse
import secrets
import string
from typing import List

AMBIGUOUS = "Il1O0"


def build_charset(include_lower: bool, include_upper: bool, include_digits: bool, include_symbols: bool, avoid_ambiguous: bool, extra_include: str, extra_exclude: str) -> str:
    charset = ""
    if include_lower:
        charset += string.ascii_lowercase
    if include_upper:
        charset += string.ascii_uppercase
    if include_digits:
        charset += string.digits
    if include_symbols:
        charset += string.punctuation
    charset += extra_include
    if avoid_ambiguous:
        charset = "".join(ch for ch in charset if ch not in AMBIGUOUS)
    if extra_exclude:
        exclude_set = set(extra_exclude)
        charset = "".join(ch for ch in charset if ch not in exclude_set)
    charset = "".join(sorted(set(charset)))
    if not charset:
        raise ValueError("Conjunto de caracteres ficou vazio após os filtros.")
    return charset


def generate_password(length: int, charset: str, require_lower: bool, require_upper: bool, require_digits: bool, require_symbols: bool) -> str:
    if length <= 0:
        raise ValueError("O tamanho deve ser > 0")

    required_groups: List[str] = []
    if require_lower:
        required_groups.append(string.ascii_lowercase)
    if require_upper:
        required_groups.append(string.ascii_uppercase)
    if require_digits:
        required_groups.append(string.digits)
    if require_symbols:
        required_groups.append(string.punctuation)

    if required_groups and length < len(required_groups):
        raise ValueError("Tamanho muito pequeno para atender aos grupos exigidos")

    password_chars: List[str] = []

    for group in required_groups:
        # escolher da interseção entre charset e o grupo
        group_chars = [c for c in group if c in charset]
        if not group_chars:
            raise ValueError("Um grupo exigido não está presente no conjunto final")
        password_chars.append(secrets.choice(group_chars))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(charset))

    # Embaralhar com segurança
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gerador de senhas seguro")
    parser.add_argument("--length", "--tamanho", type=int, default=16, help="Tamanho da senha (padrão: 16)")
    parser.add_argument("--count", "--quantidade", type=int, default=1, help="Quantidade de senhas para gerar (padrão: 1)")

    # Conjuntos incluídos
    parser.add_argument("--no-lower", "--sem-minusculas", action="store_true", help="Excluir letras minúsculas")
    parser.add_argument("--no-upper", "--sem-maiusculas", action="store_true", help="Excluir letras maiúsculas")
    parser.add_argument("--no-digits", "--sem-digitos", action="store_true", help="Excluir dígitos")
    parser.add_argument("--no-symbols", "--sem-simbolos", action="store_true", help="Excluir símbolos")

    # Exigências
    parser.add_argument("--require-lower", "--exigir-minuscula", action="store_true", help="Exigir ao menos uma minúscula")
    parser.add_argument("--require-upper", "--exigir-maiuscula", action="store_true", help="Exigir ao menos uma maiúscula")
    parser.add_argument("--require-digits", "--exigir-digito", action="store_true", help="Exigir ao menos um dígito")
    parser.add_argument("--require-symbols", "--exigir-simbolo", action="store_true", help="Exigir ao menos um símbolo")

    # Ajustes
    parser.add_argument("--avoid-ambiguous", "--evitar-ambiguos", action="store_true", help="Evitar caracteres ambíguos (Il1O0)")
    parser.add_argument("--include", "--incluir", default="", help="Caracteres extras para incluir")
    parser.add_argument("--exclude", "--excluir", default="", help="Caracteres a excluir")

    args = parser.parse_args()

    include_lower = not args.no_lower
    include_upper = not args.no_upper
    include_digits = not args.no_digits
    include_symbols = not args.no_symbols

    charset = build_charset(
        include_lower=include_lower,
        include_upper=include_upper,
        include_digits=include_digits,
        include_symbols=include_symbols,
        avoid_ambiguous=args.avoid_ambiguous,
        extra_include=args.include,
        extra_exclude=args.exclude,
    )

    for _ in range(args.count):
        pwd = generate_password(
            length=args.length,
            charset=charset,
            require_lower=args.require_lower,
            require_upper=args.require_upper,
            require_digits=args.require_digits,
            require_symbols=args.require_symbols,
        )
        print(pwd)


if __name__ == "__main__":
    main()
