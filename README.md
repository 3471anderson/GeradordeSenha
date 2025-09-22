## Monitor de Preços Online (Python)

Uma ferramenta simples e configurável que busca páginas, extrai preços usando seletores CSS ou atributos, armazena histórico em CSV e alerta quando um limite é atingido.

### Recursos
- Configuração via YAML
- Seletor CSS + atributo opcional ou regex
- Repetição com backoff e cabeçalhos reais
- Histórico gravado em `prices.csv`
- Executa uma vez ou em loop em um intervalo

### Instalação
1. Crie um ambiente virtual (recomendado).
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Copie o arquivo de exemplo e personalize:
```powershell
copy config.example.yaml config.yaml
```

### Configuração
Edite `config.yaml` com uma lista de alvos. Exemplo:
```yaml
targets:
  - name: Produto Exemplo USD
    url: https://example.org/product
    selector: span.price
    attr: text
    currency_symbol: "$"
    # regex: "(\\d+[.,]\\d+)"
    # threshold_price: 99.99
```
- `selector`: seletor CSS até o elemento do preço
- `attr`: `text` para usar o texto do elemento, ou o nome do atributo
- `currency_symbol`: símbolo opcional para remover (ex.: `$`, `R$`)
- `regex`: captura opcional para números quando o texto tem extras
- `threshold_price`: número opcional para alertar quando o preço for menor ou igual
- `headers`: cabeçalhos de requisição opcionais (mescla com os padrões)

### Uso
Executar uma vez:
```bash
python price_monitor.py --config config.yaml --once
```
Executar em loop a cada 30 minutos:
```bash
python price_monitor.py --config config.yaml --loop --interval 1800
```
Limitar execuções do loop (útil para testes):
```bash
python price_monitor.py --config config.yaml --loop --interval 60 --max-runs 3
```
Mudar o caminho do CSV de saída:
```bash
python price_monitor.py --config config.yaml --out meus_precos.csv --once
```

### Observações
- Alguns sites bloqueiam scraping. Considere customizar cabeçalhos ou intervalos e respeite `robots.txt` e os termos do site.
- Sites dinâmicos podem exigir que o preço esteja renderizado no servidor ou seletores específicos. Esta ferramenta não executa JavaScript.
- Use com responsabilidade.

---

## Gerador de Senhas (CLI)

Script simples e seguro para gerar senhas usando o módulo `secrets`.

### Uso
Gerar 1 senha de 16 caracteres (padrão):
```bash
python password_generator.py
```
Tamanho e quantidade:
```bash
python password_generator.py --length 24 --count 3
```
Exigir presença de tipos e evitar ambíguos (Il1O0):
```bash
python password_generator.py --require-lower --require-upper --require-digits --require-symbols --avoid-ambiguous
```
Personalizar conjunto de caracteres:
```bash
python password_generator.py --no-symbols --include "@#" --exclude "xyz"
```
