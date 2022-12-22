from odoo import models, fields, api


class Transaksi_datakonsumen(models.Model):
    _name = 'samawa_spektrum.transaksi_datakonsumen'
    _description = 'samawa_spektrum.transaksi_datakonsumen'

    # Data sesuai KTP
    ktp_konsumen = fields.Integer(string='NIK(No.KTP)')
    nama_konsumen = fields.Char(string='Nama')
    lahir_konsumen = fields.Datetime(string='Tempat/Tgl Lahir')
    jenis_kelamin_konsumen =  fields.Selection([
        ('laki_laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
        ('pilih', 'Pilih Jenis Kelamin')], string='Jenis Kelamin', default='pilih')
    alamat_konsumen = fields.Char(string='Alamat')
    provinsi_konsumen = fields.Char(string=' - Provinsi')
    kota_konsumen = fields.Char(string=' - Kota/Kab')
    kecamatan_konsumen = fields.Char(string=' - Kecamatan')
    kelurahan_konsumen = fields.Char(string=' - Kel/Desa')
    rt_rw_konsumen = fields.Char(string=' - RT/RW')
    kodepos_konsumen = fields.Char(string=' - KodePos')
    agama_konsumen = fields.Char(string='Agama')
    status_kawin_konsumen = fields.Char(string='Status Perkawinan')
    pekerjaan_konsumen = fields.Char(string='Pekerjaan')

    # Data Pribadi Lainnya
    telp_konsumen = fields.Char(string='No. Handphone')
    alamat_terkini_konsumen = fields.Char(string='Alamat tempat tinggal saat ini')
    status_kawin_terkini_konsumen = fields.Char(string='Status Perkawinan saat ini')
    jumlah_anak_konsumen = fields.Char(string='Jumlah anak')
    Kendaraan_konsumen = fields.Char(string='Kendaraan yang dimilik')
    nama_kerabat_konsumen = fields.Char(string='Nama kerabat yang bisa dihubungi')
    telp_kerebat_konsumen = fields.Char(string='No. Telp kerabat yang bisa dihubungi')

    # Data Perusahaan / Pekerjaan
    nama_perusahaan_konsumen = fields.Char(string='Nama Perusahaan')
    alamat_perusahaan_konsumen = fields.Char(string='Alamat Perusahaan')
    provinsi_perusahaan_konsumen = fields.Char(string='* Provinsi')
    kota_perusahaan_konsumen = fields.Char(string='* Kota/Kab.')
    kecamatan_perusahaan_konsumen = fields.Char(string='* Kecamatan')
    kelurahan_perusahaan_konsumen = fields.Char(string='* Kel/Desa')
    rt_rw__perusahaan_konsumen = fields.Char(string='* RT/RW')
    telp_perusahaan_konsumen = fields.Char(string='No. Telp. Perusahaan')
    bidang_perusahaan_konsumen = fields.Char(string='Bidang Usaha')
    lamabekerja_perusahaan_konsumen = fields.Char(string='Lama Bekerja')
    jabatan_perusahaan_konsumen = fields.Char(string='Jabatan')
    penghasilan_pokok_konsumen = fields.Char(string='Penghasilan pokok')
    penghasilan_tambahan_konsumen = fields.Char(string='Penghasilan tambahan')

    # Data pasangan
    ktp_pasangan_konsumen = fields.Integer(string='NIK(No.KTP)')
    nama_pasangan_konsumen = fields.Char(string='Nama')
    lahir_pasangan_konsumen = fields.Datetime(string='Tempat/Tgl Lahir')
    jenis_kelamin_pasangan_konsumen = fields.Selection([
        ('laki_laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
        ('pilih', 'Pilih Jenis Kelamin')], string='Jenis Kelamin', default='pilih')
    alamat_pasangan_konsumen = fields.Char(string='Alamat')
    provinsi_pasangan_konsumen = fields.Char(string=' - Provinsi')
    kota_pasangan_konsumen = fields.Char(string=' - Kota/Kab')
    kecamatan_pasangan_konsumen = fields.Char(string=' - Kecamatan')
    kelurahan_pasangan_konsumen = fields.Char(string=' - Kel/Desa')
    rt_rw_pasangan_konsumen = fields.Char(string=' - RT/RW')
    kodepos_pasangan_konsumen = fields.Char(string=' - KodePos')
    agama_pasangan_konsumen = fields.Char(string='Agama')
    status_kawin_pasangan_konsumen = fields.Char(string='Status Perkawinan')
    pekerjaan_pasangan_konsumen = fields.Char(string='Pekerjaan')

    #foto
    foto_diri_konsumen = fields.Binary(string='Foto Diri')
    foto_ktp_konsumen = fields.Binary(string='Foto KTP')
    foto_npwp_konsumen = fields.Binary(string='Foto NPWP')

    # Data NPWP
    foto_npwp_konsumen = fields.Char(string='No.NPWP')
    nama_npwp_konsumen = fields.Char(string='Nama')
    alamat_npwp_konsumen = fields.Text(string='Alamat')

    #status Berkas
    copy_ktp = fields.Selection([
        ('sudah', 'Sudah Diserahkan'),
        ('perempuan', 'Kekurangan')], string='Photo copy KTP suami/istri', default='belum')
    copy_kk = fields.Selection([
        ('sudah', 'Sudah Diserahkan'),
        ('belum', 'Kekurangan')], string='Photo copy KK', default='belum')
    slip_gaji_konsumen = fields.Selection([
        ('sudah', 'Sudah Diserahkan'),
        ('belum', 'Kekurangan')], string='Slip Gaji', default='belum')
    surat_aktif_kerja = fields.Selection([
        ('sudah', 'Sudah Diserahkan'),
        ('belum', 'Kekurangan')], string='Surat Ket. Aktif Bekerja', default='belum')
    rek_tabungan_konsumen = fields.Selection([
        ('sudah', 'Sudah Diserahkan'),
        ('belum', 'Kekurangan')], string='Rek. Tabungan 3 bln terakhir', default='belum')
    pas_foto_konsumen = fields.Selection([
        ('sudah', 'Sudah Diserahkan'),
        ('belum', 'Kekurangan')], string='Pas photo suami/istri', default='belum')
    skbmr_konsumen = fields.Selection([
        ('sudah', 'Sudah Diserahkan'),
        ('belum', 'Kekurangan')], string='SKBMR', default='belum')