import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

def connect_db():
    try:
        if not os.path.exists('database'):
            os.makedirs('database')
            
        conn = sqlite3.connect('database/textile.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_name TEXT NOT NULL,
                contact_info TEXT,
                supplier_address TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fabrics (
                fabric_id INTEGER PRIMARY KEY AUTOINCREMENT,
                fabric_name TEXT NOT NULL,
                fabric_type TEXT,
                price REAL,
                quantity INTEGER,
                supplier_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workers (
                worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                worker_name TEXT NOT NULL,
                job_title TEXT,
                phone TEXT,
                hire_date TEXT,
                salary REAL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                fabric_id INTEGER,
                sale_date TEXT,
                quantity INTEGER,
                total_price REAL,
                worker_id INTEGER,
                FOREIGN KEY (fabric_id) REFERENCES fabrics (fabric_id),
                FOREIGN KEY (worker_id) REFERENCES workers (worker_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                fabric_id INTEGER,
                receipt_date TEXT,
                received_quantity INTEGER,
                FOREIGN KEY (fabric_id) REFERENCES fabrics (fabric_id)
            )
        ''')
        
        conn.commit()
        return conn
    except Exception as e:
        messagebox.showerror("خطأ في الاتصال", f"حدث خطأ أثناء الاتصال بقاعدة البيانات: {str(e)}")
        return None

class AppStyle:
    def __init__(self):
        self.bg_color = "#f0f0f0"
        self.primary_color = "#4a6fa5"
        self.secondary_color = "#166088"
        self.accent_color = "#4fc3f7"
        self.font = ("Segoe UI", 12)
        self.title_font = ("Segoe UI", 12, "bold")

class btnStyle:
    def __init__(self):
        self.btn_color = "#166088"
        self.btnfont = ("Arial", 25 , "bold")
        self.hover_color = "green"
        self.cor_rad= 3
        self.width = 200
        self.height = 55
        self.brod_bottom = 2
        self.brod_right = 2
        self.brod_color = "black"

class btn2Style:
    def __init__(self):
        self.btn_color = "#196E78"
        self.btnfont = ("Arial", 20, )
        self.hover_color = "white"
        self.cor_rad= 3
        self.width = 150
        self.height = 40
        self.brod_bottom = 2
        self.brod_color = "black"


#Home page
class MainApp:
    def __init__(self, root):
        self.root = root
        self.style = AppStyle()
        self.btnstyle = btnStyle()
        self.setup_ui()
        
    def setup_ui(self):
        self.root.title("نظام إدارة المنسوجات - الصفحة الرئيسية")
        self.root.geometry("800x600")
        self.root.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.root, bg=self.style.primary_color,
                                height=80, highlightthickness=1,  
                                highlightbackground="black")
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="نظام إدارة المنسوجات", 
                               font=("Arial", 18, "bold"),
                               bg=self.style.primary_color, fg="white")
        title_label.pack(pady=20)
        
        content_frame = tk.Frame(self.root, bg=self.style.bg_color)
        content_frame.pack(pady=40, fill=tk.BOTH, expand=True)
        
        btn_frame = tk.Frame(content_frame, bg=self.style.bg_color)
        btn_frame.pack(pady=20)

        suppliers_btn = ctk.CTkButton(btn_frame, text="إدارة الموردين", font=self.btnstyle.btnfont,
                                      fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                      width=self.btnstyle.width, height=self.btnstyle.height,
                                      border_color=self.btnstyle.brod_color,
                                      hover_color=self.btnstyle.hover_color,
                                      border_width=self.btnstyle.brod_bottom,
                                      command=self.open_suppliers)
        suppliers_btn.pack(pady=10, padx=10, side=tk.LEFT)

        fabrics_btn = ctk.CTkButton(btn_frame, text="إدارة الأنسجة", font=self.btnstyle.btnfont,
                                    fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                    width=self.btnstyle.width, height=self.btnstyle.height,
                                    border_color=self.btnstyle.brod_color,
                                    hover_color=self.btnstyle.hover_color,
                                    border_width=self.btnstyle.brod_bottom,
                                    command=self.open_fabrics)
        fabrics_btn.pack(pady=10, padx=10, side=tk.LEFT)

        workers_btn = ctk.CTkButton(btn_frame, text="إدارة العمال", font=self.btnstyle.btnfont,
                                    fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                    width=self.btnstyle.width, height=self.btnstyle.height,
                                    border_color=self.btnstyle.brod_color,
                                    hover_color=self.btnstyle.hover_color,
                                    border_width=self.btnstyle.brod_bottom,
                                    command=self.open_workers)
        workers_btn.pack(pady=10, padx=10, side=tk.LEFT)

        sales_btn = ctk.CTkButton(btn_frame, text="إدارة المبيعات", font=self.btnstyle.btnfont,
                                  fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                  width=self.btnstyle.width, height=self.btnstyle.height,
                                  border_color=self.btnstyle.brod_color,
                                  hover_color=self.btnstyle.hover_color,
                                  border_width=self.btnstyle.brod_bottom,
                                  command=self.open_sales)
        sales_btn.pack(pady=10, padx=10, side=tk.LEFT)

        inventory_btn = ctk.CTkButton(btn_frame, text="إدارة المخزون", font=self.btnstyle.btnfont,
                                      fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                      width=self.btnstyle.width, height=self.btnstyle.height,
                                      border_color=self.btnstyle.brod_color,
                                      hover_color=self.btnstyle.hover_color,
                                      border_width=self.btnstyle.brod_bottom,
                                      command=self.open_inventory)
        inventory_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        info_frame = tk.Frame(content_frame, bg=self.style.bg_color)
        info_frame.pack(pady=20)
        
        info_label = tk.Label(info_frame, text="مرحباً بك في نظام إدارة المنسوجات\nاختر الوحدة التي تريد العمل عليها",
                              font=("Arial", 20), bg=self.style.bg_color)
        info_label.pack()
        
    def open_suppliers(self):
        self.root.withdraw()
        suppliers_window = tk.Toplevel()
        SuppliersPage(suppliers_window, self)
        
    def open_fabrics(self):
        self.root.withdraw()
        fabrics_window = tk.Toplevel()
        FabricsPage(fabrics_window, self)

    def open_workers(self):
        self.root.withdraw()
        workers_window = tk.Toplevel()
        WorkersPage(workers_window, self)

    def open_sales(self):
        self.root.withdraw()
        sales_window = tk.Toplevel()
        SalesPage(sales_window, self)

    def open_inventory(self):
        self.root.withdraw()
        inventory_window = tk.Toplevel()
        InventoryPage(inventory_window, self)


# Suppliers page
class SuppliersPage:
    def __init__(self, window, main_app):
        self.window = window
        self.main_app = main_app
        self.style = AppStyle()
        self.btnstyle = btn2Style()
        self.setup_ui()
        
    def setup_ui(self):
        self.window.title("إدارة الموردين")
        self.window.geometry("1000x700")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60,
                              highlightthickness=1, highlightbackground="black")
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة الموردين", 
                            font=("Segoe UI", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)

        top_btn_frame = tk.Frame(self.window, bg=self.style.bg_color)
        top_btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(top_btn_frame, text="عرض الكل", font=self.style.font, 
                command=self.show_suppliers).pack(side=tk.LEFT, padx=5)
        tk.Button(top_btn_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
                command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        main_frame = tk.Frame(self.window, bg=self.style.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        form_frame = tk.LabelFrame(main_frame, text="بيانات المورد", font=("Segoe UI", 12, "bold"),
                                 bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10)
        
        name_label = tk.Label(form_frame, text=": اسم المورد", font=("Segoe UI", 12),
                            bg=self.style.bg_color)
        name_label.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        self.name_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.name_entry.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        contact_label = tk.Label(form_frame, text=": بيانات التواصل", font=("Segoe UI", 12),
                               bg=self.style.bg_color)
        contact_label.grid(row=1, column=1, padx=5, pady=5, sticky='e')
        self.contact_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.contact_entry.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        address_label = tk.Label(form_frame, text=": العنوان", font=("Segoe UI", 12),
                               bg=self.style.bg_color)
        address_label.grid(row=2, column=1, padx=5, pady=5, sticky='e')
        self.address_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.address_entry.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        
        columns = ('المعرف', 'اسم المورد', 'بيانات التواصل', 'العنوان')
        self.tree = ttk.Treeview(main_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center', width=200)
        
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)
        
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        btn_frame = tk.Frame(main_frame, bg=self.style.bg_color)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ctk.CTkButton(btn_frame, text="إضافة", command=self.add_supplier,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btn_frame, text="تحديث", command=self.update_supplier,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btn_frame, text="حذف", command=self.delete_supplier,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btn_frame, text="مسح الحقول", command=self.clear_fields,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btn_frame, text="حذف جميع البيانات", command=self.clear_all_data,
                     font=("Segoe UI", 12), width=120, fg_color="#d32f2f").pack(side=tk.RIGHT, padx=5)
        
        self.show_suppliers()
    
    def show_suppliers(self):
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
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
            if cursor:
                cursor.close()
            if conn:
                try:
                    conn.close()
                except:
                    pass
    
    def add_supplier(self):
        name = self.name_entry.get().strip()
        contact = self.contact_entry.get().strip()
        address = self.address_entry.get().strip()
        
        if not name or not contact or not address:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول المطلوبة")
            return
            
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            sql = "INSERT INTO suppliers (supplier_name, contact_info, supplier_address) VALUES (?, ?, ?)"
            cursor.execute(sql, (name, contact, address))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة المورد بنجاح")
            self.clear_fields()
            self.show_suppliers()
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                try:
                    conn.close()
                except:
                    pass
    
    def update_supplier(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار مورد للتحديث")
            return
            
        supplier_id = self.tree.item(selected_item)["values"][0]
        name = self.name_entry.get().strip()
        contact = self.contact_entry.get().strip()
        address = self.address_entry.get().strip()
        
        if not name and not contact and not address:
            messagebox.showerror("خطأ", "يرجى إدخال بيانات للتحديث")
            return
            
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            sql = "UPDATE suppliers SET supplier_name=?, contact_info=?, supplier_address=? WHERE supplier_id=?"
            cursor.execute(sql, (name, contact, address, supplier_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث بيانات المورد بنجاح")
            self.clear_fields()
            self.show_suppliers()
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث: {str(e)}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                try:
                    conn.close()
                except:
                    pass
    
    def delete_supplier(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار مورد للحذف")
            return
            
        supplier_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف هذا المورد؟"):
            conn = None
            cursor = None
            try:
                conn = connect_db()
                if conn is None:
                    messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                    return
                    
                cursor = conn.cursor()
                sql = "DELETE FROM suppliers WHERE supplier_id=?"
                cursor.execute(sql, (supplier_id,))
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف المورد بنجاح")
                self.show_suppliers()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف: {str(e)}")
                if conn:
                    conn.rollback()
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    try:
                        conn.close()
                    except:
                        pass
    
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

    def clear_all_data(self):
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف جميع البيانات؟"):
            conn = None
            cursor = None
            try:
                conn = connect_db()
                if conn is None:
                    messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                    return
                    
                cursor = conn.cursor()
                cursor.execute("DELETE FROM suppliers")
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف جميع البيانات بنجاح")
                self.show_suppliers()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء حذف البيانات: {str(e)}")
                if conn:
                    conn.rollback()
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    try:
                        conn.close()
                    except:
                        pass


class FabricsPage:
    def __init__(self, window, main_app):
        self.window = window
        self.main_app = main_app
        self.style = AppStyle()
        self.btnstyle = btn2Style()
        self.setup_ui()
        
    def setup_ui(self):
        self.window.title("إدارة الأنسجة")
        self.window.geometry("1200x800")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60,
                              highlightthickness=1, highlightbackground="black")
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة الأنسجة", 
                            font=("Segoe UI", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)

        top_btn_frame = tk.Frame(self.window, bg=self.style.bg_color)
        top_btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(top_btn_frame, text="عرض الكل", font=self.style.font, 
                command=self.show_fabrics).pack(side=tk.LEFT, padx=5)
        tk.Button(top_btn_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
                command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        main_frame = tk.Frame(self.window, bg=self.style.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        form_frame = tk.LabelFrame(main_frame, text="بيانات النسيج", font=("Segoe UI", 12, "bold"),
                                 bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10)
        
        # تحديث حقول الإدخال
        name_label = tk.Label(form_frame, text=": اسم النسيج", font=("Segoe UI", 12),
                            bg=self.style.bg_color)
        name_label.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        self.name_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.name_entry.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        type_label = tk.Label(form_frame, text=": نوع النسيج", font=("Segoe UI", 12),
                            bg=self.style.bg_color)
        type_label.grid(row=1, column=1, padx=5, pady=5, sticky='e')
        self.type_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.type_entry.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        price_label = tk.Label(form_frame, text=": السعر", font=("Segoe UI", 12),
                             bg=self.style.bg_color)
        price_label.grid(row=2, column=1, padx=5, pady=5, sticky='e')
        self.price_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.price_entry.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        
        quantity_label = tk.Label(form_frame, text=": الكمية", font=("Segoe UI", 12),
                                bg=self.style.bg_color)
        quantity_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        self.quantity_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.quantity_entry.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        
        supplier_id_label = tk.Label(form_frame, text=": معرف المورد", font=("Segoe UI", 12),
                                   bg=self.style.bg_color)
        supplier_id_label.grid(row=4, column=1, padx=5, pady=5, sticky='e')
        self.supplier_id_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=40, justify='right')
        self.supplier_id_entry.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        
        columns = ('المعرف', 'اسم النسيج', 'النوع', 'السعر', 'الكمية', 'معرف المورد')
        self.tree = ttk.Treeview(main_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center', width=150)
        
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)
        
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        btn_frame = tk.Frame(main_frame, bg=self.style.bg_color)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ctk.CTkButton(btn_frame, text="إضافة", command=self.add_fabric,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btn_frame, text="تحديث", command=self.update_fabric,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btn_frame, text="حذف", command=self.delete_fabric,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btn_frame, text="مسح الحقول", command=self.clear_fields,
                     font=("Segoe UI", 12), width=120).pack(side=tk.RIGHT, padx=5)
        
        self.show_fabrics()

    def show_fabrics(self):
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
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
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def add_fabric(self):
        try:
            name = self.name_entry.get().strip()
            fabric_type = self.type_entry.get().strip()
            price = float(self.price_entry.get().strip())
            quantity = int(self.quantity_entry.get().strip())
            supplier_id = int(self.supplier_id_entry.get().strip())
            
            if not name or not fabric_type:
                messagebox.showerror("خطأ", "يرجى ملء جميع الحقول المطلوبة")
                return
                
            conn = None
            cursor = None
            try:
                conn = connect_db()
                if conn is None:
                    messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                    return
                    
                cursor = conn.cursor()
                sql = "INSERT INTO fabrics (fabric_name, fabric_type, price, quantity, supplier_id) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(sql, (name, fabric_type, price, quantity, supplier_id))
                conn.commit()
                messagebox.showinfo("نجاح", "تم إضافة النسيج بنجاح")
                self.clear_fields()
                self.show_fabrics()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
                if conn:
                    conn.rollback()
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للسعر والكمية ومعرف المورد")

    def update_fabric(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار نسيج للتحديث")
            return
            
        fabric_id = self.tree.item(selected_item)["values"][0]
        name = self.name_entry.get().strip()
        fabric_type = self.type_entry.get().strip()
        price = self.price_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        supplier_id = self.supplier_id_entry.get().strip()
        
        if not any([name, fabric_type, price, quantity, supplier_id]):
            messagebox.showerror("خطأ", "يرجى إدخال بيانات للتحديث")
            return
            
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            sql = """UPDATE fabrics 
                    SET fabric_name=?, fabric_type=?, price=?, quantity=?, supplier_id=? 
                    WHERE fabric_id=?"""
            cursor.execute(sql, (name, fabric_type, price, quantity, supplier_id, fabric_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث بيانات النسيج بنجاح")
            self.clear_fields()
            self.show_fabrics()
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث: {str(e)}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                try:
                    conn.close()
                except:
                    pass

    def delete_fabric(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار نسيج للحذف")
            return
            
        fabric_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف هذا النسيج؟"):
            conn = None
            cursor = None
            try:
                conn = connect_db()
                if conn is None:
                    messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                    return
                    
                cursor = conn.cursor()
                sql = "DELETE FROM fabrics WHERE fabric_id=?"
                cursor.execute(sql, (fabric_id,))
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف النسيج بنجاح")
                self.show_fabrics()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف: {str(e)}")
                if conn:
                    conn.rollback()
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    try:
                        conn.close()
                    except:
                        pass

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.supplier_id_entry.delete(0, tk.END)

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
            self.supplier_id_entry.delete(0, tk.END)
            self.supplier_id_entry.insert(0, values[5])
    
    def open_suppliers(self):
        self.window.withdraw()
        suppliers_window = tk.Toplevel()
        SuppliersPage(suppliers_window, self.main_app)

    def back_to_main(self):
        self.window.destroy()
        self.main_app.root.deiconify()


class WorkersPage:
    def __init__(self, window, main_app):
        self.window = window
        self.main_app = main_app
        self.style = AppStyle()
        self.setup_ui()
        
    def setup_ui(self):
        self.window.title("إدارة العمال")
        self.window.geometry("1000x700")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة العمال", 
                            font=("Arial", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)
        
        top_btn_frame = tk.Frame(self.window, bg=self.style.bg_color)
        top_btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(top_btn_frame, text="عرض الكل", font=self.style.font, 
                command=self.show_workers).pack(side=tk.LEFT, padx=5)
        tk.Button(top_btn_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
                command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        form_frame = tk.LabelFrame(self.window, text="بيانات العامل", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10, padx=20)
        
        tk.Label(form_frame, text="اسم العامل:", font=self.style.font, bg=self.style.bg_color).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="المسمى الوظيفي:", font=self.style.font, bg=self.style.bg_color).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.job_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.job_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="رقم الهاتف:", font=self.style.font, bg=self.style.bg_color).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.phone_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="تاريخ التعيين:", font=self.style.font, bg=self.style.bg_color).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.hire_date_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.hire_date_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="الراتب:", font=self.style.font, bg=self.style.bg_color).grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.salary_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.salary_entry.grid(row=4, column=1, padx=5, pady=5)
        
        btn_frame = tk.Frame(form_frame, bg=self.style.bg_color)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="إضافة", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.add_worker).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="تحديث", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.update_worker).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="حذف", font=self.style.font, bg="#d32f2f", fg="white",
                command=self.delete_worker).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="مسح الحقول", font=self.style.font, 
                command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        list_frame = tk.LabelFrame(self.window, text="قائمة العمال", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        
        self.tree = ttk.Treeview(list_frame, columns=("ID", "Name", "Job", "Phone", "HireDate", "Salary"), show="headings", height=15)
        
        self.tree.heading("ID", text="المعرف")
        self.tree.heading("Name", text="اسم العامل")
        self.tree.heading("Job", text="المسمى الوظيفي")
        self.tree.heading("Phone", text="رقم الهاتف")
        self.tree.heading("HireDate", text="تاريخ التعيين")
        self.tree.heading("Salary", text="الراتب")
        
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Name", width=150)
        self.tree.column("Job", width=120)
        self.tree.column("Phone", width=120)
        self.tree.column("HireDate", width=120)
        self.tree.column("Salary", width=100, anchor="center")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)
        
        self.show_workers()
    
    def show_workers(self):
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workers")
            rows = cursor.fetchall()
            
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            for row in rows:
                self.tree.insert("", tk.END, values=row)
                
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء جلب البيانات: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def add_worker(self):
        name = self.name_entry.get()
        job = self.job_entry.get()
        phone = self.phone_entry.get()
        hire_date = self.hire_date_entry.get()
        salary = self.salary_entry.get()

        if not name or not job or not phone or not hire_date or not salary:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول المطلوبة")
            return
            
        try:
            salary = float(salary)
            
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            sql = """INSERT INTO workers 
                     (worker_name, job_title, phone_number, hire_date, salary) 
                     VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(sql, (name, job, phone, hire_date, salary))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة العامل بنجاح")
            self.clear_fields()
            self.show_workers()
            cursor.close()
            conn.close()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيمة صحيحة للراتب")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
            if conn:
                conn.rollback()
                conn.close()
    
    def update_worker(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار عامل للتحديث")
            return
            
        worker_id = self.tree.item(selected_item)["values"][0]
        name = self.name_entry.get()
        job = self.job_entry.get()
        phone = self.phone_entry.get()
        hire_date = self.hire_date_entry.get()
        salary = self.salary_entry.get()

        if not name and not job and not phone and not hire_date and not salary:
            messagebox.showerror("خطأ", "يرجى إدخال بيانات للتحديث")
            return
            
        try:
            conn = connect_db()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM workers WHERE worker_id=%s", (worker_id,))
            current_data = cursor.fetchone()
            
            name = name if name else current_data[1]
            job = job if job else current_data[2]
            phone = phone if phone else current_data[3]
            hire_date = hire_date if hire_date else current_data[4]
            salary = float(salary) if salary else current_data[5]
            
            sql = """UPDATE workers SET 
                     worker_name=%s, job_title=%s, phone_number=%s, 
                     hire_date=%s, salary=%s 
                     WHERE worker_id=%s"""
            cursor.execute(sql, (name, job, phone, hire_date, salary, worker_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث بيانات العامل بنجاح")
            self.clear_fields()
            self.show_workers()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للراتب")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def delete_worker(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار عامل للحذف")
            return
            
        worker_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف هذا العامل؟"):
            try:
                conn = connect_db()
                cursor = conn.cursor()
                sql = "DELETE FROM workers WHERE worker_id=%s"
                cursor.execute(sql, (worker_id,))
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف العامل بنجاح")
                self.show_workers()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
    
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.job_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.hire_date_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
    
    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.job_entry.delete(0, tk.END)
            self.job_entry.insert(0, values[2])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, values[3])
            self.hire_date_entry.delete(0, tk.END)
            self.hire_date_entry.insert(0, values[4])
            self.salary_entry.delete(0, tk.END)
            self.salary_entry.insert(0, values[5])
    
    def back_to_main(self):
        self.window.destroy()
        self.main_app.root.deiconify()

class SalesPage:
    def __init__(self, window, main_app):
        self.window = window
        self.main_app = main_app
        self.style = AppStyle()
        self.setup_ui()
        
    def setup_ui(self):
        self.window.title("إدارة المبيعات")
        self.window.geometry("1200x800")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة المبيعات", 
                            font=("Arial", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)
        
        top_btn_frame = tk.Frame(self.window, bg=self.style.bg_color)
        top_btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(top_btn_frame, text="عرض الكل", font=self.style.font, 
                command=self.show_sales).pack(side=tk.LEFT, padx=5)
        tk.Button(top_btn_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
                command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        form_frame = tk.LabelFrame(self.window, text="بيانات البيع", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10, padx=20)
        
        tk.Label(form_frame, text="معرف النسيج:", font=self.style.font, bg=self.style.bg_color).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.fabric_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.fabric_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="تاريخ البيع:", font=self.style.font, bg=self.style.bg_color).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="الكمية المباعة:", font=self.style.font, bg=self.style.bg_color).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.quantity_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="السعر الإجمالي:", font=self.style.font, bg=self.style.bg_color).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.price_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="معرف العامل:", font=self.style.font, bg=self.style.bg_color).grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.worker_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.worker_entry.grid(row=4, column=1, padx=5, pady=5)
        
        btn_frame = tk.Frame(form_frame, bg=self.style.bg_color)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="إضافة", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.add_sale).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="تحديث", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.update_sale).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="حذف", font=self.style.font, bg="#d32f2f", fg="white",
                command=self.delete_sale).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="مسح الحقول", font=self.style.font, 
                command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        list_frame = tk.LabelFrame(self.window, text="قائمة المبيعات", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        
        self.tree = ttk.Treeview(list_frame, columns=("ID", "Fabric", "Date", "Quantity", "Price", "Worker"), show="headings", height=15)
        
        self.tree.heading("ID", text="المعرف")
        self.tree.heading("Fabric", text="معرف النسيج")
        self.tree.heading("Date", text="تاريخ البيع")
        self.tree.heading("Quantity", text="الكمية المباعة")
        self.tree.heading("Price", text="السعر الإجمالي")
        self.tree.heading("Worker", text="معرف العامل")
        
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Fabric", width=100, anchor="center")
        self.tree.column("Date", width=120)
        self.tree.column("Quantity", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Worker", width=100, anchor="center")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)
        
        self.show_sales()
    
    def show_sales(self):
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sales")
            rows = cursor.fetchall()
            
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            for row in rows:
                self.tree.insert("", tk.END, values=row)
                
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء جلب البيانات: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def add_sale(self):
        fabric_id = self.fabric_entry.get()
        sale_date = self.date_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        worker_id = self.worker_entry.get()

        if not fabric_id or not sale_date or not quantity or not price or not worker_id:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول المطلوبة")
            return
            
        try:
            fabric_id = int(fabric_id)
            quantity = int(quantity)
            price = float(price)
            worker_id = int(worker_id)
            
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            sql = """INSERT INTO sales 
                     (fabric_id, sale_date, quantity, total_price, worker_id) 
                     VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(sql, (fabric_id, sale_date, quantity, price, worker_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة عملية البيع بنجاح")
            self.clear_fields()
            self.show_sales()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للأرقام")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
            if conn:
                conn.rollback()
                conn.close()
    
    def update_sale(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار عملية بيع للتحديث")
            return
            
        sale_id = self.tree.item(selected_item)["values"][0]
        fabric_id = self.fabric_entry.get()
        sale_date = self.date_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        worker_id = self.worker_entry.get()

        if not fabric_id and not sale_date and not quantity and not price and not worker_id:
            messagebox.showerror("خطأ", "يرجى إدخال بيانات للتحديث")
            return
            
        try:
            conn = connect_db()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM sales WHERE sale_id=%s", (sale_id,))
            current_data = cursor.fetchone()
            
            fabric_id = int(fabric_id) if fabric_id else current_data[1]
            sale_date = sale_date if sale_date else current_data[2]
            quantity = int(quantity) if quantity else current_data[3]
            price = float(price) if price else current_data[4]
            worker_id = int(worker_id) if worker_id else current_data[5]
            
            sql = """UPDATE sales SET 
                     fabric_id=%s, sale_date=%s, quantity=%s, 
                     total_price=%s, worker_id=%s 
                     WHERE sale_id=%s"""
            cursor.execute(sql, (fabric_id, sale_date, quantity, price, worker_id, sale_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث عملية البيع بنجاح")
            self.clear_fields()
            self.show_sales()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للأرقام")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def delete_sale(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار عملية بيع للحذف")
            return
            
        sale_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف عملية البيع هذه؟"):
            try:
                conn = connect_db()
                cursor = conn.cursor()
                sql = "DELETE FROM sales WHERE sale_id=%s"
                cursor.execute(sql, (sale_id,))
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف عملية البيع بنجاح")
                self.show_sales()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
    
    def clear_fields(self):
        self.fabric_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.worker_entry.delete(0, tk.END)
    
    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            self.fabric_entry.delete(0, tk.END)
            self.fabric_entry.insert(0, values[1])
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, values[2])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, values[3])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, values[4])
            self.worker_entry.delete(0, tk.END)
            self.worker_entry.insert(0, values[5])
    
    def back_to_main(self):
        self.window.destroy()
        self.main_app.root.deiconify()

class InventoryPage:
    def __init__(self, window, main_app):
        self.window = window
        self.main_app = main_app
        self.style = AppStyle()
        self.setup_ui()
        
    def setup_ui(self):
        self.window.title("إدارة المخزون")
        self.window.geometry("1000x700")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة المخزون", 
                            font=("Arial", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)
        
        top_btn_frame = tk.Frame(self.window, bg=self.style.bg_color)
        top_btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(top_btn_frame, text="عرض الكل", font=self.style.font, 
                command=self.show_inventory).pack(side=tk.LEFT, padx=5)
        tk.Button(top_btn_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
                command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        form_frame = tk.LabelFrame(self.window, text="بيانات المخزون", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10, padx=20)
        
        tk.Label(form_frame, text="معرف النسيج:", font=self.style.font, bg=self.style.bg_color).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.fabric_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.fabric_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="تاريخ الاستلام:", font=self.style.font, bg=self.style.bg_color).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="الكمية المستلمة:", font=self.style.font, bg=self.style.bg_color).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.quantity_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)
        
        btn_frame = tk.Frame(form_frame, bg=self.style.bg_color)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="إضافة", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.add_inventory).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="تحديث", font=self.style.font, bg=self.style.secondary_color, fg="white",
                command=self.update_inventory).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="حذف", font=self.style.font, bg="#d32f2f", fg="white",
                command=self.delete_inventory).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="مسح الحقول", font=self.style.font, 
                command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        list_frame = tk.LabelFrame(self.window, text="قائمة المخزون", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        
        self.tree = ttk.Treeview(list_frame, columns=("ID", "Fabric", "Date", "Quantity"), show="headings", height=15)
        
        self.tree.heading("ID", text="المعرف")
        self.tree.heading("Fabric", text="معرف النسيج")
        self.tree.heading("Date", text="تاريخ الاستلام")
        self.tree.heading("Quantity", text="الكمية المستلمة")
        
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Fabric", width=100, anchor="center")
        self.tree.column("Date", width=120)
        self.tree.column("Quantity", width=100, anchor="center")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)
        
        self.show_inventory()
    
    def show_inventory(self):
        conn = None
        cursor = None
        try:
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()
            
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            for row in rows:
                self.tree.insert("", tk.END, values=row)
                
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء جلب البيانات: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def add_inventory(self):
        fabric_id = self.fabric_entry.get()
        receipt_date = self.date_entry.get()
        quantity = self.quantity_entry.get()

        if not fabric_id or not receipt_date or not quantity:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول المطلوبة")
            return
            
        try:
            fabric_id = int(fabric_id)
            quantity = int(quantity)
            
            conn = connect_db()
            if conn is None:
                messagebox.showerror("خطأ", "فشل الاتصال بقاعدة البيانات")
                return
                
            cursor = conn.cursor()
            sql = """INSERT INTO inventory 
                     (fabric_id, receipt_date, received_quantity) 
                     VALUES (?, ?, ?)"""
            cursor.execute(sql, (fabric_id, receipt_date, quantity))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة المخزون بنجاح")
            self.clear_fields()
            self.show_inventory()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للأرقام")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
            if conn:
                conn.rollback()
                conn.close()
    
    def update_inventory(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار مخزون للتحديث")
            return
            
        inventory_id = self.tree.item(selected_item)["values"][0]
        fabric_id = self.fabric_entry.get()
        receipt_date = self.date_entry.get()
        quantity = self.quantity_entry.get()

        if not fabric_id and not receipt_date and not quantity:
            messagebox.showerror("خطأ", "يرجى إدخال بيانات للتحديث")
            return
            
        try:
            conn = connect_db()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM inventory WHERE inventory_id=%s", (inventory_id,))
            current_data = cursor.fetchone()
            
            fabric_id = int(fabric_id) if fabric_id else current_data[1]
            receipt_date = receipt_date if receipt_date else current_data[2]
            quantity = int(quantity) if quantity else current_data[3]
            
            sql = """UPDATE inventory SET 
                     fabric_id=%s, receipt_date=%s, received_quantity=%s 
                     WHERE inventory_id=%s"""
            cursor.execute(sql, (fabric_id, receipt_date, quantity, inventory_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث المخزون بنجاح")
            self.clear_fields()
            self.show_inventory()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للأرقام")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def delete_inventory(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("خطأ", "يرجى اختيار مخزون للحذف")
            return
            
        inventory_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف هذا المخزون؟"):
            try:
                conn = connect_db()
                cursor = conn.cursor()
                sql = "DELETE FROM inventory WHERE inventory_id=%s"
                cursor.execute(sql, (inventory_id,))
                conn.commit()
                messagebox.showinfo("نجاح", "تم حذف المخزون بنجاح")
                self.show_inventory()
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
    
    def clear_fields(self):
        self.fabric_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
    
    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            self.fabric_entry.delete(0, tk.END)
            self.fabric_entry.insert(0, values[1])
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, values[2])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, values[3])
    
    def back_to_main(self):
        self.window.destroy()
        self.main_app.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
