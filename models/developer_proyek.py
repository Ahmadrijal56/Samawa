from odoo import models, fields, api


class Developer_proyek(models.Model):
    _name = 'samawa_spektrum.developer_proyek'
    _description = 'samawa_spektrum.developer_proyek'

    nama_proyek = fields.Text(string='Nama Proyek')
    lokasi_proyek = fields.Text(string='Lokasi')
    luas_proyek = fields.Char(string='Luas Lahan')
    jumlah_unit_proyek = fields.Char(string='Jumlah Unit')
    klasifikasi_proyek = fields.Text(string='Klasifikasi')
    konsep_proyek = fields.Text(string='Konsep')
    segmentasi_proyek = fields.Text(string='Subsidi')
    imb_proyek = fields.Char(string='No. IMB')
    izin_lokasi_proyek = fields.Char(string='Izin Lokasi')
    pengesahan_siteplan = fields.Char(string='No. Pengesahan Siteplan')
    sghb_induk_proyek = fields.Char(string='SHGB Induk')
    harga_tanah_proyek = fields.Char(string='Harga tanah Per-Meter')
    strategis_proyek = fields.Char(string='Strategis')
    jalan_utama_proyek = fields.Char(string='Jalan Utama')
    fasilitas_umum_proyek = fields.Char(string='Fasilitas Umum')

    status_proyek = fields.Text(string='Status')
    mulai_aktif_proyek = fields.Datetime(string='Mulai Aktif')
    batas_aktif_proyek = fields.Datetime(string='Batas Aktif')
    sisa_waktu_proyek = fields.Char(string='Sisa Waktu')
    picture1 = fields.Binary("Siteplan")
    picture2 = fields.Binary("Google Map")

