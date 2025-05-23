import tkinter as tk
import customtkinter as ctk
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
        self.font = ("Arial", 15)
        self.title_font = ("Arial", 12, "bold")

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

        # زر إدارة الموردين
        suppliers_btn = ctk.CTkButton(btn_frame, text="إدارة الموردين", font=self.btnstyle.btnfont,
                                      fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                      width=self.btnstyle.width, height=self.btnstyle.height,
                                      border_color=self.btnstyle.brod_color,
                                      hover_color=self.btnstyle.hover_color,
                                      border_width=self.btnstyle.brod_bottom,
                                      command=self.open_suppliers)
        suppliers_btn.pack(pady=10, padx=10, side=tk.LEFT)

        # زر إدارة الأنسجة
        fabrics_btn = ctk.CTkButton(btn_frame, text="إدارة الأنسجة", font=self.btnstyle.btnfont,
                                    fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                    width=self.btnstyle.width, height=self.btnstyle.height,
                                    border_color=self.btnstyle.brod_color,
                                    hover_color=self.btnstyle.hover_color,
                                    border_width=self.btnstyle.brod_bottom,
                                    command=self.open_fabrics)
        fabrics_btn.pack(pady=10, padx=10, side=tk.LEFT)

        # زر إدارة العمال
        workers_btn = ctk.CTkButton(btn_frame, text="إدارة العمال", font=self.btnstyle.btnfont,
                                    fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                    width=self.btnstyle.width, height=self.btnstyle.height,
                                    border_color=self.btnstyle.brod_color,
                                    hover_color=self.btnstyle.hover_color,
                                    border_width=self.btnstyle.brod_bottom,
                                    command=self.open_workers)
        workers_btn.pack(pady=10, padx=10, side=tk.LEFT)

        # زر إدارة المبيعات
        sales_btn = ctk.CTkButton(btn_frame, text="إدارة المبيعات", font=self.btnstyle.btnfont,
                                  fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                  width=self.btnstyle.width, height=self.btnstyle.height,
                                  border_color=self.btnstyle.brod_color,
                                  hover_color=self.btnstyle.hover_color,
                                  border_width=self.btnstyle.brod_bottom,
                                  command=self.open_sales)
        sales_btn.pack(pady=10, padx=10, side=tk.LEFT)

        # زر إدارة المخزون
        inventory_btn = ctk.CTkButton(btn_frame, text="إدارة المخزون", font=self.btnstyle.btnfont,
                                      fg_color="#166088", corner_radius=self.btnstyle.cor_rad,
                                      width=self.btnstyle.width, height=self.btnstyle.height,
                                      border_color=self.btnstyle.brod_color,
                                      hover_color=self.btnstyle.hover_color,
                                      border_width=self.btnstyle.brod_bottom,
                                      command=self.open_inventory)
        inventory_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        # رسالة الترحيب
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
        self.btnstyle= btn2Style()
        self.setup_ui()
        
    def setup_ui(self):
        self.window.title("إدارة الموردين")
        self.window.geometry("1000x700")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60
                                ,highlightthickness=1,  
                                highlightbackground="black")
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة الموردين", 
                            font=("Arial", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)
        
        main_frame = tk.Frame(self.window, bg=self.style.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        
        form_frameManage = tk.LabelFrame(main_frame, text="Manage", font=self.style.title_font,
                                    bg=self.style.bg_color, padx=10, pady=10)
        form_frameManage.pack(fill=tk.X, pady=10)
        
        ctk.CTkButton(form_frameManage, text="عرض الكل", font=self.btnstyle.btnfont,
                    hover_color=self.btnstyle.hover_color ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.show_suppliers ).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        # tk.Button(form_frameManage, text="الانتقال إلى الأنسجة", font=self.style.font,
        #         command=self.open_fabrics).pack(side=tk.LEFT, padx=5)
        
        ctk.CTkButton(form_frameManage, text="الانتقال إلى الأنسجة",
                    font=self.btnstyle.btnfont,
                    hover_color=self.btnstyle.hover_color ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.open_fabrics ).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        
        ctk.CTkButton(form_frameManage, text="العودة للصفحة الرئيسية " , font=self.btnstyle.btnfont,
                    hover_color=self.btnstyle.hover_color ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.back_to_main).pack(side=tk.RIGHT, padx=5 , pady =5)
        # tk.Button(top_buttons_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
        #         bg="red", command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        form_frame = tk.LabelFrame(main_frame, text=": بيانات المورد", font=self.style.title_font,
                                    bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(form_frame, text=": اسم المورد",
                font=self.style.font,
                bg=self.style.bg_color).grid(
                row=0,
                column=5,
                sticky="e",
                padx=5, pady=5
                )
        self.name_entry = tk.Entry(form_frame
                                , font=self.style.font
                                , width=30)
        self.name_entry.grid(row=0
                            , column=0
                            , padx=5
                            , pady=5)
        
        tk.Label(form_frame,
                text=": بيانات التواصل"
                , font=self.style.font
                , bg=self.style.bg_color).grid(row=1
                                            , column=5
                                            , sticky="e"
                                            , padx=5
                                            , pady=5)
        self.contact_entry = tk.Entry(form_frame,
                                    font=self.style.font
                                    , width=30)
        self.contact_entry.grid(row=1
                                , column=0
                                , padx=5
                                , pady=5)
        
        tk.Label(form_frame,
                text=": العنوان"
                , font=self.style.font
                , bg=self.style.bg_color).grid(row=2
                                            , column=5
                                            , sticky="e"
                                            , padx=5
                                            , pady=5)
                
        self.address_entry = tk.Entry(form_frame
                                    , font=self.style.font
                                    , width=30)
        self.address_entry.grid(row=2
                                , column=0
                                , padx=5
                                , pady=5)
        
        btn_frame = tk.Frame(form_frame, bg=self.style.bg_color)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        # tk.Button(btn_frame, text="إضافة", font=self.style.font, bg=self.style.secondary_color, fg="white",
        #         command=self.add_supplier).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(btn_frame, text="إضافة" ,font=self.btnstyle.btnfont,
                    hover_color="green" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.add_supplier).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        
        # tk.Button(btn_frame, text="تحديث", font=self.style.font, bg=self.style.secondary_color, fg="white",
        #         command=self.update_supplier).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(btn_frame, text="تحديث"  ,font=self.btnstyle.btnfont,
                    hover_color="green",
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.update_supplier).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        
        
        # tk.Button(btn_frame, text="حذف", font=self.style.font, bg="#d32f2f", fg="white",
        #         command=self.delete_supplier).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(btn_frame, text="حذف" ,font=self.btnstyle.btnfont,
                    hover_color="red",
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.delete_supplier).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        
        # tk.Button(btn_frame, text="مسح الحقول", font=self.style.font, 
        #         command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(btn_frame,text="مسح الحقول" ,font=self.btnstyle.btnfont,
                    hover_color="red" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        
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
        self.btnstyle= btn2Style()
        self.setup_ui()
        
    def setup_ui(self):
        self.window.title("إدارة الأنسجة")
        self.window.geometry("1200x800")
        self.window.configure(bg=self.style.bg_color)
        
        header_frame = tk.Frame(self.window, bg=self.style.primary_color, height=60
                                ,highlightthickness=1,  
                                highlightbackground="black")
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="إدارة الأنسجة", 
                            font=("Arial", 16, "bold"), bg=self.style.primary_color, fg="white")
        title_label.pack(pady=15)
        
        main_frame = tk.Frame(self.window, bg=self.style.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        top_btn_frame = tk.Frame(main_frame, bg=self.style.bg_color)
        top_btn_frame.pack(fill=tk.X, pady=10)
        
        
        btnn_frame = tk.LabelFrame(main_frame, text="Manage", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        btnn_frame.pack(fill=tk.X, pady=10)
        
        
        # tk.Button(top_btn_frame, text="عرض الكل", font=self.style.font, 
        #         command=self.show_fabrics).pack(side=tk.LEFT, padx=5)
        
        ctk.CTkButton(btnn_frame,text="عرض الكل"
                    ,font=self.btnstyle.btnfont,
                    hover_color=self.btnstyle.hover_color ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        # tk.Button(top_btn_frame, text="الانتقال إلى الموردين", font=self.style.font,
        #         command=self.open_suppliers).pack(side=tk.LEFT, padx=5)
        
        ctk.CTkButton(btnn_frame,text="الانتقال إلى الموردين"
                    ,font=self.btnstyle.btnfont,
                    hover_color="white" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        
        # tk.Button(top_btn_frame, text="العودة للصفحة الرئيسية", font=self.style.font,
        #         command=self.back_to_main).pack(side=tk.RIGHT, padx=5)
        
        ctk.CTkButton(btnn_frame,
                    text="العودة للصفحة الرئيسية"
                    ,font=self.btnstyle.btnfont,
                    hover_color="white" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        form_frame = tk.LabelFrame(main_frame, text="بيانات النسيج", font=self.style.title_font,
                                bg=self.style.bg_color, padx=10, pady=10)
        form_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(form_frame, text=": اسم النسيج", font=self.style.font, bg=self.style.bg_color).grid(row=0
                                                                                                    , column=2
                                                                                                    , sticky="e"
                                                                                                    , padx=5
                                                                                                    , pady=5)
        self.name_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.name_entry.grid(row=0,
                            column=0
                            , padx=5
                            , pady=5  )
        
        tk.Label(form_frame, text=": نوع النسيج", font=self.style.font, bg=self.style.bg_color).grid(row=1
                                                                                                    , column=2
                                                                                                    , sticky="e"
                                                                                                    , padx=5
                                                                                                    , pady=5)
        self.type_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.type_entry.grid(row=1
                            , column=0
                            , padx=5
                            , pady=5)
        
        tk.Label(form_frame, text=": السعر لكل متر", font=self.style.font, bg=self.style.bg_color).grid(row=2
                                                                                                    , column=2
                                                                                                    , sticky="e"
                                                                                                    , padx=5
                                                                                                    , pady=5)
        self.price_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.price_entry.grid(row=2
                            , column=0
                            , padx=5
                            , pady=5)
        
        tk.Label(form_frame, text=": الكمية المتاحة", font=self.style.font, bg=self.style.bg_color).grid(row=0
                                                                                                    , column=6
                                                                                                    , sticky="e"
                                                                                                    , padx=5,
                                                                                                    pady=5)
        self.quantity_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.quantity_entry.grid(row=0
                                , column=4
                                , padx=5
                                , pady=5)
        
        tk.Label(form_frame, text=": معرف المورد", font=self.style.font, bg=self.style.bg_color).grid(row=1
                                                                                                    , column=6
                                                                                                    , sticky="e"
                                                                                                    , padx=5
                                                                                                    , pady=5)
        self.supplier_entry = tk.Entry(form_frame, font=self.style.font, width=30)
        self.supplier_entry.grid(row=1
                                , column=4
                                , padx=5
                                , pady=5)
        
        btn_frame = tk.Frame(form_frame, bg=self.style.bg_color)
        btn_frame.grid(row=3, column=0, columnspan=4, pady=10)
        
        # tk.Button(btn_frame, text="إضافة", font=self.style.font, bg=self.style.secondary_color, fg="white",
        #         command=self.add_fabric).pack(side=tk.LEFT, padx=5)
        
        ctk.CTkButton(btn_frame,
                    text="إضافة"
                    ,font=self.btnstyle.btnfont,
                    hover_color="green" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        # tk.Button(btn_frame, text="تحديث", font=self.style.font, bg=self.style.secondary_color, fg="white",
        #         command=self.update_fabric).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(btn_frame,
                    text="تحديث"
                    ,font=self.btnstyle.btnfont,
                    hover_color="green" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        
        # tk.Button(btn_frame, text="حذف", font=self.style.font, bg="#d32f2f", fg="white",
        #         command=self.delete_fabric).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(btn_frame,
                    text="حذف"
                    ,font=self.btnstyle.btnfont,
                    hover_color="red" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
        # tk.Button(btn_frame, text="مسح الحقول", font=self.style.font, 
        #         command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(btn_frame,
                    text="مسح الحقول"
                    ,font=self.btnstyle.btnfont,
                    hover_color="red" ,
                    width=self.btnstyle.width,
                    height=self.btnstyle.height,
                    border_width=self.btnstyle.brod_bottom,
                    border_color=self.btnstyle.brod_color,
                    corner_radius=self.btnstyle.cor_rad,
                    fg_color=self.btnstyle.btn_color,
                    text_color="black",
                    command=self.clear_fields).pack(side=tk.RIGHT, padx=5 , pady =5)
        
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


# button = ctk.CTkButton(w, text="Click Me" , fg_color= "green", hover_color="red", text_color="white", corner_radius=5, width=100, height=50, border_width=1, border_color="black")
# button.place(relx=0.01, rely=0.1 )

# button1= ctk.CTkButton(w, text="Click Me" , fg_color= "green", hover_color="blue", text_color="white", corner_radius=5, width=100, height=50, border_width=1, border_color="black")
# button1.place(relx=0.01, rely=0.25 )


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
            cursor = conn.cursor()
            sql = """INSERT INTO workers 
                     (worker_name, job_title, phone_number, hire_date, salary) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (name, job, phone, hire_date, salary))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة العامل بنجاح")
            self.clear_fields()
            self.show_workers()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيمة صحيحة للراتب")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def show_workers(self):
        try:
            conn = connect_db()
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
            if conn.is_connected():
                cursor.close()
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
            messagebox.showerror("خطأ", "يرجى إدخال قيمة صحيحة للراتب")
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
            cursor = conn.cursor()
            sql = """INSERT INTO sales 
                     (fabric_id, sale_date, sold_quantity, total_price, worker_id) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (fabric_id, sale_date, quantity, price, worker_id))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة عملية البيع بنجاح")
            self.clear_fields()
            self.show_sales()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للأرقام")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def show_sales(self):
        try:
            conn = connect_db()
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
            if conn.is_connected():
                cursor.close()
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
                     fabric_id=%s, sale_date=%s, sold_quantity=%s, 
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
            cursor = conn.cursor()
            sql = """INSERT INTO inventory 
                     (fabric_id, receipt_date, received_quantity) 
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (fabric_id, receipt_date, quantity))
            conn.commit()
            messagebox.showinfo("نجاح", "تم إضافة المخزون بنجاح")
            self.clear_fields()
            self.show_inventory()
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة للأرقام")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإضافة: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def show_inventory(self):
        try:
            conn = connect_db()
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
            if conn.is_connected():
                cursor.close()
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
