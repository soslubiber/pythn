import customkinter as ctk
from tkinter import messagebox
import requests

#API ile hava durumu bilgisini çekme fonksiyonu
def hava_durumu_getir():
    api_key ="4c0e15bdbd374c2acc710c33f8a27a85"
    sehir_giriş.get()
    if sehir:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&lang=tr&units=metric"
        try:
            yanit = requests.get(url)
            veri = yanit.json()

            if veri.get("cod") == 200:
                ana = veri.get("main", {})
                sicaklik = ana.get("temp", "bilgi yok")
                basinc = ana.get("pressure", "bilgi yok")
                nem = ana.get("humidity", "bilgi yok")
                hava = veri.get("weather", [{}])[0]
                hava_durumu = hava.get("description", "bilgi yok")
                genel_durum = hava.get("main", "bilgi yok")

                sonuc = (f"Şehir: {sehir}\n"
                          f"Sıcaklık: {sicaklik}°C\n"
                          f"Basınç: {basinc} hpa\n"
                          f"Nem: {nem}%\n"
                          f"Hava Durumu: {genel_durum} - {hava_durumu}")
                
                sonuc_etiketi.configure(text=sonuc)
            else:
                #Hata mesajını göster
                hata_mesaji = veri.get("message", "Error 404")
                messagebox.showerror("Hata", f"Şehir bulunamadı: {hata_mesaji}")
        except Exception as e:
            messagebox.showerror("Hata", f"Veri alınırken bir hata oluştu: {stri(e)}")
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

pencere = ctk.CTk()
pencere.title("Hava Durumu Uygylaması")
pencere.geometry("400x400")

sehir_giris = ctk.CTkEntry(pencere, width=200)
sehir_giriş.pack(pady_10)

getir_butonu = ctk.CTkButton(pencere, text="Hava Durumu Getir",
command=hava_durumu_getir)
getir_butonu.pack(pady=5)

sonuc_etiketi = ctk.CTkLabel(pencer, text="", font=("Arial", 12),
justify="left")
sonuc_etiketi.pack(pady=10)

pencere.mainloop()

