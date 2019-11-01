# -*- coding: utf-8 -*-
# Copyright (c) 2019, Kelompok 6 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RequestOrder(Document):
	pass

	def on_submit(self):
		self.on_approve()

	def on_approve(self):
		if(self.docstatus == 1):
			report_order = frappe.new_doc("Report Order")
			report_order.id_pelanggan = self.id_pelanggan
			report_order.nama_pelanggan = self.nama_pelanggan
			for i in self.menu_makanan_line:
				report_order.append('pesanan',{
					'id_menu' : i.id_menu,
					'nama_makanan' : i.nama_makanan,
					'harga' : i.harga,
					'jml' : i.jml
				})
			report_order.kode_voucher = self.kode_voucher
			report_order.potongan_harga = self.potongan_harga
			report_order.harga = self.harga
			report_order.status_pesanan = "Belum Bayar"
			report_order.save()
			new_report_order = frappe.get_doc("Report Order", report_order.name)
			frappe.msgprint(
				'Success Create Report Order with doc no {}'.format(new_report_order))
