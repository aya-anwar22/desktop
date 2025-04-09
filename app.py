import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

def connect_db():
    return mysql.connector.connect(
        host="mysql-396ee2a4-aya786930-b86b.k.aivencloud.com",
        user="avnadmin",
        database="defaultdb",
        port=18280
    )

class AppStyle:
    def __init__(self):
        self.bg_color = "#f0f0f0"
        self.primary_color = "#4a6fa5"
        self.secondary_color = "#166088"
        self.accent_color = "#4fc3f7"
        self.font = ("Arial", 10)
        self.title_font = ("Arial", 12, "bold")

#Home page
class MainApp:
    def __init__(self, root):
        self.root = root
        self.style = AppStyle()
        self.setup_ui()
        
    def setup_ui(self):
        self.root.title("نظام إدارة المنسوجات - الصفحة الرئيسية")
        self.root.geometry("800x600")
        self.root.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.root, bg=self.style.primary_color, height=80)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="نظام إدارة المنسوجات", 
                             font=("Arial", 18, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=20)
        
        content_frame = tk.Frame(self.root, bg=self.style.bg_color)
        content_frame.pack(pady=40, fill=tk.BOTH, expand=True)
        
        btn_frame = tk.Frame(content_frame, bg=self.style.bg_color)
        btn_frame.pack(pady=20)
        
        suppliers_btn = tk.Button(btn_frame, text="إدارة الموردين", font=self.style.title_font,
                                bg=self.style.secondary_color, fg="white", width=20, height=2,
                                command=self.open_suppliers)
        suppliers_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        fabrics_btn = tk.Button(btn_frame, text="إدارة الأنسجة", font=self.style.title_font,
                              bg=self.style.secondary_color, fg="white", width=20, height=2,
                              command=self.open_fabrics)
        fabrics_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        info_frame = tk.Frame(content_frame, bg=self.style.bg_color)
        info_frame.pack(pady=20)
        
        info_label = tk.Label(info_frame, text="مرحباً بك في نظام إدارة المنسوجات\nاختر الوحدة التي تريد العمل عليها",
                             font=self.style.font, bg=self.style.bg_color)
        info_label.pack()
        
    def open_suppliers(self):
        self.root.withdraw()
        suppliers_window = tk.Toplevel()
        SuppliersPage(suppliers_window, self)
        
    def open_fabrics(self):
        self.root.withdraw()
        fabrics_window = tk.Toplevel()
        FabricsPage(fabrics_window, self)

# Suppliers page
class SuppliersPage:
    def __init__(self, window, main_app):
        self.window = window
        self.main_app = main_app
        self.style = AppStyle()
        self.setup_ui()
        

    def setup_ui(self):
        self.window.title("إدارة الموردين")
        self.window.geometry("1000x700")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة الموردين", 
                            font=("Arial", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)

        top_buttons_frame = tk.Frame(self.window, bg=self.style.bg_color)
        top_buttons_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(top_buttons_frame, text="عرض الكل", font=self.style.font, 
                command=self.show_suppliers).pack(side=tk.LEFT, padx=5)
        tk.Button(top_buttons_frame, text="الانتقال إلى الأنسجة", font=self.style.font,
                command=self.open_fabrics).pack(side=tk.LEFT, padx=5)
        tk.Button(top_buttons_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
                bg="red", command=self.back_to_main).pack(side=tk.RIGHT, padx=5)

        main_frame = tk.Frame(self.window, bg=self.style.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        form_frame = tk.LabelFrame(main_frame, text="بيانات المورد", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(form_frame, text="اسم المورد:", font=self.style.font, bg=self.style.bg_color).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="بيانات التواصل:", font=self.style.font, bg=self.style.bg_color).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.contact_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.contact_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="العنوان:", font=self.style.font, bg=self.style.bg_color).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.address_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)
        
        btn_frame = tk.Frame(form_frame, bg=self.style.bg_color)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="إضافة", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.add_supplier).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="تحديث", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.update_supplier).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="حذف", font=self.style.font, bg="#d32f2f", fg="white",
                command=self.delete_supplier).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="مسح الحقول", font=self.style.font, 
                command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        list_frame = tk.LabelFrame(main_frame, text="قائمة الموردين", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.tree = ttk.Treeview(list_frame, columns=("ID", "Name", "Contact", "Address"), show="headings", height=15)
        
        self.tree.heading("ID", text="المعرف")
        self.tree.heading("Name", text="اسم المورد")
        self.tree.heading("Contact", text="بيانات التواصل")
        self.tree.heading("Address", text="العنوان")
        
        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Name", width=200)
        self.tree.column("Contact", width=200)
        self.tree.column("Address", width=300)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

    def add_supplier(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()

        if not name or not contact or not address:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول المطلوبة")
            return
            
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = "INSERT INTO suppliers (supplier_name, contact_info, supplier_address) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, contact, address))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة المورد بنجاح")
            self.clear_fields()
            self.show_suppliers()
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def show_suppliers(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM suppliers")
            rows = cursor.fetchall()
            
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            for row in rows:
                self.tree.insert("", tk.END, values=row)
                
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء جلب البيانات: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def update_supplier(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار مورد للتحديث")
            return
            
        supplier_id = self.tree.item(selected_item)["values"][0]
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()

        if not name and not contact and not address:
            messagebox.showerror("خطأ", "يرجى إدخال بيانات للتحديث")
            return
            
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = "UPDATE suppliers SET supplier_name=%s, contact_info=%s, supplier_address=%s WHERE supplier_id=%s"
            cursor.execute(sql, (name, contact, address, supplier_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث بيانات المورد بنجاح")
            self.clear_fields()
            self.show_suppliers()
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def delete_supplier(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار مورد للحذف")
            return
            
        supplier_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف هذا المورد؟"):
            try:
                conn = connect_db()
                cursor = conn.cursor()
                sql = "DELETE FROM suppliers WHERE supplier_id=%s"
                cursor.execute(sql, (supplier_id,))
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف المورد بنجاح")
                self.show_suppliers()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
    
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
    
    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.contact_entry.delete(0, tk.END)
            self.contact_entry.insert(0, values[2])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, values[3])
    
    def open_fabrics(self):
        self.window.withdraw()
        fabrics_window = tk.Toplevel()
        FabricsPage(fabrics_window, self.main_app)
    
    def back_to_main(self):
        self.window.destroy()
        self.main_app.root.deiconify()
        self.main_app.root.deiconify()  


class FabricsPage:
    def __init__(self, window, main_app):
        self.window = window
        self.main_app = main_app
        self.style = AppStyle()
        self.setup_ui()
        

    def setup_ui(self):
        self.window.title("إدارة الأنسجة")
        self.window.geometry("1200x800")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة الأنسجة", 
                            font=("Arial", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)
        
        main_frame = tk.Frame(self.window, bg=self.style.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        top_btn_frame = tk.Frame(main_frame, bg=self.style.bg_color)
        top_btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(top_btn_frame, text="عرض الكل", font=self.style.font, 
                command=self.show_fabrics).pack(side=tk.LEFT, padx=5)
        tk.Button(top_btn_frame, text="الانتقال إلى الموردين", font=self.style.font,
                command=self.open_suppliers).pack(side=tk.LEFT, padx=5)
        tk.Button(top_btn_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
                command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        form_frame = tk.LabelFrame(main_frame, text="بيانات النسيج", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(form_frame, text="اسم النسيج:", font=self.style.font, bg=self.style.bg_color).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="نوع النسيج:", font=self.style.font, bg=self.style.bg_color).grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.type_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.type_entry.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(form_frame, text="السعر لكل متر:", font=self.style.font, bg=self.style.bg_color).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.price_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="الكمية المتاحة:", font=self.style.font, bg=self.style.bg_color).grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.quantity_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.quantity_entry.grid(row=1, column=3, padx=5, pady=5)
        
        tk.Label(form_frame, text="معرف المورد:", font=self.style.font, bg=self.style.bg_color).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.supplier_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.supplier_entry.grid(row=2, column=1, padx=5, pady=5)
        
        btn_frame = tk.Frame(form_frame, bg=self.style.bg_color)
        btn_frame.grid(row=3, column=0, columnspan=4, pady=10)
        
        tk.Button(btn_frame, text="إضافة", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.add_fabric).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="تحديث", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.update_fabric).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="حذف", font=self.style.font, bg="#d32f2f", fg="white",
                command=self.delete_fabric).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="مسح الحقول", font=self.style.font, 
                command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        list_frame = tk.LabelFrame(main_frame, text="قائمة الأنسجة", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.tree = ttk.Treeview(list_frame, columns=("ID", "Name", "Type", "Price", "Quantity", "Supplier"), show="headings", height=15)
        
        self.tree.heading("ID", text="المعرف")
        self.tree.heading("Name", text="اسم النسيج")
        self.tree.heading("Type", text="النوع")
        self.tree.heading("Price", text="السعر لكل متر")
        self.tree.heading("Quantity", text="الكمية المتاحة")
        self.tree.heading("Supplier", text="معرف المورد")
        
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Name", width=150)
        self.tree.column("Type", width=120)
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Quantity", width=100, anchor="center")
        self.tree.column("Supplier", width=80, anchor="center")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)
        
        self.show_fabrics()


    
    def add_fabric(self):
        name = self.name_entry.get()
        fabric_type = self.type_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        supplier_id = self.supplier_entry.get()

        if not name or not fabric_type or not price or not quantity or not supplier_id:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول المطلوبة")
            return
            
        try:
            price = float(price)
            quantity = int(quantity)
            supplier_id = int(supplier_id)
            
            conn = connect_db()
            cursor = conn.cursor()
            sql = """INSERT INTO fabrics 
                     (fabric_name, fabric_type, price_per_meter, available_quantity, supplier_id) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (name, fabric_type, price, quantity, supplier_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة النسيج بنجاح")
            self.clear_fields()
            self.show_fabrics()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للسعر والكمية ومعرف المورد")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def show_fabrics(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fabrics")
            rows = cursor.fetchall()
            
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            for row in rows:
                self.tree.insert("", tk.END, values=row)
                
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء جلب البيانات: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def update_fabric(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار نسيج للتحديث")
            return
            
        fabric_id = self.tree.item(selected_item)["values"][0]
        name = self.name_entry.get()
        fabric_type = self.type_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        supplier_id = self.supplier_entry.get()

        if not name and not fabric_type and not price and not quantity and not supplier_id:
            messagebox.showerror("خطأ", "يرجى إدخال بيانات للتحديث")
            return
            
        try:
            conn = connect_db()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM fabrics WHERE fabric_id=%s", (fabric_id,))
            current_data = cursor.fetchone()
            
            name = name if name else current_data[1]
            fabric_type = fabric_type if fabric_type else current_data[2]
            price = float(price) if price else current_data[3]
            quantity = int(quantity) if quantity else current_data[4]
            supplier_id = int(supplier_id) if supplier_id else current_data[5]
            
            sql = """UPDATE fabrics SET 
                     fabric_name=%s, fabric_type=%s, price_per_meter=%s, 
                     available_quantity=%s, supplier_id=%s 
                     WHERE fabric_id=%s"""
            cursor.execute(sql, (name, fabric_type, price, quantity, supplier_id, fabric_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث بيانات النسيج بنجاح")
            self.clear_fields()
            self.show_fabrics()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للسعر والكمية ومعرف المورد")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def delete_fabric(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار نسيج للحذف")
            return
            
        fabric_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف هذا النسيج؟"):
            try:
                conn = connect_db()
                cursor = conn.cursor()
                sql = "DELETE FROM fabrics WHERE fabric_id=%s"
                cursor.execute(sql, (fabric_id,))
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف النسيج بنجاح")
                self.show_fabrics()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
    
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.supplier_entry.delete(0, tk.END)
    
    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.type_entry.delete(0, tk.END)
            self.type_entry.insert(0, values[2])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, values[3])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, values[4])
            self.supplier_entry.delete(0, tk.END)
            self.supplier_entry.insert(0, values[5])
    
    def open_suppliers(self):
        self.window.withdraw()
        suppliers_window = tk.Toplevel()
        SuppliersPage(suppliers_window, self.main_app)


    
    
    def back_to_main(self):
        self.window.destroy()
        self.main_app.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
