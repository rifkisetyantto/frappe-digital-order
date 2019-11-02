# -*- coding: utf-8 -*-
# Copyright (c) 2019, Kelompok 6 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TransaksiPembayaran(Document):
	pass

	# def on_submit(self):
	# 	self.on_approve()

	# def on_approve(self):
	# 	if(self.docstatus == 1):
	# 		transaksi = frappe.new_doc("Report Order")
	# 		transaksi.total_harga = self.total_harga
	# 		transaksi.jml_cash = self.jml_cash
	# 		transaksi.kembalian = self.kembalian
	# 		new_transaksi = frappe.get_doc("Report Order", transaksi.name)
	# 		frappe.msgprint(
	# 			'Success Update Report Order with doc no {}'.format(new_transaksi)
	# 		)

	def validate(self):
		self.tambah_data()
		self.change_status_transaksi()
		self.get_point()

	def change_status_transaksi(self):
		transaksi = frappe.get_doc("Report Order",self.id_pelanggan)
		transaksi.status_pesanan = "Sudah Bayar"
		transaksi.save()

	def tambah_data(self):
		transaksi_1 = frappe.new_doc("Report Order")
		transaksi_1.total_harga = self.total_harga
		transaksi_1.jml_cash = self.jml_cash
		transaksi_1.kembalian = self.kembalian
		transaksi_1.save()

	def get_point(self):
		getpoint = frappe.new_doc("Master Pelanggan")
		getpoint.estimasi_point += self.point
		getpoint.save()