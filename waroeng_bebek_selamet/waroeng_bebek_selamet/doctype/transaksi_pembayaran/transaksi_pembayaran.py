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
		self.change_status_transaksi()

	def change_status_transaksi(self):
		transaksi = frappe.get_doc("Report Order",self.id_order)
		transaksi.status_pesanan = "Sudah Bayar"
		transaksi.save()