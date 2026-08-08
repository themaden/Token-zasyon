from tokenizers import Tokenizer

# Eğittiğimiz tokenizer'ı yüklüyoruz
tokenizer = Tokenizer.from_file("finans_bpe_tokenizer.json")

# Finans alanına özgü bir test cümlesi
cumle = "Borsa İstanbul şirketlerinin bilanço ve portföy durumları incelendi."

# Cümleyi parçalara ayıralım (encode)
output = tokenizer.encode(cumle)

print("\n--- TEST SONUÇLARI ---")
print("Orijinal Cümle:", cumle)
print("Tokenlar (Parçalar):", output.tokens)
print("Token ID'leri:", output.ids)