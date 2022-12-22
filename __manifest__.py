# -*- coding: utf-8 -*-
{
    'name': "samawa_spektrum",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Spektrum",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',    
        'views/dashboard.xml',    
        'views/developer.xml',
        'views/developer_profil.xml',
        'views/developer_proyek.xml',
        'views/developer_stockkavling.xml',
        'views/transaksi.xml',
        'views/transaksi_datakonsumen.xml',
        'views/transaksi_booking.xml',
        'views/transaksi_pembayaran.xml',
        'views/transaksi_berkas.xml',
        'views/data_laporan.xml',
        'views/data_laporan_penjualan.xml',
        'views/data_laporan_jadwaltagihan.xml',
        'views/data_laporan_batal.xml',
        'views/data_laporan_resumeharian.xml',
        'views/marketing.xml',
        'views/marketing_fee.xml',
        'views/marketing_profil.xml',
        'views/user.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
