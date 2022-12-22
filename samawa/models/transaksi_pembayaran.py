from odoo import models, fields, api


class Transaksi_pembayaran(models.Model):
    _name = 'samawa_spektrum.transaksi_pembayaran'
    _description = 'samawa_spektrum.transaksi_pembayaran'

    #pembayaran
    id_inisiasi_pembayaran = fields.Char(string='ID Inisiasi Pembayaran')
     
    #nama konsumen
    no_id = fields.Char(string='Pilih No. ID / Nama')
    nama_id = fields.Char(string='Nama Lengkap')
    alamat = fields.Char(string='Alamat')
    no_handphone = fields.Char(string='No. Handphone')

    # data kavling
    nama_proyek = fields.Char(string='Nama Proyek')
    no_kontrak = fields.Char(string='No. Kontrak')
    blok = fields.Char(string='Blok / No.')
    nama_type = fields.Char(string='Nama Type')
    luas_bangunan = fields.Char(string='Luas Bangunan (m2)')
    luas_tanah = fields.Char(string='Luas Tanah (m2)')

    # detail pembayaran
    detail_pembayaran = fields.Char(string='Detail Pembauaran')
    

