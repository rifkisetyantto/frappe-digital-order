// Copyright (c) 2019, Kelompok 6 and contributors
// For license information, please see license.txt


		frappe.ui.form.on("Menu Makanan Line", {

			jml: function(frm,cdt, cdn){
				jumlah_total(frm, cdt, cdn);
			},
		
			harga: function(frm, cdt, cdn){
				jumlah_total(frm, cdt, cdn);
			}
		});
		
		let jumlah_total = function(frm, cdt, cdn) {
		let d = locals[cdt][cdn];
		frappe.model.set_value(cdt, cdn, "sub_total", d.jml * d.harga);
		}
		
		frappe.ui.form.on("Menu Makanan Line", "sub_total", function(frm, cdt, cdn) {
		
		   let sub_total = frm.doc.menu_makanan_line
		   let total_harga = 0
		   for(let a in sub_total) {
			total_harga = total_harga + sub_total[a].sub_total
			}
		
			frm.set_value("harga",total_harga)
		})