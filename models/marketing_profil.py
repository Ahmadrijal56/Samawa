from odoo import models, fields, api


class Marketing_profil(models.Model):
    _name = 'samawa_spektrum.marketing_profil'
    _description = 'samawa_spektrum.marketing_profil'

    name_market = fields.Char(string='Nama Marketing')
    level_market = fields.Text(string='Level')
    alamat_market = fields.Text(string='Alamat')
    penjualan_market = fields.Char(string='Jumlah Penjualan')
    pj_market = fields.Text(string='Penangung Jawab')
    ktp_pj = fields.Char(string='No.KTP')
    mou_market = fields.Char(string='No.SPK / MOU')
    tim_market = fields.Char(string='Jumlah Tim Sales')
    proyek_kerjasama = fields.Text(string='Proyek Kerjasama')
    description = fields.Text(string='Description')