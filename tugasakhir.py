import tkinter as tk
from tkinter import messagebox

class Camera:
    def __init__(self, name, specs, price):
        self.name = name
        self.specs = specs
        self.price = price

class RentalSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sewa Kamera.ku")
        
        # Set ukuran window untuk desktop
        self.root.geometry("1024x650")
        self.root.configure(bg="white")  # Warna latar putih
        
        # Data kamera
        self.cameras = [
            Camera("Canon EOS R5", "45MP, Full-frame, 8K Video", 100000),
            Camera("Sony A7 III", "24MP, Full-frame, 4K Video", 75000),
            Camera("Nikon Z6", "24MP, Full-frame, 4K Video", 70000),
            Camera("Fujifilm X-T4", "26MP, APS-C, 4K Video", 65000),
            Camera("Panasonic GH5", "20MP, Micro Four Thirds, 4K Video", 60000),
            Camera("Olympus OM-D E-M1", "20MP, Micro Four Thirds", 50000),
            Camera("Sony A6400", "24MP, APS-C, 4K Video", 55000),
            Camera("Canon EOS 90D", "32MP, APS-C, 4K Video", 70000),
            Camera("Nikon D7500", "20MP, APS-C, 4K Video", 50000),
            Camera("Canon EOS Rebel T7", "24MP, APS-C, Full HD Video", 40000),
            Camera("Canon EOS M50", "24MP, APS-C, 4K Video", 45000),
            Camera("Sony ZV-1", "20MP, 1-inch, 4K Video", 50000)
        ]
        
        # Menampilkan halaman awal
        self.show_start_page()

    def show_start_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        start_frame = tk.Frame(self.root, bg="white")
        start_frame.pack(expand=True)
        
        # Teks besar
        tk.Label(start_frame, text="Abadikan Momen Indahmu dengan SewaKamera.ku", font=("Arial", 24, "bold"), fg="teal", bg="white").pack(pady=20)
        
        # Tombol untuk masuk ke halaman utama
        tk.Button(
            start_frame, 
            text="Mulai Sewa", 
            command=self.home_page, 
            font=("Arial", 16, "bold"), 
            bg="lightseagreen", 
            fg="white", 
            padx=20, 
            pady=10
        ).pack(pady=15)

    def home_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(
            self.root, 
            text="Jenis Kamera", 
            font=("Arial", 18, "bold"), 
            fg="teal", 
            bg="white"
        ).pack(pady=(20, 10))
        
        camera_frame = tk.Frame(self.root, bg="white")
        camera_frame.pack(pady=10)
        
        for i, cam in enumerate(self.cameras[:12]): 
            frame = tk.Frame(
                camera_frame, 
                width=220, 
                height=160, 
                bd=1, 
                relief="solid", 
                padx=5, 
                pady=5, 
                bg="white"
            )
            frame.grid(row=i//4, column=i%4, padx=10, pady=10)
            frame.pack_propagate(False)
            
            tk.Label(
                frame, 
                text=f"{cam.name}", 
                font=("Arial", 10, "bold"), 
                wraplength=200, 
                bg="white"
            ).pack(pady=5)
            
            tk.Label(
                frame, 
                text=f"{cam.specs}", 
                font=("Arial", 8), 
                wraplength=200, 
                bg="white"
            ).pack(pady=5)
            
            # Menambahkan pemisah ribuan pada harga
            formatted_price = f"Rp {cam.price:,.0f}".replace(",", ".")
            tk.Label(
                frame, 
                text=f"Harga: {formatted_price}/hari", 
                font=("Arial", 8), 
                bg="white"
            ).pack(pady=5)
            
            tk.Button(
                frame, 
                text="Sewa", 
                command=lambda c=cam: self.booking_page(c),
                font=("Arial", 10, "bold"), 
                bg="lightseagreen", 
                fg="white"
            ).pack(pady=10)

    def booking_page(self, camera):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header untuk halaman booking
        tk.Label(
            self.root, 
            text=f"Sewa Kamera: {camera.name}", 
            font=("Arial", 16, "bold"), 
            fg="teal", 
            bg="white"
        ).pack(pady=(20, 20))
        
        # Form input
        tk.Label(self.root, text="Nama Lengkap", font=("Arial", 12), bg="white").pack(pady=5)
        name_entry = tk.Entry(self.root, font=("Arial", 12), width=50, bg="azure")
        name_entry.pack(pady=5)
        
        tk.Label(self.root, text="Nomor Telepon", font=("Arial", 12), bg="white").pack(pady=5)
        contact_entry = tk.Entry(self.root, font=("Arial", 12), width=50, bg="azure")
        contact_entry.pack(pady=5)
        
        tk.Label(self.root, text="Alamat", font=("Arial", 12), bg="white").pack(pady=5)
        address_entry = tk.Entry(self.root, font=("Arial", 12), width=50, bg="azure")
        address_entry.pack(pady=5)
        
        tk.Label(self.root, text="Tanggal Sewa (DD-MM-YYYY)", font=("Arial", 12), bg="white").pack(pady=5)
        rental_date_entry = tk.Entry(self.root, font=("Arial", 12), width=50, bg="azure")
        rental_date_entry.pack(pady=5)
        
        tk.Label(self.root, text="Durasi Sewa (dalam hari)", font=("Arial", 12), bg="white").pack(pady=5)
        duration_entry = tk.Entry(self.root, font=("Arial", 12), width=50, bg="azure")
        duration_entry.pack(pady=5)
        
        # Tombol Submit dan Kembali
        tk.Button(
            self.root, 
            text="Submit", 
            command=lambda: self.confirm_booking(
                camera, 
                name_entry.get(), 
                contact_entry.get(),  
                address_entry.get(), 
                rental_date_entry.get(), 
                duration_entry.get()
            ), 
            font=("Arial", 12, "bold"), 
            bg="lightseagreen", 
            fg="white", 
            width=20
        ).pack(pady=10)
        
        tk.Button(
            self.root, 
            text="Kembali", 
            command=self.home_page, 
            font=("Arial", 12, "bold"), 
            bg="gray", 
            fg="white", 
            width=20
        ).pack(pady=5)

    def confirm_booking(self, camera, name, contact, address, rental_date, duration):
        if not name or not contact or not address or not rental_date or not duration:
            messagebox.showerror("Error", "Semua data harus diisi.")
            return
        
        try:
            duration = int(duration)
            if duration <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Durasi harus berupa angka positif.")
            return
        
        total_price = duration * camera.price
        confirmation_message = (
            f"Apakah data sudah benar?\n\n"
            f"Kamera: {camera.name}\n"
            f"Nama Lengkap: {name}\n"
            f"Nomor Telepon: {contact}\n"
            f"Alamat: {address}\n"
            f"Tanggal Sewa: {rental_date}\n"
            f"Durasi Sewa: {duration} hari\n"
            f"Harga Total: Rp {total_price:,.0f}".replace(",", ".") + "\n"
        )
        response = messagebox.askyesno("Konfirmasi Penyewaan", confirmation_message)
        
        if response:  # Jika pengguna memilih "Ya"
            self.payment_page(camera, name, contact, address, rental_date, duration, total_price)
        else:  # Jika pengguna memilih "Tidak"
            self.booking_page(camera)

    def payment_page(self, camera, name, contact, address, rental_date, duration, total_price):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Header untuk halaman pembayaran
        tk.Label(
            self.root, 
            text="Pembayaran", 
            font=("Arial", 16, "bold"), 
            fg="teal", 
            bg="white"
        ).pack(pady=(20, 20))
        
        tk.Label(
            self.root, 
            text=f"Harga Total: Rp {total_price:,.0f}".replace(",", "."),
            font=("Arial", 14), 
            fg="red", 
            bg="white"
        ).pack(pady=10)

        # Pilihan metode pembayaran
        transfer_bank_var = tk.BooleanVar()
        e_wallet_var = tk.BooleanVar()
        cod_var = tk.BooleanVar()

        tk.Checkbutton(
            self.root, 
            text="Transfer Bank", 
            variable=transfer_bank_var, 
            font=("Arial", 12), 
            bg="white"
        ).pack(pady=5)

        tk.Checkbutton(
            self.root, 
            text="E-Wallet", 
            variable=e_wallet_var, 
            font=("Arial", 12), 
            bg="white"
        ).pack(pady=5)

        tk.Checkbutton(
            self.root, 
            text="Cash on Delivery", 
            variable=cod_var, 
            font=("Arial", 12), 
            bg="white"
        ).pack(pady=5)
        
        tk.Button(
            self.root, 
            text="Bayar", 
            command=lambda: self.payment_success(
                camera, 
                name, 
                contact, 
                address, 
                rental_date, 
                duration, 
                total_price, 
                transfer_bank_var.get(), 
                e_wallet_var.get(), 
                cod_var.get()
            ), 
            font=("Arial", 12, "bold"), 
            bg="lightseagreen", 
            fg="white", 
            width=20
        ).pack(pady=20)

    def payment_success(self, camera, name, contact, address, rental_date, duration, total_price, transfer_bank, e_wallet, cod):
        payment_method = None
        if transfer_bank: 
            payment_method = "Transfer Bank"
        elif e_wallet:
            payment_method = "E-Wallet"
        elif cod:
            payment_method = "Cash on Delivery"
        
        if not payment_method:
            messagebox.showerror("Error", "Silakan pilih metode pembayaran.")
            return
        
        # Pop-up pembayaran berhasil
        messagebox.showinfo(
            "Pembayaran Berhasil", 
            "Pembayaran berhasil dilakukan! Klik OK untuk mendapatkan bukti sewa."
        )
        
        # Tampilkan bukti sewa
        self.rental_receipt(camera, name, contact, address, rental_date, duration, total_price, payment_method)
        
    def rental_receipt(self, camera, name, contact, address, rental_date, duration, total_price, payment_method):
        # Pop-up bukti sewa
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Bukti Sewa")
        receipt_window.geometry("440x340")
        receipt_window.configure(bg="white")

        # Perintah screenshoot
        tk.Label(
            receipt_window, 
            text="Screenshoot halaman ini sebagai bukti sewa!", 
            font=("Arial", 12, "bold"), 
            fg="red", 
            bg="white", 
            anchor="w", 
            justify="left"
        ).pack(pady=(20, 5), padx=20, fill="x")

        # Rincian sewa
        receipt_text = f"Nama Lengkap: {name}\n" \
                       f"Nomor Telepon: {contact}\n" \
                       f"Alamat: {address}\n" \
                       f"Kamera: {camera.name}\n" \
                       f"Tanggal Sewa: {rental_date}\n" \
                       f"Durasi: {duration} hari\n" \
                       f"Harga Total: Rp {total_price:,.0f}".replace(",", ".") + "\n"\
                       f"Metode Pembayaran: {payment_method}"
        tk.Label(
            receipt_window, 
            text=receipt_text, 
            font=("Arial", 10), 
            bg="white", 
            anchor="w", 
            justify="left"
        ).pack(pady=(10, 20), padx=20, fill="x")

        # Pesan terima kasih
        tk.Label(
            receipt_window, 
            text="Terima kasih telah menggunakan layanan kami.", 
            font=("Arial", 10), 
            fg="black", 
            bg="white", 
            anchor="w", 
            justify="left"
        ).pack(pady=(0, 20), padx=20, fill="x")

        # Tombol tutup
        tk.Button(
            receipt_window, 
            text="Tutup", 
            command=lambda: (receipt_window.destroy(), self.show_start_page()), 
            font=("Arial", 12, "bold"), 
            bg="gray", 
            fg="white"
        ).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalSystem(root)
    root.mainloop()
