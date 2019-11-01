// Copyright (c) 2019, Kelompok 6 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transaksi Pembayaran', {
	id_pesanan: function(frm) {
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Master Pelanggan",
				name: frm.doc.id_pelanggan
			},
		callback: function(r){
			if(r.message){
				frm.set_value('nama_pelanggan',r.message.nama_pelanggan);
				frm.set_value('status',r.message.status);
				frm.set_value('point',r.message.point);
			}
		}
		})
	},
	metode_pembayaran: function(frm){
		if(metode_pembayaran == 'Point'){
			//proses
		}
		else{
			// proses cash
		}
	}
});
