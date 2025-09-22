## Gerador de Senhas Seguro (CLI)

Script em Python para gerar senhas fortes de forma segura (usa o módulo `secrets`).
Sem dependências externas.

Arquivo principal: `GeradorSenha.py`

### Instalação
Nenhuma dependência extra. Requer Python 3.8+.

### Uso básico
Gerar 1 senha de 16 caracteres (padrão):
```bash
python GeradorSenha.py
```

### Opções principais
Você pode usar as flags em português (PT) ou em inglês (EN). Ambas funcionam.

- Tamanho e quantidade:
```bash
# PT
python GeradorSenha.py --tamanho 24 --quantidade 3
# EN
python GeradorSenha.py --length 24 --count 3
```

- Exigir presença de tipos de caracteres:
```bash
# PT
python GeradorSenha.py --exigir-minuscula --exigir-maiuscula --exigir-digito --exigir-simbolo
# EN
python GeradorSenha.py --require-lower --require-upper --require-digits --require-symbols
```

- Evitar caracteres ambíguos (Il1O0):
```bash
# PT
python GeradorSenha.py --evitar-ambiguos
# EN
python GeradorSenha.py --avoid-ambiguous
```

- Incluir/Excluir caracteres específicos e remover conjuntos padrão:
```bash
# Remover símbolos do conjunto padrão, incluir "@#" e excluir "xyz"
# PT
python GeradorSenha.py --sem-simbolos --incluir "@#" --excluir "xyz"
# EN
python GeradorSenha.py --no-symbols --include "@#" --exclude "xyz"
```

### Listagem completa das flags
- `--tamanho`, `--length` (int, padrão: 16): comprimento da senha
- `--quantidade`, `--count` (int, padrão: 1): quantas senhas gerar
- `--sem-minusculas`, `--no-lower`: excluir letras minúsculas
- `--sem-maiusculas`, `--no-upper`: excluir letras maiúsculas
- `--sem-digitos`, `--no-digits`: excluir dígitos
- `--sem-simbolos`, `--no-symbols`: excluir símbolos
- `--exigir-minuscula`, `--require-lower`: exigir ao menos uma minúscula
- `--exigir-maiuscula`, `--require-upper`: exigir ao menos uma maiúscula
- `--exigir-digito`, `--require-digits`: exigir ao menos um dígito
- `--exigir-simbolo`, `--require-symbols`: exigir ao menos um símbolo
- `--evitar-ambiguos`, `--avoid-ambiguous`: evitar caracteres ambíguos (Il1O0)
- `--incluir`, `--include` (str): caracteres extras para incluir
- `--excluir`, `--exclude` (str): caracteres a excluir

Observações:
- Se você exigir grupos (ex.: `--exigir-maiuscula` etc.), o tamanho deve ser suficiente para comportar todos os grupos exigidos.
- Se, após filtros e exclusões, o conjunto de caracteres ficar vazio, o programa avisará.

### Boas práticas
- Use tamanhos maiores (20+ caracteres) e exija múltiplos tipos quando possível.
- Evite reutilizar senhas. Considere um gerenciador de senhas.
- Ative 2FA onde houver suporte.

### Exemplos rápidos
- 5 senhas de 20 caracteres, fortes e sem ambíguos (PT):
```bash
python GeradorSenha.py --tamanho 20 --quantidade 5 --exigir-minuscula --exigir-maiuscula --exigir-digito --exigir-simbolo --evitar-ambiguos
```
- 3 senhas sem símbolos, mas incluindo "@#" (EN):
```bash
python GeradorSenha.py --length 18 --count 3 --no-symbols --include "@#"
```
