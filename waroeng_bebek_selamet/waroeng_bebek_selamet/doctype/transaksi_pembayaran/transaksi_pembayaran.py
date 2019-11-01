# -*- coding: utf-8 -*-
# Copyright (c) 2019, Kelompok 6 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TransaksiPembayaran(Document):
	pass

	def on_submit(self):
		self.change_status_transaksi()

	def change_status_transaksi(self):
		if(self.id_pesanan):
			bayar = frappe.get_doc("Report Order",self.id_pelanggan)
			bayar.status = 'Sudah Bayar'
			bayar.save()