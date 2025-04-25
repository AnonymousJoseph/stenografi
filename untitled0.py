from PIL import Image
import stepic
import argparse

# Metin gömme fonksiyonu
def encode_image(image_path, text, output_path):
    # Görseli aç
    img = Image.open(image_path)
    
    # Metni görsele göm
    encoded_img = stepic.encode(img, text.encode())
    
    # Yeni görseli kaydet
    encoded_img.save(output_path)
    print(f"Metin başarıyla gömüldü ve {output_path} olarak kaydedildi.")

# Metni görselden çıkarma fonksiyonu
def decode_image(image_path):
    # Görseli aç
    img = Image.open(image_path)
    
    # Gömülü metni çıkar
    decoded_text = stepic.decode(img)
    
    if decoded_text:
        print("Gömülü metin: ", decoded_text)
    else:
        print("Görselde gömülü bir metin bulunamadı.")

# Komut satırı arayüzü (CLI) için ana fonksiyon
def main():
    parser = argparse.ArgumentParser(description="Stenografi: Görsele metin gömme ve çıkarma")
    parser.add_argument('action', choices=['encode', 'decode'], help="Yapılacak işlem (encode veya decode)")
    parser.add_argument('image_path', help="Görsel dosyasının yolu")
    parser.add_argument('--text', help="Gömülecek metin (encode işlemi için)")
    parser.add_argument('--output', help="Çıktı görsel dosyasının adı (encode işlemi için)")
    
    # Kullanıcıdan parametreleri al
    args = parser.parse_args()
    
    # Encode işlemi
    if args.action == 'encode':
        if not args.text or not args.output:
            print("Metin ve çıktı dosya adı zorunludur.")
            return
        encode_image(args.image_path, args.text, args.output)
    
    # Decode işlemi
    elif args.action == 'decode':
        decode_image(args.image_path)

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    main()




