from odoo import models, fields, api


class Transaksi_booking(models.Model):
    _name = 'samawa_spektrum.transaksi_booking'
    _description = 'samawa_spektrum.transaksi_booking'

    #booking unit
    booking_id = fields.Char(string='Booking ID')

    #data pembeli
    no_id = fields.Char(string='Pilih No. ID / Nama')
    nama_id = fields.Char(string='Nama Lengkap')
    alamat = fields.Char(string='Alamat')
    no_handphone = fields.Char(string='No. Handphone')

    # data kavling
    nama_proyek = fields.Char(string='Nama Proyek')
    blok = fields.Char(string='Blok / No.')
    nama_type = fields.Char(string='Nama Type')
    luas_bangunan = fields.Char(string='Luas Bangunan (m2)')
    luas_tanah = fields.Char(string='Luas Tanah (m2)')
    metode_pembelian = fields.Char(string='Metode Pembelian')
    harga_jual = fields.Char(string='Harga Jual')
    total_kewajiban_uang_muka = fields.Char(string='Total Kewajiban Uang Muka')

    #jadweal pembanyaran
    jadwal_pembayaran = fields.Char(string='Jadwal Pembayaran')

