{
    'name': 'IPI NT default',
    'version': '16.0.1.0.0',
    'summary': 'Módulo para personalizar regras fiscais no Odoo',
    'sequence': 10,
    'author': 'Brainess Company, Odoo Community Association (OCA)',
    'website': 'https://www.brainesscompany.com',
    'description': '''
        Este módulo personaliza o comportamento do módulo l10n_br_sale,
        preenchendo automaticamente o campo ipi_tax_id com o valor "IPI NT"
        ao adicionar uma nova linha de venda.
    ''',

    'category': 'Accounting/Localizations',
    'depends': [
        'l10n_br_sale',  # Dependência do módulo fiscal brasileiro para vendas
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}