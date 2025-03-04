# Default IPI NT

Este módulo personaliza o comportamento do módulo `l10n_br_sale` no Odoo, preenchendo automaticamente o campo `ipi_tax_id` com o valor "IPI NT" ao adicionar uma nova linha de venda.

---

## Funcionalidades

- **Preenchimento Automático do IPI NT**: Ao adicionar uma nova linha de venda, o campo `ipi_tax_id` é preenchido automaticamente com o imposto "IPI NT", caso não tenha sido definido manualmente.

---

## Requisitos

- Odoo 16 (ou versão compatível com o módulo `l10n_br_sale`).
- Módulo `l10n_br_sale` instalado e configurado.

---

## Instalação

1. **Coloque o módulo na pasta `addons`**:
   - Copie a pasta `meu_modulo_fiscal` para o diretório `addons` do Odoo.

2. **Reinicie o servidor Odoo**:
   - Reinicie o servidor para que o Odoo reconheça o novo módulo.

3. **Atualize a lista de aplicativos**:
   - Ative o modo desenvolvedor (em `Configurações > Ativar Modo Desenvolvedor`).
   - Vá para `Apps > Atualizar Lista de Aplicativos`.

4. **Instale o módulo**:
   - Pesquise por "Meu Módulo Fiscal Personalizado" na lista de aplicativos e clique em "Instalar".

---

## Como Usar

Após a instalação, o módulo funcionará automaticamente. Ao adicionar uma nova linha de venda:

1. Abra um pedido de venda existente ou crie um novo.
2. Adicione uma nova linha de produto.
3. O campo `ipi_tax_id` será preenchido automaticamente com o valor "IPI NT", caso não tenha sido definido manualmente.

---

## Personalização

Se você precisar alterar o nome do imposto que é preenchido automaticamente, edite o arquivo `models/sale_order_line.py` e modifique a linha:

```python
ipi_nt_tax = self.env['account.tax'].search([
    ('name', '=', 'IPI NT'),  # Altere para o nome do imposto desejado
    ('type_tax_use', '=', 'sale'),
], limit=1)