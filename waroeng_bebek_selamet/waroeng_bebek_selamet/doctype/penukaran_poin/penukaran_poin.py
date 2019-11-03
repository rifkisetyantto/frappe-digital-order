# -*- coding: utf-8 -*-
# Copyright (c) 2019, Kelompok 6 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PenukaranPoin(Document):
	pass

	def on_submit(self):
		self.on_approve()
		# self.kurang_point()

	def on_approve(self):
		if(self.docstatus == 1):
			tukar_poin = frappe.new_doc("Report Tukar Poin")
			tukar_poin.id_pelanggan = self.id_pelanggan
			tukar_poin.nama_pelanggan = self.nama_pelanggan
			for i in self.menu_makanan_poin_line:
				tukar_poin.append('report_tukar_poin_line',{
					'id_menu' : i.id_menu,
					'nama_makanan' : i.nama_makanan,
					'harga_poin' : i.harga_poin,
					'jumlah' : i.jumlah
				})
			tukar_poin.jml_poin = self.jml_poin
			tukar_poin.save()
			new_tukar_poin = frappe.get_doc("Report Tukar Poin", tukar_poin.name)
			frappe.msgprint(
				'Success Create Report Tukar Poin {}'.format(new_tukar_poin)
			)
			self.kurang_point()

	def kurang_point(self):
		kurangin = frappe.get_doc("Master Pelanggan", self.id_pelanggan)
		kurangin.point = kurangin.point - self.jml_poin
		kurangin.save()
	