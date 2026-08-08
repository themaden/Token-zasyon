from tokenizers import Tokenizer, models, trainers, pre_tokenizers
import os

# 1. BPE modelini başlatıyoruz
tokenizer = Tokenizer(models.BPE(unk_token="[UNK]"))

# 2. Türkçe karakterleri doğru işlemek için ByteLevel ön-işleyicisi ekliyoruz
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)

# 3. Eğitici ayarları
trainer = trainers.BpeTrainer(
    vocab_size=2000,  # Finans sözlüğümüzün büyüklüğü
    min_frequency=2,   # En az 2 kere geçen parçaları al
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
)

# 4. Eğitimi çalıştırıyoruz
print("Tokenizer eğitiliyor...")
# Otomatik veri dosyası algılama (bazı sistemlerde dosya adı sonuna .txt eklenmiş olabilir)
if os.path.exists("finans_verisi.txt"):
    files = ["finans_verisi.txt"]
elif os.path.exists("finans_verisi.txt.txt"):
    files = ["finans_verisi.txt.txt"]
else:
    raise FileNotFoundError(
        "Veri dosyası bulunamadı: beklenen finans_verisi.txt veya finans_verisi.txt.txt"
    )

tokenizer.train(files, trainer)

# 5. Modeli kaydediyoruz
tokenizer.save("finans_bpe_tokenizer.json")
print("✅ Harika! Tokenizer eğitildi ve 'finans_bpe_tokenizer.json' olarak kaydedildi.")