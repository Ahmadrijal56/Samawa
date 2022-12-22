from odoo import models, fields, api


class Developer_stockkavling(models.Model):
    _name = 'samawa_spektrum.developer_stockkavling'
    _description = 'samawa_spektrum.developer_stockkavling'

    # Data Kavling
    type_kavling = fields.Char(string='Nama Type')
    blok_kavling = fields.Char(string='Blok')
    nomor_kavling = fields.Char(string='Nomor')
    luas_bangunan_kavling = fields.Char(string='Luas Bangunan (m2)')
    luas_tanah_kavling = fields.Char(string='Luas Tanah (m2)')
    hook_kavling = fields.Char(string='Hook / Tanah Lebih (m2)')
    zona_indent_kavling = fields.Char(string='Zona Indent')
    tenor_sisa_kavling = fields.Char(string='Tenor Sisa')
    status_kavling = fields.Selection([
        ('tersedia', 'Tersedia'),
        ('booked', 'Booked'),
        ('terjual', 'Terjual'),
        ('pilih', 'Pilih')], string='Status Kavling', default='pilih')
    hadap_kavling = fields.Selection([
        ('barat', 'Barat'),
        ('timur', 'Timur'),
        ('selatan', 'Selatan'),
        ('utara', 'Utara'),
        ('pilih', 'Pilih')], string='Hadap Kavling', default='pilih')
    rencana_kpr = fields.Char(string='Rencana KPR')
    
    # Harga Jual dan Uang Muka
    nilai_booking = fields.Char(string='Nilai Booking Fee')
    uang_muka = fields.Char(string='Uang Muka')
    amount_hook = fields.Char(string='Amount Hook')
    biaya_strategis = fields.Char(string='Biaya Strategis')
    jalan_utama_kavling = fields.Char(string='*Jalan Utama')
    fasilitas_umum_kavling = fields.Char(string='*Fasilitas Umum')
    amount_kewajiban_indent = fields.Char(string='Amount Kewajiban Indent')
    amount_cicilan_sisa = fields.Char(string='Amount Cicilan Sisa')
    total_amount_indent = fields.Char(string='Total Amount Indent')
    total_amount_uang_muka = fields.Char(string='Total Amount Uang Muka')
    total_harga_jual = fields.Char(string='Total Harga Jual')
    harga_jual_cash_cash = fields.Char(string='Harga Jual Cash Cash')
    harga_jaul_cash_bertahap = fields.Char(string='Harga Jual Cash Bertahap')
    cicilan_indent = fields.Char(string='Cicilan Indent')
    cicilan_sisa = fields.Char(string='Cicilan Sisa')

    #fee Marketing
    nilai_fee_unit = fields.Char(string='Nilai Fee Unit')

    #foto kavling terbaru
    foto_kavling = fields.Binary(string='Foto Kavling Terbaru')

    #progres bangunan
    status_bangunan_kavling = fields.Selection([
        ('indent', 'Indent'),
        ('bangun', 'Bangun'),
        ('ready', 'Ready'),
        ('qualified', 'Qualified'),
        ('pilih', 'Pilih Status Bangunan')], string='Status Bangunan', default='pilih')
    tahap_bangunan_kavling = fields.Char(string='Tahap Bangunan (%)')
    
    listrik_kavling = fields.Selection([
        ('terpasang', 'Terpasang'),
        ('belum', 'Belum Terpasang'),
        ('pilih', 'Pilih')], string='Listrik', default='pilih')
    
    pompa_air_kavling = fields.Selection([
        ('terpasang', 'Terpasang'),
        ('belum', 'Belum Terpasang'),
        ('pilih', 'Pilih')], string='Pompa Air', default='pilih')

    #legalitas
    no_sertifikat_kavling = fields.Char(string='No. Sertifikat')
    no_imb_kavling = fields.Char(string='No. IMB')
    no_pbb = fields.Char(string='No. PBB')

    def action_test(self):
        print("Button Di pencet")




