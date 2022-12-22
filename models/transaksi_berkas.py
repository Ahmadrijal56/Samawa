from odoo import models, fields, api


class Transaksi_berkas(models.Model):
    _name = 'samawa_spektrum.transaksi_berkas'
    _description = 'samawa_spektrum.transaksi_berkas'

    #Data Konsumen
    no_id = fields.Char(string='Pilih No. ID / Nama')
    nama_id = fields.Char(string='Nama Lengkap')
    alamat = fields.Char(string='Alamat')
    no_handphone = fields.Char(string='No. Handphone')
    nama_proyek = fields.Char(string='Nama Proyek')
    blok = fields.Char(string='Blok / No.')
    nama_type = fields.Char(string='Nama Type')
    luas_bangunan = fields.Char(string='Luas Bangunan (m2)')
    luas_tanah = fields.Char(string='Luas Tanah (m2)')
    metode_pembelian = fields.Char(string='Metode Pembelian')
    harga_jual = fields.Char(string='Harga Jual')
    total_kewajiban_uang_muka = fields.Char(string='Total Kewajiban Uang Muka')

    #data pribadi
    pribadi1 = fields.Char(string='Photo copy KTP suami/istri')
    pribadi2 = fields.Char(string='Photo copy KK')
    pribadi3 = fields.Char(string='Photo copy Surat Nikah/Cerai')
    pribadi4 = fields.Char(string='Pas photo suami/istri')
    pribadi5 = fields.Char(string='Photo copy NPWP Pribadi')
    pribadi6 = fields.Char(string='Photo copy SPT (jika ada)')
    pribadi7 = fields.Char(string='Photo copy Buku Tabungan / Rekening koran 3 bulan terakhir')

    #data Perusahaan
    perusahaan1 = fields.Char(string='Surat Keterangan Kerja dari Perusahaan')
    perusahaan2 = fields.Char(string='Photo copy Kartu ID Pegawai (jika ada)')
    perusahaan3 = fields.Char(string='Slip gaji 3 bulan terakhir')
    perusahaan4 = fields.Char(string='SIUP & NPWP Perusahaan / Pernyataan keberatan')
   
    #data lainya
    lain1 = fields.Char(string='SKBMR dari Kelurahan')
    lain2 = fields.Char(string='Formulir isian Bank Penyedia KPR')
