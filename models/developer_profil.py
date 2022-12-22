from odoo import models, fields, api


class Developer_profil(models.Model):
    _name = 'samawa_spektrum.developer_profil'
    _description = 'samawa_spektrum.developer_profil'

    nama_dev = fields.Char(string='Nama Developer')
    alamat_dev = fields.Text(string='Alamat')
    telp_dev = fields.Text(string='No.Telp')
    email_dev = fields.Text(string='Email')
    pimpinan_dev = fields.Text(string='Pimpinan')
    proyek_dev_aktif = fields.Text(string='List Proyek Aktif')
    regis_dev = fields.Text(string='Tgl.Registrasi')

    nama_user = fields.Text(string='Nama Lengkap')
    telp_user = fields.Text(string='No.Handphone')
    email_user = fields.Text(string='Email')
    user_id = fields.Text(string='Username')
    level_user = fields.Text(string='Level User')
    status_user = fields.Text(string='Status')
    image = fields.Binary(" ", help="This field holds the image used as avatar for \
        this contact, limited to 1024x1024px",)


    def action_test(self):
        print("Button Di pencet")

