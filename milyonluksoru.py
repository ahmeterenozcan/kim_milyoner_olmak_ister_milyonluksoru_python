
sehirler=["adana", "adıyaman", "afyonkarahisar", "ağrı", "amasya", "ankara", "antalya", "artvin", "aydın",
          "balıkesir", "bilecik", "bingöl", "bitlis", "bolu", "burdur", "bursa", "çanakkale", "çankırı", "çorum",
          "denizli", "diyarbakır", "edirne", "elazığ", "erzincan", "erzurum", "eskişehir", "gaziantep", "giresun", "gümüşhane",
          "hakkari", "hatay", "ısparta", "mersin", "istanbul", "izmir", "kars", "kastamonu", "kayseri", "kırklareli", "kırşehir",
          "kocaeli", "konya", "kütahya", "malatya", "manisa", "kahramanmaraş", "mardin", "muğla", "muş", "nevşehir", "niğde", "ordu",
          "rize", "sakarya", "samsun", "siirt", "sinop", "sivas", "tekirdağ", "tokat", "trabzon", "tunceli", "şanlıurfa", "uşak", "van",
          "yozgat", "zonguldak", "aksaray", "bayburt", "karaman", "kırıkkale", "batman", "şırnak", "bartın", "ardahan", "ığdır", "yalova",
          "karabük", "kilis", "osmaniye", "düzce"]

s_harfi=0
v_harfi=0
g_harfi=0
h_harfi=0
counter=0
for k in sehirler:
    counters=0
    counterv=0
    counterh=0
    counterg=0
    for i in k:
        if(i=="ş"):
            if(counters==0):
                s_harfi+=1
                counters+=1
        elif(i=="v"):
            if(counterv==0):
                v_harfi+=1
                counterv+=1
        elif(i=="g"):
            if(counterg==0):
                g_harfi+=1
                counterg+=1
        elif(i=="h"):
            if(counterh==0):
                h_harfi+=1
                counterh+=1

print(s_harfi,v_harfi,g_harfi,h_harfi)

