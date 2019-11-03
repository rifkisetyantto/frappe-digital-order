# -*- coding: utf-8 -*-
# Copyright (c) 2019, Kelompok 6 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TransaksiPembayaran(Document):
	pass

	def validate(self):
		self.change_status_transaksi()
		self.get_point()

	def change_status_transaksi(self):
		transaksi = frappe.get_doc("Report Order",self.id_order)
		transaksi.status_pesanan = "Sudah Bayar"
		transaksi.total_harga = self.total_harga
		transaksi.jml_cash = self.jml_cash
		transaksi.kembalian = self.kembalian
		transaksi.save()

	def get_point(self):
		getpoint = frappe.get_doc("Master Pelanggan",self.id_pelanggan)
		getpoint.point += self.estimasi_point
		getpoint.save()