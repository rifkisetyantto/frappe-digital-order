// Copyright (c) 2019, Kelompok 6 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transaksi Pembayaran', {
	id_pelanggan: function(frm) {
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Master Pelanggan",
				name: frm.doc.id_pelanggan
			},
			callback: function(r){
				if(r.message.status == 'Gold'){
					let dapet_poin = frm.doc.total_harga * 0.07
					frm.set_value("estimasi_point",dapet_poin)
				}
				else if(r.message.status == 'Silver'){
					let dapet_poin = frm.doc.total_harga * 0.05
					frm.set_value("estimasi_point",dapet_poin)
				}
				else{
					let dapet_poin = frm.doc.total_harga * 0.03
					frm.set_value("estimasi_point",dapet_poin)
				}
			}
		});
	},

	jml_cash: function(frm) {
		hitung_kembalian(frm);
	},

	harga: function(frm) {
		total_harga(frm);
	},

	potongan_harga: function(frm) {
		total_harga(frm);
	}
});

let hitung_kembalian = function(frm) {
	let harga = frm.doc.harga
	let potongan = frm.doc.potongan_harga
	let jumlah_cash = frm.doc.jml_cash

	let total = harga-potongan
	let kembalian = jumlah_cash-total
	frm.set_value("kembalian",kembalian)
}

let total_harga = function(frm) {
	let harga = frm.doc.harga
	let potongan = frm.doc.potongan_harga

	let total = harga-potongan
	frm.set_value("total_harga",total)
}