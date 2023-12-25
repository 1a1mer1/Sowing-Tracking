from datetime import datetime
from dateutil.relativedelta import relativedelta

# Çim türleri ve tekrar ekim zamanları (bir sonraki yılın aynı tarihi olarak ayarlandı)
grass_types = {
    "ryegrass": relativedelta(years=1),
    "reygrass": relativedelta(years=1),
    "reygras": relativedelta(years=1),
    "ryegras": relativedelta(years=1),
    "bahia": relativedelta(years=3),
    "bahian": relativedelta(years=3),
    "brome": relativedelta(years=2),
    "yonca": relativedelta(years=4),
    "alfalfa": relativedelta(years=3),
    "maralfalfa": relativedelta(years=3),
    "darı otu": relativedelta(years=1),
    "fescue": relativedelta(years=5),
    "teffgrass": relativedelta(years=1),
    "teffgras": relativedelta(years=1),
    "teff": relativedelta(years=1)
}

# Çim türleri için ekstra bilgiler
grass_info = {
    "ryegrass": "Ryegrass, hızlı büyüyen ve dayanıklı bir çim türüdür.",
    "reygrass": "Reygrass, hızlı büyüyen ve dayanıklı bir çim türüdür.",
    "reygras": "Reygrass, hızlı büyüyen ve dayanıklı bir çim türüdür.",
    "ryegras": "Ryegrass, hızlı büyüyen ve dayanıklı bir çim türüdür.",
    "bahia": "Bahia otu, sıcak mevsimler için uygun ve kışın uykuya geçer.",
    "bahian": "Bahia otu, sıcak mevsimler için uygun ve kışın uykuya geçer.",
    "brome": "Brome, hoş bir görünüme sahip dayanıklı bir çim türüdür.",
    "yonca": "Yonca, yaygın olarak kullanılan ve uzun ömürlü bir çim türüdür.",
    "alfalfa": "Alfalfa, yüksek besin değeri olan dayanıklı bir çim türüdür.",
    "maralfalfa": "Maralfalfa, yüksek besin değeri olan dayanıklı bir çim türüdür.",
    "darı otu": "Darı otu, hızlı büyüyen ve yaygın olarak kullanılan bir çim türüdür.",
    "fescue": "Fescue, uzun ömürlü ve dayanıklı bir çim türüdür.",
    "teffgrass": "Teffgrass, hızlı büyüyen ve dayanıklı bir çim türüdür.",
    "teffgras": "Teffgrass, hızlı büyüyen ve dayanıklı bir çim türüdür.",
    "teff": "Teff, hızlı büyüyen ve dayanıklı bir çim türüdür."
}

def get_user_input():
    print("(Çıkış yapmak için 'exit' yazın.)")
    grass_type = input("Ekilen çim türünü girin: ")

    if grass_type.lower() == "exit":
        print("Çıkış yapılıyor...")
        return None, None

    # Girilen çim türünü küçük harfe çeviriyoruz
    grass_type = grass_type.lower()

    while grass_type not in grass_types:
        if grass_type.lower() == "exit":
            print("Çıkış yapılıyor...")
            return None, None

        print("Geçersiz çim türü! Lütfen doğru çim türünü girin.")
        grass_type = input("Ekilen çim türünü girin: ")
        # Girilen çim türünü küçük harfe çeviriyoruz
        grass_type = grass_type.lower()

    planting_date_str = input("Ekim yapılan tarihi (gün/ay/yıl) girin: ")
    if planting_date_str.lower() == "exit":
        print("Çıkış yapılıyor...")
        return None, None

    planting_date = datetime.strptime(planting_date_str, "%d/%m/%Y")

    return grass_type, planting_date

def calculate_replanting_date(grass_type, planting_date):
    replanting_interval = grass_types[grass_type]
    # Tekrar ekim tarihi olarak bir sonraki yılın aynı tarihi ekleniyor
    replanting_date = planting_date + replanting_interval
    return replanting_date

def main():
    while True:
        grass_type, planting_date = get_user_input()

        if grass_type is None:
            break

        replanting_date = calculate_replanting_date(grass_type, planting_date)

        current_date = datetime.now()
        days_since_planting = (current_date - planting_date).days

        print(f"{grass_type.capitalize()} için tekrar ekim tarihi (gün/ay/yıl): {replanting_date.day}/{replanting_date.month}/{replanting_date.year}")
        print(f"Ekim yapılan tarihten geçen süre: {days_since_planting} gün")

        if grass_type in grass_info:
            print("Ek bilgi:", grass_info[grass_type])
        print()

if __name__ == "__main__":
    main()